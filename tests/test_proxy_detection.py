from __future__ import annotations

import pandas as pd

from ai_governance_toolkit.analytics.proxy_detection import (
    classify_proxy_association,
    correlation_ratio,
    cramers_v,
    proxy_association_scan,
)


def test_cramers_v_returns_value_between_zero_and_one() -> None:
    x = pd.Series(["A", "A", "B", "B", "B"])
    y = pd.Series(["X", "X", "Y", "Y", "X"])

    score = cramers_v(x, y)

    assert 0.0 <= score <= 1.0


def test_correlation_ratio_returns_value_between_zero_and_one() -> None:
    categories = pd.Series(["A", "A", "B", "B"])
    measurements = pd.Series([1.0, 2.0, 10.0, 11.0])

    score = correlation_ratio(categories, measurements)

    assert 0.0 <= score <= 1.0
    assert score > 0.0


def test_classify_proxy_association() -> None:
    assert classify_proxy_association(0.05) == "Very low"
    assert classify_proxy_association(0.15) == "Low"
    assert classify_proxy_association(0.25) == "Moderate"
    assert classify_proxy_association(0.35) == "High"


def test_proxy_association_scan_ranks_variables() -> None:
    df = pd.DataFrame(
        {
            "gender": ["Female", "Female", "Male", "Male", "Female", "Male"],
            "subject_area": ["Arts", "Health", "STEM", "STEM", "Arts", "Business"],
            "weekly_hours": [1.0, 2.0, 5.0, 6.0, 1.5, 4.5],
        }
    )

    result = proxy_association_scan(
        df,
        protected_col="gender",
        candidate_cols=["subject_area", "weekly_hours"],
    )

    assert len(result) == 2
    assert "association_score" in result.columns
    assert result["association_score"].is_monotonic_decreasing
