---
skill: validate-outcome
stage: 11
name: Outcome validation
triggered_by: [deploy]
triggers: []
gate: product gate
gate_owner: Product owner
writes_outside: [ticket]
consults: []
---

# /validate-outcome — Outcome validation

## Purpose

Go back and ask whether the problem from stage 1 was actually solved.

## Preconditions

The change has been in production for the period set in stage 2. Business indicators available.

## What it does

- Compares observed behaviour in production against the problem stated in stage 1.
- Distinguishes three outcomes and names them without softening: the problem was solved, it was half solved and here is what was left out, or it was not solved and the original hypothesis was wrong.
- Records the hypothesis that failed, which is as valuable as a root cause and is lost just as easily.

## What it does NOT do

- Does not decide what to do about the outcome: product does.

## Gate

**Product gate.** Owned by: Product owner.

## Dossier

**Reads:** Post-deployment check and the stage 1 criteria.

**Writes:** The outcome measured against the original problem.
