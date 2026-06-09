from __future__ import annotations
from pathlib import Path
import pandas as pd
from ai_governance_toolkit.data_ingestion.load_synthetic_detection_data import load_ai_detection_data
from ai_governance_toolkit.data_ingestion.data_validation import yes_no_to_bool
from ai_governance_toolkit.analytics.ai_detection_bias_audit import run_ai_detection_bias_audit
from ai_governance_toolkit.analytics.gender_ai_gap_monitor import build_gender_ai_gap_monitoring
from ai_governance_toolkit.governance.risk_scoring_engine import assess_system_inventory
from ai_governance_toolkit.reporting.dashboard_data_export import export_outputs


def load_ai_proficiency_data(path: str | Path) -> pd.DataFrame:
    """Load and normalise the synthetic AI proficiency survey dataset."""
    df = pd.read_csv(path)
    for col in ['ai_training_completed','career_ai_tool_used','academic_misconduct_flag']:
        if col in df.columns: df[col] = yes_no_to_bool(df[col])
    for col in ['weekly_genai_use_hours','ai_confidence_score_1_5','assessment_score_after_ai_integration']:
        if col in df.columns: df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def run_partner_demo_pipeline(ai_detection_path: str | Path, ai_proficiency_path: str | Path, inventory_path: str | Path, evidence_path: str | Path, output_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Run the full partner demo pipeline from CSV inputs."""
    ai_detection_df = load_ai_detection_data(ai_detection_path); ai_proficiency_df = load_ai_proficiency_data(ai_proficiency_path); inventory_df = pd.read_csv(inventory_path); evidence_df = pd.read_csv(evidence_path)
    detection_outputs = run_ai_detection_bias_audit(ai_detection_df)
    outputs = {'ai_detection_audit_ready': detection_outputs['audit_ready_data'], 'ai_detection_fairness_summary': detection_outputs['fairness_summary'], 'ai_detection_fairness_gaps': detection_outputs['fairness_gaps'], 'gender_ai_gap_monitoring': build_gender_ai_gap_monitoring(ai_proficiency_df), 'system_risk_assessment': assess_system_inventory(inventory_df, evidence_df)}
    export_outputs(outputs, output_dir)
    return outputs
