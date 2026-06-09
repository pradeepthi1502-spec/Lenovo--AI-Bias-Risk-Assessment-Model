"""
Generate two synthetic datasets for the Future17 AI Governance Risk Toolkit.

Outputs:
1. synthetic_ai_detection_demo.csv
2. synthetic_ai_proficiency_survey_demo.csv

Important:
- This does not use real student data.
- This is scenario-based synthetic data for public GitHub demonstration.
- It is designed to test fairness auditing, AI detection risk, and gender AI proficiency gaps.
"""

import numpy as np
import pandas as pd


RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)


def generate_ai_detection_dataset(n=2000):
    """
    Generate synthetic AI detection tool audit data.

    Purpose:
    To simulate how a university could audit an AI plagiarism / AI-writing detector
    for false positives, false negatives, appeals, and human review outcomes by gender.
    """

    genders = ["Female", "Male", "Non-disclosed"]
    subject_areas = ["STEM", "Business", "Arts & Humanities", "Health", "Social Sciences"]
    socioeconomic_bands = ["Low", "Middle", "High"]
    ai_experience_levels = ["Low", "Medium", "High"]

    rows = []

    for i in range(1, n + 1):
        gender = np.random.choice(genders, p=[0.52, 0.43, 0.05])

        if gender == "Male":
            subject_area = np.random.choice(
                subject_areas,
                p=[0.36, 0.24, 0.13, 0.12, 0.15]
            )
        elif gender == "Female":
            subject_area = np.random.choice(
                subject_areas,
                p=[0.20, 0.22, 0.24, 0.22, 0.12]
            )
        else:
            subject_area = np.random.choice(
                subject_areas,
                p=[0.25, 0.20, 0.20, 0.15, 0.20]
            )

        socioeconomic_band = np.random.choice(
            socioeconomic_bands,
            p=[0.30, 0.50, 0.20]
        )

        experience_score = 0

        if gender == "Male":
            experience_score += 0.35
        elif gender == "Female":
            experience_score -= 0.10

        if subject_area == "STEM":
            experience_score += 0.45
        elif subject_area == "Business":
            experience_score += 0.25
        elif subject_area == "Arts & Humanities":
            experience_score -= 0.15

        if socioeconomic_band == "High":
            experience_score += 0.35
        elif socioeconomic_band == "Low":
            experience_score -= 0.30

        experience_score += np.random.normal(0, 0.45)

        if experience_score < -0.25:
            prior_ai_experience = "Low"
        elif experience_score < 0.65:
            prior_ai_experience = "Medium"
        else:
            prior_ai_experience = "High"

        ai_training_completed = np.random.choice(
            ["Yes", "No"],
            p=[
                {"Low": 0.28, "Medium": 0.45, "High": 0.62}[prior_ai_experience],
                1 - {"Low": 0.28, "Medium": 0.45, "High": 0.62}[prior_ai_experience],
            ],
        )

        confidence_base = {
            "Low": 2.1,
            "Medium": 3.2,
            "High": 4.1
        }[prior_ai_experience]

        if ai_training_completed == "Yes":
            confidence_base += 0.35

        ai_confidence_score = np.clip(
            np.random.normal(confidence_base, 0.65),
            1,
            5
        )

        actual_ai_use_probability = {
            "Low": 0.18,
            "Medium": 0.35,
            "High": 0.58
        }[prior_ai_experience]

        if subject_area in ["STEM", "Business"]:
            actual_ai_use_probability += 0.08

        if ai_training_completed == "Yes":
            actual_ai_use_probability += 0.05

        actual_ai_use_probability = min(actual_ai_use_probability, 0.85)

        actual_ai_use = np.random.choice(
            ["Yes", "No"],
            p=[actual_ai_use_probability, 1 - actual_ai_use_probability]
        )

        writing_formality_score = np.clip(
            np.random.normal(
                0.58
                + (0.06 if subject_area in ["Business", "Health"] else 0)
                - (0.04 if subject_area == "Arts & Humanities" else 0),
                0.16
            ),
            0,
            1
        )

        paraphrase_similarity_score = np.clip(
            np.random.normal(
                0.34
                + (0.22 if actual_ai_use == "Yes" else 0)
                + (0.05 if prior_ai_experience == "High" else 0),
                0.17
            ),
            0,
            1
        )

        source_citation_quality_score = np.clip(
            np.random.normal(
                0.62
                + (0.07 if ai_training_completed == "Yes" else -0.05)
                + (0.05 if prior_ai_experience == "High" else 0),
                0.18
            ),
            0,
            1
        )

        detector_score = (
            0.18
            + 0.35 * (actual_ai_use == "Yes")
            + 0.22 * paraphrase_similarity_score
            + 0.12 * writing_formality_score
            - 0.08 * source_citation_quality_score
            + np.random.normal(0, 0.12)
        )

        if prior_ai_experience == "Low" and actual_ai_use == "No":
            detector_score += 0.06

        if gender == "Female" and prior_ai_experience == "Low":
            detector_score += 0.035

        detector_score = np.clip(detector_score, 0, 1)

        detection_flag = "Yes" if detector_score >= 0.50 else "No"

        human_review_completed = "No"
        misconduct_case_opened = "No"
        appeal_submitted = "No"
        appeal_successful = "No"

        if detection_flag == "Yes":
            human_review_probability = 0.74 if detector_score < 0.72 else 0.88
            human_review_completed = np.random.choice(
                ["Yes", "No"],
                p=[human_review_probability, 1 - human_review_probability]
            )

            case_probability = 0.48
            if actual_ai_use == "Yes":
                case_probability += 0.22
            if human_review_completed == "Yes":
                case_probability -= 0.10

            case_probability = np.clip(case_probability, 0.05, 0.90)

            misconduct_case_opened = np.random.choice(
                ["Yes", "No"],
                p=[case_probability, 1 - case_probability]
            )

        if misconduct_case_opened == "Yes":
            appeal_probability = 0.40 if actual_ai_use == "No" else 0.18
            appeal_submitted = np.random.choice(
                ["Yes", "No"],
                p=[appeal_probability, 1 - appeal_probability]
            )

        if appeal_submitted == "Yes":
            appeal_success_probability = 0.58 if actual_ai_use == "No" else 0.16
            appeal_successful = np.random.choice(
                ["Yes", "No"],
                p=[appeal_success_probability, 1 - appeal_success_probability]
            )

        is_false_positive = "Yes" if detection_flag == "Yes" and actual_ai_use == "No" else "No"
        is_false_negative = "Yes" if detection_flag == "No" and actual_ai_use == "Yes" else "No"

        rows.append({
            "student_id": f"STUD{i:05d}",
            "gender": gender,
            "subject_area": subject_area,
            "socioeconomic_band": socioeconomic_band,
            "prior_ai_experience": prior_ai_experience,
            "ai_training_completed": ai_training_completed,
            "ai_confidence_score_1_5": round(ai_confidence_score, 2),
            "actual_ai_use": actual_ai_use,
            "writing_formality_score": round(writing_formality_score, 3),
            "paraphrase_similarity_score": round(paraphrase_similarity_score, 3),
            "source_citation_quality_score": round(source_citation_quality_score, 3),
            "detector_score": round(detector_score, 3),
            "detection_flag": detection_flag,
            "human_review_completed": human_review_completed,
            "misconduct_case_opened": misconduct_case_opened,
            "appeal_submitted": appeal_submitted,
            "appeal_successful": appeal_successful,
            "is_false_positive": is_false_positive,
            "is_false_negative": is_false_negative,
            "stress_test_note": "Synthetic demonstration only - not real student data"
        })

    return pd.DataFrame(rows)


