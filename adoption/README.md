# Adoption

In this order. Each step works without the ones after it, and none requires the previous one to
be perfect.

## 1. The standards catalog, empty

A repository of your own, with a rule format, a validator and a generated catalog. Empty on
purpose: a set copied from an industry guide describes whoever copied it, not your
organisation.

- [ ] Repository created, using the format in `templates/rule.md`
- [ ] Format validator running
- [ ] A low-friction place to record false positives, outside the rule approval process

## 2. The pre-review

It returns the most for what it costs and forces nobody else to change how they work.

- [ ] `/self-review` implemented
- [ ] Linters and static analysis reachable from the skill
- [ ] Personal credentials per person, never shared
- [ ] A branch convention that links to the ticket

## 3. The change review, with harvesting inside it

Both together. An assisted review that does not harvest leaves the cycle open.

- [ ] `/review` implemented, designed to run several times
- [ ] `/harvest` triggered by `/review`, never by a person
- [ ] Confirmed that whoever builds does not review their own change

## 4. The functional verification script

Cheap, and it draws a clear line between review and QA.

- [ ] `/verify` implemented
- [ ] Script template adopted

## 5. Refinement and design

Once the catalog holds rules worth consulting before settling an architecture.

- [ ] `/refine` and `/design` implemented
- [ ] `/catalog` available to both
- [ ] Confirmed that whoever proposes a design does not accept it

## 6. Operations and SRE

Requires the data sources to exist and be trustworthy, usually the longest work of all.

- [ ] Correlation id propagated end to end
- [ ] One source of truth per question
- [ ] Declared, sufficient retention
- [ ] A rollback procedure exercised, not merely documented
- [ ] `/operate` and `/postmortem` implemented

## 7. Gate 0, definition and requirements

They depend on product picking up the habit, and that cannot be decreed.

- [ ] `/cauce`, `/define` and `/specify` implemented
- [ ] The dossier adopted as the only source of context

## 8. Outcome validation

Last, because it needs trustworthy business data and the willingness to record that a
hypothesis failed.

- [ ] `/validate-outcome` implemented
- [ ] A validation window set in stage 2 of every piece of work
