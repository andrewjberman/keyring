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

## LGIC_BLANKFIX-S4 -- a refused key's line says another firm's store though its bucket is this firm's

```json
{
  "id": "LGIC_BLANKFIX-S4",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-07T15:24:34Z",
  "one_line": "The two REFUSED lines of the round-2 run say 'this key belongs to another firm's store' while the same line gives the key's bucket as the 49 Financial bucket; the refusal rests on a path token, and the sentence states more than was read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt: REFUSED S3Key code/bronze/cot_bronze_ingest.py ... conflict: path token 'cot' names firm 'cottonwood', the root entry's scope is '49financial'; the key's bucket: opal-data-bd (two lines, bd-49f-fees-runner/lambda_function.py:43 and bd-49f-runner/lambda_function.py:59)",
      "BF-e-3 worker report: the path-token conflict check, firm tokens and source tokens alike, routes to REFUSED-CROSS-FIRM; whether this is a real cross-firm reference is not decided"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ROUND_ANALYSIS.round1.md E3: a match is on (bucket, key), never the key alone; a key matched across two firms is refused. Round-2 decomposition: a REFUSED line states a finding about the code whole.",
  "world_is": "The key's bucket is 49 Financial's (opal-data-bd) and only its path names Cottonwood (a file called cot_bronze_ingest.py under code/bronze/). The line's opening sentence asserts another firm's store; what was measured is a Cottonwood-named code file kept in the 49 Financial bucket. A reader who did not build the check could take it as a cross-firm data reference. The run exits 0 with these two lines; whether FWD-1 reads them as actionable, and whether the wording should say 'names another firm' instead, is for BE8-AC3's grader and the CTO. Nothing was changed."
}
```

## LGIC_BLANKFIX-W2-S6 -- the order's counts (1,965 names, 119 unassigned, 51 contested) and three test assertions are stale; the repository reads 1,966 / 120 / 52

```json
{
  "id": "LGIC_BLANKFIX-W2-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T17:25:30Z",
  "one_line": "TO BF-r-3 states 1,965 names, 119 unassigned and 51 in contested folders; the repository at the worktree HEAD reads 1,966, 120 and 52, so three typed-total assertions of test_opal_naming_scope.py failed at the base and BR3-AC1 could not pass until they were rewritten as relations.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_scope.py table at 5b74b29963: SCOPE-TABLE roots=61 items=1966 assigned=1846 unassigned=120; contested: items=52",
      "python lib/tests/test_opal_naming_scope.py at 5b74b29963: three FAIL lines (contested --map last line, contested --map counts, no-map line) comparing against folders=12 items=51; with the landed map table reads unassigned=68 as AMENDMENT 1 says"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-r-3 CONTEXT: the table reads 1,965 repository names, 119 unassigned, 51 in 12 contested folders; the existing scope test passes at the base.",
  "world_is": "The repository holds one more census name in a contested folder (52), so every total is one higher. The three assertions that typed 51 were rewritten in lib/tests/test_opal_naming_scope.py to hold on relations (folders listed equal the contested rows, items equal the sum of the CONTESTED lines, assigned plus unassigned equals items, assigned with the map greater than without, assigned equal to the held folder's items)."
}
```

## LGIC_BLANKFIX-W1-S7 -- TO BF-r-2 expects the role rule to change what the three W2-S4 policies print; it changes nothing on the real root, because the grader already places 

```json
{
  "id": "LGIC_BLANKFIX-W1-S7",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T17:50:00Z",
  "one_line": "TO BF-r-2 expects the role rule to change what the three W2-S4 policies print; it changes nothing on the real root, because the grader already places those names",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py keys infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json: 36 policies; the six policies whose exception now names its role (bd-silver-merge-policy, bd-allocation-checker-permissions, monolith-bd49f-xref-silver-read, describe-tags-self, cross-firm-bucket-deny, historical-prices-policy) print the exception's system with system_slot_filled_here=no; the four policies whose {system} slot the run fills (pipeline-chain x2, runner-shared-read, gold-layer-trigger) fill it from the role",
      "python lib/opal_naming.py grade: describe-tags-self -> cloudops-describe-tags-self-policy, cross-firm-bucket-deny -> firmsep-cross-firm-bucket-deny-policy, monolith-bd49f-xref-silver-read -> schwab-monolith-bd49f-xref-silver-read-policy: the system is in the grader's own canonical form (resources.json rows), so the map exception is not read for it",
      "ROOTCHECK line of infra/aws/terraform/bd-pipeline before (HEAD d6291f1bac modules) and after this order: identical, diff empty; items=140 right=9 fix=111 not_asked=9 pattern=3 carded=0 refused=2 hole=6"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-r-2 cell: an exception keyed (name, type) with no role never overrides a role's answer; round 2 built the opposite for three policies (W2-S4), so the build should change what those lines print or fix them.",
  "world_is": "No line of the real root changes: the three W2-S4 policies print firmsep-/cloudops-/schwab- before and after, because grade() already returns a canonical form with the system filled, and decide() reads the root map's system only where the canonical keeps a {system} blank. The role rule is built and proved by the difference control in the three tests and by the keys command (exception_with_role=6, exception_without_role_overriding=0), but on this root it has nothing to override. The six exceptions' only live effect today is as the root map's record."
}
```

## LGIC_BLANKFIX-W1-S8 -- TO BF-r-2 AMENDMENT 1 item 3 limits what `fills` stops the entry from filling; it does not say whether the entry's home scope may still judge a key's 

```json
{
  "id": "LGIC_BLANKFIX-W1-S8",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T17:50:00Z",
  "one_line": "TO BF-r-2 AMENDMENT 1 item 3 limits what `fills` stops the entry from filling; it does not say whether the entry's home scope may still judge a key's firm",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_keyfill.py _classify: REFUSED-CROSS-FIRM compares the key's bucket firm with the entry's scope, and _conflict compares path tokens with the entry's scope and source",
      "infra/logic/registry/root_map.json _about.fills: 'a reader must then print the item's partial form and the reason ... rather than a finished name built from the home value'",
      "run of every root whose entry carries fills (opal-assets and the ten investor-reporting roots): the root check's lines are identical before and after the build, so no real line moves"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 item 3: with fills, a {scope} or {source} blank is not filled from the entry and the line prints HOLE with the reason; nothing is said about the refusal tests that read the entry's scope.",
  "world_is": "Judged inside the cell: when an entry's fills leaves out scope, the bucket-firm refusal does not compare against the home scope; when it leaves out scope or source, the path-token conflict is not run. The home value is not the key's firm, so a refusal built on it would state a finding about the code that was not measured (the defect of row LGIC_BLANKFIX-S4). Entries without fills behave as before. If the issuer wanted the refusals kept against the home scope, it is one condition in _classify."
}
```



## LGIC_BLANKFIX-W1-S9 -- TO BF-r-5 AMENDMENT 2: two of the four key rulings (etf_universe.json, daily/49financial) are not matched, because opal_naming_keyfill.bucket_of canno

```json
{
  "id": "LGIC_BLANKFIX-W1-S9",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T18:26:00Z",
  "one_line": "TO BF-r-5 AMENDMENT 2: two of the four key rulings (etf_universe.json, daily/49financial) are not matched, because opal_naming_keyfill.bucket_of cannot read their bucket; hole=2 remains",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only: ROOTCHECK ok=True items=140 right=9 fix=114 not_asked=10 pattern=3 carded=0 refused=2 hole=2; the two HOLE lines are S3Key daily/49financial [infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/backfill_49f_daily_from_monolith_rps.py:65] and S3Key config/etf_universe.json [same file:66]",
      "opal_naming_keyfill.bucket_of on both returns (None, 'the file has 2 bucket candidates and the key's statement picks none: opal-data-assets (line 61), opal-data-etfs (line 64)'): the key is a module-level constant (DAILY_PREFIX, UNIVERSE_KEY) whose own statement names no bucket; the bucket ETFS_BUCKET = 'opal-data-etfs' is a separate constant at line 64",
      "infra/logic/registry/key_rulings.json rows ('opal-data-etfs', 'daily/49financial') and ('opal-data-etfs', 'config/etf_universe.json') exist; per AMENDMENT 2 item 3 an item whose bucket cannot be read matches no row and keeps its card line, which is what prints (card line plus 'the bucket was not read (...)')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 2: the four stored-file HOLE lines are answered by key_rulings.json; the bucket is the one opal_naming_keyfill.bucket_of(item) reads.",
  "world_is": "Two of the four are answered (session-trigger-mode.json prints FIX to blackdiamond/49financial/state/session-trigger-mode.json; ticker_lookup.json prints NOT-ASKED). The two ETF keys stay HOLE because bucket_of picks no bucket for them. lib/opal_naming_keyfill.py is outside this order's grant. A reader that follows a key's constant to the bucket the code pairs it with (ETFS_BUCKET at the call sites) would match both; or the rows could name the file. BR5-AC1 fails as written on hole=2 and is reported, not forced."
}
```


## LGIC_BLANKFIX-W1-S10 -- TO BF-r-5 AMENDMENT 1 step 0 is built as a RETYPE only: 40 more literals under a function-name context carry no kind token and stay untyped, one of th

```json
{
  "id": "LGIC_BLANKFIX-W1-S10",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T18:26:00Z",
  "one_line": "TO BF-r-5 AMENDMENT 1 step 0 is built as a RETYPE only: 40 more literals under a function-name context carry no kind token and stay untyped, one of them in the bd-pipeline root",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "first build typed every kebab literal under a function-name context LAMBDA: census_repo() items went 1966 -> 2006, 40 items absent -> LAMBDA, among them infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py:54 opal-assets-bd49f-reporting-pull (a 141st item of the bd-pipeline root, against the order's 140 of 140)",
      "shipped build: the rule applies only where the last-token rule would have typed the literal; python lib/tests/test_opal_naming_function_literal.py -> FNLITERAL-TEST ok=True fees_runner=LAMBDA runner=LAMBDA retyped=2 other_changes=0 items=1966",
      "the other 39 are in inf-pipeline, investor-reporting, news and seeking-alpha Lambdas (e.g. inf-api-txn at inf-pipeline/inf-api-txn/lambda_function.py:161)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 step 0 item 1: a literal held under a function-name context is typed LAMBDA, before the last-token rule; item 2: nothing else changes. The test measures 'every item whose type changed', every one to LAMBDA.",
  "world_is": "Read literally, item 1 also adds items the last-token rule never typed, which grows the census and the bd-pipeline root by one line; the measurement spec compares items that exist on both sides. Judged inside the cell: the minimal reading, a retype of what is already typed. If the issuer wants the 40 typed as Lambdas, it is one line in _census_classify (hoist the function-context test above the kind lookup and drop the `if t` guard); the grader would then judge 40 more names."
}
```

## LGIC_BLANKFIX-W2-S7 -- the map entry is looked up by the root's last path word, not by the map's key

```json
{
  "id": "LGIC_BLANKFIX-W2-S7",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T17:56:52Z",
  "one_line": "check_root looks the map entry up by the root folder's last path word ('directory'), but the landed map keys a nested root by 'investor-reporting/directory'; so no entry is found for the second root and resolve() returns None for every name.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_rootcheck.py check_root: name = os.path.basename(opal_naming_scope._norm_root(root)); entry = doc['roots'].get(name); resolve(doc, name, ...) -- name is 'directory'",
      "python (at worktree HEAD): doc['roots'].get('directory') -> None; resolve(doc,'directory','irpt-x','IAM_ROLE') -> None; resolve(doc,'investor-reporting/directory','irpt-x','IAM_ROLE') -> {'system':'irpt','scope':'global','source':'irpt','basis':'root-default'}",
      "fills honoured: no line of org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/SECOND_ROOT_TRACE_round3.txt fills a firm from the map entry (no entry was read at all); the 2 FIX lines are schedule cadence suffixes, the system irpt is already in the current names"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-r-6 AMENDMENT 1: the map key form is 'investor-reporting/directory'; if it is not what check_root passes to resolve, that is a finding.",
  "world_is": "check_root passes the last path word, so a nested map key never matches. On a root whose names already lead with the system (this one) the run still reads RIGHT/FIX; on a root that needs {system} filled from the map it would print a HOLE 'no map entry for this root' though the map holds one. lib/ was not edited."
}
```

## LGIC_BLANKFIX-W2-S8 -- the run counts 15 names, the scope with the map counts 17; the two stored files are never run

```json
{
  "id": "LGIC_BLANKFIX-W2-S8",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T17:56:52Z",
  "one_line": "check_root counts 15 names for investor-reporting/directory; the scope's own root_items(root, map) counts 17: the run calls root_items(root) with no map, so the 2 stored-file keys of the root's Lambda source folder (investor-reporting/directory and investor-reporting/directory/_refresh) are never run; BR6-AC1 cannot pass as written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_second_root.py -> 'FAIL: items=15 but len(root_items(root, map)[0]) = 17' / 'SECOND-ROOT ok=False ... items=15 hole=0 differs=0' (rc 1)",
      "lib/opal_naming_rootcheck.py check_root: opal_naming_scope.root_items(root) (no map_path), twice (items and expected_n), so ROOTCHECK ok=True is self-consistent at 15; with the map, scope adds source folder infra/aws/lambda/investor-reporting/directory",
      "the two missing names: S3Key investor-reporting/directory [infra/aws/lambda/investor-reporting/directory/handler.py:53]; S3Key investor-reporting/directory/_refresh [infra/aws/lambda/investor-reporting/directory/refresh.py:71]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-r-6 BR6-AC1: `items` equals len(opal_naming_scope.root_items(root, map)[0]); AMENDMENT 1: 17 names, 4 schedules or event rules, 7 policies, 2 stored files, 1 source folder.",
  "world_is": "The run's last line reads ROOTCHECK ok=True items=15 (4 roles + 7 policies + 3 schedules + 1 event rule), but the stored files are not in it; the order's own comparison, against the map-aware scope, reads 17. The check was not weakened; BR6-AC1 is recorded FAIL and the order stays pending. The fix lies in lib/opal_naming_rootcheck.py (pass the map to root_items and key the entry by the map's own key form, one change with W2-S7), outside this worker's grant. A re-run after that fix would also grade the two stored-file lines, which this run has not."
}
```

## LGIC_BLANKFIX-W2-S9 -- the two stored-file names of investor-reporting/directory are HOLE and only the registry can close them