def generate_ai_proficiency_survey_dataset(n=1000):
    """
    Generate synthetic AI proficiency survey data.

    Purpose:
    To simulate gender-linked differences in AI access, AI confidence,
    training completion, AI tool use, assessment outcomes, and misconduct flags.
    """

    genders = ["Female", "Male", "Non-disclosed"]
    subject_areas = ["STEM", "Business", "Arts & Humanities", "Health", "Social Sciences"]
    socioeconomic_bands = ["Low", "Middle", "High"]
    ai_access_levels = ["Low", "Medium", "High"]

    rows = []

    for i in range(1, n + 1):
        gender = np.random.choice(genders, p=[0.52, 0.43, 0.05])

        if gender == "Male":
            subject_area = np.random.choice(
                subject_areas,
                p=[0.36, 0.24, 0.13, 0.12, 0.15]
            )
        elif gender == "Female":
            subject_area = np.random.choice(
                subject_areas,
                p=[0.20, 0.22, 0.24, 0.22, 0.12]
            )
        else:
            subject_area = np.random.choice(
                subject_areas,
                p=[0.25, 0.20, 0.20, 0.15, 0.20]
            )

        socioeconomic_band = np.random.choice(
            socioeconomic_bands,
            p=[0.30, 0.50, 0.20]
        )

        access_score = 0.5

        if socioeconomic_band == "High":
            access_score += 0.25
        elif socioeconomic_band == "Low":
            access_score -= 0.20

        if subject_area == "STEM":
            access_score += 0.15
        elif subject_area == "Business":
            access_score += 0.08

        if gender == "Male":
            access_score += 0.06
        elif gender == "Female":
            access_score -= 0.03

        access_score += np.random.normal(0, 0.12)

        if access_score < 0.45:
            ai_access_level = "Low"
        elif access_score < 0.70:
            ai_access_level = "Medium"
        else:
            ai_access_level = "High"

        weekly_hours_base = {
            "Low": 0.8,
            "Medium": 2.2,
            "High": 4.3
        }[ai_access_level]

        if subject_area == "STEM":
            weekly_hours_base += 1.0
        elif subject_area == "Business":
            weekly_hours_base += 0.5

        if gender == "Male":
            weekly_hours_base += 0.45

        weekly_genai_use_hours = max(
            0,
            np.random.normal(weekly_hours_base, 1.25)
        )

        training_probability = {
            "Low": 0.25,
            "Medium": 0.42,
            "High": 0.60
        }[ai_access_level]

        if subject_area in ["STEM", "Business"]:
            training_probability += 0.08

        training_probability = min(training_probability, 0.85)

        ai_training_completed = np.random.choice(
            ["Yes", "No"],
            p=[training_probability, 1 - training_probability]
        )

        confidence_base = {
            "Low": 2.0,
            "Medium": 3.1,
            "High": 4.0
        }[ai_access_level]

        if ai_training_completed == "Yes":
            confidence_base += 0.35

        if gender == "Male":
            confidence_base += 0.15

        ai_confidence_score = np.clip(
            np.random.normal(confidence_base, 0.70),
            1,
            5
        )

        career_tool_probability = (
            0.25
            + 0.08 * (subject_area == "Business")
            + 0.08 * (ai_confidence_score >= 4)
            + 0.10 * (ai_training_completed == "Yes")
        )

        career_tool_probability = np.clip(career_tool_probability, 0.05, 0.85)

        career_ai_tool_used = np.random.choice(
            ["Yes", "No"],
            p=[career_tool_probability, 1 - career_tool_probability]
        )

        assessment_score_after_ai_integration = np.clip(
            np.random.normal(
                61
                + 2.1 * ai_confidence_score
                + 1.5 * (ai_training_completed == "Yes")
                + 1.2 * (weekly_genai_use_hours > 3)
                - 1.0 * (ai_access_level == "Low"),
                9.5
            ),
            0,
            100
        )

        misconduct_probability = (
            0.04
            + 0.018 * (weekly_genai_use_hours > 5)
            + 0.015 * ((ai_training_completed == "No") and (weekly_genai_use_hours > 2))
        )

        misconduct_probability = np.clip(misconduct_probability, 0.01, 0.30)

        academic_misconduct_flag = np.random.choice(
            ["Yes", "No"],
            p=[misconduct_probability, 1 - misconduct_probability]
        )

        rows.append({
            "student_id": f"SURV{i:05d}",
            "gender": gender,
            "subject_area": subject_area,
            "socioeconomic_band": socioeconomic_band,
            "ai_access_level": ai_access_level,
            "weekly_genai_use_hours": round(weekly_genai_use_hours, 2),
            "ai_confidence_score_1_5": round(ai_confidence_score, 2),
            "ai_training_completed": ai_training_completed,
            "career_ai_tool_used": career_ai_tool_used,
            "assessment_score_after_ai_integration": round(
                assessment_score_after_ai_integration,
                2
            ),
            "academic_misconduct_flag": academic_misconduct_flag,
            "demo_note": "Synthetic survey-style data for dashboard demonstration only"
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    ai_detection_df = generate_ai_detection_dataset(n=2000)
    ai_proficiency_df = generate_ai_proficiency_survey_dataset(n=1000)

    ai_detection_df.to_csv("synthetic_ai_detection_demo.csv", index=False)
    ai_proficiency_df.to_csv("synthetic_ai_proficiency_survey_demo.csv", index=False)

    print("Synthetic datasets generated successfully.")
    print("1. synthetic_ai_detection_demo.csv")
    print("2. synthetic_ai_proficiency_survey_demo.csv")