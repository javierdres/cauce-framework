# Contributing to GATE

GATE is in use and under continuous improvement. The most valuable contributions come from
having applied it, not from having read it.

## What helps most

**Adoption experience.** Which stage was hardest to roll out, which one you skipped and what
happened, at what team size. That is worth more than a wording fix.

**Sharpened skill contracts.** If implementing a skill showed it is missing a limit, or doing
something it should not, change it and explain the case that prompted it.

**New anti-patterns.** That section grew out of real mistakes. If you have seen one that is
missing, add it with what it cost.

## What does not belong here

Specific standard rules. The catalog belongs to each organisation and lives in its own
repository: this framework defines how it is fed, not what it says.

Ceremonies, cadence or estimation. GATE describes the journey of a piece of work and who
clears each step; how you organise the team sits outside.

Generic good practice with no decision behind it. If you cannot trace it to something that
happened, it is not material for this framework yet.

## Before opening a pull request

Run the validator. It checks the contracts are complete and the trigger chain closes both ways.

```
python3 bin/validate.py
```

If you touched `GATE.md`, regenerate the PDF.

```
python3 bin/build_pdf.py GATE.md
```

## Licence of contributions

By submitting a contribution you agree it is published under the repository's licences: CC BY
4.0 for documentation and MIT for code. Nothing to sign.
