from __future__ import annotations
import pandas as pd


def representation_summary(df: pd.DataFrame, group_col: str, minimum_subgroup_size: int = 100) -> pd.DataFrame:
    """Summarise representation for a protected or monitored group."""
    if group_col not in df.columns:
        raise ValueError(f"Column not found: {group_col}")
    summary = df.groupby(group_col, dropna=False).size().reset_index(name='record_count')
    total = summary['record_count'].sum()
    summary['percentage'] = (summary['record_count'] / total * 100).round(2)
    summary['sample_size_warning'] = summary['record_count'] < minimum_subgroup_size
    return summary.sort_values('record_count', ascending=False)


def missingness_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing value counts and percentages for every column."""
    summary = pd.DataFrame({'column': df.columns, 'missing_count': [df[col].isna().sum() for col in df.columns], 'total_count': len(df)})
    summary['missing_percentage'] = (summary['missing_count'] / summary['total_count'] * 100).round(2)
    return summary.sort_values('missing_percentage', ascending=False)
