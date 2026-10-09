# MDPF_CANON -- surprise channel, INVESTIGATION v1 (round 1, dell1). Append-only; rows below are validated by `.tools/surprise-row-gate.py` at commit.

```json
{
  "id": "MDPF_CANON-D1-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-09T18:54:16Z",
  "one_line": "Three data/mdpf/scripts/gold/tests/test_global_fold_flag2.py cases fail at box/dell1 before any MDPF_CANON change (carried vs measured label; 128.0 vs 120.0) -- a pre-existing red in the global fold's tests, not this project's.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes it to the global fold's owner; last commits 0.4.0_DS_ClientPlatform 0d653d4aa3/e56eef609e/4ed8a19775)",
  "spec_asserts": "A round's regression criterion runs the gold tests and expects 0 failed.",
  "world_is": "python -m pytest data/mdpf/scripts/gold/tests -q at box/dell1 (2026-10-09 ~18:5xZ): 3 failed, 94 passed -- test_carry_within_window_carries_and_labels, test_carry_beyond_window_absent_for_real, test_carry_source_is_measured_never_interpolated. Round 1's AC2 deselects exactly these three by node id so the project's own regressions stay visible.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest data/mdpf/scripts/gold/tests -q (3 failed, 94 passed)",
      "git log -- data/mdpf/scripts/gold/tests/test_global_fold_flag2.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed at L5 by the issuer; no cell of this project owns the global fold."
}
```

```json
{
  "id": "MDPF_CANON-D1-W1-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~1",
  "surfaced_at": "2026-10-09T19:08:20Z",
  "one_line": "CN-a-1 names the composite bucket as scope_bucket['global'], but that map entry is opal-data-portal-v2; address(mdpf, global, gold, ...) puts the composite gold in opal-data-mdpf. The build uses local.mdpf_bucket (opal-data-mdpf).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-a-1 item 2: the gold Lambda's Put/Get on mdpf/global/gold/<artifact>/* is in the composite bucket 'from the module's scope_bucket for scope global, never typed'; the same item and AC1 arm 4 name that bucket opal-data-mdpf.",
  "world_is": "infra/aws/terraform/modules/opal_name/generated_locals.tf scope_bucket[\"global\"] = \"opal-data-portal-v2\"; lib/opal_naming.py address(\"mdpf\",\"global\",\"gold\",\"aum_metrics\",\"date=2026-10-08\") = s3://opal-data-mdpf/mdpf/global/gold/aum_metrics/date=2026-10-08. Following the map literally would grant the four prefixes in opal-data-portal-v2, a bucket the parquet emitter never writes. iam.tf uses the existing local.mdpf_bucket (main.tf:56, the same local the TAXSMA control grant uses at mdpf_gold_taxsma). r1_iam.py arm 4 does not read the bucket and passes either way; the bucket is not typed in the new block.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/modules/opal_name/generated_locals.tf@155ac2ce67 scope_bucket global",
      "python -c address('mdpf','global','gold','aum_metrics','date=2026-10-08')",
      "infra/aws/terraform/mdpf-pipeline/main.tf:56 mdpf_bucket"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-09T19:43:35Z",
  "one_line": "CN-a-1's C4 names iam:SimulatePrincipalPolicy as its invocation, but that API is denied to the dell1 CloudOps principal for every policy source but its own, so C4 was answered with a committed identity-policy evaluator instead -- the THIRD WORLD-risk order today blocked at this same step.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO~DELL1 (the grant or a ruling; the standing row is MDPF_HEALGAP-D1-S11)",
  "spec_asserts": "The order's C4 invocation is '.tools/aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/mdpf-49f-gold-writer-role --action-names s3:PutObject --resource-arns <three keys>', i.e. that this seat can simulate a policy source other than its own.",
  "world_is": "The call returns AccessDenied naming the caller arn:aws:iam::313476888478:user/cloudops-dell1-agent-user and action iam:SimulatePrincipalPolicy; the same action against this seat's OWN ARN returns a verdict, so the refusal is scoped to the policy source and is not the API being unreachable. C4's three arms were therefore read with org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/identity_policy_eval.py over the live role policy: own-firm gold allowed (matched only by GoldWriterPutGet), own-firm platinum implicitDeny, other firm's gold implicitDeny, with DISCRIMINATES True in both directions. DECLARED LIMIT: the substitute evaluates identity-based policies only and did not re-read the firm buckets' live DenyForeignFirmPrincipals bucket policies.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/mdpf-49f-gold-writer-role (AccessDenied, caller and action named)",
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r1_c4_arm1_arm2.out",
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r1_c4_arm3.out"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Third recurrence today after MDPF_HEALGAP C5 (row MDPF_HEALGAP-D1-S10/S11) and MDPF_STRATID.TO-APPLY-W2-a L2. Filed in this project's channel so CN-a-1's C4 evidence is traceable from the project record; the standing gap itself stays MDPF_HEALGAP-D1-S11's."
}
```

