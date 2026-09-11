---
skill: refine
stage: 3
name: Refinement
triggered_by: [specify]
triggers: [design]
gate: engineering gate
gate_owner: Engineering lead
writes_outside: [subtasks]
consults: [catalog]
---

# /refine — Refinement

## Purpose

Turn requirements into executable work, with the risks on the table before any code is written.

## Preconditions

Stage 2 approved. Read access to the code of every component that might be involved.

## What it does

- Breaks the work into tasks, each with a verifiable output.
- Maps which components are affected by reading the actual code. A map drawn from memory or from an old diagram is wrong precisely about the systems that changed the most.
- Raises security and compliance risks, grounded in the data classification and in the hard rules currently in force.
- Detects when a requirement collides with a rule in force and raises it as a product decision, not as a problem to solve later.
- Proposes the test plan, including regression over whatever the change brushes against.
- Proposes the observability plan. Whatever is not instrumented here does not exist in stage 10.

## What it does NOT do

- Does not implement.
- Does not commit to dates.
- Does not let a risk through without an owner.

## Gate

**Engineering gate.** Owned by: Engineering lead.

## Dossier

**Reads:** Acceptance and compliance criteria.

**Writes:** Subtasks, component map, risks with owners, test and observability plans.
