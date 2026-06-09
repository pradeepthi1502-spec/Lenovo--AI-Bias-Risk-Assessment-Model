# AI Governance Risk Toolkit for UK Higher Education

A responsible AI governance toolkit for auditing gender-linked fairness risks in university AI systems, including AI detection tools, student-facing chatbots, VLE engagement analytics, career-service AI tools, AI-assisted assessment pilots, and digital-divide monitoring.

This project was developed from the Future17 Lenovo × QS Global Challenge and focuses on one core question:

> Are universities deploying AI systems in ways that unintentionally disadvantage students because of unequal AI access, AI confidence, or AI proficiency?

The project does not train a model to predict student outcomes. Instead, it provides a governance analytics framework for assessing whether AI systems used by universities create fairness, proxy-bias, transparency, or deployment risks.

---

## Project Summary

UK universities are increasingly adopting AI tools across student support, assessment, academic integrity, learning analytics, and career services. However, governance is not always keeping pace with deployment.

The original project began as a gender-bias risk framework for university AI systems. It has since been rebuilt into a practical AI governance toolkit that combines:

* AI system inventory
* Current deployment risk monitoring
* Future deployment readiness assessment
* Gender AI proficiency gap monitoring
* Fairness metrics
* Proxy-bias detection
* Governance control scoring
* Evidence pack validation
* Deployment decision support

The toolkit is designed to help universities, public-sector partners, and technology vendors assess AI systems before they are scaled across student populations.

---

## Why This Problem Matters

The strongest AI risk in UK universities is not currently admissions automation. Admissions decisions remain largely human-led in the UK higher education context.

The more immediate risk is different.

AI systems are already appearing in areas such as:

* AI plagiarism and detection tools
* Student support chatbots
* VLE and learning engagement analytics
* Career-service tools
* AI-assisted marking and feedback pilots
* Assessment support workflows

These systems can influence student support, suspicion, academic misconduct processes, feedback quality, progression, employability, and access to opportunities.

At the same time, student AI use is uneven. Evidence from the UK higher education sector shows that male students, STEM and Health students, and more socioeconomically advantaged students are more likely to use generative AI tools. This creates a serious governance issue:

> If universities deploy AI systems into a student population with unequal AI fluency, those systems may unintentionally reward students who already know how to use AI and penalise those who do not.

This project turns that problem into an auditable analytics and governance workflow.

---

## Toolkit Modules

### Module 0: AI System Inventory

Identifies and records the AI systems currently used or being piloted by a university.

Example systems:

* AI detection tools
* Student-facing chatbots
* VLE engagement analytics
* Career-service AI tools
* AI-assisted marking tools
* Early-alert prediction systems
* Automated essay scoring tools
* Enrolment forecasting tools

The inventory captures:

* System name
* Owner
* Vendor
* Purpose
* Decision influence
* Student groups affected
* Human oversight model
* Risk tier
* Deployment status

---

### Module 1: Current Deployment Risk Monitor

Assesses AI systems that are already live or commonly used in universities.

Priority systems:

1. AI plagiarism and detection tools
2. Student-facing chatbots
3. VLE engagement analytics
4. Career-service AI tools

This module focuses on live operational risk, including:

* False positive risk
* False negative risk
* Student appeal routes
* Human review quality
* Differential impact by gender
* Proxy bias through behavioural or demographic variables
* Governance evidence gaps

---

### Module 2: Future Deployment Readiness Framework

Assesses systems that universities are likely to procure, pilot, or scale in the next 12 to 36 months.

Example systems:

* AI-assisted marking and feedback
* Early-alert or at-risk student prediction
* Enrolment forecasting
* Automated essay scoring
* Admissions-support tools

The aim is to assess readiness before these systems become deeply embedded in student-facing processes.

---

### Module 3: Gender AI Proficiency Gap Monitor

Tracks whether unequal AI confidence, access, and usage patterns may create unfair outcomes.

This is the project’s most novel component.

The module monitors whether AI-integrated education systems may advantage students who are already more AI-proficient.

Example indicators:

* AI tool usage by gender
* AI confidence by gender
* AI training completion by gender
* Assessment outcomes after AI integration
* Academic misconduct flags by gender
* Career-service AI usage by gender
* VLE engagement changes after AI chatbot deployment

The purpose is not to blame students for different AI usage patterns. The purpose is to help institutions identify whether AI-enabled education is widening existing digital inequality.

---

### Module 4: Governance Evidence Pack Validator

Checks whether the university or vendor has provided sufficient governance evidence before deployment or scaling.

Evidence checks include:

* AI system owner
* Purpose statement
* Data Protection Impact Assessment
* Equality Impact Assessment
* Vendor model card
* Fairness testing evidence
* False positive testing
* Human review process
* Student appeal route
* Monitoring schedule
* Incident log
* Audit history
* Responsible escalation process

The validator helps identify whether an AI system is technically useful but governance-weak.

---

## Case Studies

### Case Study 1: AI Detection Tool Bias Stress Test

AI detection tools are one of the most urgent live-risk areas in higher education because they may influence academic misconduct processes.

This case study uses a synthetic stress-test dataset to demonstrate how universities could audit AI detection tools for fairness.

Example fields:

* Gender
* Subject area
* Prior AI experience
* Actual AI use
* Detector score
* Detection flag
* Academic misconduct case opened
* Appeal outcome
* Human override decision

Metrics tested:

* False positive rate by gender
* False negative rate by gender
* Detection flag rate by gender
* Appeal success rate by gender
* Human override rate by gender
* Largest fairness gap
* Deployment risk classification

The goal is not to claim that gendered harm has already been proven. The goal is to provide the audit structure required to test whether such harm exists before students are affected at scale.

---

### Case Study 2: OULAD VLE Learning Analytics Fairness Audit

The Open University Learning Analytics Dataset is used to demonstrate the toolkit on a large real higher education dataset.

This case study focuses on VLE engagement analytics and early-alert style risk monitoring.

The audit examines whether behavioural data such as clicks, engagement timing, and submission patterns may create proxy risks or unequal model outcomes across demographic groups.

Example analysis:

* Representation analysis
* Engagement distribution analysis
* Proxy detection
* Outcome gap analysis
* Fairness metric calculation
* Risk scoring
* Deployment recommendation

This provides a real-data demonstration of how the toolkit can be used beyond synthetic examples.

---

## Toolkit Architecture

```text
University AI System
        ↓
AI System Inventory
        ↓
Dataset / Logs / Vendor Evidence
        ↓
Representation Analysis
        ↓
Proxy Bias Detection
        ↓
Fairness Metrics
        ↓
Governance Evidence Pack Validation
        ↓
Control Maturity Scoring
        ↓
Residual Risk Engine
        ↓
Deployment Decision
        ↓
Executive Report
```

---

## Repository Structure

```text
future17-ai-governance-risk-toolkit/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── CHANGELOG.md
│
├── docs/
│   ├── 01_problem_statement.md
│   ├── 02_research_evidence_base.md
│   ├── 03_methodology.md
│   ├── 04_system_risk_profiles.md
│   ├── 05_fairness_metrics.md
│   ├── 06_proxy_bias_detection.md
│   ├── 07_governance_controls.md
│   ├── 08_partner_demo_script.md
│   └── references.md
│
├── data/
│   ├── README.md
│   ├── raw/
│   │   ├── oulad/
│   │   └── synthetic/
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── 00_project_overview.ipynb
│   ├── 01_oulad_data_preparation.ipynb
│   ├── 02_vle_fairness_audit_oulad.ipynb
│   ├── 03_ai_detection_synthetic_stress_test.ipynb
│   ├── 04_gender_ai_proficiency_gap_monitor.ipynb
│   ├── 05_governance_risk_scoring_demo.ipynb
│   └── 06_end_to_end_partner_demo.ipynb
│
├── src/
│   └── ai_governance_toolkit/
│       ├── config/
│       ├── data_ingestion/
│       ├── analytics/
│       ├── governance/
│       ├── pipelines/
│       └── reporting/
│
├── dashboard/
│   ├── streamlit_app.py
│   ├── pages/
│   └── assets/
│
├── reports/
│   ├── sample_ai_detection_risk_report.pdf
│   ├── sample_oulad_vle_fairness_report.pdf
│   └── sample_executive_summary.md
│
├── tests/
│   ├── test_fairness_metrics.py
│   ├── test_proxy_detection.py
│   ├── test_risk_scoring_engine.py
│   ├── test_evidence_pack_validator.py
│   └── test_integrated_pipeline.py
│
└── scripts/
    ├── generate_synthetic_ai_detection_data.py
    ├── run_oulad_audit.py
    ├── run_ai_detection_audit.py
    └── run_full_partner_demo.py
```

