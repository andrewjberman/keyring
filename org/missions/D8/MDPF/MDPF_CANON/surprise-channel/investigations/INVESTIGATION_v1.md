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

```json
{
  "id": "MDPF_CANON-D1-W5-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~5",
  "surfaced_at": "2026-10-09T21:57:30Z",
  "one_line": "BLOCKING: CN-b-2's required output path deliverables/X2_GLOBAL_BASIS.md is outside the order's <paths> grant; the lane gate refuses it (ADHC_OWNPTH.004/005).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "The order tells the worker to write org/missions/D8/MDPF/MDPF_CANON/deliverables/X2_GLOBAL_BASIS.md, and check r2_checks.py basis reads exactly that path.",
  "world_is": "The order's <paths> grants only deliverables/0.9.0_WK_MDPF_CANON~5/, the ledger and the investigation file. safe-commit refused a commit of deliverables/X2_GLOBAL_BASIS.md: lane TREE_DELIVERABLES permits only the serial-named sub-folder. The file and the ledger X2 citation are written and r2_checks.py basis reads 3 of 3 in the worktree, but not committed; the order was not flipped complete and no proof instance was committed. A copy of the basis sits at deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md. The issuer lands the top-level file (or amends <paths>) and the ledger edit.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit refusal text, ADHC_OWNPTH.005, 2026-10-09T21:56Z on wk-MDPF_CANON-5",
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-b-2.md section 3 <paths>"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W7-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~7",
  "surfaced_at": "2026-10-09T21:54:34Z",
  "one_line": "CN-b-4 AC1 is unsatisfiable by any valid Terraform: r2_checks.py extracts ARNs with a no-quote regex but demands scope_bucket[\"key\"] inside the ARN string.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "A composite ARN written as \"arn:aws:s3:::${module.<m>.scope_bucket[\"mdpf\"]}/...\" passes r2_checks.py builder (3 of 3) and leaves r1_iam.py at 6 of 6.",
  "world_is": "r2_checks.py:256 extracts ARNs with re.findall(r'\"(arn:aws:s3:::[^\"]*)\"', body); the double quotes inside scope_bucket[\"mdpf\"] end the capture at 'scope_bucket[', so r2 builder reads 1 of 3 (BUILDER and EQUALS fail on a truncated string) and r1_iam.py GLOBAL, which passed at base, now reads no Put on the composite prefixes (5 of 6). Line 272 then requires the double-quoted key. Terraform has no escape for a quote inside an interpolation, and single quotes do not match line 272. The edit itself is correct and the effect unchanged (module mdpf_scope_buckets, scope_bucket[\"mdpf\"] = opal-data-mdpf in generated_locals.tf, which is the builder's PRODUCT-scope bucket mapping, so no registry row). Worker did not edit the check; edit left uncommitted in the worktree.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py:256,272",
      "infra/aws/terraform/modules/opal_name/generated_locals.tf:65-79 @01d8169f27"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W4-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~4",
  "surfaced_at": "2026-10-09T22:51:00Z",
  "one_line": "CN-b-1 census cannot see the portal front-end: portal/ is an empty directory in this worktree, so any browser-side reader of json/portfolios/aum-timeseries.json is unseen.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The task order asks for an UNSCOPED census over the whole corpus including the portal source (readers of the stale served key).",
  "world_is": "portal/ holds 0 entries and git ls-files portal returns nothing in wk-MDPF_CANON-4; Grep over portal/ and mcportal/ returned 0 hits. The census row for the front-end is excluded-with-reason (absence not established) and INSTRUMENT clause (c) says so. Retiring the stale served key needs a portal-repo read the cell could not do.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md INSTRUMENT line (c)",
      "git ls-files portal on wk-MDPF_CANON-4 returned 0 lines, 2026-10-09T22:50Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S8",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-09T23:05:00Z",
  "one_line": "The front-end readers row W4-S1 could not see are seen from the main tree's portal pin: portal's readers of json/portfolios/aum-timeseries.json exist only in api/ and no page calls them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-b-1's census names every reader of the stale served key, the portal front-end included (row MDPF_CANON-D1-W4-S1 left it unseen).",
  "world_is": "At portal pin c96efe17 (main tree), 3 files under portal/src name getAUMTimeSeries or getModelTimeSeries: api/portal-proxy.ts:338-346 (fetches /api/general/portfolios/aum-timeseries.json), api/endpoints/aum.ts:322-328 and :447-449 (wrap it), and pages/ModelPortfolios.tsx:418 (a comment only; :569 records the page's legacy fetch DELETED). No file outside src/api calls either reader. The key has defined readers but no live page caller at this pin; retiring it removes dead code in portal/src/api as a portal-repo act.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/api/portal-proxy.ts:338-346 @c96efe17",
      "portal/src/api/endpoints/aum.ts:328,449 @c96efe17",
      "grep -rln getModelTimeSeries|getAUMTimeSeries portal/src -> 3 files; outside src/api only ModelPortfolios.tsx:418 (comment)"
    ]
  },
  "notes": "Answers row MDPF_CANON-D1-W4-S1 (the unseen front-end limb): seen, no live page caller. The retirement act lands with the publisher switch (PRD M5), not in round 2.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S9",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-11T02:30:00Z",
  "one_line": "BLOCKING: the first scheduled daily write (2026-10-10 13:30Z) built 12 of 16 A4 objects -- global refused by the producer's cross-axis gate, 49financial and two inflection types held by the legacy CONFLICT guard -- so FWD-1 is not REALIZED and CN-a-2 AC3 cannot grade.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "ROUND2_CLOSE carried item 1 and the round-1 analysis section 3: the 2026-10-10 13:30Z fire writes the four types x four scopes at their address() paths, prior partitions unchanged, global byte-identical to its legacy figures, and the first account_units partitions exist for 49financial, inflection and global.",
  "world_is": "r2_daily.py read --fire 2026-10-10T13:30:00Z: 1 of 4 arms. WRITTEN 4 of 12 series (inflection/account_distribution 2026-10-10; cottonwood x3 2026-10-09). UNCHANGED PASS 540 of 540. PARITY 5 of 5 equal, global compared 0. UNITS 2 of 3, global missing. The Lambda's log (RequestId 996aca3d, one invocation, 13:30:37Z-13:31:37Z) ends 'cycle complete: 12/16 A4 objects built; errors=[global]'. Global: 'CROSS-AXIS COHERENCE GATE FAILED (global) -- REFUSING TO EMIT', check (v), 5 models on 2026-10-09 with model_value=None against account_count present; the value leg's own line reads 'aum_daily ... day 2021-09-02..2026-10-08', one trading day behind the count leg's axis_last 2026-10-09. 49financial and inflection: six 'CONFLICT (recorded, not overwritten)' lines on existing legacy dated JSON; that set equals the arm-1 missing set outside global (set equality; the mechanism is INFERRED, not read from code). The fire fell on Saturday 2026-10-10, T-1 frontier Friday 2026-10-09.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/DAILY_READ_20261010T1330Z.md",
      "r2_daily.py read --fire 2026-10-10T13:30:00Z, exit 1, run 2026-10-11T02:2xZ against snapshot @9f652c3086",
      "aws logs filter-log-events /aws/lambda/mdpf-gold-lambda 2026-10-10T13:20Z-14:30Z, 329 lines; lines 289-303 (global gate), 316-326 (R1 INCOMPLETE, CONFLICT, PARTIAL, cycle complete)"
    ]
  },
  "notes": "Not a defect shown in CN-a-2's writer: where a scope was built its parquet matches the legacy values (arm 3, 5 of 5). The shortfall sits at the producer's input gate and conflict guard. One fire is one sample; the next fires (2026-10-11 13:30Z if the schedule runs weekends, and the 2026-10-12 trading-day fire) are the negative/positive arms. Also on the log, ungraded: A7 reconciliation ERROR on mdpf_aggregate_aua, ROW11 frontier-stamp STALE on 49financial and inflection. Routing: the CVO's L9 grades CN-a-2 AC3 on this read; whether the guard or the value-feed lag is a project cell is the CTO's call at the round-2 analysis.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S10",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-11T02:55:00Z",
  "one_line": "The value leg (smartx fact_model_aum_daily) lands one trading day behind the T-1 frontier on every Saturday and Sunday run, so a weekend gold fire cannot read both legs at the frontier; Friday's value first lands in Monday's partition.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Round-2 analysis @71e85b7191 section 2 and section 3 item 1: on the 2026-10-09 fire both legs agreed; whether the value feed delivers Friday's data only on the next trading day (a weekend clock mismatch that recurs every Saturday fire) or missed once is not measured.",
  "world_is": "s3://opal-data-assets/smartx/platform/silver/fact_model_aum_daily/ holds 89 objects, one partition per calendar day written about 13:25Z. The run_date R partition ends its `day` axis at: Sat 09-19 and Sun 09-20 -> Thu 09-17; Mon 09-21 -> Fri 09-18; Sat 09-26 and Sun 09-27 -> Thu 09-24; Mon 09-28 -> Fri 09-25; Sat 10-03 and Sun 10-04 -> Thu 10-01; Mon 10-05 -> Fri 10-02; Tue-Fri 10-06..10-09 -> the prior trading day; Sat 10-10 -> Thu 10-08. 7 of 7 weekend partitions in four weekends end at Thursday; every Monday ends at Friday. Friday 2026-10-09's value rows have not landed as of 2026-10-11T02:5xZ. The count leg reaches Friday on the same weekend day, so global's cross-axis gate (v) refuses on the Saturday fire. The producer's gate is correct and is not loosened. Mechanism (SmartX publishes on business-day mornings) is INFERRED; bronze landing times were not read; the owner of the SmartX feed and the silver Lambda was not read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round3/VALUE_LEG_CLOCK_20261011.md",
      "infra/aws/lambda/opal-assets/opal-assets-daily-emitter/channel_sources.py:58 (SMARTX_AUM prefix)",
      "boto3 list_objects_v2 + parquet read of `day`, 2026-10-11T02:5xZ, denominator 89 objects, 18 run_dates read (09-19..09-21, 09-26..10-10)"
    ]
  },
  "notes": "Falsifiers: the Sunday 2026-10-11 13:30Z fire should refuse global again; the Monday 2026-10-12 13:30Z fire should read both legs at Friday 2026-10-09. A refusal on Monday with both legs at Friday would put the defect in the producer. Per the round-2 analysis item 1, a structurally late value leg is filed against the value feed's owner; the issuer cuts no cell for it. Whether weekend fires are expected to be current is a spec question for the CTO: FWD-1's 16 of 16 read is a trading-day-fire read.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W8-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~8",
  "surfaced_at": "2026-10-11T03:09:41Z",
  "one_line": "CN-c-1 states 12 global by_model entries are held at one firm (6 at three or fewer accounts); the stated rule gives 10 in aggregate-aua-timeseries. The six-at-three-or-fewer count reproduces; the 12 does not.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO MDPF_CANON.TO-CN-c-1 section 1 (path@335258e392): the global figure has 12 by_model entries held at ONE firm, 6 of them at three or fewer accounts, each value equal to that firm's.",
  "world_is": "Read-only get, 2026-10-08, opal-data-assets, four scopes, three objects each. aggregate-aua-timeseries: 10 global by_model entries held by exactly one firm under key match (6 at three or fewer accounts; 10 of 10 value-equal to that firm's); 11 if cottonwood key divz (display Dividend SMA, absent from data/mdpf/scripts/gold/mdpf_model_registry.json) is matched by display name alone; 2 null entries and 2 zero-firm entries (see row S2). account-distribution: 9 of 14 single-firm (2 total_aum equal). aum-metrics: 2 of 7 single-firm (2 equal). Union of single-firm names across the three objects: 10. Denominator: 41 global by_model entries read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api get-object, bucket opal-data-assets, portal/gold/mdpf/{global,49financial,inflection,cottonwood}/{aum-metrics,account-distribution,aggregate-aua-timeseries}/2026-10-08.json (read-only, 12 objects)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md (Single-firm entries and Method sections)",
      "data/mdpf/scripts/gold/mdpf_model_registry.json@335258e392 (divz absent; _changelog v4 renames)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The basis states the count this method yields and does not correct the cell text; the 12 is the issuer's figure and its reconciliation is for the issuer and the CTO."
}
```

