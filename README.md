# Skills

Reusable agent skills by Jordan Ranz, organized around four areas of work.

## Categories

- [Engineering](skills/engineering) — building, reviewing, debugging, and operating software and agent systems.
- [Product](skills/product) — discovery, strategy, prioritization, design, and delivery.
- [Leadership](skills/leadership) — decisions, communication, management, and organizational effectiveness.
- [Career](skills/career) — professional development, job search, interviewing, and positioning.

## Available skills

- [`feature-workflow`](skills/engineering/feature-workflow) — implement a small complete change with clear contracts and state ownership.
- [`project-validation`](skills/engineering/project-validation) — validate real behavior and assess static analysis, test, and CI coverage.
- [`maintain-feature-workflow`](skills/engineering/maintain-feature-workflow) — reconcile implementation instructions with project changes.
- [`maintain-project-validation`](skills/engineering/maintain-project-validation) — reconcile validation instructions and project-local check documentation.
- [`skill-scouter`](skills/engineering/skill-scouter) — inspect an agent skill and render an evidence-backed RPG-style Power Level character card.
- [`skillprint`](skills/engineering/skillprint) — compile an agent skill into a deterministic, source-traceable workflow graph.
- [`jev-decision-engineering`](skills/engineering/jev-decision-engineering) — design and evaluate Jev routing, scoring, context selection, and escalation in real workflows.
- [`resume-refinement`](skills/career/resume-refinement) — tailor and verify resumes without stretching the facts.
- [`evaluate-role-fit`](skills/career/evaluate-role-fit) — compare opportunities against verified experience, goals, and constraints.
- [`refine-application-response`](skills/career/refine-application-response) — interview for and refine authentic application answers.
- [`manage-job-search`](skills/career/manage-job-search) — maintain a selective pipeline and durable private search context.

## Bundles

[Bundle manifests](bundles) provide installable collections without duplicating skill files. A skill has one canonical category but may appear in multiple bundles.

Each skill begins with a `SKILL.md` file. Required companion skills are declared in `metadata.requires-skills` and in the instructions. Install declared companions as sibling directories; the [feature-development bundle](bundles/feature-development.yaml) includes the complete implementation and validation set. Bundle manifests describe collections; they do not install skills themselves. See [bundle installation](bundles/README.md) for layout and dependency details.
