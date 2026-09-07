---
name: idea-triage-gate
description: Formalize and rapidly evaluate rough research, engineering, or product ideas. Use when an idea is incomplete or ambiguous and the user needs distinct testable interpretations, a bounded novelty and market check, order-of-magnitude feasibility and resource estimates, the cheapest discriminating test, and a BUILD, TEST, PARK, or KILL decision. Do not use as a full autoresearch, implementation, fundraising, or deployment workflow.
---

# Idea Triage Gate

Turn a quick idea into a decision without pretending that early evidence is stronger than it is.

## Scope

Act as one accountable idea gate. Recover the user's intended opportunity, expose materially different interpretations, test the weakest assumptions first, and recommend the smallest useful next commitment.

This skill may:

- formalize an incomplete research, engineering, product, or hybrid idea;
- compare multiple non-equivalent formalizations;
- conduct a bounded novelty, prior-art, competitor, and buyer check when tools allow;
- estimate data, compute, cash, time, integration, and team requirements by order of magnitude;
- design a cheap falsification test; and
- return `BUILD`, `TEST`, `PARK`, or `KILL`.

This skill must not:

- run a full literature review or open-ended autoresearch loop;
- build, deploy, purchase, contact people, or publish without separate authorization;
- turn social-media claims into evidence;
- invent benchmarks, costs, citations, customers, market size, or technical readiness;
- reward novelty that has no plausible path to validation or use; or
- collapse scientific novelty, engineering differentiation, and commercial advantage into one claim.

## Evidence discipline

Label important statements as one of:

- **Given**: supplied by the user or artifact;
- **Observed**: directly verified in a source, repository, dataset, or experiment;
- **Inferred**: a reasoned conclusion from stated facts;
- **Estimated**: an order-of-magnitude calculation with assumptions;
- **Unknown**: information that could change the verdict.

Treat screenshots, posts, headlines, and remembered projects as discovery leads or design patterns. Verify their underlying papers, repositories, product pages, or documentation before using them as evidence. A bounded scan is not an exhaustive novelty search; state the search date, scope, and confidence.

## Workflow

### 1. Normalize the raw idea

Restate the idea in one sentence without improving it yet. Extract what is known about:

- problem or observation;
- proposed mechanism;
- intended user and economic buyer;
- input, output, and success criterion;
- data, compute, time, cash, team, geography, and regulatory constraints; and
- assumptions or dependencies.

Do not force a clarifying question when a reversible assumption permits progress. Record the assumption. Ask only when a missing choice would materially change scope, authorization, or safety.

### 2. Generate distinct formalizations

If ambiguity is material, create two to five formalizations. Use only interpretations that change at least one of mechanism, customer, evidence burden, resource envelope, or failure mode. Do not pad the set with wording variants.

Consider, when relevant:

- a falsifiable scientific hypothesis;
- a system or algorithm with explicit interfaces and metrics;
- a narrow product wedge tied to a painful workflow;
- a service or tooling layer that avoids owning an expensive core model; and
- a scale-down proxy that tests the mechanism before scaling.

Read [references/formalization-playbook.md](references/formalization-playbook.md) whenever the idea is underspecified or has multiple plausible meanings. Consult [references/pattern-library.md](references/pattern-library.md) for recombination prompts, never as evidence.

### 3. Run cheap contradiction checks

Before scoring, try to kill each formalization on paper:

- Does the mechanism contradict a known physical, mathematical, data, latency, or incentive constraint?
- Is the claimed improvement merely a metric or benchmark substitution?
- Is necessary data legally or practically inaccessible?
- Does inference cost erase the buyer's benefit?
- Is a platform owner able to absorb the feature trivially?
- Does success require a capability that the proposed test does not measure?
- Is the user different from the buyer, with no credible procurement path?

Record fatal constraints separately from ordinary risks. A score cannot average away a fatal constraint.

### 4. Perform a bounded evidence check

For novelty or commercialization claims that may have changed, search current sources when tools are available. Prefer:

1. papers, official repositories, documentation, standards, patents, and company product pages;
2. reproducible benchmarks or datasets with stated methodology;
3. credible secondary analysis for context; and
4. social posts only as leads.

Stop when the nearest relevant neighbors, likely novelty delta, and main market alternative are clear enough to choose the next test. If browsing is unavailable, label novelty and market conclusions `provisional` and lower confidence; do not silently rely on memory.

For each formalization report:

