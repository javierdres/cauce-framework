# Adoption

In this order. Each step works without the ones after it, and none requires the previous one to
be perfect.

## 0. Scaffold what everyone needs anyway

The standards catalog is identical for anyone starting out, and so is the shape of a project's
config. Neither is worth building by hand.

```
python3 bin/bootstrap.py catalog ../our-standards
python3 bin/bootstrap.py config  ../the-project-you-picked
```

The first writes a complete catalog repository: rule format, validator, catalog generator,
false-positive record, governance and contributing guides. Empty of rules, on purpose.

The second drops `.gate/config.yml` into your project, filling in whatever it can read off the
repository — its remotes, its branch convention, its lint and test commands — and leaving the
rest for `/init` to ask about.

- [ ] Catalog scaffolded, `python3 bin/validate.py` clean inside it
- [ ] Catalog repository created and committed
- [ ] `.gate/config.yml` in the project you picked

## 1. The standards catalog, empty

Empty on purpose: a set copied from an industry guide describes whoever copied it, not your
organisation. What matters now is that it exists and that rules can only enter through
`/harvest`, traceable to a real decision.

- [ ] Custodians named, before the first hard rule rather than during the argument about it
- [ ] Everyone knows rules are harvested, not written

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

## 7. Stage 0, definition and requirements

They depend on product picking up the habit, and that cannot be decreed.

- [ ] `/init`, `/define` and `/specify` implemented
- [ ] The dossier adopted as the only source of context

## 8. Outcome validation

Last, because it needs trustworthy business data and the willingness to record that a
hypothesis failed.

- [ ] `/validate-outcome` implemented
- [ ] A validation window set in stage 2 of every piece of work
