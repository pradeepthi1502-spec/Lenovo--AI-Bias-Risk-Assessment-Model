from __future__ import annotations
from pathlib import Path
import pandas as pd
from .data_validation import read_csv_checked, yes_no_to_bool

AI_DETECTION_REQUIRED_COLUMNS = ['student_id','gender','subject_area','socioeconomic_band','prior_ai_experience','actual_ai_use','detector_score','detection_flag','human_review_completed','misconduct_case_opened','appeal_submitted','appeal_successful']


def load_ai_detection_data(path: str | Path) -> pd.DataFrame:
    """Load the synthetic AI detection dataset and normalise audit fields."""
    df = read_csv_checked(path, required_columns=AI_DETECTION_REQUIRED_COLUMNS, dataset_name='synthetic AI detection dataset')
    for col in ['actual_ai_use','detection_flag','human_review_completed','misconduct_case_opened','appeal_submitted','appeal_successful']:
        df[col] = yes_no_to_bool(df[col])
    df['detector_score'] = pd.to_numeric(df['detector_score'], errors='coerce').fillna(0.0)
    return df
