---
skill: operate
stage: 10
name: Operations and SRE
triggered_by: [deploy, alert]
triggers: [postmortem]
gate: operations gate
gate_owner: Operations owner
writes_outside: [alerts, incidents]
consults: []
---

# /operate — Operations and SRE

## Purpose

Keep the service up, detect before the user does, and recover inside the committed window.

## Preconditions

Accessible data sources: application and infrastructure logs, metrics, traces, audit trail, external dependency status. A correlation id propagated end to end and a declared retention period.

## What it does

- Correlates the sources from a symptom and separates cause from noise, grounding every claim in the source that can prove it.
- Compares current behaviour against the baseline before the last change and links it to the ticket that introduced it.
- Proposes what deserves an alert and, above all, what does not: if nobody will do anything differently when it fires, it is a dashboard number.
- Prepares the recovery drill script and compares the real result against the committed window.

## What it does NOT do

- Never touches production without confirmation, including silencing an alert.
- Never asserts a cause without the source that proves it.

## Gate

**Operations gate.** Owned by: Operations owner.

## Dossier

**Reads:** A system in production.

**Writes:** Diagnoses backed by evidence, incidents, recovery drill results.