---

## Methods Used

### Representation Analysis

Checks whether relevant student groups are sufficiently represented in the dataset or system logs.

Example checks:

* Gender distribution
* Subgroup sample size
* Missing demographic values
* Underrepresented categories
* Sample size stability warnings

---

### Fairness Metrics

Calculates whether AI system outcomes differ across student groups.

Metrics include:

* Selection rate
* False positive rate
* False negative rate
* Accuracy
* Flag rate
* Appeal success rate
* Human override rate
* Largest fairness gap

---

### Proxy Bias Detection

Detects whether non-protected variables may indirectly encode gender or other demographic characteristics.

Example proxy variables:

* School type
* Postcode
* Subject choice
* Attendance
* VLE engagement timing
* Writing style
* Submission behaviour
* AI confidence
* Prior AI experience

Methods include:

* Cramer's V for categorical associations
* Correlation ratio for categorical-continuous relationships
* Proxy risk ranking
* Proxy safety scoring

---

### Governance Control Assessment

Assesses whether the university has the controls required to safely deploy the AI system.

Controls include:

* System ownership
* Human review
* Appeals process
* DPIA
* Equality impact assessment
* Monitoring plan
* Vendor transparency
* Audit schedule
* Incident response

---

### Risk Scoring Engine

The toolkit calculates:

1. Inherent risk
2. Control maturity
3. Fairness risk
4. Proxy risk
5. Residual risk
6. Deployment recommendation

The risk engine is system-specific. Different AI systems have different risk profiles.

For example:

* AI detection tools place higher weight on false positive risk and appeal processes.
* Student chatbots place higher weight on escalation, safeguarding, and response reliability.
* VLE analytics place higher weight on behavioural proxy bias and intervention impact.
* AI-assisted marking places higher weight on assessment fairness and human moderation.

---

## Deployment Decision Logic

The toolkit produces one of five deployment recommendations:

| Recommendation          | Meaning                                                        |
| ----------------------- | -------------------------------------------------------------- |
| Approve                 | Risk is low and controls are strong                            |
| Approve with monitoring | Risk is manageable but requires ongoing review                 |
| Pilot only              | System should not be scaled until more evidence is collected   |
| Pause deployment        | Risk or governance gaps are too significant                    |
| Reject / prohibit       | System creates unacceptable risk or lacks essential safeguards |

---

## Example Outputs

The project generates:

* Fairness audit tables
* Proxy bias rankings
* Representation summaries
* Governance evidence checklists
* Control maturity scores
* Residual risk scores
* Deployment recommendations

---

## Limitations

This project is a governance analytics prototype, not a legal compliance product.

Current limitations include:

* AI detection tool analysis uses synthetic stress-test data because real academic misconduct datasets are sensitive and not publicly available.
* OULAD is useful for VLE and learning analytics fairness testing, but it does not contain AI detector outputs or chatbot conversations.
* Gender is used as the primary fairness dimension in the current version, but future versions should include intersectional analysis.
* The toolkit supports human decision-making. It should not be used to make automated decisions about individual students.
* The scoring framework should be calibrated with institutional stakeholders before live deployment.

---


## References

Key sources and frameworks used in this project include:

* HEPI Student Generative AI Survey 2025
* Jisc LearnWise chatbot pilot
* Jisc AI in Assessment Pilot
* Open University Learning Analytics Dataset
* NIST AI Risk Management Framework
* ICO AI and data protection guidance
* UK GDPR
* Equality Act 2010
* Public Sector Equality Duty
* OECD AI Principles
* EU AI Act
* Russell Group AI principles
