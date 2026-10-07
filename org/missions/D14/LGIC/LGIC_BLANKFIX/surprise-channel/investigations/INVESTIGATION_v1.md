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

## LGIC_BLANKFIX-S2 -- a name that already says daily keeps that word though its schedule is weekdays only

```json
{
  "id": "LGIC_BLANKFIX-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-07T13:04:28Z",
  "one_line": "The thread run prints a complete fix ending in -daily for two rules whose schedules fire Monday to Friday only; the cadence reader calls the same expressions undecided.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt lines for bd-49f-fees-runner-daily and bd-49f-fees-session-daily (kind FIX)",
      "BF-t-4 worker report: undecided rows 2 and 4 of the root, same two names",
      "lib/opal_naming.py _cadence_slot: the word is read from the name's tokens"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 FWD-4 ACCEPT: a person who reads the schedule itself agrees with the word the list chose.",
  "world_is": "bd-49f-fees-runner-daily (cron(30 22 ? * MON-FRI *)) and bd-49f-fees-session-daily (cron(20 22 ? * MON-FRI *)) print FIX ...-daily because grade() takes the cadence word from the current name and never reads the expression. BF-t-4's reader returns no word for both ('MON-FRI days only: not every day'). The root check fills a cadence only where the name carries none, so a wrong word already in a name is not caught. Not fixed here: no cell of round 1 compares a carried word with the expression."
}
```

## LGIC_BLANKFIX-S3 -- a library layer with a registry row prints a fix with a system, against the ruling that such names are not asked for one

```json
{
  "id": "LGIC_BLANKFIX-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-07T13:04:28Z",
  "one_line": "openpyxl-layer prints FIX tradeops-openpyxl-layer in the thread run because resources.json carries a row for it; Andrew's CALL 3 puts library layers under the fourth verdict.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt line: FIX LAMBDA_LAYER openpyxl-layer -> tradeops-openpyxl-layer [infra/aws/terraform/bd-pipeline/layers.tf:8]",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/prd/C_VERDICT_FOURTH_VALUE_RECORD.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 FWD-3 and CALL 3 of 2026-09-21: a library-named Lambda layer is not asked to say which business system it belongs to.",
  "world_is": "The fourth verdict applies only when no registry row resolves a system (BF-t-2's face, from _slots R1.e). infra/logic/registry/resources.json holds a row placing openpyxl-layer under tradeops, so the name grades OUT-OF-PATTERN with a complete fix that adds a system. Whether a row outranks the ruling for layers, or the row should go, is the registry owner's and the CTO's; nothing was changed."
}
```

## LGIC_BLANKFIX-W5-S1 -- the unpatched section already carries the bare token NO-SYSTEM-ASKED; the check grades the schema sentence

```json
{
  "id": "LGIC_BLANKFIX-W5-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~5",
  "surfaced_at": "2026-10-07T13:50:53Z",
  "one_line": "The unpatched renderer's section already contains the token NO-SYSTEM-ASKED (verdicts closed list), so the difference control cannot be the bare token; the check grades the schema sentence bullet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_canon_patch.py prints: informational: the bare token NO-SYSTEM-ASKED in the UNPATCHED section (verdicts closed list): True",
      "infra/logic/render_naming_section.py:322-323 renders grade.verdicts as a whole; line 324 reads only ALIAS and OUT-OF-PATTERN sentences"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-e-5: the check asserts the UNPATCHED renderer's output does not contain NO-SYSTEM-ASKED and its schema sentence.",
  "world_is": "The token alone is present unpatched, through the verdicts closed list; only the sentence is absent. I read 'it' as the token plus its schema sentence (the bullet '- **NO-SYSTEM-ASKED:** <sentence>') and graded unpatched_has_verdict on that. Test not weakened: the sentence is the thing the cell names, and the patched arm shows it while the unpatched arm does not. Also measured: the committed 02_DOCTRINE.md already differs from an unpatched regeneration by 23 lines (stale stamps, row W2-S3)."
}
```

## LGIC_BLANKFIX-W3-S3 -- the root check does not read the new REFUSED-CROSS-FIRM class, so the two Cottonwood-path HOLE lines lose their reason

