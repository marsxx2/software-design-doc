---
name: sdd-stakeholder-review
description: "Prepare a software design document for stakeholder review, manage the review cycle, consolidate feedback, track open questions and decisions, and record sign-off. Use whenever the user is about to share a design doc, tech spec, or architecture proposal, wants a review checklist, reviewer-specific questions, a feedback summary, an approval log, or asks 'how do I get buy-in on this design?'"
---

# SDD: Stakeholder Review

Reviews fail when reviewers do not know what is being asked of them. This skill sets up focused reviews and closes the loop on feedback.

## Phase A: Prepare the review
1. Read the draft. Produce a **review brief** (half page): what changed, the 3-5 decisions where feedback matters most, what is explicitly not up for debate, and the deadline.
2. Map reviewers to sections and write targeted questions per role:
   - Engineers: feasibility, complexity, missing failure modes
   - Product/PM: scope, requirement coverage, priorities
   - QA: testability, acceptance criteria
   - Security/compliance: threat surface, data handling
   - Ops/SRE: deployability, observability, runbooks
   - Design/UX: flows, states, accessibility
3. Run a pre-review readiness check: all sections present, no unresolved `[TBD]` in critical sections, diagrams render, glossary present. Report gaps before circulation.

## Phase B: Consolidate feedback
Cluster comments by section and theme. For each cluster record: the concern, the proposed change, and a disposition (Accept / Decline with reason / Needs discussion / Deferred).

## Phase C: Close out
Update the doc, add decisions to the Decision Log (Appendix B), and produce a sign-off record.

## Output templates

```markdown
## Review brief
**Purpose** · **Decisions needing input** · **Out of scope for feedback** · **Deadline** · **How to comment**

## Reviewer questions
| Reviewer | Sections | Questions |

## Feedback log
| # | Reviewer | Section | Comment | Disposition | Rationale | Doc change |

## Sign-off
| Name | Role | Decision (Approve / Approve with changes / Block) | Date | Conditions |
```

## Guidance
- Ask for specific input, not "any thoughts?". Targeted questions get far better feedback.
- Always record why a suggestion was declined; it prevents the same debate recurring.
- Do not mark the doc approved until blocking items have a recorded resolution.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