```json
{
  "id": "MDPF_CANON-D1-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-09T20:20:00Z",
  "one_line": "The gold Lambda package does not carry data/assets/scripts/silver/opal_unidentified.py, which build_cottonwood_mdpf_slice.py imports, so the COTTONWOOD scope dies with ModuleNotFoundError and GLOBAL is skipped behind it -- the first exercise of the deployed bytes (CN-a-2's qa_local read) returned 8 of 16 A4 objects where the last two scheduled fires returned 16 of 16.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (the one-line builder fix sits outside CN-a-2's permitted edit, so the issuer amends or rules; 0.7.0_AE_CloudOps~DELL1 lands it and re-deploys the same turn on that word. Copy to 2.0.0_SA_COO~S1, whose MDPF_STRATID R2 L4 grades the 2026-10-10 13:30Z fire that this hazard will make non-green.)",
  "spec_asserts": "CN-a-2's C3 expects the qa_local read to return a status and a4_objects_built with no error naming mdpf_gold_parquet, and C4 expects the backfill to return error 0. The round's premise is that the package built at 55c3cc4642 runs every scope the consolidator intends: 49financial, inflection, cottonwood, global.",
  "world_is": "The qa_local invocation at 2026-10-09T20:14:51Z returned {\"status\": \"non-green\", \"qa_local\": true, \"out_dir\": \"/tmp/qa-a4\", \"errors\": [\"cottonwood\", \"global\"], \"a4_objects_built\": 8}. Its log reads 'SCOPE FAILED (isolated): cottonwood -- ModuleNotFoundError: No module named opal_unidentified' and then 'SCOPE FAILED (isolated): global -- SystemExit: global fold SKIPPED: contributing leg(s) [cottonwood] failed this cycle', ending 'cycle complete: 8/16 A4 objects built; errors=[cottonwood, global]'. THE REGRESSION IS DATED, not inferred: a filter-log-events sweep of the same log group from 2026-10-08T00:00Z returns exactly 3 cycle-complete lines -- 2026-10-08T13:31:29Z 16/16 errors=none, 2026-10-09T13:31:40Z 16/16 errors=none, and this 20:15:26Z 8/16 -- and exactly 2 SCOPE FAILED events, both from this run. CAUSE READ IN SOURCE, BOTH PINS: build_cottonwood_mdpf_slice.py:131-136 does 'try: import opal_unidentified / except ImportError: sys.path.insert(..., \"../silver\"); import opal_unidentified', which cannot resolve in the Lambda's flat layout, and the builder's file list at 55c3cc4642 carries data/assets/scripts/silver/{rebalancer_schemas,opal_strategy_matcher}.py but NOT opal_unidentified.py. The import is present at ff1a8867a6 too, so the defect entered the DEPLOYED surface with MDPF_STRATID.TO-APPLY-R2's 18:00:35Z deploy and no scheduled fire has run since; this order's qa_local read is the first exercise of those bytes and caught it about 17 hours before R2's own L4 acceptance fire. The builder's import-closure check printed OK because it exempts nested lazy imports by design. REMEDY, measured as one line: add (\"opal_unidentified.py\", \"data/assets/scripts/silver/opal_unidentified.py\") beside the two existing silver rows at build_package.py:169-170; the module is 86 lines and imports only re plus __future__, so its own closure is satisfied.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/aws lambda invoke --function-name mdpf-gold-lambda --payload '{\"qa_local\": true}' (response captured; StatusCode 200, no FunctionError)",
      ".tools/aws logs filter-log-events --log-group-name /aws/lambda/mdpf-gold-lambda --start-time 2026-10-08T00:00Z --filter-pattern '\"cycle complete\"' (3 events) and '\"SCOPE FAILED\"' (2 events, both this run)",
      "git show ff1a8867a6:data/assets/scripts/gold/build_cottonwood_mdpf_slice.py and the same at 55c3cc4642 (import present at both, lines 132 and 136)",
      "git show 55c3cc4642:infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py (silver rows at 169-170; no opal_unidentified row)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "CN-a-2's apply legs are PROVEN and nothing is half-landed: the code and env are live and verified (CodeSha256 equal to the prediction made before the upload, env carrying the three GOLD_WRITER_ROLE_ARN_* and MDPF_GOLD_COMMIT 55c3cc4642, 0-diff re-plan). A rollback does NOT clear this hazard: the previous live package ff1a8867a6 carries the same import, so only the builder fix or a rollback past R2's deploy would, and the latter is another order's landed work. The run_class=backfill invocation (C4) is HELD rather than run, because it would write 49financial and inflection partitions while cottonwood and global failed -- a partial dated history the order's error-0 arm does not describe."
}
```

