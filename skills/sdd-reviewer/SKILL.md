---
name: sdd-reviewer
description: "Audits an existing software design document against best practices: completeness of the eight core sections, clarity, consistency, traceability, growth readiness, and visuals, and returns a scored report with prioritized fixes. Use whenever the user shares a design doc, tech spec, RFC, or architecture document and asks for a review, critique, quality check, gap analysis, or 'is this ready for review?'"
---

# SDD Reviewer (orchestrator)

Review an existing design document and report what to fix, in priority order.

## Workflow
1. **Read the whole document** first. Identify type (SDD, RFC, ADR, spec) and map its sections to the canonical eight.
2. **Completeness check.** For each canonical section, mark: Present & strong / Present but thin / Missing. Use the criteria in `references/review-checklist.md`.
3. **Run the focused audits** (apply their logic inline, or invoke the skills):
   - Style and terminology: `sdd-style-consistency`
   - Requirements-to-design coverage and decision rationale: `sdd-traceability`
   - Scalability and extensibility: `sdd-future-growth-review`
   - Staleness vs code/tickets if provided: `sdd-doc-maintenance`
   - Missing or weak diagrams: `sdd-diagram-generator`
4. **Score and prioritize.** Score each dimension 1-5 (see checklist). Classify findings: **Blocker** (design cannot be implemented or approved), **Major** (likely rework or confusion), **Minor** (polish).
5. **Report.** Do not rewrite the document unless asked; deliver the review.

## Report template

```markdown
# SDD Review: [Title]

**Overall readiness:** Ready / Ready with changes / Not ready
**Summary (3 sentences):** ...

## Scorecard
| Dimension | Score (1-5) | Note |
|-----------|-------------|------|
| Completeness | | |
| Clarity & plain language | | |
| Consistency | | |
| Architecture soundness & rationale | | |
| Interfaces & data specificity | | |
| Traceability | | |
| Risks, assumptions & dependencies | | |
| Growth & maintainability | | |
| Visuals | | |

## Findings
| # | Severity | Section | Finding | Why it matters | Suggested fix |

## Top 5 fixes
## Strengths worth keeping
## Questions for the author
```

## Guidance
- Lead with the verdict and the top fixes; reviewers are busy.
- Criticize the document, not the author, and acknowledge real strengths.
- Say what you could not verify (no code access, no requirements source) instead of implying coverage you did not do.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
