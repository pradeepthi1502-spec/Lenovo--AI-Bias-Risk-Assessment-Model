from __future__ import annotations
from pathlib import Path
import pandas as pd

EXPECTED_OULAD_FILES = ['studentInfo.csv','studentVle.csv','studentAssessment.csv','assessments.csv','vle.csv','courses.csv','studentRegistration.csv']


def check_oulad_files(oulad_dir: str | Path) -> pd.DataFrame:
    """Return availability status for the expected OULAD CSV files."""
    oulad_dir = Path(oulad_dir)
    return pd.DataFrame([{'file': f, 'path': str(oulad_dir / f), 'available': (oulad_dir / f).exists()} for f in EXPECTED_OULAD_FILES])


def load_oulad_tables(oulad_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Load available OULAD CSV tables into a dictionary."""
    oulad_dir = Path(oulad_dir)
    status = check_oulad_files(oulad_dir)
    missing = status.loc[~status['available'], 'file'].tolist()
    if missing:
        raise FileNotFoundError('Missing OULAD files: ' + ', '.join(missing) + '. Download OULAD and place the CSV files in data/raw/oulad/.')
    return {f.replace('.csv',''): pd.read_csv(oulad_dir / f) for f in EXPECTED_OULAD_FILES}


def build_oulad_student_features(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Create a student-level feature table for VLE fairness auditing."""
    student_info = tables['studentInfo']; student_vle = tables['studentVle']; student_assessment = tables['studentAssessment']; assessments = tables['assessments']
    key_cols = ['code_module', 'code_presentation', 'id_student']
    vle_features = student_vle.groupby(key_cols).agg(total_vle_clicks=('sum_click','sum'), avg_vle_clicks_per_record=('sum_click','mean'), vle_activity_records=('sum_click','count'), first_vle_activity_day=('date','min'), last_vle_activity_day=('date','max')).reset_index()
    assessment_joined = student_assessment.merge(assessments, on='id_assessment', how='left', suffixes=('_student','_assessment'))
    assessment_features = assessment_joined.groupby(key_cols).agg(assessment_score_avg=('score','mean'), assessment_score_min=('score','min'), assessment_score_max=('score','max'), assessments_submitted=('id_assessment','count'), avg_days_submitted=('date_submitted','mean')).reset_index()
    features = student_info.merge(vle_features, on=key_cols, how='left').merge(assessment_features, on=key_cols, how='left')
    for col in ['total_vle_clicks','avg_vle_clicks_per_record','vle_activity_records','assessments_submitted']:
        features[col] = features[col].fillna(0)
    if 'assessment_score_avg' in features.columns:
        features['assessment_score_avg'] = features['assessment_score_avg'].fillna(features['assessment_score_avg'].median())
    features['is_unsuccessful_outcome'] = features['final_result'].isin(['Fail','Withdrawn'])
    features['low_engagement_flag'] = features['total_vle_clicks'] < features['total_vle_clicks'].quantile(0.25)
    return features
