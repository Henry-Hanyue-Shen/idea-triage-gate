# Portable gate contract

Use `IDEA_GATE.json` only when the assessment must be handed to another agent, conversation, or automated workflow. Human-readable output remains primary.

## Required top-level fields

```json
{
  "schema_version": "1.0",
  "idea_id": "stable-short-id",
  "assessment_date": "YYYY-MM-DD",
  "source_idea": "verbatim or minimally normalized input",
  "constraints": {
    "time": "known limit or unknown",
    "cash": "known limit or unknown",
    "compute": "known limit or unknown",
    "team": "known limit or unknown"
  },
  "formalizations": [],
  "champion_id": "F1 or null",
  "overall_verdict": "BUILD|TEST|PARK|KILL",
  "next_action": "one bounded action",
  "unknowns": [],
  "evidence_register": []
}
```

Each formalization must contain:

- `id`, `title`, `problem`, `mechanism`, `target_user`, `buyer`, and `success_metric`;
- `assumptions`, `nearest_neighbors`, `innovation_delta`, and `fatal_constraints` as arrays;
- `ratings` for `innovation`, `plausibility`, `commercialization`, and `resource_fit`;
- `resource_estimate` with `compute_class`, `hardware`, `duration`, `cash_range`, `data`, and `team`;
- `cheapest_test`; and
- `verdict`.

Each rating contains integer `rating` from 0 to 4, `confidence` (`low`, `medium`, or `high`), and `rationale`.

For `BUILD` and `TEST`, `cheapest_test` must be an object containing:

- `decision_question`
- `minimal_artifact`
- `baseline`
- `metric`
- `pass_threshold`
- `fail_threshold`
- `resource_cap`
- `largest_confound`
- `next_if_pass`
- `next_if_fail`

For `PARK` and `KILL`, `cheapest_test` may be `null` when no bounded test is justified.

Each evidence-register entry should include `claim`, `status` (`given`, `observed`, `inferred`, `estimated`, or `unknown`), `source`, and `as_of`. Use `null` for a missing source, never a fabricated citation.

## Decision invariants

- Formalization IDs are unique.
- `champion_id`, when present, names a formalization.
- `BUILD` has no fatal constraints and is not `frontier_only`.
- `BUILD` and `TEST` include a complete cheapest test.
- `frontier_only` cannot be `BUILD`.
- A top-level `BUILD` must name a formalization whose verdict is `BUILD`.
- A top-level `TEST` must name a formalization whose verdict is `TEST` or `BUILD`.
- An empty formalization set is invalid.

The included validator checks these structural invariants, not factual truth.