```json
{
  "id": "MDPF_CANON-D1-W8-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~8",
  "surfaced_at": "2026-10-11T03:09:41Z",
  "one_line": "Two global by_model entries (opal_growth_sma 45 accounts, opal_div_sma 40 accounts) carry a non-null figure and nonzero account counts at 2026-10-08 while no firm scope holds either entry on that date.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to the owner of the global fold, dim_mdpf_aggregate_aua_timeseries.py)",
  "spec_asserts": "The round-2 basis premise, carried into CN-c-1: every combined (global) figure sums at least 2 firms.",
  "world_is": "aggregate-aua-timeseries global by_model at 2026-10-08: opal_growth_sma and opal_div_sma are non-null with nonzero account_count. 49financial account_count is null for both at 2026-10-08; its last nonzero date for both is 2026-07-17. inflection has no growth key; cottonwood has no growth key and its divz is unmatched. Measured: the global account_count at 2026-10-08 equals its 2026-07-17 value, and both equal the 49financial 2026-07-17 value; the global model_value at 2026-10-08 is not equal to its 2026-07-17 value. Min firms at the as-of for these entries is 0. The mechanism that carries them was not read beyond the global meta by_model_channels and cottonwood_carry keys.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api get-object, opal-data-assets, portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-08.json and portal/gold/mdpf/49financial/aggregate-aua-timeseries/2026-10-08.json (read-only)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md (Method: zero-firm entries)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Hazard ARMED: the fold re-emits these carried entries on each run. The basis states them as emitted; it does not argue they are safe."
}
```

