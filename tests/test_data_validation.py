from __future__ import annotations

import pandas as pd
import pytest

from ai_governance_toolkit.data_ingestion.data_validation import (
    require_columns,
    yes_no_to_bool,
)


def test_yes_no_to_bool_converts_common_values() -> None:
    series = pd.Series(["Yes", "No", "true", "false", "1", "0"])

    result = yes_no_to_bool(series)

    assert result.tolist() == [True, False, True, False, True, False]


def test_require_columns_passes_when_columns_exist() -> None:
    df = pd.DataFrame({"a": [1], "b": [2]})

    require_columns(df, ["a", "b"], dataset_name="test")


def test_require_columns_raises_when_missing() -> None:
    df = pd.DataFrame({"a": [1]})

    with pytest.raises(ValueError):
        require_columns(df, ["a", "b"], dataset_name="test")
