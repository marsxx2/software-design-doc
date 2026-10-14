---
name: sdd-author
description: "Orchestrates the full process of creating a software design document (SDD) end to end: gathers requirements, then drafts introduction, architecture, data, interface, component, UI, assumptions, and glossary sections with diagrams, traceability, and a stakeholder review pack. Use whenever the user wants to write, draft, or create a software design document, technical design doc, tech spec, architecture document, or system design for a new feature, service, or product, even if they only describe the system and don't say 'SDD'."
---

# SDD Author (orchestrator)

Drive the creation of a complete software design document by running the individual SDD skills in a sensible order, adapting depth to the size of the system.

## Step 0: Inventory inputs and confirm the subject (do this first, always)
Before any drafting or questions:
1. **List every input.** Attached or uploaded files (check `/mnt/user-data/uploads/` as well as the conversation), linked docs, pasted text, code or repos, and the user's message. Long files that are not fully in context must be read in full with the file tools, not skimmed.
2. **Read the source material completely** and extract: system name, domain, purpose, users, scope, existing requirements, stack, standards, integrations, constraints, and the language it is written in.
3. **Determine the subject.** If the user says "this", "the attached", or "this backend/project", the attachment is the subject. If there is no attachment, the user's message is the subject.
4. **Run the conflict check.** Compare the message with the source material. If they describe different systems, domains, scales, or stacks, STOP and ask one short question that quotes both sides and asks which to design. Do not start drafting on a guess. Details in the message that the source material does not contain (a stack, a traffic number, a feature) are proposals; list them as `[ASSUMPTION]` and confirm them, never present them as established facts.
5. **State the plan in two lines** at the top of your reply before drafting: `Subject: <name>` and `Based on: <files / message>`, plus the document language. This lets the user catch a wrong subject immediately.

Then choose scope and depth. Ask (one compact question) or infer: size (small change / feature / new service / whole platform), audience, delivery format. Choose:
- **Lightweight** (small change): Sections 1, 2, 4, 7 only.
- **Standard** (feature/service): all sections, moderate depth.
- **Comprehensive** (platform): all sections plus traceability, growth review, and walkthrough.

### Source-document mode
When the user supplies an existing project description, PRD, or spec (as in "write the design doc for this"), the SDD is a *design derived from that document*, not a new invention:
- Reuse its terminology, entity names, standards, and integrations exactly; do not rename domain concepts.
- Convert its stated requirements into `REQ-###` entries and record the source section for each (for example "source: spec §4.2") so the traceability matrix can link back to it.
- Fill gaps with `[ASSUMPTION]` / `[TBD]`, and propose technology choices (frameworks, databases) only where the source is silent and the user asked for them; label them as proposals.
- Do not import details from unrelated documents or earlier examples in the conversation.

## Step 1: Requirements
Run `sdd-requirements-gathering` on the inputs inventoried in Step 0. Stop and resolve blocking open questions with the user before heavy design work; a design on unclear requirements is rework in waiting. If the user wants speed, proceed with explicit `[ASSUMPTION]` markers.

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

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
