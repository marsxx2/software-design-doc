---
name: sdd-glossary
description: "Write Section 8 (Glossary of Terms) of a software design document by extracting and defining technical terms, acronyms, domain jargon, and project-specific names from the document or notes provided. Use whenever the user asks for a glossary, wants acronyms defined, says the doc is hard for newcomers to read, or is finalizing an SDD, tech spec, or architecture doc."
---

# SDD: Glossary

A glossary lets mixed audiences (engineers, PMs, stakeholders) read the same document without a translator.

## Workflow
1. Scan the full document (or the provided text) for: acronyms, technical terms, domain-specific words, internal project/codenames, and words used with a special meaning.
2. Decide inclusion: include a term if a new team member or non-technical stakeholder could plausibly not know it. Skip universally known words.
3. Write each definition in one or two plain sentences that explain meaning in this project's context, not a textbook definition. Expand acronyms on first mention.
4. Flag terms used inconsistently in the document (two names for one thing, one name for two things) and propose a single standard.
5. Sort alphabetically.

## Output template

```markdown
# 8. Glossary

| Term | Definition | Section(s) |
|------|------------|-----------|
| API | Application Programming Interface: a defined way for programs to talk to each other. | 4 |
| Idempotency | Property of an operation that can be repeated safely with the same result. | 4.2 |
```

Then append a short **Terminology issues** list if inconsistencies were found.

## Guidance
- Link each term to the section where it matters so readers can jump to context.
- Never define a term using itself or another undefined term.
- Keep definitions neutral and stable; avoid including status or opinion.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
