# Contributing

Thanks for helping improve this plugin. Contributions of new skills, better
instructions, fixes, and documentation are all welcome.

## Ways to contribute
- **Report a problem:** open an issue using the bug template. Include the skill name, the prompt you used, and what you expected.
- **Suggest a skill or improvement:** use the feature request template.
- **Submit a change:** fork, branch, edit, and open a pull request.

## Skill structure
Each skill lives in `skills/<skill-name>/` and must contain a `SKILL.md`:

```markdown
---
name: sdd-example            # must match the folder name; lowercase, hyphens
description: "What it does AND when to trigger it. Include the phrases users actually say."
---

# Title
Instructions in the imperative form...
```

Guidelines:
1. **Description is the trigger.** Put all "when to use" information in the description, and make it specific enough that Claude recognizes the situation. Quote the value in YAML because descriptions contain colons.
2. **Explain why, not only what.** Reasoned guidance generalizes better than rigid rules.
3. **Keep `SKILL.md` under ~500 lines.** Move long material to `references/` and point to it from `SKILL.md`.
4. **Keep the shared conventions:** canonical section numbers, `REQ-`/`DEC-`/`ASM-` IDs, and `[ASSUMPTION]`/`[TBD]` markers, so skills compose.
5. **Do not invent facts.** Skills must surface gaps rather than fabricate system details.
6. **Original content only.** Do not paste text from copyrighted sources; summarize ideas in your own words and attribute where appropriate.
7. **No malicious content.** Skills must not contain code or instructions that facilitate unauthorized access, data exfiltration, or deception.

## Local checks
```bash
pip install pyyaml
python scripts/validate.py
```
The script checks manifests, frontmatter, name/folder agreement, and that every skill is listed in the README. CI runs the same check on each push and pull request.

## Adding a skill: checklist
- [ ] Folder `skills/<name>/SKILL.md` with valid frontmatter
- [ ] Skill listed in the README tables
- [ ] Entry added under "Unreleased" in `CHANGELOG.md`
- [ ] `python scripts/validate.py` passes
- [ ] Tried at least two realistic prompts and noted results in the PR

## Commit and PR style
Short imperative commit messages ("Add rollback section to sdd-interface-design"). One logical change per PR. Describe what changed and why, and include before/after output if behavior changed.

## Code of conduct
By participating you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## License
Contributions are licensed under the project's [MIT License](LICENSE).
