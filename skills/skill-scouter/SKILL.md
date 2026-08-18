---
name: skill-scouter
description: Inspect an agent skill and render an evidence-backed RPG-style Power Level character card. Use when evaluating, comparing, auditing, understanding, or optimizing SKILL.md packages, including their purpose, qualities, token footprint, references, dependencies, maintenance, and ecosystem adoption.
---

# Skill Scouter

Measure first, then judge. Keep ecosystem popularity outside Power.

## Scout a skill

1. Resolve the target skill directory and repository root. For a remote target, fetch it into a temporary directory without modifying its source.
2. Run the deterministic inspector:

   ```bash
   python3 scripts/inspect_skill.py <skill-directory> \
     --repo-root <repository-root> \
     --skills-root <directory-containing-skills>
   ```

   Repeat `--skills-root` when dependencies may live in multiple category directories. Omit options that do not apply.
3. Follow every dependency reported as resolved. Treat a delegating wrapper and its dependency as one effective capability. Flag missing dependencies instead of guessing their contents.
4. Read the target `SKILL.md`, the references required for a typical invocation, and enough optional material to judge coverage. Do not treat maximum package tokens as typical invocation cost.
5. Read [references/power-rubric.md](references/power-rubric.md), assign the five Power inputs, and record a short evidence-based reason for each. Do not increase Power because of installs, stars, leaderboard rank, author fame, or repository size.
6. Gather current ecosystem metadata only when browsing or a connected source is available. Record its source and observation date. Use `Unknown` for missing values, never zero.
7. Render the card below. Display the raw integer score through 9,000. When the score is greater than 9,000, replace the visible number with `IT'S OVER 9000!` while retaining the raw value in machine-readable results.

## Character card

```text
<SKILL NAME>

POWER LEVEL    <raw score | IT'S OVER 9000!>

PURPOSE
<one sentence>

BEST FOR
<one sentence>

QUALITIES
Effectiveness    <10-segment bar>  <label>
Reliability      <10-segment bar>  <label>
Efficiency       <10-segment bar>  <label>
Coverage         <10-segment bar>  <label>
Guidance         <10-segment bar>  <label>
Discoverability  <10-segment bar>  <label>

FOOTPRINT
Activation       <body tokens>
Typical use      <effective range or best available estimate>
References       <count>
Dependencies     <names or None>

ECOSYSTEM
Leaderboard      <rank · source · scope | Unknown>
Installs         <count | Unknown>
License          <license | Unknown>
Scouted          <date>
```

Use ten fixed segments: `█` filled and `░` empty. Map 1–2 to Weak, 3–4 Limited, 5–6 Capable, 7–8 Strong, 9 Excellent, and 10 Exceptional.

After the card, state the strongest evidence, largest deduction, and measurement limitations. Label static inspection honestly; examples and validators are not equivalent to matched behavioral fixtures.

## Improve a skill

Treat optimization as a controlled experiment:

1. Work on a copy or reviewable branch. Never publish automatically.
2. Freeze the rubric, original score, and evaluation fixtures before editing.
3. Target the weakest quality with the smallest evidence-backed change.
4. Validate and rerun the same fixtures. If the inspector changed, run `python3 scripts/test_inspector.py`.
5. Rescout with the frozen rubric. Keep the change only when evidence shows improvement without a material regression.

Do not raise Power with filler, unnecessary references or tests, removed safeguards, or a changed rubric. Report the before and after score, changed qualities, edits, regressions, and a keep/revert verdict.
