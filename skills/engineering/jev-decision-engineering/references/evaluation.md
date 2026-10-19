# Evaluation contract

Use this when designing a new Jev route, ranking step, context selector, or confidence gate. Keep the record small enough to inspect during a failed case.

## Decision record

| Field | Question it answers |
| --- | --- |
| `decision_id`, `version` | Which policy and question produced this result? |
| `input_ref` | Which redacted case or content hash was evaluated? |
| `candidates` | Was the correct option available to select? |
| `answer`, `probabilities` or `score` | What did Jev return? |
| `gate`, `reason` | Why did code accept, review, or reject it? |
| `selected_systems`, `selected_context` | What did the decision change? |
| `downstream_invoked` | Did the larger agent or tool actually run? |
| `latency_ms`, `input_tokens`, `output_tokens` | What did each measured step cost? |
| `outcome` | Was the user's task handled correctly? |

Use references or hashes for sensitive inputs. A trace should not become a second copy of private content. If context was selected but never sent to a downstream model, record it as *candidate reduction*, not token savings.

## Comparison

Run the same labeled cases through the baseline and Jev-assisted path. Compare task success, false narrowings, escalation rate, total wall time, and total model usage. Include service failures. Segment high-cost mistakes rather than hiding them in an average. If labels or outcomes are unavailable, describe the evaluation as a smoke test and leave savings unclaimed.

Thresholds should follow the cost of mistakes and the observed distributions. Revisit them when the question wording, candidates, model, or downstream action changes.