```json
{
  "id": "LGIC_BLANKFIX-W2-S9",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T19:14:37Z",
  "one_line": "The two stored-file names of investor-reporting/directory print HOLE: each is skipped by Card 1, the card names no correct name and says no none-owed, and no key_rulings.json row can match them because the bucket is chosen per firm at run time.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/SECOND_ROOT_TRACE_round3.txt: 'HOLE S3Key investor-reporting/directory ... [infra/aws/lambda/investor-reporting/directory/handler.py:53]' and 'HOLE S3Key investor-reporting/directory/_refresh ... [infra/aws/lambda/investor-reporting/directory/refresh.py:71]'; last line 'ROOTCHECK ok=True ... items=17 right=13 fix=2 ... hole=2'.",
      "lib/opal_naming_rootcheck.py load_card_rows(): both keys carry the Card 1 text ('segment 1 investor-reporting is neither a source nor a tier ... Zero registry mints follow'); key_rulings.json has 4 rows, none for these keys; opal_naming_keyfill.fill_keys(items, entry) returns 0 rows for the root's 2 stored files (measured).",
      "infra/aws/lambda/investor-reporting/directory/handler.py:50-53: DIRECTORY_BUCKET_ENV = 'IRPT_DIRECTORY_BUCKET_MAP' (the bucket is read from an environment map, one bucket per firm) and DIRECTORY_PREFIX default 'investor-reporting/directory'; refresh.py:71 REFRESH_PREFIX = 'investor-reporting/directory/_refresh'."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-r-6 AMENDMENT 2 step 6: holes are expected now that the two stored-file names are read; each is reported whole, grouped by what would close it.",
  "world_is": "Closing either HOLE is a registry decision (4.0.0_SA_CRO owns key_rulings.json and the card): a ruling that the key is a prefix under each firm's own bucket and either names the canonical form or says none is owed. A (bucket, key) row cannot be written once because the bucket is per firm and not in the repository; nothing the run or the map entry (fills: [system], no firm) can supply closes it. The run honoured fills: no line fills a firm or a source from the map entry."
}
```

## LGIC_BLANKFIX-W2-S10 -- the wider function-name rule adds two names to bd-pipeline, not one

```json
{
  "id": "LGIC_BLANKFIX-W2-S10",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T21:24:00Z",
  "one_line": "TO BF-q-4 says bd-pipeline will read 141 names where it read 140; with the wider rule it reads 142, because a second function-name literal in the same root (bd-price-update) is also typed LAMBDA.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only, last line: 'ROOTCHECK ok=True root=infra/aws/terraform/bd-pipeline items=142 right=9 fix=118 not_asked=12 pattern=3 carded=0 refused=0 hole=0' (base: items=140 fix=116).",
      "Census diff of that root, wide switch off vs on: two added lines, 'FIX LAMBDA opal-assets-bd49f-reporting-pull -> opal-assets-bd49f-reporting-pull-lambda [infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py:54]' and 'FIX LAMBDA bd-price-update -> advi-49f-price-update-lambda [infra/aws/lambda/bd-pipeline/bd-allocation-processor/lambda_function.py:117]'.",
      "infra/aws/lambda/bd-pipeline/bd-allocation-processor/lambda_function.py:117 is FunctionName='bd-price-update' in a client call: a function-name context the order's own rule covers; the order named only the line-54 literal."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-q-4 CELL: bd-pipeline will read 141 names where it read 140.",
  "world_is": "bd-pipeline reads 142 (fix 118): the rule adds every function-name literal with no kind token under the root, and the root holds two. No criterion depends on the count (BQ4-AC2 is the line checks, which pass); the rule was not narrowed to reach 141. Both added names grade without raising."
}
```

## LGIC_BLANKFIX-W1-S11 -- the face's REFUSED expectation for the two cot_bronze_ingest.py lines is overtaken by a key ruling

```json
{
  "id": "LGIC_BLANKFIX-W1-S11",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T22:05:30Z",
  "one_line": "TO BF-q-3 says the two bd-pipeline lines for code/bronze/cot_bronze_ingest.py must still print REFUSED after the build; the root check prints FIX for them because a registry key ruling for (opal-data-bd, that key) has landed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/key_rulings.json@cab8510cc3 line 45: a row with key 'code/bronze/cot_bronze_ingest.py'.",
      "python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json (run in the worktree after the build): 'FIX S3Key code/bronze/cot_bronze_ingest.py -> blackdiamond/49financial/code/bronze/bronze_ingest.py' at lambda_function.py:43 and :59; last line 'ROOTCHECK ok=True ... fix=116 ... refused=0 hole=0'.",
      "opal_naming_keyfill.fill_keys(items, root_map['bd-pipeline']) after the build (measured): both rows class REFUSED-CROSS-FIRM, basis \"conflict: path token 'cot' names firm 'cottonwood', the root entry's scope is '49financial'\" -- the same text as before the build; the module does not read key rulings."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-q-3 WORKER FACE last sentence: the two bd-pipeline lines for code/bronze/cot_bronze_ingest.py must still print REFUSED after the build.",
  "world_is": "The root check prints FIX for both lines: the root check answers a key the registry rules on first (lib/opal_naming_rootcheck.py module docstring, line 9), so fill_keys' REFUSED-CROSS-FIRM class is no longer what the line shows. What this build holds is the class: fill_keys still classes both REFUSED-CROSS-FIRM (the key's path word 'cot' names Cottonwood in 49 Financial's bucket opal-data-bd), and crossfirm prints them as REFUSED. The build did not change either."
}
```

## LGIC_BLANKFIX-W1-S12 -- the face's existing no-brace rule for key-ruling lines and the lines command did not exist

```json
{
  "id": "LGIC_BLANKFIX-W1-S12",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-07T22:50:50Z",
  "one_line": "TO BF-q-2 AMENDMENT 1 speaks of the lines command's existing no-brace rule; the lines command held none, so the brace rule was added in both the line decision and the lines command.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_rootcheck.py@807831814c lines_check (before the build): it checked rule codes, NOT-ASKED wording, FIX target collisions, REFUSED wording and the count line; no check of a brace in a FIX detail. decide() kept 'if \"{\" not in form' only for the {system}/{cadence} fill path, and the key-ruling branch returned the registry canonical with no brace test.",
      "After the build: decide() turns a FIX from a key ruling that carries any brace other than {scope}-on-a-per-firm-row into HOLE, and lines_check fails the run on a FIX line with such a brace (tests in lib/tests/test_opal_naming_rootcheck.py: 'the same {scope} on a row that is not per-firm is refused' and 'the lines command refuses {scope} on a FIX line whose row is not per-firm')."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-q-2 AMENDMENT 1: the check's own no-brace rule and the lines command must admit exactly {scope} on a line whose row is per-firm and refuse every other brace as today.",
  "world_is": "No brace rule existed on a key-ruling line or in the lines command before this build, so 'as today' described the {system}/{cadence} fill path only. The build adds the rule for key-ruling FIX lines and the lines command; the bd-pipeline count line is unchanged by it (ROOTCHECK ok=True items=142 right=9 fix=118 not_asked=12 pattern=3 carded=0 refused=0 hole=0 before and after)."
}
```

## LGIC_BLANKFIX-S5 -- the proof checker raises on a directory artifact path where it should refuse

```json
{
  "id": "LGIC_BLANKFIX-S5",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T00:20:05Z",
  "one_line": "The proof-of-spec checker crashes (rc 2, PermissionError) when a proof instance names a DIRECTORY as an artifact path; a worker worked round it by listing 13 files one by one.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "BF-q-6 worker report (0.9.0_WK_LGIC_BLANKFIX~2, commit 51fde5ac43): the checker crashed, rc=2, PermissionError, on a directory artifact path; the instance lists the 13 per-root files as separate rows",
      "NOT reproduced by the issuer: the crash is the worker's report; the instance as committed validates rc=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The spine, L7: proof-of-spec-check.py refuses an instance whose artifact rows do not resolve at their pins. A refusal is a verdict with a reason.",
  "world_is": "On a directory path the checker does not refuse: it raises and exits 2, which reads as a tool failure and not as a verdict. The file is .tools/proof-of-spec-check.py, outside this project's write surface; its owner is 1.0.0_SA_CTO. Nothing was changed. The worker did not file a row; the issuer files it at the drain."
}
```

## LGIC_BLANKFIX-W2-S11 -- six firm-unfilled stored-file holes of opal-assets fit none of the cell's four named hole classes

```json
{
  "id": "LGIC_BLANKFIX-W2-S11",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-08T01:59:31Z",
  "one_line": "BF-s-6 defines source_bucket as a bucket whose firm could not be filled; six opal-assets S3Key holes have the same cause (the root serves several firms, the map gives no firm) but are stored-file keys, so hole_class prints them as other.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json @ the BF-s-6 build: HOLE-CLASSES carded=22 source_bucket=3 event_rule=3 unknown_word=4 other=6; the six other lines are all opal-assets S3Key partial forms (schwab/{scope}/silver/account_xref, gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json, platinum/mdpf/aggregate_aua/, bronze/, bronze/eclipse/, code/bronze/templates/), printed whole by the command as OTHER-HOLE lines",
      "lib/opal_naming_rootcheck.py hole_class: source_bucket requires line type S3_BUCKET, the cell's wording 'a bucket on a root that serves more than one firm whose firm could not be filled'; the same detail text 'this root serves more than one firm; its map entry does not give the firm' sits on these S3Key lines"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-s-6 item 3: source_bucket = a bucket on a root that serves more than one firm whose firm could not be filled; other = none of the four named classes, printed whole.",
  "world_is": "The cell's wording reads literally as the S3_BUCKET line type, so the worker built it so; the stored-file keys with the same missing-firm cause are counted other_holes=6 and printed whole. Whether they belong in source_bucket is the CTO's reading of round 5 item S5 (the opal-assets sort); the one function hole_class changes in one place if so."
}
```

## LGIC_BLANKFIX-W4-S1 -- the reproduction had to live inside the worktree, not a temporary folder

```json
{
  "id": "LGIC_BLANKFIX-W4-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-08T02:05:03Z",
  "one_line": "BF-s-8 step 1 says build the reproduction in a temporary folder; the checker only grades an instance inside its own tree, so the reproduction was built under the worktree's .scratch/ and the crash (rc 2) reproduced there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Reproduction: .tools/proof-of-spec-check.py <instance under .scratch/> BQ6-AC1 with one PENDING-THIS-COMMIT row naming a directory printed PermissionError, TOOL-ERROR, rc=2; the same instance naming a file printed VALID (rc=0). An instance outside the tree is refused by the checker's artifact-resolution/CHECKER-SCOPE branch (.tools/proof-of-spec-check.py, near line 383) before any artifact is read."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-s-8 step 1: in a temporary folder build the smallest instance and governing order the checker accepts.",
  "world_is": "The checker refuses an instance whose path is outside its repository root (CHECKER-SCOPE), so the temporary folder had to sit inside the worktree (.scratch/, removed after). The governing order used was the existing BF-q-6 order in the tree, not a copy. The crash reproduced; the fix is in .tools/proof-of-spec-check.py (artifact-resolution loop, one early directory test)."
}
```

## LGIC_BLANKFIX-W1-S13 -- six holes of opal-assets fit none of the four classes S1 to S4

```json
{
  "id": "LGIC_BLANKFIX-W1-S13",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-08T01:57:30Z",
  "one_line": "TO BF-s-5: 6 of opal-assets' 20 holes (and of the 38) fit none of the CTO's classes S1 to S4: a stored-file key whose {scope} is open on a multi-firm root.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/HOLES_SORTED_round5.txt: last line HOLES-SORTED ok=True roots=13 holes=38 carded=22 source_bucket=3 event_rule=3 unknown_word=4 new=6; all 6 NEW lines are type S3Key on root opal-assets, each 'partial form ...{scope}...; could not fill {source}/{scope}: this root serves more than one firm; its map entry does not give the firm'.",
      "sort_holes.py (same folder): CLASSES tests S1, S3, S2, S4 in order; NEW_KINDS names the sixth kind; names: schwab/silver/account_xref, gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json, platinum/mdpf/aggregate_aua/, bronze/, bronze/eclipse/, code/bronze/templates/."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-s-5 CONTEXT: the CTO sorted the 17 lines it read into four classes, S1 carded, S2 source-owned bucket, S3 event rule, S4 unknown first word; the cell allows a fifth value NEW for a line no rule takes.",
  "world_is": "Over all 38 holes: S1 carded=22, S2 source_bucket=3 (all opal-data-ycharts), S3 event_rule=3, S4 unknown_word=4, NEW=6. The NEW class is an S3Key (a key, not a bucket) on the multi-firm root opal-assets whose map entry gives no firm; the buckets the check read are opal-data-bd, opal-data-cot, opal-data-assets, opal-data-portal-v2 or none (two keys name several buckets, none picked). S2 as the CTO worded it (a source-owned bucket) does not cover a key; a ruling on how a multi-firm root's keys get their firm is a fifth route. Nothing in lib/ or the registry was changed."
}
```

## LGIC_BLANKFIX-W3-S4 -- the Schwab key's path also carries a master account, which the firm test read as a firm of its own

```json
{
  "id": "LGIC_BLANKFIX-W3-S4",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T02:21:39Z",
  "one_line": "the Schwab key's path also carries a master account, which the firm test read as a firm of its own",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/scopes.json row key 08242234: class MASTER, firm 49financial, vendor schwab",
      "lib/opal_naming_keyfill.py _tok_firm and tests 'SOURCE: a path naming its own registry source in a firm's bucket is not refused' and 'SOURCE DIFFERENCE CONTROL: a path naming another FIRM (a master of Cottonwood) is refused' in lib/tests/test_opal_naming_keyfill.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-s-7 cell item 2 says the conflict is only the source test: a path whose first segment is a source the registry knows names ITS source.",
  "world_is": "Removing the source conflict alone moved the refusal of schwab/08242234/silver/fact_rps (bd-pipeline, bucket opal-data-assets) to the firm test: the path word 08242234 is a MASTER row of scopes.json and v.scope maps it to itself, so lib/opal_naming_keyfill.py _firm_check read it as a firm other than the root's 49financial. scopes.json gives that MASTER row firm=49financial. The build maps a master token to its row's firm (_tok_firm) before comparing, so a master of the bucket's own firm is no conflict and a master of another firm (z09, Cottonwood) is refused as that firm."
}
```

## LGIC_BLANKFIX-W3-S5 -- the registry holds no bucket-to-source table; the source test now reads the one source a product scope's bucket belongs to

```json
{
  "id": "LGIC_BLANKFIX-W3-S5",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T02:21:39Z",
  "one_line": "the registry holds no bucket-to-source table; the source test now reads the one source a product scope's bucket belongs to",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/scopes.json: PRODUCT rows mdpf, etfs, irpt, harvest carry bucket; the firm rows carry bucket_firm only",
      "python lib/opal_naming_keyfill.py crossfirm --map infra/logic/registry/root_map.json: last line KEYFILL-CROSSFIRM ok=True roots=13 keys=79 checked=47 ruled=11 unchecked=21 refused=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-s-7 cell item 2: refuse a key for a source only where the registry says the bucket belongs to one source and the path names another.",
  "world_is": "The registry says a bucket belongs to a FIRM (scopes.json bucket and bucket aliases, v.bucket_firm); it names no source for a bucket as such. The only statement of one-source ownership it carries is a PRODUCT scope row whose key is also a systems.json source (mdpf, etfs, irpt, harvest) with its bucket. The build reads that as the bucket's one source (_bucket_source); a firm bucket and a shared store (opal-data-assets) name none, so no source is refused there. Today no real stored key is refused for a source on that rule: the real sweep prints refused=0. If the CTO wants a different table (for example the source a firm bucket's pipeline tree writes), it is a registry row to add."
}
```

## LGIC_BLANKFIX-W3-S6 -- meta/templates/ was not an unread bucket: the reader read the wrong one (the copy's source bucket)

