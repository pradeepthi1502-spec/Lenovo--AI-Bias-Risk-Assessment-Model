from __future__ import annotations
import pandas as pd
from ai_governance_toolkit.analytics.ai_detection_bias_audit import run_ai_detection_bias_audit
from ai_governance_toolkit.analytics.gender_ai_gap_monitor import build_gender_ai_gap_monitoring


def run_current_deployment_monitor(ai_detection_df: pd.DataFrame | None = None, ai_proficiency_df: pd.DataFrame | None = None) -> dict[str, pd.DataFrame]:
    """Run audits for current university AI deployments."""
    outputs: dict[str, pd.DataFrame] = {}
    if ai_detection_df is not None:
        detection_outputs = run_ai_detection_bias_audit(ai_detection_df)
        outputs.update({'ai_detection_audit_ready': detection_outputs['audit_ready_data'], 'ai_detection_fairness_summary': detection_outputs['fairness_summary'], 'ai_detection_fairness_gaps': detection_outputs['fairness_gaps']})
    if ai_proficiency_df is not None:
        outputs['gender_ai_gap_monitoring'] = build_gender_ai_gap_monitoring(ai_proficiency_df)
    return outputs
