---
name: sdd-data-design
description: "Write Section 3 (Data Design) of a software design document: database structure, data models, entity-relationship diagrams, data flow, validation and integrity rules, storage and retrieval strategy, retention and migration. Use whenever the user mentions schema, tables, data model, ERD, database design, data flow, validation rules, or how data is stored or retrieved in an SDD or tech spec."
---

# SDD: Data Design

Explain how information is modeled, stored, validated, and moved through the system.

## Workflow
1. List the core entities and their relationships (cardinality included).
2. Choose storage technology per data type (relational, document, cache, object store, search index) and justify it.
3. Define table/collection structure: fields, types, keys, indexes, constraints.
4. Describe data flows: where data enters, how it is transformed, where it is persisted, where it leaves.
5. Specify validation and integrity rules at each layer (client, API, database).
6. Cover access patterns, scalability (partitioning, replication), retention, backup, privacy/PII handling, and migration strategy.

## Output template

```markdown
# 3. Data Design

## 3.1 Data model overview
[ERD as Mermaid `erDiagram` or via sdd-diagram-generator.]

## 3.2 Storage choices
| Data | Store | Why |

## 3.3 Schema
### Table: `orders`
| Column | Type | Null | Key/Index | Notes |
Constraints: ...

## 3.4 Data flow
[Data flow diagram + numbered narrative from ingress to egress.]

## 3.5 Validation and integrity rules
| Field/entity | Rule | Enforced at |

## 3.6 Access patterns and performance
[Top read/write queries, the index that serves each one.]

## 3.7 Retention, backup, privacy, migration
```

## Guidance
- Design indexes from the real access patterns in 3.6, not by habit.
- State which layer is the source of truth for each rule; duplicated validation that disagrees is a classic bug source.
- Flag personal or regulated data (PII, PHI, payment) explicitly and link to the compliance items in Section 7.
- If the user has an existing schema, document it as-is first, then show proposed changes.

## Shared conventions (all SDD skills)

- **Source material first.** Before drafting anything, look for attached or uploaded files (check the conversation and `/mnt/user-data/uploads/`), linked docs, and pasted text. When the user says "this", "the attached", "this backend/project/spec", that material IS the subject. Read it fully, treat it as the source of truth, and take the system name, domain, terminology, stack, and requirements from it.
- **Stop on conflicts.** If the prompt's description disagrees with the source material (different domain, system, scale, or stack), do not silently follow either one. Stop and ask one short question that shows the discrepancy ("The attached spec describes a dental clinic system, but your message describes a URL shortener. Which should I design?"). A requested stack or number that the source material does not mention is a *proposal to confirm*, not a fact.
- **Match the language.** Write the document in the language of the source material or request. If the source material and the prompt use different languages, ask which language the document should be in. Keep identifiers, code, and standard names (FHIR, REST, SQL) in their original form; for right-to-left languages keep the structure and numbering unchanged.
- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