```json
{
  "id": "LGIC_BLANKFIX-W3-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T04:05:00Z",
  "one_line": "meta/templates/ was not an unread bucket: the reader read the wrong one (the copy's source bucket)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py:157-163 (PROVENANCE_RIDERS row: src_bucket opal-data-cot beside dst_prefix blackdiamond/cottonwood/meta/templates/) and :74, :255, :475 (MONOLITH = opal-data-assets, the bucket dst_prefix is listed in)",
      "python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json before the build: the HOLE for this key carried no 'bucket was not read' text, because bucket_of returned opal-data-cot"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 of TO BF-s-2 names meta/templates/ among the keys whose bucket bucket_of could not read, so no ruling row was matched.",
  "world_is": "bucket_of returned a bucket for it: opal-data-cot, pooled from the src_bucket entry of the same statement. The registry row (key_rulings.json, blackdiamond/cottonwood/meta/templates/) is under opal-data-assets, the monolith the dst_prefix is written to. The hole therefore was a wrong read, not an unread bucket, and its text did not say the bucket was not read. The build reads the field the key is the value of (dst_prefix): every statement of the file that reads row['dst_prefix'] and names a bucket names MONOLITH (opal-data-assets), so that bucket decides, and the row now matches."
}
```

## LGIC_BLANKFIX-W3-S7 -- the dict-row and keyword-call keys needed two more same-file rules than the two the amendment lists

```json
{
  "id": "LGIC_BLANKFIX-W3-S7",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T04:05:00Z",
  "one_line": "the dict-row and keyword-call keys needed two more same-file rules than the two the amendment lists",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_keyfill.py _bucket_via_field and _bucket_via_container (this build); tests 'FIELD', 'CONTAINER' and their DIFFERENCE CONTROL cases in lib/tests/test_opal_naming_keyfill.py",
      "infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py:127-143 (forwardfill_v2/ in the opal-data-cot row of MAP, three rows in one statement) and infra/aws/lambda/investor-reporting/performance/tenants.py:155-165 (forwardfill_v2/ as data_plane_prefix beside data_plane_bucket='opal-data-cot' in one call)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 item 1: extend the reader only by rules that read evidence in the same file, giving as the rules a bucket passed through a local variable or function parameter, and a per-firm choice made by calling a function.",
  "world_is": "Neither forwardfill_v2/ key is passed through a variable or a function: each sits in a statement that names several buckets (a three-row MAP; a three-route ROUTES dict), so bucket_of returned 'names several buckets, none picked'. Two further rules read the same file: (1) the bucket that shares the key's own call or dict literal (exactly one distinct bucket there decides; none or several read none), and (2) where the key is the value of a dict field F, the buckets named by the statements that read that field in the file (all the same bucket decides; different buckets read none). Rule 2 is tried first because rule 1 alone would give meta/templates/ the dict's src_bucket. Each rule has a DIFFERENCE CONTROL in the test. If the CTO wants only the amendment's two rules, the two functions are the whole extra."
}
```

## LGIC_BLANKFIX-W3-S8 -- quarantine/ and firms/ are not decided by their own files: two holes keep saying the bucket was not read, now with the reason

```json
{
  "id": "LGIC_BLANKFIX-W3-S8",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T04:05:00Z",
  "one_line": "quarantine/ and firms/ are not decided by their own files: two holes keep saying the bucket was not read, now with the reason",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/_keys/keys.py:114 (QUARANTINE_PREFIX = 'quarantine/'; no S3 call and no bucket literal in the file)",
      "infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py:35, :135, :154, :195-207 (the key is listed with Bucket=bucket, a parameter of discover_firms; its call site passes run's parameter bucket; run's call site passes args.bucket, from the argument --bucket whose default is os.environ.get(IRPT_EVIDENCE_BUCKET))"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 item 1 lists quarantine/ and firms/ among the keys to be read; item 3 asks for the count of HOLE lines that say the bucket was not read, before and after.",
  "world_is": "Neither file names a bucket: keys.py builds key strings and calls S3 nowhere; backfill_covered_account_ids.py takes its bucket from a command-line argument or an environment variable. The row's bucket (opal-data-ycharts) cannot be read from these files without guessing from the folder, which the amendment forbids. The reader returns no bucket and the reason now says what it found: 'key constant QUARANTINE_PREFIX (line 114) is used at lines 548,596,598, none names a bucket', and 'Bucket=bucket (line 135), a parameter of discover_firms ... line 154 passes bucket, a parameter of run; line 207 passes args.bucket, which names no bucket literal in this file'. Both HOLE lines remain and still say the bucket was not read. A way to close them is a registry choice (a row that names the environment variable IRPT_EVIDENCE_BUCKET as bucket_from, or a ruling by key for these two files), not a reader rule."
}
```

## LGIC_BLANKFIX-W2-S12 -- the registry's key-ruling rows carry no field that says what fills an open place, so the six opal-assets _quarantine/ lines stay HOLE

```json
{
  "id": "LGIC_BLANKFIX-W2-S12",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-08T03:52:00Z",
  "one_line": "the registry's key-ruling rows carry no field that says what fills an open place, so the six opal-assets _quarantine/ lines stay HOLE",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/key_rulings.json _about.row_fields @331e3fe609: bucket, key, shape, canonical, none_owed, evidence, owner; no field for what fills a place",
      "python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json: six OTHER-HOLE opal-assets lines '_quarantine/ -> partial form {source}/{scope}/state/quarantine/; a brace remains that no per-firm answer admits' before and after the build"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-s-1 AMENDMENT 1 item 1: a key-ruling row's canonical may carry the grammar's place names when the ROW says, for each, what fills it; read _about for the field that carries that; if no field does, the row cannot be admitted: report it and leave the HOLE.",
  "world_is": "No _about field names what fills a place. The only statement is prose inside the _quarantine/ row's evidence field ('WHAT FILLS THE TWO PLACES: {source} and {scope} are the first two segments of the partition that was rejected'); evidence is declared as 'what was read and measured', and reading a convention out of its prose would be a guess at a schema. Per the amendment the row is not admitted: the six lines stay HOLE (class other), no reader was built for an unratified field, and the test asserts that a one-place and a two-place canonical are both HOLE and the same row with no open place is FIX. To admit it the registry's owner adds a ratified field (for example one entry per place with its source) to key_rulings.json _about and the row; the reader is then a few lines in decide()."
}
```

## LGIC_BLANKFIX-W2-S13 -- BS1-AC2 reads carded_class_holes=5 after the build: each remaining line is a bucket the key reader does not read or a bucket name, not a missing ruling

```json
{
  "id": "LGIC_BLANKFIX-W2-S13",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-08T03:52:00Z",
  "one_line": "BS1-AC2 reads carded_class_holes=5 after the build: each remaining line is a bucket the key reader does not read or a bucket name, not a missing ruling",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json: last line ALL-ROOTS ok=True ... hole=23 carded_class_holes=5 (was 8)",
      "lib/opal_naming_keyfill.bucket_of on the opal-assets templates line returns ('opal-data-cot', ...) the SOURCE bucket of the PROVENANCE_RIDERS dict, while the ruling row is under opal-data-assets (the destination)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-s-1 BS1-AC2: carded_class_holes=0 over every mapped root.",
  "world_is": "Five carded lines remain and AMENDMENT 1 item 3 names the reason: investor-reporting/core quarantine/ (keys.py:114, no bucket literal in the file); investor-reporting/performance forwardfill_v2/ (tenants.py:164, several buckets none picked); opal-assets forwardfill_v2/ (ingest-mirror lambda_function.py:142, several buckets none picked); opal-assets blackdiamond/cottonwood/meta/templates/ (lambda_function.py:163, the key reader picks the source bucket opal-data-cot where the row is under opal-data-assets); investor-reporting/narrative S3_BUCKET opal-data-news-v2 (evidence.py:58, a bucket name; answered by name_rulings.json, BF-s-4). Rows exist for the first four keys and are not matched only because the bucket is not read as the row's. Not forced; keyfill not edited. The order stays pending."
}
```

## LGIC_BLANKFIX-W2-S14 -- a per-firm row's variable is a function the file calls, not a string constant, so the keyfill reader never matched it; the row match now also reads the file's code

```json
{
  "id": "LGIC_BLANKFIX-W2-S14",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-08T03:52:00Z",
  "one_line": "a per-firm row's variable is a function the file calls, not a string constant, so the keyfill reader never matched it; the row match now also reads the file's code",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/holdings/snapshot.py:663 directory_handler._bucket_for(registry_firm_id) and ops/status.py:405; key_rulings.json per-firm rows bucket_from _bucket_for",
      "lib/opal_naming_keyfill.runtime_bucket reads string constants only (names=(_bucket_for,) finds nothing in these files)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "key_rulings.json _about.per_firm: MATCH when the key equals the row's and the file that declares the item names bucket_from.",
  "world_is": "The file names _bucket_for as code (an attribute call), never as a string, so the three lines (holdings snapshot.py:64 and :665, ops status.py:407) printed HOLE 'bucket was not read'. lib/opal_naming_rootcheck.py now has named_in_source(item, asked): Python ast of the item's own file, a name, attribute, def or import counts; a comment, docstring or string does not. _ruling_of unions its answer with the runtime reader's. The three lines print FIX with {scope} kept. keyfill is read, not edited; if BF-s-2 extends runtime_bucket the two agree."
}
```

## LGIC_BLANKFIX-W2-S15 -- TO BF-s-1 is issued_to 0.9.0_WK_LGIC_BLANKFIX~1 but handed to the ~2 re-seat, so the lane gate refuses ~2's commit of the order's own paths

```json
{
  "id": "LGIC_BLANKFIX-W2-S15",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-08T03:58:35Z",
  "one_line": "TO BF-s-1 is issued_to 0.9.0_WK_LGIC_BLANKFIX~1 but handed to the ~2 re-seat, so the lane gate refuses ~2's commit of the order's own paths",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-commit.sh --author 0.9.0_WK_LGIC_BLANKFIX~2 ... -- lib/opal_naming_rootcheck.py lib/tests/test_opal_naming_rootcheck.py <proof>: rc=1, 'WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block' for three paths",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/LGIC_BLANKFIX.TO-BF-s-1.carded-class.md line 6: <issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>; the only non-terminal order issued to ~2 at HEAD is BF-s-9 (staged)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The instruction to this worker: commit on the branch through .tools/safe-commit.sh as 0.9.0_WK_LGIC_BLANKFIX~2.",
  "world_is": "The owned-paths gate grants a worker exactly the paths of non-terminal orders issued_to its serial (ADHC_OWNPTH.005). BF-s-1 names ~1, so the build (lib/opal_naming_rootcheck.py, its test) and the proof instance sit uncommitted in C:/tmp/wk-blankfix-2 on wk-LGIC_BLANKFIX-2. No override was used. Only this channel file, lane ANY, is committed. The issuer re-issues the order to ~2 (or commits the worktree diff) to land the build."
}
```

## LGIC_BLANKFIX-S6 -- a ruling matched on a file path broke when the file moved

```json
{
  "id": "LGIC_BLANKFIX-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T05:45:51Z",
  "one_line": "A key ruling matched on the path of the file that declares the key stopped matching when another project moved that file; the estate-wide run gained a hole from a file move.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/key_rulings.json @ac99c10b2e: the (opal-data-ycharts, firms/) row carries declared_in = [infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py]",
      "that path does not exist on the trunk; the file is at infra/aws/lambda/investor-reporting/export/tools/backfill_covered_account_ids.py since commit 8d66fb03da (0.9.0_WK_IRPT_BCKEND~168, IB-pr-360)",
      "the issuer's run after 8ae82065ba: ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0 -- the one hole is HOLE S3Key firms/ at the new path"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "key_rulings.json _about.row_fields (declared_in): a row matches when the item's key equals the row's key and the file declaring the item is one of declared_in; no bucket is read.",
  "world_is": "The match is exact on a repository path, and a path is not a stable identity: a move by any project silently un-matches the row and the name prints as a hole again. The registry's lane wrote the path while the file was at the old place in its tree; the move arrived on the laptop in the level-set of ~05:00Z. Asked of 4.0.0_SA_CRO: correct the path (msg sent). Not decided here: whether declared_in should match on something a move does not break (the file's name within the root's source folder, or the declaring function), or whether a check should refuse a declared_in path that does not exist."
}
```

## LGIC_BLANKFIX-S7 -- the key reader's own test is red on the trunk: it types the path of a file another project moved

```json
{
  "id": "LGIC_BLANKFIX-S7",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T06:24:39Z",
  "one_line": "lib/tests/test_opal_naming_keyfill.py prints ok=False on the trunk at the round's last merge: one REAL FILE case types a source path that IRPT_BCKEND moved.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/tests/test_opal_naming_keyfill.py on the trunk after merge 0d9d0abb47: FAIL line and KEYFILL-TEST ok=False cases=86",
      "lib/tests/test_opal_naming_keyfill.py:464",
      "git log: 8d66fb03da IB-pr-360 move backfill tool to export/tools/"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ROUND_ANALYSIS.round1.md ruling 3, restated for round 4: no test that passed at the base fails. Round-5 order context: a test asserts relations and the rows it needs by name, never a typed total.",
  "world_is": "The case at lib/tests/test_opal_naming_keyfill.py:464 names investor-reporting/export/backfill_covered_account_ids.py; the file is at export/tools/ since commit 8d66fb03da (0.9.0_WK_IRPT_BCKEND~168), which reached the laptop's shared tree in the ~05:00Z level-set, after BF-s-2 built the case and passed (86 of 86 in its tree). On the trunk now: 'FAIL: REAL FILE: firms/ ... unreadable: FileNotFoundError', KEYFILL-TEST ok=False cases=86. python -m pytest lib/tests passes (194): the plain script is not collected by it. Same cause as row S6, in a test instead of a registry row: a typed repository path is not a stable identity. Not fixed at the drain (a red at the drain is a row, not a silent re-cut): it is the first item for the next round, and the fix is to find the file by name under the root's source folder, not to retype the path."
}
```

## LGIC_BLANKFIX-S8 -- the saved all-roots run and a second seat's run differ by one unmapped root's name count

```json
{
  "id": "LGIC_BLANKFIX-S8",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T06:24:39Z",
  "one_line": "The exercise's check compares the whole live output with the saved file; on the trunk it reads repeat=DIFFERS because an UNMAPPED root gained a name between the two runs. The totals over the mapped roots are identical.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_ROOTS_round5.txt against org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round5_second_seat.txt: diff is one line (49)",
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py on the trunk: ALL-ROOTS-R5 ok=False ... repeat=DIFFERS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 FWD-9 ACCEPT: one person runs the check once and reads its totals; a different person runs it and gets the same.",
  "world_is": "The worker's saved run and the issuer's second-seat run print the same last line (ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0). One line differs between the two whole outputs: 'UNMAPPED infra/aws/terraform/nfra-ctlpln-identity names=10' against 'names=11' -- another project committed a name in a root the map does not cover. So 'the same totals' holds for everything the check reads, and the estate moved under the part it does not. The check script (a worker's deliverable) fails on the whole-output compare; the criterion BS9-AC1 passed in the worker's tree at its run. For the grader: whether FWD-9's repeat is the mapped totals, or the whole output on a pinned commit."
}
```

