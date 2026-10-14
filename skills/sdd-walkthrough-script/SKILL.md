---
name: sdd-walkthrough-script
description: "Write a concise script, outline, and slide or screen-share plan for a short asynchronous video walkthrough (such as a Loom recording) of a software design document, covering diagrams, key decisions, and trade-offs so reviewers understand intent before reading. Use whenever the user wants to record, present, or narrate a design doc, prepare a design review talk, explain an architecture to reviewers, or reduce back-and-forth during review."
---

# SDD: Walkthrough Script

A 5-10 minute recorded walkthrough conveys the intent behind a design far faster than text alone, and reduces review back-and-forth.

## Workflow
1. Read the SDD and identify the audience (engineers, execs, cross-team) and the desired outcome (approval, feedback on X, awareness).
2. Choose 3-5 key messages: the problem, the core idea, the riskiest decisions with trade-offs, what feedback is needed.
3. Select the visuals to show (usually the context diagram, one detail diagram, one sequence flow, the decision table) and specify exactly what to point at.
4. Write a spoken-language script with timing. Keep sentences short and conversational; avoid reading the document aloud.
5. End with explicit asks and a deadline.

## Output template

```markdown
# Walkthrough: [Doc title] (target length: ~7 min)

**Audience:** ... **Goal:** ... **Feedback wanted on:** 1) ... 2) ...

## Run sheet
| Time | Screen to show | Say (key points) |
|------|----------------|------------------|
| 0:00-0:30 | Doc title / summary | Hook: what problem, why now |
| 0:30-2:00 | Context diagram | Walk left to right, name main components |
| 2:00-4:30 | Decision DEC-003 + sequence diagram | Option A vs B, why chosen, risk |
| 4:30-6:00 | Open questions | Where I need input |
| 6:00-6:30 | Closing | Ask, deadline, where to comment |

## Full script
[Spoken text per segment.]

## Recording tips
- Zoom in on diagrams; close unrelated tabs.
- Say what you're pointing at.
- Put timestamps in the video description matching the run sheet.

## Companion written summary
[3-5 bullet recap + link to the doc, to post with the video.]
```

## Guidance
- Front-load the conclusion; reviewers who stop watching at 2 minutes should still know the proposal.
- Name the trade-offs honestly; walkthroughs that hide weaknesses invite harsher reviews later.
- If asked, produce captions-ready text (short lines) from the script.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
