from __future__ import annotations


def deployment_decision_from_residual_risk(residual_risk_score: float) -> str:
    """Map residual risk score to a deployment decision."""
    if residual_risk_score < 2.0: return 'Approve'
    if residual_risk_score < 2.8: return 'Approve with monitoring'
    if residual_risk_score < 3.5: return 'Pilot only'
    if residual_risk_score < 4.2: return 'Pause deployment'
    return 'Reject / prohibit'


def decision_rationale(decision: str) -> str:
    """Return a short explanation for a deployment decision."""
    return {'Approve':'Risk is low and controls are strong.','Approve with monitoring':'Risk is manageable but requires active monitoring.','Pilot only':'System should remain limited until stronger evidence is collected.','Pause deployment':'Material fairness, evidence, or governance gaps must be fixed before scaling.','Reject / prohibit':'Risk is unacceptable or essential safeguards are absent.'}.get(decision, 'Decision requires further review.')
