---
skill: define
stage: 1
name: Definition
triggered_by: [intake]
triggers: [specify]
gate: product gate
gate_owner: Product owner
writes_outside: [ticket]
consults: [catalog]
---

# /define — Definition

## Purpose

Turn a need expressed in business language into a statement an engineering team can assess.

## Preconditions

An open dossier. Access to product documentation and to the record of past decisions.

## What it does

- Drafts the statement separating the observed problem from the solution someone already imagined. Most requests arrive with a solution inside and without the problem that motivated it.
- Flags ambiguity instead of resolving it: a statement that admits two readings comes back with both.
- Classifies the data involved: personal, health, financial, or regulated under any applicable rule.
- Looks for precedent: earlier tickets, decisions already taken, related incidents, catalog rules that apply to the domain.

## What it does NOT do

- Does not design the solution.
- Does not estimate or prioritise.
- Does not move to stage 2 without a data classification.

## Gate

**Product gate.** Owned by: Product owner.

## Dossier

**Reads:** A dossier with the type of work and who is asking.

**Writes:** Problem, context, constraints and data classification.
