from __future__ import annotations
from pathlib import Path
from typing import Iterable
import pandas as pd


def require_columns(df: pd.DataFrame, required_columns: Iterable[str], dataset_name: str = "dataset") -> None:
    """Raise a clear error if a dataframe is missing required columns."""
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"{dataset_name} is missing required columns: {', '.join(missing)}")


def ensure_parent_dir(path: str | Path) -> Path:
    """Create a file's parent directory and return the path as a Path object."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def yes_no_to_bool(series: pd.Series) -> pd.Series:
    """Convert Yes/No, True/False, and 1/0 style values into booleans."""
    return series.astype(str).str.strip().str.lower().map({'yes': True, 'no': False, 'true': True, 'false': False, '1': True, '0': False}).fillna(False).astype(bool)


def read_csv_checked(path: str | Path, required_columns: Iterable[str] | None = None, dataset_name: str = "dataset") -> pd.DataFrame:
    """Read a CSV file and optionally validate required columns."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find {dataset_name}: {path}")
    df = pd.read_csv(path)
    if required_columns is not None:
        require_columns(df, required_columns, dataset_name=dataset_name)
    return df
