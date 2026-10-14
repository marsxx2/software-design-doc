---
name: sdd-requirements-gathering
description: "Gather and structure the inputs needed before writing a software design document: functional and non-functional requirements, stakeholder expectations, technical constraints, existing system documentation, and open questions. Use at the very start of any design doc, tech spec, or architecture effort, when the user has vague or scattered notes, a PRD, tickets, or meeting transcripts to convert into requirements, or says 'what do I need before designing this?'"
---

# SDD: Requirements Gathering

Good designs start from a solid, shared understanding of what is needed. This skill turns raw material into structured, ID'd requirements and a list of what is still unknown.

## Workflow
1. **Collect sources.** Inventory and fully read whatever the user provides, including attached or uploaded files (check `/mnt/user-data/uploads/`): PRDs, specs, tickets, emails, meeting notes, existing docs, code. Attached material outranks short descriptions in the chat. If sources contradict each other or the user's message, list the conflicts and ask before continuing. If nothing is provided, interview the user, asking the highest-value questions first and only a few at a time.
2. **Extract requirements.** Separate:
   - Functional requirements (what the system does)
   - Non-functional requirements (performance, availability, security, scalability, accessibility, compliance, maintainability)
   - Constraints (tech stack, budget, timeline, legacy systems)
   - Stakeholder expectations and success metrics
3. **Normalize.** Rewrite each as a single, testable statement. Assign `REQ-###` IDs and a priority (Must/Should/Could). Note source and stakeholder.
4. **Surface gaps.** List ambiguities, conflicts between stakeholders, and missing non-functional targets as numbered open questions.
5. **Summarize existing system** (if any): what exists, what can be reused, known pain points.

## Output template

```markdown
# Requirements Brief: [Project]

## Stakeholders
| Name/Role | Interest | Key expectations |

## Functional requirements
| ID | Requirement | Priority | Source | Acceptance criterion |

## Non-functional requirements
| ID | Category | Target (measurable) | Source |

## Constraints
## Existing system summary
## Success metrics
## Open questions
| # | Question | Owner | Blocks |
```

## Guidance
- A requirement is testable if someone could write a pass/fail check for it. Rewrite vague ones ("easy to use") or move them to open questions.
- Record conflicts instead of silently choosing a side; stakeholders should resolve them.
- This output feeds `sdd-intro-overview` and the traceability matrix, so keep IDs stable once assigned.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
