from __future__ import annotations

import pandas as pd

from ai_governance_toolkit.analytics.fairness_metrics import (
    binary_classification_rates_by_group,
    classify_gap,
    largest_group_gap,
    rate_by_group,
    summarise_fairness_gaps,
)


def test_rate_by_group_returns_percentage_rates() -> None:
    df = pd.DataFrame(
        {
            "gender": ["Female", "Female", "Male", "Male"],
            "flag": [True, False, True, True],
        }
    )

    result = rate_by_group(df, group_col="gender", outcome_col="flag")

    female_rate = result.loc[result["gender"] == "Female", "rate"].iloc[0]
    male_rate = result.loc[result["gender"] == "Male", "rate"].iloc[0]

    assert female_rate == 50.0
    assert male_rate == 100.0


def test_largest_group_gap_calculates_difference() -> None:
    summary = pd.DataFrame({"group": ["A", "B", "C"], "rate": [10.0, 35.0, 20.0]})

    gap = largest_group_gap(summary, "rate")

    assert gap == 25.0


def test_classify_gap_thresholds() -> None:
    assert classify_gap(3.0) == "Very low"
    assert classify_gap(7.0) == "Low"
    assert classify_gap(12.0) == "Moderate"
    assert classify_gap(17.0) == "High"
    assert classify_gap(25.0) == "Very high"


def test_summarise_fairness_gaps_returns_expected_columns() -> None:
    summary = pd.DataFrame(
        {
            "gender": ["Female", "Male"],
            "false_positive_rate": [12.0, 4.0],
            "false_negative_rate": [8.0, 18.0],
        }
    )

    result = summarise_fairness_gaps(
        summary,
        ["false_positive_rate", "false_negative_rate"],
    )

    assert set(result.columns) == {
        "metric",
        "largest_gap_percentage_points",
        "risk_band",
    }
    assert len(result) == 2


def test_binary_classification_rates_by_group(ai_detection_sample) -> None:
    result = binary_classification_rates_by_group(
        ai_detection_sample,
        group_col="gender",
        actual_col="actual_ai_use",
        predicted_col="detection_flag",
    )

    assert "false_positive_rate" in result.columns
    assert "false_negative_rate" in result.columns
    assert "flag_rate" in result.columns
    assert set(result["gender"]) == {"Female", "Male"}
