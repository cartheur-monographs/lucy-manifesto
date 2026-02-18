# The Lucy Manifesto

The design and manufacturing criteria for the Lucy prototype.

## Purpose

This repository is the working home for an evolving manifesto built from `source.pdf`.
The goal is to progressively extract, structure, and refine the source material into a clear engineering proposal.

## Project Status

This is the initial project setup (`v0` scaffold).

## Repository Layout

- [`README.md`](README.md): project overview and workflow
- [`source.pdf`](source.pdf): canonical source material
- [`docs/ROADMAP.md`](docs/ROADMAP.md): phased implementation plan
- [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md): writing and review standards
- [`docs/PROJECT_OUTLINE.md`](docs/PROJECT_OUTLINE.md): GA144-based Lucy revitalization outline
- [`docs/manifesto-v0.1.md`](docs/manifesto-v0.1.md): current manifesto draft baseline
- [`docs/requirements.md`](docs/requirements.md): testable requirement set (`R*`, `S*`, `N*`)
- [`docs/architecture-ga144.md`](docs/architecture-ga144.md): runtime/module architecture for `v0.1`
- [`docs/test-strategy.md`](docs/test-strategy.md): validation and traceability plan

## Workflow

1. Extract source text from `source.pdf` into working notes.
2. Organize notes into themed sections (requirements, constraints, manufacturing).
3. Draft manifesto chapters.
4. Review for technical consistency and decision traceability.
5. Publish versioned revisions.

## First Milestones

- Define chapter structure for the manifesto.
- Produce first extracted notes set from `source.pdf`.
- Refine said notes in `source.txt`.
- Deliver and review `v0.1` manifesto draft at [`docs/manifesto-v0.1.md`](docs/manifesto-v0.1.md).

## v0.1 Gate Logic

- Source intent and interpretation: [`source.txt`](source.txt) -> [`docs/manifesto-v0.1.md`](docs/manifesto-v0.1.md)
- What must be true: [`docs/manifesto-v0.1.md`](docs/manifesto-v0.1.md) -> [`docs/requirements.md`](docs/requirements.md)
- How it is built: [`docs/requirements.md`](docs/requirements.md) -> [`docs/architecture-ga144.md`](docs/architecture-ga144.md)
- How it is verified: [`docs/architecture-ga144.md`](docs/architecture-ga144.md) + [`docs/requirements.md`](docs/requirements.md) -> [`docs/test-strategy.md`](docs/test-strategy.md)

`v0.1` completion gate:

- [`docs/manifesto-v0.1.md`](docs/manifesto-v0.1.md)
- [`docs/requirements.md`](docs/requirements.md)
- [`docs/architecture-ga144.md`](docs/architecture-ga144.md)
- [`docs/test-strategy.md`](docs/test-strategy.md)
