# Power rubric

Power estimates useful capability for the skill's intended task. Score each input from 0–100, then compute:

```text
power = round(100 × (
  task_value × 0.25 +
  effectiveness × 0.30 +
  reliability × 0.20 +
  efficiency × 0.15 +
  coverage × 0.10
))
```

## Inputs

- **Task value — 25%:** Importance, frequency, and consequence of the intended outcome. Narrow does not mean weak when the narrow task is valuable.
- **Effectiveness — 30%:** How strongly the workflow appears to improve the outcome. Prefer executable capability, precise procedures, domain knowledge, worked examples, and behavioral uplift.
- **Reliability — 20%:** Consistency and verifiability: completion conditions, failure handling, validators, tests, reproduced runs, maintained dependencies, and absence of contradictions.
- **Efficiency — 15%:** Value relative to activation tokens, typical reference loading, tool calls, latency, setup, and repeated work. Follow aliases and runtime-loaded instructions before scoring.
- **Coverage — 10%:** Realistic variations, boundary cases, failure states, supported environments, and appropriate limits. Do not reward irrelevant breadth.

Distinguish documentation claims, structural examples, observed agent runs, and matched with-skill versus baseline fixtures.

## Displayed diagnostics

Display Guidance and Discoverability, but do not add them again to Power:

- **Guidance:** clarity, actionability, sequencing, output contract, and completion boundary.
- **Discoverability:** whether the name and description communicate what the skill does and when it should trigger.

Assign all six displayed qualities independently from 0–100. Convert to bars with `round(value / 10)`, clamped from 1–10 for a present skill.

## Gates and deductions

- Material unmitigated destructive, credential, network, or untrusted-content risk reduces Reliability.
- Missing evidence is not failure, but limits claims about Reliability and Effectiveness.
- A missing dependency reduces Coverage and Reliability.
- Broken references, stale internal counts, duplicated content, or host-specific invocation reduce Reliability or Efficiency in proportion to impact.
- Stars, installs, rank, contributors, and author reputation belong under Ecosystem only.

Use concrete evidence labels such as `static inspection`, `structure validated`, `examples extracted`, `observed run`, and `baseline uplift`. Avoid unsupported labels such as `battle-tested`.
