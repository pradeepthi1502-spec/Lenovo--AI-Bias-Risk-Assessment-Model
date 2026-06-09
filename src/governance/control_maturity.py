from __future__ import annotations
import pandas as pd
STATUS_SCORE_MAP = {'Provided': 1.0, 'Partial': 0.5, 'Missing': 0.0}


def evidence_completion_score(evidence_df: pd.DataFrame, status_col: str = 'status', scale_to_five: bool = True) -> float:
    """Calculate evidence completion score from evidence status values."""
    if evidence_df.empty: return 0.0
    score = float(evidence_df[status_col].map(STATUS_SCORE_MAP).fillna(0.0).mean())
    return round(score * 5 if scale_to_five else score, 2)


def control_maturity_from_evidence(evidence_df: pd.DataFrame, minimum_score: float = 1.0, maturity_adjustment: float = -0.3) -> float:
    """Estimate control maturity from evidence completion status."""
    score = evidence_completion_score(evidence_df, scale_to_five=True)
    return round(max(minimum_score, min(5.0, score + maturity_adjustment)), 2)


def evidence_summary_by_system(evidence_df: pd.DataFrame, system_id_col: str = 'system_id', status_col: str = 'status') -> pd.DataFrame:
    """Summarise evidence counts by system."""
    return evidence_df.groupby([system_id_col, status_col]).size().unstack(fill_value=0).reset_index()