```json
{
  "id": "MDPF_CANON-D1-W8-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~8",
  "surfaced_at": "2026-10-11T03:09:41Z",
  "one_line": "Served global opal_aggregate_aua at 2026-10-08 is not equal to global model_aua plus non_model_aua (tolerance 0.011); the identity the fold states at dim_mdpf_aggregate_aua_timeseries.py:2257 holds on 460 of 484 non-null dates.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to the owner of the global fold, dim_mdpf_aggregate_aua_timeseries.py)",
  "spec_asserts": "dim_mdpf_aggregate_aua_timeseries.py:2257 (docstring): opal_aggregate_aua[i] == model_aua[i] + non_model_aua[i] at every date; the build-time assertion _assert_global_composition (:1858) states the same identity.",
  "world_is": "Served global aggregate-aua-timeseries at 2026-10-08: the identity does not hold at the as-of; it holds on 460 of the 484 non-null dates of the global axis (9 of 493 dates are null). Measured as holding: global model_aua equals the sum of the three firms' model_aua; global non_model_aua equals 49financial's. The size of the gap is not characterised here. The step that produces the served opal_aggregate_aua after the build assertion was not read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api get-object, opal-data-assets, portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-08.json (read-only; identity checked over the full date axis)",
      "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py@335258e392:2257 and :1858"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The headline family's min firms is 3 by the fold's leg rule (:2424-2425) and all four legs being non-null at the as-of; this row does not depend on the identity holding."
}
```

```json
{
  "id": "MDPF_CANON-D1-W8-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~8",
  "surfaced_at": "2026-10-11T03:09:41Z",
  "one_line": "The cell's expectation that each single-firm global value equals that firm's value holds for 2 of 9 single-firm entries in the account-distribution object; the other 7 do not match their one firm's total_aum.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-1 section 1 and AC3 (path@335258e392): each global entry held at one firm has a value equal to that firm's value at the as-of.",
  "world_is": "account-distribution 2026-10-08: global entries held at one firm are 9; value equal (total_aum, relative tolerance 1e-6) for 2 (inflection 50/50 blends). The 7 cottonwood-held entries are not equal. The cottonwood object's generated_at is 2026-10-09T13:31Z; the global and inflection objects are 2026-10-08T13:31Z, so build time may account for the difference. Not characterised. In aggregate-aua-timeseries and aum-metrics the same comparison holds for every single-firm entry.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api get-object, opal-data-assets, portal/gold/mdpf/{global,cottonwood,inflection}/account-distribution/2026-10-08.json (read-only; generated_at read)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md (Single-firm entries)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed because the cell's value-equality expectation does not hold on this object; the basis reports the measured booleans."
}
```

```json
{
  "id": "MDPF_CANON-D1-W8-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~8",
  "surfaced_at": "2026-10-11T03:10:37Z",
  "one_line": "CN-c-1 says moving X2 from OWED to GRANTED is Andrew's act, but infra/logic/06_CONFORMANCE_LEDGER.md already reads X2 GRANTED (Andrew-direct 2026-09-15) on the round-2 basis that the CTO's 2026-10-08 read contradicts.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "Andrew (decider of X2 per ledger row line 136); routed by 2.0.0_SA_COO~D1",
  "spec_asserts": "TO CN-c-1 section 1 (path@335258e392): the X2 row cites the new basis; its status is not changed, since moving X2 from OWED to GRANTED is Andrew's acknowledgement.",
  "world_is": "infra/logic/06_CONFORMANCE_LEDGER.md@335258e392 line 136: X2 status **GRANTED**, decider Andrew, decided 2026-09-15, PERMANENT; line 116 and line 226 carry the same GRANTED state. The OWED premise in the cell does not match the row. The grant's stated basis (aggregate counts only, every global figure sums at least 2 firms, per the round-2 basis) is contradicted in part by the served output (rows MDPF_CANON-D1-W8-S1 to S4). The status is left unchanged, as the cell directs.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/06_CONFORMANCE_LEDGER.md@335258e392:136 (X2 row, GRANTED)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md (round-2 basis, read-only)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md (round-3 basis, Method)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed as a premise failure: the cell's OWED premise does not match the ledger. Whether the GRANTED state should be re-read against the new basis is Andrew's act; this cell does not change it."
}
```

