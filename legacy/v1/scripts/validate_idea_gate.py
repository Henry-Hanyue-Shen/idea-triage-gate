#!/usr/bin/env python3
"""Validate IDEA_GATE.json structure and decision invariants without dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


VERDICTS = {"BUILD", "TEST", "PARK", "KILL"}
CONFIDENCE = {"low", "medium", "high"}
COMPUTE_CLASSES = {"local", "single_gpu", "small_cluster", "funded_cluster", "frontier_only"}
RATING_KEYS = {"innovation", "plausibility", "commercialization", "resource_fit"}
TEST_KEYS = {
    "decision_question",
    "minimal_artifact",
    "baseline",
    "metric",
    "pass_threshold",
    "fail_threshold",
    "resource_cap",
    "largest_confound",
    "next_if_pass",
    "next_if_fail",
}


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_keys(value: Any, keys: set[str], path: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{path} must be an object")
        return
    for key in sorted(keys - value.keys()):
        errors.append(f"{path}.{key} is required")


def validate_report(report: Any) -> list[str]:
    errors: list[str] = []
    top_keys = {
        "schema_version", "idea_id", "assessment_date", "source_idea", "constraints",
        "formalizations", "champion_id", "overall_verdict", "next_action", "unknowns",
        "evidence_register",
    }
    require_keys(report, top_keys, "$", errors)
    if not isinstance(report, dict):
        return errors

    if report.get("schema_version") != "1.0":
        errors.append("$.schema_version must equal '1.0'")
    for key in ("idea_id", "assessment_date", "source_idea", "next_action"):
        if not nonempty(report.get(key)):
            errors.append(f"$.{key} must be a non-empty string")
    require_keys(report.get("constraints"), {"time", "cash", "compute", "team"}, "$.constraints", errors)
    for key in ("unknowns", "evidence_register"):
        if not isinstance(report.get(key), list):
            errors.append(f"$.{key} must be an array")

    overall = report.get("overall_verdict")
    if overall not in VERDICTS:
        errors.append(f"$.overall_verdict must be one of {sorted(VERDICTS)}")

    formalizations = report.get("formalizations")
    if not isinstance(formalizations, list) or not formalizations:
        errors.append("$.formalizations must be a non-empty array")
        return errors

    seen: set[str] = set()
    verdict_by_id: dict[str, str] = {}
    form_keys = {
        "id", "title", "problem", "mechanism", "target_user", "buyer", "success_metric",
        "assumptions", "nearest_neighbors", "innovation_delta", "ratings", "fatal_constraints",
        "resource_estimate", "cheapest_test", "verdict",
    }
    resource_keys = {"compute_class", "hardware", "duration", "cash_range", "data", "team"}

    for index, item in enumerate(formalizations):
        path = f"$.formalizations[{index}]"
        require_keys(item, form_keys, path, errors)
        if not isinstance(item, dict):
            continue
        item_id = item.get("id")
        if not nonempty(item_id):
            errors.append(f"{path}.id must be a non-empty string")
        elif item_id in seen:
            errors.append(f"{path}.id duplicates {item_id!r}")
        else:
            seen.add(item_id)
        for key in ("title", "problem", "mechanism", "target_user", "buyer", "success_metric"):
            if not nonempty(item.get(key)):
                errors.append(f"{path}.{key} must be a non-empty string")
        for key in ("assumptions", "nearest_neighbors", "innovation_delta", "fatal_constraints"):
            if not isinstance(item.get(key), list):
                errors.append(f"{path}.{key} must be an array")

        ratings = item.get("ratings")
        require_keys(ratings, RATING_KEYS, f"{path}.ratings", errors)
        if isinstance(ratings, dict):
            for key in RATING_KEYS:
                rating = ratings.get(key)
                require_keys(rating, {"rating", "confidence", "rationale"}, f"{path}.ratings.{key}", errors)
                if not isinstance(rating, dict):
                    continue
                number = rating.get("rating")
                if not isinstance(number, int) or isinstance(number, bool) or not 0 <= number <= 4:
                    errors.append(f"{path}.ratings.{key}.rating must be an integer from 0 to 4")
                if rating.get("confidence") not in CONFIDENCE:
                    errors.append(f"{path}.ratings.{key}.confidence must be one of {sorted(CONFIDENCE)}")
                if not nonempty(rating.get("rationale")):
                    errors.append(f"{path}.ratings.{key}.rationale must be a non-empty string")

        resource = item.get("resource_estimate")
        require_keys(resource, resource_keys, f"{path}.resource_estimate", errors)
        compute_class = resource.get("compute_class") if isinstance(resource, dict) else None
        if compute_class not in COMPUTE_CLASSES:
            errors.append(f"{path}.resource_estimate.compute_class must be one of {sorted(COMPUTE_CLASSES)}")

        verdict = item.get("verdict")
        if verdict not in VERDICTS:
            errors.append(f"{path}.verdict must be one of {sorted(VERDICTS)}")
        elif nonempty(item_id):
            verdict_by_id[item_id] = verdict

        fatal = item.get("fatal_constraints")
        if verdict == "BUILD" and isinstance(fatal, list) and fatal:
            errors.append(f"{path}: BUILD cannot have fatal constraints")
        if verdict == "BUILD" and compute_class == "frontier_only":
            errors.append(f"{path}: frontier_only cannot receive BUILD")
        if verdict in {"BUILD", "TEST"}:
            test = item.get("cheapest_test")
            require_keys(test, TEST_KEYS, f"{path}.cheapest_test", errors)
            if isinstance(test, dict):
                for key in TEST_KEYS:
                    if key == "resource_cap":
                        if not isinstance(test.get(key), dict) or not test.get(key):
                            errors.append(f"{path}.cheapest_test.resource_cap must be a non-empty object")
                    elif not nonempty(test.get(key)):
                        errors.append(f"{path}.cheapest_test.{key} must be a non-empty string")

    champion = report.get("champion_id")
    if champion is not None and champion not in seen:
        errors.append("$.champion_id must be null or name a formalization")
    champion_verdict = verdict_by_id.get(champion)
    if overall == "BUILD" and champion_verdict != "BUILD":
        errors.append("top-level BUILD requires a BUILD champion")
    if overall == "TEST" and champion_verdict not in {"TEST", "BUILD"}:
        errors.append("top-level TEST requires a TEST or BUILD champion")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_idea_gate.py IDEA_GATE.json", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    errors = validate_report(report)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {path} satisfies IDEA_GATE schema 1.0 structural invariants")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
