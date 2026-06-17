# FlowRouter

**Controlled context continuity for AI work.**  
Split the work, route the lanes, and transfer only selected context forward.

FlowRouter is a public-safe TrustCore pattern for keeping AI work from collapsing into one noisy inherited context.

It is **not** an execution gate.  
It is a **context boundary**: a way to decide what parts of AI work should become future working context at all.

---

## Why this matters

AI systems often mix many different things into one response:

- direct answers
- assumptions
- research notes
- code
- recommendations
- decisions
- next actions
- tool outputs
- memory candidates

If that whole mixture is carried forward as context, future work may inherit assumptions as facts, recommendations as permission, or private signals as public action.

FlowRouter separates the work before it becomes inherited context.

---

## Core idea

FlowRouter asks:

> Should this piece of work become future context?

That is different from an execution gate, which asks:

> May this action proceed?

And it is different from a consequence boundary, which asks:

> May this system create real-world effect?

FlowRouter sits earlier in the workflow.  
It helps structure the context that later systems, agents, reviewers, or gates may rely on.

---

## Context boundary

FlowRouter treats context promotion as a controlled step.

A piece of AI output should not automatically become trusted future context just because it appeared in a conversation, summary, tool result, or generated artifact.

FlowRouter-style context handling separates:

| Layer | Question |
|---|---|
| Answer | What was directly asked and answered? |
| Assumption | What was inferred but not verified? |
| Recommendation | What is suggested but not approved? |
| Decision | What has actually been accepted? |
| Action | What would create an external effect? |
| Transfer Block | What selected context may move forward? |

---

## Transfer Blocks

A **Transfer Block** is a selected unit of context that may be moved forward with boundaries attached.

It is not a raw transcript.  
It is not a memory dump.  
It is not a generic summary.

A Transfer Block should make clear:

- source
- target
- purpose
- status
- allowed use
- known uncertainty
- whether human approval is still required

This keeps future work from treating every previous message as equal authority.

---

## What this repository contains

This repository contains public-safe FlowRouter material:

```text
context-boundary-lab/
  README.md
  SPEC.md
  cases/
  gate_api/
  reports/
  tests/

context_boundary_lab/
  helper package for local tests

flowrouter-vs-execution-boundary.md
```

The goal is to demonstrate context-boundary failure modes without exposing private TrustCore architecture, unpublished IP, customer data, secrets, or internal implementation details.

---

## Example failure modes

The context-boundary lab focuses on cases such as:

- a recommendation reused as permission
- stale approval reused after the situation changed
- private signal promoted into public action
- tool output treated as verified truth
- refusal or review boundary lost during summarization
- answer, assumption, and action mixed into the same future context

These are not execution failures yet.  
They are context-continuity failures that can pressure later execution gates.

---

## Public-safe scope

This repository is a public preview and research surface.

It does **not** contain:

- production TrustCore architecture
- private gate implementations
- customer data
- secrets or credentials
- unpublished internal anchors
- production security claims
- compliance certification claims

It is intended to explain the FlowRouter pattern and provide a safe reference point for discussion.

---

## Relationship to TrustCore

TrustCore focuses on control before consequence.

FlowRouter contributes one earlier layer:

> Route AI work before it becomes inherited context.

This helps preserve the boundary between information, recommendation, decision, approval, and action.

---

## Status

Public-safe preview.

The material in this repository is experimental and explanatory.  
It should not be treated as production security software or compliance tooling.

---

## Contact

TrustCore AI Systems Oy  
Public brand: **TrustCore**  
Website: **https://trustcore.fi**

For discussion, pilots, or security-related contact:

- **kari.hyotyla@trustcore.fi**
- **security@trustcore.fi**
