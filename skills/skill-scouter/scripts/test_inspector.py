#!/usr/bin/env python3
"""Deterministic regression tests for the Skill Scouter inspector."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from inspect_skill import inspect


def write_skill(root: Path, name: str, description: str, body: str) -> Path:
    skill = root / name
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        f'---\nname: {name}\ndescription: "{description}"\n---\n\n{body}\n',
        encoding="utf-8",
    )
    return skill


def inspect_path(path: Path, repo_root: Path | None = None, *roots: Path) -> dict:
    return inspect(
        argparse.Namespace(
            target=str(path),
            repo_root=str(repo_root) if repo_root else None,
            skills_root=[str(root) for root in roots],
            compact=True,
        )
    )


class InspectorTests(unittest.TestCase):
    def test_quoted_description_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = write_skill(Path(tmp), "quoted", 'Use when someone says "scan it" today', "Do the scan.")
            self.assertEqual(inspect_path(skill)["skill"]["description"], 'Use when someone says "scan it" today')

    def test_delegating_alias_includes_required_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = write_skill(root, "target", "Target skill", "Perform the real workflow carefully.")
            alias = write_skill(root, "alias", "Alias skill", 'Use the Skill tool with skill "target".')
            result = inspect_path(alias, None, root)
            target_result = inspect_path(target)
            self.assertEqual([item["name"] for item in result["dependencies"]], ["target"])
            self.assertEqual(
                result["footprint"]["effective_body_tokens_before_references"],
                result["footprint"]["body_tokens"] + target_result["footprint"]["body_tokens"],
            )

    def test_dynamic_runtime_counts_only_first_skill_as_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "skill-data"
            first = write_skill(data, "first", "First skill", "First workflow.")
            write_skill(data, "second", "Second skill", "Second workflow with extra text.")
            router = write_skill(root, "router", "Runtime router", "At runtime skills get first, then skills get second when requested.")
            result = inspect_path(router, root)
            first_result = inspect_path(first)
            self.assertEqual([item["required_by_default"] for item in result["dynamic_dependencies"]], [True, False])
            self.assertEqual(
                result["footprint"]["effective_body_tokens_before_references"],
                result["footprint"]["body_tokens"] + first_result["footprint"]["body_tokens"],
            )

    def test_broken_local_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = write_skill(Path(tmp), "broken", "Broken reference", "Read [the guide](references/missing.md).")
            broken = inspect_path(skill)["integrity"]["broken_local_links"]
            self.assertEqual([item["target"] for item in broken], ["references/missing.md"])

    def test_estimate_mode_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = write_skill(Path(tmp), "estimate", "Estimate tokens", "12345678")
            env = os.environ.copy()
            env["SKILL_SCOUTER_TOKENIZER"] = "estimate"
            completed = subprocess.run(
                ["python3", str(Path(__file__).with_name("inspect_skill.py")), str(skill), "--compact"],
                check=True,
                capture_output=True,
                text=True,
                env=env,
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["footprint"]["token_method"], "estimated_chars_div_4")


if __name__ == "__main__":
    unittest.main()
