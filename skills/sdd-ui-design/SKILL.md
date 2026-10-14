---
name: sdd-ui-design
description: "Write Section 6 (User Interface Design) of a software design document: screen inventory, wireframes or mockup descriptions, navigation, user workflows, interaction states, validation and error messages, responsive behavior, accessibility. Use whenever the user asks to document UI/UX in a design doc, describe user flows, specify screens, list accessibility requirements, or turn mockups into design specs."
---

# SDD: User Interface Design

Document how users interact with the system so engineering, design, and QA share one understanding of the experience.

## Workflow
1. Identify user roles and their top tasks.
2. Map each task to a workflow (step list or flow diagram), then to the screens involved.
3. For each screen: purpose, key elements, data shown, actions, states (empty, loading, error, success, disabled), and validation messages.
4. Define navigation structure and responsive behavior.
5. List accessibility requirements (WCAG 2.1 AA target unless told otherwise): keyboard navigation, focus order, contrast, labels, screen reader behavior, touch target size.
6. Link wireframes or mockups. If none exist, describe layout in structured text, or generate low-fidelity wireframes with the frontend/visual tools available.

## Output template

```markdown
# 6. User Interface Design

## 6.1 Users and primary tasks
| Role | Task | Frequency | Requirement |

## 6.2 Workflows
### Workflow: [name]
1. User ... → 2. System ...
[Flow diagram]

## 6.3 Screen inventory
| Screen | Purpose | Roles | Linked wireframe |

## 6.4 Screen specifications
### [Screen name]
- **Layout:** ...
- **Elements:** ...
- **Actions:** ...
- **States:** empty / loading / error / success
- **Validation & messages:** ...
- **Data source:** API from 4.3

## 6.5 Navigation and responsive behavior

## 6.6 Accessibility
[Checklist with pass criteria.]

## 6.7 Design system references
```

## Guidance
- Specify non-happy-path states. Empty, error, and loading screens are usually where UI specs are incomplete.
- Tie each screen's data to the API that supplies it so frontend and backend stay aligned.
- State accessibility as testable criteria ("all controls reachable by Tab, visible focus ring"), not intent.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
