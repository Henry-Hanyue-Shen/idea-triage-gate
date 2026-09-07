"""Small dependency-free CI check for required skill metadata and files."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
yaml = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")

assert skill.startswith("---\nname: idea-triage-gate\n"), "SKILL.md frontmatter is missing or malformed"
assert "description:" in skill.split("---", 2)[1], "SKILL.md description is missing"
assert "TODO" not in skill, "SKILL.md still contains TODO text"
assert 'default_prompt: "Use $idea-triage-gate' in yaml, "default prompt must name the skill"

required = [
    "README.md",
    "LICENSE",
    "references/formalization-playbook.md",
    "references/evaluation-rubric.md",
    "references/pattern-library.md",
    "references/gate-contract.md",
    "scripts/validate_idea_gate.py",
    "examples/idea-gate.json",
]
missing = [path for path in required if not (ROOT / path).is_file()]
assert not missing, f"missing required files: {missing}"
print("OK: required skill files and metadata are present")
