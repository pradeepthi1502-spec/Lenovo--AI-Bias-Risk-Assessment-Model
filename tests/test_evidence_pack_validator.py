from __future__ import annotations

import pandas as pd

from ai_governance_toolkit.governance.evidence_pack_validator import (
    DEFAULT_REQUIRED_EVIDENCE,
    validate_evidence_by_system,
    validate_evidence_pack,
)


def test_validate_evidence_pack_marks_missing_items(evidence_sample) -> None:
    system_evidence = evidence_sample[evidence_sample["system_id"] == "AI-001"]

    result = validate_evidence_pack(system_evidence)

    assert len(result) == len(DEFAULT_REQUIRED_EVIDENCE)
    assert "is_missing_or_partial" in result.columns
    assert result["is_missing_or_partial"].any()


def test_validate_evidence_pack_marks_provided_as_satisfactory() -> None:
    evidence = pd.DataFrame(
        [
            {"evidence_item": "System description", "status": "Provided"},
            {"evidence_item": "Decision influence map", "status": "Provided"},
        ]
    )

    result = validate_evidence_pack(
        evidence,
        required_items=["System description", "Decision influence map"],
    )

    assert result["is_satisfactory"].all()


def test_validate_evidence_by_system_returns_one_row_per_system(evidence_sample) -> None:
    result = validate_evidence_by_system(evidence_sample)

    assert set(result["system_id"]) == {"AI-001", "AI-002"}
    assert "evidence_completion_score" in result.columns
    assert "approval_blocker" in result.columns
