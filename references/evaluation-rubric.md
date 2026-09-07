# Evaluation rubric

Rate dimensions independently from 0 to 4. Always attach confidence and a short reason. Evidence quality controls confidence; enthusiasm does not.

## Innovation

- **0 — known duplicate:** no meaningful delta from a dominant or obvious alternative.
- **1 — cosmetic:** packaging, branding, or benchmark substitution with little mechanism or workflow change.
- **2 — useful recombination:** known pieces combined for a narrower setting or user; novelty is mainly execution.
- **3 — defensible delta:** a clear technical, scientific, data, or workflow contribution with limited direct precedent.
- **4 — foundational:** a well-specified new capability or mechanism with strong evidence against close neighbors.

Do not assign 4 from a bounded search alone. Treat patentability as a separate legal question.

## Plausibility

- **0 — contradicted:** violates a hard constraint or depends on an unsupported causal step.
- **1 — remote:** several critical mechanisms are unobserved and no faithful cheap proxy exists.
- **2 — uncertain but testable:** credible pieces exist; one or two decisive assumptions remain.
- **3 — plausible:** mechanisms and dependencies are supported; integration risk remains manageable.
- **4 — demonstrated:** the core mechanism works in a representative setting with a credible baseline.

Do not equate a demo with general validity.

## Commercialization

- **0 — no beneficiary:** no identifiable user, payer, or valuable decision.
- **1 — vague demand:** broad market language without a painful job or adoption route.
- **2 — plausible wedge:** clear user and problem, but willingness to pay or distribution is untested.
- **3 — strong wedge:** measurable benefit, reachable buyer, tolerable integration, and credible unit economics.
- **4 — validated pull:** repeated adoption or payment evidence and a defensible route to expansion.

A research-only idea may score 0–1 commercially and still merit a scientific `TEST`; say so explicitly.

## Resource fit

- **0 — frontier-only:** requires infrastructure, capital, data, or permissions outside the stated envelope with no faithful proxy.
- **1 — major mismatch:** feasible in principle but needs a funded cluster, large proprietary dataset, long certification, or a large team.
- **2 — stretch:** possible with a bounded grant, rented small cluster, specialist collaborator, or several months.
- **3 — practical:** single GPU to small cluster, accessible data, and a small capable team.
- **4 — lightweight:** laptop, API, simulator, public data, or a short field test can resolve the key question.

## Confidence

- `low`: mostly assumptions, memory, social leads, or sparse sources;
- `medium`: direct sources exist but coverage, replication, or market evidence is incomplete;
- `high`: representative direct evidence, reproducible tests, or repeated buyer behavior supports the rating.

## Hard gates

Hard gates override ratings:

- a fatal scientific or engineering contradiction;
- required data cannot legally or practically be obtained;
- no test observes the claimed mechanism or outcome;
- resource class is `frontier_only` and the user did not authorize that envelope;
- buyer economics are structurally negative with no narrower wedge; or
- the claimed novelty is already the ordinary behavior of an accessible incumbent and no defensible differentiation remains.

Use `PARK` when the blocker has a credible time-bound enabler. Use `KILL` when it does not. Use `TEST` when a cheap experiment can resolve the blocker.

## Portfolio selection

Do not average ratings into a winner. Choose the branch with the best combination of:

1. important outcome;
2. discriminating cheap test;
3. absence of fatal constraints;
4. resource fit; and
5. upside if the test succeeds.

Prefer learning rate per dollar over headline scale.
