# Academic Scoring, Venue Positioning, and Gate

## One academic score, no utility score

Assign one integer Academic Potential score from 1 to 10. Explain novelty, academic significance, and prospective contribution depth separately, then choose an overall anchored judgment. Do not mechanically average dimensions or treat maturity as a dimension. This score is an editorial estimate, not a calibrated measurement.

| Score | Anchor |
|---|---|
| 1 | Central premise contradicted or exact contribution already established with no meaningful remaining research question |
| 2 | Negligible conceptual difference or academic contribution |
| 3 | Small extension with limited new understanding |
| 4 | Identifiable contribution, but differentiation or significance is weak |
| 5 | Plausible incremental contribution with a mixed academic case |
| 6 | Clear, worthwhile contribution with credible potential for a focused scholarly paper |
| 7 | Strong, nontrivial contribution to an important question |
| 8 | Compelling advance with substantial depth or influence beyond the immediate setting |
| 9 | Exceptional prospective contribution that could reshape an important research direction |
| 10 | Rare, potentially foundational advance with exceptionally strong conceptual positioning; never claim future impact is established |

Attach low/medium/high confidence based on source relevance, coverage, and clarity of the claimed contribution. Confidence is not implementation completeness. A strong open question can score highly without the user's own results. A claimed mechanism must still have an articulated rationale; do not score purely on imagined benefits if everything succeeds.

Give a reason in at most 50 words, the largest upward/downward driver, and a source-backed comparison when possible. Avoid false precision such as 7.83. Report “Not assessable” only when an essential basis is genuinely missing; do not force missing evidence into score 1 or 5.

## Venue positioning

Aim to identify 3 conferences and 1 journal when the domain supports this; use fewer rather than pad. Use current official scopes, tracks, calls, and ranking editions. Verify CCF classifications where relevant. Do not claim cross-domain equivalence without justification.

For each venue provide fit, relevant track, conceptual positioning (stretch / plausible target / more conservative target), contribution-specific evidence obligations, official citations, and uncertainty. Labels describe relative academic ambition, never guaranteed acceptance. Distinguish topic mismatch from insufficient contribution strength.

There is no fixed score-to-venue mapping: 6/10 does not automatically equal CCF-B, and 8/10 does not imply ICLR acceptance. Explain how this particular contribution fits this particular venue. A specialized venue can suit an excellent idea better than a broad prestigious one.

Evaluate venue potential conditional on competent completion of normal research obligations. Missing future experiments, proofs, or writing do not by themselves invalidate fit. Name those obligations separately. Do not claim that a merely imagined breakthrough makes any venue attainable.

Do not invent personalized acceptance percentages. Official historical rates, if relevant, require year, track, source, and denominator where available; label them historical, not this idea's probability.

## GO / NO-GO

The gate means “passes the user's stated academic screen,” not “is personally useful.” Never produce a utility score, ROI verdict, or personal investment recommendation.

Policy fields: minimum score (optional integer 1–10); mandatory venue criteria (optional explicit logical condition); preferred venues (nonbinding). At least one binding criterion is required to compute a gate. Use AND across binding criteria unless the user explicitly specifies otherwise. Record exact user wording as well as the normalized policy. Confidence is descriptive unless the user explicitly makes it a requirement.

- GO: all binding academic criteria are met on the available assessment.
- NO-GO: at least one binding criterion is demonstrably not met. List the failed criterion and evidence; do not claim the topic is universally worthless.
- No invented third verdict: when no policy exists, set gate=null and status=awaiting_policy. When a required assessment cannot be made, set gate=null and status=incomplete. These are process states, not merit verdicts. Complete all other useful work first.

For mandatory venue conditions, use met/not_met/unknown. Unknown does not automatically mean NO-GO. If one binding criterion fails, NO-GO is justified even if another is unknown; otherwise unresolved binding criteria leave the gate pending.

Changing the user's workload or threshold only recomputes the gate; it must not retroactively change the academic score. Changing the idea or substantive evidence can change the score and requires a new assessment revision. Preserve both historical results.

Examples: score 6 with minimum 7 gives NO-GO; the same assessment with minimum 6 gives GO if no other binding condition fails. An untested 8/10 topic with minimum 7 can receive GO. A preferred venue mismatch alone does not veto GO. None of these outcomes determines whether the topic is useful to the user.
