# LGIC_BLANKFIX -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `2.0.0_SA_COO~G`. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW
row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row is `LGIC_BLANKFIX-S<k>`; a
worker's is `LGIC_BLANKFIX-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## LGIC_BLANKFIX-S1 -- the naming library's tests are red at the base: 6 of 93 fail

```json
{
  "id": "LGIC_BLANKFIX-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-07T12:30Z",
  "one_line": "The naming library's tests are red at the base: 6 of 93 fail before this project writes anything, so 'must stay green' (PRD C-CHECK) cannot be the bar a cell is graded on.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest lib/tests/test_opal_naming.py -q at HEAD ce2f42661d, laptop, 2026-10-07: 6 failed, 87 passed",
      "failing: test_grade_agrees_with_every_worked_case[inf-silver-chain|LAMBDA], [opal-portal-data-proxy-api|API_GW], [Inflection-SilverChain-DimConversionFailure|CW_ALARM], [wsb-49f-model-aua-pull-daily|SCHEDULE], [inf/otp-relay/token|SECRET]; test_lambda_plane_consumers_is_import_aware_not_a_bare_substring (assert 8 == 7)",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md base measurement 7"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 C-CHECK: a change to the grader lands in lib/opal_naming.py under LGIC_ENFORCE's existing tests, which must stay green.",
  "world_is": "Those tests are not green at the base. Five worked cases grade differently from their recorded answers (one prints 'portal/inf/otp-relay/token' where the case records '{system}/inf/otp-re...') and one consumer count reads 8 against a recorded 7. Cause not investigated; the registry was edited three times on 2026-10-07 after the cases were recorded. Round 1's cells are graded on 'no failure outside these six'. The owner of the six is LGIC_ENFORCE (held at stop)."
}
```

## LGIC_BLANKFIX-W3-S1 -- a root map exception keyed (name, type) cannot tell apart two resources of the same root that share both

```json
{
  "id": "LGIC_BLANKFIX-W3-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-07T12:18:00Z",
  "one_line": "bd-pipeline has two IAM_POLICY resources named s3-access on different roles (iam.tf:363 on the advi exporter role, iam.tf:855 on the blackdiamond allocation-processor role); the BF-t-3 exception key (name, type) and resources.json's (name, type) row key cannot give them different systems.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/bd-pipeline/iam.tf:362-364 (aws_iam_role_policy.bd_exporter_s3, name s3-access, role bd_exporter) and :854-856 (aws_iam_role_policy.bd_allocation_processor_s3, name s3-access, role bd_allocation_processor); pipeline-chain repeats the same way at iam.tf:256 and :614 (both advi by their roles)",
      "python lib/opal_naming_rootmap.py reference infra/aws/terraform/bd-pipeline --map ROOT_MAP_PROPOSED.json: rows=57 agree=57 disagree=0; the 12 {system}-blank names have no row and none was proposed as an exception"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-t-3 worker face: an exception is `{name, type, system, evidence}` and matches on (name, type); the proposal lists every name SY1 leaves undecided.",
  "world_is": "Two resources of one root can share (name, type) and differ in owning role, so one exception would set both. Not resolved in the reader (the face fixes the match key); the s3-access pair is left out of the proposal and listed in the report with the attached-role evidence (advi at :363, blackdiamond at :855)."
}
```
