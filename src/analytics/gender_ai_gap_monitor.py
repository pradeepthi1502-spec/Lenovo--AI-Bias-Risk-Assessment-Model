from __future__ import annotations
import pandas as pd


def build_gender_ai_gap_monitoring(df: pd.DataFrame, group_cols: list[str] | None = None) -> pd.DataFrame:
    """Aggregate AI proficiency survey data for dashboard monitoring."""
    if group_cols is None: group_cols = ['gender','subject_area']
    summary = df.groupby(group_cols, dropna=False).agg(student_count=('student_id','count'), avg_weekly_genai_use_hours=('weekly_genai_use_hours','mean'), avg_ai_confidence_score=('ai_confidence_score_1_5','mean'), ai_training_completion_rate=('ai_training_completed','mean'), career_ai_tool_usage_rate=('career_ai_tool_used','mean'), avg_assessment_score_after_ai_integration=('assessment_score_after_ai_integration','mean'), academic_misconduct_flag_rate=('academic_misconduct_flag','mean')).reset_index()
    for col in ['ai_training_completion_rate','career_ai_tool_usage_rate','academic_misconduct_flag_rate']:
        summary[col] = (summary[col] * 100).round(2)
    for col in ['avg_weekly_genai_use_hours','avg_ai_confidence_score','avg_assessment_score_after_ai_integration']:
        summary[col] = summary[col].round(2)
    return summary


def ai_gap_summary_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    """Create an overall gender-level summary of AI access and usage indicators."""
    return build_gender_ai_gap_monitoring(df, group_cols=['gender'])
