"""Validate v2 structure and the recorded academic screen, not scholarly truth."""
import json
import sys
from pathlib import Path


def validate_report(r):
    errors = []
    if not isinstance(r, dict):
        return ['report must be an object']
    required = {'schema_version', 'idea_id', 'idea_revision', 'run_id', 'prompt_version', 'assessed_at', 'confirmation', 'academic', 'policy', 'gate', 'venues', 'research_obligations', 'decisive_unknowns', 'evidence_summary', 'prior_run_reference'}
    errors.extend(f'missing {k}' for k in sorted(required - r.keys()))
    if r.get('schema_version') != '2.0':
        errors.append('schema_version must be 2.0')
    def obj(key):
        v = r.get(key)
        if not isinstance(v, dict):
            errors.append(f'{key} must be an object')
            return {}
        return v
    a, p, g, c = (obj(k) for k in ('academic', 'policy', 'gate', 'confirmation'))
    for k in ('venues', 'research_obligations', 'decisive_unknowns'):
        if not isinstance(r.get(k), list):
            errors.append(f'{k} must be an array')
    score = a.get('score')
    valid_score = type(score) is int and 1 <= score <= 10
    if score is not None and not valid_score:
        errors.append('score must be an integer 1–10 or null')
    if a.get('confidence') not in ('low', 'medium', 'high', None):
        errors.append('invalid confidence')
    if valid_score and a.get('confidence') is None:
        errors.append('scored assessments need confidence')
    if c.get('status') not in ('confirmed', 'waived', 'awaiting'):
        errors.append('invalid confirmation status')
    if (score is not None or g.get('verdict') is not None) and c.get('status') not in ('confirmed', 'waived'):
        errors.append('scoring requires confirmation or waiver')
    threshold = p.get('minimum_score')
    valid_threshold = type(threshold) is int and 1 <= threshold <= 10
    if threshold is not None and not valid_threshold:
        errors.append('minimum_score must be an integer 1–10 or null')
    mandatory = p.get('mandatory_venue_criteria', [])
    checks = g.get('criteria_checks', [])
    if not isinstance(mandatory, list) or any(not isinstance(x, str) or not x for x in mandatory):
        errors.append('mandatory criteria must be nonempty strings in an array')
        mandatory = []
    if len(set(mandatory)) != len(mandatory):
        errors.append('duplicate mandatory criteria')
    if not isinstance(checks, list):
        errors.append('criteria_checks must be an array')
        checks = []
    expected = list(mandatory) + (['minimum_score'] if threshold is not None else [])
    statuses = {}
    for check in checks:
        if not isinstance(check, dict):
            errors.append('each check must be an object'); continue
        key, status = check.get('criterion'), check.get('status')
        if not isinstance(key, str):
            errors.append('criterion must be a string'); continue
        if key in statuses:
            errors.append('duplicate criterion check')
        statuses[key] = status
        if status not in ('met', 'not_met', 'unknown'):
            errors.append('invalid criterion status')
        if not isinstance(check.get('reason'), str) or not check['reason'].strip():
            errors.append('criterion check needs a reason')
    if set(statuses) != set(expected):
        errors.append('checks must match binding criteria exactly; preferences are nonbinding')
    if valid_threshold:
        actual = ('met' if score >= threshold else 'not_met') if valid_score else 'unknown'
        if statuses.get('minimum_score') != actual:
            errors.append('minimum_score check disagrees with score')
        statuses['minimum_score'] = actual
    if not expected:
        verdict, status = None, 'awaiting_policy'
    elif 'not_met' in statuses.values():
        verdict, status = 'NO-GO', 'decided'
    elif all(statuses.get(k) == 'met' for k in expected):
        verdict, status = 'GO', 'decided'
    else:
        verdict, status = None, 'incomplete'
    if (g.get('verdict'), g.get('status')) != (verdict, status):
        errors.append(f'gate must be {verdict!r} with status {status}')
    def forbidden(v):
        if isinstance(v, dict):
            return any(k == 'utility_score' or forbidden(x) for k, x in v.items())
        return isinstance(v, list) and any(forbidden(x) for x in v)
    if forbidden(r):
        errors.append('personal utility must not be scored')
    return errors


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: validate_assessment.py RESULT.json')
    try:
        issues = validate_report(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError, ValueError) as exc:
        sys.exit(str(exc))
    print('\n'.join(issues) if issues else 'OK: v2 structural and policy checks passed')
    sys.exit(bool(issues))
