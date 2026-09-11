---
skill: build
stage: 5
name: Development
triggered_by: [person]
triggers: [self-review]
gate: none
gate_owner: —
writes_outside: [repositories]
consults: [catalog]
---

# /build — Development

## Purpose

Implement, leaving the trail the later stages depend on.

## Preconditions

A dossier with an accepted design. A branch linked to the ticket. Linters, static analysis and tests installed.

## What it does

- Consults the catalog before proposing a pattern.
- Instruments whatever the observability plan called for, in the same change and not afterwards.
- Writes the tests alongside the code, not as a later task that gets cut when the deadline bites.

## What it does NOT do

- Does not decide architecture: that was settled in stage 4.
- Does not open the change proposal: that is /self-review.

## Gate

None. This skill does not stop the chain.

## Dossier

**Reads:** Decision record and subtasks.

**Writes:** The change implemented, instrumented and tested.
