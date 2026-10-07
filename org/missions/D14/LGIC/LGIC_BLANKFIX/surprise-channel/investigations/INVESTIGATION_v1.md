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

## LGIC_BLANKFIX-W2-S1 -- Neither .tools/naming-gate.py nor .tools/naming-apply-gate.py has a --self-test

```json
{
  "id": "LGIC_BLANKFIX-W2-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T12:29:02Z",
  "one_line": "Neither .tools/naming-gate.py nor .tools/naming-apply-gate.py has a --self-test, so BF-t-2's step 3 ('each gate's own --self-test gains one arm') has nothing to extend; I added a --self-test to each (two arms: s3-access IAM_POLICY takes the fourth verdict and passes, pipeline-chain IAM_POLICY still refuses).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp: python .tools/naming-gate.py --help at base 2894923538 lists only --diff, --enforce, --post-from-index (add_argument at .tools/naming-gate.py:1901-1903)",
      "python .tools/naming-apply-gate.py: add_argument at .tools/naming-apply-gate.py:379-382 lists dir, --plan-json, --enforce only",
      "after the edit: python .tools/naming-gate.py --self-test -> NAMING-GATE-SELF-TEST: PASS; python .tools/naming-apply-gate.py --self-test -> NAMING-APPLY-GATE-SELF-TEST: PASS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-t-2 build step 3 and BF2-AC3: each naming gate has its own --self-test that gains one arm and still passes.",
  "world_is": "Neither gate carried a --self-test. BF2-AC3 'both naming gates still pass their self-tests with the new arm' is therefore met by a self-test this order created, not by an existing one: it proves the two judge() paths handle the fourth value and keep refusing a group-B name, and says nothing about any prior self-test coverage because there was none. Both gates edited inside the order's paths; no other behavior changed."
}
```

## LGIC_BLANKFIX-W2-S2 -- One worked case in GRADING_RULE.md contradicts the fourth verdict: pandas-pyarrow-layer|LAMBDA_LAYER is record

```json
{
  "id": "LGIC_BLANKFIX-W2-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T12:29:02Z",
  "one_line": "One worked case in GRADING_RULE.md contradicts the fourth verdict: pandas-pyarrow-layer|LAMBDA_LAYER is recorded OUT-OF-PATTERN with canonical {system}-pandas-pyarrow-layer, and grade() now returns NO-SYSTEM-ASKED with pandas-pyarrow-layer; the case is not in lib/tests/test_opal_naming.py, so I restated it there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md worked_cases: {name pandas-pyarrow-layer, type LAMBDA_LAYER, verdict OUT-OF-PATTERN, canonical_form {system}-pandas-pyarrow-layer, why 'R1.e ... so {system}'}",
      "python -m pytest lib/tests/test_opal_naming.py before restating it: 8 failed (the six at base + this case + test_iv3_controls[CloudWatchLogs-IAM_POLICY-...]); after: 6 failed, the same six",
      "lib/tests/test_opal_naming.py _FOURTH_VERDICT_CASES (one entry) and test_iv3_controls CloudWatchLogs row updated to NO-SYSTEM-ASKED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-t-2: where a worked case in lib/tests/test_opal_naming.py records OUT-OF-PATTERN for a group-A name, update that case to the fourth value.",
  "world_is": "The worked cases live in GRADING_RULE.md, outside this order's grant, not in the test file. I did not edit GRADING_RULE.md; test_opal_naming.py overrides the one case at load time and names why. GRADING_RULE.md still says R1.e yields {system} for a library layer and its V-2 wording is stale; its owner is LGIC_NAMING / the issuer."
}
```

## LGIC_BLANKFIX-W2-S3 -- infra/logic/render_naming_section.py renders only grade.ALIAS and grade.OUT-OF-PATTERN as verdict sentences (l

```json
{
  "id": "LGIC_BLANKFIX-W2-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T12:29:02Z",
  "one_line": "infra/logic/render_naming_section.py renders only grade.ALIAS and grade.OUT-OF-PATTERN as verdict sentences (line 324), so the new grade.NO-SYSTEM-ASKED sentence is not carried into the canon's generated section; the verdicts closed list (line 322) does follow the schema and will show four.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/render_naming_section.py:322-326: verdicts list read as a whole, then for field in ('ALIAS','OUT-OF-PATTERN') each sentence rendered; no other verdict key is read",
      "python infra/logic/render_naming_section.py --check at this worktree: CHECK: STALE -- 3 failure(s), section stamp NAMING_SCHEMA v1.10 vs render v1.15 (the section was already 4 versions behind v1.14 at the base, so staleness is not caused by this order)",
      "--content-diff after the edit: CONTENT-DIFF 30, includes /grade/not_graded and /grade/unplaceable as DROPPED; the renderer reads no /grade/NO-SYSTEM-ASKED key, so that sentence is not rendered"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-t-2: read each outside reader of a verdict; for any that would mishandle the fourth value, file one row naming file and line.",
  "world_is": "The renderer does not fail on the fourth value, but it will print a four-value verdict list with no sentence saying what the fourth means, until its field tuple at line 324 gains NO-SYSTEM-ASKED. Also read, no row owed: lib/opal_lgctfm.py:251-278 records the verdict verbatim and TENSION_VERDICTS (line 1157) leaves NO-SYSTEM-ASKED out, so such a name raises no TENSION row, consistent with 'no remedy owed' (the comment at 1151-1157 does not name it); .tools/safe-apply.sh:92-94 is a comment and delegates to the two gates; infra/logic/registry/exemptions.json lines 33 and 192 mention OUT-OF-PATTERN only inside prose reasons."
}
```

