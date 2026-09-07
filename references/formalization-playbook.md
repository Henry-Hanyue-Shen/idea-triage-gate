# Formalization playbook

Use this playbook when the raw idea admits materially different meanings. The objective is not to make the idea sound polished. It is to expose testable alternatives whose evidence, cost, or commercial path differs.

## Recover the invariant

Write the smallest claim shared by all reasonable interpretations:

> For `[user or system]`, changing `[mechanism or intervention]` should improve `[outcome]` under `[conditions]` relative to `[baseline]`.

Mark every missing field `unknown`; do not fill it with a fashionable assumption.

## Branch on consequential ambiguity

Create a new formalization only when at least one branch changes:

- the causal or algorithmic mechanism;
- the unit of analysis or target population;
- the output and success metric;
- the buyer and workflow;
- the required data or compute;
- the closest prior art; or
- the cheapest falsification test.

Useful lenses include:

### Scientific hypothesis

- Construct or phenomenon
- Intervention or comparison
- Observable outcome
- Boundary conditions
- Falsifier

### Engineering system

- Input and output contract
- Components and interfaces
- Critical invariant
- Baseline system
- Bottleneck and failure mode
- Evaluation workload

### Product wedge

- User and payer
- Painful repeated job
- Current workaround
- Smallest deliverable improvement
- Adoption trigger
- Distribution path

### Service or tooling layer

- Expensive capability deliberately not owned
- External dependency or API
- Proprietary orchestration, data, or workflow value
- Unit-economics sensitivity
- Supplier substitution risk

### Scale-down proxy

- Full-scale claim
- Smaller mechanism-preserving setting
- What transfers and what does not
- Proxy-to-production gap
- Evidence needed before scaling

## Reject cosmetic variants

Two variants are duplicates if they differ only in audience wording, model brand, interface style, or aspirational market. Merge them and preserve the stricter assumptions.

## Formalization card

For each surviving branch produce:

- `title`
- `problem`
- `mechanism`
- `target_user`
- `buyer`
- `success_metric`
- `baseline`
- `assumptions`
- `falsifier`
- `resource_envelope`
- `commercial_wedge`

If no branch is falsifiable, the correct gate result is not `BUILD`.
