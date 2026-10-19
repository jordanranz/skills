---
name: project-validation
description: Plan and run implementation-grounded validation, investigate failures, and assess coverage. Also use when explicitly asked to improve lint, compiler, test, build, or CI safeguards.
---

# Project validation

Own evidence about behavior and the effectiveness of checks. Accept the intended contract from requirements or the implementation task; do not silently redefine it. This skill has no required companion and can validate independently of feature-workflow.

Read project-local check documentation such as docs/project-checks.md when present. Verify commands and coverage against current code and configuration. If documentation is absent, discover existing checks directly. Do not assume tools exist or create documentation unless that work is in scope. Keep project facts outside this reusable skill.

Choose the mode from the request: validate a change with existing tools, or improve safeguards when that implementation work is authorized. Reading this skill from a maintainer does not expand the maintainer's edit scope. Neither mode grants permission to change product behavior, publish, alter sharing, or incur upgrades.

## Validate a change

1. Read project instructions and the actual diff. Identify acceptance criteria, the most important invariant, affected functions, state and write paths, and the highest-impact plausible failure. Clarify consequential ambiguity before judging correctness.
2. Inspect actual usage: startup, configuration, input, mutation, and output. Use safe deterministic fixtures or an isolated copy where needed. Select checks by the risks they cover. Distinguish static analysis, runtime checks, and user-flow evidence.
3. Run relevant existing checks. Exercise the happy path and highest-impact failure case against real functions, routes, CLI invocations, or browser interactions. Check validation, resulting state, and user-visible errors where relevant. Do not replace the implementation with duplicated logic in a test model. Manual reproduction is acceptable when proportionate and repeatable. For instructions-only changes, review contracts, metadata, references, and representative task walkthroughs; do not invent an app failure case or run unrelated app checks.
4. Record each important check's criterion, covered code, exact command or steps, expected behavior, actual result, and assumptions. For performance questions, establish comparable baselines with deterministic input sizes. Record relevant timing, payload size, or responsiveness and measurement limits.
5. For critical invariants, when practical, save a reversible baseline and introduce a representative bug in an isolated copy or test setup. Confirm the intended check fails for the expected reason. Restore only that change and rerun to confirm the original result. Never use live data or publish the broken variant. Report omitted demonstrations and their effect on confidence. A setup failure does not establish target-bug detection.
6. Reassess coverage whenever implementation changes, including new mutation paths, ordering, inputs, moved code, and changed contracts. Update checks from actual code and intended behavior, then rerun affected checks. An old pass is not evidence for new behavior.
7. Investigate failures as possible product bugs, stale checks, setup problems, or mistaken assumptions. Reproduce and identify the cause. Return product findings to implementation; fix them only within the authorized task. Correct inaccurate checks with evidence. Do not weaken assertions, skip checks, reduce coverage, or redefine the contract merely to pass. Change expectations only with evidence of an intentional contract change and explain why.

## Improve safeguards when requested

Choose enforcement from an observed correction, costly plausible bug, or coverage gap:

- Invalid state or competing writes: recommend stronger state ownership, types, or data constraints. Product changes belong to implementation work.
- Mechanically detectable code mistakes: compiler or lint rules.
- Behavioral regressions: focused tests against real implementation.
- Dependency violations: module boundaries or a focused architecture check.
- Judgment and workflow conventions: skill instructions.

Explain what bug a proposed safeguard catches, its maintenance cost, and where it runs. Prefer existing tools and the smallest useful addition. Routine validation does not install tooling. When CI work is authorized, share project commands locally and in CI, use reproducible dependencies, and ensure relevant failures fail the job. Demonstrate important new checks can detect representative violations, restore, and rerun. Review configuration changes and update local check documentation when commands or coverage change.

## Report evidence

Distinguish passed, failed, not run, and not covered. Include commands or steps, results, coverage, assumptions, limitations, and next actions. Separate product bugs, verification drift, and environment failures. Static analysis catches specific defect classes; it does not establish correct user behavior. Ordinary tests are not formal verification. For a formal check, state its property, relationship to code, bounds, and assumptions; use a dedicated verification skill when available.

The optional maintain-project-validation skill reconciles stale validation instructions and local check documentation. Its absence does not block validation. Ordinary validation does not require a maintenance pass.
