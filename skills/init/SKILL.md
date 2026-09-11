---
skill: init
stage: 0
name: Entry point
triggered_by: [person]
triggers: [define]
gate: none
gate_owner: —
writes_outside: [ticket]
consults: []
---

# /init — Entry point

## Purpose

Take in a need in any format and open the dossier that will travel with the work through the whole cycle.

## Preconditions

Access to the issue tracker and to the history of previous work.

A `.gate/config.yml` in the project. If it does not exist, this skill creates it from
`templates/gate-config.yml` before anything else.

## What it does

- **Reads `.gate/config.yml` first, and completes it.** If the file is missing, it is created
  from the template. If any field required to start is empty, the chain stops here: fill in
  what can be detected from the repository — repositories, branch convention, lint and test
  commands — propose the rest, and ask. Nothing else happens until those fields are filled.
- Reports the fields that are still empty and which stage will need each one. An empty optional
  field is a valid declaration that the stage using it is not in use yet, not an error.
- Classifies the type of work: new project, change to something that exists, or incident. That classification decides which stage the chain enters at.
- Identifies who is asking and what for. That is the only thing that cannot be missing; stage 1 gathers everything else by asking.
- Checks whether a dossier or ticket already covers the same thing, and updates it instead of opening a duplicate.
- Opens the dossier and links it to the ticket.

## What it does NOT do

- Does not define the problem or propose a solution.
- Does not prioritise or estimate.
- Does not open the ticket without approval from whoever asked.

## Gate

None. This skill does not stop the chain.

## Dossier

**Reads:** A need in any format: a note, an email, a transcript, a support ticket. And
`.gate/config.yml`, which it completes before opening anything.

**Writes:** An open dossier, with who is asking, what for, and what type of work it is.
