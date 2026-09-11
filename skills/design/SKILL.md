---
skill: design
stage: 4
name: Design
triggered_by: [refine]
triggers: []
gate: design gate
gate_owner: Engineering lead, not the person who will build it
writes_outside: [decision record]
consults: [catalog]
---

# /design — Design

## Purpose

Settle the architecture decision before any code is written, and put it on the record.

## Preconditions

Stage 3 approved.

## What it does

- Puts forward at least two workable alternatives with their consequences, rather than presenting one as if it were the only option.
- Names what each alternative closes off for the future, which usually weighs more than its cost today.
- Checks every alternative against the rules in force and against the patterns the project already holds.
- Writes the decision record: what was decided, what was ruled out and why, and what would have to change to revisit it.

## What it does NOT do

- Does not pick the alternative: a person who did not draft the proposal picks it.
- Does not proceed with a single alternative presented without contrast.

## Gate

**Design gate.** Owned by: Engineering lead, not the person who will build it.

## Dossier

**Reads:** Affected components and risks.

**Writes:** An architecture decision record.
