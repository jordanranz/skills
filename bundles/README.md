# Bundles

Bundles are small YAML manifests that group canonical skills without copying them.

```yaml
name: example
description: A short explanation of the outcome.
skills:
  - skills/category/skill-name
```

A skill may appear in multiple bundles while retaining one canonical location under `skills/`.