```json
{
  "id": "MDPF_CANON-D1-S11",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-11T03:33:24Z",
  "one_line": "Three of the five check_en_r2.py r6 subcommands read FAIL at box/dell1 HEAD before any MDPF_CANON change: r6-headers-current, r6-undeclared-inert and r6-reproduces.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CTO ruling msg 3431: the new generate target is proven with opal_naming's own tests plus check_en_r2.py r6 arms.",
  "world_is": "Run from the repo root at box/dell1 2026-10-11 ~03:3xZ with `python -I <check_en_r2.py> <sub>`: r6-declared-moves -> PASS-DECLARED-MOVES (18 pairs probed, 0 not moved); r6-delta0-ordered -> PASS-DELTA0-IN-ORDER (bucket_for branches taken: mapped True, unmapped True); r6-headers-current -> FAIL-HEADER-STALE (10 generated files; the marks of data/firm_registry.json, firm-config.mjs and directory_runner.py do not hash their listed scopes.json at HEAD); r6-undeclared-inert -> FAIL-UNDECLARED-FILE-MOVES-A-VIEW (10 views probed; data/firm_registry.json moved when event_rules.json was changed, a file its mark does not list); r6-reproduces -> FAIL-GENERATE-DIFFERS (13 written; at least one generated file at HEAD differs from regeneration). lib/tests/test_opal_naming.py reads 96 passed. The checker is an issuer fixed input of 2.0.0_SA_COO~G dated at LGIC_ENFORCE round 2; whether the three FAILs are checker staleness or registry drift at HEAD was not established here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r6-headers-current / r6-undeclared-inert / r6-reproduces, run at box/dell1 HEAD",
      "python -m pytest lib/tests/test_opal_naming.py -q -> 96 passed"
    ]
  },
  "notes": "MDPF_CANON CN-c-2 asks only for the two arms that read PASS at the base (r6-declared-moves, r6-delta0-ordered) plus opal_naming's own tests; the other three are not this project's to fix. Routed to the generator's owner (1.0.0_SA_CTO through LGIC_ENFORCE) as a row, not a message.",
  "disposition": "UNDER_INVESTIGATION"
}
```
```json
{
  "id": "MDPF_CANON-D1-W9-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T03:04:50Z",
  "one_line": "CN-c-2 step 2 premise fails: the daily runner does not put lib/opal_naming.py on the Stage-0 pull's import path, so the builder import the cell requires cannot resolve there. Cell stopped at step 2; no file edited, no AWS call.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-2 step 2: the Stage-0 script imports from lib.opal_naming (as the sibling gold writer does). If lib/opal_naming.py is NOT on the runner's path for a Stage-0 script, file a BLOCKING row stating what the runner syncs, and stop on this cell.",
  "world_is": "The runner syncs two trees only: s3://opal-data-mdpf/code/scripts/ to /opt/mdpf/scripts/ and s3://opal-data-mdpf/code/config/ to /opt/mdpf/config/ (dispatch :125, :130). The repo-root lib/ tree is in neither. Stage 0 runs as \"$PY\" \"$S0_SCRIPT\" --date \"$RUN_DATE\" --upload with S0_SCRIPT=/opt/mdpf/scripts/bronze/pull_orion_model_composition.py (dispatch :248, :251) and no PYTHONPATH is exported anywhere in the dispatch or the user-data bootstrap (pip installs only). sys.path[0] is therefore /opt/mdpf/scripts/bronze, and the script has no sys.path insert (its imports end at :49). lib is not a child of that directory, so the import raises ModuleNotFoundError on the runner. The Stage-0 failure is non-fatal to the chain (dispatch :251-262 WARN, chain continues). The sibling gold writer (mdpf_gold_parquet.py:52) resolves its repo-root insert four levels above /opt/mdpf/scripts/gold, which is /, so it has the same gap on the runner (not graded by this cell).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh@2280b72ff4:125,130 (s3 sync of code/scripts and code/config only)",
      "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh@2280b72ff4:248,251 (S0_SCRIPT and its invocation, no PYTHONPATH)",
      "data/mdpf/scripts/bronze/pull_orion_model_composition.py@2280b72ff4:37-49 (imports; no sys.path insert)",
      "infra/aws/ec2/mdpf-daily-runner/user-data.sh@2280b72ff4 (bootstrap: pip installs only, no lib sync)",
      "data/mdpf/scripts/gold/mdpf_gold_parquet.py@2280b72ff4:52 (sibling lib import)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The stop is at step 2 of CN-c-2. Steps 1 and 3 (the script and the IAM grant) were not edited. The fix is a runner-side decision (what the dispatch syncs or exports, and CloudOps' deploy), not a worker's path choice, so the cell does not type the prefix. AC1 at base: 0 of 3 arms, exit=1."
}
```

```json
{
  "id": "MDPF_CANON-D1-W9-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T03:17:13Z",
  "one_line": "CN-c-2 section 1.3 GRANT cannot take its bronze bucket from an opal_name module output: the module exposes scope_bucket per scope and no tier-bucket output, and no scopes.json row maps to opal-data-assets. The grant is not written; the script and the generated homes file are.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-2 section 1.3: the runner role's grant on the builder's bronze bucket and prefix takes its bucket from an opal_name module output (module.<m>.scope_bucket[...] or the module's tier-bucket output), never a typed name. If the module cannot express the bronze tier's bucket, add the registry row and regenerate generated_locals.tf; if that needs a ruling, file a row and stop on the criterion.",
  "world_is": "The FIRM bronze tier home is opal-data-assets (infra/logic/registry/tiers.json FIRM.bronze, home shared, rule R4). The opal_name module's outputs are name, scope_short, scope_long, scope_class, scope_bucket, fence_patterns, account_id, fence_exemption_arns and fence_scoped_statements (infra/aws/terraform/modules/opal_name/main.tf); scope_bucket is per scope and gives opal-data-inflection for inflection and opal-data-mdpf for mdpf, never opal-data-assets. No scopes.json row carries bucket opal-data-assets (the ten buckets listed are all firm, product or master buckets). The registry row the cell names would add a scope or re-home a firm row, a change to the closed scope enumeration; the worker judges that a ruling is needed and does not add it. The iam.tf statements are not written. Consequence to carry to the drain: the Stage-0 script now writes the new home only, so until the grant lands its puts are AccessDenied, and the feeder (CN-c-3) reads the new home only after its own cell lands.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/tiers.json@e4a8f39862 (FIRM.bronze shared opal-data-assets)",
      "infra/aws/terraform/modules/opal_name/main.tf@e4a8f39862 (output blocks: no tier bucket)",
      "infra/logic/registry/scopes.json@e4a8f39862 (bucket values; no opal-data-assets row)",
      "infra/aws/terraform/modules/opal_name/generated_locals.tf@e4a8f39862 (scope_bucket map: inflection -> opal-data-inflection, mdpf -> opal-data-mdpf)",
      "python lib/opal_naming.py address() on mdpf/inflection/bronze/orion_model_composition/date={date} -> s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date={date}"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker at step 3 (GRANT). Writer check at this commit: 2 of 3 arms (NO TYPED PASS, DEST PASS, GRANT FAIL). Steps 1 and 2 (generator, generated bronze_homes.json, repo test, script) are written and green; the homes check reads 3 of 3. Not deployed. The grant decision (a registry row and regenerate, or a module output for the tier bucket) is the CTO's ruling; the order stays open."
}
```

