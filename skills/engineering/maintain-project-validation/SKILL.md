---
name: maintain-project-validation
description: Reconcile project-validation instructions and project-local check documentation with changed code, commands, runtime, or CI. Use for requested upkeep or confirmed validation drift, not routine validation or tooling installation.
metadata:
  requires-skills: project-validation
---

# Maintain project validation

Requires [project-validation](../project-validation/SKILL.md) as a sibling directory. Install it with this skill, or use the feature-development bundle. If missing, report the dependency and pause dependent maintenance.

Edit only project-validation and its project-local check documentation, such as docs/project-checks.md. Product intent and implementation guidance belong to feature-workflow. Do not edit product code, tests, dependencies, package scripts, lint/compiler configuration, or CI. Use only the companion's validation procedure within this narrower scope; do not enter its safeguard-improvement mode or invoke other maintainers recursively. Recommend separate implementation work for uncovered gaps.

## Inspect and reconcile

1. Read project instructions, validation guidance, local check documentation, and the actual diff. Trace each affected claim to supporting code, scripts, configuration, and CI. Follow moved code, new state writers, changed ordering, and failure behavior.
2. Use a recorded baseline if available; otherwise inspect relevant history. If instructions are untracked or history is unavailable, inspect current supporting files and state the limit. Include uncommitted changes. Distinguish observed configuration, executed checks, proposed checks, and uncovered behavior.
3. Update stale commands, paths, coverage, and assumptions from code and intended requirements. A product bug does not justify relaxing expectations. A missing check is a gap, not permission to install tools. Keep exact commands and project facts in local documentation, not reusable skill bodies. Check local/CI agreement when affected, without changing enforcement.
4. For wording or link changes, review documents and references only. If commands, coverage, assumptions, or procedures change, use project-validation on affected checks where safe and practical; capture before/after results when useful. Apply its isolated failure-demonstration guidance only when the critical check's effectiveness is affected. Never mutate the live app for instruction upkeep. Report skipped execution and demonstrations with reasons.
5. Review the maintenance diff and walk through the affected procedure. Confirm metadata and links, ownership boundaries, evidence labels, and accurate verification claims. Do not duplicate the companion's validation mechanics here.

## Report

Report current, updated, product finding, or unresolved per affected instruction item, with reasons and evidence. Separately report checks as passed, failed, not run, or not covered using the companion's reporting contract. A procedure can be updated while a product finding remains. Record reviewed scope, date, inspected revision plus dirty paths; use existing baseline records without adding tracking machinery. Preserve the last successful execution record for blocked checks and record the present limitation separately. A document observation date does not imply a passing check.
