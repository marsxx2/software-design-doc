# software-design-doc

[![Validate](https://github.com/marsxx2/software-design-doc/actions/workflows/validate.yml/badge.svg)](https://github.com/marsxx2/software-design-doc/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Claude plugin that helps you **create, review, and maintain software design documents (SDDs)**. It contains 19 skills: two orchestrators, eight section writers, and nine process and best-practice helpers. The structure follows the sections and best practices described in Atlassian's guide to software design documents (see [Attribution](#attribution-and-disclaimer)).

- [What you get](#what-you-get)
- [Installation](#installation)
- [How to use it](#how-to-use-it)
- [Prompt cookbook](#prompt-cookbook)
- [Tips for better results](#tips-for-better-results)
- [Troubleshooting](#troubleshooting)
- [Repository layout](#repository-layout)
- [Contributing](#contributing) · [License](#license) · [Attribution](#attribution-and-disclaimer)

## What you get

### Orchestrators
| Skill | Use it to |
|-------|-----------|
| `sdd-author` | Create a full SDD end to end: requirements, all sections, diagrams, traceability, review pack |
| `sdd-reviewer` | Audit an existing design doc and get a scored, prioritized report |

### Section skills
| Skill | Section produced |
|-------|------------------|
| `sdd-intro-overview` | 1. Introduction & Overview |
| `sdd-system-architecture` | 2. System Architecture |
| `sdd-data-design` | 3. Data Design |
| `sdd-interface-design` | 4. Interface Design |
| `sdd-component-design` | 5. Component Design |
| `sdd-ui-design` | 6. User Interface Design |
| `sdd-assumptions-dependencies` | 7. Assumptions & Dependencies |
| `sdd-glossary` | 8. Glossary |

### Process and best-practice skills
| Skill | Purpose |
|-------|---------|
| `sdd-requirements-gathering` | Turn scattered notes into structured, ID'd requirements and open questions |
| `sdd-stakeholder-review` | Prepare a review, consolidate feedback, record sign-off |
| `sdd-style-consistency` | Plain language, consistent terminology and formatting |
| `sdd-diagram-generator` | Mermaid/SVG architecture, ER, sequence, data flow, and state diagrams |
| `sdd-traceability` | Requirements traceability matrix and decision log |
| `sdd-future-growth-review` | Scalability, extensibility, and lock-in review |
| `sdd-doc-maintenance` | Keep the doc current: staleness report, changelog, versioning |
| `sdd-walkthrough-script` | Script and run sheet for an async video walkthrough (e.g., Loom) |
| `sdd-template-publisher` | Reusable templates for Confluence, Git, Notion, Docs, Word |

### Conventions shared by every skill
- **Fixed section numbering** (1 to 8, plus Appendices A to C), so sections drafted separately assemble into one document.
- **Stable IDs:** `REQ-###` requirements, `DEC-###` decisions, `ASM-###` assumptions.
- **Visible gaps:** inferred facts are marked `[ASSUMPTION: ...]` and missing facts `[TBD: ...]`. The skills are instructed not to invent details about your system.
- **Markdown by default**, so output pastes into Confluence, Notion, or a repo. Ask for Word or PDF and Claude will use the appropriate format skill.

## Installation

Pick the option that matches where you use Claude. Menu names and commands can change between releases; check the current Claude documentation if something differs.

### Option A: Claude Code, from GitHub (recommended)
```
/plugin marketplace add marsxx2/software-design-doc
/plugin install software-design-doc@software-design-doc
```
(The repository includes a `.claude-plugin/marketplace.json`, so the repo itself acts as a one-plugin marketplace.)

### Option B: Claude Code, from a local clone
```bash
git clone https://github.com/marsxx2/software-design-doc.git
claude --plugin-dir ./software-design-doc
```

### Option C: Claude.ai or the desktop app, as individual skills
Plugins are not installed there, but each skill works on its own.
1. Build upload-ready files: `./scripts/package-skills.sh` (creates one `.zip` per skill in `dist/`).
2. In Claude, open **Settings → Capabilities → Skills** and upload the zips you want. Upload at least `sdd-author` or `sdd-reviewer` plus the skills they call.

Note: the orchestrators hand off to other skills by name, so they work best when the full set is installed.

## How to use it

There are three ways to invoke the skills, from most hands-off to most explicit.

### 1. Just describe the job (auto-trigger)
Each skill's description lists the situations it covers, so a natural request normally activates the right skill:

```
Write a design doc for <your system>. Key needs: <3-5 requirements>.
Scale: <numbers>. Stack: <technologies>.
```
```
Write a design doc based on the attached <file name>.
```
```
Here is our tech spec [paste or attach]. Is it ready for review?
```

> **Use your own details.** Examples in this README (URL shortener, order management, payments API, and so on) are fictional. If you copy one verbatim, Claude will design *that* system. When you attach a file, say so ("based on the attached ...") and do not paste example requirements for a different system. If your message and your attachment disagree, the skills stop and ask which one is correct.

### 2. Name the skill
Naming the skill is the most reliable method, especially for the narrower ones:

```
Use sdd-data-design to write the data design section for an order
management system with orders, customers, and inventory.
```

### 3. Slash invocation (Claude Code)
Plugin skills are namespaced by plugin name. Type `/` to browse, or call one directly:
```
/software-design-doc:sdd-author write the design doc for <your system> based on the attached <file>
```

### Common workflows

**A. Create a new design doc**
1. Start with context: system name, users, scale, stack, constraints, deadlines, and attach or link any PRD, spec, tickets, or code. Attached material is treated as the source of truth.
2. Ask: `Use sdd-author to create a standard-depth SDD for <system>.`
3. Answer the clarifying questions. `sdd-author` first runs `sdd-requirements-gathering`, then drafts sections 1 to 8.
4. Review the architecture checkpoint after Section 2 and correct course there. It is the cheapest place to change direction.
5. Ask for the quality pass: traceability, future-growth review, style check.
6. Ask for the delivery format: Markdown, Confluence-ready, Word, or PDF.

**B. Review an existing doc**
1. Paste or attach the doc.
2. Ask: `Use sdd-reviewer on this doc.`
3. You get a readiness verdict, a 1 to 5 scorecard across nine dimensions, severity-ranked findings (Blocker / Major / Minor), and the top fixes.
4. Follow up with targeted skills (for example `sdd-traceability` for coverage gaps).

**C. Keep a doc current**
```
Our API moved from REST to gRPC for the order service. Use sdd-doc-maintenance
to find what's stale in the design doc, update it, and add a changelog entry.
```

**D. Small change, small doc**
```
Use sdd-author in lightweight mode for adding rate limiting to our public API.
```
Lightweight mode covers Sections 1, 2, 4, and 7 only.

**E. Get buy-in**
```
Use sdd-stakeholder-review to build a review pack for this doc, then use
sdd-walkthrough-script to write a 7-minute Loom script.
```

**F. Standardize across a team**
```
Use sdd-template-publisher to create a Confluence-ready SDD template with
guidance text, plus a lightweight variant.
```

**G. Turn an existing spec or project description into an SDD**
```
Use sdd-author to write the software design document based on the attached
project-description.md. Write it in the same language as the attachment.
Propose a technology stack only where the spec is silent.
```
`sdd-author` begins by stating `Subject:` and `Based on:` so you can confirm it picked up the right file. It reuses the spec's terminology, converts its requirements into `REQ-` IDs with a source reference back to the spec, and marks anything it had to infer. If you add a stack or traffic target in the same message, it treats those as proposals to confirm, not facts from the spec.

### Depth levels for `sdd-author`
| Level | Sections | Use for |
|-------|----------|---------|
| Lightweight | 1, 2, 4, 7 | Small changes and spikes |
| Standard (default) | 1 to 8 | New features and services |
| Comprehensive | 1 to 8 + traceability, growth review, walkthrough | Platforms, high-risk or cross-team systems |

## Prompt cookbook

| Goal | Example prompt |
|------|----------------|
| Structure messy inputs | `Use sdd-requirements-gathering on these meeting notes: [paste]` |
| Write the intro | `Write the introduction and scope for our billing migration, including non-goals` |
| Document architecture | `Use sdd-system-architecture. We're choosing between a modular monolith and microservices; record the trade-offs` |
| Model data | `Design the schema and data flow for multi-tenant document storage, with PII handling` |
| Specify APIs | `Use sdd-interface-design for the payments API: endpoints, error model, auth, idempotency` |
| Detail a module | `Write the component design for the retry scheduler, with a sequence diagram` |
| Specify screens | `Use sdd-ui-design for the onboarding flow including empty, loading, and error states and WCAG AA criteria` |
| Capture risks | `Collect every assumption in this doc into a register with impact-if-false` |
| Build a glossary | `Generate the glossary and flag inconsistent terms` |
| Draw diagrams | `Make a Mermaid sequence diagram of checkout`; `Make an ERD from this schema` |
| Check coverage | `Use sdd-traceability and tell me which requirements have no design coverage` |
| Stress-test scale | `Run sdd-future-growth-review: what breaks at 10x traffic and what are the triggers to act?` |
| Polish | `Run sdd-style-consistency; keep technical meaning but cut jargon` |
| Impact analysis | `If we drop requirement REQ-014, what design elements and tests are affected?` |

## Tips for better results

- **Give context up front.** Anything missing becomes an `[ASSUMPTION]` or `[TBD]`, which you then have to resolve.
- **Say what the attachment is.** Write "based on the attached <file>" rather than "this backend" alone, and keep requirements in the prompt consistent with the file.
- **Attach real artifacts.** Existing schemas, OpenAPI files, PRDs, tickets, and code let the skills document what exists rather than guess.
- **State the audience and goal.** "For execs who need to approve budget" and "for the engineers who will build it" yield different emphasis.
- **Work in stages.** Draft, then review, then run traceability, then publish. Each turn is easier to correct than one giant request.
- **Resolve the open-items list.** `sdd-author` ends with the top open questions; answering them and re-running a section is faster than editing by hand.
- **Specify output format early** (Markdown, Confluence, Word, PDF) so you don't have to reformat later.
- **Treat output as a draft.** The skills structure and accelerate the work; your team still owns technical correctness, security review, and compliance decisions.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| A skill didn't trigger | Name it in the prompt (`Use sdd-...`) or use the slash form in Claude Code |
| Orchestrator skips a sub-skill | Install the full plugin; in claude.ai upload every skill the orchestrator calls |
| Output is about the wrong system | You probably pasted example text from this README, or your message contradicts your attachment. Re-run with "based on the attached <file>" and your own details. Update to plugin 1.0.1 or later, which asks when they conflict |
| Output is in the wrong language | State the language you want ("write it in Persian" / "in English"); with mixed-language inputs the skills ask |
| Output is generic | Add concrete context: scale numbers, stack, constraints, existing docs |
| Document is too long | Request lightweight mode or name only the sections you need |
| Mermaid diagram won't render | Wrap labels with special characters in quotes; ask for SVG instead |
| Plugin commands differ from this README | Claude's plugin interface evolves; check the current official docs |

## Repository layout

```
.
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # lets the repo act as a marketplace
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md         # frontmatter (name, description) + instructions
│       └── references/      # optional supporting files
├── scripts/
│   ├── validate.py          # structure and metadata checks (used by CI)
│   └── package-skills.sh    # zips each skill for claude.ai upload
├── tests/
│   └── regression-prompts.md  # prompts with expected behavior, run after editing skills
├── .github/                 # CI workflow, issue and PR templates
├── CHANGELOG.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md  SECURITY.md  LICENSE
└── README.md
```

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve a skill, and run `python scripts/validate.py` before opening a PR.

## License

Released under the [MIT License](LICENSE).

## Attribution and disclaimer

The section structure and best practices were informed by Atlassian's public article "Software Design Document [Tips & Best Practices]". All skill text in this repository is original. This project is independent and is not affiliated with, endorsed by, or sponsored by Atlassian or Anthropic. Product and company names are trademarks of their respective owners.