- nearest technical or scientific neighbors;
- nearest product or workflow alternative;
- the exact claimed delta;
- whether that delta is new, merely recombined, or still unknown; and
- what evidence would reverse the conclusion.

### 5. Estimate feasibility and resource fit

Use order-of-magnitude ranges, not false precision. Separate training, inference, data acquisition, integration, evaluation, and ongoing operations. State assumptions for:

- compute class: `local`, `single_gpu`, `small_cluster`, `funded_cluster`, or `frontier_only`;
- representative hardware and hardware-hours;
- data volume, provenance, labeling, and access;
- prototype time and team capabilities;
- cash range excluding and including labor when possible;
- latency, memory, bandwidth, energy, and reliability constraints; and
- dependencies outside the team's control.

Never infer that the user owns expensive infrastructure. Prefer a laptop, a single commodity GPU, a rented burst, a simulator, a reduced domain, or an API-backed proxy when it still tests the core mechanism.

An idea that only works through frontier-scale infrastructure—such as thousands of top-tier GPUs or an equivalent capital burden—cannot receive `BUILD` unless the user explicitly places that envelope in scope. Use `PARK` when a credible future enabler exists; otherwise use `KILL`. A credible scale-down test can receive `TEST`, but success at small scale must not be described as proof of full-scale viability.

### 6. Evaluate commercialization

Commercialization is a mechanism, not a large market label. Identify:

- specific user and payer;
- painful job and current workaround;
- narrow first wedge;
- measurable benefit and switching trigger;
- distribution or procurement route;
- integration, trust, compliance, and support burden;
- gross-margin or compute-unit-economics risk;
- defensibility from data, workflow, distribution, IP, know-how, or network effects; and
- the cheapest evidence of willingness to adopt or pay.

Keep “interesting research,” “useful capability,” and “fundable business” as separate conclusions.

### 7. Score with hard gates

Read [references/evaluation-rubric.md](references/evaluation-rubric.md) before assigning ratings. Rate each dimension from 0 to 4 with `low`, `medium`, or `high` confidence:

- innovation;
- plausibility;
- commercialization;
- resource fit.

The ratings summarize reasoning; they do not calculate the verdict. Apply hard constraints first.

Use exactly one verdict per formalization:

- `BUILD`: no known fatal constraint, a credible user or research value proposition, and a prototype within the stated resource envelope;
- `TEST`: a decisive uncertainty can be reduced by a bounded cheap test;
- `PARK`: potentially valuable, but blocked by timing, capital, data, regulation, or a missing enabling capability;
- `KILL`: contradicted, commoditized without a wedge, impossible to validate meaningfully, economically dominated, or frontier-only without a scale-down path.

When there are multiple formalizations, name one champion or state that none survives. Preserve a runner-up only if its failure mode or test is meaningfully different.

### 8. Specify the cheapest discriminating test

For every `BUILD` or `TEST`, give:

- decision question;
- minimal artifact or protocol;
- baseline or control;
- metric;
- pass threshold;
- fail threshold;
- maximum time, cash, data, and compute;
- largest confound;
- next action if passed; and
- next action if failed.

The test must distinguish between competing explanations. “Build a demo,” “do more research,” and “ask users” are not sufficient without a decision threshold.

## Output contract

Lead with a compact decision memo:

1. **Normalized idea**
2. **Distinct formalizations**
3. **Comparison** — evidence, ratings, fatal constraints, and resource bands
4. **Verdict** — champion plus `BUILD`, `TEST`, `PARK`, or `KILL`
5. **Cheapest next test**
6. **Unknowns that could flip the verdict**
7. **Sources and search boundary**, if a search was performed

Keep the first-pass memo concise enough to support a same-day decision. Expand only at the user's request or when the idea's risk justifies it.

When the result must pass between agents or conversations, also emit `IDEA_GATE.json` according to [references/gate-contract.md](references/gate-contract.md). Validate it with:

```bash
python scripts/validate_idea_gate.py IDEA_GATE.json
```

Do not imply that a validated JSON file validates the underlying idea; it validates only the report structure and decision invariants.

## Handoff behavior

If deeper work is warranted, return a bounded request to the calling conversation rather than silently starting a full workflow. State exactly which follow-up is needed: literature search, patent search, customer discovery, benchmark, prototype, cost quote, legal review, or domain-expert check.

The calling agent owns that work. This gate resumes when the resulting evidence is returned.