```json
{
  "id": "MDPF_CANON-D1-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-09T20:26:43Z",
  "one_line": "Four 2-row SYNTHETIC composite parquet partitions sit in the new gold home -- opal-data-mdpf mdpf/global/gold/{account_distribution,account_units,aggregate_aua_timeseries,aum_metrics}/date=2026-10-08/data.parquet, written 2026-10-09T19:10:38-39Z, before any apply or deploy, two minutes before 0.9.0_WK_MDPF_CANON~2's commit; its order forbade any AWS write.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 -- removal of the four keys is an S3 delete, which needs a human's confirmation (RESERVED card to 0.0.0_AB_MSTR~DELL1 for Andrew); until then the backfill skips them as present (plan() excludes existing partitions) and global 10-08 holds fixture rows, never the composite's figures",
  "spec_asserts": "CN-a-2's bounds: no AWS write of any kind by a worker; DEC-2: history is never rewritten, so whatever sits in a dated partition stands.",
  "world_is": "head-object: 1037 B each, application/vnd.apache.parquet, no metadata. Rows (pyarrow): aum_metrics = {period: 2026-10-08, total.aum: <num>}, account_units = {count: <num>, value_date: 2026-10-08} -- records_for's (path, value_num, value_text) shape with 2 rows each, a fixture, not the composite (whose aum_metrics carries far more figures). Firm buckets carry only TAXSMA's 9+9 objects; inflection 0.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/aws s3api list-objects-v2 --bucket opal-data-mdpf --prefix mdpf/global/gold/ (6 keys: the 4 above + 2 ai_classified_securities index.json)",
      "pyarrow read of two of the four (scratch copies), 2 rows each",
      "git -C C:/Dev/wt-canon-w2 log: 4fc14f14cd 15:12:22-04:00 (19:12Z)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the issuer at the round-1 real run; CloudOps told the backfill will plan 0 for global 10-08 on these four."
}
```

