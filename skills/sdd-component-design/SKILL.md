---
name: sdd-component-design
description: "Write Section 5 (Component Design) of a software design document: per-module purpose and responsibilities, inputs and outputs, algorithms and processing logic, internal data structures, dependencies, error cases. Use whenever the user wants low-level design, module or class specs, sequence diagrams for a component, algorithm descriptions, or detailed design of any individual service or module."
---

# SDD: Component Design

Provide enough detail per component that an engineer who did not attend the design discussions can implement it.

## Workflow
1. Take the component list from Section 2 and give each one a subsection. Skip trivial components with a one-line entry.
2. For each: purpose, responsibilities (and explicit non-responsibilities), public interface, inputs/outputs, key logic, internal data structures, dependencies, failure modes, and tests that prove it works.
3. For non-trivial behavior add a sequence or state diagram and pseudocode for the algorithm.
4. Note performance characteristics (complexity, expected load) where they matter.

## Output template (repeat per component)

```markdown
## 5.n [Component name]
**Purpose:** one sentence
**Responsibilities:** ...
**Not responsible for:** ...
**Requirements covered:** REQ-...

### Interface
| Operation | Inputs | Outputs | Errors |

### Processing logic
[Numbered steps or pseudocode. Include sequence/state diagram if flow is non-trivial.]

### Data structures and algorithms
[Choice + complexity + why.]

### Dependencies
[Internal components, libraries, external services.]

### Failure modes and handling
| Failure | Detection | Response |

### Test considerations
[What unit/integration tests must demonstrate.]
```

## Guidance
- Writing "not responsible for" prevents overlapping ownership between components, a common source of duplicate logic.
- Prefer pseudocode that mirrors the intended control flow over prose paragraphs; it is easier to review and to implement.
- Keep component interfaces consistent with Section 4. If they diverge, fix the source of truth rather than documenting both.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
