from __future__ import annotations

from ai_governance_toolkit.analytics.gender_ai_gap_monitor import (
    ai_gap_summary_by_gender,
    build_gender_ai_gap_monitoring,
)


def test_build_gender_ai_gap_monitoring_groups_by_gender_and_subject(ai_proficiency_sample) -> None:
    result = build_gender_ai_gap_monitoring(ai_proficiency_sample)

    assert "student_count" in result.columns
    assert "avg_weekly_genai_use_hours" in result.columns
    assert "ai_training_completion_rate" in result.columns
    assert {"gender", "subject_area"}.issubset(result.columns)


def test_build_gender_ai_gap_monitoring_rates_are_percentages(ai_proficiency_sample) -> None:
    result = build_gender_ai_gap_monitoring(ai_proficiency_sample)

    assert result["ai_training_completion_rate"].between(0, 100).all()
    assert result["career_ai_tool_usage_rate"].between(0, 100).all()
    assert result["academic_misconduct_flag_rate"].between(0, 100).all()


def test_ai_gap_summary_by_gender(ai_proficiency_sample) -> None:
    result = ai_gap_summary_by_gender(ai_proficiency_sample)

    assert "gender" in result.columns
    assert "subject_area" not in result.columns
    assert set(result["gender"]) == {"Female", "Male"}