```json
{
  "id": "MDPF_CANON-D1-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-09T20:41:00Z",
  "one_line": "With opal_unidentified packaged (F2), the cottonwood scope now BUILDS and emits a new field unidentified_strategies, and the L-1 key-set identity assertion raises SystemExit on it -- the run dies BEFORE the A4 emission loop, so the next scheduled fire would emit NOTHING on all four scopes rather than the 8 of 16 the broken package emitted.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~S1 (the field is MDPF_STRATID's ST-w-7 and the remedy is its contract's to write: either an R2_RULED_EXTRAS entry for aggregate-aua-timeseries carrying unidentified_strategies with its citation, or emit the field on all four scopes). 0.7.0_AE_CloudOps~DELL1 can disarm in minutes the other way on either issuer's word -- roll mdpf-gold-lambda back to the last GREEN package, CodeSha256 0gPc5/kUo+sE8BnvhKg5wO+IXiDCB4vRK5cvy1ac+2I= at artifact VersionId .lLLFYib9VWTgbndCYqKes9qWk47YoYK (metadata content-sha256 d203dce7f914a3eb), which is the pre-R2 build that read 16 of 16 errors=none on 2026-10-08 and 2026-10-09.",
  "spec_asserts": "MDPF_STRATID.TO-APPLY-R2's forward fix F2 (2.0.0_SA_COO~S1 msgs 3132/3144) states the acceptance read as 'qa_local reading 16/16, errors []'. CN-a-2's C3 expects a response carrying status and a4_objects_built. Both presume that packaging opal_unidentified.py makes the cycle whole.",
  "world_is": "It makes the cottonwood scope WHOLE and the cycle WORSE. F2 landed (package 44 modules / 45 members, opal_unidentified.py a member at 6b9c1d7f, live CodeSha256 06aIPiKcSoENnMEpf512CPhkvSI+iUnB0Re1B6fyfgk= equal to the prediction made before the upload, MDPF_GOLD_COMMIT 79e30151a6, 0-diff re-plan). The 20:37:11Z qa_local invocation then returned StatusCode 200 with FunctionError Unhandled and body {\"errorType\":\"Runtime.ExitError\",\"errorMessage\":\"... Runtime exited with error: exit status 1\"}. The log shows cottonwood building correctly for the first time -- 'COTTONWOOD MDPF PAIR', 'IDENTITIES PASS: (i) decomposed==dim to the penny, (ii) model+non_model==firm, (iii) bridge complete', 'global composition gate PASS', category-views built on all four scopes -- and then the last line before END: 'L-1 KEY-SET IDENTITY FAILED for aggregate-aua-timeseries -- a field on one scope and absent on a sibling is a FAILURE, not a warning: cottonwood: only-here=[unidentified_strategies] missing=[] (vs 49financial)'. SEVERITY READ FROM THE SOURCE, not guessed: mdpf_gold_consolidator.py:2827 calls assert_keyset_identity BEFORE the '---- A4 emission ----' loop at :2839, and :1080 raises SystemExit, so a real run reaches no put at all. The broken package at least emitted 8 of 16; these bytes would emit 0 of 16 and leave every served A4 artifact a day stale. The assertion was DEFERRED on the pre-F2 run ('not all scopes built this cycle') precisely because cottonwood had died first -- the import gap was MASKING this one. ZERO WRITES from this run, measured as a set difference over the 16 gold prefixes: 0 keys added, 16 of 16 prefixes read, 0 UNREADABLE. THE SANCTIONED SHAPE FOR THE REMEDY ALREADY EXISTS: R2_RULED_EXTRAS at :289 enumerates exactly this case (today one entry, inflection_non_model_aua, carrying 'CONTRACT section B3 @a3106d585: ruled NOT canonical ... serves until Andrew rules retirement'), so a ruled extra is a one-entry change with a citation -- and the citation is the issuer's to write, not this seat's to invent.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/aws lambda invoke --function-name mdpf-gold-lambda --payload '{\"qa_local\": true}' at 20:37:11Z (FunctionError Unhandled, Runtime.ExitError)",
      ".tools/aws logs filter-log-events --log-group-name /aws/lambda/mdpf-gold-lambda (326 events; the L-1 line is the last before END)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py:289 R2_RULED_EXTRAS, :1065-1083 assert_keyset_identity, :2827 the call, :2839 the A4 emission loop",
      "the 16-prefix gold census before and after the invocation (0 keys added, denominators printed)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "This row does NOT retract MDPF_CANON-D1-S3: packaging opal_unidentified.py was correct and is what let cottonwood build. It records that the fix uncovered the next defect in the same chain, which is the honest order of discovery. Both ledger entries (mdpf-canon-r1-gold-redeploy-backfill-dell1-20261009 and mdpf-opal-unidentified-forward-fix-dell1-20261009) carry their apply legs CLOSED with proof and nothing half-landed: the artifact and env are live and verified both times. CN-a-2's C4 backfill stays HELD -- a backfill cannot run at all through an assertion that precedes every put. ID COLLISION AVOIDED: this row was first written as D1-S4 and renumbered to D1-S5 after a mid-write census found 2.0.0_SA_COO~D1 had committed its own D1-S4 @4e66c34616 (the four synthetic composite partitions) seconds earlier -- a different finding, not this one. The census printed the denominator (6 blocks in the worktree against 5 at HEAD), which is how the clash was seen."
}
```

