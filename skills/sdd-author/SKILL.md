---
name: sdd-author
description: "Orchestrates the full process of creating a software design document (SDD) end to end: gathers requirements, then drafts introduction, architecture, data, interface, component, UI, assumptions, and glossary sections with diagrams, traceability, and a stakeholder review pack. Use whenever the user wants to write, draft, or create a software design document, technical design doc, tech spec, architecture document, or system design for a new feature, service, or product, even if they only describe the system and don't say 'SDD'."
---

# SDD Author (orchestrator)

Drive the creation of a complete software design document by running the individual SDD skills in a sensible order, adapting depth to the size of the system.

## Step 0: Scope and depth
Ask (one compact question) or infer: system/feature name, size (small change / feature / new service / whole platform), audience, and delivery format. Choose:
- **Lightweight** (small change): Sections 1, 2, 4, 7 only.
- **Standard** (feature/service): all sections, moderate depth.
- **Comprehensive** (platform): all sections plus traceability, growth review, and walkthrough.

## Step 1: Requirements
Run `sdd-requirements-gathering`. Stop and resolve blocking open questions with the user before heavy design work; a design on unclear requirements is rework in waiting. If the user wants speed, proceed with explicit `[ASSUMPTION]` markers.

## Step 2: Draft the sections in dependency order
1. `sdd-intro-overview` (Section 1)
2. `sdd-system-architecture` (Section 2) with `sdd-diagram-generator`
3. `sdd-data-design` (Section 3)
4. `sdd-interface-design` (Section 4)
5. `sdd-component-design` (Section 5)
6. `sdd-ui-design` (Section 6), skip for back-end only systems
7. `sdd-assumptions-dependencies` (Section 7), harvested from all earlier sections
8. `sdd-glossary` (Section 8), built last from the complete text

Checkpoint with the user after Section 2; architecture is the cheapest place to course-correct.

## Step 3: Quality pass
- `sdd-traceability` (Appendices A and B)
- `sdd-future-growth-review` (standard/comprehensive)
- `sdd-style-consistency`

## Step 4: Review and publish
- `sdd-stakeholder-review` to create the review pack
- `sdd-walkthrough-script` if an async walkthrough will help
- `sdd-template-publisher` or a file-format skill (docx/pdf) to deliver in the requested format

## Assembling the document
Use `references/sdd-template.md` for the skeleton: document-control block, sections 1-8, appendices. Keep section numbering exactly as in the template. Deliver a single document; do not leave the user with eight fragments.

## Rules of engagement
- Do not invent system facts. Use `[ASSUMPTION]` and `[TBD]` markers and summarize them at the end as the open-items list.
- Be proportionate. A three-page design for a small feature beats a thirty-page one nobody reads.
- Finish with a short summary: what was produced, the top open questions, and the recommended next step.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
