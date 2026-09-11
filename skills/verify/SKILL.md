---
skill: verify
stage: 8
name: Functional verification
triggered_by: [self-review, person]
triggers: []
gate: QA gate
gate_owner: Verifier
writes_outside: []
consults: []
---

# /verify — Functional verification

## Purpose

Check against the criteria from stage 2, on the running system.

## Preconditions

The change deployed to a test environment. The script drafted in stage 6.

## What it does

- Writes the script with one checkbox per verifiable result, not one per case, so a failure points at what failed.
- One block per affected component, naming what to look at on each screen.
- The precondition written as a check the tester can perform, with what to do if it is not met.
- Steps executable with the tools the tester already has.
- Known false alarms, stated up front.
- What to do with whatever cannot be tested in that environment: leave it unchecked and note it, never mark it failed.

## What it does NOT do

- Does not run the tests.
- Does not sign off on any criterion.

## Gate

**QA gate.** Owned by: Verifier.

## Dossier

**Reads:** The verification script.

**Writes:** A result per criterion.
