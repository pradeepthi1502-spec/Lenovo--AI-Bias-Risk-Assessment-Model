from __future__ import annotations
import pandas as pd
from .proxy_detection import proxy_association_scan


def vle_fairness_summary(df: pd.DataFrame, group_col: str = 'gender') -> pd.DataFrame:
    """Summarise VLE engagement and outcome indicators by group."""
    summary = df.groupby(group_col, dropna=False).agg(student_count=('id_student','count'), avg_total_vle_clicks=('total_vle_clicks','mean'), avg_assessment_score=('assessment_score_avg','mean'), unsuccessful_outcome_rate=('is_unsuccessful_outcome','mean'), low_engagement_flag_rate=('low_engagement_flag','mean')).reset_index()
    summary['avg_total_vle_clicks'] = summary['avg_total_vle_clicks'].round(2)
    summary['avg_assessment_score'] = summary['avg_assessment_score'].round(2)
    summary['unsuccessful_outcome_rate'] = (summary['unsuccessful_outcome_rate'] * 100).round(2)
    summary['low_engagement_flag_rate'] = (summary['low_engagement_flag_rate'] * 100).round(2)
    return summary


def run_vle_engagement_audit(df: pd.DataFrame, protected_col: str = 'gender', candidate_proxy_cols: list[str] | None = None) -> dict[str, pd.DataFrame]:
    """Run fairness and proxy-risk checks for VLE analytics."""
    if candidate_proxy_cols is None:
        candidate_proxy_cols = ['region','highest_education','imd_band','age_band','num_of_prev_attempts','studied_credits','disability','code_module']
    return {'vle_fairness_summary': vle_fairness_summary(df, group_col=protected_col), 'proxy_association_summary': proxy_association_scan(df, protected_col=protected_col, candidate_cols=candidate_proxy_cols)}