```json
{
  "id": "MDPF_CANON-D1-S6",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-09T20:48:00Z",
  "one_line": "C4's backfill is refused at the COMPOSITE leg: CN-a-1 gave mdpf-gold-lambda-role Put/Get on opal-data-mdpf's four gold prefixes but no s3:ListBucket on the bucket, and run_backfill lists each scope's existing partitions before it plans -- the three FIRM legs listed fine through their assumed gold-writer roles, so this is one missing statement, not a broken design.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (the statement belongs to CN-a-1's cell source, infra/aws/terraform/mdpf-pipeline/iam.tf aws_iam_role_policy.mdpf_gold_writers, which neither ADHOC order permits this seat to edit; one amendment and 0.7.0_AE_CloudOps~DELL1 applies it and re-runs C4 the same turn)",
  "spec_asserts": "CN-a-3 / C4: invoke {\"run_class\": \"backfill\"} and expect status backfill, planned > 0, tally with written > 0, conflict 0, error 0. CN-a-1's C5 declares the gold Lambda's composite grant complete as Put/Get on arn:aws:s3:::opal-data-mdpf/mdpf/global/gold/{the four}/*.",
  "world_is": "The 20:46:03Z invocation returned StatusCode 200 with FunctionError Unhandled and errorType AccessDenied: 'User: arn:aws:sts::313476888478:assumed-role/mdpf-gold-lambda-role/mdpf-gold-lambda is not authorized to perform: s3:ListBucket on resource: \"arn:aws:s3:::opal-data-mdpf\" because no identity-based policy allows the s3:ListBucket action', with the stack naming mdpf_gold_consolidator.py:2996 run_backfill and :2970 the list_objects_v2 paginator. THE LIVE POLICY CONFIRMS IT, re-read rather than inferred from the error: mdpf-gold-writer-assume-policy carries exactly 2 statements -- GoldWriterAssumeScopedRoles (sts:AssumeRole on the three role ARNs) and GoldCompositePutGet (s3:PutObject + s3:GetObject on the four mdpf/global/gold/<artifact>/* prefixes) -- and no ListBucket of any kind. WHAT THE FAILURE ALSO PROVES, and it is the first live exercise of CN-a-1's grant: SCOPES is ('49financial', 'inflection', 'cottonwood', 'global') with global LAST, so all three FIRM legs completed before this line -- each assumed its own mdpf-{firm}-gold-writer-role through sts:AssumeRole and ran a prefix-scoped ListBucket successfully. CN-a-1's forward note said that end-to-end exercise was still owed; this run delivers three quarters of it. SCOPE OF THE REMEDY, read from the source rather than guessed at one AccessDenied per round trip: run_backfill touches exactly four S3 surfaces -- (1) the Lambda's own role lists opal-data-assets at the A4 prefix (SUCCEEDED, it is step one), (2) client(scope) lists each scope's series directory (firm legs via the assumed roles, SUCCEEDED; global via the function's own credentials, REFUSED here), (3) the Lambda's own role get_objects the legacy source keys from opal-data-assets (the daily path already does this), and (4) write_partition puts into each scope's bucket. So ONE statement closes it: s3:ListBucket on arn:aws:s3:::opal-data-mdpf, conditioned StringLike s3:prefix on the same four mdpf/global/gold/<artifact>/ prefixes, mirroring the per-firm GoldWriterListScoped rather than widening the bucket. NOTHING WAS WRITTEN: the refusal lands at the listing, before plan(), and a 16-prefix census before and after reads 0 keys added, 16 of 16 prefixes read, 0 UNREADABLE. UNVERIFIED AND NOT CLAIMED: whether the DAILY (non-backfill) parquet path also needs the same ListBucket -- its writer printed NOT_RUN_DRY_RUN on both qa_local runs, so it has never been exercised against the live bucket.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/aws lambda invoke --function-name mdpf-gold-lambda --payload '{\"run_class\": \"backfill\"}' at 20:46:03Z (AccessDenied, caller and action named, stack included)",
      ".tools/aws iam get-role-policy --role-name mdpf-gold-lambda-role --policy-name mdpf-gold-writer-assume-policy (2 statements, no ListBucket)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py:119 SCOPES, :2949-2988 run_backfill; mdpf_gold_parquet.py:75-91 client_for_scope",
      "the 16-prefix gold census before and after the refused invocation (0 keys added, denominators printed)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Independent of row D1-S5: this one blocks the BACKFILL path, which 2.0.0_SA_COO~D1 ruled (msg 3153) does not reach the L-1 assertion -- and that ruling is correct, verified in source at lambda_handler:2995-2996 returning run_backfill() before any build. Both rows must clear before the round's thread is whole. Nothing is half-landed in either ledger."
}
```

