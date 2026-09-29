---
name: jev-decision-engineering
description: Design or review a Jev decision layer in an application or agent workflow. Use when typed semantic judgments might route requests, select context, score candidates, or decide escalation, and the result needs a measured comparison with simpler alternatives.
---

# Jev decision engineering

Build a small semantic decision that changes a real downstream action. Start with the existing workflow and identify one place where code has enough candidates and facts, but needs judgment about meaning. Do not add Jev when an exact lookup, rule, search index, or simple parser already solves the problem.

## Design the seam

1. Name the decision, its candidate outcomes, the downstream consumer, and the cost of a wrong answer. State what happens when Jev is uncertain or unavailable.
2. Keep facts, arithmetic, authorization, and side effects in deterministic code. Jev may classify, compare, or score supplied evidence; it does not establish facts that were never supplied or grant permission to act.
3. Select the smallest useful state and question. Keep private data and source text out unless the task requires them and their use is permitted. For implementation details, check the current [TypeSafe documentation](https://docs.typesafe.ai/) and [official SDK](https://github.com/typesafe-ai/typesafe-sdk-js); do not rely on a remembered API shape.
4. Validate the typed response in code, then apply a policy matched to the consequence. A confidence value is evidence about the model's answer, not proof the route is correct. A harmless suggestion and an irreversible action need different gates. Preserve a no-match or broader-review path.
5. Connect the accepted decision to an actual consumer, or label it as an advisory plan. Do not claim a workflow is automated when it only emits a trace.

## Make the benefit testable

Before adding the call, record a baseline: the current rule, keyword route, or larger-agent path. Define representative labeled cases, including ambiguity, missing evidence, and provider failure. Test the **downstream result**, not only whether Jev chose the expected label.

Emit a trace that can answer: what question was asked, what answer and uncertainty came back, what code selected, what context actually entered a larger model, whether that model ran, and the latency and token usage of both paths where available. Redact sensitive input and avoid logging credentials. Distinguish measured savings from estimated context reduction. Use the [evaluation contract](references/evaluation.md) when designing traces or comparisons.

Keep the integration only if it improves task quality or reduces total cost or latency on the representative set. Report false narrowings and escalation rates alongside averages. If Jev makes a case uncertain, use the fallback instead of forcing a crisp answer.

## Keep the boundary reusable

Put project-specific intents, rubrics, thresholds, file manifests, permissions, and data sources in the project. The shared skill describes how to judge and verify the seam. Record why Jev was chosen over the baseline and which observations would reverse that decision.

For broader patterns, the [10 Levels of Jev](https://github.com/disler/ten-levels-of-jev) is a useful progression, not an implementation checklist. Add a level when a real workflow and evidence justify it.
