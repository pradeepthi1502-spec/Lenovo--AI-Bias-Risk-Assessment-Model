"""
Generate processed datasets for the Future17 AI Governance Risk Toolkit.

This script takes the two raw synthetic datasets:

1. data/raw/synthetic/synthetic_ai_detection_demo.csv
2. data/raw/synthetic/synthetic_ai_proficiency_survey_demo.csv

and creates processed / dashboard-ready datasets:

1. data/processed/ai_detection_audit_ready.csv
2. data/processed/gender_ai_gap_monitoring.csv
3. data/processed/ai_system_inventory_demo.csv
4. data/processed/governance_evidence_pack_demo.csv
5. data/processed/system_risk_assessment_demo.csv
6. data/processed/oulad_audit_ready_schema.csv

Important:
- This script does not use real student data.
- It processes synthetic demonstration data only.
- It is designed for public GitHub portfolio use.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


RAW_SYNTHETIC_DIR = Path("data/raw/synthetic")
PROCESSED_DIR = Path("data/processed")


def yes_no_to_bool(series: pd.Series) -> pd.Series:
    """Convert Yes/No, True/False, and boolean-like values into booleans."""
    return (
        series.astype(str)
        .str.strip()
        .str.lower()
        .map(
            {
                "yes": True,
                "no": False,
                "true": True,
                "false": False,
                "1": True,
                "0": False,
            }
        )
        .fillna(False)
        .astype(bool)
    )


def find_input_file(file_name: str) -> Path:
    """
    Find an input file either in data/raw/synthetic/ or in the current folder.

    This makes the script easier to run for GitHub users who may place the
    CSV files in different locations during testing.
    """
    expected_path = RAW_SYNTHETIC_DIR / file_name
    fallback_path = Path(file_name)

    if expected_path.exists():
        return expected_path

    if fallback_path.exists():
        return fallback_path

    raise FileNotFoundError(
        f"Could not find {file_name}. Place it in data/raw/synthetic/ "
        f"or in the current working directory."
    )


def process_ai_detection_data(input_path: Path) -> pd.DataFrame:
    """
    Convert the raw synthetic AI detection dataset into an audit-ready dataset.

    Adds:
    - boolean audit columns
    - false positive / false negative indicators
    - true positive / true negative indicators
    - case escalation indicator
    - appeal success after case indicator
    - detector risk band
    """

    df = pd.read_csv(input_path)

    required_columns = [
        "student_id",
        "gender",
        "subject_area",
        "socioeconomic_band",
        "prior_ai_experience",
        "actual_ai_use",
        "detector_score",
        "detection_flag",
        "human_review_completed",
        "misconduct_case_opened",
        "appeal_submitted",
        "appeal_successful",
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(
            "AI detection input file is missing required columns: "
            + ", ".join(missing_columns)
        )

    processed = df.copy()

    bool_columns = [
        "actual_ai_use",
        "detection_flag",
        "human_review_completed",
        "misconduct_case_opened",
        "appeal_submitted",
        "appeal_successful",
    ]

    for col in bool_columns:
        processed[col] = yes_no_to_bool(processed[col])

    processed["detector_score"] = pd.to_numeric(
        processed["detector_score"],
        errors="coerce",
    ).fillna(0)

    processed["is_false_positive"] = (
        processed["detection_flag"] & ~processed["actual_ai_use"]
    )
    processed["is_false_negative"] = (
        ~processed["detection_flag"] & processed["actual_ai_use"]
    )
    processed["is_true_positive"] = (
        processed["detection_flag"] & processed["actual_ai_use"]
    )
    processed["is_true_negative"] = (
        ~processed["detection_flag"] & ~processed["actual_ai_use"]
    )

    processed["case_escalated_after_flag"] = (
        processed["detection_flag"] & processed["misconduct_case_opened"]
    )
    processed["appeal_success_after_case"] = (
        processed["appeal_submitted"] & processed["appeal_successful"]
    )

    processed["detector_risk_band"] = pd.cut(
        processed["detector_score"],
        bins=[-0.001, 0.30, 0.50, 0.70, 1.00],
        labels=["Low", "Borderline", "High", "Very High"],
    )

    processed["audit_note"] = (
        "Synthetic audit-ready record. Not real student data."
    )

    return processed


def build_ai_detection_fairness_summary(audit_df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a subgroup-level fairness summary for AI detection auditing.

    This is optional but useful for dashboarding and sanity checks.
    """

    summary = (
        audit_df.groupby("gender", dropna=False)
        .agg(
            student_count=("student_id", "count"),
            actual_ai_use_rate=("actual_ai_use", "mean"),
            detection_flag_rate=("detection_flag", "mean"),
            false_positive_rate=("is_false_positive", "mean"),
            false_negative_rate=("is_false_negative", "mean"),
            human_review_rate=("human_review_completed", "mean"),
            misconduct_case_rate=("misconduct_case_opened", "mean"),
            appeal_submission_rate=("appeal_submitted", "mean"),
            appeal_success_rate=("appeal_successful", "mean"),
            avg_detector_score=("detector_score", "mean"),
        )
        .reset_index()
    )

    percentage_columns = [
        "actual_ai_use_rate",
        "detection_flag_rate",
        "false_positive_rate",
        "false_negative_rate",
        "human_review_rate",
        "misconduct_case_rate",
        "appeal_submission_rate",
        "appeal_success_rate",
    ]

    for col in percentage_columns:
        summary[col] = (summary[col] * 100).round(2)

    summary["avg_detector_score"] = summary["avg_detector_score"].round(3)

    return summary


