# CAUCE

**Cycle of Assisted, Unified Construction and Engineering.** An AI-assisted SDLC framework: it
defines the stages of the software life cycle, their inputs and outputs, the human control
points and the actors of each one.

Agnostic of company, domain, language and platform.

*Cauce* is Spanish for the bed of a river. AI assistance without a channel is a flood. With
one, it is a river.

## Where to start

[CAUCE.md](CAUCE.md) is the full document. If you have ten minutes, read section 2 (the single
entry point and the dossier) and section 6 (the actors, and the line between what the AI does
and what people do).

## What is here

```
├── CAUCE.md            The full framework
├── skills/             The 16 skills, each with its contract
├── templates/          Dossier, design decision, QA script, postmortem, rule
├── bin/
│   ├── validate.py     Checks the contracts are complete and the chain closes
│   └── build_pdf.py    Regenerates the PDF from the Markdown
├── adoption/           How to roll it out, step by step
└── docs/CAUCE.pdf      The document as PDF
```

## What is deliberately not here

**Your organisation's rules.** The standards catalog belongs to each organisation and lives in
its own repository. This framework defines how that catalog is fed, not what it says.

**Ceremonies, cadence or estimation.** CAUCE describes the journey of a piece of work and who
clears each step. Scrum, Kanban or whatever you use to organise the team keeps working on top.

**Skill implementations.** Every skill declares its contract: who triggers it, what it
delivers, where it stops to ask. Wiring that to your tools is your part.

## The skills

Fourteen cycle skills and two cross-cutting ones. Each declares in its frontmatter who triggers
it, what it triggers, which gate it has, who owns that gate, what it writes outside and what it
consults.

```
python3 bin/validate.py
```

Checks that every contract is complete and that the chain closes both ways: if A says it
triggers B, B has to say it is triggered by A.

## The five moments of human invocation

`/cauce` when the need is born. `/build` when someone sits down to implement. `/review` when
someone reviews, several times. `/verify` when someone tests. `/deploy` when someone deploys.

The framework chains everything else. Mechanisms that depend on a person remembering to invoke
them do not happen.

## How to adopt it

See [adoption/](adoption/README.md). The framework pays from the second step; there is no need
to wait for the whole thing.

## Where it comes from

CAUCE is not a literature review. It comes from leading development teams and watching the same
four problems repeat: quality depending on who used the assistant that day, decisions
evaporating between conversations, security arriving late, and nobody able to answer which
standard was applied to a change.

Every rule in this framework answers something that went wrong in practice. The gates exist
because automation once executed more than it should have. The three role incompatibilities
exist because a small team with strong assistance converges fast, and sometimes in the wrong
direction. Stage 12 exists because it is easy to find an empty standards catalog next to a
change carrying a hundred and fifty discussion comments.

It is a living framework, in use and under continuous improvement. What are skill contracts
today will keep changing as it gets applied.

## Author and licence

Author and rights holder: **Javier Núñez**.

| What | Licence |
|---|---|
| Documentation: `CAUCE.md`, `README.md`, `skills/`, `templates/`, `adoption/`, `docs/` | [CC BY 4.0](LICENSE-DOCS) |
| Code: `bin/` | [MIT](LICENSE) |

You may use CAUCE in your organisation, adapt it and redistribute it, including commercially.
All that is asked is attribution.

### About the name

The licence covers the work, not the name. If you adapt CAUCE for your organisation, use it
freely. If you publish a derivative with substantial changes to the stages, the gates or the
split between what the AI does and what people do, give it another name and mention where it
came from: that way "CAUCE" keeps meaning one thing.
