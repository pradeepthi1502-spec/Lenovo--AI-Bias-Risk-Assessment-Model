from __future__ import annotations
from pathlib import Path
import pandas as pd
from ai_governance_toolkit.analytics.ai_detection_bias_audit import run_ai_detection_bias_audit
from ai_governance_toolkit.analytics.gender_ai_gap_monitor import build_gender_ai_gap_monitoring
from ai_governance_toolkit.governance.risk_scoring_engine import assess_system_inventory
from ai_governance_toolkit.reporting.dashboard_data_export import export_outputs


def run_integrated_assessment(ai_detection_df: pd.DataFrame, ai_proficiency_df: pd.DataFrame, inventory_df: pd.DataFrame, evidence_df: pd.DataFrame, output_dir: str | Path | None = None) -> dict[str, pd.DataFrame]:
    """Run the integrated governance assessment pipeline."""
    detection_outputs = run_ai_detection_bias_audit(ai_detection_df)
    outputs = {'ai_detection_audit_ready': detection_outputs['audit_ready_data'], 'ai_detection_fairness_summary': detection_outputs['fairness_summary'], 'ai_detection_fairness_gaps': detection_outputs['fairness_gaps'], 'gender_ai_gap_monitoring': build_gender_ai_gap_monitoring(ai_proficiency_df), 'system_risk_assessment': assess_system_inventory(inventory_df, evidence_df)}
    if output_dir is not None: export_outputs(outputs, output_dir)
    return outputs
