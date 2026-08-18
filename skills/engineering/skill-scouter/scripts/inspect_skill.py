#!/usr/bin/env python3
"""Collect deterministic structural facts from an Agent Skill package."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
from pathlib import Path
from typing import Any

TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".txt"}
LINK_RE = re.compile(r"\[[^]]*\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
SKILL_CALL_RE = re.compile(r"(?:Skill tool|skill)\b[^\n]*", re.I)
QUOTED_NAME_RE = re.compile(r'["\']([a-z0-9]+(?:-[a-z0-9]+)*)["\']')
DYNAMIC_SKILL_RE = re.compile(r"\bskills\s+get\s+([a-z0-9]+(?:-[a-z0-9]+)*)")


def token_counter():
    if os.environ.get("SKILL_SCOUTER_TOKENIZER", "auto").lower() == "estimate":
        return lambda value: math.ceil(len(value) / 4), "estimated_chars_div_4"
    try:
        import tiktoken  # type: ignore

        encoding = tiktoken.get_encoding("o200k_base")
        return lambda value: len(encoding.encode(value)), "o200k_base"
    except Exception:
        return lambda value: math.ceil(len(value) / 4), "estimated_chars_div_4"


COUNT_TOKENS, TOKEN_METHOD = token_counter()


def split_skill(text: str) -> tuple[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("SKILL.md must contain YAML frontmatter delimited by ---")
    return match.group(1), match.group(2)


def scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", frontmatter)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        value = value[1:-1]
    return value


def find_repo_root(skill_dir: Path) -> Path:
    for candidate in (skill_dir, *skill_dir.parents):
        if (candidate / ".git").exists():
            return candidate
    return skill_dir


def resolve_named_skill(name: str, roots: list[Path]) -> Path | None:
    candidates: set[Path] = set()
    for root in roots:
        direct = root / name / "SKILL.md"
        if direct.exists():
            candidates.add(direct.parent.resolve())
        candidates.update(path.parent.resolve() for path in root.rglob("SKILL.md") if path.parent.name == name)
    return next(iter(candidates)) if len(candidates) == 1 else None


def skill_body_tokens(skill_dir: Path) -> int:
    text = (skill_dir / "SKILL.md").read_text(errors="ignore")
    return COUNT_TOKENS(split_skill(text)[1])


def inspect(args: argparse.Namespace) -> dict[str, Any]:
    target = Path(args.target).resolve()
    skill_dir = target.parent if target.is_file() else target
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        raise FileNotFoundError(f"No SKILL.md found in {skill_dir}")

    repo_root = Path(args.repo_root).resolve() if args.repo_root else find_repo_root(skill_dir)
    roots = [Path(root).resolve() for root in args.skills_root]
    text = skill_file.read_text(errors="ignore")
    frontmatter, body = split_skill(text)
    files = [path for path in skill_dir.rglob("*") if path.is_file()]
    text_files = [path for path in files if path.suffix.lower() in TEXT_SUFFIXES]
    support_files = [path for path in files if path.name not in {"SKILL.md", "openai.yaml"} and "agents" not in path.parts]

    broken: list[dict[str, str]] = []
    local_links = 0
    for markdown in (path for path in text_files if path.suffix.lower() == ".md"):
        for link in LINK_RE.findall(markdown.read_text(errors="ignore")):
            target_text = link.split("#", 1)[0]
            if not target_text or re.match(r"^[a-z]+://", target_text):
                continue
            local_links += 1
            if not (markdown.parent / target_text).resolve().exists():
                broken.append({"file": str(markdown.relative_to(skill_dir)), "target": link})

    dependency_names: set[str] = set()
    for line in SKILL_CALL_RE.findall(body):
        dependency_names.update(QUOTED_NAME_RE.findall(line))

    dependencies = []
    dependency_body_tokens = 0
    for name in sorted(dependency_names):
        resolved = resolve_named_skill(name, roots)
        tokens = skill_body_tokens(resolved) if resolved else None
        dependency_body_tokens += tokens or 0
        dependencies.append({"name": name, "resolved": bool(resolved), "path": str(resolved) if resolved else None, "body_tokens": tokens})

    dynamic_dependencies = []
    dynamic_body_tokens = 0
    dynamic_names = list(dict.fromkeys(DYNAMIC_SKILL_RE.findall(body)))
    for index, name in enumerate(dynamic_names):
        candidate = repo_root / "skill-data" / name
        resolved = candidate if (candidate / "SKILL.md").exists() else None
        tokens = skill_body_tokens(resolved) if resolved else None
        required = index == 0
        if required:
            dynamic_body_tokens += tokens or 0
        dynamic_dependencies.append({"name": name, "required_by_default": required, "resolved": bool(resolved), "path": str(resolved) if resolved else None, "body_tokens": tokens})

    support_text = [path for path in support_files if path in text_files]
    support_counts = [COUNT_TOKENS(path.read_text(errors="ignore")) for path in support_text]
    body_tokens = COUNT_TOKENS(body)

    return {
        "skill": {"name": scalar(frontmatter, "name"), "description": scalar(frontmatter, "description"), "license": scalar(frontmatter, "license"), "path": str(skill_dir), "repo_root": str(repo_root)},
        "footprint": {
            "token_method": TOKEN_METHOD,
            "metadata_tokens": COUNT_TOKENS(frontmatter),
            "body_tokens": body_tokens,
            "skill_tokens": COUNT_TOKENS(text),
            "effective_body_tokens_before_references": body_tokens + dependency_body_tokens + dynamic_body_tokens,
            "text_package_tokens": sum(COUNT_TOKENS(path.read_text(errors="ignore")) for path in text_files),
            "support_text_tokens": sum(support_counts),
            "average_support_text_tokens": round(sum(support_counts) / len(support_counts)) if support_counts else 0,
            "files": len(files),
            "support_files": len(support_files),
            "scripts": sum(1 for path in files if "scripts" in path.parts),
            "assets": sum(1 for path in files if "assets" in path.parts),
        },
        "integrity": {"local_links": local_links, "broken_local_links": broken},
        "dependencies": dependencies,
        "dynamic_dependencies": dynamic_dependencies,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Skill directory or SKILL.md")
    parser.add_argument("--repo-root", help="Repository root for runtime skill resolution")
    parser.add_argument("--skills-root", action="append", default=[], help="Root to search for delegated skills; repeatable")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()
    print(json.dumps(inspect(args), indent=None if args.compact else 2, sort_keys=True))


if __name__ == "__main__":
    main()
