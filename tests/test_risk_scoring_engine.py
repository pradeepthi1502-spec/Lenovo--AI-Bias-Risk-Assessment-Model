from __future__ import annotations

import pandas as pd

from ai_governance_toolkit.governance.deployment_decision_rules import (
    deployment_decision_from_residual_risk,
)
from ai_governance_toolkit.governance.risk_scoring_engine import (
    assess_system_inventory,
    assess_system_risk,
    calculate_inherent_risk,
    calculate_residual_risk,
)


def test_calculate_inherent_risk_averages_scores() -> None:
    result = calculate_inherent_risk(
        {
            "impact_severity": 5,
            "decision_criticality": 4,
            "scale": 3,
        }
    )

    assert result == 4.0


def test_calculate_residual_risk_reduces_inherent_risk() -> None:
    inherent = 4.0
    residual = calculate_residual_risk(
        inherent_risk_score=inherent,
        control_maturity_score=5.0,
    )

    assert residual < inherent
    assert residual == 2.0


def test_deployment_decision_from_residual_risk() -> None:
    assert deployment_decision_from_residual_risk(1.5) == "Approve"
    assert deployment_decision_from_residual_risk(2.2) == "Approve with monitoring"
    assert deployment_decision_from_residual_risk(3.0) == "Pilot only"
    assert deployment_decision_from_residual_risk(3.8) == "Pause deployment"
    assert deployment_decision_from_residual_risk(4.5) == "Reject / prohibit"


def test_assess_system_risk_returns_expected_fields(inventory_sample, evidence_sample) -> None:
    system = inventory_sample.iloc[0]
    evidence = evidence_sample[evidence_sample["system_id"] == system["system_id"]]

    result = assess_system_risk(system, evidence)

    expected_keys = {
        "system_id",
        "system_name",
        "system_type",
        "risk_tier",
        "inherent_risk_score",
        "control_maturity_score",
        "evidence_completion_score",
        "residual_risk_score",
        "deployment_recommendation",
    }

    assert expected_keys.issubset(result.keys())


def test_assess_system_inventory_returns_dataframe(inventory_sample, evidence_sample) -> None:
    result = assess_system_inventory(inventory_sample, evidence_sample)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == len(inventory_sample)
    assert "deployment_recommendation" in result.columns