## LGIC_BLANKFIX-S9 -- item E5 was labelled FWD-5 and described FWD-6 (answered before the cut)

```json
{
  "id": "LGIC_BLANKFIX-S9",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T17:11:48Z",
  "one_line": "The round-5 analysis's item E5 was labelled FWD-5 but described a refusal at the moment a name is written, which is FWD-6's ACCEPT in the PRD; answered by 1.0.0_SA_CTO msg 106956 before the cut.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md @34ba4c1c90 -- item E5 'FWD-5: run it with nothing written first ... the check, run before any name is written, refuses a new stored name the canon would print as FIX'",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md:59-64 -- FWD-5: a person who has never run the check follows written instructions on a fresh copy and it finishes",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md:66-71 -- FWD-6: whoever creates a name the check cannot place hears about it when they create it",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md @cbdf36254c -- amended: E5 serves FWD-6; E6 added for FWD-5 as the PRD states it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 FWD-5: anyone can run the check from start to finish without writing anything for it first (no skip list). FWD-6: the creator of an unplaceable name hears at creation.",
  "world_is": "The analysis @34ba4c1c90 joined FWD-5's words to FWD-6's mechanism. Asked of 1.0.0_SA_CTO (msg 106951); answered msg 106956 and the analysis amended @cbdf36254c. Round 6 is cut on the amended text: BF-u-6 serves FWD-6, BF-u-7 serves FWD-5. Nothing open for the issuer."
}
```


## LGIC_BLANKFIX-W1-S14 -- the scope enumeration misses names declared through locals, modules or a .json file: 11 of the 24 names=0 roots declare names

```json
{
  "id": "LGIC_BLANKFIX-W1-S14",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-08T17:55:29Z",
  "one_line": "The scope enumeration misses names a root declares through locals, modules (opal_name, partner-firm-table, served-guard) or a .json file: 11 of the 24 'names=0' roots declare names, and 5 more roots print only part of theirs.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json at this worktree: 'UNMAPPED <root> names=0' for 24 roots; reading each root's .tf (and the one .json file etfs-rivalfunds reads) shows 11 of the 24 declare named resources the scope enumeration does not count. Per root, one declaring line:",
      "infra/aws/terraform/c3materialize-b4/main.tf:77 -- name = \"opal-c3materialize-b4-sbm\" (a local) names the ECR repository, IAM role, inline policy and CodeBuild project",
      "infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json:11 -- \"role_name\": \"etfs-rivalfunds-daily-role\" (names come from a .json file; lambdas.tf:14 'name = each.value.role_name')",
      "infra/aws/terraform/investor-reporting/holdings-performance/iam.tf:34-40 -- module \"irpt_holdings_performance_role_name\" { source = \"../../modules/opal_name\" system = \"irpt\" ... } assigned at iam.tf:51 'name = module.irpt_holdings_performance_role_name.name'",
      "infra/aws/terraform/investor-reporting/reporting-gold/iam.tf:24-30 -- module \"irpt_reporting_gold_role_name\" { source = \"../../modules/opal_name\" system = \"irpt\" ... }",
      "infra/aws/terraform/mdpf-secclass/new-security-classifier/main.tf:112-118 -- module \"name_lambda\" { source = \"../../modules/opal_name\" system = \"mdpf\" ... }; main.tf:157-164 assign local.function_name, local.role_name, local.schedule_name",
      "infra/aws/terraform/nfra-agentbus/iam.tf:21 -- name = local.role_a_name (and sqs.tf:10 name = local.q_a_to_b_name; kms.tf:41 name = \"alias/${local.prefix}\")",
      "infra/aws/terraform/nfra-agentbus-alyssa01/sqs.tf:8 -- name = local.q_a_to_b_name (iam.tf:12 name = local.role_a_name; iam.tf:58 name = local.user_b_name)",
      "infra/aws/terraform/nfra-ctlpln-agentbus/sqs.tf:30 -- name = module.queue_name[each.key].name (module opal_name, system = \"agentbus\", sqs.tf:20)",
      "infra/aws/terraform/partner-firms/demo.tf:31-34 -- module \"firm_demo\" { source = \"../modules/partner-firm-table\" firm_id = \"demo\" }; the table name is built at modules/partner-firm-table/main.tf:22 'name = \"opal-partner-${var.firm_id}\"' (four firms, four tables)",
      "infra/aws/terraform/served-guard-49f/_root.tf:36-40 -- module \"guard\" { source = \"../modules/served-guard\" firm = \"49f\" ... }; modules/served-guard/main.tf:181 'name = \"${local.name}-on-write\"' is an EVENT_RULE built from var.firm",
      "infra/aws/terraform/served-guard-cot/_root.tf:31-34 -- module \"guard\" { source = \"../modules/served-guard\" firm = \"cot\" ... } (same module, same rule)",
      "The same blind spot also hides stored names in roots the census DOES read, so they classify as no-stored-name: infra/aws/terraform/transcripts/main.tf:119-120 'resource \"aws_s3_bucket\" \"transcripts\" { bucket = local.bucket' and pull.tf:121 'name = local.pull_rule_name' (census: names=2, both LAMBDA); infra/aws/terraform/modules/served-guard/main.tf:181 (census: IAM_POLICY=4 only); infra/aws/terraform/served-guard-inf/_root.tf:32-35 (census: IAM_POLICY=1); infra/aws/terraform/mdpf-secclass/sector-writer/main.tf:83-90 (etfs bucket and run-list prefix built in locals).",
      "infra/logic/registry/root_map.json _about, paragraph 'A ROOT WITH NOTHING TO NAME': names=0 alone never justifies names: 'none' -- 'nfra-agentbus reads names=0 and declares IAM roles named from local.role_a_name'. The other 13 of the 24 are not this class: 7 attach to buckets or APIs declared elsewhere, 4 are modules whose names come from the caller, and 2 declare nothing at all (canonical-schwab-si2-schedule/main.tf, opal-assets-absence/main.tf: terraform, provider and locals blocks only)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-u-1 step 4: 'If any root reads DECLARES-NAMES, file ONE surprise row for the class (the scope enumeration misses names declared that way), listing the roots and one declaring line each.' The census line 'UNMAPPED <root> names=0' is read by the registry as a root with nothing to name (root_map.json _about).",
  "world_is": "11 of the 24 names=0 roots declare named resources (ECR, IAM, CodeBuild, Lambda, SQS, KMS alias, DynamoDB, EventBridge rules, schedules) that opal_naming_scope.root_items does not enumerate, because the name is built in a local, through a module the enumeration does not follow, or in a generated .json file. Five further roots (transcripts, modules/served-guard, served-guard-inf, mdpf-secclass/sector-writer, investor-reporting/reporting-read) print only the names written as literals; transcripts and the served-guard module declare a bucket and an EVENT_RULE that the census does not list. If any of these roots is mapped, the check still grades only the names the enumeration returns, so a wrong name in the missing set is never on the list (FWD-2). Entered as 'none' on the zero, the root would be mis-entered. The ruling file MAP_ENTRIES_FOR_RULING_round6.md gives each of the 11 a verdict DECLARES-NAMES and a drafted ordinary entry; the enumeration gap itself is lib/opal_naming_scope.py's and is not touched by this cell."
}
```

## LGIC_BLANKFIX-W1-S15 -- TO BF-u-6 says the commit-time naming gate is WARN today; the repository has it ENFORCING

```json
{
  "id": "LGIC_BLANKFIX-W1-S15",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-08T18:23:39Z",
  "one_line": "TO BF-u-6 (and CLAUDE.md rule 30) call the commit-time naming gate 'WARN today'; org/mcp/naming-gate.enforce exists, so the gate refuses.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/mcp/naming-gate.enforce -- present in this worktree (test -e, rc 0).",
      ".tools/naming-gate.py module docstring: 'ENFORCE is on with --enforce, env NAMING_GATE_ENFORCE=1, or a present org/mcp/naming-gate.enforce: a REFUSE then exits 1.'",
      "python .tools/naming-gate.py --diff <a diff adding schedule irpt-directory-newjob to infra/aws/terraform/investor-reporting/directory/schedule.tf> (run in the worktree): 'NAMING-GATE: REFUSE 1 graded', rc=1.",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/PRE_WRITE_REFUSAL_PATTERNS_20261008.md row 16 and pattern 4 already record the same drift (ENFORCE since 2026-09-17)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-u-6 THE CELL: 'the commit-time naming gate already in the tree (CLAUDE.md rule 30, WARN today)'.",
  "world_is": "The gate is in ENFORCE mode and refused the wrong-name arm of the design's measurement with rc=1. The design (FWD6_DESIGN_round6.md) is written against ENFORCE. No criterion is blocked."
}
```

## LGIC_BLANKFIX-W1-S16 -- TO BF-u-6 gives the PRD's FWD-6 as lines 66-71; the ACCEPT's last clause is at line 72

```json
{
  "id": "LGIC_BLANKFIX-W1-S16",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-08T18:23:39Z",
  "one_line": "The order names PRD lines 66-71 for FWD-6; the block is lines 67-73 (line 66 is blank; the ACCEPT's closing clause 'longer than it was the last time anyone ran the check' is line 72).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md lines 66-73 printed with sed -n 66,73p at trunk 41361dfefe: 66 blank, 67 'FWD-6 Whoever creates a name...', 68-69 DONE WHEN, 70-72 ACCEPT, 73 SOURCE."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-u-6 THE CELL: 'The PRD's FWD-6 is ...LGIC_BLANKFIX_PRD.md lines 66-71: its ACCEPT has two halves'; BU6-AC2: 'FWD-6's ACCEPT (PRD lines 66-71)'.",
  "world_is": "Lines 66-71 end mid-sentence in the ACCEPT; the second half of the ACCEPT (the list of unplaceable names no longer than before) is on line 72. The design quotes lines 67-73. Nothing is blocked; the CVO's reading at BU6-AC2 should take lines 67-73."
}
```

## LGIC_BLANKFIX-S10 -- 180 UNDECIDED fields hold 73 of the 74 drafted entries (parked to round 7)

```json
{
  "id": "LGIC_BLANKFIX-S10",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T18:39:50Z",
  "one_line": "Of the 74 entries BF-u-1 drafted, only inf-pipeline loads: 60 ordinary entries carry 180 UNDECIDED fields between them and 13 names:none entries wait on the reader (BF-u-2). 4.0.0_SA_CRO asks that a worker measure the 180.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND6_NOTES_20261008.md @6091606dd8 -- 'UNDECIDED fields: 180. By field: source 51, fills 49, scope 33, exceptions 26, system 19, why 2'; per-root list follows",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND6_NOTES_20261008.md @6091606dd8 -- 'Per entry (each alone): 1 PASS (inf-pipeline), 73 FAIL'; decided subset all ok=True mapped=14 items=776 hole=69",
      "4.0.0_SA_CRO msg 107107 -- 'have the round-6 worker measure the 180 UNDECIDED fields'; REC retire the 2 empty roots as dead Terraform rather than add a third why",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md -- FROZEN at the cut; no round-6 cell measures UNDECIDED fields"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round 6 E1: map the next roots, largest first; BF-u-1 drafts each field decided by a file and line or UNDECIDED, and the registry's lane writes the entries.",
  "world_is": "The drafts leave 180 fields UNDECIDED, so 73 of 74 entries cannot land; measuring them is work no frozen round-6 cell carries. Parked: owner 2.0.0_SA_COO~G; un-parks at the round-6 drain-end message to 1.0.0_SA_CTO as a round-7 input, with the CRO's empty-root retirement recommendation. The 13 names:none entries are BF-u-2's (slot ~4, queued)."
}
```

## LGIC_BLANKFIX-W4-S2 -- BU3-AC2 expects stale_hints=0 but the estate holds one item whose file is not in its ruling's declared_in

