# System Risk Profiles

Different AI systems create different types of risk. This toolkit therefore uses system-specific risk profiles rather than one generic scoring model.

## Risk Domains

The project uses five practical risk domains in the technical toolkit.

| Domain | Description |
|---|---|
| Data assurance | Quality, representation, missingness, proxy risk, temporal relevance |
| Model fairness | Error rates, selection rates, outcome gaps, drift, explanation quality |
| Decision impact | How much the AI output shapes real student outcomes |
| Human oversight | Review, override, staff literacy, escalation, appeals |
| Governance readiness | DPIA, equality review, monitoring, vendor evidence, incident response |

## Deployment Categories

| Category | Meaning |
|---|---|
| Live / current | Systems already used or commonly available |
| Active pilot / scaling | Systems being piloted or prepared for wider use |
| Near-future readiness | Systems likely to be procured or scaled in the next 12–36 months |

## Live / Current Systems

### 1. AI Detection Tool

Examples:

- AI writing detectors
- Plagiarism-integrated AI detection
- Academic misconduct flagging systems

Primary risks:

- False positives
- False negatives
- Unequal flag rates
- Weak appeal processes
- Over-trust in detector outputs
- Poor transparency

Recommended weighting:

| Domain | Weight |
|---|---:|
| Model fairness | 30% |
| Decision impact | 25% |
| Human oversight | 20% |
| Governance readiness | 15% |
| Data assurance | 10% |

High-priority controls:

- False positive testing
- Mandatory human review
- Student appeal route
- Evidence threshold before misconduct action
- Detector score logging
- Staff training on limitations

---

### 2. Student-Facing Chatbot

Examples:

- Course information chatbot
- Student support chatbot
- IT support chatbot
- Admissions information chatbot

Primary risks:

- Incorrect advice
- Unequal usage
- Poor escalation
- Safeguarding failure
- Hallucinated policy guidance
- Weak transparency

Recommended weighting:

| Domain | Weight |
|---|---:|
| Governance readiness | 25% |
| Human oversight | 25% |
| Decision impact | 20% |
| Data assurance | 15% |
| Model fairness | 15% |

High-priority controls:

- Clear notice that AI is being used
- Escalation route to human staff
- Safeguarding trigger rules
- Source document version control
- Query logging
- Regular answer-quality audits

---

### 3. VLE Engagement Analytics

Examples:

- Moodle engagement analytics
- Canvas engagement dashboards
- Blackboard analytics
- Informal early-alert indicators

Primary risks:

- Behavioural proxy bias
- Caring-responsibility penalties
- Misleading engagement assumptions
- Over-flagging students with non-standard study patterns
- Unequal intervention quality

Recommended weighting:

| Domain | Weight |
|---|---:|
| Data assurance | 25% |
| Model fairness | 25% |
| Decision impact | 20% |
| Human oversight | 20% |
| Governance readiness | 10% |

High-priority controls:

- Proxy-bias testing
- Subgroup performance review
- Human contextual review
- Student data correction route
- Intervention outcome tracking

---

### 4. Career-Service AI

Examples:

- CV feedback tools
- Mock interview tools
- Career recommendation systems
- Job matching platforms

Primary risks:

- Reinforcing gendered career pathways
- Unequal confidence effects
- Biased feedback on communication style
- Salary or role recommendation disparities
- Penalising career gaps

Recommended weighting:

| Domain | Weight |
|---|---:|
| Model fairness | 25% |
| Data assurance | 25% |
| Decision impact | 20% |
| Governance readiness | 15% |
| Human oversight | 15% |

High-priority controls:

- Recommendation distribution review
- Gender pathway analysis
- Feedback quality testing
- Human careers adviser review
- Student explanation and challenge route

## Active Pilot / Scaling Systems

### 5. AI-Assisted Marking and Feedback

Primary risks:

- Unequal feedback quality
- Over-reliance by markers
- Writing-style bias
- Score drift
- Poor explanation quality

Recommended weighting:

| Domain | Weight |
|---|---:|
| Model fairness | 30% |
| Human oversight | 25% |
| Decision impact | 20% |
| Governance readiness | 15% |
| Data assurance | 10% |

High-priority controls:

- Marker moderation
- Feedback quality review
- Rubric alignment testing
- Appeal pathway
- Student notice

## Near-Future Systems

### 6. Early-Alert Prediction

Primary risks:

- Behavioural proxy bias
- Unfair intervention targeting
- Labelling students as risky
- Feedback loops
- Cumulative disadvantage

Recommended weighting:

| Domain | Weight |
|---|---:|
| Data assurance | 25% |
| Model fairness | 25% |
| Decision impact | 25% |
| Human oversight | 15% |
| Governance readiness | 10% |

### 7. Enrolment Forecasting

Primary risks:

- Biased demand forecasts
- Under-supporting certain student groups
- Resource allocation inequality
- Historic pattern reinforcement

Recommended weighting:

| Domain | Weight |
|---|---:|
| Data assurance | 30% |
| Governance readiness | 25% |
| Decision impact | 20% |
| Model fairness | 15% |
| Human oversight | 10% |

### 8. Automated Essay Scoring

Primary risks:

- Writing-style bias
- Language-pattern bias
- Threshold effects
- Weak explainability
- Over-automation of academic judgement

Recommended weighting:

| Domain | Weight |
|---|---:|
| Model fairness | 35% |
| Data assurance | 25% |
| Decision impact | 20% |
| Human oversight | 10% |
| Governance readiness | 10% |

### 9. Admissions-Support AI

Primary risks:

- Historical selection bias
- School-type and postcode proxies
- Subject-choice bias
- Unfair ranking
- Lack of transparency

Recommended weighting:

| Domain | Weight |
|---|---:|
| Data assurance | 30% |
| Model fairness | 25% |
| Decision impact | 20% |
| Governance readiness | 15% |
| Human oversight | 10% |

Important note:

> Admissions-support AI is included as a future-readiness system, not as the main live deployment case for the UK university context.

