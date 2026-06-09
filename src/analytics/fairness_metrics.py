from __future__ import annotations
from dataclasses import dataclass
import pandas as pd

@dataclass
class FairnessGapResult:
    """Container for a fairness gap result."""
    metric: str
    largest_gap: float
    risk_band: str


def rate_by_group(df: pd.DataFrame, group_col: str, outcome_col: str, as_percentage: bool = True) -> pd.DataFrame:
    """Calculate outcome rate by group."""
    result = df.groupby(group_col, dropna=False).agg(record_count=(outcome_col, 'count'), rate=(outcome_col, 'mean')).reset_index()
    if as_percentage:
        result['rate'] = (result['rate'] * 100).round(2)
    return result


def largest_group_gap(summary_df: pd.DataFrame, metric_col: str) -> float:
    """Calculate the largest gap across groups for a metric column."""
    return float(summary_df[metric_col].max() - summary_df[metric_col].min())


def classify_gap(gap_percentage_points: float) -> str:
    """Classify a fairness gap using percentage-point thresholds."""
    if gap_percentage_points < 5: return 'Very low'
    if gap_percentage_points < 10: return 'Low'
    if gap_percentage_points < 15: return 'Moderate'
    if gap_percentage_points < 20: return 'High'
    return 'Very high'


def summarise_fairness_gaps(summary_df: pd.DataFrame, metric_cols: list[str]) -> pd.DataFrame:
    """Create a table of largest subgroup gaps for selected metrics."""
    return pd.DataFrame([{'metric': metric, 'largest_gap_percentage_points': round(largest_group_gap(summary_df, metric), 2), 'risk_band': classify_gap(largest_group_gap(summary_df, metric))} for metric in metric_cols])


def binary_classification_rates_by_group(df: pd.DataFrame, group_col: str, actual_col: str, predicted_col: str) -> pd.DataFrame:
    """Calculate FPR, FNR, TPR, TNR, and flag rate by group."""
    rows = []
    for group, sub in df.groupby(group_col, dropna=False):
        actual = sub[actual_col].astype(bool); pred = sub[predicted_col].astype(bool)
        tp = int((pred & actual).sum()); tn = int((~pred & ~actual).sum()); fp = int((pred & ~actual).sum()); fn = int((~pred & actual).sum())
        rows.append({group_col: group, 'record_count': len(sub), 'true_positive': tp, 'true_negative': tn, 'false_positive': fp, 'false_negative': fn, 'false_positive_rate': round((fp/(fp+tn) if (fp+tn) else 0)*100, 2), 'false_negative_rate': round((fn/(fn+tp) if (fn+tp) else 0)*100, 2), 'true_positive_rate': round((tp/(tp+fn) if (tp+fn) else 0)*100, 2), 'true_negative_rate': round((tn/(tn+fp) if (tn+fp) else 0)*100, 2), 'flag_rate': round(pred.mean()*100 if len(pred) else 0, 2), 'accuracy': round(((tp+tn)/len(sub) if len(sub) else 0)*100, 2)})
    return pd.DataFrame(rows)
