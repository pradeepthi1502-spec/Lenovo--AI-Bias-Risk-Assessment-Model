from __future__ import annotations

import pandas as pd

from ai_governance_toolkit.pipelines.current_deployment_risk_monitor import (
    run_current_deployment_monitor,
)
from ai_governance_toolkit.pipelines.future_deployment_readiness import (
    run_future_deployment_readiness,
)
from ai_governance_toolkit.pipelines.integrated_assessment_pipeline import (
    run_integrated_assessment,
)


def test_run_current_deployment_monitor(ai_detection_sample, ai_proficiency_sample) -> None:
    outputs = run_current_deployment_monitor(
        ai_detection_df=ai_detection_sample,
        ai_proficiency_df=ai_proficiency_sample,
    )

    assert "ai_detection_audit_ready" in outputs
    assert "ai_detection_fairness_summary" in outputs
    assert "gender_ai_gap_monitoring" in outputs


def test_run_future_deployment_readiness(inventory_sample, evidence_sample) -> None:
    outputs = run_future_deployment_readiness(
        inventory_df=inventory_sample,
        evidence_df=evidence_sample,
    )

    assert "evidence_validation" in outputs
    assert "risk_assessment" in outputs
    assert isinstance(outputs["risk_assessment"], pd.DataFrame)


def test_run_integrated_assessment(
    tmp_path,
    ai_detection_sample,
    ai_proficiency_sample,
    inventory_sample,
    evidence_sample,
) -> None:
    outputs = run_integrated_assessment(
        ai_detection_df=ai_detection_sample,
        ai_proficiency_df=ai_proficiency_sample,
        inventory_df=inventory_sample,
        evidence_df=evidence_sample,
        output_dir=tmp_path,
    )

    assert "ai_detection_audit_ready" in outputs
    assert "gender_ai_gap_monitoring" in outputs
    assert "system_risk_assessment" in outputs

    exported_files = list(tmp_path.glob("*.csv"))
    assert exported_files
