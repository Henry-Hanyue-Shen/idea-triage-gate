import copy
import json
import unittest
from pathlib import Path

from scripts.validate_idea_gate import validate_report


ROOT = Path(__file__).resolve().parents[1]


class ValidateIdeaGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid = json.loads((ROOT / "examples" / "idea-gate.json").read_text(encoding="utf-8"))

    def test_example_is_valid(self):
        self.assertEqual(validate_report(self.valid), [])

    def test_build_cannot_be_frontier_only(self):
        report = copy.deepcopy(self.valid)
        report["formalizations"][0]["verdict"] = "BUILD"
        report["formalizations"][0]["resource_estimate"]["compute_class"] = "frontier_only"
        report["overall_verdict"] = "BUILD"
        self.assertTrue(any("frontier_only" in error for error in validate_report(report)))

    def test_test_requires_discriminating_test(self):
        report = copy.deepcopy(self.valid)
        report["formalizations"][0]["cheapest_test"] = None
        self.assertTrue(any("cheapest_test" in error for error in validate_report(report)))

    def test_duplicate_formalization_id_is_rejected(self):
        report = copy.deepcopy(self.valid)
        report["formalizations"].append(copy.deepcopy(report["formalizations"][0]))
        self.assertTrue(any("duplicates" in error for error in validate_report(report)))


if __name__ == "__main__":
    unittest.main()
