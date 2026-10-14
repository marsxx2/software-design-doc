---
name: sdd-template-publisher
description: "Create a reusable, standardized software design document template (blank and example-filled) and prepare it for a central location such as Confluence, Notion, a Git repo, or a Google/Word doc, with guidance text per section, document-control block, and ID conventions. Use whenever the user wants an SDD template, a standard format for design docs across teams or projects, wants to publish or store the doc centrally, or asks to convert an SDD into a Confluence page or repo markdown."
---

# SDD: Template & Publishing

Standardized structure makes design documents easier to write, review, and find.

## Workflow
1. Ask (or infer from context) the target platform: Confluence, Notion, Git repo (Markdown), Google Docs, Word. Also ask whether the org already has a template to align with.
2. Generate the template from `references/sdd-template.md` (bundled with this skill): document-control block, sections 1-8, appendices, each with brief guidance in blockquotes telling authors what belongs there and a short example.
3. Adapt to platform:
   - **Markdown/Git:** directory layout `docs/design/<feature>/sdd.md` + `diagrams/`; Mermaid for diagrams; PR-based review; README pointing to template.
   - **Confluence:** headings map to page sections, use a table of contents and status macro, one page per major section for large systems, labels (`sdd`, `design`, team), page properties for document control. Provide Markdown that pastes cleanly and list the macros to add manually.
   - **Notion/Docs:** database properties for status, owner, version, reviewers.
   - **Word/PDF:** use the docx/pdf skills to produce the file after drafting.
4. Provide a **filled example** for a small fictional system so authors see the expected depth.
5. Provide a **how to use** note: when an SDD is required, when a lighter one-page design is enough, naming and storage conventions, review and approval process.

## Output
- `sdd-template-blank.md` with guidance text
- `sdd-template-example.md` (optional)
- Adoption note: where it lives, naming convention, owner, and review workflow

## Guidance
- Make guidance text deletable: authors should remove it once the section is written.
- Include a "lightweight variant" (sections 1, 2, 4, 7 only) for small changes so the template is not skipped for being heavy.
- Store the template in one central, searchable place and link it from team onboarding.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
