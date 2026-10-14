---
name: sdd-future-growth-review
description: "Review a software design for scalability, extensibility, flexibility, and likely future change: load growth, new features, new platforms, tech debt, vendor lock-in, migration paths, and the points where the design would be expensive to change. Use whenever the user asks if a design will scale, wants a future-proofing or extensibility review, asks 'what happens when we 10x', plans a roadmap against an architecture, or is finalizing a design doc."
---

# SDD: Future Growth Review

Evaluate whether the design can evolve without costly rework, and make the growth assumptions explicit.

## Workflow
1. **Establish growth scenarios** with the user, or propose defaults and mark them as assumptions: 10x users/data/traffic, new region, new client platform, new major feature, new integration, team doubling, regulatory change.
2. **Walk the design** against each scenario and find the first thing that breaks or becomes expensive: single points of failure, shared databases, synchronous chains, hard-coded configuration, tight coupling, unbounded queries, per-tenant assumptions, schema rigidity.
3. **Assess extensibility:** are extension points (plugins, config, feature flags, versioned APIs, event hooks) in the right places? Is there anywhere a change would ripple across many components?
4. **Check lock-in and replaceability:** list vendor/library dependencies and how hard each would be to swap.
5. **Classify findings:** *Address now* (cheap now, costly later), *Plan for* (document trigger and approach), *Accept* (conscious trade-off, record in Decision Log).
6. **Avoid over-engineering.** For each recommendation, state the trigger that justifies it. Building for hypothetical scale with no trigger is its own cost.

## Output template

```markdown
# Future Growth Review

## Growth scenarios
| # | Scenario | Likelihood | Horizon | Source |

## Findings
| # | Scenario | Weak point | Impact | Recommendation | Classification | Trigger/threshold |

## Extensibility assessment
## Lock-in and replaceability
| Dependency | Replacement difficulty | Mitigation |

## Scaling plan summary
[What scales horizontally, what needs redesign, and at what load.]

## Decisions to record
[Items for the Decision Log.]
```

## Guidance
- Use numbers where possible (requests/s, GB/day, tenants). "Scales well" without a number is not a finding.
- Name the trigger ("when write throughput exceeds N/s, introduce partitioning") so future teams know when to act.
- Keep recommendations proportional; mark speculative ones clearly.

## Shared conventions (all SDD skills)

- Canonical section numbers: 1 Introduction & Overview, 2 System Architecture, 3 Data Design, 4 Interface Design, 5 Component Design, 6 User Interface Design, 7 Assumptions & Dependencies, 8 Glossary. Appendices: A Traceability Matrix, B Decision Log, C Open Questions. Keep these numbers so sections from different skills assemble cleanly.
- Mark anything you had to infer as `[ASSUMPTION: ...]` and anything missing as `[TBD: ...]`. Never invent facts about the user's system to make a section look complete; a visible gap is more useful to reviewers than a plausible fabrication.
- Give requirements stable IDs (`REQ-001`) and design decisions stable IDs (`DEC-001`) so they can be traced.
- Write in plain language. Define a term the first time it appears or add it to the glossary.
- Output Markdown by default so the section pastes into Confluence, Notion, or a repo. If the user asks for a Word doc, PDF, or Confluence page, use the matching skill or tool for that format after drafting.
