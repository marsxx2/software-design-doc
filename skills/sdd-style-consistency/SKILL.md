---
name: sdd-style-consistency
description: "Review and fix writing style, terminology, formatting, and structure of a software design document so it reads clearly and consistently: plain language, jargon control, consistent terms and headings, visuals where needed. Use whenever the user asks to proofread, polish, simplify, or standardize a design doc, tech spec, or architecture doc, or says it is confusing, inconsistent, or too jargon-heavy."
---

# SDD: Style & Consistency Review

Make the document easy to read, uniform, and unambiguous.

## Checks (run in order)
1. **Structure.** Sections follow the canonical numbering and each has the expected subsections. Heading levels do not skip. Section order matches the document overview.
2. **Terminology.** Build a term map: for each concept, find all names used. Pick one canonical name and replace the rest. Make sure canonical terms appear in the glossary.
3. **Plain language.** Flag long sentences (>30 words), nested clauses, passive voice hiding the actor, undefined jargon and acronyms, and filler ("basically", "simply", "obviously").
4. **Formatting.** Consistent heading case, list style, table layout, code block language tags, ID formats (`REQ-001`), date and number formats.
5. **Visuals.** Locate paragraphs that describe structure, flow, or relationships in prose and recommend a diagram (hand to `sdd-diagram-generator`). Check every diagram has a caption and is referenced in text.
6. **Voice and tone.** Present tense, active voice, direct statements ("The service validates the token") instead of hedges.
7. **Cross-references.** Section references and IDs resolve; no orphaned references.

## Output
Default to returning the corrected document plus a short change summary. If the user wants only a review, return a findings table instead:

```markdown
| # | Location | Issue type | Current | Suggested | Severity |
```

Then a summary: counts per issue type, the top 3 patterns, and the canonical term list.

## Guidance
- Preserve technical meaning. When a rewrite might change meaning, flag it for the author instead of guessing.
- Fix the root cause (e.g., one inconsistent term used 30 times) with one global recommendation, not 30 findings.
- Do not impose a style the doc's team has already standardized; follow the existing house style when there is one.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
