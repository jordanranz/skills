---
name: maintain-feature-workflow
description: Reconcile feature-workflow instructions with changed architecture, conventions, product constraints, or repeated corrections. Use for requested instruction upkeep or confirmed workflow drift, not routine feature implementation.
metadata:
  requires-skills: feature-workflow, project-validation
---

# Maintain feature workflow

Requires [feature-workflow](../feature-workflow/SKILL.md) and [project-validation](../project-validation/SKILL.md) as sibling directories. Install the feature-development bundle, or install these companions together. If either is missing, report it and pause dependent maintenance.

Edit only feature-workflow and its project-local implementation context, such as docs/project-context.md. Read project-validation only to check the ownership boundary. Do not edit validation instructions, check documentation, product code, tests, tooling, or CI. Report findings in those areas to their owner. Do not invoke other maintainers recursively.

## Inspect and reconcile

1. Read project instructions, the parent skills, and the actual working diff. Identify the requested correction or suspected drift. Use a recorded baseline if available; otherwise inspect relevant history. For untracked instructions or missing history, inspect current supporting code and report the historical limit. Include uncommitted changes.
2. Compare implementation guidance with actual entry points, state owners, dependencies, conventions, and product constraints. Follow moved or renamed code. Distinguish an intentional contract change supported by requirements from implementation that violates an unchanged promise.
3. Make the smallest evidence-backed instruction correction. Remove obsolete facts and duplication. Do not generalize a one-off exception. Keep reusable guidance in the skill and project facts local. Preserve the parent's implementation commitments and validation handoff; check the companion's owned obligations without copying them here. Never relax an invariant merely because code violates it.
4. Review the diff, metadata, and references. Walk a representative feature request through contract definition, scoped implementation, and validation handoff. Do not implement the example. A document walkthrough is not runtime evidence. Wording-only edits require no app checks.

## Report

For each finding, report current, updated, product finding, or unresolved, with supporting evidence and reasons. These instruction outcomes are separate from check execution results. State what was reviewed, what changed, and remaining uncertainty. A concise date and inspected revision plus dirty paths in the report is sufficient; use an existing baseline record when one exists rather than inventing tracking infrastructure. Do not mark unreviewed context current or claim checks ran when they did not. Product fixes and validation upkeep remain separate tasks.