## LGIC_BLANKFIX-W3-S2 -- a legacy_addresses.json row matches by key path alone, and one of the root's keys matches a row whose bucket is not the key's bucket

```json
{
  "id": "LGIC_BLANKFIX-W3-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-07T12:34:00Z",
  "one_line": "The key silver/prices/canonical_prices.parquet written by bd-price-update (bucket opal-data-bd, 49 Financial) classes LEGACY on the legacy_addresses.json row cottonwood-silver-canonical-prices, whose bucket is opal-data-cot; a census item carries no bucket, so the BF-t-5 match (the face's rule: the key matches an entry) cannot tell the two stores apart.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_keyfill.py dir infra/aws/lambda/bd-pipeline --root bd-pipeline --map ROOT_MAP_PROPOSED.json: LEGACY S3Key 'silver/prices/canonical_prices.parquet' where=infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py:441 basis=legacy_addresses.json row cottonwood-silver-canonical-prices (bucket opal-data-cot)",
      "infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py:54 reads S3_BUCKET 'opal-data-bd' (census item, graded ALIAS of opal-data-49financial); :441 put_object(Bucket=S3_BUCKET, Key='silver/prices/canonical_prices.parquet')",
      "infra/logic/registry/legacy_addresses.json row cottonwood-silver-canonical-prices: bucket opal-data-cot, template silver/prices/canonical_prices.parquet"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-t-5 worker face: LEGACY is tested after PATTERN and before ADDRESS; the key matches an entry of legacy_addresses.json (reusing _on_list/_legacy_list).",
  "world_is": "The row is classed LEGACY with the key's own bytes as canonical and the cottonwood row (and its bucket) named in basis, as the face orders; the same key under the 49 Financial bucket would otherwise be the ADDRESS blackdiamond/49financial/silver/prices/canonical_prices.parquet. Not resolved in the classifier (an item has no bucket field and the face fixes the rule); whether bd-price-update's store is the cottonwood legacy store, a same-path store of 49 Financial, or a row that should be bucket-scoped is for the registry's owner."
}
```

## LGIC_BLANKFIX-W1-S3 -- the six keys the amendment calls raise-HOLEs are the six carded keys

```json
{
  "id": "LGIC_BLANKFIX-W1-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T12:53:00Z",
  "one_line": "TO BF-t-6 AMENDMENT 1 says six keys of the root's source folder are grade() raises and print as HOLE; all six are carded, so rule 1 prints them CARDED and no key of the root is a raise-HOLE.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only (HEAD of wk-LGIC_BLANKFIX-1): items=140 right=10 fix=101 not_asked=6 pattern=1 carded=6 hole=16; the 16 HOLE lines are 8 EVENT_RULE {cadence}, 6 IAM_POLICY {system} and 2 S3Key cot-path conflicts; none carries a grade() raise text",
      "stdlib walk of opal_naming_scope.root_items(root)[0] calling opal_naming.grade on each: 6 RaiseDefect, on S3Key '%s' (bd-49f-etf-ownership-daily-canonical/lambda_function.py:102), 'daily/49financial' (backfill_49f_daily_from_monolith_rps.py:65), 'config/etf_universe.json' (:66), 'platinum/reports/%s/etf_ownership.pdf' (etf-ownership-daily/lambda_function.py:72), 'blackdiamond/49f/session-trigger-mode.json' (bd-49f-session-trigger/lambda_function.py:78), 'config/ticker_lookup.json' (bd-price-update/lambda_function.py:155); the same six are the six CARDED lines"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-t-6 AMENDMENT 1: a name grade() raises on is a HOLE (rule 3); six such keys exist in this root's source folder.",
  "world_is": "The six raising keys are the six keys NOT_JUDGED_R13.json cards (plane repo), and rule 1 (CARDED) is tested before rule 3 (HOLE), so they print CARDED and zero raise-HOLE lines exist for this root. The rule-3 path is exercised by the unit test (a hand-made raise) and not by the real root. The built order follows the rule order as written; the two statements cannot both hold for this root."
}
```
