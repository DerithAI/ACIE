import unittest
from formalization.state_models import transition, InvalidTransition, effective_actions, approval_matches

class StateModelTests(unittest.TestCase):
    def test_valid_action_path(self):
        state = "DRAFT"
        for target in ["SUBMITTED", "ALLOWED", "AUTHORIZED", "DISPATCHED", "ACKNOWLEDGED", "VERIFIED"]:
            state = transition(state, target, "action")
        self.assertEqual(state, "VERIFIED")

    def test_unknown_outcome_requires_reconciliation(self):
        self.assertEqual(transition("DISPATCHED", "OUTCOME_UNKNOWN", "action"), "OUTCOME_UNKNOWN")
        with self.assertRaises(InvalidTransition):
            transition("OUTCOME_UNKNOWN", "DISPATCHED", "action")
        self.assertEqual(transition("OUTCOME_UNKNOWN", "RECONCILIATION_PENDING", "action"), "RECONCILIATION_PENDING")

    def test_approval_required_path(self):
        self.assertEqual(transition("AWAITING_APPROVAL", "APPROVED", "action"), "APPROVED")
        with self.assertRaises(InvalidTransition):
            transition("AWAITING_APPROVAL", "AUTHORIZED", "action")

    def test_adaptation_requires_staged_monitoring_before_promotion(self):
        self.assertEqual(transition("MONITORING", "PROMOTED", "adaptation"), "PROMOTED")
        with self.assertRaises(InvalidTransition):
            transition("EVALUATED", "PROMOTED", "adaptation")

    def test_effective_permissions_are_intersection(self):
        result = effective_actions({"read", "write"}, {"read", "write"}, {"read"}, {"read", "publish"})
        self.assertEqual(result, {"read"})

    def test_approval_is_bound_to_exact_digest_and_expiry(self):
        decision = {"proposal_digest": "a"*64, "outcome": "ALLOW", "expires_at": "2026-11-05T03:00:00Z"}
        self.assertTrue(approval_matches(decision, "a"*64, "2026-11-05T02:00:00Z"))
        self.assertFalse(approval_matches(decision, "b"*64, "2026-11-05T02:00:00Z"))
        self.assertFalse(approval_matches(decision, "a"*64, "2026-11-05T03:00:00Z"))

if __name__ == "__main__":
    unittest.main()
