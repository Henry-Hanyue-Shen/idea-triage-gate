# Recombination pattern library

These are design prompts abstracted from projects and research directions previously collected by the maintainer. They are not endorsements, verified performance claims, or substitutes for current source checks.

Use at most the patterns that expose a materially different formalization.

## Representation and prediction

- **Structure follows dependency:** infer a sparse graph or modular architecture from feature relationships instead of fixing all connections in advance.
- **Distribution before point estimate:** predict a return, risk, or outcome distribution when tail behavior matters more than the mean.
- **Causal reconstruction:** infer plausible latent causes from observed effects, with explicit identifiability limits.
- **Compositionality stress test:** test whether a model's decomposition bias helps ordinary cases but damages idioms, exceptions, or coupled phenomena.

## Agent organization

- **Versioned shared memory:** make decisions, provenance, and reusable notes addressable across agents and reversible across turns.
- **Organization before headcount:** change topology, role boundaries, incentives, or peer coordination before adding agents.
- **Expensive reader, cheap actor:** use a stronger model for interpretation or verification and a smaller model for repetitive generation, while measuring communication loss.
- **Gate rather than pipeline:** place a narrow accountable audit between creation and downstream action; return missing evidence to the caller.
- **Just-in-time tools:** assemble the smallest task-specific harness rather than keeping every tool and context active.

## Efficient models and deployment

- **Mechanism-preserving scale-down:** test the claim on a reduced domain, simulator, or smaller model before paying full-scale cost.
- **Quantization-aware local wedge:** treat memory, latency, and privacy as product constraints, not afterthoughts.
- **Tiny edge specialist:** narrow the action and data domain enough that an embedded model can beat a general cloud workflow on latency or availability.
- **From-scratch teaching stack:** expose an end-to-end mechanism in a small reproducible implementation when education or auditability is the value.

## Information and workflow products

- **API composition instead of scraping:** build on stable public interfaces when data ownership is not the differentiator.
- **Architecture as observability:** make tool calls, request chains, provenance, and failure recovery inspectable as a first-class interface.
- **Document-scale decomposition:** split large inputs deterministically, preserve page or section provenance, then aggregate with bounded context.
- **Domain commerce agent:** anchor an agent in a specific transaction, catalog, policy, and escalation path rather than a generic assistant.

## How to use a pattern

For any selected pattern, state:

1. what the pattern changes in the raw idea;
2. which assumption it removes or introduces;
3. whether it improves plausibility, resource fit, or commercialization;
4. the new failure mode; and
5. the evidence needed to keep it.

Do not cite this library as proof that an approach works. Locate the underlying current sources if the pattern becomes part of the recommendation.
