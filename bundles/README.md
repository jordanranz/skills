# Bundles

Bundles are small YAML manifests that group canonical skills without copying them.

```yaml
name: example
description: A short explanation of the outcome.
skills:
  - skills/category/skill-name
```

A skill may appear in multiple bundles while retaining one canonical location under `skills/`.

## Feature development

[`feature-development.yaml`](feature-development.yaml) includes feature-workflow, project-validation, and their two maintainers. The implementation and maintenance skills declare required companions in the string-valued `metadata.requires-skills` field of their frontmatter. This documents dependencies for agents and installers; it is not a promise that a host automatically resolves them.

Use a compatible installer to install every manifest member, or copy the four canonical directories into the target project's `.agents/skills/` directory. Preserve their names and keep them as siblings so relative references resolve. The manifest alone does not perform installation. If a required companion is missing, dependent work reports that condition instead of silently omitting its obligations. Project-validation works independently. Parent skills mention maintainers as optional upkeep tools, so ordinary implementation and validation do not require loading them.

Keep target-project facts in its own documentation, such as `docs/project-context.md` and `docs/project-checks.md`. These files are not part of the reusable bundle. Existing project documentation may be used instead; missing context is discovered from code rather than filled with assumptions from another project.
