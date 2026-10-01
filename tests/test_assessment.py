import copy
import importlib.util
import json
from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',R/'scripts/validate_assessment.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.r=json.loads((R/'examples/assessment-v2.json').read_text())
    def test_open_topic_can_go(self):
        self.assertEqual(m.validate_report(self.r),[])
    def test_threshold_failure(self):
        self.r['academic']['score']=6
        self.assertTrue(m.validate_report(self.r))
        self.r['gate'].update(verdict='NO-GO',criteria_checks=[{'criterion':'minimum_score','status':'not_met','reason':'6 < 7'}])
        self.assertEqual(m.validate_report(self.r),[])
    def test_no_policy(self):
        self.r['policy']['minimum_score']=None
        self.r['gate'].update(verdict=None,status='awaiting_policy',criteria_checks=[])
        self.assertEqual(m.validate_report(self.r),[])
    def test_unknown_venue(self):
        self.r['policy']['mandatory_venue_criteria']=['target fit']
        self.r['gate']['criteria_checks'].append({'criterion':'target fit','status':'unknown','reason':'scope unavailable'})
        self.assertTrue(m.validate_report(self.r))
        self.r['gate'].update(verdict=None,status='incomplete')
        self.assertEqual(m.validate_report(self.r),[])
    def test_confirmation_required(self):
        self.r['confirmation']['status']='awaiting'
        self.assertTrue(m.validate_report(self.r))
    def test_utility_forbidden(self):
        self.r['utility_score']=9
        self.assertTrue(m.validate_report(self.r))
    def test_invalid_scores(self):
        for score in [True,0,11,7.5,'8']:
            r=copy.deepcopy(self.r);r['academic']['score']=score
            self.assertTrue(m.validate_report(r))
    def test_preference_not_gate(self):
        self.r['policy']['preferred_venues']=['Example Venue']
        self.assertEqual(m.validate_report(self.r),[])
    def test_failed_condition_overrides_unknown(self):
        self.r['academic']['score']=6
        self.r['policy']['mandatory_venue_criteria']=['target fit']
        self.r['gate'].update(verdict='NO-GO',criteria_checks=[{'criterion':'minimum_score','status':'not_met','reason':'6 < 7'},{'criterion':'target fit','status':'unknown','reason':'pending'}])
        self.assertEqual(m.validate_report(self.r),[])
