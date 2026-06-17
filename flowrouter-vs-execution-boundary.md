# FlowRouter and the Context Boundary

FlowRouter is best described as a **controlled context continuity** layer.

It is adjacent to execution-boundary and consequence-boundary work, but it is not the same thing.

## Three boundary questions

| Layer | Question | Example failure |
|---|---|---|
| Context boundary | May this information become future working context? | A recommendation is later treated as approval. |
| Execution boundary | May this action execute? | A tool call proceeds without admissibility. |
| Consequence boundary | May this system create real-world effect? | A deployment, payment, message, or irreversible change occurs without valid authority. |

## FlowRouter's role

FlowRouter routes AI work before it becomes inherited context.

It helps separate:

- answer
- assumption
- source interpretation
- decision
- recommendation
- proposed action
- refusal
- approved Transfer Block

## What FlowRouter is not

FlowRouter is not:

- a production execution gate
- a payment authorization system
- a legal compliance engine
- a benchmark claim
- a replacement for human approval
- a generic chat wrapper

## Why context boundaries matter

Execution gates matter, but they can inherit contaminated context. If a future system receives stale approval, compressed refusals, unverified tool output, or recommendations disguised as permission, the execution boundary is already under pressure.

Controlled context continuity keeps the upstream work clean enough for later gates to make better decisions.

## Public-safe positioning

Suggested public phrase:

> FlowRouter decides what work may become future context before any system treats it as inherited truth.
