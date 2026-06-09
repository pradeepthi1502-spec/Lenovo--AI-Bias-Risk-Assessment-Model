from __future__ import annotations
import pandas as pd
from .control_maturity import control_maturity_from_evidence, evidence_completion_score
from .deployment_decision_rules import deployment_decision_from_residual_risk

DEFAULT_INHERENT_RISK = {'ai_detection_tool':4.5,'student_chatbot':3.1,'vle_engagement_analytics':3.4,'career_service_ai':3.0,'ai_assisted_marking_feedback':4.2,'early_alert_prediction':4.1,'automated_essay_scoring':4.3,'admissions_support':4.4}


def calculate_inherent_risk(scores: dict[str, float]) -> float:
    """Calculate inherent risk as the average of risk factor scores."""
    if not scores: return 0.0
    return round(sum(float(v) for v in scores.values()) / len(scores), 2)


def calculate_residual_risk(inherent_risk_score: float, control_maturity_score: float, control_reduction_factor: float = 0.50) -> float:
    """Calculate residual risk after controls."""
    control_effect = (control_maturity_score / 5) * control_reduction_factor
    return round(max(0.0, inherent_risk_score * (1 - control_effect)), 2)


def assess_system_risk(system_row: pd.Series | dict, evidence_df: pd.DataFrame | None = None, inherent_risk_map: dict[str, float] | None = None) -> dict[str, object]:
    """Assess a single AI system and return risk scores plus deployment decision."""
    if inherent_risk_map is None: inherent_risk_map = DEFAULT_INHERENT_RISK
    system_type = system_row['system_type']
    inherent_risk_score = float(inherent_risk_map.get(system_type, 3.0))
    evidence_score = 0.0 if evidence_df is None or evidence_df.empty else evidence_completion_score(evidence_df)
    control_maturity_score = 1.0 if evidence_df is None or evidence_df.empty else control_maturity_from_evidence(evidence_df)
    residual_risk_score = calculate_residual_risk(inherent_risk_score, control_maturity_score)
    return {'system_id': system_row.get('system_id'), 'system_name': system_row.get('system_name'), 'system_type': system_type, 'risk_tier': system_row.get('risk_tier'), 'inherent_risk_score': inherent_risk_score, 'control_maturity_score': control_maturity_score, 'evidence_completion_score': evidence_score, 'residual_risk_score': residual_risk_score, 'deployment_recommendation': deployment_decision_from_residual_risk(residual_risk_score)}


def assess_system_inventory(inventory_df: pd.DataFrame, evidence_df: pd.DataFrame, system_id_col: str = 'system_id') -> pd.DataFrame:
    """Assess all systems in an inventory using evidence pack data."""
    return pd.DataFrame([assess_system_risk(system, evidence_df[evidence_df[system_id_col] == system[system_id_col]]) for _, system in inventory_df.iterrows()])