```json
{
  "id": "MDPF_CANON-D1-W9-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T03:19:13Z",
  "one_line": "The commit-time naming limb REFUSES the cell's generated home and its generator: the key_prefix literal in data/mdpf/config/bronze_homes.json (a NEW hand-kept carrier of 'inflection') and the 'mdpf' literal in .tools/gen_mdpf_bronze_homes.py:23 (a hand-kept carrier of 'mdpf'). The cell's code is not committed.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-2 section 1.1 and bounds 3: the JSON's literals are the commit-time naming gate's to grade; if that gate REFUSES them, file a BLOCKING row with the gate's text and stop, never a workaround.",
  "world_is": "safe-commit (naming limb, LGIC_ENFORCE DEC-6, ENFORCE mode) on the four paths of the code commit: REFUSE 3 graded. Printed refusals: '.tools/gen_mdpf_bronze_homes.py:23 mdpf -> lookup(mdpf): NEW hand-kept carrier (context rule); hand-kept carrier of mdpf outside every permitted context: read it through lookup(mdpf)'; 'data/mdpf/config/bronze_homes.json:10 mdpf/inflection/bronze/orion_model_composition -> same: CONFORMANT as S3Key, but a NEW hand-kept carrier of inflection outside every permitted context: read it through lookup(inflection)'. The bucket line (json:9, opal-data-assets) printed CONFORMANT as S3_BUCKET. The commit aborted and unstaged the files; no commit landed. The script and the repo test were not named in the refusal. The generator's output is a registry-derived JSON carrier, which the naming gate does not recognise as generated (lib/opal_naming.py's generated carriers carry a generated mark, and this file is written by .tools/, not by lib generate). Resolution is a CTO decision: a permitted generated context for the homes file, or a lib generate target for it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output, 2026-10-11T03:18Z, worktree C:/Dev/wk-canon-9 branch wk-MDPF_CANON-9 at e4a8f39862: [naming-gate] NAMING-GATE: REFUSE 3 graded; rc=1; files unstaged",
      "lib/opal_naming.py generated-carrier mark (MARK = GENERATED by lib/opal_naming.py from infra/logic/registry@...) at e4a8f39862",
      ".tools/gen_mdpf_bronze_homes.py@uncommitted (OUT path literal, line 23)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed at step 4 (commit). Stopped on the naming limb, per the order's rule for a refused JSON literal. Code files remain UNCOMMITTED in the worktree: .tools/gen_mdpf_bronze_homes.py, data/mdpf/config/bronze_homes.json, data/mdpf/scripts/gold/tests/test_mdpf_bronze_homes.py, and the modified data/mdpf/scripts/bronze/pull_orion_model_composition.py. Their checks pass in the worktree (homes 3 of 3; writer 2 of 3, GRANT open per S2)."
}
```

```json
{
  "id": "MDPF_CANON-D1-W9-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T03:46:00Z",
  "one_line": "The commit-time naming limb REFUSES the code commit on lib/opal_naming.py:73, the new BRONZE_HOME_FEEDS literal naming the scopes 'mdpf' and 'inflection' outside lookup(). The cell's code is not committed; the order stops at step 1.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-2 section 1.1 step 1 (the generated target is a lib VIEWS row whose feed map names the scope and tier) and section 2 bound 3 (every new address comes from the builders); a naming-gate refusal is filed as a BLOCKING row with the gate's text and the cell stops, never a workaround.",
  "world_is": "safe-commit naming limb (LGIC_ENFORCE DEC-6, ENFORCE) on the 8-path code commit: 'NAMING REFUSE lib/opal_naming.py:73 inflection -> lookup(inflection): NEW hand-kept carrier (context rule); hand-kept carrier of inflection outside every permitted context: read it through lookup(inflection)'; 'NAMING OUT-OF-PATTERN lib/opal_naming.py:73 mdpf -> lookup(mdpf): EXISTING hand-kept carrier (context rule): WARN'; 'NAMING-GATE: REFUSE 2 graded'. 'ERROR: BLOCKED -- the naming limb refused. Commit aborted; files unstaged.' Nothing landed. The generated JSON and generated_locals.tf were not named in the refusal. Pre-commit commit-gate printed clean for 7 of 8 files.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output, 2026-10-11T03:45Z, worktree C:/Dev/wk-canon-9 branch wk-MDPF_CANON-9 at 9f933161c4 plus uncommitted files: NAMING-GATE: REFUSE 2 graded",
      "lib/opal_naming.py:73 (uncommitted) BRONZE_HOME_FEEDS = {\"orion_model_composition\": (\"mdpf\", \"inflection\")}"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Stopped on the naming limb, per the order's rule for a refused literal. The literal is the cell's own feed declaration: the scope name is typed in lib, not read through lookup(). Resolution is a CTO decision: a permitted context for the declaration, or a registry row for the feed (infra/logic/registry/scopes.json is in this order's paths). No rename, no move, no workaround was made. Code files remain UNCOMMITTED in C:/Dev/wk-canon-9: lib/opal_naming.py, data/mdpf/config/bronze_homes.json, infra/aws/terraform/modules/opal_name/generated_locals.tf, infra/aws/terraform/modules/opal_name/main.tf, infra/aws/terraform/mdpf-pipeline/iam.tf, data/mdpf/scripts/bronze/pull_orion_model_composition.py, lib/tests/test_opal_naming_bronze_homes.py, data/mdpf/scripts/gold/tests/test_mdpf_bronze_homes.py."
}
```

