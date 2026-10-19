# Engineering

Skills for building, reviewing, debugging, and operating software and agent systems.

- [`feature-workflow`](feature-workflow) — implementation contracts, state ownership, and complete flows. Requires project-validation.
- [`project-validation`](project-validation) — checks, failure investigation, evidence, and authorized safeguard improvements. No required companions.
- [`maintain-feature-workflow`](maintain-feature-workflow) — upkeep of implementation instructions and project context. Requires feature-workflow and project-validation.
- [`maintain-project-validation`](maintain-project-validation) — upkeep of validation instructions and local check documentation. Requires project-validation.

Install the [feature-development bundle](../../bundles/feature-development.yaml) for all four. Keep project-specific constraints and commands in the target project's documentation, not in the canonical skills.

- [`skill-scouter`](skill-scouter) — inspect and compare agent skills using an evidence-backed Power Level.
- [`skillprint`](skillprint) — compile agent skills into deterministic, source-traceable workflow graphs.
- [`jev-decision-engineering`](jev-decision-engineering) — add Jev decisions where they change a workflow and measure the result.
