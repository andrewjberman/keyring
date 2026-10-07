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

## LGIC_BLANKFIX-W1-S1 -- Source folders tied to two Terraform roots are contested: infra/aws/lambda/cot-pipeline (c

```json
{
  "id": "LGIC_BLANKFIX-W1-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T12:22Z",
  "one_line": "Source folders tied to two Terraform roots are contested: infra/aws/lambda/cot-pipeline (cot-pipeline and opal-assets) and infra/aws/lambda/investor-reporting (12 investor-reporting roots); 12 folders, assigned to no root.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_scope.py table (lib/opal_naming_scope.py, branch wk-LGIC_BLANKFIX-1) prints 12 CONTESTED lines; SCOPE-TABLE ok=True roots=61 items=1962 assigned=1843 unassigned=119",
      "evidence kinds read: infra/aws/lambda/ci/lambda-source-map.json tf_file, non-comment .tf paths under infra/aws/lambda/, and artifact_key = \"<prefix>/...\" literals in each root's .tf files"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-t-1: a source folder claimed by two roots is said so in source_dir_basis and filed as one row; it is assigned to neither root.",
  "world_is": "The artifact_key prefix investor-reporting/ is used by 12 sibling roots under infra/aws/terraform/investor-reporting/, and cot-pipeline/ by both the cot-pipeline and opal-assets roots, so the pipeline folder is claimed by each; a per-function source-map tie inside such a folder overlaps and is contested too. 43 investor-reporting items and 8 cot-pipeline items are therefore counted unassigned. None of the contested folders belongs to the round's picked root."
}
```

## LGIC_BLANKFIX-W1-S2 -- The TO says the bd-pipeline root's source folder is infra/aws/lambda/bd-pipeline/ alone; t

```json
{
  "id": "LGIC_BLANKFIX-W1-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T12:22Z",
  "one_line": "The TO says the bd-pipeline root's source folder is infra/aws/lambda/bd-pipeline/ alone; the repository ties a second folder, infra/aws/lambda/historical-prices-scheduler, so the scope holds 140 items, not 139.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json: function historical-prices-scheduler source_dir infra/aws/lambda/historical-prices-scheduler, tf_file infra/aws/terraform/bd-pipeline/lambdas.tf",
      "python lib/opal_naming_scope.py items infra/aws/terraform/bd-pipeline prints SCOPE-ITEMS ok=True root=infra/aws/terraform/bd-pipeline items=140 tf_items=96 source_items=44 source_dirs=2; the folder infra/aws/lambda/bd-pipeline alone holds 43 items"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-t-1 CONTEXT: the root's Lambda source folders are, at the cut, infra/aws/lambda/bd-pipeline/ (37 graded names, 16 with a {source}/{scope} blank, 6 carded).",
  "world_is": "The scope derived from the repository holds that folder (43 items: 6 carded, 1 pattern, 15 group D, 21 plain) plus infra/aws/lambda/historical-prices-scheduler (1 item, INSTANCE_PROFILE bd-exporter-profile, plain), which lambdas.tf deploys as module.historical_prices_scheduler. The TO's 16 blanks are the 15 group-D names plus the 1 pattern name. Three folders under infra/aws/lambda/bd-pipeline (bd-served-vintage-alarm, bd-49f-freshness-probe, bd-49f-etf-ownership-daily-canonical) carry no source-map or tf-path tie; they enter the scope only through the artifact_key prefix bd-pipeline/."
}
```
