# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/).

## [1.0.1] - 2026-10-14

### Fixed
- `sdd-author` ignored attached or uploaded files and designed whatever the prompt text described. It now begins with an input inventory, treats attachments as the source of truth, and states `Subject:` / `Based on:` before drafting.
- No check existed for a prompt that contradicts the attachment. All skills now stop and ask which to follow when the two disagree.
- Requirements stated only in the prompt (stack, traffic numbers) are now treated as proposals to confirm when the source material does not contain them.

### Added
- Source-document mode in `sdd-author` for deriving an SDD from an existing spec, preserving its terminology and linking each `REQ-` to its source section.
- Language rule: match the language of the source material, and ask when inputs are in different languages.
- `sdd-reviewer` and `sdd-requirements-gathering` now look for uploaded files.
- `tests/regression-prompts.md`.

### Changed
- README examples use placeholders instead of a concrete fictional system, with a warning not to paste them verbatim. Added a workflow for turning an existing spec into an SDD and troubleshooting rows for wrong-system and wrong-language output.

## [1.0.0] - 2026-10-14

### Added
- Orchestrator skills: `sdd-author`, `sdd-reviewer`.
- Section skills: `sdd-intro-overview`, `sdd-system-architecture`, `sdd-data-design`,
  `sdd-interface-design`, `sdd-component-design`, `sdd-ui-design`,
  `sdd-assumptions-dependencies`, `sdd-glossary`.
- Process skills: `sdd-requirements-gathering`, `sdd-stakeholder-review`,
  `sdd-style-consistency`, `sdd-diagram-generator`, `sdd-traceability`,
  `sdd-future-growth-review`, `sdd-doc-maintenance`, `sdd-walkthrough-script`,
  `sdd-template-publisher`.
- Shared SDD template and review checklist reference files.
- Plugin manifest, marketplace manifest, validation script, CI workflow.
