from __future__ import annotations

from ai_governance_toolkit.analytics.ai_detection_bias_audit import (
    ai_detection_fairness_summary,
    prepare_ai_detection_audit_data,
    run_ai_detection_bias_audit,
)


def test_prepare_ai_detection_audit_data_adds_error_columns(ai_detection_sample) -> None:
    result = prepare_ai_detection_audit_data(ai_detection_sample)

    expected_columns = {
        "is_false_positive",
        "is_false_negative",
        "is_true_positive",
        "is_true_negative",
        "case_escalated_after_flag",
        "appeal_success_after_case",
    }

    assert expected_columns.issubset(result.columns)
    assert result["is_false_positive"].sum() == 1
    assert result["is_false_negative"].sum() == 1


def test_ai_detection_fairness_summary_has_group_metrics(ai_detection_sample) -> None:
    audit = prepare_ai_detection_audit_data(ai_detection_sample)
    summary = ai_detection_fairness_summary(audit)

    assert set(summary["gender"]) == {"Female", "Male"}
    assert "false_positive_rate" in summary.columns
    assert "false_negative_rate" in summary.columns
    assert "avg_detector_score" in summary.columns


def test_run_ai_detection_bias_audit_returns_three_outputs(ai_detection_sample) -> None:
    outputs = run_ai_detection_bias_audit(ai_detection_sample)

    assert set(outputs.keys()) == {
        "audit_ready_data",
        "fairness_summary",
        "fairness_gaps",
    }
    assert not outputs["audit_ready_data"].empty
    assert not outputs["fairness_summary"].empty
    assert not outputs["fairness_gaps"].empty
