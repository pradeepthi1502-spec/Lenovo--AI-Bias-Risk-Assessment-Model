# Proxy Bias Detection

## Purpose

Proxy bias occurs when a variable does not explicitly contain gender but still indirectly encodes gender-linked patterns.

Example:

A model may not use gender directly, but it may use variables such as subject area, school type, postcode, VLE engagement timing, writing style, or career gaps. These variables may correlate with gender or with gendered social patterns.

Proxy bias matters because removing the gender column does not automatically make an AI system fair.

## Common Proxy Variables in University AI Systems

| Variable | Why it may create proxy bias |
|---|---|
| Subject area | Gendered patterns exist across STEM, Health, Arts, Business, and Humanities |
| School type | May encode socioeconomic and regional differences |
| Postcode | May encode income, ethnicity, school access, and regional opportunity |
| VLE login frequency | May disadvantage students with caring, work, or commuting responsibilities |
| Submission timing | May reflect work/care constraints rather than academic ability |
| Writing style | May encode linguistic, cultural, or gendered communication patterns |
| Attendance | May reflect caring duties, disability, work, or commuting constraints |
| Career gaps | May penalise maternity, caring, illness, or economic disruption |
| AI confidence | May reflect unequal prior exposure to AI tools |
| Prior AI experience | May create advantage for students who already had AI access |

## Proxy Detection Methods

### 1. Cramer's V

Used for categorical-to-categorical relationships.

Example:

- Gender vs subject area
- Gender vs school type
- Gender vs AI experience level

Interpretation:

| Association strength | Proxy concern |
|---|---|
| Very low | Low concern |
| Low | Monitor |
| Moderate | Investigate |
| High | Strong proxy concern |
| Very high | Serious proxy concern |

### 2. Correlation Ratio

Used for categorical-to-continuous relationships.

Example:

- Gender vs detector score
- Gender vs VLE clicks
- Gender vs mock interview score
- Gender vs AI confidence score

### 3. Distribution Comparison

Used to compare whether variables behave differently across groups.

Example:

- Detector scores by gender
- VLE logins by gender
- Submission timing by gender
- Feedback score by gender

### 4. Proxy Risk Ranking

Variables are ranked by strength of association with gender or other monitored attributes.

Example output:

| Variable | Association method | Association score | Proxy concern |
|---|---|---:|---|
| Subject area | Cramer's V | 0.31 | Moderate |
| Prior AI experience | Cramer's V | 0.28 | Moderate |
| VLE login timing | Correlation ratio | 0.18 | Monitor |
| Postcode band | Cramer's V | 0.12 | Low |

## Suggested Proxy Assurance Scoring

| Proxy association | Proxy assurance score |
|---|---:|
| Very low | 5 |
| Low | 4 |
| Moderate | 3 |
| High | 2 |
| Very high | 1 |

Important naming rule:

> If higher scores mean safer, use `proxy_assurance_score` or `proxy_safety_score`, not `proxy_risk_score`.

## Proxy Bias in AI Detection Tools

AI detection tools may create proxy risk through:

- Writing style
- English language background
- Subject area
- Prior AI experience
- Prompt-editing confidence
- Use of grammar tools
- Assessment type

Audit questions:

- Are detector scores higher for one gender after controlling for actual AI use?
- Are students with lower AI confidence more likely to be falsely flagged?
- Are certain subject areas disproportionately flagged?
- Are appeal outcomes equal across groups?

## Proxy Bias in VLE Analytics

VLE analytics may create proxy risk through:

- Login frequency
- Time of day
- Number of clicks
- Submission timing
- Forum participation
- Video viewing behaviour

Audit questions:

- Are students flagged as disengaged because of non-standard study patterns?
- Does low VLE activity actually predict poor outcomes equally across groups?
- Are interventions fairly distributed?
- Does the model punish students with caring or work responsibilities?

## Proxy Bias in Career Tools

Career tools may create proxy risk through:

- Subject area
- Society memberships
- Work history
- Career gaps
- Confidence scores
- Interview communication style
- CV wording

Audit questions:

- Are women recommended lower-paid or gender-stereotyped roles?
- Are career gaps treated as negative signals?
- Do mock interview tools penalise communication styles unequally?
- Are STEM roles recommended unequally after controlling for skills?

## Minimum Output

The proxy detection module should output:

- Tested variables
- Association method
- Association score
- Proxy concern level
- Recommended mitigation
- Whether the variable should be excluded, transformed, monitored, or justified

## Recommended Mitigations

| Proxy issue | Possible mitigation |
|---|---|
| Strong proxy with weak justification | Remove variable |
| Useful but sensitive proxy | Keep with monitoring and explanation |
| Behavioural proxy | Add contextual review |
| High subgroup disparity | Require human review |
| Vendor cannot explain feature influence | Pause deployment |
| Proxy affects high-stakes decision | Require equality review before approval |

