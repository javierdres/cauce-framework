---
skill: catalog
stage: cross-cutting
name: Cross-cutting
triggered_by: []
consulted_by: [refine, design, self-review, review]
triggers: []
gate: none
gate_owner: —
writes_outside: []
consults: [catalog]
---

# /catalog — Cross-cutting

## Purpose

Fetch the rules in force that apply by scope and by project, so the other skills do not each solve it their own way.

## Preconditions

A catalog readable by machine.

## What it does

- Filters by status, scope and projects.
- Returns rules in force with their real severity, and candidates always as suggestions.
- If the catalog cannot be read, says so explicitly rather than passing over it in silence.

## What it does NOT do

- Does not assess code.
- Does not promote or edit rules.

## Gate

None. This skill does not stop the chain.

## Dossier

**Reads:** Scope and project of the work.

**Writes:** Applicable rules with their severity.
