---
name: sdd-traceability
description: "Build and audit a traceability matrix for a software design document, linking requirements to design decisions, components, interfaces, data entities, tests, and implementation tasks so the reasoning behind every choice is clear and coverage gaps are visible. Use whenever the user asks 'why did we decide this', wants requirements coverage, a requirements traceability matrix (RTM), decision log, impact analysis for a change, or an audit of orphaned requirements or unjustified design elements."
---

# SDD: Traceability

Traceability answers two questions: *is every requirement covered by the design?* and *does every design element exist for a reason?*

## Workflow
1. **Inventory IDs.** Extract all `REQ-`, `DEC-`, `ASM-` IDs and all design elements (components, endpoints, tables, screens) from the document. Assign IDs to elements that lack them (`CMP-`, `API-`, `TBL-`, `UI-`).
2. **Link.** For each requirement, find the decisions, components, interfaces, data entities, and UI screens that satisfy it. Add test IDs and ticket links if the user provides them.
3. **Audit.**
   - *Uncovered requirements*: REQ with no design element.
   - *Orphan design elements*: element linked to no requirement (candidate gold-plating or missing requirement).
   - *Decisions without rationale or alternatives*.
   - *Requirements without a test or acceptance criterion*.
4. **Report** coverage percentages and the specific gaps.
5. **Decision log.** Maintain Appendix B so each `DEC-###` records context, decision, rationale, status (Proposed/Accepted/Superseded), and the date and owner.

## Output templates

```markdown
# Appendix A: Traceability Matrix
| Requirement | Decision(s) | Component(s) | Interface(s) | Data | UI | Test(s) | Status |
|-------------|-------------|--------------|--------------|------|----|---------|--------|
| REQ-001 | DEC-003 | CMP-Orders | API-012 | TBL-orders | UI-04 | TC-101 | Covered |

# Appendix B: Decision Log
| ID | Title | Status | Date | Owner | Rationale | Supersedes |

## Coverage report
- Requirements covered: X / Y (Z%)
- Uncovered: REQ-...
- Orphan elements: ...
- Missing tests: ...
```

## Impact analysis mode
When the user proposes a change to a requirement or component, walk the matrix both directions and list every affected decision, component, interface, test, and UI element.

## Guidance
- Keep the matrix generated from the document, not hand-maintained, so it does not drift. Re-run after edits.
- Orphans are not always wrong (infrastructure often serves no single requirement); mark those as "cross-cutting" with a reason.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