```json
{
  "id": "MDPF_CANON-D1-W9-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T03:46:00Z",
  "one_line": "No plane claims data/mdpf/config/bronze_homes.json: as a VIEWS target it is UNCLASSIFIED in 'lib/opal_naming.py targets' (rc=1), and two lib tests that require every target classified FAIL, so libs TESTS is 2 of 3 arms, not 3 of 3.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-2 section 1.1 step 1: add the target as a VIEWS row and run 'targets', reading its SHIP / REPO-ONLY placement; the JSON reaches the runner by the existing data/mdpf/config -> code/config path. Section 4 NOTE: 'libs' is 3 of 3 at base, a guard the edit must keep green.",
  "world_is": "'lib/opal_naming.py targets' with the new VIEWS row: 'UNCLASSIFIED - data/mdpf/config/bronze_homes.json measured: no plane claims it'; rc=1. The S3 probe _sdc().file_to_s3_target and bundle_for_member are both None for the new file; the tracked sibling data/mdpf/config/route_bindings.yaml is also None/None. The runner's config path is the dispatch sync s3://${MDPF_BUCKET}/${CODE_PREFIX}/config/ -> /opt/mdpf/config/ (infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:130), which no classified plane writes. lib/tests/test_opal_naming.py: 94 passed, 2 failed: test_targets_report_covers_every_known_target_exactly_once (asserts nothing UNCLASSIFIED at the cut) and test_cmd_targets_exit_code_tracks_unclassified (asserts exit 0). r3_checks.py libs: TESTS FAIL (pytest rc=1), DECLARED PASS, DELTA0 PASS: 2 of 3 arms. Measured on uncommitted worktree bytes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python lib/opal_naming.py targets, worktree C:/Dev/wk-canon-9 at 9f933161c4 plus uncommitted, 2026-10-11T03:44Z: UNCLASSIFIED row, TARGETS 14, rc=1",
      "python -m pytest lib/tests/test_opal_naming.py: 2 failed, 94 passed (both failures name the targets tests)",
      "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:130 (config sync, read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A SHIP claim is each plane's own record (EN-g-9, R-26); a classification written into targets_report for this file would be a rule no plane wrote, so the cell did not add one, and it did not edit lib/tests (read-only grant). The plane record for data/mdpf/config/*.json would live in .tools/safe_deploy_core.py, outside this order's paths. Resolution is a CTO ruling: a plane claim for the file, or a declared exemption in the classifier. The order stays open; AC3 is FAIL."
}
```

```json
{
  "id": "MDPF_CANON-D1-W9-S6",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T03:46:00Z",
  "one_line": "The committed generated_locals.tf predates the registry: regenerating it also adds four '4698' lines (the inflection scope's masters) that HEAD does not carry. Kept what the generator wrote; not hand-reverted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-c-2 section 1.1 step 1: if generating generated_locals.tf moves anything beyond the new local and its mark (drift that predates the cell), keep what the generator wrote and say so in a row; do not hand-revert.",
  "world_is": "generate --target generated_locals.tf (mark over exemptions.json,scopes.json,tiers.json) against HEAD: the new bronze_homes local and its mark move, and in addition scope_short, scope_long, scope_class and scope_bucket each gain a '4698' key (the masters of the inflection row in scopes.json). The HEAD mark reads over exemptions.json,scopes.json. scopes.json is unmodified in this worktree.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git diff of infra/aws/terraform/modules/opal_name/generated_locals.tf after generate (scratch diff), worktree at 9f933161c4 plus uncommitted",
      "infra/logic/registry/scopes.json inflection row masters [\"4698\"] (unmodified, read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The generator output is committed-candidate bytes, not hand-edited. A CTO or CloudOps ruling decides whether the committed locals are regenerated in a separate commit. No apply or plan was run."
}
```

```json
{
  "id": "MDPF_CANON-D1-W9-S7",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~9",
  "surfaced_at": "2026-10-11T04:05:46Z",
  "one_line": "The runner-code SHIP claim for data/mdpf/config/ and data/mdpf/scripts/ is measured from the dispatch sync lines, but nothing in the repo copies the repo tree to the runner's code/ prefix: the copy is a hand step, so the new Stage-0 config reaches the runner only when someone syncs it. Plane not widened; the claim is the measured sync.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (with CloudOps): hand-sync data/mdpf/config/bronze_homes.json to s3://opal-data-mdpf/code/config/ and data/mdpf/scripts/ to code/scripts/ before the first post-deploy daily run",
  "spec_asserts": "TO CN-c-2 amendment 3, S5: classify data/mdpf/config/ and data/mdpf/scripts/ as SHIP on a runner-code plane, MEASURED from infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh :125 and :130; if the measured sync differs from the plane (for example, nothing automated copies the repo dir to code/), file a row and do not widen the plane.",
  "world_is": "The measured sync is real (dispatch :125 'aws s3 sync s3://${MDPF_BUCKET}/${CODE_PREFIX}/scripts/', :130 the same for config/, CODE_PREFIX=\"code\", MDPF_BUCKET=\"opal-data-mdpf\"), and the plane is classified SHIP runner-code in targets (rc=0). But no tracked script writes the code/ prefix: a grep of .tools/ and infra/aws/ec2/ for 's3 sync' finds only the runner's reads (dispatch :125, :130, mdpf-dim-backfill-20260729.sh :41, mdpf-catchup-etlfix-ws3.sh :40) and a comment in .tools/safe_deploy_core.py :85. infra/aws/terraform/mdpf-pipeline/iam.tf :196 says the code/ prefix is about 20 commits behind HEAD. The new script raises when /opt/mdpf/config/bronze_homes.json is missing (no fallback, by spec), so a script deployed without its config sync fails Stage 0 of the daily chain.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:28-29, :125, :130 (read; CODE_PREFIX and MDPF_BUCKET assignments and the two sync lines)",
      "python lib/opal_naming.py targets, worktree C:/Dev/wk-canon-9 at 4d304235d5 plus uncommitted, 2026-10-11T04:05Z: 'SHIP runner-code data/mdpf/config/bronze_homes.json ... :130', TARGETS 14, rc=0",
      "Native grep of .tools/ and infra/aws/ec2/ for 's3 sync' (no repo writer of the code/ prefix), 2026-10-11T04:05Z",
      "infra/aws/terraform/mdpf-pipeline/iam.tf:196 (read; the code/ prefix is about 20 commits behind HEAD)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The plane claim stays as the runner's own sync list says (the order forbids widening it). Whether the repo-to-code copy should be automated is a CTO or CloudOps ruling; this row does not propose the mechanism. The ARMED hazard is the missing config sync at deploy, not the classification."
}
```

