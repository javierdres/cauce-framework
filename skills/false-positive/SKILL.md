---
skill: false-positive
stage: cross-cutting
name: Cross-cutting
triggered_by: []
consulted_by: [self-review, review]
triggers: []
gate: none
gate_owner: —
writes_outside: [false-positive record]
consults: [false-positives]
---

# /false-positive — Cross-cutting

## Purpose

Put on the record a finding the team rejected, and why, so it does not get raised again.

## Preconditions

Write access to the false-positive record.

## What it does

- Records what the analysis raises, why it does not apply, and what to check before raising it again.
- Links the origin of the rejection.
- Deliberately skips the rule approval process: if recording a false positive cost an approval, nobody would record one.

## What it does NOT do

- Does not fix the rule that produced the false positive: that is a catalog change, through its own process.

## Gate

None. This skill does not stop the chain.

## Dossier

**Reads:** A rejected finding and its reason.

**Writes:** An entry in the false-positive record.
