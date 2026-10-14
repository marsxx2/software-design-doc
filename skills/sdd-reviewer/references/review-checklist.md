# SDD Review Checklist

Score each dimension 1 (absent/poor) to 5 (excellent).

## Completeness
- All eight core sections present; appendices for traceability, decisions, open questions.
- No unresolved `[TBD]` in sections 2-5.
- 5 = every section substantive and consistent with the others; 1 = multiple sections missing.

## Clarity & plain language
- A new team member can follow it without a guide; jargon defined; sentences direct.
- Audience and purpose stated up front.

## Consistency
- Same names for same concepts; consistent IDs, headings, formats.
- Interfaces in Section 4 match component interfaces in Section 5 and UI data sources in Section 6.

## Architecture soundness & rationale
- Components have clear single responsibilities; communication paths explicit.
- Each major decision has alternatives and trade-offs; decisions trace to requirements.
- Cross-cutting concerns addressed: security, observability, resilience, deployment.

## Interfaces & data specificity
- Concrete request/response examples; error model defined; versioning and auth specified.
- Schema with keys, indexes, constraints; validation rules and layer of enforcement; PII handling.

## Traceability
- Every requirement maps to design elements and tests; no orphan elements without reason.
- Decision log maintained.

## Risks, assumptions & dependencies
- Assumptions have validation and impact-if-false; dependencies have fallbacks; compliance listed.

## Growth & maintainability
- Scaling limits and triggers named; extension points identified; lock-in understood.
- Ownership and review cadence for keeping the doc current.

## Visuals
- Architecture, data flow/ERD, and at least one sequence for the critical path; captions and legends present.

## Severity definitions
- **Blocker:** prevents implementation or approval (missing requirement coverage, contradictory interfaces, unaddressed critical risk).
- **Major:** likely to cause rework or misunderstanding.
- **Minor:** polish, style, small gaps.

## Readiness verdict
- **Ready:** no blockers, at most a few majors.
- **Ready with changes:** no blockers, several majors with clear fixes.
- **Not ready:** any blocker, or widespread thinness.