```json
{
  "id": "MDPF_CANON-D1-S12",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-11T05:10:00Z",
  "one_line": "Row MDPF_CANON-D1-W9-S7's hand step is DONE: bronze_homes.json, the Stage-0 writer and the feeder are on s3://opal-data-mdpf/code/ at the repo bytes, the runner pulled to the builder's address once, and the feeder read is DELTA=0. S7's disarm_owner may disposition it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "ADHOC.canon-r3-bronze-intake: the three files are copied by hand to code/ before the first post-deploy daily run (row S7 disarm_owner clause); deploy exactly the three files, never a tree sync.",
  "world_is": "Measured 2026-10-11T05:00-05:06Z on dell1 from box/dell1 (six source paths unchanged since pin d437b0648f): code/config/bronze_homes.json absent before, now ETag b2d27b65d2e766f9ce599503793bb985 464 B; code/scripts/bronze/pull_orion_model_composition.py ETag 0f2ba775.. -> e64b70fe47621d5df4f87c0fa93efa70; code/scripts/gold/build_mdpf_wsc_inflection_feeder.py ETag 2024adcc.. -> ee2412111e130d8c19574b4f07c051cd; each read back byte-equal to the repo file. One Stage-0 run on i-02448edb624a7a7cf (SSM f1b89351-3669-479a-868a-598939f07e92) exit 0, 9 model files + _meta/pull_complete.json under date=2026-10-11 at the builder's keys. History copied 1030 of 1030 objects, source untouched. Feeder local read with --eclipse-date 2026-10-09: 750 rows, DELTA=0 on every data-bearing column (only _ingested_at differs). TWO FACTS THE ORDER DID NOT EXPECT: (1) the runner-policy grant was already live at order start, applied 2026-10-11T04:41:01Z by cloudops-dell1-agent-user (CloudTrail) with no ledger proof left, so the 0/1/0 plan could not be reproduced; (2) the runner was started by this order and is left RUNNING (stopping EC2 is a confirm-class act); the next dispatch stops it at its own end. The rest of code/ is untouched and still behind HEAD.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/critical_paths/change_management/20261011T0439Z_mdpf-canon-r3-bronze-intake-dell1-20261011_deploy_completion.md (ledger CLOSED, 7 legs with proof)",
      "aws s3api head-object / get-object read-backs and cmp against data/mdpf/** at HEAD, 2026-10-11T05:00Z",
      "aws cloudtrail lookup-events ResourceName=mdpf-daily-runner-ec2-role: PutRolePolicy 2026-10-11T04:41:01Z cloudops-dell1-agent-user",
      "aws ssm get-command-invocation f1b89351-3669-479a-868a-598939f07e92 (PULL_EXIT=0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Evidence row, no defect asserted: records that row MDPF_CANON-D1-W9-S7's hand step was performed and measured. Disposition of S7 and of this row is the COO's and CVO's; the old bronze prefix is not deleted (an S3 delete needs a human's confirmation)."
}
```

```json
{
  "id": "MDPF_CANON-D1-S13",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T05:50:00Z",
  "one_line": "DISARM OF D1-W8-S2 BY ITS DISARM OWNER (CTO, per REMEDIATION_v3): the two carried zero-firm entries (opal_growth_sma, opal_div_sma) are SMA-cohort per-model lines that feed no headline and no trend-stack figure; the fold fix is cut in round 4.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "D1-W8-S2: the global fold re-emits by_model entries no firm holds at the date, with counts frozen at 49financial's 2026-07-17 values, on every run.",
  "world_is": "Served global aggregate-aua-timeseries 2026-10-08 (read 05:4xZ): both entries carry cohort_class 'sma' (45 / 40 accounts; 3,974,709.60 / 17,079,326.24). opal_aggregate_aua 2,147,378,054.74 equals model_aua 1,828,584,618.68 + non_model_aua 289,570,622.57 + sma_additive_aua 410,420.98 (pfde) + tax_additive_aua 28,812,392.51 (tax), so the two carried lines are in no headline sum. The portal Global trend stack builds from non-SMA keys only (ModelPortfolios.tsx nonSmaKeys, cohort_class !== 'sma'). What remains exposed is the two per-model lines wherever a by_model listing includes the SMA cohort. Placement: round-4 cell on the global fold (drop or null a by_model entry no firm holds at the date) under its never-widen pair; Andrew's X2 call dell1-20261011T053810Z-fe9b option A would also fold them.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api get-object opal-data-assets portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-08.json (read-only, 1.0.0_SA_CTO~DELL1 2026-10-11T05:4xZ)",
      "portal/src/pages/ModelPortfolios.tsx nonSmaKeys filter (Global VALUE re-point block)",
      "org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round3.md section 2"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S14",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T05:50:00Z",
  "one_line": "DISARM OF D1-W8-S3 BY ITS DISARM OWNER (CTO): no front-end band is derived as total minus model; the Global stack reads non_model_aua as a field, so the additive gap shows as stack-below-line by pfde + tax (about 1.4%) on 24 dates, never as a mislabelled band.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "D1-W8-S3: the fold docstring states opal_aggregate_aua == model_aua + non_model_aua at every date and says the front end derives the non-model band as total minus model.",
  "world_is": "portal/src/pages/ModelPortfolios.tsx: the (oaa - model_aua) client re-derive is retired (:80); the Global aggregate line is a FIELD READ of opal_aggregate_aua (:789) and the Non-Model band a FIELD READ of non_model_aua (:1872, :2071). So the band is the producer's non_model_aua. On the 24 dates where the headline carries sma_additive_aua + tax_additive_aua, the model bars plus the band sum below the aggregate line by that amount (2026-10-08: 29,222,813.49 of 2,147,378,054.74). Placement: round-4 LOCAL cell corrects the fold docstring to the additive identity; a portal cell renders the two additive components as their own band so the stack meets the line.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/ModelPortfolios.tsx:80, :789, :1872, :2071 (main-tree portal pin)",
      "served global aggregate-aua-timeseries 2026-10-08, the same read as D1-S13"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S15",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T05:50:00Z",
  "one_line": "DISARM OF D1-W8-S5 BY ITS DISARM OWNER (CTO): the X2 re-read is put to Andrew as open call dell1-20261011T053810Z-fe9b, HELD for him (X2 is his grant); FWD-3 stays NOT REALIZED until he answers.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "D1-W8-S5: 06_CONFORMANCE_LEDGER X2 stands GRANTED on the round-2 basis while the round-3 basis reads by_model min firms 0 and non-model series min firms 1.",
  "world_is": "Open call dell1-20261011T053810Z-fe9b (fork, REC option A: fold by_model entries held at fewer than 2 firms into one line and keep the one-firm series out of global; B: accept and rewrite FWD-3), published to s3 box=dell1 and HELD for Andrew. No served output moves before his word.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/state/dell1/open_calls.json row dell1-20261011T053810Z-fe9b",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md @945e1add0c"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```