```json
{
  "id": "LGIC_BLANKFIX-W4-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-08T19:05:00Z",
  "one_line": "Built to the cell, `all` prints stale_hints=1 (not 0): the bd-pipeline freshness probe declares `bronze/`, a file the opal-assets-ingest-mirror ruling does not list; BU3-AC2 cannot be met as written.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_rootcheck.py (worktree wk-LGIC_BLANKFIX-4) `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json` -> `STALE-HINT bd-pipeline || FIX S3Key bronze/ -> orion/inflection/bronze/; the ruling's declared_in names infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py; the key is declared in infra/aws/lambda/bd-pipeline/bd-49f-freshness-probe/lambda_function.py  [...:74]`; last line ends `other_holes=0 stale_hints=1`",
      "infra/logic/registry/key_rulings.json -- the `bronze/` row (bucket opal-data-inf) lists only the ingest-mirror lambda_function.py in declared_in; the line's answer is the same as at the base (before and after bodies of the run differ only by the STALE-HINT line)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BU3-AC2: stale_hints=0 at the cut 'since every declared_in path exists' (4.0.0_SA_CRO, msg 106778); build item 2: a stale hint is a match where the item's file is not in the row's declared_in.",
  "world_is": "Existence of every declared_in path is not the test the build defines: the probe's `bronze/` matched this row at the base through its (bucket, key) match and now matches it as the only candidate of the key, so by the defined rule it is one stale hint. No weakening made. Two ways to reach 0, both outside this cell: the registry's lane adds the probe path to the row's declared_in, or the COO amends item 2 so a match the item's own bucket confirms is not stale."
}
```

## LGIC_BLANKFIX-W4-S3 -- BF-v-4 newly counts a local-built SCHEDULE name whose cadence the cadence reader cannot see: one new HOLE in a mapped root

```json
{
  "id": "LGIC_BLANKFIX-W4-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-08T21:34:00Z",
  "one_line": "BF-v-4 counts a local-built schedule name in the mapped root investor-reporting/intake and the run prints one new HOLE (hole=0 -> hole=1): the cadence reader sees only literal names, so no cadence row exists for it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json at wk-LGIC_BLANKFIX-4: `OTHER-HOLE investor-reporting/intake || SCHEDULE irpt-intake-poll -> partial form irpt-intake-poll-{cadence}; could not fill {cadence}: no cadence row for this name  [infra/aws/terraform/investor-reporting/intake/main.tf:122]`; the last line reads hole=1 other_holes=1 where the round-6 run (ALL_ROOTS_round6.txt) read hole=0",
      "infra/aws/terraform/investor-reporting/intake/main.tf:122 `schedule_name = \"irpt-intake-poll\"` (a literal local); the schedule resource names itself name = local.schedule_name",
      "lib/opal_naming_cadence.py cadences() builds its rows from opal_naming.census_tf_names(), which reads only literal names, so a schedule or event rule named through a local never gets a cadence row (lib/opal_naming_cadence.py:228-235)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-v-4 step 1: a locals value that is a literal is counted as an ordinary item with its where at the declaring line, and step 2: a mapped root's names newly counted by step 1 are graded like any other.",
  "world_is": "Graded like any other, the newly counted SCHEDULE has no cadence row, so decide() cannot fill {cadence} and prints a HOLE; the same newly counted names in investor-reporting/core, ycharts and opal-assets grade FIX or RIGHT. The moved mapped-root counts: investor-reporting/core items 21 -> 22, investor-reporting/intake 5 -> 10, investor-reporting/ycharts 14 -> 16, opal-assets 84 -> 117 (all other mapped roots unchanged). The hole is the honest reading and nothing was hidden or weakened; the repair is outside this cell's grant (lib/opal_naming_cadence.py would read the same locals the scope now resolves), and a where at the resource block line would not repair it because the cadence reader keys on the literal census names."
}
```

## LGIC_BLANKFIX-W4-S4 -- the round-5 saved-run check reads BF-v-4's newly counted names in four mapped roots as a difference

```json
{
  "id": "LGIC_BLANKFIX-W4-S4",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-08T21:40:00Z",
  "one_line": "The round-5 saved-run check (deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py, the BU3-AC3 instrument) now prints repeat=DIFFERS because BF-v-4 counts new names in four mapped roots.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py at wk-LGIC_BLANKFIX-4 -> `FAIL: investor-reporting/ycharts: 16 rows for 14 saved lines` / `FAIL: opal-assets: 117 rows for 84 saved lines` / `ALL-ROOTS-R5 ok=False mapped=13 unmapped=74 items=412 hole=0 stopped=0 repeat=DIFFERS`",
      "the same four roots are listed in row LGIC_BLANKFIX-W4-S3 with their before and after item counts; the unchanged mapped roots still match their saved lines"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-v-4 step 2: a mapped root's names newly counted by step 1 are graded like any other; and BU3-AC3 (round 6): no line of a mapped root changes its answer from the round-5 saved runs.",
  "world_is": "The two statements cannot both hold once a mapped root carries a name built in a local: the new lines are added rows, not changed answers, but the round-5 checker compares row counts against the saved file and reads any added row as a difference. No weakening made and the ~2 checker is outside this cell's grant; a later cell may re-baseline the saved run or let the checker ignore rows whose where is not in the saved file."
}
```

## LGIC_BLANKFIX-W3-S9 -- BF-v-5: the loader refuses the HOME-source convention where the root's system equals its scope (5 roots), and 39 entries took HOME scope/source values the round-6 drafts left UNDECIDED

```json
{
  "id": "LGIC_BLANKFIX-W3-S9",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T21:54:30Z",
  "one_line": "To decide the drafts' UNDECIDED scope/source fields I applied the registry's own HOME-value convention (opal-assets, investor-reporting/*); it needs the registry owner's ratification, and the loader refuses it for five roots whose system equals their scope.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/root_map.json:271 (opal-assets) and :362-:401 (investor-reporting/*): scope and source are entered as HOME values and fills leaves them out; I applied that to 55 fields (23 scope, 32 source) in 39 entries in org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/MAP_ENTRIES_round7.json (each field's _cite says which rule)",
      "lib/opal_naming_rootmap.py:_check_scope refuses scope == source ('a product is never a scope beneath itself'): the HOME source = the root's own system key is therefore unavailable for etfs-reports, etfs-netassets, etfs-canon (scope etfs), harvest (scope harvest) and mdpf-pipeline (scope mdpf); their source stays UNDECIDED in the entries file",
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_entries_land.py -> land=50 held=24 refused=0 undecided_fields=47 (round 6: 1 of 74 loading, 180 undecided)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-v-5: decide every UNDECIDED field the root's own files and the registry decide; a value is never taken from a folder's name alone; entries the loader accepts land.",
  "world_is": "Where a root touches several firms' buckets, or declares no stored name, or reads no one vendor, no file names a single scope or source; the only decision available is the registry's own HOME-value convention, which the draft authors did not apply. It is a convention extension, not a finding: 4.0.0_SA_CRO adopts or amends it per entry. For the five product roots the convention cannot apply and a real upstream source (or a ruling that an etfs/mdpf/harvest root names its upstream vendor) is owed."
}
```

## LGIC_BLANKFIX-W3-S10 -- BF-v-5: three round-6 UNDECIDED systems are decided by registry rows the drafts did not read, and the 42 inf-pipeline exceptions change no output line

```json
{
  "id": "LGIC_BLANKFIX-W3-S10",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-08T21:54:30Z",
  "one_line": "The round-6 drafts call the system of trade-pipeline, ticket-center and partner-etl-ops-alerts undecided, but the registry already names them; and listing the own-token exceptions changes no line the check prints.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/systems.json:406 (portal owner_basis): 'Terraform roots portal-auth, portal-content, trade-pipeline tagged Project = OpalPortal (main.tf:32), ticket-center tagged OpalPortal/TicketCenter'; infra/aws/terraform/trade-pipeline/main.tf:32 carries the tag; the draft (MAP_ENTRIES line 276, :746) says 'no systems.json key' / UNDECIDED",
      "infra/logic/registry/resources.json: rows partner-etl-ops-queue, partner-etl-ops-sqs-consumer, partner-etl-ops-sqs-consumer-role are system advi ('CALL2 F15 -- a5 family F15'); the draft (line 796) says no one system owns the channel",
      "ROOTCHECK for inf-pipeline with the 42 own-token exceptions and without them prints identical lines (items=364 right=39 fix=224 not_asked=57 pattern=13 hole=31 both ways), because an exception only acts on a name whose canonical form still carries a {system} blank and 3 of 364 do",
      "the blanket default tag Project = OpalPortal also sits on shared-infra, c3materialize-b4 and the six CompDiff roots (_root.tf), so the tag alone decides no root; the portal row names trade-pipeline and ticket-center explicitly"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round 6 drafted trade-pipeline, ticket-center and partner-etl-ops-alerts with system UNDECIDED, and exceptions as 'names the default would place wrongly'.",
  "world_is": "The registry decides those three systems (portal, portal, advi), so I decided them with the row cited; and the listed exceptions are redundant for the printed result today (they matter only for a {system}-blank name whose owner differs from the default). I entered them as the round-6 measurement defines them; the registry owner may drop them."
}
```

## LGIC_BLANKFIX-W4-S5 -- census --all-roots prints counts per root, not one line per name

```json
{
  "id": "LGIC_BLANKFIX-W4-S5",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-08T22:03:00Z",
  "one_line": "BF-v-1 CONTEXT says `census --all-roots` prints one line per name; it prints one ROOT line per mapped root, one UNCOUNTED line per uncounted name, and no RIGHT/FIX/... line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming.py census --all-roots at wk-LGIC_BLANKFIX-4 (HEAD d67274877f) -> 166 lines; first words: ALL-ROOTS 1, HOLE-CLASSES 1, OTHER-HOLE 1, ROOT 13, ROOTS 1, TOTALS 1, UNCOUNTED 74, UNMAPPED 74; zero lines of kind RIGHT, FIX, NOT-ASKED, PATTERN, CARDED, REFUSED or HOLE",
      "lib/opal_naming_rootcheck.py all_roots() (lines 723-841) calls run_one(..., report_only=True) into a local list and prints only that list's last (ROOTCHECK) line inside the ROOT line; ALL_ROOTS_round6.txt carries the same line kinds (ROOT 13, UNMAPPED 74, no per-name line)",
      "per-name lines come from `python lib/opal_naming.py census --root <root folder>` (check_root); the README section written by this cell says so"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-v-1 CONTEXT: the all-roots output is 'One line per name: KIND type current -> detail [where]', and the README section is to explain 'each line kind ... the per-name kinds'.",
  "world_is": "The per-name kinds exist only in a single-root run; the all-roots run shows them as per-root and total COUNTS (right=, fix=, ...). The README section describes the output as it is and names the single-root command for the per-name lines; the order's criterion is unaffected."
}
```

## LGIC_BLANKFIX-W1-S17 -- The CVO's first repair for arm C (call place() for an unmapped root) would not have rescued it

```json
{
  "id": "LGIC_BLANKFIX-W1-S17",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-08T22:36:50Z",
  "one_line": "The CVO's first repair for arm C (call place() for an unmapped root) would not have rescued it: arm A's name has no {system} blank, so removing the map entry changes nothing the check prints.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "armC_output.txt in org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1 (control FIX irpt-daily-pull-lambda; entry removed HOLE no map entry; fills [scope] HOLE multi-firm), produced by armC_run.py beside it at trunk 7d4d1524d9",
      "root check on a copy of the map without the entry, run in this worktree: ROOTCHECK ok=True ... items=15 right=13 fix=2 not_asked=0 hole=0 (lines FIX irpt-holdings-snapshot-daily, FIX irpt-directory-refresh-daily)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO BF-v-3 CONTEXT, repair 1: arm C (remove the root's map entry, expect `{system}: no map entry for this root` from place()) can be made to print by letting step 1 call place() for an unmapped root.",
  "world_is": "With the investor-reporting/directory entry removed from a copy of the map, check_root prints FIX SCHEDULE irpt-directory-refresh -> irpt-directory-refresh-daily unchanged (15 items, hole=0): the name irpt-directory-newjob-{cadence} has no {system} blank, so decide() never reaches the no-map-entry clause. The HOLE prints only for a name whose form has a {system} blank, e.g. a NEW Lambda `daily-pull` (grade: {system}-daily-pull-lambda): HOLE ... {system}: no map entry for this root. The design re-targets arm C to that name."
}
```

## LGIC_BLANKFIX-W1-S18 -- Two round-6 claims are contradicted by the code

```json
{
  "id": "LGIC_BLANKFIX-W1-S18",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-08T22:36:50Z",
  "one_line": "Two round-6 claims are contradicted by the code: an unmapped root DOES print root-check lines (hole=48 on smartx-pipeline), and the code holds 18 HOLE texts, not the grade's 14.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "check_fwd6_design_round7.py in org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1 prints one HOLE-TEXT line per text and the last line hole_texts=18 owned=18 unowned=0",
      "lib/opal_naming_rootcheck.py _ruling_of returns the three unread reasons (lines 207, 215, 218) and decide appends ans[ruling_unread] to the card and raised HOLE (lines 403-404, 409)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD6 design round 6, decision rule step 4: 'Unmapped roots have no lines, so no HOLE count to ratchet'; the CVO grade BU6-AC2: 'decide() and its callers print 14 distinct texts'.",
  "world_is": "python lib/opal_naming_rootcheck.py infra/aws/terraform/smartx-pipeline --map infra/logic/registry/root_map.json --report-only prints 117 item lines and ROOTCHECK ok=True ... hole=48 for a root with no map entry, so lines exist and the design now says why the ratchet leaves them out (no root map entry is 15 of the 48). The ast enumeration of lib/opal_naming_rootcheck.py finds 18 HOLE texts: 4 returns in decide, the card line, the frame, 8 why clauses, the collision, and 3 reasons _ruling_of appends to a card or raised HOLE (the grade counted 14, which omits the frame and the 3 suffixes). All 18 now have an owner row."
}
```

## LGIC_BLANKFIX-W2-S16 -- the repeat check had more than line numbers failing it at the trunk

```json
{
  "id": "LGIC_BLANKFIX-W2-S16",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-08T22:46:00Z",
  "one_line": "BF-v-6 names line numbers as the only failure of the repeat check; on the trunk it crashed first (FileNotFoundError) on a mapped root with no saved run and no ROOT line, and the root-line and ALL-ROOTS-field compares would also have failed on added names and roots.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py at base 4e2130eb1b -> traceback FileNotFoundError .../all_roots_round5/aaii-v2-bucket-lifecycle.txt (the map now holds 63 roots; 11 print 'NOTHING-TO-NAME <root> why=... names=0' and no ROOT line, so the script's ADDED list, built from ROOT lines, missed them)",
      "live `all` (63 mapped): ROOT lines differ from the saved ones for investor-reporting/core, intake, ycharts and opal-assets (items 22/10/16/117 vs 21/5/14/84; intake carries hole=1); last-line fields mapped, completed, items, right, fix, not_asked, pattern, hole and the HOLE-CLASSES fields all differ; live carries kinds NOTHING-TO-NAME (11), OTHER-HOLE (59), UNCOUNTED (242) that the saved run lacks",
      "the build compares per name and verdict, roots by presence and COMPLETED/STOPPED status, ALL-ROOTS fields roots_total and stopped only, and lists the rest: ALL-ROOTS-R5 ok=True mapped=13 unmapped=74 items=412 hole=0 stopped=0 repeat=identical with 39 ADDED roots, 40 ADDED-NAME, 3 UNLISTED-KIND lines printed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-v-6 THE CELL: the script reads ok=False on the trunk only because commit 51f4545acd shifted ycharts line numbers; the build is the name-line identity and the ADDED-NAME / not-compared-kind rules (items 1 to 3).",
  "world_is": "Three more causes stood at the base: a mapped root with no saved run and no ROOT line (NOTHING-TO-NAME) was not treated as ADDED; the per-root FIX brace check paired live rows with saved lines by position, which breaks when a name is added; and the ROOT-line and ALL-ROOTS-field compares failed on any added name or root. I made the added/not-compared rule cover them (item 2's intent) and kept every saved-run check as it was. A live-side HOLE (intake irpt-intake-poll, 'no cadence row') is printed as ADDED-NAME and is not graded here."
}
```

## LGIC_BLANKFIX-S11 -- the declares check reads newly mapped roots as missing (instrument, not census)

```json
{
  "id": "LGIC_BLANKFIX-S11",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-08T23:00:08Z",
  "one_line": "BV4-AC3's instrument reads ok=False on the trunk after the registry's lane mapped 8 of its 11 roots: it looks only for UNMAPPED lines, so a newly mapped root reads MISSING although still_zero=0.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_declares_names.py run on the trunk at the round-7 close -- 'DECLARES-CHECK ok=False roots=11 still_zero=0'; 8 lines 'MISSING <root>: no UNMAPPED line'",
      "infra/logic/registry/root_map.json @9b9928ea92 (4.0.0_SA_CRO, msg 107404) -- 50 entries written; mapped 63 of 87",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/LGIC_BLANKFIX.TO-BF-v-4.uncounted-names.md -- BV4-AC3 passed at its merge @52ea3e1784, before the entries landed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BV4-AC3: every root round 6 found declaring names behind a zero reads names > 0 or uncounted > 0.",
  "world_is": "The census holds (still_zero=0; the 3 still unmapped read above zero). The instrument assumed the roots stay unmapped; once mapped they print ROOT lines it does not read. Round-8 input: read a mapped root's ROOT line (items) as well. Owner 2.0.0_SA_COO~G; un-parks at the round-7 drain-end message."
}
```

## LGIC_BLANKFIX-W4-S6 -- the all command prints UNCOUNTED lines for mapped roots only (instrument, not census)

```json
{
  "id": "LGIC_BLANKFIX-W4-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-09T00:14:46Z",
  "one_line": "The all command prints one UNCOUNTED line only for a mapped root; an unmapped root prints a count (UNMAPPED <root> names=N uncounted=N) and no line, so a by-reason count of its UNCOUNTED lines cannot be read from that output alone.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round7.txt -- 24 UNMAPPED lines (for example 'UNMAPPED infra/aws/terraform/mdpf-pipeline names=64 uncounted=10') and 242 UNCOUNTED lines against uncounted=301 on the ALL-ROOTS line; 301 - 242 = 59, the sum of the UNMAPPED uncounted= fields",
      "lib/opal_naming_rootcheck.py lines 739-763 @HEAD -- emit_uncounted() runs for mapped roots only; the unmapped branch adds len(r_unc) to uncounted_all and prints the count",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_uncounted_delta.py -- reads the unmapped roots' names with opal_naming_scope.root_names and checks lines + unmapped counts == the live uncounted field (live run: 13 printed + 4 unmapped = 17)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-w-2 item 4: the script runs the all command once, counts the residual UNCOUNTED lines by reason and prints residual_reasons and bare_reasons.",
  "world_is": "The all output carries the reason only on the 242 round-7 lines of mapped roots (13 of the 17 residual now); the other names sit behind a count. The script counts them by calling root_names for each UNMAPPED root, a second read of the same repository at the same bytes, not a second all run. Round-8 input for the lane of opal_naming_rootcheck.py: print the unmapped roots' UNCOUNTED lines too, or the by-reason count of the estate stays a two-source read."
}
```

## LGIC_BLANKFIX-W4-S7 -- the not-judged cards still skip 47 names of the news and portal systems for a reason systems.json no longer holds

```json
{
  "id": "LGIC_BLANKFIX-W4-S7",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-09T01:54:56Z",
  "one_line": "47 name lines in the mapped roots (45 in news-pipeline, 2 in portal-auth and data-refresh) are skipped by a card that says the token (news, portal) is unresolved or in no vocabulary, while grade() reads the same names and returns a canonical form.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/systems.json: key news (PRODUCT, owner_basis Andrew-direct 2026-10-07 'Yes confirm as written') and key portal (PLATFORM_SUBSYSTEM) are system rows",
      "python lib/opal_naming_rootcheck.py news-pipeline --map infra/logic/registry/root_map.json: 59 HOLE lines, 45 of them 'skipped by a card; the card gives no correct name'; opal_naming.grade('news-ingestion-lambda-role', 'IAM_ROLE') returns CONFORMANT and grade('NewsIngestionPolicy', 'IAM_POLICY') returns OUT-OF-PATTERN with canonical news-ingestion-policy",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/REGISTRY_ROWS_round8.json: 47 name rulings drafted over those cards, each citing the card's own reason and the system row that now answers it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-6 owner table H4: a card that gives no correct name is a registry ruling of 4.0.0_SA_CRO (the card's canonical form or its no_name_owed line).",
  "world_is": "The cards were written against a registry in which news and portal were unresolved (OWNER_CARDS_R4.md Card 2); the registry has since resolved both, the cards were not revisited, and the root check still prints HOLE for each. A name ruling answers the line without editing the card file; a retired card would answer it too. The cell drafted the rulings and did not touch the card file (NOT_JUDGED_R13.json, outside the grant). The cards on the words 'security' and 'cache' (security-ops, portal-auth) are not stale: the grader still raises there, and 7 drafted rulings carry an explicit rename target (secops-..., portal-cache-...)."
}
```

## LGIC_BLANKFIX-W4-S8 -- the platinum key grammar admits no folder below a table, so drafted canonicals fold a folder into the table word

```json
{
  "id": "LGIC_BLANKFIX-W4-S8",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~4",
  "surfaced_at": "2026-10-09T01:54:56Z",
  "one_line": "grade() raises K4a on a platinum key such as mdpf/global/platinum/model_portfolios/views/ ('views' is not an entity partition {entity}={id}); the drafted key rulings therefore spell a folder into the table word (model_portfolios_views, macro_timeseries, market_overview_details).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -c \"import sys; sys.path.insert(0,'lib'); import opal_naming as o; print(o.grade('mdpf/global/platinum/model_portfolios/views/','S3Key'))\" raises RaiseDefect K4a: 'views' is not an entity partition {entity}={id}; the same path under gold grades CONFORMANT",
      "infra/aws/lambda/smartx_ingestion_pipeline/precompute_views.py:45 S3_OUTPUT_PREFIX = 'json/model_portfolios/views/'; infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py:57 DETAILS_PREFIX = 'json-tiered/market-overview/details/'",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/REGISTRY_ROWS_round8.json: rows json/model_portfolios/views/, json/macro/timeseries/, json-tiered/market-overview/details/ and the other json-tiered and json/market/ rows carry a flattened table word"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The key_rulings.json row_fields: canonical is the whole correct address under key.grammar, which grade() returns CONFORMANT.",
  "world_is": "The served keys of the portal bucket are folder trees (family/subfamily/file) and the platinum grammar reads one table level and then entity partitions. The drafted canonicals are CONFORMANT but are not a folder-for-folder move, so a served-output act that follows them also renames the portal's request paths. Whether the grammar should admit a sub-folder, or the registry's owner prefers the gold tier for these keys, is the CRO's and the CTO's call; every such row says it is a target name only."
}
```

## LGIC_BLANKFIX-W5-S2 -- STEP 13 of the onboarding checklist still types a run time

```json
{
  "id": "LGIC_BLANKFIX-W5-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~5",
  "surfaced_at": "2026-10-09T02:54:20Z",
  "one_line": "infra/logic/10_ONBOARDING_CHECKLIST.md STEP 13 still types a run time ('takes about 15 seconds') that the README section no longer states; the order's grant leaves STEP 13's text unchanged beyond its link.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/10_ONBOARDING_CHECKLIST.md:344-345 at 13e918299d: 'It reads the repository only (no AWS, no credentials), takes about 15 seconds, and runs to its totals'; the order's own CONTEXT says the map has overtaken such timings."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-w-5 build item 2: STEP 13 keeps (or gains) its link to the section; change nothing else in either document.",
  "world_is": "STEP 13 carries a typed timing of the same kind the order removes from the README section. The order's checker grades the README section only, so it reads ok=True with this sentence in place. Whether the checklist sentence is removed is the issuer's and the registry owner's call."
}
```

## LGIC_BLANKFIX-W3-S11 -- round 8 BF-w-4: recorded own-token exception lists omit LAMBDA names and one new mdpf policy

```json
{
  "id": "LGIC_BLANKFIX-W3-S11",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~3",
  "surfaced_at": "2026-10-09T03:18:10Z",
  "one_line": "The own-token exception lists entered in round 6/7 omit LAMBDA-type names (inf-pipeline 1, harvest 2) and one newer mdpf-pipeline policy, so the recorded lists are shorter than the same method gives on today's census.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "round 8 measurement (same method as the round-6 section: opal_naming.grade canonical form leads with a systems.json key other than the root's default) via lib/opal_naming_scope.root_names + opal_naming.grade at wk-LGIC_BLANKFIX-3: inf-pipeline (default advi) lists 46, infra/logic/registry/root_map.json holds 45 -- the missing one is LAMBDA inf-api-eclipse (eclipse); harvest (default harvest) lists 13, MAP_ENTRIES_round7.json holds 11 -- missing LAMBDA amgt-resapp-chatter-axis and LAMBDA opal-amgt-scoped-api (amgt); mdpf-pipeline (default mdpf) lists 1, MAP_ENTRIES_round7.json holds [] -- IAM_POLICY gateway-taxsma-workbook-bearer-read-policy (gateway, infra/aws/terraform/mdpf-pipeline/iam.tf:1274)",
      "ROOTCHECK prints identical lines with or without an exception unless the name still carries a {system} blank (row LGIC_BLANKFIX-W3-S10), so no printed line moves"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The round-6/7 entries' exceptions are 'every name of the root graded with opal_naming.grade whose canonical form leads with a systems.json key other than the default'.",
  "world_is": "Three roots' recorded lists are one to two names short on the current census (LAMBDA names, and a policy added to mdpf-pipeline after the round-6 measurement). I kept the round-7 lists for the entries whose exceptions the round-7 file already decided, and measured the new lists for the 15 entries I decided (they include LAMBDA names). The registry owner may add the three LAMBDA names and the mdpf policy; nothing prints differently."
}
```

## LGIC_BLANKFIX-W1-S19 -- the placement switch refuses in the gates, but safe-commit and safe-apply act on the rc only while the older switch is on

```json
{
  "id": "LGIC_BLANKFIX-W1-S19",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T03:28:06Z",
  "one_line": "the placement switch refuses in the gates, but safe-commit and safe-apply act on the rc only while the older switch is on",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/naming-gate.py (decide_exit) and .tools/safe-commit.sh lines 1030-1048 at trunk, read this session",
      ".tools/safe-apply.sh lines 238-252 and 295-309: 'if [ \"$NAPPLY_ENFORCE\" -eq 1 ] && [ \"$NPLAN_RC\" -ne 0 ]'",
      "ls org/mcp at the end of the build: naming-gate.enforce present, naming-place.enforce absent"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A switch file org/mcp/naming-place.enforce whose presence makes the gate refuse (TO BF-w-1 build item 2).",
  "world_is": "Both gates now exit 1 on a placement refusal while the new switch file is present, whatever naming-gate.enforce says. The callers decide what rc 1 does: .tools/safe-commit.sh unstages and aborts only when NGATE_ENFORCE=1 (naming-gate.enforce present or NAMING_GATE_ENFORCE=1), and .tools/safe-apply.sh blocks only when NAPPLY_ENFORCE=1; with the older switch absent a placement refusal is printed and the commit or apply goes on. Today naming-gate.enforce is present, so the two switches agree; turning only the new one on while the older is off would not block. Neither caller is in this order's grant."
}
```

## LGIC_BLANKFIX-W1-S20 -- safe-apply gives the plan-mode gate no tree, so door 2 finds an added resource's root by its name

```json
{
  "id": "LGIC_BLANKFIX-W1-S20",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T03:28:06Z",
  "one_line": "safe-apply gives the plan-mode gate no tree, so door 2 finds an added resource's root by its name",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/safe-apply.sh line 296: NPLAN_OUT=\"$(python \"$NAPPLY_GATE\" --plan-json \"$NPLAN_TMP.json\" 2>&1)\"",
      "exercise_fwd6_arms.py arms A, B and G drive the apply gate's plan mode on a hand-built plan that adds a name the tree holds"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Design 'Where it runs' step 3: the apply gate's plan mode calls the same placement step for an ADDED resource.",
  "world_is": "safe-apply.sh runs 'python naming-apply-gate.py --plan-json FILE' and passes neither the -chdir tree nor the root, and a plan document carries no path. The built gate takes an optional --root DIR and otherwise asks the scope which one root enumerates the added name (lib/opal_naming_rootcheck.py roots_of_name). A name no root lists (built from a variable or module) or that two roots list is graded by grade() alone and a NAMING PLACE-NOTICE line says so. The one-line follow-up, 'pass --root \"$NAPPLY_TREE\"' at safe-apply.sh line 296, is the safe-apply owner's: the file is outside this order's grant."
}
```

## LGIC_BLANKFIX-W1-S21 -- the build has no override, so turning the placement switch on leaves a creator with a registry-owed HOLE no way through

```json
{
  "id": "LGIC_BLANKFIX-W1-S21",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T03:28:06Z",
  "one_line": "the build has no override, so turning the placement switch on leaves a creator with a registry-owed HOLE no way through",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FWD6_DESIGN_round6.md 'The exercise that would prove it', arm H; TO BF-w-1 build item 3 'arms A to G' and 'FWD6-ARMS ok=True arms=7 held=7'",
      ".tools/naming-gate.py _NOT_A_NAME_VERDICTS: DECLARED-EXCEPTION and WAIVED-READ rows are never placed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Design arm H: an R20 register row id the registry holds passes the step with the id printed; a made-up id still refuses. The order's build list and its REPORT say arms A to G only (seven).",
  "world_is": "Arm H is not built, because the order names seven arms and the cell's build list has no override item. With the switch present, a NEW name the canon cannot place (a HOLE owed by 4.0.0_SA_CRO) refuses until the CRO writes the row; the only other pass is a declared exception the matrix already recognises (verdict DECLARED-EXCEPTION), which the step skips by design. Nothing is harmed while the switch stays absent, but the switch should not be turned on until the override is decided."
}
```

## LGIC_BLANKFIX-W1-S22 -- commit-time cost is about 13 s for a one-root commit; a builder-chosen cap of 8 roots is the only bound, and a hand-built diff cannot add a file the disk lacks

```json
{
  "id": "LGIC_BLANKFIX-W1-S22",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T03:28:06Z",
  "one_line": "commit-time cost is about 13 s for a one-root commit; a builder-chosen cap of 8 roots is the only bound, and a hand-built diff cannot add a file the disk lacks",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "arm A diff through .tools/naming-gate.py --diff, timed by the uncommitted harness .scratch/try_gate.py, this session: 'rc=1  12.8s' (switch present) and 'rc=0  15.0s' (absent)",
      "python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json at this trunk: ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24 ... hole=287"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Design 'Where it runs' step 5: one root check is about 8 s; the many-root cost is UNMEASURED and the build cell measures it and states the bound; the design's 'hole=0 over the 13 mapped roots' was the ratchet's starting denominator.",
  "world_is": "MEASURED this session at the trunk: the arm A commit (one root, placement, then HEAD run for the ratchet) takes 12.8 s with the switch present and 15.0 s with it absent, against about 2 s without the step; one root run is 3.5 to 4.5 s. Many roots are not measured: the gate places at most PLACE_ROOT_CAP = 8 roots per commit, prints a NAMING PLACE-NOTICE naming the rest, and does not refuse for them. The cap is the builder's choice (the design states none). A new .tf file that is in a diff but not on disk is not seen by the scope, so a hand-built diff cannot add one; in a real commit the file is on disk and in the index. The design's 'hole=0 over 13 mapped roots' no longer holds (ALL-ROOTS at this trunk: mapped=63, hole=287), so the exercise prints each arm's own head and post HOLE counts instead."
}
```

## LGIC_BLANKFIX-S12 -- two round-8 instruments read red on the trunk because their fixture HOLE closed before the merge

```json
{
  "id": "LGIC_BLANKFIX-S12",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T04:13:00Z",
  "one_line": "Two round-8 instruments read red on the trunk: ROOTCHECK-TEST (case 5, 'a fixed HOLE: the count shrinks') and arm F of exercise_fwd6_arms.py both edit the intake root's cron to remove a live HOLE, and that HOLE was already gone when BF-w-1 merged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run by 3.0.0_SA_CVO at HEAD ca565d1871: python lib/tests/test_opal_naming_rootcheck.py -> 'FAIL: a fixed HOLE: the count shrinks, no new line' and 'ROOTCHECK-TEST ok=False cases=319'",
      "run by 3.0.0_SA_CVO at HEAD ca565d1871: exercise_fwd6_arms.py -> 'ARM F ratchet shrinks | NOT HELD ... got: rc=0 holes head=0 post=0' and 'FWD6-ARMS ok=False arms=7 held=6'",
      "lib/tests/test_opal_naming_rootcheck.py:160-165 -- case 5 edits INTAKE_TF's cron and expects head_holes > post_holes",
      "run by 3.0.0_SA_CVO: python lib/opal_naming_rootcheck.py lines infra/aws/terraform/investor-reporting/intake --map infra/logic/registry/root_map.json -> 'NOT-ASKED SCHEDULE irpt-intake-poll ...' and 'ROOTCHECK ok=True ... hole=0'",
      "git merge-base --is-ancestor 46d6a05de0 cd219e95cd -> true: the CRO's round-8 registry write (2026-10-08 22:53 -0400) precedes the BF-w-1 merge (23:50 -0400)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Drain end ROUND8: BF-w-1 re-proved 'ROOTCHECK-TEST ok=True cases=320' and 'FWD6-ARMS ok=True arms=7 held=7'; the order bars a test from depending on a typed estate state that moves.",
  "world_is": "The re-proof ran in the slot's worktree, cut before the registry write. On the merged trunk the intake HOLE is NOT-ASKED, so the shrink case has nothing to shrink and both instruments read false. The build is not shown wrong: arms A-E and G hold. The fixture is a live estate HOLE, the same class as rows S6, S7 and S8. Repair: plant the HOLE in the overlay text, as arm D does, instead of reading one off the estate."
}
```

## LGIC_BLANKFIX-D1-S1 -- round-close-check grades 0 of 5 round-8 orders because their status carries a suffix; MAY-CLOSE is vacuous

```json
{
  "id": "LGIC_BLANKFIX-D1-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-09T04:18:02Z",
  "one_line": "round-close-check grades 0 of 5 round-8 orders because their status carries a suffix; MAY-CLOSE is vacuous",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/round-close-check.py --project LGIC_BLANKFIX --round 8 at origin/CLOUD 2b788e3b6b: 'ORDERS ... 5 order(s), 0 complete, 5 not complete and outside the verdict' ... 'graded=0 ... verdict=MAY-CLOSE'",
      "all five TO-BF-w-* order files read '<status>complete -- proof-of-spec VALID (rc=0)</status>'; .tools/round-close-check.py:275 tests o['status'] == 'complete' exactly"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "canonical-drive obligation 3: verdict=REFUSED means the round is not finished, so the check grades the round's complete orders and their proofs.",
  "world_is": "An order whose status is 'complete -- <note>' counts as neither complete nor terminal, so its proof is never read and the verdict passes on zero graded orders. Round 8 is genuinely complete (handoff 85ba7c79b2, each proof re-run by the issuer); the defect is in the instrument, whose owner is not this seat."
}
```

## LGIC_BLANKFIX-D1-W2-S1 -- the apply gate's pre-plan (directory) stage can never print a placement refusal, so the pre-plan wiring has no producer today

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T06:02:00Z",
  "one_line": "BF-x-3 asks safe-apply to act on a placement refusal in both stages, but the apply gate's pre-plan (directory) mode has no placement step and cannot refuse, so only the plan stage can produce one today.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/naming-apply-gate.py _main_dir: 'refused = sum(1 for g in graded if g[6])  # always 0: DIR mode grades every literal with judge_capped()' and its exit is 1 only on NAMING ERROR in enforce; place_additions is called only from run_plan",
      "exercise_switch_on.py arms B1 and B2 (0.9.0_WK_LGIC_BLANKFIX~2): the pre-plan wiring in .tools/safe-apply.sh blocks with exit 6 on a stand-in gate that prints 'NAMING-PLACE: REFUSE 1' while the switch is present, and passes with it absent; the real directory-mode gate prints no such line"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-x-3 build 2: safe-apply acts on the placement refusal from naming-apply-gate.py 'in both its pre-plan and plan stages'.",
  "world_is": "Both stages are wired to act on the gate's NAMING-PLACE line (pre-plan: exit 6 for an unscoped apply, warn only for a scoped or planfile apply as before; plan: exit 7). Only the plan stage has a producer: the directory mode cannot tell an addition from an existing resource and runs no placement step. The pre-plan arms therefore use a stand-in gate and prove the script's wiring, not the gate's output. No change to the gate's directory mode was made; whether it should place anything is the owner's call."
}
```

## LGIC_BLANKFIX-D1-W2-S2 -- org/naming-place-override-audit.log is named in the write grant but is gitignored runtime state (*.log), so the audit lines never travel in a commit

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T06:21:00Z",
  "one_line": "BF-x-4 lists org/naming-place-override-audit.log in its paths, but .gitignore line 68 (*.log) ignores it, as it does org/git-author-override-audit.log, so each box's override rows stay on that box.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git check-ignore -v org/naming-place-override-audit.log org/git-author-override-audit.log -> .gitignore:68:*.log for both; git ls-files org/git-author-override-audit.log -> empty",
      "exercise_override.py arm O1 (0.9.0_WK_LGIC_BLANKFIX~2): the audit line is appended in the box's tree by .tools/safe-commit.sh and the gate reads it there"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-x-4 build 1 and its paths block: safe-commit appends one audit line to org/naming-place-override-audit.log, a path inside the write grant.",
  "world_is": "The file is created at first use and is never tracked, like the older git-author-override audit log the cell modelled it on; the gate's check is local to the box and the 600-second window, so nothing needs the line to travel. I did not create the file, add a negation to .gitignore (outside the grant) or commit a placeholder. Whether the override rows should be tracked for review is the owner's call."
}
```

## LGIC_BLANKFIX-D1-S2 -- the scope test pins uncounted as the ALL-ROOTS line's last field, so BF-x-5's appended field reads red at the drain

```json
{
  "id": "LGIC_BLANKFIX-D1-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-09T07:04:59Z",
  "one_line": "the scope test pins uncounted as the ALL-ROOTS line's last field, so BF-x-5's appended field reads red at the drain",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain hygiene on wk-LGIC_BLANKFIX-1 @467d08b99b: 'FAIL: the estate run counts uncounted at the end of its last line: other_holes=2 stale_hints=0 uncounted=0 counted_at_caller=17' / 'SCOPE-TEST ok=False assertions=831'; the trunk reads SCOPE-TEST ok=True assertions=831",
      "lib/tests/test_opal_naming_scope.py:370 asserts last.split()[-1].startswith('uncounted='); TO-BF-x-5 build item 1 told the cell to append counted_at_caller after uncounted, and its grant did not name the scope test"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Every lib/tests/test_opal_naming_*.py script that passes at the base passes after the build (each order's CONTEXT bar).",
  "world_is": "The cut asked for a new trailing field and named the one reader it knew (the rootcheck test), not the scope test that reads the same line by position. Issuer's cut defect; ruled by TO-BF-x-5 AMENDMENT 2 (grant the scope test; read uncounted by key)."
}
```

## LGIC_BLANKFIX-D1-W1-S1 -- BX1-AC2 cannot read ok=True: hole_before is read from the round-8 ALL-ROOTS line (hole=10, mapped=63) but the live run is mapped=78

```json
{
  "id": "LGIC_BLANKFIX-D1-W1-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T06:20:50Z",
  "one_line": "BX1-AC2 cannot read ok=True: hole_before is read from the round-8 ALL-ROOTS line (hole=10, mapped=63) but the live run is mapped=78",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ALL_ROOTS_round8.txt last line: 'ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24 ... hole=10 ... other_holes=10'",
      "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_h8_rule.py -> ten names NOT-ASKED; 'H8-RULE ok=False owned=10 not_asked=10 hole_before=10 hole_after=41 mapped=78'",
      "the order's CONTEXT gives the base reading hole=51 mapped=78; 51 minus the ten H8 holes is 41 = hole_after"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BX1-AC2: hole_before is read from ALL_ROOTS_round8.txt and hole_after < hole_before holds once the ten H8 names read NOT-ASKED.",
  "world_is": "The round-8 file was taken with 63 roots mapped; the live run maps 78, so hole_before=10 is not comparable with hole_after=41. The build holds (10 of 10 names NOT-ASKED, hole fell 51 to 41 on the same 78 roots) but the order's own comparison reads false. Not weakened; the order stays open for the issuer to name the right baseline (the CONTEXT's hole=51)."
}
```

## LGIC_BLANKFIX-D1-W1-S2 -- exercise_override.py (the ~2 script the order says to keep passing) fails O12 at the base and O1, O5, O7 once BF-y-1 moves the audit row; the script is outside the write grant

```json
{
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T08:32:54Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "LGIC_BLANKFIX-D1-W1-S2",
  "one_line": "exercise_override.py (the ~2 script the order says to keep passing) fails O12 at the base and O1, O5, O7 once BF-y-1 moves the audit row; the script is outside the write grant",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "at base 46f6d8a447: python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/exercise_override.py -> 'O12 ... got: switch present, audit log absent ... FAIL' and 'OVERRIDE-ARMS ok=False arms=12 held=11' (O12 expects naming-place.enforce ABSENT; the switch is present since 4d2bfc6dfd)",
      "after BF-y-1 the same unmodified script: O1, O5, O7 FAIL (they read the ignored org/naming-place-override-audit.log, which the cell no longer writes) plus O12: 'OVERRIDE-ARMS ok=False arms=12 held=8'",
      "the adjusted copy org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_override.py (O1/O5/O7 read the staged jsonl row, O12 compares the switch and audit file bytes before and after): 'OVERRIDE-ARMS ok=True arms=12 held=12'"
    ]
  },
  "spec_asserts": "The lead's brief: keep exercise_override.py and exercise_switch_on.py passing, adjusting only an arm the cell legitimately changes, and name each such arm.",
  "world_is": "The ~2 script lies outside this order's <paths>, so it was left as it was and its adjusted copy sits in the ~1 deliverables folder (arms named in its docstring: O1, O5, O7, O12; O2-O4, O6, O8-O11 unchanged). exercise_switch_on.py passes unchanged (SWITCH-ON ok=True arms=11 held=11). The ~2 script still fails O12 on its own, a defect that predates this cell."
}
```

## LGIC_BLANKFIX-D1-W1-S3 -- BLIND: a real override commit adds org/audit/naming-place-override-audit.jsonl, a path the MSTR ledger hook's record-only list does not name; no hook or lane gate ran in the temporary trees

```json
{
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T08:32:54Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "LGIC_BLANKFIX-D1-W1-S3",
  "one_line": "BLIND: a real override commit adds org/audit/naming-place-override-audit.jsonl, a path the MSTR ledger hook's record-only list does not name; no hook or lane gate ran in the temporary trees",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      ".tools/git-hooks/mstr-ledger-check.sh lists record-only paths near its line 197-199 (org/mcp/agent-spawn-audit.log, org/git-author-override-audit.log, org/audit/archive/*); org/audit/naming-place-override-audit.jsonl is not among them",
      "exercise_audit_in_commit.py cuts the naming stage of .tools/safe-commit.sh and lands with git commit --only in a temporary repository that carries no hooks, so no hook and no lane gate graded the audit path"
    ]
  },
  "spec_asserts": "BF-y-1: safe-commit.sh adds the audit file to the pathspec of the commit it permits, so the landed commit carries its own row.",
  "world_is": "Not exercised end to end: whether a hook (the MSTR ledger check for an MSTR-authored commit, or a lane/ownership gate for another lane) refuses a commit that carries org/audit/naming-place-override-audit.jsonl is unread. A refusal fails closed (the override commit does not land, the unwind removes the row), so the hazard is INERT. The hook and the lane tables are outside BF-y-1's paths; the owner of each decides."
}
```

## LGIC_BLANKFIX-D1-W1-S4 -- a refusal AFTER the naming stage (a later gate) leaves the override row on disk; only the naming blocks and a failed git commit unwind it

```json
{
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T08:32:54Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "LGIC_BLANKFIX-D1-W1-S4",
  "one_line": "a refusal AFTER the naming stage (a later gate) leaves the override row on disk; only the naming blocks and a failed git commit unwind it",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      ".tools/safe-commit.sh: _np_unwind is called on the two naming-stage BLOCKED branches and when git commit returns non-zero; the gates between them (surprise-row-gate, prd-manifest-gate, comp-system, pipeline-gate2) exit 1 without it",
      "exercise_audit_in_commit.py C6 holds the naming-stage refusal (rc=1, disk and index = the seed); with _np_unwind neutered the same arm FAILS (audit disk CHANGED, index CHANGED), so the unwind is what holds C6"
    ]
  },
  "spec_asserts": "BF-y-1: a commit with no override line does not touch the audit file; nothing else in the commit flow changes.",
  "world_is": "When a later gate refuses an overridden commit, the row for that unlanded attempt can stay in the working copy and ride into the next commit that stages the file, as an audit row of an attempt that permitted nothing. Over-recording, never under-recording; the naming-stage and commit-failure cases are held and exercised."
}
```

## LGIC_BLANKFIX-D1-W1-S5 -- msg_sha256 binds the message text as PASSED to safe-commit.sh (the -F bytes, or -m texts joined by a blank line), not the bytes git stores after its own message cleanup

```json
{
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T08:50:05Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "LGIC_BLANKFIX-D1-W1-S5",
  "one_line": "msg_sha256 binds the message text as PASSED to safe-commit.sh (the -F bytes, or -m texts joined by a blank line), not the bytes git stores after its own message cleanup",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      ".tools/safe-commit.sh override block (BF-y-2): NP_MSGFILE is written from COMMIT_ARGS (-F file bytes; -m texts joined by a blank line); the commit itself is `git commit --only \"${COMMIT_ARGS[@]}\"`, which applies git's default cleanup (whitespace mode for -F/-m: trailing whitespace and surrounding blank lines stripped, one trailing newline added)",
      "exercise_override_bound.py B1/B2 hold the hash against the text as passed (-F bytes; two -m texts joined by a blank line); a stored-message hash was not computed, and `-F -` (stdin) is read by no override reader at all, as before BF-y-2"
    ]
  },
  "spec_asserts": "BF-y-2: msg_sha256 = sha256 of the exact committed message (the -m/-F text, as passed).",
  "world_is": "The binding is to the text safe-commit.sh is handed, which is what the gate can be handed before the commit exists; git's cleanup can change trailing whitespace and blank lines in the stored message, so the stored message may differ from the hashed text in whitespace only. The row still cannot admit a commit whose message text differs in any other byte (B7 holds one extra byte refused). A reader who needs the stored message's own hash would have to hash it after the commit, which is outside this gate. The row's trust base is unchanged: a seat that can stage a row and hash its own message can still forge one."
}
```

## LGIC_BLANKFIX-S13 -- round 9's two exercise scripts spawn a bare bash and false-fail on a box with WSL

```json
{
  "id": "LGIC_BLANKFIX-S13",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T07:55:00Z",
  "one_line": "Round 9's exercise_switch_on.py and exercise_override.py spawn a bare 'bash' from Python; on a Windows box with WSL installed CreateProcess reaches System32 bash.exe first, so both read ok=False on the laptop although every arm holds with Git Bash.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run by 3.0.0_SA_CVO in a detached worktree of origin/CLOUD 4016b2ec41: exercise_switch_on.py -> 'SWITCH-ON ok=False arms=11 held=1'; exercise_override.py -> 'OVERRIDE-ARMS ok=False arms=12 held=7'; one arm's output 'WSL (9 - Relay) ERROR: CreateProcessCommon:800: execvpe(/bin/bash) failed'",
      "the same scripts through a wrapper that maps argv[0] 'bash' to the Git Bash executable and changes nothing else: 'SWITCH-ON ok=True arms=11 held=11', 'OVERRIDE-ARMS ok=True arms=12 held=12'",
      "exercise_switch_on.py run_bash(): subprocess.run(['bash', ...]); prepending Git's /usr/bin to PATH does not change the result (System32 precedes PATH in the CreateProcess search)",
      "CLAUDE.md Git section: Python spawning ANY MSYS binary uses .tools/msys_argv_guard.py msys_safe_run(), never bare unix names"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BX3's criterion and BX4-AC1 read ok=True wherever the issuer or the CVO runs them.",
  "world_is": "They read ok=True on dell1 and ok=False on the laptop for an environment reason, not a gate one. The production gates spawn no bare bash (naming-gate.py, naming-apply-gate.py, opal_naming_rootcheck.py, opal_naming.py searched)."
}
```

## LGIC_BLANKFIX-D1-W2-S3 -- the base has 88 Terraform roots and 10 unmapped, not 87 and 9: advi/billing-read (4 names) is a root the round-9 close does not hold, so the cell's census reads roots_total=86, not 85, after the two retirements

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T09:23:30Z",
  "one_line": "the base has 88 Terraform roots and 10 unmapped, not 87 and 9: advi/billing-read (4 names) is a root the round-9 close does not hold, so the cell's census reads roots_total=86, not 85, after the two retirements",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming.py census --all-roots on this worktree at 0f652707c8 (before any edit): 'ALL-ROOTS ok=True roots_total=88 mapped=78 unmapped=10 ... hole=0'; UNMAPPED infra/aws/terraform/advi/billing-read names=4 uncounted=0",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9.txt: roots_total=87 unmapped=9 with no advi/billing-read; investor-reporting/export reads items=29 there and items=35 on this base",
      "check_held_entries_round10.py (0.9.0_WK_LGIC_BLANKFIX~2): after the seven entries and the two retirements the merged run prints roots_total=86 mapped=85 unmapped=1 (advi/billing-read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order's CONTEXT: at this cut the census reads roots_total=87 mapped=78 unmapped=9; after the two retirements roots_total reads 85 (the CRO's ruling R10-4).",
  "world_is": "The base is later than the round-9 close: advi/billing-read exists, is tracked, and no map entry or cell names it. The cell maps the seven it was given and retires the two; it does not map the tenth. The check compares the merged denominator with the live count before the retirements (88 - 2 = 86) and lists the unmapped root by name, so it neither hides it nor claims 85. Whoever owns advi/billing-read owes it an entry; roots_total=85 holds only once it is mapped or retired."
}
```

