---
name: sdd-interface-design
description: "Write Section 4 (Interface Design) of a software design document: internal module interfaces, external APIs and integrations, protocols, endpoint specs, message formats, error and exception handling, authentication and security. Use whenever the user asks about API design or documentation, REST/GraphQL/gRPC contracts, event or message schemas, third-party integrations, error handling conventions, or authN/authZ in a design doc."
---

# SDD: Interface Design

Define every boundary across which the system communicates, so teams can build both sides in parallel.

## Workflow
1. Inventory interfaces: internal (module to module), external exposed (public/partner APIs), external consumed (third-party services), and events/queues.
2. For each, choose protocol and style (REST, GraphQL, gRPC, WebSocket, message bus) and justify.
3. Specify contracts: endpoints/operations, request and response shapes, status codes, versioning, pagination, idempotency, rate limits.
4. Define a single error model used everywhere (code, message, details, correlation ID) and the retry/timeout behavior.
5. Define authentication, authorization, and transport security per interface.

## Output template

```markdown
# 4. Interface Design

## 4.1 Interface inventory
| ID | Interface | Type | Consumer | Provider | Protocol |

## 4.2 API conventions
Versioning · Pagination · Idempotency · Rate limiting · Naming

## 4.3 Endpoint / operation specs
### POST /v1/orders
- **Purpose:** ...
- **Auth:** ...
- **Request:** ```json { ... } ```
- **Response 201:** ```json { ... } ```
- **Errors:** 400 validation_failed, 401, 409 conflict, ...
- **Requirement:** REQ-...

## 4.4 Events and messages
| Event | Producer | Consumers | Schema | Delivery guarantee |

## 4.5 Error handling
[Error envelope, error code catalogue, retry and timeout policy.]

## 4.6 Security and authentication
[AuthN method, scopes/roles, token lifetime, transport encryption, input sanitization.]

## 4.7 Third-party integrations
| Service | Purpose | Failure behavior | Fallback |
```

## Guidance
- Show at least one concrete request/response example per interface; examples expose ambiguity that prose hides.
- Specify what happens when the dependency is down. Integration failure behavior is where designs are usually silent and production is not.
- Keep versioning and backward-compatibility rules explicit, since they constrain every later change.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