```json
{
  "id": "MDPF_CANON-D1-W10-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~10",
  "surfaced_at": "2026-10-11T06:16:51Z",
  "one_line": "CN-d-1 asks for two docstrings in dim_mdpf_aggregate_aua_timeseries.py to be changed; the live pure-addition guard TXA1-AC4 forbids any removed line in that file vs HEAD. The first edit removed the HEADLINE header line and the guard failed; resolved by restoring every existing line and adding lines only.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-d-1 step 3: change the build_global_artifact HEADLINE IDENTITY paragraph (say it is the BASE identity) and change nothing else in the file; the cell reads as an in-place edit of existing docstring text.",
  "world_is": "data/mdpf/tests/taxsma/test_taxsma_aggregate.py::test_ac4_no_existing_line_in_the_production_module_was_changed runs git diff --unified=0 HEAD on that file and asserts zero removed lines. The in-place edit failed it with one removed line (the header). The served-identity wording was added as new lines only; the diff now has 0 removed lines and 272 of 272 stratid+taxsma+canon tests pass.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/mdpf/tests/taxsma/test_taxsma_aggregate.py:104-131@fdc574c044",
      "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py (HEADLINE IDENTITY block, build_global_artifact docstring)@fdc574c044"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```
```json
{
  "id": "MDPF_CANON-D1-W10-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~10",
  "surfaced_at": "2026-10-11T06:16:51Z",
  "one_line": "assert_global_served_identity has no difference to the cent for a date where opal_aggregate_aua is set and model_aua or non_model_aua is None; the refusal names that date with a reason text in the difference slot, because no difference exists to print.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-d-1 step 1: the refusal lists up to the first five violations as (date, difference to the cent); a date with opal set and model_aua None is refused (test 5 of the cell).",
  "world_is": "A difference cannot be computed against a None term, so the function records (date, 'model_aua or non_model_aua absent') for that date. It prints no level. The served 2026-10-08 global object has no such date: check r4_cn_d_1.py A4 passes on 484 non-null opal dates.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py assert_global_served_identity (the model/non-model None branch)@fdc574c044",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_1.py A4 PASS (484 non-null dates)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```
```json
{
  "id": "MDPF_CANON-D1-W10-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~10",
  "surfaced_at": "2026-10-11T06:19:46Z",
  "one_line": "The order's closing step flips its own <status> to complete, but the task-order file is outside this worker's <paths>; the flip is NOT made by the worker and the order stays open on that step.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-d-1 section 5: flip this order's <status> to complete in the same commit as the proof instance, only when every mechanical criterion passes.",
  "world_is": "The order file is task-orders/MDPF_CANON.TO-CN-d-1.served-identity-and-cottonwood-vintage.md, line 127 reads <status>pending</status>. Section 3 of the same order lists the write grant (<paths>) and that file is not in it, so the commit that touches it would sit outside the lane. Both mechanical criteria pass; the flip is left to the COO.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-d-1.served-identity-and-cottonwood-vintage.md:127@fdc574c044",
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-d-1.served-identity-and-cottonwood-vintage.md section 3 <paths>@fdc574c044"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W12-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~12",
  "surfaced_at": "2026-10-11T06:17:45Z",
  "one_line": "CN-d-3 portal commit: git refused the order's commit form (--author only) with 'Committer identity unknown' (rc=128) in the nested portal repository; committed with the committer supplied per command, no git config written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-d-3 section 5.1: git -C portal commit --author \"0.9.0_WK_MDPF_CANON~12 <0.9.0_WK_MDPF_CANON~12@opal.agent>\" -F <msgfile> (the order names the author only; no committer identity).",
  "world_is": "The nested repository on wk-MDPF_CANON-12-portal has no committer identity configured (git: fatal, unable to auto-detect email address, rc=128). The commit landed as 133fb8af1479 after GIT_COMMITTER_NAME and GIT_COMMITTER_EMAIL were set for that single command; no git config was written and no hook was bypassed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C C:/dev/wk-canon-12/portal commit (first attempt) refused: 'Committer identity unknown', rc=128",
      "portal branch wk-MDPF_CANON-12-portal commit 133fb8af1479 (author and committer 0.9.0_WK_MDPF_CANON~12, 2 files, 52 insertions, 3 deletions)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```
