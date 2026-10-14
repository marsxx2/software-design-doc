---
name: sdd-assumptions-dependencies
description: "Write Section 7 (Assumptions & Dependencies) of a software design document: technical assumptions, external libraries and services, hardware/software/infrastructure constraints, regulatory and compliance requirements, risks if assumptions fail. Use whenever the user asks about constraints, dependencies, risks, compliance, environment assumptions, or wants to harvest every [ASSUMPTION] marker from other SDD sections into one register."
---

# SDD: Assumptions & Dependencies

Make hidden premises visible. A design is only as sound as the assumptions it rests on, and unrecorded assumptions fail silently.

## Workflow
1. Collect every `[ASSUMPTION: ...]` marker already in the document and every dependency mentioned in Sections 2-6.
2. Add environment assumptions: runtime versions, cloud/provider, network, expected load, team skills.
3. List dependencies: libraries (with versions and licenses), external services and SLAs, internal teams or systems, data sources.
4. List constraints: hardware, budget, timeline, platform, legacy compatibility.
5. List regulatory/compliance items: privacy law, accessibility law, industry standards, data residency.
6. For each assumption, record how it will be validated, who owns that, and what happens to the design if it is false.

## Output template

```markdown
# 7. Assumptions & Dependencies

## 7.1 Technical assumptions
| ID | Assumption | Validation | Owner | Impact if false |
|----|-----------|------------|-------|-----------------|
| ASM-001 | ... | ... | ... | ... |

## 7.2 Dependencies
| Dependency | Type (lib/service/team/data) | Version/SLA | Risk | Fallback |

## 7.3 Constraints
Hardware · Software · Infrastructure · Budget · Timeline

## 7.4 Regulatory and compliance
| Requirement | Applies to | Design response |

## 7.5 Risk summary
[Top risks ranked by likelihood x impact.]
```

## Guidance
- The "impact if false" column is the most valuable one; if you cannot fill it in, the assumption may be load-bearing and deserves a validation task.
- Flag dependencies on a single vendor or unmaintained library as risks, with a fallback.
- Do not assert compliance conclusions as legal advice; list the obligations and recommend review by the appropriate specialist.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