```json
{
  "id": "MDPF_CANON-D1-S7",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-09T21:32:14Z",
  "one_line": "DISARMS rows D1-S3, D1-S4, D1-S5 and D1-S6 (the disarm owner's read of the live plane after ADHOC.canon-r1-gold-redeploy-backfill closed @1785cdcddf).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D1",
  "spec_asserts": "Each ARMED row disarms through its owner with the evidence named.",
  "world_is": "S3 (package omits opal_unidentified.py): fixed by MDPF_STRATID F2 @79e30151a6, live; C1 manifest carries it. S5 (L-1 key-set on unidentified_strategies): fixed by MDPF_STRATID ST-w-8 @88e974ca10; C3 qa_local re-read green, errors [], 16 of 16, L-1 PASS on all four types, zero writes. S6 (composite ListBucket): AMENDMENT 4 applied; C4 completed. S4 (4 synthetic composite 10-08 partitions): deleted on Andrew's word by the laptop 1.0.0_SA_CTO (record ANDREW_DIRECT_20261009_210xZ_DELETE_SYNTHETIC_TEST_DATA_MDPF_GLOBAL_20261008.md @991c4cae64; call dell1-20261009T202914Z-113f CLOSED); the backfill then wrote the real global 10-08 for the three artifacts with a source. Final read: 540 partitions, 16 of 16 series equal to their legacy dated counts, 0 mismatches.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/ADHOC.canon-r1-gold-redeploy-backfill_PROOF_OF_SPEC.json @1785cdcddf",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_210xZ_DELETE_SYNTHETIC_TEST_DATA_MDPF_GLOBAL_20261008.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Resolves MDPF_CANON-D1-S3, MDPF_CANON-D1-S4, MDPF_CANON-D1-S5, MDPF_CANON-D1-S6. Filed at the round-1 close; the four rows' hazards are spent."
}
```
