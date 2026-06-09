# Governance Controls and Evidence Pack

## Purpose

Technical metrics are not enough to approve an AI system.

An AI system may perform reasonably in testing but still be unsafe if governance is weak, accountability is unclear, appeal routes are missing, or the vendor cannot provide adequate evidence.

This document defines the governance controls and evidence pack requirements used by the toolkit.

## Core Governance Principle

> If there is no evidence pack, there should be no approval.

## Mandatory Evidence Pack

Every AI system should provide the following before approval or scaling.

| Evidence item | Purpose |
|---|---|
| System description | Defines what the system is and what it does |
| Intended use statement | Prevents scope creep |
| Decision influence map | Shows how the AI output affects students |
| Named system owner | Creates accountability |
| Data dictionary | Documents variables and data sources |
| Demographic coverage summary | Shows whether key groups are represented |
| Fairness testing results | Shows subgroup performance and outcome gaps |
| False positive testing | Critical for AI detection and flagging systems |
| Human oversight procedure | Explains review and override controls |
| Student appeal route | Protects student rights |
| DPIA | Data protection risk assessment |
| Equality impact assessment | Equality and fairness risk assessment |
| Vendor model card | Documents model purpose, limitations, and testing |
| Monitoring plan | Defines post-deployment review |
| Incident log | Tracks issues after deployment |
| Rollback or suspension plan | Allows safe withdrawal if harm appears |

## Governance Control Categories

### 1. Accountability Controls

Checks:

- Is there a named owner?
- Is the system listed in an AI inventory?
- Is responsibility shared across academic, legal, IT, data, and equality teams?
- Is there a named escalation route?

Minimum evidence:

- AI system registry entry
- Named accountable owner
- Governance approval record

### 2. Transparency Controls

Checks:

- Are students told when AI materially shapes an outcome?
- Is there a plain-language explanation?
- Is the vendor transparent about system limits?
- Are staff trained to explain the system?

Minimum evidence:

- Student notice text
- Staff guidance
- Vendor documentation
- Plain-language explanation

### 3. Human Oversight Controls

Checks:

- Is there meaningful human review?
- Can humans override the system?
- Are staff trained not to rubber-stamp outputs?
- Are contested cases escalated?

Minimum evidence:

- Human review procedure
- Override logging
- Staff training records
- Escalation process

### 4. Student Rights Controls

Checks:

- Can students challenge a decision?
- Can students request human review?
- Can students correct inaccurate data?
- Is the appeal route accessible?

Minimum evidence:

- Appeal procedure
- Human review request process
- Data correction pathway
- Named contact point

### 5. Fairness and Monitoring Controls

Checks:

- Are fairness metrics reviewed before deployment?
- Are metrics monitored after deployment?
- Are subgroup results reviewed?
- Are incidents logged?

Minimum evidence:

- Fairness audit
- Subgroup performance report
- Monitoring schedule
- Incident log
- Remediation tracker

### 6. Vendor Controls

Checks:

- Does the vendor provide performance evidence?
- Does the vendor allow audit access?
- Are model changes disclosed?
- Are limitations documented?

Minimum evidence:

- Vendor model card
- Audit clause
- Change notification clause
- Termination or suspension rights

## Control Maturity Scoring

| Score | Meaning | Description |
|---:|---|---|
| 0 | Absent | No evidence or control exists |
| 1 | Ad hoc | Informal or inconsistent control |
| 2 | Partial | Some control exists but is incomplete |
| 3 | Adequate | Control is documented and usable |
| 4 | Strong | Control is mature and regularly reviewed |
| 5 | Exemplary | Control is robust, monitored, and externally defensible |

## Deployment Decision Rules

| Condition | Recommendation |
|---|---|
| Low residual risk and strong evidence | Approve |
| Manageable risk with monitoring needs | Approve with monitoring |
| Insufficient evidence but limited harm | Pilot only |
| Material governance gaps | Pause deployment |
| No human oversight, no appeal, or serious unresolved disparity | Reject / prohibit |

## High-Risk System Red Lines

The toolkit should not recommend approval where:

- There is no meaningful human oversight
- Students cannot appeal or challenge
- The vendor refuses basic documentation
- Fairness testing is absent for a high-stakes system
- Serious subgroup disparity remains unresolved
- The system is used as the sole basis for a significant student decision
- The system cannot be monitored after deployment

## Governance Outputs

The governance module should output:

- Evidence pack completeness score
- Missing evidence list
- Control maturity score
- Critical gaps
- Required mitigations
- Approval recommendation
- Review date

