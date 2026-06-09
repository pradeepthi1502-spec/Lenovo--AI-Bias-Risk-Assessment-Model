from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


# Ensure tests can import the package from the src/ layout without installation.
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = REPO_ROOT / "src"

if SRC_PATH.exists():
    sys.path.insert(0, str(SRC_PATH))


@pytest.fixture
def ai_detection_sample() -> pd.DataFrame:
    """Small synthetic AI detection fixture for unit tests."""
    return pd.DataFrame(
        [
            {
                "student_id": "S001",
                "gender": "Female",
                "subject_area": "Arts & Humanities",
                "actual_ai_use": False,
                "detection_flag": True,
                "human_review_completed": True,
                "misconduct_case_opened": True,
                "appeal_submitted": True,
                "appeal_successful": True,
                "detector_score": 0.72,
            },
            {
                "student_id": "S002",
                "gender": "Female",
                "subject_area": "Business",
                "actual_ai_use": False,
                "detection_flag": False,
                "human_review_completed": False,
                "misconduct_case_opened": False,
                "appeal_submitted": False,
                "appeal_successful": False,
                "detector_score": 0.28,
            },
            {
                "student_id": "S003",
                "gender": "Male",
                "subject_area": "STEM",
                "actual_ai_use": True,
                "detection_flag": True,
                "human_review_completed": True,
                "misconduct_case_opened": True,
                "appeal_submitted": False,
                "appeal_successful": False,
                "detector_score": 0.81,
            },
            {
                "student_id": "S004",
                "gender": "Male",
                "subject_area": "STEM",
                "actual_ai_use": True,
                "detection_flag": False,
                "human_review_completed": False,
                "misconduct_case_opened": False,
                "appeal_submitted": False,
                "appeal_successful": False,
                "detector_score": 0.41,
            },
        ]
    )


@pytest.fixture
def ai_proficiency_sample() -> pd.DataFrame:
    """Small synthetic AI proficiency fixture for monitoring tests."""
    return pd.DataFrame(
        [
            {
                "student_id": "P001",
                "gender": "Female",
                "subject_area": "Business",
                "weekly_genai_use_hours": 2.0,
                "ai_confidence_score_1_5": 3.0,
                "ai_training_completed": True,
                "career_ai_tool_used": False,
                "assessment_score_after_ai_integration": 68.0,
                "academic_misconduct_flag": False,
            },
            {
                "student_id": "P002",
                "gender": "Female",
                "subject_area": "Business",
                "weekly_genai_use_hours": 3.0,
                "ai_confidence_score_1_5": 4.0,
                "ai_training_completed": False,
                "career_ai_tool_used": True,
                "assessment_score_after_ai_integration": 72.0,
                "academic_misconduct_flag": False,
            },
            {
                "student_id": "P003",
                "gender": "Male",
                "subject_area": "STEM",
                "weekly_genai_use_hours": 5.0,
                "ai_confidence_score_1_5": 5.0,
                "ai_training_completed": True,
                "career_ai_tool_used": True,
                "assessment_score_after_ai_integration": 76.0,
                "academic_misconduct_flag": True,
            },
        ]
    )


@pytest.fixture
def inventory_sample() -> pd.DataFrame:
    """Small AI system inventory fixture."""
    return pd.DataFrame(
        [
            {
                "system_id": "AI-001",
                "system_name": "Academic Integrity AI Detector",
                "system_type": "ai_detection_tool",
                "risk_tier": "High",
            },
            {
                "system_id": "AI-002",
                "system_name": "Student Support Chatbot",
                "system_type": "student_chatbot",
                "risk_tier": "Moderate",
            },
        ]
    )


@pytest.fixture
def evidence_sample() -> pd.DataFrame:
    """Small governance evidence fixture."""
    return pd.DataFrame(
        [
            {"system_id": "AI-001", "evidence_item": "System description", "status": "Provided"},
            {"system_id": "AI-001", "evidence_item": "Decision influence map", "status": "Partial"},
            {"system_id": "AI-001", "evidence_item": "Appeal route", "status": "Missing"},
            {"system_id": "AI-002", "evidence_item": "System description", "status": "Provided"},
            {"system_id": "AI-002", "evidence_item": "Decision influence map", "status": "Provided"},
            {"system_id": "AI-002", "evidence_item": "Appeal route", "status": "Provided"},
        ]
    )
