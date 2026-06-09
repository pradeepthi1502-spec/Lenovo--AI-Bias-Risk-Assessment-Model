from __future__ import annotations
import pandas as pd
from .fairness_metrics import summarise_fairness_gaps


def prepare_ai_detection_audit_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add audit-ready columns for AI detection tool analysis."""
    audit = df.copy()
    audit['is_false_positive'] = audit['detection_flag'].astype(bool) & ~audit['actual_ai_use'].astype(bool)
    audit['is_false_negative'] = ~audit['detection_flag'].astype(bool) & audit['actual_ai_use'].astype(bool)
    audit['is_true_positive'] = audit['detection_flag'].astype(bool) & audit['actual_ai_use'].astype(bool)
    audit['is_true_negative'] = ~audit['detection_flag'].astype(bool) & ~audit['actual_ai_use'].astype(bool)
    audit['case_escalated_after_flag'] = audit['detection_flag'].astype(bool) & audit['misconduct_case_opened'].astype(bool)
    audit['appeal_success_after_case'] = audit['appeal_submitted'].astype(bool) & audit['appeal_successful'].astype(bool)
    if 'detector_score' in audit.columns:
        audit['detector_risk_band'] = pd.cut(audit['detector_score'], bins=[-0.001,0.30,0.50,0.70,1.00], labels=['Low','Borderline','High','Very High'])
    return audit


def ai_detection_fairness_summary(audit_df: pd.DataFrame, group_col: str = 'gender') -> pd.DataFrame:
    """Summarise AI detection fairness metrics by group."""
    summary = audit_df.groupby(group_col, dropna=False).agg(student_count=('student_id','count'), actual_ai_use_rate=('actual_ai_use','mean'), detection_flag_rate=('detection_flag','mean'), false_positive_rate=('is_false_positive','mean'), false_negative_rate=('is_false_negative','mean'), human_review_rate=('human_review_completed','mean'), misconduct_case_rate=('misconduct_case_opened','mean'), appeal_submission_rate=('appeal_submitted','mean'), appeal_success_rate=('appeal_successful','mean'), avg_detector_score=('detector_score','mean')).reset_index()
    for col in ['actual_ai_use_rate','detection_flag_rate','false_positive_rate','false_negative_rate','human_review_rate','misconduct_case_rate','appeal_submission_rate','appeal_success_rate']:
        summary[col] = (summary[col] * 100).round(2)
    summary['avg_detector_score'] = summary['avg_detector_score'].round(3)
    return summary


def run_ai_detection_bias_audit(df: pd.DataFrame, group_col: str = 'gender') -> dict[str, pd.DataFrame]:
    """Run the complete AI detection fairness audit."""
    audit = prepare_ai_detection_audit_data(df)
    summary = ai_detection_fairness_summary(audit, group_col=group_col)
    gaps = summarise_fairness_gaps(summary, ['detection_flag_rate','false_positive_rate','false_negative_rate','human_review_rate','misconduct_case_rate','appeal_success_rate'])
    return {'audit_ready_data': audit, 'fairness_summary': summary, 'fairness_gaps': gaps}
