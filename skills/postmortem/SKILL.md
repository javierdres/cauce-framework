---
skill: postmortem
stage: 10
name: Postmortem
triggered_by: [operate]
triggers: [harvest]
gate: closing gate
gate_owner: Operations owner
writes_outside: [document]
consults: []
---

# /postmortem — Postmortem

## Purpose

Reconstruct what happened and why, so the organisation learns from the incident.

## Preconditions

A closed incident. Access to the data sources for that period.

## What it does

- Reconstructs the timeline from the sources, not from the memory of whoever was on call.
- Separates the root cause from the contributing factors.
- Names what would have caught the problem sooner, and whether that exists or has to be built.
- Triggers /harvest with the root cause.

## What it does NOT do

- Does not assign blame to people.
- Does not close the incident: a person does.

## Gate

**Closing gate.** Owned by: Operations owner.

## Dossier

**Reads:** An incident.

**Writes:** Timeline, root cause, and material for stage 12.
