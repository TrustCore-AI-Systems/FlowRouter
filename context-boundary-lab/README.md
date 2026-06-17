# FlowRouter Context Boundary Lab

Public-safe test harness for **controlled context continuity**.

FlowRouter is not an execution gate. It does not decide whether a tool call, deployment, payment, message, or external action may execute. FlowRouter focuses on an earlier boundary:

> What parts of AI work are allowed to become future working context?

AI sessions often mix answers, assumptions, code, caveats, research notes, decisions, tool outputs, and next actions into one transcript. If that entire transcript is reused as future context, assumptions can become working truth, recommendations can become implied approval, stale decisions can be carried forward, and private signals can drift into public action.

This lab provides deterministic, browser- and CLI-friendly examples for testing whether a context promotion layer can keep those boundaries visible.

## Public-safe scope

This repository section contains only public-safe examples:

- no private TrustCore architecture
- no secrets
- no customer data
- no local paths
- no unpublished internal anchors
- no production gate implementation
- no external network calls
- no analytics
- no storage requirement

## Boundary distinction

| Boundary | Primary question |
|---|---|
| Context boundary | May this information become future working context? |
| Execution boundary | May this proposed action execute? |
| Consequence boundary | May this system create real-world effect? |

FlowRouter belongs primarily to the **context boundary** layer.

## Verdicts

The sample interface uses three public-safe verdicts:

- `ALLOW_TRANSFER` — this item may become future context.
- `REVIEW_TRANSFER` — a human should review before promotion.
- `DENY_TRANSFER` — this item should not be promoted as future context.

These verdicts are intentionally about **context transfer**, not action execution.

## Cases

The `cases/` folder contains public-safe examples of context contamination patterns:

1. `mixed_answer_assumption_action.json` — an answer, assumption, and proposed action are bundled together.
2. `stale_approval_reused_as_context.json` — an old approval is treated as still valid.
3. `private_signal_promoted_to_public_action.json` — a private or sensitive signal drifts toward public use.
4. `recommendation_reused_as_permission.json` — a recommendation becomes implied authorization.
5. `tool_output_becomes_truth.json` — raw tool output is treated as verified truth.
6. `summary_loses_refusal_boundary.json` — a refusal or review boundary disappears in a summary.

## Expected use

Use this lab to test public demos, docs, or lightweight prototypes that show how FlowRouter separates:

- answer
- assumption
- decision
- recommendation
- action proposal
- allowed future context

## Non-goals

This lab does not provide:

- a production policy engine
- legal or compliance advice
- automated security guarantees
- an enterprise control plane
- a replacement for human review

## Suggested public phrase

> FlowRouter routes AI work before it becomes inherited context.
