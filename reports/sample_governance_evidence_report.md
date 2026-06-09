# Sample Governance Evidence Pack Report

### Report status

This report demonstrates how the toolkit checks whether a university AI system has enough governance evidence before approval or scaling.

It is based on the project framework's evidence-pack logic and is intended for public GitHub demonstration.

---

## Required evidence items

| Evidence item | Why it matters |
|---|---|
| System description | Defines what the system is and what it does |
| Decision influence map | Shows where AI affects student outcomes |
| Data dictionary | Explains variables and data sources |
| Demographic coverage summary | Checks whether groups are represented |
| Fairness and performance test results | Shows whether the system was tested properly |
| Human oversight procedure | Prevents rubber-stamping and automation bias |
| Vendor model card | Improves transparency |
| DPIA summary | Supports data protection review |
| Equality impact assessment | Supports equality-risk review |
| Student notice and explanation text | Supports transparency |
| Appeal route | Protects student rights |
| Rollback or suspension plan | Allows safe withdrawal |
| Monitoring schedule | Supports ongoing review |
| Incident log | Captures harm, errors, and complaints |

---

## Evidence status scoring

| Status | Score |
|---|---|
| Provided | 1.0 |
| Partial | 0.5 |
| Missing | 0.0 |

The toolkit converts evidence completeness into a control maturity score.

---

## Governance interpretation

| Finding | Recommended response |
|---|---|
| Most evidence provided | Approve or approve with monitoring |
| Important evidence partial | Pilot only or conditional approval |
| Critical evidence missing | Pause deployment |
| No appeal route or human oversight | Pause or reject |
| No fairness testing for high-risk system | Pause deployment |

---

## Critical blocker examples

A system should not be approved if:

- It affects students materially but has no appeal route.
- It flags, ranks, or profiles students without human review.
- It lacks fairness testing for protected or monitored groups.
- It has no monitoring schedule.
- Vendor documentation is unavailable.
- Students are not told when AI materially affects them.

---