```json
{
  "id": "LGIC_BLANKFIX-W3-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-07T14:00:00Z",
  "one_line": "lib/opal_naming_rootcheck.py decide() reads the key basis only for class UNDECIDED, so the two cot-path HOLE lines, now class REFUSED-CROSS-FIRM, print the generic 'a blank remains that no module fills' and lose the cross-firm reason.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_rootcheck.py:90 `if key is not None and key.get(\"class\") == \"UNDECIDED\": why.append(...)`; lines 69-72 read LEGACY and ADDRESS only",
      "python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline (this worktree, after BF-e-3): ROOTCHECK ok=True items=140 right=9 fix=102 not_asked=6 pattern=1 carded=6 hole=16; HOLE S3Key code/bronze/cot_bronze_ingest.py -> partial form {source}/{scope}/code/bronze/cot_bronze_ingest.py; could not fill a blank remains that no module fills [bd-49f-fees-runner/lambda_function.py:43]",
      "python lib/tests/test_opal_naming_rootcheck.py after BF-e-3: ROOTCHECK-TEST ok=True cases=27; right fell 10 to 9 and fix rose 101 to 102 because silver/prices/canonical_prices.parquet at bd-price-update:441 is no longer LEGACY (its bucket opal-data-bd is not the legacy row's opal-data-cot)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-e-3: REFUSED-CROSS-FIRM is a new class value, the registry's cross-firm separation stated on a line; the Cottonwood file is printed and reported.",
  "world_is": "The new class reaches the root check, whose decide() has no branch for it: the line stays a HOLE (partial form with {source}/{scope}) as before, but its reason is the generic one, not the key row's basis (bucket or path token and both firms). The rootcheck module is outside this order's paths and was not edited; whether decide() should read REFUSED-CROSS-FIRM is the cell that owns that module."
}
```

## LGIC_BLANKFIX-W7-S1 -- The root map proposal carries no source_dirs: the landed map has one entry (bd-pipeline), which owns no contes

```json
{
  "id": "LGIC_BLANKFIX-W7-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~7",
  "surfaced_at": "2026-10-07T14:10:58Z",
  "one_line": "The root map proposal carries no source_dirs: the landed map has one entry (bd-pipeline), which owns no contested folder, and the repository decides the folder owners but not the scope of their entries.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/root_map.json roots keys: ['bd-pipeline'] at HEAD",
      "infra/aws/lambda/ci/lambda-source-map.json: irpt-directory-refresh/-search -> investor-reporting/directory, irpt-export-render -> export, irpt-holdings -> holdings, irpt-intake-poller -> intake, irpt-narrative -> narrative, irpt-status -> ops, irpt-performance-adapter -> performance, irpt-49f-reporting-publish-lambda -> reporting-publish, irpt-ycharts-generate -> ycharts/generate, each tf_file in the same-named root; cot-rebalancer-runner tf_file infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf; five cot-pipeline folders tf_file in infra/aws/terraform/cot-pipeline",
      "scope undecided: investor-reporting roots read per-firm buckets from firm_registry.json (directory/iam.tf:1-14, ycharts/generate.tf:236-249), performance spans orion, blackdiamond and cottonwood, holdings, intake, ops and reporting-publish name no firm; cot-pipeline names opal-data-cot, opal-data-bd, opal-data-inf, opal-data-etfs and resources.json places its cot-* names under five systems (advi, mdpf, posn, blackdiamond, etfs)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-e-7: the proposal is the landed map plus source_dirs on the entry of the root shown to own each contested folder, adding an entry only where the repository decides system, scope and source.",
  "world_is": "No entry could be added on the repository's word, so ROOT_MAP_SOURCE_DIRS_PROPOSED.json is the landed map byte for byte and the reader assigns nothing from it (SCOPE-TABLE unassigned=119 both ways). With a scratch map listing the eleven owners as source_dirs the reader assigns 40 of the 51 contested items (table unassigned 119 -> 79). Missing: scope for each of the 11 roots (and system for cot-pipeline and opal-assets, source for the investor-reporting roots other than ycharts), which is the registry owner's to decide. The parent folder infra/aws/lambda/investor-reporting (11 items: shared _authz, _keys, _scope and reports code) is declared by all 12 sibling roots and is left undecided on purpose."
}
```

## LGIC_BLANKFIX-W7-S2 -- infra/aws/lambda/cot-pipeline/bd-cot-freshness-probe holds 4 repository names and is declared by no root's .tf

```json
{
  "id": "LGIC_BLANKFIX-W7-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~7",
  "surfaced_at": "2026-10-07T14:10:58Z",
  "one_line": "infra/aws/lambda/cot-pipeline/bd-cot-freshness-probe holds 4 repository names and is declared by no root's .tf and no source-map function.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git grep bd-cot-freshness-probe -- infra/aws/terraform infra/aws/lambda/ci matches only infra/aws/terraform/cot-pipeline/CHANGELOG.json at HEAD",
      "python lib/opal_naming_scope.py contested: infra/aws/lambda/cot-pipeline items=4 (these four) before the sub-folder cot-rebalancer-runner items=4"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-e-7 cell: the owner of a folder is the root whose .tf declares the Lambda functions built from it.",
  "world_is": "For bd-cot-freshness-probe there is no such root: it is under the cot-pipeline folder only by the artifact_key prefix of the cot-pipeline root. If the map lists infra/aws/lambda/cot-pipeline for the cot-pipeline root, the reader assigns the four names to it by the parent listing; whether that is the right root for an undeclared function is the registry owner's call."
}
```

## LGIC_BLANKFIX-W7-S3 -- The order says the table reads 1,962 repository names; at HEAD of this branch it reads 1,965 with the same 119

```json
{
  "id": "LGIC_BLANKFIX-W7-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~7",
  "surfaced_at": "2026-10-07T14:10:58Z",
  "one_line": "The order says the table reads 1,962 repository names; at HEAD of this branch it reads 1,965 with the same 119 unassigned.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_scope.py table at the base of wk-blankfix-7 (before any edit): SCOPE-TABLE ok=True roots=61 items=1965 assigned=1846 unassigned=119",
      "row LGIC_BLANKFIX-W1-S1 recorded items=1962 assigned=1843 unassigned=119 on branch wk-LGIC_BLANKFIX-1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-e-7 THE CELL: python lib/opal_naming_scope.py table reads 1,962 repository names and leaves 119 unassigned.",
  "world_is": "The repository gained three assigned names since that run; the unassigned 119 and the 51 contested items are unchanged. No test of this order depends on 1,962: the tests read the total from the census."
}
```

## LGIC_BLANKFIX-W1-S4 -- the cell's DIFFERENCE CONTROL (daily-named rule on cron(30 22 ? * MON-FRI *) reads agrees=False) contradicts AMENDMENT 1 P1, under which that cron gives daily and agrees=True

```json
{
  "id": "LGIC_BLANKFIX-W1-S4",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T13:58:30Z",
  "one_line": "the cell's DIFFERENCE CONTROL (daily-named rule on cron(30 22 ? * MON-FRI *) reads agrees=False) contradicts AMENDMENT 1 P1, under which that cron gives daily and agrees=True",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/tests/test_opal_naming_cadence.py (branch wk-LGIC_BLANKFIX-1): CADENCE-TEST ok=True cases=45",
      "python lib/opal_naming_cadence.py contradicted infra/aws/terraform/bd-pipeline: CADENCE-CONTRADICTED ok=True root=infra/aws/terraform/bd-pipeline rows=20 contradicted=0",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/prd/E1_CADENCE_RULES_RATIFIED.md (Correction to this seat's round-1 analysis)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-e-1 cell text: a name carrying daily on cron(30 22 ? * MON-FRI *) reads agrees=False, the same name on cron(30 22 * * ? *) reads agrees=True.",
  "world_is": "AMENDMENT 1 P1 (NAMING_SCHEMA.json v1.16 cadence.daily_definition) gives daily to a once-a-day cron on five or more days of the week, so word_for(cron(30 22 ? * MON-FRI *)) is daily and verdict_for reads agrees=True for a daily-named rule; the amendment governs where it and the cell text differ. The test file keeps a difference control of the same shape on a schedule that does NOT give daily (a daily-named rule on rate(15 minutes) reads agrees=False; on cron(30 22 * * ? *) agrees=True) and asserts MON-FRI agrees=True. Real root: contradicted=0."
}
```

## LGIC_BLANKFIX-W1-S5 -- choices the cell left open: a ruled event rule's row word is its on-{event} tail, and word_for also reads */N, 0/N minute and hour steps

```json
{
  "id": "LGIC_BLANKFIX-W1-S5",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T13:58:30Z",
  "one_line": "choices the cell left open: a ruled event rule's row word is its on-{event} tail, and word_for also reads */N, 0/N minute and hour steps",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_cadence.py estate (branch wk-LGIC_BLANKFIX-1): CADENCE-ESTATE ok=True rows=142 decided=119 undecided=23",
      "lib/opal_naming_cadence.py cadences() and _cron()"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-e-1: a ruled event rule has the complete canonical name in lib/opal_naming_event_rules.json; word_for returns the ratified word for each period AMENDMENT 1 names by the same exact-period rule as today.",
  "world_is": "The cell does not say what the cadences() row word is for the ruled event rule, nor whether step crons are read. Built: the ruled row's word is the tail of the canonical from -on- ('on-session-complete'), which is what _cadence_slot reads from the renamed form, so it agrees once renamed; the root therefore prints decided=20 undecided=0. Cron minute steps */N and 0/N (N dividing 60) give {N}min, and an hour step 0/N or */N (N dividing 24, N 2 to 23, minute single, every day) gives {N}h; a step that does not divide the period (0/7) stays undecided. Whole estate: rows=142 decided=119 undecided=23 (12 unruled event rules, 2 non-literal expressions, 1 Nth-weekday, 7 several-hours-a-day, 1 rate(72 hours))."
}
```

## LGIC_BLANKFIX-W1-S6 -- the naming commit limb (ENFORCE) refuses lib/opal_naming_event_rules.json, the data file the cell mandates, as a NEW hand-kept carrier of 'bd' and '49f'

```json
{
  "id": "LGIC_BLANKFIX-W1-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T14:06:53Z",
  "one_line": "the naming commit limb (ENFORCE) refuses lib/opal_naming_event_rules.json, the data file the cell mandates, as a NEW hand-kept carrier of 'bd' and '49f'",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-commit.sh ... -- lib/opal_naming_event_rules.json (branch wk-LGIC_BLANKFIX-1, 2026-10-07): ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). naming-gate REFUSE lib/opal_naming_event_rules.json:5 bd-49f-session-complete -> lookup('49financial'); REFUSE :7 blackdiamond-49f-runner-on-session-complete -> lookup('49financial'); NAMING-GATE: REFUSE 2 graded",
      ".tools/naming-gate.py header, THE CONTEXT RULE: a firm token is permitted only in infra/logic/registry/*.json, generated blocks, key()/address()/name()/lookup() arguments, or opal_name module arguments; nothing admits lib/*.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-e-1: ruled event-rule rows are kept as DATA in a new file lib/opal_naming_event_rules.json, {name, type, canonical, evidence}, inside the order's write grant.",
  "world_is": "The ruled row holds two real names (bd-49f-session-complete and its ruled canonical). The commit limb is in ENFORCE and refuses both strings in a new file outside the registry, with no override a worker may use. The file is written and the library reads it; it is NOT committed. The branch tip commit carries the code, tests and rows, and lib/opal_naming_cadence.py fails loud (FileNotFoundError) on a checkout without that file. The issuer or the CTO decides the carrier: an R20 declared exception for the file, or the rows in a path the context rule admits (infra/logic/registry/, outside this grant). The order is NOT flipped to complete."
}
```

## LGIC_BLANKFIX-W2-S4 -- TO BF-e-8 rule 1 says an inline policy's {system} is filled from its role

```json
{
  "id": "LGIC_BLANKFIX-W2-S4",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T15:07:22Z",
  "one_line": "TO BF-e-8 rule 1 says an inline policy's {system} is filled from its role; the root map also holds ruled exceptions for inline-policy names (cross-firm-bucket-deny -> firmsep, describe-tags-self -> cloudops, monolith-bd49f-xref-silver-read -> schwab) whose role's system is advi, and the order does not say which wins.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_policyrole.py root infra/aws/terraform/bd-pipeline: cross-firm-bucket-deny (iam.tf:658), describe-tags-self (iam.tf:636) and monolith-bd49f-xref-silver-read (iam.tf:470) all sit on bd-exporter-ec2-role, role_system=advi",
      "infra/logic/registry/root_map.json roots.bd-pipeline.exceptions: those three names carry ruled systems firmsep, cloudops, schwab (Andrew-direct 2026-09-21 CALL 2 a5 families F02, F05, F14); the base run printed them as FIX firmsep-/cloudops-/schwab- names and the round-2 run prints them unchanged"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-e-8 rule 1: for an IAM_POLICY whose canonical carries {system} and whose declaration policy_roles knows, fill {system} from its role's system.",
  "world_is": "lib/opal_naming_rootcheck.py decide() applies the role's system only when the root map gives the name no ruled exception (basis root-default) or no entry; a ruled exception keeps winning, so the run's lines for those three names did not change and no ruling is overridden. If the order meant the role to win over an exception, those three lines would print advi- instead and contradict three ruled families; the issuer decides."
}
```

## LGIC_BLANKFIX-W2-S5 -- TO BF-e-8 rule 4 says a CARDED line prints 'the whole correct name where the card gives one', but no card row of NOT_JUDGED_R13.json carries a correct

```json
{
  "id": "LGIC_BLANKFIX-W2-S5",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T15:07:22Z",
  "one_line": "TO BF-e-8 rule 4 says a CARDED line prints 'the whole correct name where the card gives one', but no card row of NOT_JUDGED_R13.json carries a correct-name field, so no CARDED line of the run can print one.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json: 462 rows, the union of keys over every row is {name, plane, type, where, card, card_ref}; the six cards of bd-pipeline carry K1/K3/K4a reasons and no name",
      "python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only: six CARDED lines, each the card's first sentence"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-e-8 rule 4: a CARDED line prints the card's text up to its first sentence end, and the whole correct name where the card gives one.",
  "world_is": "decide() prints the first sentence and, if a card row ever gains a correct_name, canonical or canonical_name key, appends it as 'Correct name: ...' (tested with a hand-made card). On the real file no card gives one, so the clause is reachable in the test only."
}
```
