---
name: sdd-system-architecture
description: "Write Section 2 (System Architecture) of a software design document: high-level architecture, major components and subsystems, architectural style and design patterns, key design decisions and trade-offs, deployment view. Use whenever the user asks to design, describe, or document a system's architecture, choose between monolith/microservices/serverless, justify architectural choices, or fill in the architecture part of an SDD or tech spec."
---

# SDD: System Architecture

Describe how the system is structured and why. The goal is that an engineer can find where any piece of functionality lives and understand the reasoning behind the shape.

## Workflow
1. Identify the major components/subsystems and the responsibility of each (one sentence each).
2. Map how they communicate: sync vs async, protocols, data ownership.
3. Name the architectural style and patterns (layered, event-driven, hexagonal, CQRS, etc.) and why they fit the requirements.
4. Record significant decisions with alternatives considered and trade-offs. Use `DEC-###` IDs.
5. Add a diagram. Use the `sdd-diagram-generator` skill when available; otherwise include a Mermaid block.
6. Cover cross-cutting concerns briefly: security, observability, scalability, resilience, deployment.

## Output template

```markdown
# 2. System Architecture

## 2.1 Architectural overview
[Paragraph + diagram.]

## 2.2 Components and subsystems
| Component | Responsibility | Owns data? | Talks to |
|-----------|----------------|------------|----------|

## 2.3 Architectural style and patterns
[Style, patterns, and the requirement each one serves.]

## 2.4 Key design decisions
### DEC-001: [Decision title]
- **Context:** ...
- **Options considered:** A, B, C
- **Decision:** ...
- **Trade-offs / consequences:** ...
- **Related requirements:** REQ-...

## 2.5 Cross-cutting concerns
Security · Observability · Scalability · Resilience · Deployment

## 2.6 Technology stack
| Layer | Choice | Rationale |
```

## Guidance
- A decision without a rejected alternative is usually not a decision yet; record at least one alternative and why it lost.
- Tie every major choice back to a requirement ID. Choices that serve no requirement are candidates for removal.
- Do not describe internal component logic here; that belongs in Section 5.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
