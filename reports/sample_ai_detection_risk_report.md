# Sample AI Detection Tool Risk Report  
## Synthetic Stress-Test Demonstration

This report is based on synthetic demonstration data.

It does not use real student records, real academic misconduct data, or University of Birmingham data.

The purpose is to demonstrate how a university could audit an AI detection or plagiarism tool before using it in high-stakes academic misconduct workflows.

---

## AI system assessed

| Field | Value |
|---|---|
| System type | AI detection / academic integrity tool |
| Deployment category | Current deployment risk |
| Student impact area | Academic misconduct |
| Risk tier | High |
| Primary concern | False positive and false negative risk |
| Required control | Human review and appeal route |

---

## Key audit questions

1. Does the tool flag students differently across gender groups?
2. Are false positive rates materially different by gender?
3. Are false negative rates materially different by gender?
4. Are flagged students receiving human review?
5. Are appeal outcomes monitored?
6. Is there enough evidence to justify continued use or scaling?

---

## Required fields in real deployment logs

A university partner would need to provide anonymised logs including:

| Field | Purpose |
|---|---|
| Student group attribute | Enables subgroup fairness audit |
| Detector score | Allows threshold and distribution testing |
| Detection flag | Shows who was flagged |
| Confirmed AI use or adjudicated outcome | Enables false positive / false negative testing |
| Human review status | Checks oversight quality |
| Misconduct case outcome | Shows operational impact |
| Appeal submission and appeal outcome | Tests student rights and correction mechanisms |

---

## Metrics calculated

| Metric | Why it matters |
|---|---|
| Detection flag rate | Shows how often students are flagged |
| False positive rate | Measures wrongful suspicion risk |
| False negative rate | Measures missed AI-use risk |
| Human review rate | Tests whether oversight is meaningful |
| Misconduct case rate | Shows escalation impact |
| Appeal success rate | Indicates whether errors are corrected |

---

## Interpretation framework

A high false positive rate is serious because AI detection tools can influence academic misconduct processes and student records.

A gender gap in false positive rate does not automatically prove discrimination. It indicates that the system requires deeper review before deployment or scaling.

The correct governance response is not automatic rejection. The correct response depends on:

- Size of the fairness gap
- Reliability of the ground truth label
- Availability of human review
- Strength of student appeal rights
- Whether the tool is advisory or determinative
- Whether the vendor can provide validation evidence

---

## Example deployment recommendation

| Recommendation | Rationale |
|---|---|
| Pilot only / pause deployment | Use should remain limited until false positive testing, human review, appeal evidence, and subgroup monitoring are complete |

---

## Required mitigations

1. Do not allow sole reliance on AI detector output.
2. Require human review before academic misconduct escalation.
3. Provide plain-language student notice.
4. Provide a clear appeal route.
5. Monitor false positives and false negatives by gender and other available protected characteristics.
6. Retest after major vendor updates or threshold changes.
7. Keep an incident log and report unresolved disparity to the governance committee.

---

