---
name: sdd-doc-maintenance
description: "Keep a software design document current as the project evolves: detect stale or contradicted sections by comparing against code, tickets, or change notes, update affected sections, bump versions, maintain a changelog, and set review cadence. Use whenever the user says the design doc is outdated, a feature or architecture changed, asks to sync docs with code, wants a changelog or version history, or asks how to keep documentation up to date."
---

# SDD: Documentation Maintenance

Documentation that drifts from reality is worse than none, because readers trust it. This skill keeps the SDD accurate with small, regular updates.

## Workflow
1. **Collect change signals.** Ask for or inspect: merged PRs, changed code/config/schema/API specs, closed tickets, incident reports, decision records, release notes. If a repo is available, diff the relevant areas.
2. **Map changes to sections.** Use this guide:
   - New/removed service or dependency → Sections 2, 7, diagrams
   - Schema/migration → Section 3
   - API/event change → Section 4
   - Logic/algorithm change → Section 5
   - UI change → Section 6
   - New constraint/assumption invalidated → Section 7
3. **Detect staleness.** Flag statements contradicted by the current code or tickets, references to removed components, outdated diagrams, and `[TBD]` items past their date.
4. **Update.** Edit affected sections minimally, update diagrams (via `sdd-diagram-generator`), and refresh the traceability matrix (via `sdd-traceability`).
5. **Record.** Add a changelog entry and bump the version.
6. **Set cadence.** Recommend review triggers (every release, every quarter, after any incident) and an owner per section.

## Output template

```markdown
## Document control
| Version | Date | Author | Summary of changes | Sections affected |

## Staleness report
| Section | Statement | Evidence it is stale | Proposed update | Confidence |

## Maintenance plan
| Section | Owner | Review trigger | Last reviewed |
```

Versioning guidance: major for architecture or scope changes, minor for new or changed components/interfaces, patch for clarifications.

## Guidance
- Prefer linking to the source of truth (OpenAPI file, schema migrations) over copying details that will rot.
- When code and doc disagree, ask which is correct before editing; sometimes the code is the bug.
- Keep a visible "Last reviewed" date near the top so readers can judge freshness.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