## LGIC_BLANKFIX-D1-W2-S4 -- lib/opal_naming_keyfill.bucket_of reads the file's only opal-data literal as the bucket of every key in the file, so a correct key-ruling row for a key in another bucket (a globgrph or lambda-artifacts bucket, or an s3:// URI constant) is dropped and the hole stays

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S4",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T09:24:00Z",
  "one_line": "lib/opal_naming_keyfill.bucket_of reads the file's only opal-data literal as the bucket of every key in the file, so a correct key-ruling row for a key in another bucket (a globgrph or lambda-artifacts bucket, or an s3:// URI constant) is dropped and the hole stays",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming_rootcheck.py _ruling_of: 'a candidate must also agree on the bucket wherever the item's bucket is known' -- known, _why = bucket_of(item); cands = [r for r in cands if r.get('bucket') in (None, known)]",
      "lib/opal_naming_keyfill.bucket_of on the shared-infra items of infra/aws/lambda/infrastructure_monitor/lambda_function.py: warehouse/_branch_head.main.json -> ('opal-data-portal-v2', \"the file's only bucket literal 'opal-data-portal-v2' (line 96)\") while the code reads GLOBGRPH_BUCKET = 'opal-313476888478-globgrph' at line 123; contract_integrity/latest.json the same",
      "bucket_of on ec2/astn-wsjft/deploy.sh -> 'opal-data-astn' (line 58) and on ec2/etfs-reports -> 'opal-data-etfs' (line 49), while both keys are in s3://opal-313476888478-lambda-artifacts/... URI constants (astn-wsjft-orchestrator/lambda_function.py:61, etfs-reports-orchestrator/lambda_function.py:53)",
      "check_held_entries_round10.py: the rows for those keys (REGISTRY_ROWS_round10.json) merge with no refusal and the four HOLE lines stay; each has an OWNED line to 1.0.0_SA_CTO in HOLES_OWNED_round10.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A registry row (bucket, key[, declared_in]) answers a stored-file path wherever the code writes that bucket and key.",
  "world_is": "A row whose bucket is the true bucket does not match when the reader names a different one, so four paths on two newly mapped roots stay HOLE although their rows are drafted. The registry's existing row for warehouse/_branch_head.main.json has the same problem on this root. I did not edit lib/ (outside the grant) and did not write a row with the wrong bucket to force a match."
}
```

## LGIC_BLANKFIX-D1-W2-S5 -- the ruling keeps harvest at '11 amgt names' and 0 on the others; grade() measures 13 on harvest (two LAMBDA names) and 1 on mdpf-pipeline (an IAM policy led by gateway), so the entries list what is measured

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S5",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T09:24:30Z",
  "one_line": "the ruling keeps harvest at '11 amgt names' and 0 on the others; grade() measures 13 on harvest (two LAMBDA names) and 1 on mdpf-pipeline (an IAM policy led by gateway), so the entries list what is measured",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ROOT_MAP_ROUND10_RULINGS_20261009.md:50 'Exceptions stay as measured in round 8 (harvest's 11 amgt names; 0 on the others).'",
      "check_held_entries_round10.py prints EXCEPTIONS harvest listed=13 measured=13 and EXCEPTIONS mdpf-pipeline listed=1 measured=1; the round-8 draft lists 11 for harvest (MAP_ENTRIES_round8.json) and 0 for mdpf-pipeline",
      "the 13 are the 11 plus the LAMBDAs amgt-resapp-chatter-axis (chatter-axis-schedule.tf:178) and opal-amgt-scoped-api (scoped-amgt-api.tf:455); the 1 is the IAM policy gateway-taxsma-workbook-bearer-read-policy (mdpf-pipeline/iam.tf:1274); mdpf-pipeline read 64 items at round 8 and reads 78 now"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The ruling's measured counts (R10-3, :50): harvest 11, the other four roots 0.",
  "world_is": "The root map's own rule is 'measured by the cell'; the entries carry the 13 and the 1, each cited to its line, and the check fails on an unlisted or a wrongly listed exception. None of them changes a verdict (the names already lead with their own system), so the registry owner can strike the three extra rows without effect if the ruling's counts are meant literally."
}
```

