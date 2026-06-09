# Sample OULAD VLE Fairness Audit Report  
## Learning Analytics Demonstration

## AI system assessed

| Field | Value |
|---|---|
| System type | VLE engagement analytics / early-alert style monitoring |
| Deployment category | Current or near-future deployment risk |
| Student impact area | Learning support and intervention |
| Risk tier | Moderate to high depending on use |
| Primary concern | Behavioural proxy bias and unequal flagging |
| Required control | Human review before intervention or escalation |

---

## Why VLE analytics needs fairness auditing

VLE analytics can appear neutral because it uses behavioural indicators such as clicks, logins, submission timing, and activity records.

However, engagement data may encode structural differences.

Example risks:

- Caring responsibilities may affect login timing.
- Employment responsibilities may affect engagement frequency.
- Subject area may shape expected VLE activity.
- Socioeconomic conditions may affect access and consistency.
- Platform behaviour may not reflect actual learning effort.

The audit question is:

> Are VLE-based indicators creating unequal support, suspicion, or intervention patterns across student groups?

---

## Dataset preparation summary

The prepared OULAD student feature table should include:

| Field | Purpose |
|---|---|
| Gender | Subgroup fairness analysis |
| Region | Potential proxy-risk variable |
| Highest education | Background and proxy-risk analysis |
| IMD band | Socioeconomic proxy-risk analysis |
| Disability | Future intersectional fairness analysis |
| Total VLE clicks | Engagement feature |
| Assessment score average | Outcome indicator |
| Final result | Course outcome |
| Low engagement flag | Demonstration flag for audit testing |

---

## Metrics to review

| Metric | Why it matters |
|---|---|
| Representation by gender | Checks subgroup sample size |
| Average VLE clicks by gender | Shows engagement distribution differences |
| Low engagement flag rate by gender | Tests unequal flagging risk |
| Unsuccessful outcome rate by gender | Identifies outcome gaps |
| Proxy association with gender | Identifies variables requiring governance review |

---

## Proxy-bias review

Potential proxy variables in OULAD include:

- Region
- IMD band
- Highest education
- Age band
- Studied credits
- Previous attempts
- Disability
- Subject module

A high proxy association score does not prove bias. It means the variable may indirectly encode a protected or sensitive characteristic and should be reviewed before use in decision-making.

---

## Example governance decision

| Recommendation | Rationale |
|---|---|
| Approve with monitoring | VLE analytics may support students, but indicators should remain advisory and must be monitored for unequal flagging or intervention patterns |

---

## Required mitigations

1. Do not treat VLE engagement as a direct measure of student ability.
2. Require human review before labelling a student as at-risk.
3. Monitor low-engagement flag rates across gender and other groups.
4. Review proxy variables before modelling.
5. Explain to students how engagement data is used.
6. Provide correction routes where data is inaccurate.
7. Reassess fairness after each academic cycle.

---

