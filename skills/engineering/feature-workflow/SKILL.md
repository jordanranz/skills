---
name: feature-workflow
description: Implement features and bug fixes in an existing project with explicit acceptance criteria, clear state ownership, and small complete flows.
metadata:
  requires-skills: project-validation
---

# Feature workflow

Own intended behavior and implementation. The required companion [project-validation](../project-validation/SKILL.md) owns checks and evidence. Install both as sibling skill directories, or use the feature-development bundle. If the companion is missing, report the dependency and pause dependent work; do not silently omit validation. Read companions in the same task; these references do not require spawning agents.

Prioritize correctness, then measured performance, code structure, and tradeoffs. Scale effort to scope, complexity, and risk. Do not implement unrelated improvements.

## Inspect and define the contract

- Read project instructions, manifests, relevant code, and existing checks. Inspect the working diff and preserve pre-existing changes. Follow the current stack and conventions rather than assuming a language or framework.
- Read project-local context such as docs/project-context.md when present. Confirm relevant facts against code. If absent, inspect the project directly; do not invent constraints or create documentation unless that work is in scope.
- Restate acceptance criteria as observable behavior. Clarify ambiguities that affect correctness; state assumptions for minor details. Name the most important invariant, its owner, and the user harm if it breaks.
- Trace input, validation, mutation, and output. Identify dependency boundaries and system invariants. Explain and resolve conflicts before implementing behavior that violates them.

## Build one complete flow

- Implement the smallest usable end-to-end flow before optional cases or polish. Keep feature-specific logic together. Extract abstractions only for demonstrated reuse or boundaries that make correctness easier to enforce.
- Give persisted state one authoritative owner and one clear mutation path. Route writes through it; derive views instead of maintaining competing copies. Make validation and allowed transitions explicit. Do not add persistence when unnecessary.
- Follow existing dependency interfaces. Design important boundaries so existing modules, types, or constraints can enforce them. Use project-validation to evaluate additional safeguards instead of introducing a framework by default.
- Explain each changed block and non-obvious line. Simplify or walk through code the developer cannot explain before expanding the change.
- Measure a likely bottleneck before optimizing. Use project-validation for reproducible measurements; add complexity only when requirements or evidence justify it.

## Obtain evidence and review

Before implementation, use project-validation to plan evidence from acceptance criteria, intended invariants, relevant paths, and failure risks. After implementation, evaluate the actual diff and any changed assumptions or contracts. Fix product bugs within the authorized scope and rerun affected checks. Resolve disputed behavior against requirements; validation must not redefine the contract to pass.

Review the complete diff for scope, accidental edits, boundary violations, duplicate state ownership, and unexplained code. Report delivered behavior, validation results, assumptions, tradeoffs, and remaining limitations. Distinguish observation from inference. Do not declare completion without reporting evidence and gaps.

## Instruction upkeep

The optional maintainer, maintain-feature-workflow, updates these instructions when upkeep is requested or confirmed drift affects future work. Its absence does not block feature work. Routine implementation does not require a maintenance pass. Keep project-specific facts local; do not bake them into this reusable skill. Skill references do not expand authorization to publish, change sharing, or incur upgrades.
