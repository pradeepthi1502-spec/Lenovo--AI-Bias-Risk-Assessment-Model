from __future__ import annotations
import pandas as pd
from .control_maturity import evidence_completion_score

DEFAULT_REQUIRED_EVIDENCE = ['System description','Decision influence map','Data dictionary','Demographic coverage summary','Fairness and performance test results','Human oversight procedure','Vendor model card','DPIA summary','Equality impact assessment','Student notice and explanation text','Appeal route','Rollback or suspension plan','Monitoring schedule','Incident log']


def validate_evidence_pack(evidence_df: pd.DataFrame, required_items: list[str] | None = None, item_col: str = 'evidence_item', status_col: str = 'status') -> pd.DataFrame:
    """Validate whether a system evidence pack contains required items."""
    required_items = DEFAULT_REQUIRED_EVIDENCE if required_items is None else required_items
    records = []
    for item in required_items:
        matches = evidence_df[evidence_df[item_col] == item]
        status = 'Missing' if matches.empty else str(matches.iloc[0][status_col])
        records.append({'evidence_item': item, 'status': status, 'is_satisfactory': status == 'Provided', 'is_missing_or_partial': status in ['Missing','Partial']})
    return pd.DataFrame(records)


def validate_evidence_by_system(evidence_df: pd.DataFrame, system_id_col: str = 'system_id') -> pd.DataFrame:
    """Create evidence validation summary for every AI system."""
    rows = []
    for system_id, sub in evidence_df.groupby(system_id_col):
        validation = validate_evidence_pack(sub)
        rows.append({'system_id': system_id, 'evidence_completion_score': evidence_completion_score(sub), 'provided_count': int((validation['status'] == 'Provided').sum()), 'partial_count': int((validation['status'] == 'Partial').sum()), 'missing_count': int((validation['status'] == 'Missing').sum()), 'approval_blocker': bool((validation['status'] == 'Missing').any())})
    return pd.DataFrame(rows)
