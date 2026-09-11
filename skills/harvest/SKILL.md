---
skill: harvest
stage: 12
name: Learning
triggered_by: [review, postmortem]
triggers: []
gate: per-rule gate
gate_owner: Standard custodian
writes_outside: [catalog]
consults: [catalog, false-positives]
---

# /harvest — Learning

## Purpose

Make decisions and root causes outlive the conversation or the shift where they appeared.

## Preconditions

Write access to the standards repository. Catalog and false-positive record up to date.

## What it does

- Takes two sources: resolved threads from a review, and root causes from an incident.
- Harvests only what meets both conditions: the thread closed with an explicit outcome, and the claim still holds outside that case.
- Discards what describes how a particular project is built, which belongs in that project's documentation, and generic good practice with no decision of our own behind it, which the industry baseline already covers.
- Deduplicates against the catalog before drafting. If the rule already exists, it edits the existing one, adding the origin and a line to its history.
- Drafts the rule as a candidate, never as in force.
- Always closes with three lists: harvested, discarded with the reason, and pending decisions.

## What it does NOT do

- Does not promote a rule to in force.
- Never writes a rule without confirmation, rule by rule.
- Does not invent rules with no linkable origin.

## Gate

**Per-rule gate.** Owned by: Standard custodian.

## Dossier

**Reads:** Resolved threads and root causes.

**Writes:** Candidate rules and the three-list report.