def process_ai_proficiency_data(input_path: Path) -> pd.DataFrame:
    """
    Aggregate synthetic AI proficiency survey data into dashboard-ready form.

    Produces the Gender AI Gap Monitoring dataset grouped by:
    - gender
    - subject_area

    Metrics include:
    - average weekly AI use
    - average AI confidence
    - training completion rate
    - career AI tool usage rate
    - assessment score after AI integration
    - academic misconduct flag rate
    """

    df = pd.read_csv(input_path)

    required_columns = [
        "student_id",
        "gender",
        "subject_area",
        "socioeconomic_band",
        "ai_access_level",
        "weekly_genai_use_hours",
        "ai_confidence_score_1_5",
        "ai_training_completed",
        "career_ai_tool_used",
        "assessment_score_after_ai_integration",
        "academic_misconduct_flag",
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(
            "AI proficiency input file is missing required columns: "
            + ", ".join(missing_columns)
        )

    processed = df.copy()

    bool_columns = [
        "ai_training_completed",
        "career_ai_tool_used",
        "academic_misconduct_flag",
    ]

    for col in bool_columns:
        processed[col] = yes_no_to_bool(processed[col])

    numeric_columns = [
        "weekly_genai_use_hours",
        "ai_confidence_score_1_5",
        "assessment_score_after_ai_integration",
    ]

    for col in numeric_columns:
        processed[col] = pd.to_numeric(processed[col], errors="coerce")

    grouped = (
        processed.groupby(["gender", "subject_area"], dropna=False)
        .agg(
            student_count=("student_id", "count"),
            avg_weekly_genai_use_hours=("weekly_genai_use_hours", "mean"),
            avg_ai_confidence_score=("ai_confidence_score_1_5", "mean"),
            ai_training_completion_rate=("ai_training_completed", "mean"),
            career_ai_tool_usage_rate=("career_ai_tool_used", "mean"),
            avg_assessment_score_after_ai_integration=(
                "assessment_score_after_ai_integration",
                "mean",
            ),
            academic_misconduct_flag_rate=("academic_misconduct_flag", "mean"),
        )
        .reset_index()
    )

    percentage_columns = [
        "ai_training_completion_rate",
        "career_ai_tool_usage_rate",
        "academic_misconduct_flag_rate",
    ]

    for col in percentage_columns:
        grouped[col] = (grouped[col] * 100).round(2)

    grouped["avg_weekly_genai_use_hours"] = (
        grouped["avg_weekly_genai_use_hours"].round(2)
    )
    grouped["avg_ai_confidence_score"] = (
        grouped["avg_ai_confidence_score"].round(2)
    )
    grouped["avg_assessment_score_after_ai_integration"] = (
        grouped["avg_assessment_score_after_ai_integration"].round(2)
    )

    grouped["monitoring_note"] = (
        "Synthetic subgroup dashboard data. Not real student data."
    )

    return grouped


def build_ai_system_inventory_demo() -> pd.DataFrame:
    """
    Build a demo AI system inventory.

    This mirrors the governance requirement that every AI system should be
    registered before approval or deployment.
    """

    return pd.DataFrame(
        [
            {
                "system_id": "AI-001",
                "system_name": "Academic Integrity AI Detector",
                "system_type": "ai_detection_tool",
                "deployment_status": "Live",
                "owner_team": "Academic Registry",
                "vendor_type": "Third-party",
                "student_impact_area": "Academic misconduct",
                "risk_tier": "High",
                "human_review_required": True,
            },
            {
                "system_id": "AI-002",
                "system_name": "Student Support Chatbot",
                "system_type": "student_chatbot",
                "deployment_status": "Live",
                "owner_team": "Student Services",
                "vendor_type": "Third-party",
                "student_impact_area": "Student support",
                "risk_tier": "Moderate",
                "human_review_required": True,
            },
            {
                "system_id": "AI-003",
                "system_name": "VLE Engagement Analytics Dashboard",
                "system_type": "vle_engagement_analytics",
                "deployment_status": "Live",
                "owner_team": "Learning Analytics",
                "vendor_type": "Platform-integrated",
                "student_impact_area": "Learning support",
                "risk_tier": "Moderate",
                "human_review_required": True,
            },
            {
                "system_id": "AI-004",
                "system_name": "Career Services CV Reviewer",
                "system_type": "career_service_ai",
                "deployment_status": "Live",
                "owner_team": "Careers Service",
                "vendor_type": "Third-party",
                "student_impact_area": "Employability",
                "risk_tier": "Moderate",
                "human_review_required": False,
            },
            {
                "system_id": "AI-005",
                "system_name": "AI-Assisted Feedback Tool",
                "system_type": "ai_assisted_marking_feedback",
                "deployment_status": "Pilot",
                "owner_team": "Assessment Innovation",
                "vendor_type": "Third-party",
                "student_impact_area": "Assessment feedback",
                "risk_tier": "High",
                "human_review_required": True,
            },
            {
                "system_id": "AI-006",
                "system_name": "Early Alert Prediction Model",
                "system_type": "early_alert_prediction",
                "deployment_status": "Proposed",
                "owner_team": "Student Success",
                "vendor_type": "Internal / third-party hybrid",
                "student_impact_area": "Progression support",
                "risk_tier": "High",
                "human_review_required": True,
            },
        ]
    )


def build_governance_evidence_pack_demo() -> pd.DataFrame:
    """
    Build a demo evidence-pack status dataset.

    This reflects the framework requirement that AI systems must submit
    governance evidence before approval.
    """

    evidence_items = [
        "System description",
        "Decision influence map",
        "Data dictionary",
        "Demographic coverage summary",
        "Fairness and performance test results",
        "Human oversight procedure",
        "Vendor model card",
        "DPIA summary",
        "Equality impact assessment",
        "Student notice and explanation text",
        "Appeal route",
        "Rollback or suspension plan",
        "Monitoring schedule",
        "Incident log",
    ]

    system_ids = ["AI-001", "AI-002", "AI-003", "AI-004", "AI-005", "AI-006"]
    rng = np.random.default_rng(21)

    rows = []

    for system_id in system_ids:
        for item in evidence_items:
            if system_id == "AI-001" and item in [
                "Fairness and performance test results",
                "Appeal route",
                "Human oversight procedure",
            ]:
                status = rng.choice(["Partial", "Missing"], p=[0.65, 0.35])
            elif system_id in ["AI-005", "AI-006"]:
                status = rng.choice(
                    ["Provided", "Partial", "Missing"],
                    p=[0.42, 0.38, 0.20],
                )
            else:
                status = rng.choice(
                    ["Provided", "Partial", "Missing"],
                    p=[0.62, 0.28, 0.10],
                )

            rows.append(
                {
                    "system_id": system_id,
                    "evidence_item": item,
                    "status": status,
                    "is_required_for_approval": True,
                }
            )

    return pd.DataFrame(rows)


def build_system_risk_assessment_demo(
    inventory_df: pd.DataFrame,
    evidence_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build a processed system-level risk assessment dataset.

    Score convention:
    - inherent_risk_score: higher means riskier
    - control_maturity_score: higher means stronger controls
    - evidence_completion_score: higher means stronger evidence
    - residual_risk_score: higher means more remaining risk after controls
    """

    inherent_risk_map = {
        "ai_detection_tool": 4.5,
        "student_chatbot": 3.1,
        "vle_engagement_analytics": 3.4,
        "career_service_ai": 3.0,
        "ai_assisted_marking_feedback": 4.2,
        "early_alert_prediction": 4.1,
    }

    rows = []

    for _, system in inventory_df.iterrows():
        system_id = system["system_id"]
        system_type = system["system_type"]

        evidence_subset = evidence_df[evidence_df["system_id"] == system_id]

        provided_rate = (evidence_subset["status"] == "Provided").mean()
        partial_rate = (evidence_subset["status"] == "Partial").mean()

        evidence_completion_score = round(
            (provided_rate + 0.5 * partial_rate) * 5,
            2,
        )

        inherent_risk_score = inherent_risk_map.get(system_type, 3.0)

        control_maturity_score = round(
            max(1.0, min(5.0, evidence_completion_score - 0.3)),
            2,
        )

        control_reduction_factor = 0.50

        residual_risk_score = round(
            inherent_risk_score
            * (1 - (control_maturity_score / 5) * control_reduction_factor),
            2,
        )

        if residual_risk_score < 2.0:
            deployment_recommendation = "Approve"
        elif residual_risk_score < 2.8:
            deployment_recommendation = "Approve with monitoring"
        elif residual_risk_score < 3.5:
            deployment_recommendation = "Pilot only"
        elif residual_risk_score < 4.2:
            deployment_recommendation = "Pause deployment"
        else:
            deployment_recommendation = "Reject / prohibit"

        rows.append(
            {
                "system_id": system_id,
                "system_name": system["system_name"],
                "system_type": system_type,
                "risk_tier": system["risk_tier"],
                "inherent_risk_score": inherent_risk_score,
                "control_maturity_score": control_maturity_score,
                "evidence_completion_score": evidence_completion_score,
                "residual_risk_score": residual_risk_score,
                "deployment_recommendation": deployment_recommendation,
            }
        )

    return pd.DataFrame(rows)


def build_oulad_audit_ready_schema() -> pd.DataFrame:
    """
    Create a schema file for the future OULAD processed dataset.

    The actual OULAD data should be downloaded separately and not committed
    to GitHub as raw third-party data.
    """

    rows = [
        {
            "field_name": "student_id",
            "description": "Anonymised student identifier.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "string/integer",
        },
        {
            "field_name": "gender",
            "description": "Gender field used for subgroup fairness testing.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
        {
            "field_name": "region",
            "description": "Student region. May be used for proxy-risk checks.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
        {
            "field_name": "highest_education",
            "description": "Prior education level. May be used for proxy-risk checks.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
        {
            "field_name": "imd_band",
            "description": "Socioeconomic deprivation band. May be used for fairness and proxy analysis.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
        {
            "field_name": "age_band",
            "description": "Student age band.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
        {
            "field_name": "disability",
            "description": "Disability indicator for future intersectional analysis.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
        {
            "field_name": "total_vle_clicks",
            "description": "Aggregated VLE engagement count.",
            "source": "OULAD studentVle.csv",
            "expected_type": "numeric",
        },
        {
            "field_name": "assessment_score_avg",
            "description": "Average assessment score across available assessments.",
            "source": "OULAD studentAssessment.csv",
            "expected_type": "numeric",
        },
        {
            "field_name": "final_result",
            "description": "Final course result used for learning analytics audit demonstration.",
            "source": "OULAD studentInfo.csv",
            "expected_type": "categorical",
        },
    ]

    return pd.DataFrame(rows)


def main() -> None:
    """Run all processing steps and save processed datasets."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    ai_detection_input = find_input_file("synthetic_ai_detection_demo.csv")
    ai_proficiency_input = find_input_file("synthetic_ai_proficiency_survey_demo.csv")

    ai_detection_audit_ready = process_ai_detection_data(ai_detection_input)
    ai_detection_fairness_summary = build_ai_detection_fairness_summary(
        ai_detection_audit_ready
    )

    gender_ai_gap_monitoring = process_ai_proficiency_data(ai_proficiency_input)

    ai_system_inventory = build_ai_system_inventory_demo()
    governance_evidence_pack = build_governance_evidence_pack_demo()
    system_risk_assessment = build_system_risk_assessment_demo(
        ai_system_inventory,
        governance_evidence_pack,
    )
    oulad_schema = build_oulad_audit_ready_schema()

    ai_detection_audit_ready.to_csv(
        PROCESSED_DIR / "ai_detection_audit_ready.csv",
        index=False,
    )
    ai_detection_fairness_summary.to_csv(
        PROCESSED_DIR / "ai_detection_fairness_summary.csv",
        index=False,
    )
    gender_ai_gap_monitoring.to_csv(
        PROCESSED_DIR / "gender_ai_gap_monitoring.csv",
        index=False,
    )
    ai_system_inventory.to_csv(
        PROCESSED_DIR / "ai_system_inventory_demo.csv",
        index=False,
    )
    governance_evidence_pack.to_csv(
        PROCESSED_DIR / "governance_evidence_pack_demo.csv",
        index=False,
    )
    system_risk_assessment.to_csv(
        PROCESSED_DIR / "system_risk_assessment_demo.csv",
        index=False,
    )
    oulad_schema.to_csv(
        PROCESSED_DIR / "oulad_audit_ready_schema.csv",
        index=False,
    )

    print("Processed datasets generated successfully.")
    print(f"Input 1: {ai_detection_input}")
    print(f"Input 2: {ai_proficiency_input}")
    print(f"Output folder: {PROCESSED_DIR.resolve()}")
    print("Generated files:")
    for file_path in sorted(PROCESSED_DIR.glob("*.csv")):
        print(f" - {file_path}")


if __name__ == "__main__":
    main()