## LGIC_BLANKFIX-D1-W1-S6 -- the order says test_opal_naming_rootcheck.py reads ROOTCHECK-TEST ok=False at the base on case 5 only; on this worktree it reads ok=True cases=324 with the base-pin keyfill and with the BF-z-1 keyfill

```json
{
  "id": "LGIC_BLANKFIX-D1-W1-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~1",
  "surfaced_at": "2026-10-09T10:02:49Z",
  "one_line": "the order says test_opal_naming_rootcheck.py reads ROOTCHECK-TEST ok=False at the base on case 5 only; on this worktree it reads ok=True cases=324 with the base-pin keyfill and with the BF-z-1 keyfill",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/tests/test_opal_naming_rootcheck.py in C:/tmp/wk-blankfix-1 with lib/opal_naming_keyfill.py temporarily set to git show 32c925520c:lib/opal_naming_keyfill.py (restored after): last line ROOTCHECK-TEST ok=True cases=324",
      "same test with the BF-z-1 keyfill: ROOTCHECK-TEST ok=True cases=324; the other nine lib/tests/test_opal_naming_*.py scripts also print ok=True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order's CONTEXT: every lib/tests/test_opal_naming_*.py prints ok=True at the base except test_opal_naming_rootcheck.py, which reads ok=False there on case 5 only (row S12; cell BF-x-2 repairs it).",
  "world_is": "At base 32c925520c the rootcheck test already prints ok=True (324 cases, no FAIL line), so case 5 does not fail in this worktree; whether BF-x-2 already landed in the base or the failure depends on the device or the day is not read here. The BF-z-1 keyfill build does not change the result either way."
}
```

