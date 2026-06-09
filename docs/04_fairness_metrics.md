# Fairness Metrics

This document defines the fairness metrics used by the toolkit.

## Purpose

Fairness metrics help assess whether an AI system produces different outcomes or error patterns across student groups.

The toolkit does not rely on overall accuracy alone because a system can look accurate overall while still performing poorly for a subgroup.

## Protected and Monitoring Groups

The current version focuses on gender-linked fairness risk.

Recommended group fields:

- Gender
- Subject area
- Level of study
- Age band
- Disability status
- Socioeconomic indicator
- International status
- Prior AI experience
- AI training completion

Future versions should expand into intersectional analysis.

## Core Metrics

### Selection Rate

The proportion of students receiving a positive, selected, recommended, flagged, or escalated outcome.

Formula:

```text
Selection Rate = Number of selected students / Total number of students in group
```

Example use cases:

- Career recommendation shown
- Early-alert intervention triggered
- Scholarship shortlist
- Positive assessment outcome

### Flag Rate

The proportion of students flagged by a system.

Formula:

```text
Flag Rate = Number of flagged students / Total number of students in group
```

Example use cases:

- AI detection flag
- At-risk flag
- Proctoring flag
- Academic integrity concern

### False Positive Rate

The proportion of students incorrectly flagged as positive or risky.

Formula:

```text
False Positive Rate = False Positives / (False Positives + True Negatives)
```

Example:

A student did not misuse AI, but an AI detector flags their work as AI-generated.

This is critical for AI detection tools because false accusations can cause serious harm.

### False Negative Rate

The proportion of actual positive or risky cases missed by the system.

Formula:

```text
False Negative Rate = False Negatives / (False Negatives + True Positives)
```

Example:

A student did misuse AI, but the detector fails to flag it.

### Accuracy

The proportion of correct predictions.

Formula:

```text
Accuracy = Correct Predictions / Total Predictions
```

Important warning:

> Accuracy is not enough. A system can have high accuracy overall but still produce unequal false positive rates by gender.

### Outcome Gap

The absolute difference in an outcome rate between two groups.

Formula:

```text
Outcome Gap = Absolute difference between group outcome rates
```

Example:

```text
Male flag rate = 12%
Female flag rate = 20%
Outcome gap = 8 percentage points
```

### Largest Fairness Gap

The largest absolute gap across all tested fairness metrics.

Example:

| Metric | Largest gap |
|---|---:|
| Flag rate | 8 percentage points |
| False positive rate | 14 percentage points |
| Appeal success rate | 5 percentage points |

Largest fairness gap = 14 percentage points.

## Suggested Fairness Gap Scoring

| Largest gap | Fairness assurance score |
|---|---:|
| Less than 5 percentage points | 5 |
| 5 to 10 percentage points | 4 |
| 10 to 15 percentage points | 3 |
| 15 to 20 percentage points | 2 |
| More than 20 percentage points | 1 |

Important naming rule:

> If a higher score means better performance, call it a fairness assurance score, not a fairness risk score.

## AI Detection Tool Metrics

AI detection tools should be audited using:

- Detector score distribution by gender
- Detection flag rate by gender
- False positive rate by gender
- False negative rate by gender
- Misconduct case conversion rate by gender
- Appeal success rate by gender
- Human override rate by gender

Minimum requirement:

> No AI detector should be used as the sole basis for academic misconduct action.

## VLE Analytics Metrics

VLE analytics systems should be audited using:

- Engagement distribution by gender
- At-risk flag rate by gender
- False positive rate by gender
- False negative rate by gender
- Intervention rate by gender
- Intervention outcome by gender
- Engagement proxy association with gender

## Career-Service AI Metrics

Career-service tools should be audited using:

- Tool usage by gender
- Recommendation type by gender
- Salary band recommendation by gender
- Role seniority recommendation by gender
- Feedback sentiment by gender
- Mock interview score by gender
- Human adviser escalation by gender

## AI-Assisted Marking Metrics

AI-assisted marking tools should be audited using:

- Score distribution by gender
- Feedback quality by gender
- Disagreement rate between human and AI scores
- Appeal rate by gender
- Successful appeal rate by gender
- Rubric alignment by gender
- Writing-style proxy analysis

## Small Sample Warning

If a subgroup has too few records, the toolkit should display a warning.

Example:

```text
Warning: The subgroup sample size is below the recommended threshold. Fairness results may be unstable and should not be used for final deployment decisions without further evidence.
```

## Recommended Output Table

| Group | Count | Selection/flag rate | FPR | FNR | Accuracy | Appeal success | Human override |


