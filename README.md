# Idea Triage Gate

Idea Triage Gate is a portable Codex skill for turning a rough research, engineering, or product idea into a resource-aware decision.

It does not require the idea to arrive formalized. When several interpretations would lead to different evidence, customers, experiments, or costs, the skill keeps those interpretations separate, evaluates each one, and selects the cheapest useful next commitment.

Maintained by Hanyue Shen, Founder at YH Intelligence Technology, Co., Ltd. Contact: [hanyueshen@yh-intel.com](mailto:hanyueshen@yh-intel.com).

## What it does

- reconstructs the core problem, mechanism, user, buyer, metric, and constraints from informal input;
- generates two to five materially distinct formalizations when ambiguity matters;
- runs bounded novelty, prior-art, competitor, and buyer checks;
- separates observed facts, user premises, inferences, estimates, and unknowns;
- estimates data, compute, cash, time, integration, and team needs by order of magnitude;
- applies hard feasibility gates before ratings;
- designs the cheapest discriminating test; and
- returns `BUILD`, `TEST`, `PARK`, or `KILL`.

An idea that only becomes plausible with frontier-scale infrastructure cannot receive `BUILD` unless that resource envelope is explicitly in scope. A faithful scale-down experiment may still receive `TEST`.

## What it does not do

This is not a full autoresearch pipeline. It does not launch open-ended literature review, run experiments, build products, contact customers, purchase compute, raise funds, or publish on its own. It returns a bounded follow-up request when deeper work is justified.

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/Henry-Hanyue-Shen/idea-triage-gate.git ~/.codex/skills/idea-triage-gate
```

On Windows PowerShell:

```powershell
git clone https://github.com/Henry-Hanyue-Shen/idea-triage-gate.git "$env:USERPROFILE\.codex\skills\idea-triage-gate"
```

Restart or refresh Codex skill discovery after installation.

## Use

The input can be one sentence:

```text
Use $idea-triage-gate on this: Could a small model rewrite the tool graph while several agents work so we use less context and fewer expensive calls?
```

You can also state an envelope:

```text
Use $idea-triage-gate. I have two weeks, one developer, one 24 GB GPU, and at most $1,000. Formalize every materially different version and tell me what to test first.
```

For agent-to-agent handoff, ask for `IDEA_GATE.json`. Validate its structure without external dependencies:

```bash
python scripts/validate_idea_gate.py examples/idea-gate.json
```

The validator checks report structure and decision invariants. It does not certify the truth or business value of the idea.

## Decision model

- `BUILD`: prototype now within the stated envelope.
- `TEST`: resolve one decisive uncertainty with a bounded cheap experiment.
- `PARK`: retain the idea, but wait for a credible missing enabler.
- `KILL`: stop because a fatal constraint, dominated economics, lack of a wedge, or an untestable frontier-only dependency remains.

Ratings for innovation, plausibility, commercialization, and resource fit summarize the evidence. They never average away a fatal constraint.

## Design lineage

The included pattern library abstracts recurring design moves from previously collected work on sparse architectures, distributional prediction, causal reconstruction, agent organization, shared memory, efficient local models, document processing, and narrow evidence gates. Those abstractions are prompts for exploration, not proof that any source claim is true.

This repository contains an original implementation and vendors no code or private prompts from the referenced projects. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

MIT. Copyright 2026 Hanyue Shen.