## LGIC_BLANKFIX-D1-S3 -- retiring opal-assets-absence removes the last repo trace of an ORPHANED log group: the function it names, opal-assets-absence-check, does not exist, but /aws/lambda/opal-assets-absence-check is live with 6 streams, ~4.8 KB and NO retention policy, declared by nothing (drift=LIVE-no-DECLARED)

```json
{
  "id": "LGIC_BLANKFIX-D1-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-09T10:31:19Z",
  "one_line": "retiring opal-assets-absence removes the last repo trace of an ORPHANED log group: the function it names, opal-assets-absence-check, does not exist, but /aws/lambda/opal-assets-absence-check is live with 6 streams, ~4.8 KB and NO retention policy, declared by nothing (drift=LIVE-no-DECLARED)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-find --corpus aws 'opal-assets-absence': DENOMINATOR 1 hit across 2844 aws nodes scanned, the single hit [LOG_GROUP] /aws/lambda/opal-assets-absence-check drift=LIVE-no-DECLARED src=full-derive (graph vintage 2026-10-09 06:17:57Z, stitch manifest 1089b9991c93).",
      "lambda get-function-configuration --function-name opal-assets-absence-check: ResourceNotFoundException 'Function not found: arn:aws:lambda:us-east-1:313476888478:function:opal-assets-absence-check'. The function is gone.",
      "logs describe-log-groups --log-group-name-prefix /aws/lambda/opal-assets-absence-check: storedBytes 4811, retentionInDays None -- no retention policy, so it never expires.",
      "logs describe-log-streams --query length(logStreams): 6. Not a husk -- the function ran before it was removed.",
      "The root's own state is EMPTY (terraform state list prints nothing, rc=0, against a positive control of 238 addresses on infra/aws/terraform/opal-assets), so the log group is NOT owned by this root and the order's refusal clause does not fire: that clause turns on a non-empty state or a resource OWNED by the root, and neither holds. The retirement proceeded."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-aa-1 step 2: 'Prove nothing in AWS is owned by it ... record AWS-OWNED <root> count=0'. The cell's adversary preflight names the arm this row came from: 'a resource outside state but in AWS (the AWS-OWNED read)'.",
  "world_is": "AWS-OWNED is genuinely 0 for this root, and the orphan is reported rather than rounded away. After this commit the folder is gone from git, so nothing in the repo mentions opal-assets-absence-check at all and the log group's only trace is this row plus the evidence file. It costs ~4.8 KB and nothing operationally; it is a cleanup item with no owner, not a hazard. Owner of the choice: whoever owns the estate's LIVE-no-DECLARED set -- a log-group delete is out of this cell's grant and is listed for Andrew in the report alongside the two remote-state objects.",
  "notes": "ID DEVIATION, REPORTED NOT ADJUDICATED: the order prescribes the scheme LGIC_BLANKFIX-D1-CO1-S<k>, and the live surprise-row gate refuses it. Only the CO1 segment is wrong -- the D1 coordinate is REQUIRED, not optional: the gate states 'A row filed on dell1 is written <CODE>-D1-S<n> (worker: <CODE>-D1-W<n>-S<k>); a bare id is the laptop's', with laptop/cloud-local = <CODE>-S<n>, sitez = <CODE>-Z-S<n>, dell1 = <CODE>-D1-S<n>, dell2 = <CODE>-D2-S<n>. This seat first over-corrected to a bare LGIC_BLANKFIX-S14 after reading the gate's abbreviated grammar string, and the fabric limb refused that too -- correctly, since a bare id would have claimed the laptop fabric for a dell1 row. The id here is the next free dell1 bare index. 2.0.0_SA_COO~B1 may re-label; the only thing the order got wrong is CO1. Distinct from the W1/W2 rows, which concern the naming keyfill and the root map rather than AWS orphans."
}
```

## LGIC_BLANKFIX-D1-W2-S6 -- 20 of 254 stored-file lines (13 RIGHT, 7 FIX) have no key ruling and no key class: the grader alone produced the location, so source and owner are read from the grader's address by the key grammar's slot order

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S6",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T11:34:30Z",
  "one_line": "20 of 254 stored-file lines (13 RIGHT, 7 FIX) have no key ruling and no key class: the grader alone produced the location, so source and owner are read from the grader's address by the key grammar's slot order",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "check_fwd4_stored_files.py prints FWD4-STORED ok=True files=254 with_source_owner=230 undecided=24; origins counted from the same run: 218 key ruling, 16 key class ADDRESS, 20 grader only (opal_naming_keyfill._classify skips an item whose graded canonical has no {source}/{scope} blank, so no key row exists for it)",
      "examples of the 20: RIGHT S3Key blackdiamond/49financial/bronze/ and FIX S3Key blackdiamond/49f/bronze/ -> blackdiamond/49financial/bronze/ (root opal-assets); FIX S3Key platinum/mdpf/global/aum-metrics.json -> mdpf/global/platinum/aum-metrics.json (yang-pipeline)",
      "lib/opal_naming_rootcheck.py stored_origin()/stored_source_owner(): the address is split on '/', segment 1 is a source only if it is in the registry's source vocabulary, segment 2 an owner only if it is in the firm or product scope vocabulary; else UNDECIDED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-ab-2 Build 1: 'source=<system> owner=<firm or system> read from the same ruling or key class that produced the location (never inferred from the folder name)'.",
  "world_is": "For these 20 lines the producer is the grader (grade() with the key grammar {source}/{scope}/{tier}/...), which is neither a ruling nor a key class. They are read from the grader's own address by the grammar's slot order and the vocabulary, never from the folder the file sits in now, and UNDECIDED when a word is in no vocabulary. If the CTO reads 'ruling or key class' as excluding the grader, these 20 lines should print UNDECIDED instead; that is a one-line change in stored_origin()."
}
```

## LGIC_BLANKFIX-D1-W2-S7 -- a key ruling's own `owner` field names who moves the store (a directive or project), not the firm that owns the file, so it is not the line's owner= value

```json
{
  "id": "LGIC_BLANKFIX-D1-W2-S7",
  "project": "LGIC_BLANKFIX",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-09T11:34:31Z",
  "one_line": "a key ruling's own `owner` field names who moves the store (a directive or project), not the firm that owns the file, so it is not the line's owner= value",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/key_rulings.json _about.row_fields: 'owner (who moves the store, where one is named)'; the 161 rows hold values such as 'ADVI_FIRMBKTS moves the bucket opal-data-inf ...' and 'Directive D8 (the Yang portal pipeline ...)'",
      "the printed owner= is the second segment of the ruling's canonical address (the key grammar's {scope}: a firm such as 49financial, or a scope such as global)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BF-ab-2 Build 1 and FWD-4 ACCEPT: 'a stored file's new location with where it came from and whose it is filled in'; the order's word 'owner' could be read as the ruling row's `owner` field.",
  "world_is": "Two meanings of 'owner' live in the repository: the ruling row's mover and the address's scope (whose file it is). The line prints the second, as FWD-4 says 'whose it is'. The ruling's mover text is long prose and stays on the ruling."
}
```
