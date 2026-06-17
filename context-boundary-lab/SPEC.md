# Context Boundary Lab Specification

Version: `0.1-public-preview`

## Purpose

The purpose of this lab is to model a public-safe **context promotion boundary**.

A context promotion boundary evaluates whether a piece of AI-generated or AI-observed information should be allowed to move forward into future work as context.

This is different from evaluating whether an action may execute.

## Problem statement

AI work frequently creates mixed artifacts. A single response can contain:

- a direct answer
- an assumption
- a partial source interpretation
- a recommendation
- a draft action
- a caveat
- a refusal
- a tool result
- a decision-like statement
- a next step

When the entire artifact is blindly carried forward, future systems may lose the distinction between what was known, guessed, suggested, refused, approved, or merely observed.

## Core rule

> Context in is not automatically context allowed forward.

## Objects

### Context item

A context item is a unit of candidate information that might be promoted into future context.

Example fields:

```json
{
  "id": "case-001:item-001",
  "type": "assumption",
  "content": "The prior approval still applies.",
  "source": "assistant_response",
  "target_use": "future_planning",
  "risk_flags": ["stale_authority"],
  "human_review_required": true
}
```

### Context snapshot

A context snapshot describes the surrounding state at the moment of evaluation.

Example fields:

```json
{
  "current_task": "prepare_public_repo_copy",
  "target_surface": "public_github",
  "user_approval_state": "not_approved_for_publish",
  "sensitivity_level": "public_safe_required"
}
```

### Evaluation result

A result should preserve:

- verdict
- reason codes
- explanation
- safe transformed content, if applicable
- review requirement
- audit-friendly trace metadata

Example:

```json
{
  "verdict": "REVIEW_TRANSFER",
  "reason_codes": ["MIXED_ACTION_AND_ASSUMPTION"],
  "explanation": "The item mixes an assumption with a proposed action and should not be promoted without review.",
  "safe_content": null,
  "human_review_required": true
}
```

## Verdict semantics

| Verdict | Meaning |
|---|---|
| `ALLOW_TRANSFER` | Safe to carry forward as future context. |
| `REVIEW_TRANSFER` | Potentially useful, but needs human review before promotion. |
| `DENY_TRANSFER` | Should not be promoted as future context. |

## Public reason codes

Suggested reason codes:

- `MIXED_ANSWER_ASSUMPTION_ACTION`
- `STALE_APPROVAL`
- `PRIVATE_SIGNAL_PUBLIC_SURFACE`
- `RECOMMENDATION_AS_PERMISSION`
- `RAW_TOOL_OUTPUT_UNVERIFIED`
- `REFUSAL_BOUNDARY_LOST`
- `AUTHORITY_SCOPE_AMBIGUOUS`
- `TARGET_SURFACE_PUBLIC`
- `HUMAN_APPROVAL_REQUIRED`

## Minimal invariant set

1. A recommendation must not be promoted as approval.
2. A draft action must not be promoted as permission.
3. A private signal must not be promoted into a public surface without review.
4. A stale approval must not be reused as current authorization.
5. A summary must preserve refusal and review boundaries.
6. Raw tool output must not be promoted as verified truth without validation.

## Public demo pattern

A safe demo can show:

1. mixed AI output
2. lane split
3. candidate Transfer Blocks
4. context boundary evaluation
5. final promoted context
6. held or denied items

## Safety note

This specification is illustrative and public-safe. It is not a production security control and does not represent any private TrustCore implementation.
