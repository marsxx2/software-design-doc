---
name: sdd-intro-overview
description: "Write Section 1 (Introduction & Overview) of a software design document: system description, objectives, key requirements, scope and non-goals, intended audience, document map, and background. Use whenever the user is starting a design doc, tech spec, or architecture doc, asks for a project summary, purpose statement, or scope section, or says 'start the SDD', even if they don't name the section."
---

# SDD: Introduction & Overview

The introduction sets the frame for every later section. A reader who stops after this page should know what is being built, why, for whom, and what is out of scope.

## Inputs to gather
Pull from attached files, the conversation, and any requirements brief, or ask once for the missing items: product/system name, problem being solved, target users, business or technical goals, known requirements, deadlines or constraints, and any prior art or existing system. If a requirements-gathering output (`sdd-requirements-gathering`) exists, use it instead of re-asking.

## Output template

```markdown
# 1. Introduction & Overview

## 1.1 Purpose of this document
[Why this document exists and what decisions it supports.]

## 1.2 Audience
[Who should read it and what each audience should take away: developers, PMs, QA, stakeholders.]

## 1.3 System description
[2-4 sentences: what the system is and does, in plain language.]

## 1.4 Objectives and key requirements
| ID | Objective / requirement | Priority |
|----|-------------------------|----------|
| REQ-001 | ... | Must |

## 1.5 Scope
**In scope:** ...
**Out of scope (non-goals):** ...

## 1.6 Background
[Context a new reader needs: existing systems, prior decisions, market or user drivers.]

## 1.7 Document overview
[One line per later section so readers can jump to what they need.]
```

## Guidance
- State non-goals explicitly. Scope disputes are the most common cause of a design drifting, and a written non-goal ends them early.
- Keep objectives measurable where possible ("p95 page load under 2s") rather than aspirational ("fast").
- Prioritize requirements (Must / Should / Could) so later trade-off discussions have an anchor.
- Keep it to roughly one page. Detail belongs in later sections.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
