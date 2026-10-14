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

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
