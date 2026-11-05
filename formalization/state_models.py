"""Executable reference transition guards for ACIE governance and adaptation models.

These helpers are a small conformance reference, not a production authorization engine.
"""
from __future__ import annotations

ACTION_TRANSITIONS = {
    "DRAFT": {"SUBMITTED", "WITHDRAWN"},
    "SUBMITTED": {"ALLOWED", "ALLOWED_WITH_CONDITIONS", "AWAITING_APPROVAL", "DENIED", "REVISION_REQUIRED", "ESCALATED"},
    "ALLOWED": {"AUTHORIZED", "EXPIRED", "REVOKED"},
    "ALLOWED_WITH_CONDITIONS": {"AUTHORIZED", "REVISION_REQUIRED", "EXPIRED", "REVOKED"},
    "AWAITING_APPROVAL": {"APPROVED", "REJECTED", "EXPIRED", "ESCALATED"},
    "APPROVED": {"AUTHORIZED", "EXPIRED", "REVOKED"},
    "AUTHORIZED": {"DISPATCHED", "REVOKED", "EXPIRED"},
    "DISPATCHED": {"ACKNOWLEDGED", "FAILED", "OUTCOME_UNKNOWN"},
    "ACKNOWLEDGED": {"VERIFIED", "FAILED", "OUTCOME_UNKNOWN"},
    "OUTCOME_UNKNOWN": {"RECONCILIATION_PENDING"},
    "RECONCILIATION_PENDING": {"VERIFIED", "FAILED", "OUTCOME_UNKNOWN"},
    "REVISION_REQUIRED": {"DRAFT"},
    "ESCALATED": {"SUBMITTED", "DENIED", "EXPIRED"},
}
ADAPTATION_TRANSITIONS = {
    "PROPOSED": {"TRIAGED", "REJECTED"},
    "TRIAGED": {"REVIEW_REQUIRED", "ABORTED"},
    "REVIEW_REQUIRED": {"SANDBOXED", "REJECTED"},
    "SANDBOXED": {"EVALUATED"},
    "EVALUATED": {"APPROVAL_PENDING", "REJECTED"},
    "APPROVAL_PENDING": {"STAGED", "REJECTED"},
    "STAGED": {"MONITORING"},
    "MONITORING": {"PROMOTED", "ROLLED_BACK"},
}
AUTONOMY_LEVELS = {"MANUAL": 0, "GUARDED": 1, "AUTONOMOUS": 2, "FULL": 3}

class InvalidTransition(ValueError):
    pass

def transition(current: str, target: str, model: str = "action") -> str:
    table = ACTION_TRANSITIONS if model == "action" else ADAPTATION_TRANSITIONS if model == "adaptation" else None
    if table is None:
        raise ValueError(f"Unknown state model: {model}")
    if target not in table.get(current, set()):
        raise InvalidTransition(f"Transition {current} -> {target} is not allowed in {model} model")
    return target

def effective_actions(mission_actions, actor_actions, tool_actions, policy_actions):
    """Return the intersection of all four capability envelopes."""
    return set(mission_actions) & set(actor_actions) & set(tool_actions) & set(policy_actions)

def approval_matches(decision: dict, proposal_digest: str, now_iso: str) -> bool:
    """Check exact digest binding, allow outcome, and lexical RFC3339 expiry ordering."""
    if decision.get("proposal_digest") != proposal_digest:
        return False
    if decision.get("outcome") not in {"ALLOW", "ALLOW_WITH_CONDITIONS"}:
        return False
    expiry = decision.get("expires_at")
    if expiry and now_iso >= expiry:
        return False
    return True
