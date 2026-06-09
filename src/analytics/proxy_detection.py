from __future__ import annotations
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency


def cramers_v(x: pd.Series, y: pd.Series) -> float:
    """Calculate Cramer's V association between two categorical variables."""
    table = pd.crosstab(x.fillna('Missing'), y.fillna('Missing'))
    if table.shape[0] < 2 or table.shape[1] < 2: return 0.0
    chi2 = chi2_contingency(table)[0]; n = table.sum().sum(); r, k = table.shape; denom = n * min(k - 1, r - 1)
    return 0.0 if denom == 0 else float(np.sqrt(chi2 / denom))


def correlation_ratio(categories: pd.Series, measurements: pd.Series) -> float:
    """Calculate categorical-continuous association."""
    valid = pd.DataFrame({'category': categories, 'measurement': measurements}).dropna()
    if valid.empty: return 0.0
    groups = valid.groupby('category')['measurement']; overall = valid['measurement'].mean()
    numerator = sum(len(g) * (g.mean() - overall) ** 2 for _, g in groups)
    denominator = sum((valid['measurement'] - overall) ** 2)
    return 0.0 if denominator == 0 else float(np.sqrt(numerator / denominator))


def classify_proxy_association(score: float) -> str:
    """Classify proxy association strength."""
    if score < 0.10: return 'Very low'
    if score < 0.20: return 'Low'
    if score < 0.30: return 'Moderate'
    return 'High'


def proxy_association_scan(df: pd.DataFrame, protected_col: str, candidate_cols: list[str]) -> pd.DataFrame:
    """Rank candidate proxy variables by association with a protected attribute."""
    rows = []
    for col in candidate_cols:
        if col not in df.columns: continue
        if pd.api.types.is_numeric_dtype(df[col]):
            score = correlation_ratio(df[protected_col], df[col]); method = 'correlation_ratio'
        else:
            score = cramers_v(df[col], df[protected_col]); method = 'cramers_v'
        rows.append({'variable': col, 'method': method, 'association_score': round(score, 3), 'proxy_risk_band': classify_proxy_association(score)})
    return pd.DataFrame(rows).sort_values('association_score', ascending=False).reset_index(drop=True) if rows else pd.DataFrame(columns=['variable','method','association_score','proxy_risk_band'])
