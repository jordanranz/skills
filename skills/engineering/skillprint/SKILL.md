---
name: skillprint
description: Compile an agent skill into a deterministic, source-traceable workflow graph for inspection, explanation, comparison, or rendering in the Skillprint app. Use when visualizing how a SKILL.md package works, deriving nodes and edges from its instructions, explaining human/agent/artifact handoffs, or producing structured workflow data for jordanranz/skillprint.
---

# Skillprint

Turn skill instructions into a compact workflow map. Preserve evidence; do not invent behavior to make the graph more interesting.

## Compile a skill

1. Resolve the target skill directory. For Jordan Ranz skills, use `https://github.com/jordanranz/skills` as the canonical repository; skills are flat within their category, such as `skills/engineering/skill-scouter` and `skills/engineering/skillprint`.
2. Read the target `SKILL.md` completely. Read only references required to understand its normal execution path.
3. Identify the trigger, required inputs, ordered actions, human decisions, produced artifacts, verification, and loops.
4. Create the smallest graph that preserves meaningful control flow. Prefer 3–8 nodes.
5. Give every node a direct source trace. Quote sparingly; otherwise use a faithful paraphrase.
6. Validate that every edge follows an explicit dependency or sequence. Mark inferred relationships as interpretations.
7. Return the structured graph below plus a one-sentence purpose and best-use summary.

## Graph contract

```json
{
  "purpose": "One sentence",
  "bestFor": "One sentence",
  "nodes": [
    {
      "id": "stable-kebab-id",
      "kind": "human | agent | artifact | loop",
      "label": "Short action label",
      "note": "Two-to-four-word caption",
      "summary": "What happens and why",
      "actor": "Human, Agent, or Human + agent",
      "output": "Concrete output",
      "source": "Direct source trace or faithful paraphrase"
    }
  ],
  "edges": [["source-node-id", "target-node-id"]]
}
```

Use node kinds consistently:

- `human`: judgment, confirmation, or input that cannot be safely inferred.
- `agent`: analysis or execution performed by the agent.
- `artifact`: a durable output or verified result.
- `loop`: an explicit return, retry, or recurring frontier.

## Determinism rules

- Derive identical node IDs, order, and labels from unchanged source.
- Use source order as the primary node order.
- Merge adjacent instructions only when they share the same actor and output.
- Split branches only when the source defines a real choice or parallel path.
- Never add decorative branches, scores, installs, or popularity data.
- Keep assessment separate from visualization. Use the sibling `skill-scouter` skill when a Scouter Score or quality evaluation is required.

## Project locations

- Canonical skills: `https://github.com/jordanranz/skills`
- Skillprint application: `https://github.com/jordanranz/skillprint`
- Skillprint responsibility: workflow compilation and source traceability.
- Skill Scouter responsibility: deterministic inspection and evidence-backed assessment.
