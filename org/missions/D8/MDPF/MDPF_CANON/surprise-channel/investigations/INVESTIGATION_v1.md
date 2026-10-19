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

```json
{
  "id": "MDPF_CANON-D1-W13-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~13",
  "surfaced_at": "2026-10-11T06:18:09Z",
  "one_line": "CN-d-4 COMPLETE-FLIP REFUSED BY THE GATE: to-pipeline-gate check_complete_flip finds no instance beside the order (tree stem search wants deliverables/<serial>/MDPF_CANON.TO-CN-d-4.count-audit-reads-the-gold-artifact.proof_of_spec.json); the order directs the to_id-named instance, which is VALID (rc=0); the flip is held at pending.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1",
  "spec_asserts": "CN-d-4 Section 5: write the instance at deliverables/0.9.0_WK_MDPF_CANON~13/MDPF_CANON.TO-CN-d-4.proof_of_spec.json and flip <status> to complete in the SAME commit as the proof instance; the flip is the criterion.",
  "world_is": "The order file is named MDPF_CANON.TO-CN-d-4.count-audit-reads-the-gold-artifact.md; .tools/to-pipeline-gate.py _proof_instance_candidates (tree branch) searches deliverables/*/<order-stem>.proof_of_spec.json, so the to_id-named instance is not a candidate. Commit refused: 'flips to complete on PIPELINE-REGISTERED project MDPF_CANON, and NO proof-of-spec instance was found beside it' (code commit ed1d3241d9 LOCAL on wk-MDPF_CANON-13; the flip was reverted to pending and not committed). The fix text the gate prints (a tag block in the TO face, or a pipeline-override line) is a workaround and was not applied.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-d-4.count-audit-reads-the-gold-artifact.md@73fdbf8d0a",
      ".tools/to-pipeline-gate.py@ed1d3241d9 lines 3176-3191 (_proof_instance_candidates) and 3253 (the refusal text)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~13/MDPF_CANON.TO-CN-d-4.proof_of_spec.json (proof-of-spec-check.py rc=0, violations=0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W14-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~14",
  "surfaced_at": "2026-10-11T06:17:08Z",
  "one_line": "CN-d-5 LEFT THE --files SUMMARY DENOMINATOR AND THE NAMED OUTPUT UNDEFINED: the order names `files <N>`, `equal <E>`, `not_equal <K>` and the `| named <n> | named_not_equal <k>` suffix with no definition, and no line format for the named grading; the worker defined them and states the definition in the tool's docstring.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-d-5 section 1.1: the summary line is `MDPF-CODE-EQUALITY: trees <T> | files <N> | equal <E> | not_equal <K>`, with `| named <n> | named_not_equal <k>` appended under --files; N, E, K and the body printed under --files are not defined.",
  "world_is": "The tool defines files as the count of distinct relative names across the local and S3 sides of the trees shown, so equal + not_equal = files; under --files it prints the trees that hold the named files, then one NAMED EQUAL or NAMED NOT_EQUAL line per name with its class; exit codes and REFUSED texts follow the order. The live whole-tree run reads files 77 | equal 48 | not_equal 29 over five trees.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/mdpf-code-equality.py (worktree wk-MDPF_CANON-14, uncommitted at filing; module docstring MODES paragraph)",
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-d-5.runner-code-equality-step.md@73fdbf8d0a section 1.1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-S16",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-11T06:29:14Z",
  "one_line": "safe-merge.sh --continue committed a merge from a stale index snapshot after HEAD moved, and the merge commit reverted a peer's commit (7 paths); restored byte-exact in c190e6faf8.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "safe-merge.sh --continue: 'committing the merge as <author> (from the index snapshot taken right after the merge; a peer's later staging cannot enter it)' -- a peer's later STAGING cannot enter, and a peer's later COMMIT is expected to survive the merge.",
  "world_is": "Drain of wk-MDPF_CANON-14: the merge was opened at HEAD 68e13832ab; peer commit b1bd62f384 (0.7.0_AE_CloudOps~SC1, 02:24:57 local) landed on box/dell1 while the conflict was being resolved; --continue then committed 0468b6c8ba (02:25:38) with parents (b1bd62f384, 912327aeab) and a tree built from the older snapshot. `git diff 0468b6c8ba^1 0468b6c8ba` showed 2 modified and 5 deleted paths of the peer's commit (E87_PREFIRE_VERSIONS 109,418 lines, its proof instance, a log, two outputs, and its ledger entry reverted). The four earlier merges of this round (24e8981f2f, 9ecb1d4a66, 54e1fc41d8, 68e13832ab) show no path outside their branch. Repair: `git restore --source=b1bd62f384` of the 7 paths and commit c190e6faf8 under the audited GIT_COMMIT_AUTHOR_OVERRIDE=SHARED_CLOUD_OPS, because the five tier2 paths are another lane's; `git diff b1bd62f384 HEAD` over the 7 paths reads 0 lines. Not measured: whether the tool re-reads HEAD after a conflicted resolve; the fix belongs to the tool's owner.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show --stat 0468b6c8ba and git diff --name-status 0468b6c8ba^1 0468b6c8ba (7 peer paths reverted, read 2026-10-11 ~06:3xZ)",
      "git diff b1bd62f384 HEAD over the 7 paths = 0 lines after c190e6faf8",
      ".tools/safe-merge.sh --continue output line: committing the merge as 2.0.0_SA_COO~D1 (from the index snapshot taken right after the merge)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the tool is 0.0.0_AB_MSTR. Mitigation for any drain with a conflict to resolve: after --continue, run `git diff <merge>^1 <merge> --name-status` and read every path outside the branch's own set before anything else lands."
}
```

```json
{
  "id": "MDPF_CANON-D1-W15-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~15",
  "surfaced_at": "2026-10-11T07:28:32Z",
  "one_line": "TO CN-e-1 step 4 requires catching UnknownModelError for the registry-miss case, but step 1 lists only entry_for_key in the crosswalk import; the instrument imports UnknownModelError beside it so the except clause resolves.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-e-1 step 1 (imports): 'from mdpf_revamp_model_crosswalk import entry_for_key  # noqa: E402'; step 4: 'None where the registry does not know the key (UnknownModelError)'.",
  "world_is": "The except clause names UnknownModelError, which is not in scope under the step 1 import line alone (NameError at the first unknown by_model key). The edited import line is 'from mdpf_revamp_model_crosswalk import UnknownModelError, entry_for_key  # noqa: E402' in data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py (worktree wk-MDPF_CANON-15). Behaviour is the step 4 behaviour; only the import name set differs. The reader check passes 5 of 5 and the census and seam arms pass.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py:279 class UnknownModelError(KeyError) @a67e04d469 (worktree base)",
      "data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py import block after the edit (CN-e-1 commit)",
      "python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/checks/r5_cn_e_1.py reader -> ROUND 5 READER: 5 of 5 arms"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker at CN-e-1 so the import difference from the order's step 1 is traceable. The CVO reads it at L8."
}
```

```json
{
  "id": "MDPF_CANON-D1-S17",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-12T17:50:00Z",
  "one_line": "The one on-demand gold run built the new global account-distribution (exactly the two cottonwood_fold keys beyond a process stamp) but could NOT land it: the writer reports status conflict on every object whose as-of date already exists, so C4's served-object clause is unobservable until a new as-of date is minted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "ADHOC.canon-r4-code-deploy C4 / pair section 5: after the one on-demand run the global account-distribution for the latest date gains exactly meta.cottonwood_fold.value_date and .age_trading_days; every other object of every scope and type is value-equal; the manifest errors are empty.",
  "world_is": "Measured 2026-10-12T17:31:44Z-17:32:57Z. Invoke status 200, no FunctionError, payload status green, errors [], a4_objects_built 16 of 16. Served objects: 18 of 18 baseline objects value-equal and byte-equal (sha256) before and after, INCLUDING global/account-distribution/2026-10-12.json (sha256 0a8205c0e791...), i.e. it did NOT gain the two keys. Cause read from the run's own manifest s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json: writes carry status conflict for 13 objects, unchanged for 3, staged 4, written 1 (the taxsma control). The conflict row for global/account-distribution/2026-10-12.json lists business_diff_paths = [_provenance.process_time, meta.cottonwood_fold.age_trading_days, meta.cottonwood_fold.value_date] (3 of 3), so the new body differs from the existing one by exactly the two keys plus the process-time stamp, which meets the order's content expectation, but the object was not replaced. The only new object under portal/gold/mdpf/ is the manifest itself. The other 12 conflicts differ by provenance or time stamps, plus cottonwood meta.assignment_date, source, value_date_rekey and one knowledge_date (cottonwood sidecar-driven; not from this change). The pair's own section 6 acceptance is the FIRST SCHEDULED run that mints a new as-of date; the next is 2026-10-13T13:30Z.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json (writes[], run.data_as_of 2026-10-09)",
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r4_served_baseline_BEFORE_20261012.json and the after-read compare, 18 of 18 equal",
      "aws lambda invoke 2026-10-12T17:31:38Z-17:32:57Z, StatusCode 200"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "This seat did not retry: the order allows ONE run and a retry could not differ. The ledger mdpf-canon-r4-code-deploy-dell1-20261012 keeps leg L6 open and is held on the first scheduled run reading the served global account-distribution for a new date. Whether C4 grades on the manifest's business diff or waits for that run is the issuer's and the CVO's."
}
```

```json
{
  "id": "MDPF_CANON-D1-S18",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-12T17:50:30Z",
  "one_line": "The gold lambda's declared vintage MDPF_GOLD_COMMIT still reads 88e974ca10 while the deployed package is built from 0d39789fdf, so every run manifest stamps run.code.commit 88e974ca10, a vintage its own bytes do not match.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "infra/aws/terraform/mdpf-pipeline/gold-lambda.tf (the environment block's own rule): WHEN RE-PINNING, SET THIS FROM THE --pin YOU ACTUALLY BUILT WITH. The order's D2 says the plan moves only the function's code and forbids a source edit.",
  "world_is": "Measured 2026-10-12T17:30-17:33Z. Function environment MDPF_GOLD_COMMIT = 88e974ca10237b6555bcda633ca83a54e4a5dcc9 before and after D2 (the plan graded it unchanged). The deployed package's in-zip BUILD_MANIFEST source_vintage.commit = 0d39789fdf38df2550cf1b60fb03798fadca22e2. The on-demand run's manifest run.code.commit read 88e974ca10. Same drift class gold-lambda.tf documents three times already (2026-08-24, 2026-08-28). Nothing served moves; the provenance line is wrong until a one-line env change is applied.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda get-function-configuration mdpf-gold-lambda, 2026-10-12T17:25Z and 17:31Z",
      "deployed package BUILD_MANIFEST.json read from Code.Location, 2026-10-12T17:31Z",
      "s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-10-09/20261012T173257Z.json run.code"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Fix is a one-line value change in gold-lambda.tf plus a targeted apply, under its own order and pair: it is an environment attribute, which this order's plan check treats as a stop. Not done here."
}
```

```json
{
  "id": "MDPF_CANON-D1-S19",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-12T17:44:32Z",
  "one_line": "Correction to rows MDPF_CANON-D1-S17 and MDPF_CANON-D1-S18: both carry surfaced_at values (17:50:00Z and 17:50:30Z) that are later than the commit that landed them; the true surfacing hour is 17:38Z-17:39Z.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A row's surfaced_at is the time the finding was surfaced, taken from the clock (surprise-row-gate WARNs on a future stamp).",
  "world_is": "Rows D1-S17 and D1-S18 were committed at 17:39Z in commit 17d0f0fc74 with surfaced_at 2026-10-12T17:50:00Z and 2026-10-12T17:50:30Z, typed by hand ahead of the clock. The facts in both rows were measured 17:30Z-17:36Z. The channel is append-only, so the rows are not edited; this row is the correction (issuer's note msg 4515).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "surprise-row-gate WARN at commit 17d0f0fc74: 'surfaced_at 2026-10-12T17:50:30Z, 11 min after the commit time 2026-10-12T17:39Z'",
      "2.0.0_SA_COO~D1 msg 4515, 2026-10-12T17:41:50Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No fact in S17 or S18 depends on the stamp; both stand."
}
```

```json
{
  "id": "MDPF_CANON-D1-W16-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~16",
  "surfaced_at": "2026-10-12T18:25:06Z",
  "one_line": "Global category-views re-sums by_model into Models and compares it with total_aua at the gold plane. On a date whose fold pool is held by one firm the fold line is None, Models falls short, and ViewPlaneError is raised outside any isolation, which aborts build_all for every scope.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to 1.0.0_SA_CTO, owner of the Global category-views gold-plane read; the fold may not suppress the as-of pool until that read takes it)",
  "spec_asserts": "CN-f-1 Step 2: read every statement from the fold guard to the last use of arts[global][by_model]; a statement that re-sums by_model or compares it with a headline total is a BLOCKING row. The fold moves dollars out of by_model without redistribution and leaves headline totals unchanged.",
  "world_is": "mdpf_gold_consolidator.py: _shape_category_views (def at :635) sums the as-of model_value of every by_model member into Models (models_aum, :787) and passes total_aua to registry.build_category_views (:990). The Global call (:3084) is not inside _isolated. mdpf_category_registry.py:1325-1331 raises ViewPlaneError when sum(TOP_LEVEL_PEERS) differs from total_aua beyond RECON_TOLERANCE. Measured read-only 2026-10-12 on the served global objects at 2026-10-09: other_models_emitted_as_of True and the as-of is not in suppressed_dates, so NOT live today. It is reachable on any day the as-of pool is held by fewer than two firms. The consolidator's own note at :684-689 records that such a raise aborted build_all for all scopes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r6_cn_f_1_comparator.py read of the served global objects at 2026-10-09: K0-K10 11 of 11",
      "read-only probe .scratch/as_of_probe.py: other_models_emitted_as_of True; as-of in suppressed_dates False; fold_keys 11; emitted dates 47",
      "mdpf_category_registry.py:1325-1331 (gold-plane raise); mdpf_gold_consolidator.py:635, :787, :990, :3084"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not fixed in this cell: the consumer sits outside the cell's paths, and the registry is read-only for this order. No level printed."
}
```

```json
{
  "id": "MDPF_CANON-D1-W16-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~16",
  "surfaced_at": "2026-10-12T18:25:06Z",
  "one_line": "The aum-metrics current value for the Other Models row falls back to its last real pooled value when the as-of is null, so a suppressed as-of would show dollars the fold had withheld.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to 1.0.0_SA_CTO: a fold line's current value must be honest-None on a suppressed as-of, not the last pooled value)",
  "spec_asserts": "CN-f-1 Step 3b: the other_models row is built by the existing code from the folded series and follows the honest-None law (a null is absent, never zero and never carried).",
  "world_is": "dim_mdpf_aum_metrics.py build_aum_metrics, by_model loop: cur_val = mvals[gi]; when that is None it sets cur_val = _frontier(mvals) (:364-369), which returns the last non-None value. When the as-of fold line is suppressed it is None on the as-of, so the row would carry its last pooled dollars as current and its q-cells would be computed from that carried figure. Measured read-only: the as-of is emitted today, so it does not fire now.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "read-only probe .scratch/as_of_probe.py: other_models_emitted_as_of True at 2026-10-09",
      "dim_mdpf_aum_metrics.py:364-369 (_frontier) and the by_model loop of build_aum_metrics"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed here: the fallback is pre-existing code for absent keys, and changing it is a decision for the issuer. The new fact is that a fold line reaches it."
}
```

```json
{
  "id": "MDPF_CANON-D1-W16-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~16",
  "surfaced_at": "2026-10-12T18:25:06Z",
  "one_line": "The AC4 roll-up delta is not the as-of delta: on 2026-10-09 the fold line is emitted, so the two blends' dollars stay in Models through Other Models. The change falls on per-model rows and history, not on the as-of roll-up total.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-f-1 section 4, AC4 SEMANTIC: the only client-visible deltas are the two inflection blends leaving the Model Portfolios roll-up, the Total Holdings count, and per-model history starting where Global first combined two firms.",
  "world_is": "Read-only probe at 2026-10-12 on the served global objects at 2026-10-09: other_models_emitted_as_of True; 11 fold keys, 9 held by one firm and 2 by none on the as-of; 5 of 5 kept lines carried on the as-of. With the fold line emitted on the as-of, no suppressed dollars fall on the as-of, so the Models total is unchanged there. The suppressed dollars fall on 438 of 485 valued dates, which is the per-model history change. The fold changes no account_count_total and no distribution total (spec), so no total count moves; the count changes are per-model. Judgment for L9, not graded by this worker.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "read-only probe .scratch/as_of_probe.py at 2026-10-12: other_models_emitted_as_of True; kept lines 5 of 5 on the as-of",
      "r6_cn_f_1_comparator.py K5: dates where the gap moved 438 of 485 valued dates, each equal to its suppressed dollars"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded as a premise check for the round-6 close. No level printed."
}
```

```json
{
  "id": "MDPF_CANON-D1-W16-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~16",
  "surfaced_at": "2026-10-12T18:40:21Z",
  "one_line": "AMENDMENT 1 disarms S2 only for a one-firm as-of. On a no-pool as-of the fold line is None on the last date with no dollars withheld, yet aum-metrics still fills the Other Models current value from its last pooled value, so the carried dollars are served as current.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to 1.0.0_SA_CTO: the current-value fallback in build_aum_metrics must not fill a fold line from an earlier date)",
  "spec_asserts": "AMENDMENT 1 step 6a and the S2 disarm claim: the as-of line is never None-with-dollars, and a pool with no value on the last date is not a refusal because there are no dollars to withhold.",
  "world_is": "dim_mdpf_aum_metrics.py build_aum_metrics by_model loop: cur_val = mvals[gi] (:551); when that is None it sets cur_val = _frontier(mvals) (:555), which returns the last non-None value of the series (:364-369). On a day where no folded line has a value on the last date, the fold line is None on the last date while it carried dollars on an earlier date, so the row is built with that earlier value as its current aum. Measured here by reading the code, not by running build_aum_metrics. Today's as-of (2026-10-09) is emitted, so the path is not live; it is reachable on any no-pool day.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dim_mdpf_aum_metrics.py:551-556 and :364-369 (read at HEAD d2849f4221)",
      "r6 contract C12 no-pool arm asserts the Global build only, not the aum-metrics row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed here: the fallback is pre-existing code and the order does not name aum-metrics' current value. The issuer must rule whether a fold line on a no-pool day is absent from the aum-metrics by_model or carried. No level printed."
}
```

```json
{
  "id": "MDPF_CANON-D1-W16-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~16",
  "surfaced_at": "2026-10-12T18:40:21Z",
  "one_line": "The refusal does not stop the global staging write: build_all writes the unfolded global aggregate to gold/mdpf_revamp/global/aggregate_aua_timeseries.json before the fold guard runs, so on a refused day that object is still written although Global is refused whole.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to 1.0.0_SA_CTO: rule whether the staging copy moves behind the fold guard, or whether a refused day skips it)",
  "spec_asserts": "AMENDMENT 1 step 6a: Global is refused WHOLE (its category views, aum-metrics and account distribution are not built or written for that run) and the prior Global object stays served.",
  "world_is": "mdpf_gold_consolidator.py: stage_put of f-string STAGING_PREFIX/global/aggregate_aua_timeseries.json at :2838, inside the global branch before the tax and SMA overlays, and before guard_global_min_firms_fold at :2943. The staged copy is pre-tax, pre-overlay and unfolded on every run, not only on a refused day. Its readers are unverified: comp-pipescript io reports the consolidator's dynamic prefixes as UNRESOLVED-PREFIX and cannot name who reads the staged key. The amendment's 'not built or written' list does not name this object.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mdpf_gold_consolidator.py:2838 (stage_put of global/aggregate_aua_timeseries.json) and :2943 (guard) at HEAD d2849f4221",
      "comp-pipescript io data/mdpf/scripts/gold/mdpf_gold_consolidator.py: READS none detected; UNRESOLVED-PREFIX (4); WRITES none detected"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed here: moving the write changes staged content on every run, which is outside this amendment. The reader question is open."
}
```

```json
{
  "id": "MDPF_CANON-D1-S20",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-13T14:00:16Z",
  "one_line": "The qa_local dry run of mdpf-gold-lambda created two NEW tax-prelude objects (a bronze and a silver workbook snapshot for knowledge date 2026-10-13); the order expected the stores to read the same, because it assumed a second acquisition on the same day is a no-op conditional create. It is not: the key carries the response sha256, which differs per acquisition.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "ADHOC.canon-r6-fold-deploy leg d and pair section 4: qa_local does not pass dry_run into the tax prelude, whose stores are conditional creates; run after the same day's fire each store already holds that date, so the writes are no-ops; every store and the control key read the SAME VersionId, and a change is a STOP with a BLOCKING row naming the key.",
  "world_is": "Measured 2026-10-13T13:58Z. The one dry run (invoke 13:57:03Z-13:58:18Z, 200, green, errors [], 16 of 16) left all 16 served objects byte-equal with the same VersionId, the control key mdpf/global/state/taxsma_control/current.json at VersionId exA7udEpsIfWTRSK4HmnhLK.X7Y4Ebil, the four durable stores' EXISTING objects at their VersionIds (bronze yZlDy9Xq.., silver XGDYmwoko75.., dispositions 49f YARonRjo.. cot aWcj2tjY.., gold assets 49f A0axHKqe.. cot n6xJnCBb..), and the emitter CodeSha256 unchanged. It ALSO created, at 2026-10-13T13:58:14Z, two objects that did not exist at the before print: s3://opal-data-assets/gateway/global/bronze/taxsma_workbook/date=20261013/354362accd108ee3d84f80fab41b1595f9ebd1afc7b244e2e097e7948f22e853-231f1f19e583de1242fa4ff8bce4b53992a8d78694a8979e8e351b7c1482cb94.json (5,656 B, VersionId xVpjCobJKbo.s9RN500CcKxWf1sqLPdY) and s3://opal-data-assets/gateway/global/silver/taxsma_workbook/date=2026-10-13/354362accd108ee3d84f80fab41b1595f9ebd1afc7b244e2e097e7948f22e853-231f1f19e583de1242fa4ff8bce4b53992a8d78694a8979e8e351b7c1482cb94.parquet (15,673 B, VersionId J.xeeTys9uvPCo7TRw_nfRB4PdTpmcs_). Same snapshot_id 354362ac.., a different response_sha256 (231f1f19.. against the fire's 5ac6579c..): each acquisition of the workbook is a new key. The same pattern is on record for date=20261012: one object at 13:31:43Z (the fire) and a second at 17:32:49Z (the CN-d-1 real run of 17:31Z), on the code BEFORE this order, so the cause is the acquisition, not the four deployed files. The gold assets objects and the dispositions did not change.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r6_taxstores_before_20261013.json and ..._after_...json",
      "aws s3api head-object / list-objects-v2 on the two keys, 2026-10-13T13:58Z (LastModified 13:58:14Z inside the invoke window)",
      "aws s3api list-objects-v2 prefix gateway/global/bronze/taxsma_workbook/date=20261012/ (13:31:43Z and 17:32:49Z)",
      "aws lambda invoke 2026-10-13T13:57:03Z-13:58:18Z StatusCode 200 payload status green errors []"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "STOPPED as the order says; no further act. No rollback taken: the objects are write-once creates a code rollback would not remove, the same two-object pattern followed the real run on the CN-d-1 code, and a rollback would put the pre-fold code on tomorrow's first folded fire. The four keys and the prior package (artifact VersionId qUUF7ZdR5eqGOL.5j8fJgrR2RAMhcviU, MDPF_GOLD_COMMIT 88e974ca10) stay recorded in ledger mdpf-canon-r6-fold-deploy-dell1-20261013 for the issuer's call before 2026-10-14T12:45Z. Whether a consumer reads 'latest object under date=' and can pick up a second snapshot is not measured here."
}
```

```json
{
  "id": "MDPF_CANON-D1-S21",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-13T19:27:52Z",
  "one_line": "The global category-views snapshot of a date and the NEWEST global time series disagree on that same date by -4,649.20 to +301,207.84 over the 21 dated category-views objects (18 of 21 nonzero), because the served time series restates its own history; against each date's own dated time-series object the remainder is 0.00 on 21 of 21. Cause of the restatement not established.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v2.13-v2.16 FWD-9 DONE WHEN (2): on each drawn date every grouped series equals the sum of its served members to the cent, and the stack sums to opal_aggregate_aua; the Client chips are read from that date's category-views node and Other AUA is the remainder non_model_aua minus the two chips minus the carve-out ETF members.",
  "world_is": "Measured 2026-10-13T19:27:52Z, read-only. 21 dated objects portal/gold/mdpf/global/category-views/2026-08-27.json .. 2026-10-12.json; per date remainder = non_model_aua - nodes.Client.children['Client - Opal Supervised'].aum - ['Client - Opal Unsupervised'].aum - (opal_div_sma + opal_growth_sma). Against the newest aggregate-aua-timeseries (2026-10-09.json at the read): min -4,649.20, max +301,207.84, nonzero on 18 of 21. Against each date's OWN dated aggregate-aua-timeseries object: 0.00 on 21 of 21. Between a date's own dated ts object and the newest ts on the SAME as-of date: non_model_aua differs on 18 of 21 dates (range -4,649.20 .. +301,207.84, the same numbers as the remainder), model_aua on 20 (range -301,207.84 .. +24,107,399.71), opal_aggregate_aua on 18 (+405,856.99 .. +24,514,901.22); the carve-out members and the additive terms do not differ. The +301,207.84 on non_model_aua is matched by -301,207.84 on model_aua on the same date (a reclassification between buckets); the +24.1M model_aua and +24.5M aggregate restatements are history that a later object carries and the earlier did not. The cause of either restatement was not established here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-assets/portal/gold/mdpf/global/category-views/ (21 dated objects)",
      "s3://opal-data-assets/portal/gold/mdpf/global/aggregate-aua-timeseries/<date>.json (own-date objects) and the newest key, compared on the same as-of date",
      "CTO msg 5109 (the +301,207.84 and -4,649.20 figures) reproduced by the issuer"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Consequence for FWD-9: the cent-exact Client sum holds against a date's own dated ts object (21 of 21) and not against the newest (3 of 21). The grade and the client-facing PROD card must state which object the sum is read against; the card carries this difference (CTO msg 5109). No served object moved."
}
```

```json
{
  "id": "MDPF_CANON-D1-S22",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-13T21:12:32Z",
  "one_line": "The MDPF portal publisher's role cannot read its own prior-run pointer (platinum/mdpf/_manifests/latest.json: s3:GetObject AccessDenied), so its 'unchanged means no write' check never fires and all 18 scope/type pairs are rewritten every run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "opal-assets-mdpf-portal-publisher/lambda_function.py: a pair whose source is unchanged since the prior run records status 'unchanged' and issues no put_object; the pointer latest.json is read once per run for that comparison.",
  "world_is": "Measured 2026-10-13T21:12:32Z, read-only. Manifest s3://opal-data-portal-v2/platinum/mdpf/_manifests/2026-10-13/20261013T135047Z-4fca44fb.json: prior_pointer_note = AccessDenied on s3:GetObject of platinum/mdpf/_manifests/latest.json for assumed-role opal-assets-mdpf-egress-publisher-role/opal-assets-mdpf-portal-publisher; rows 18, every row status 'published' (0 'unchanged'), all_present true, missing_pairs []. The pointer object exists (LastModified 2026-10-13T13:50:54Z). Surfaced by the CN-j-1 draft fork; the issuer re-read the manifest. Effect: each daily run rewrites every served platinum leaf with the same data bytes and a newer _provenance.written_at; nothing served is wrong. It matters to any change that adds leaves (CN-j-1 adds four): they also republish daily.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-portal-v2/platinum/mdpf/_manifests/2026-10-13/20261013T135047Z-4fca44fb.json (prior_pointer_note, rows)",
      "infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py (the unchanged check)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not fixed here: the role's grant is IAM (a Terraform pair of its own), not in any MDPF_CANON cell. The IAM simulation the fork cites was not re-run by the issuer (this identity holds no SimulatePrincipalPolicy grant yet); the manifest AccessDenied text is the evidence."
}
```

```json
{
  "id": "MDPF_CANON-D1-S23",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-13T22:38:19Z",
  "one_line": "The code-equality tool .tools/mdpf-code-equality.py (CN-d-5, round 4) hashes the checkout's working-tree bytes, not the git blob, so a CRLF working-tree file reads DIFFER against an S3 object that equals its git blob byte for byte.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "docs/deployment/MDPF_RUNNER_CODE_SYNC.md and CN-d-5: a runner-tree name reads EQUAL when the S3 object equals the repo's file; the round-4 close is 'every file the dispatch chain executes or reads is EQUAL, every other non-EQUAL name is listed with its reason'.",
  "world_is": "Measured 2026-10-13T22:38:19Z, read-only, by the issuer re-checking a read-only fork's claim. data/mdpf/scripts/gold/mdpf_model_registry.json: S3 md5 6b89cc935c, git blob (git show HEAD:path) md5 6b89cc935c, working-tree md5 fa784dd4ab: S3 equals the blob and not the working tree, and the tool lists the name as DIFFER (one of CloudOps' 8 runner-member rows, 2026-10-12). Cause: the dell1 checkout has CRLF line endings on that file. data/mdpf/config/bronze_homes.json is a true difference of one line: S3 carries _generated 'infra/logic/registry@bd1619b411e1330c', the repo '@280826a6a96c3b37' (provenance comment only, FIRMBKTS-owned under PRD v2.11 R2). Effect: a false DIFFER inflates the non_EQUAL count and a named-file deploy from a CRLF checkout could write CRLF bytes (whether safe-deploy.sh normalizes was not verified). Of CloudOps' 8 runner members, the issuer re-verified 2 of 8 against S3 and the blob here; the other 6 dispositions are the fork's read (round7/CODE_SYNC_RUNNER_MEMBERS_READ.md).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-mdpf/code/scripts/gold/mdpf_model_registry.json vs git show HEAD:data/mdpf/scripts/gold/mdpf_model_registry.json (md5 6b89cc935c both)",
      "s3://opal-data-mdpf/code/config/bronze_homes.json vs git show HEAD:data/mdpf/config/bronze_homes.json (one _generated line)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Repair is one LOCAL line of the tool (compare against the git blob, or normalise EOL) plus its test: it batches into round 7's repair cell once the CTO's round-6 analysis is in hand; not cut here (the round-6 spec and decomposition are frozen)."
}
```

```json
{
  "id": "MDPF_CANON-D1-S24",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T14:05:00Z",
  "one_line": "The round-6 packet's /portfolios card (client-facing, for Andrew) reads Total Holdings 8,607 -> 8,607 (delta 0) because it was run with --date 2026-10-13; at the documented run date 2026-10-14 the same tool reads 8,607 -> 8,430 (-177), the pair's named delta within roster drift.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py after --date 2026-10-13: Total Holdings 8607 8607 0 (the account-distribution object is keyed by RUN date, so <= 2026-10-13 returns the unfolded 2026-10-13.json, the same object the BEFORE snapshot pinned)",
      "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py after --date 2026-10-14: Total Holdings 8607 8430 -177; AFTER folded objects ['aum-metrics', 'account-distribution', 'aggregate-aua-timeseries']",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py docstring: 'Run on 2026-10-14 after the first folded fire:  python portfolios_card.py after --date 2026-10-14'",
      "round6/NEVER_WIDEN_PAIR_R6_CN_F_1.md section 6: 'Total Holdings -185'"
    ]
  },
  "spec_asserts": "The card to Andrew states the client-visible deltas the fold makes, read on the folded objects (pair section 6; the tool's own run instruction).",
  "world_is": "Total Holdings did move: -177 (the pair said -185; the 8-account gap is the roster drift R7 prints, 211 vs 207). The packet's 'delta 0' is a read of the unfolded distribution against itself. Every other card row is the same at either date. Nothing served is wrong; the card is wrong if it goes as written.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W22-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~22",
  "surfaced_at": "2026-10-14T14:39:21Z",
  "one_line": "The order names only the after-line dates as the things to keep; the AFTER table title printed the --date argument, which is None when the default date is used, so the title now prints the date actually read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "MDPF_CANON.TO-CN-k-1 section 1 Part B step 5: everything else in the output, the before subcommand, the pinned snapshot logic and every number stay as they are.",
  "world_is": "At HEAD of this worktree, portfolios_card.py main() builds the AFTER title from args.date. With --date now optional, that value is None on the default path, so the title would read 'at or before None'. The worker changed the title argument to the resolved date (d_read); on an explicit --date run the argument and the resolved date are the same string, so the printed title is unchanged there.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py at HEAD (pre-edit) show() call: 'AFTER (dated global objects at or before %s, source %s)' % (args.date, args.source)",
      "the edited file, after-path block: d_read is the explicit --date or the newest account-distribution key; the show() title argument is d_read"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Resolved in the cell at commit. Recorded because the title change is a step the order did not name; no number, key or exit code moves."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T14:41:00Z",
  "one_line": "The CN-n-1 QA drive ended RAISED, not with a Global refusal: a gold-plane ViewPlaneError on the inflection scope (the D1-W16-S1 raise family) aborted build_all before the manifest was written, so manifest errors read ['_drive'] and carry no 'global' entry.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (routes to 1.0.0_SA_CTO, the owner of the gold-plane read; the same hazard as MDPF_CANON-D1-W16-S1, which this row does not disarm)",
  "spec_asserts": "CN-n-1 Step 2 and FWD-3 third arm: on a one-firm Global pool build_all completes with status non-green, errors ['global'], writes 0 and blocked-calls 0, and the three firm scopes build as before.",
  "world_is": "Measured 2026-10-14T14:35Z-14:36Z by one dry-run drive (r7_cn_n_1.py drive, one run, not repeated). run/qa_run.json: status RAISED, manifest_errors keys ['_drive'] only, trigger null. run/qa_run.log: 'QA DRIVE: build_all raised ViewPlaneError: REFUSING EMIT for inflection' (gold-plane peers do not sum to total_aua beyond the one-cent rule; levels not copied here). That is the W16-S1 mechanism (a re-sum against a headline total, raised outside isolation), now reached on the inflection scope on the plant's as-of 2026-10-13 rather than on Global. Served prefixes before and after are byte-identical (cmp run/served_before.json run/served_after.json). No S3 write: run/s3_ops.json blocked [] and calls s3.GetObject 1369, s3.ListObjectsV2 1100.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json (status RAISED, manifest_errors ['_drive'])",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.log ('QA DRIVE: build_all raised ViewPlaneError')",
      "org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md row MDPF_CANON-D1-W16-S1 (the ARMED hazard this run reached)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "AC1 and AC2 were not run: the order's Step 3 says stop on them when build_all raises, and it did. The order stays open. The refusal arm is not demonstrated by this run. Served objects were not changed."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T14:41:00Z",
  "one_line": "The QA plant sets model_value to None on the one-firm lines without moving account_count, so the global cross-axis presence gate (v) fails Global's isolated scope with a CROSS-AXIS error, not the min-firms refusal the order names.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "r7_cn_n_1.py plant_single_firm_pool docstring: only model_value at the last-date index of the other firms' fold lines is set to None; nothing else moves. CN-n-1 Step 3: a refusal text other than the min-firms prefix is a finding about the guard or the plant.",
  "world_is": "run/qa_run.log: 'SCOPE FAILED (isolated): global -- AssertionError: CROSS-AXIS COHERENCE GATE FAILED (global)' with presence disagreement (v) on 2026-10-13 for two by_model lines whose model_value is None while account_count is set. The prefix 'GLOBAL MIN-FIRMS FOLD REFUSED' does not appear in the log. Whether guard_global_min_firms_fold ran before the cross-axis gate is not established here; its call site is mdpf_gold_consolidator.py:2943, directly after guard_global_served_identity at :2942.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.log (SCOPE FAILED (isolated) global line and the (v) block)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py (plant_single_firm_pool, the in-place model_value edit)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py:2942-2943 (build_all guard call order)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not repaired here: the plant and the instrument are read-only for this order. The issuer decides whether the plant must also move the count for the presence gate to read a clean one-firm day."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T14:41:00Z",
  "one_line": "On a RAISED drive the instrument's fallback manifest carries writes ['?'], so the run record reads writes=1 and the grade arm N6 (no manifest writes) would count a write that the call guard never saw.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-n-1 Step 2: the run expects writes=0 and blocked-calls=0; the bounds say no AWS write of any kind, by the run or by the worker, and the instrument blocks and records every non-read call.",
  "world_is": "run/qa_run.json manifest_writes is ['?']: r7_cn_n_1.py cmd_drive sets the fallback manifest 'writes': ['?'] when build_all raises (the placeholder is counted as one write in the printed line). run/s3_ops.json: blocked [] and only s3.GetObject 1369 and s3.ListObjectsV2 1100 are recorded, so no write-kind call reached the guard. The Tee logger also printed 'I/O operation on closed file' on interpreter exit (stderr only; the record files were written before it).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/s3_ops.json (blocked [] and the call counts)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json (manifest_writes ['?'])",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py:306 (the fallback manifest literal)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not repaired here: the instrument is read-only for this order. The served prefixes were byte-identical before and after the run, so the placeholder is a record-keeping defect, not a write."
}
```

```json
{
  "id": "MDPF_CANON-D1-W23-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~23",
  "surfaced_at": "2026-10-14T14:40:10Z",
  "one_line": "The worker face names this order's row ids MDPF_CANON-D1-W17-S<k>, but this worker's serial is 0.9.0_WK_MDPF_CANON~23; the row gate requires W{n} to equal the committing worker's suffix, so the rows are minted MDPF_CANON-D1-W23-S<k>.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Worker face section 5 (proof and rows): a row id on this project carries the dell1 infix MDPF_CANON-D1-W17-S<k>; the spawn rule: the allocator coordinate W{n} is the ~<n> of the serial, and the gate requires W{n} to equal the committing worker's suffix.",
  "world_is": "This worker's serial is 0.9.0_WK_MDPF_CANON~23 (worktree C:/dev/wk-canon-r7-23). The W17 in the face is a template value that does not match the serial. A W17 row would be refused by the gate from this worktree, so the rows minted by this worker are W23. Nothing else in the cell is affected.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "slot23_CN-j-1.md section 5: 'A row id on this project carries the dell1 infix: MDPF_CANON-D1-W17-S<k>'",
      "org/surprise_channel/schemas/investigation_item.schema.json id description: W{n} must equal the committing worker's suffix"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker. The issuer (2.0.0_SA_COO~D1) owns the face template; no cell content depends on the id number."
}
```
```json
{
  "id": "MDPF_CANON-D1-W23-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~23",
  "surfaced_at": "2026-10-14T14:40:10Z",
  "one_line": "The AC3 real-data arm reads 95 dated category-views gold objects (49financial 27, inflection 26, cottonwood 20, global 22), not the 91 the order measured on 2026-10-13 (26, 25, 19, 21); four dated objects were added between the cut and this run. The arm reads all of them and passes 6 of 6.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Worker face section 1 and the preflight: the four scopes hold 26, 25, 19 and 21 dated category-views objects (91) as measured 2026-10-13; AC3 reads 91 dated gold objects.",
  "world_is": "Read-only paginated listing of portal/gold/mdpf/{scope}/category-views/ in opal-data-assets on 2026-10-14 returns 27, 26, 20 and 22 dated objects (95 in total). The publisher and the issuer's arm both follow the live listing; no expectation in the code or the arm depends on the count.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_j_1.py real (R0 CONTROL: {'49financial': 27, 'inflection': 26, 'cottonwood': 20, 'global': 22}; R3 190 cells, 0 unequal)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker. Counts are read at the run date; the grown tree is expected for a daily fire, and the figures in the order are a 2026-10-13 measurement."
}
```

```json
{
  "id": "MDPF_CANON-D1-W23-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~23",
  "surfaced_at": "2026-10-14T14:44:05Z",
  "one_line": "The order's AC1-AC3 expect strings (ending '-- and exit=0') and the face's timeout 120 prefix cannot both be recorded verbatim: the check prints the summary line and the echoed exit line on separate lines, and the proof checker requires the recorded invocation to equal the criterion's text exactly.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Worker face section 4: each criterion's expectation reads 'ROUND 7 CN-J-1 <ARM>: n of n arms -- and exit=0', and each invocation runs under timeout 120. proof-of-spec-check.py: a PASS row's output_evidence must match expect, and the recorded invocation must equal the criterion's invocation modulo placeholders.",
  "world_is": "r7_cn_j_1.py prints 'ROUND 7 CN-J-1 UNIT: 6 of 6 arms' as one line and the shell echo 'exit=0' as the next line; no output line contains '-- and exit=0'. The first instance draft failed the checker on this and on the timeout prefix. The record now carries the criterion's invocation text exactly, and expect as the summary line then exit=0 with a whitespace span. The timeout 120 bound was applied at run time and is stated in session_log.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 at the first draft: 'does NOT match expect' x3 and 'invocation-alignment ... NOT the criterion's invocation' x3",
      "r7_cn_j_1.py unit/seam/real stdout (worktree 8ae1cfdafb + wk-MDPF_CANON-23 commit): final lines 'ROUND 7 CN-J-1 <ARM>: n of n arms' then exit=0 from the shell echo"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker. The issuer owns the face's expect wording; the record keeps the criterion text and the checker's matching rule decides the verdict."
}
```

```json
{
  "id": "MDPF_CANON-D1-W23-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~23",
  "surfaced_at": "2026-10-14T14:46:19Z",
  "one_line": "The commit-time naming gate WARNs on the new provenance URI f\"s3://{GOLD_BUCKET}/{dated[0][1]}\" at lambda_function.py:558 ('segment 1 {x} is neither a source nor a tier'). The same f-string shape exists unchanged at line 414 (_publish_one) and is not graded there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Worker face section 1 Step 1/2 and bounds: add no bucket, prefix or name; the publisher's serve keys are existing-pipeline f-strings, and the naming gate's non-application for an existing pipeline applies. CLAUDE.md section 4: every S3 address is lib/opal_naming.py output, R19 migration is per project.",
  "world_is": "The provenance source_keys entries reuse GOLD_BUCKET and the listed gold key, the same way _publish_one does (line 414). Commit 4e954e2d8b passed with the naming gate WARN (NAMING-GATE: WARN 1 graded). The WARN grades only added lines, so the existing pattern is graded only where it is newly typed. No new bucket, prefix or name is typed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit 4e954e2d8b: '[naming-gate] NAMING RAISE infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py:558 s3://{x}/{x} -> (rule or registry defect)'",
      "git show 8ae1cfdafb:infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py line 414: source_keys [f\"s3://{GOLD_BUCKET}/{src['key']}\"]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker. A naming-gate rule question for the LGIC owner; the existing publisher line is outside this cell and was not changed."
}
```
```json
{
  "id": "MDPF_CANON-D1-W18-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "The AUA Trend tooltip renderer has no null filter on its rows, so a Client chip carrying null on a non-as-of date is printed as a $0 row (source read; not rendered).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1c.7 and judgment AC4: a Client chip with a null value draws no bar or area segment and no tooltip row; if the tooltip prints $0 for a null, file a row.",
  "world_is": "portal/src/pages/ModelPortfolios.tsx renderTrendTooltip (line 1165 buckets = payload minus interp_total, no value filter; line 1195 value fmtVal(Number(entry.value)), and Number(null) is 0). recharts 3.7.0 combineTooltipPayload (node_modules/recharts/es6/state/selectors/combiners/combineTooltipPayload.js) pushes one tooltip entry per graphical item with no null filter; tooltipSelectors.js filters only the dataPoints, not the entries. Not rendered in a browser by this worker, so the $0 row is the source-read expectation for the round-7 render to confirm.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/pages/ModelPortfolios.tsx:1165 and :1195 (portal commit pending on wk-MDPF_CANON-18-portal)",
      "C:/dev/wk-canon-r7-18/portal/node_modules/recharts/es6/state/selectors/combiners/combineTooltipPayload.js (recharts 3.7.0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "CN-i-1 declares no AWS egress and bounds the worker to no AWS call, but its AC3 proof command is a data arm that performs read-only S3 gets; the worker ran it once, read-only.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 preflight EGRESS CLASS NONE (the worker reads no AWS and writes none); section 2 bound 3 'No AWS call of any kind'; section 4 AC3 'reads the SERVED inputs (read-only AWS gets)'.",
  "world_is": "r7_cn_i_1.py data issues get_object reads against opal-data-assets and a keys listing; it is the issuer's proof command and is named by AC3. The worker ran it once under timeout 120 as the criterion names it; no write, deploy or store call was made. The declared egress class and the bound do not describe AC3.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-i-1.aua-trend-grouping.md (face section 2 bound 3, preflight EGRESS CLASS, AC3)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_i_1.py (data subcommand, served() and keys_under())"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "The AUA Trend stack is specified to sum to opal_aggregate_aua to the cent, but the data arm passes with exact equality on only 24 of 487 valued dates and classes the rest as a model_aua rounding gap, with a worst residual far beyond cents.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1 item 6: the whole stack sums to opal_aggregate_aua to the cent (carve-outs drawn once), except on a fold-suppressed date.",
  "world_is": "r7_cn_i_1.py data, arm D1 (AC3 output, read-only, run at 0a06280a plus this worker's portal commit): 'stack == opal_aggregate_aua on 487 valued dates of 496: exact 24, model_aua rounding gap 463, fold-suppressed 0, failing 0'; the same line prints a worst residual in the billions of dollars. The arm passes on its own classification; the cent identity holds on 24 dates. Recorded, not adjudicated: the CVO grades FWD-9 (6).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "AC3 output line D1 (r7_cn_i_1.py data, exit 0, 5 of 5 arms)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_i_1.py (arm D1 classification)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "The task order names the bar and area fills for the new colours but not the area gradient defs, which resolve their own colour from the series label; the worker routed the gradient through the same colour resolver.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1c.6: the areas (:2239) prefer trendColorOf over getModelColor for the group series.",
  "world_is": "ModelPortfolios.tsx gradient defs (about line 2239) set the stop colour from getModelColor(s.label); each area fill is url(#gradient-<key>). Left alone, the Custom Models, ETF, ALT and Client areas would fill with the default gradient colour while their strokes take the group colour. The worker changed the gradient colour line to the same resolver as the area stroke (trendSeriesColor, then getModelColor). No other line changed for this.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/pages/ModelPortfolios.tsx:2239 (gradient colour) and :2324 (area stroke colour)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "The bar and area show chains admit a series only when its label is a model in trendModelOrder, so the Client chips would mount hidden; the worker added a show gate for them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1c.5: the Client chips are drawn on the as-of date and draw nothing on other dates; the chips mount in STACK_SERIES.",
  "world_is": "The show expression (ModelPortfolios.tsx about lines 2078 and 2321) ends in trendModelOrder.includes(s.label), which is false for 'Client Supervised' and 'Client Unsupervised', so a mounted Client series would be hidden on every date. Added: show = Global and hasClientChips (the as-of object carries a Client value). Per-firm stays hidden.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/pages/ModelPortfolios.tsx:2078 (bar show) and :2321 (area show)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S6",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "Relabelling the non_model band to 'Other AUA' would move its colour off the Non-Model silver if the label were resolved by getModelColor; the worker maps the band key to the Non-Model colour explicitly.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1c.3 relabels non_model to 'Other AUA' and keeps every other label on getModelColor; section 1c.6 keeps every other label on getModelColor.",
  "world_is": "getModelColor('Other AUA') is not a registered name (modelPortfolioColors.ts registers 'Non-Model' at line 128, primary #C3CADA). By the worker's read, an unknown name resolves to a deterministic palette entry, not null, so the relabel alone would repaint the band. trendSeriesColor maps key non_model to getModelColor('Non-Model').",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/lib/modelPortfolioColors.ts:128-130 (Non-Model primary) and :161-166 (fallback palette entries)",
      "C:/dev/wk-canon-r7-18/portal/src/pages/ModelPortfolios.tsx:155-157 (trendSeriesColor)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S7",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "Colour collision: the Client Unsupervised chip resolves to the same hex as the Ultra-Short Term model series.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 closing note: if a series' resolved colour equals another series' colour, file an OBSERVATION row naming both hex values; do not edit the colour registry.",
  "world_is": "Client Unsupervised resolves through l1ColorOf to PALETTE.orange500 = #f97316 (CategoryViewTree L1_COLOR). Ultra-Short Term resolves to MODEL_PORTFOLIO_COLORS primary #f97316 (modelPortfolioColors.ts:58). Same hex, two series. No other pair among the resolved trend colours is equal (Custom #d946ef, ETF #22d3ee, ALT #ff4f1f, Client Supervised #fbbf24, Other AUA #C3CADA).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/components/CategoryViewTree.tsx:93 (Client - Opal Unsupervised = orange500)",
      "C:/dev/wk-canon-r7-18/portal/src/lib/modelPortfolioColors.ts:58 (Ultra-Short Term primary #f97316)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S8",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "The provenance guard forbids a direct model_value read outside the paired accessor, so the carve-out lines are read through readModelSeries rather than from by_model.model_value as the task order words it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1c (carve-out memo): read the two carve-out lines from globalMdpfData.by_model.opal_div_sma / opal_growth_sma model_value, exposing them by period.",
  "world_is": "scripts/provenance-read-guard.mjs admits model_value reads only through src/lib/pairedProvenanceRead.ts; a direct read in the page fails the guard. The worker reads the same served values through readModelSeries(globalMdpfData, key).value keyed by period, with no arithmetic in the memo. The guard prints OK after the change.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/lib/pairedProvenanceRead.ts:162-170 and :548-571 (model_value read through the paired accessor)",
      "C:/dev/wk-canon-r7-18/portal/src/pages/ModelPortfolios.tsx:499-508 (globalCarveOutByPeriod)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W18-S9",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~18",
  "surfaced_at": "2026-10-14T14:45:34Z",
  "one_line": "The area tooltip sort list named 'Non-Model', which the relabel to 'Other AUA' would have dropped from the sort; the worker replaced it with the stack-order band names.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-i-1 section 1c.3 relabels the band; the task order is silent on the tooltip sort list.",
  "world_is": "trendModelOrderWithNonModel (ModelPortfolios.tsx line 937) appended 'Non-Model' to the area tooltip's sortOrder; sort keys are display names, so 'Other AUA' would sort after every model by the unknown-name default instead of its place. The list now carries the Client chips, 'Other AUA', 'ETF Strategies' and 'ALT Strategies' in stack order. The renderer's Non-Model branch (entry.name === 'Non-Model') is now unreachable and was left in place.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r7-18/portal/src/pages/ModelPortfolios.tsx:937-939"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W20-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~20",
  "surfaced_at": "2026-10-14T14:48:43Z",
  "one_line": "The worker face handed to CN-m-1 carries the issuer's RECORD FACE section (pre-read values, expected record shape, the four ANCHORS readers) under a marker that says it does not travel to the worker.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-m-1.staged-global-aggregate-reader-census.md@0c1a6cac3c lines 143-183: the RECORD FACE section (ISSUER NOTES, THE ISSUER'S PRE-READ, expected shape of the record); the same text is in the worker face file handed to the worker",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_m_1.py@0c1a6cac3c lines 30-35: ANCHORS, the four readers V2 requires the record to list"
    ]
  },
  "spec_asserts": "The census is written blind: the RECORD FACE does not travel to the worker (the order's own marker at its RECORD FACE section; the spine's L7 rule that the record face never travels).",
  "world_is": "The RECORD FACE was readable by the worker before grounding. No value from it is cited; every count in the record derives from this worker's own reads. The anchors are known to the worker, so V2 can be met by listing them and cannot tell a blind census from a sighted one. Pre-read counts (universe 28 of 8,831; staged ETag and size) also differ from this worker's live reads (universe 28 of 8,812), which is why no pre-read value was used.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed so the CVO can grade AC3 and the round-7 close knowing the census was not blind. The worker has not altered the check, the order or the RECORD FACE."
}
```

```json
{
  "id": "MDPF_CANON-D1-W20-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~20",
  "surfaced_at": "2026-10-14T14:48:43Z",
  "one_line": "The pre-read says the publisher and egress-publisher roles both cover the staged key; Terraform and the live publisher Lambda config disagree on which role the portal publisher runs as, and only the portal-publisher role's Terraform grants the key.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda get-function-configuration --function-name opal-assets-mdpf-portal-publisher: Role opal-assets-mdpf-egress-publisher-role, LastModified 2026-10-09T22:21:52Z",
      "infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf:45,89-90: role opal-assets-mdpf-portal-publisher-role with GetObject on gold/mdpf_revamp/*",
      "infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf:85,171-172: egress role GetObject on portal/gold/mdpf/* only; no gold/mdpf_revamp grant",
      "comp-iam simulate opal-assets-mdpf-egress-publisher-role s3:GetObject on the staged key --no-control: STATE NOT-DECIDABLE (s3:prefix missing from the context)"
    ]
  },
  "spec_asserts": "Pre-read: the publisher and egress-publisher roles both cover gold/mdpf_revamp/* (issuer notes, IAM bullet).",
  "world_is": "The live publisher runs as the egress role, whose Terraform does not grant the staged key. The portal-publisher role's Terraform grants the key but is not the live Lambda role. The publisher code reads portal/gold/mdpf/ only, so the reach of the code is unchanged.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "CN-m-1 records the portal-publisher role in iam_static (grant present) and the egress role in iam_live (NOT-DECIDABLE, not a deny)."
}
```

```json
{
  "id": "MDPF_CANON-D1-W20-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~20",
  "surfaced_at": "2026-10-14T14:48:43Z",
  "one_line": "Two repo notes give the accrual bridge fire time as 14:10Z and 15:45Z; the live schedule mdpf-accrual-bridge-daily is cron(40 13 * * ? *), 13:40Z.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/EC2_MANIFEST.json:482 (accrual_bundle note: mdpf-accrual-trigger 14:10Z UTC scheduler)",
      "infra/aws/terraform/mdpf-pipeline/CHANGELOG.json:23 (Scheduler cron(45 15)Z)",
      "aws scheduler get-schedule --name mdpf-accrual-bridge-daily: ScheduleExpression cron(40 13 * * ? *), State ENABLED"
    ]
  },
  "spec_asserts": "The accrual bridge leg fires at 14:10Z (EC2 manifest note at infra/aws/ec2/EC2_MANIFEST.json:482).",
  "world_is": "The live schedule fires at 13:40Z. CN-m-1 uses the live time. The repo notes are stale.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W20-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~20",
  "surfaced_at": "2026-10-14T14:48:43Z",
  "one_line": "aws s3api get-bucket-logging returns empty stdout with rc 0 on every opal-data bucket sampled, so server access logging reads as absent, with no in-estate positive case of a LoggingEnabled block to control the call shape.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-logging --bucket opal-data-assets --output json: rc 0, 0 bytes of stdout",
      "same call on opal-data-bd, opal-data-cot, opal-data-inf, opal-data-49financial, opal-data-portal-v2: rc 0, 0 bytes each",
      "aws s3api get-bucket-location --bucket opal-data-assets --output json (same shim): rc 0, 38 bytes, LocationConstraint null"
    ]
  },
  "spec_asserts": "server_access_logging is true only if the logging call returns a LoggingEnabled block; an empty object means none (CN-m-1 Step 1, trail).",
  "world_is": "The empty result is recorded as false per the spec. No sampled bucket returned a LoggingEnabled block, so the call shape has no observed positive case here. The false value is an absence, not an exercised negative (ABSENT != EXERCISED-AGAINST).",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W20-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~20",
  "surfaced_at": "2026-10-14T14:48:43Z",
  "one_line": "The code universe scan (suffix and literal-key match) cannot see a reader whose key comes from a config row: .tools/comp-freshness GETs the staged key in content mode from served_freshness_config.yaml:115 and names no literal key.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/comp-freshness:1090-1097 (_fetch_object_doc runs s3 cp on the config's s3_key_prefix); :1119 is its call under as_of content mode",
      "data/served_freshness_config.yaml:115 (s3_key_prefix of mdpf_leg_gold_revamp_staging_aggregate, as_of_field as_of_last)",
      "check universe mode at HEAD 0c1a6cac3c: 28 files naming both strings; comp-freshness is absent (no .py suffix, no literal key)"
    ]
  },
  "spec_asserts": "The code class is the repo's consumers found by the universe scan (CN-m-1 Step 1, code).",
  "world_is": "A config-driven reader exists outside the scan and is listed by hand in CN-m-1. The scan method cannot show that no other config-driven reader exists.",
  "disposition": "UNDER_INVESTIGATION"
}
```


```json
{
  "id": "MDPF_CANON-D1-W17-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~17",
  "surfaced_at": "2026-10-14T14:42:41Z",
  "one_line": "The order's premise that the served frontier cell is the 2026-10-09 roster does not hold at filing: the live comparator reads served objects at as_of_last 2026-10-13.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-h-1 (face section 1) names the served 2026-10-09 frontier counts as the 2026-08-17 roster wearing a 2026-10-09 date, and AC3 reads those served objects.",
  "world_is": "r6_cn_h_1.py comparator at 2026-10-14 on box/dell1, worktree HEAD 7df957722b: K0 reads served objects with as_of_last 2026-10-13; served frontier counts equal the staged roster on 17 of 17 mapped keys (the freeze holds on the 10-13 cell); K1 at axis 2026-10-13 returns as-of 2026-10-13 for global, 49financial and inflection. The served cell is dated 10-13, not 10-09. The freeze finding stands; only the date named in the order differs.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r6_cn_h_1.py comparator (K0 and K1 lines, exit 0)",
      "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py@7df957722b load_account_dist_frontier_counts (A4 selection, WARN on no qualifying key)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker at AC3 for the issuer (2.0.0_SA_COO~D1). The round-7 AC4 judgment is graded on the objects after the first scheduled run that carries the code."
}
```

```json
{
  "id": "MDPF_CANON-D1-W17-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~17",
  "surfaced_at": "2026-10-14T14:42:41Z",
  "one_line": "data/mdpf/scripts/gold/tests/test_global_fold_flag2.py replaces the module-level loader with a stub and never restores it, so every later test in the same pytest process reads the stub.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A test of the loader exercises the real function and reads the A4 objects through an injected fake S3 client (CN-h-1 step 4, idiom of test_global_served_identity.py).",
  "world_is": "test_global_fold_flag2.py line 46 (_stub) assigns spine.load_account_dist_frontier_counts = lambda ... at module level with no monkeypatch. Run in one process with test_canplat_p1_1.py and data/mdpf/tests/canon/, six tests of the new file failed (KeyError and DID NOT RAISE) before the new file pinned the real function with an autouse fixture. After the pin the combined run shows only the three pre-existing flag2 reds (MDPF_CANON-D1-S1).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest -q data/mdpf/scripts/gold/tests/test_canplat_p1_1.py data/mdpf/scripts/gold/tests/test_global_fold_flag2.py data/mdpf/tests/canon/ (6 failed before the pin; 3 failed after, all pre-existing)",
      "data/mdpf/scripts/gold/tests/test_global_fold_flag2.py@7df957722b:46 (_stub)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker. The stub is not in this order's paths; its owner is the global fold's test owner. The new file does not depend on the stub's absence."
}
```


```json
{
  "id": "MDPF_CANON-D1-W17-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~17",
  "surfaced_at": "2026-10-14T14:47:25Z",
  "one_line": "The commit-time naming gate refuses the A4 account-distribution key the face prescribes (a new literal portal/gold/mdpf/{x}/account-distribution/ prefix, out of the canonical portal pattern); the order's code cannot land without a registry row or an R20 entry that is outside this order's paths.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-h-1 step 1 (face) names the key portal/gold/mdpf/{scope}/account-distribution/<date>.json as the loader's source; CLAUDE.md rule 30 requires every S3 address to be lib/opal_naming.py address() output and a builder refusal to be a missing registry row, never a hand-typed workaround.",
  "world_is": "safe-commit at 0.9.0_WK_MDPF_CANON~17 on wk-MDPF_CANON-17 (HEAD 7df957722b) refused: NAMING REFUSE data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:798 portal/gold/mdpf/{x}/account-distribution/ -> portal/{scope}/gold/mdpf/{x}/account-distribution/ (NEW and OUT-OF-PATTERN as S3Key; LGIC_ENFORCE ENFORCE mode). lib/opal_naming.py has no builder for the portal A4 home (its portal functions cover firm-access and display maps only). The pre-existing line 694 carries the same shape and is not refused because it is not new. The worker did not rewrite the key to evade the gate. The loader change, the two stub edits and the new test file are uncommitted in the worktree; AC1-AC3 PASS on that tree (reader 8 of 8, seams 4 of 4, comparator 5 of 5).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit -F .scratch/msg1.txt -- <four paths> at 0.9.0_WK_MDPF_CANON~17 (rc=1; NAMING-GATE: REFUSE 1 graded, line 798)",
      "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py@7df957722b:694 (pre-existing portal/gold/mdpf/{served_firm_id}/aggregate-aua-timeseries/ prefix, not new)",
      "lib/opal_naming.py@7df957722b (no portal A4 address builder; grep of portal names returns firm-access and display-map entries only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the worker as a BLOCKING row. Resolution owner: 2.0.0_SA_COO~D1 with the CTO -- either a naming registry row under infra/logic/registry/ (outside this order's paths) or an R20 register entry Andrew acknowledges. The order's status stays pending until the code lands."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T15:04:10Z",
  "one_line": "The corrected CN-n-1 QA drive (re-seated run, one drive) did not refuse Global on the min-firms guard: manifest_errors.global reads 'AssertionError: CROSS-AXIS COHERENCE GATE FAILED (global) -- REFUSING TO EMIT' with presence disagreement (v), so the refusal arm the order names is not demonstrated.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-n-1 Step 2 and FWD-3 third arm: on a one-firm Global pool build_all completes with status non-green, errors ['global'], writes 0 and blocked-calls 0, and manifest_errors.global carries the prefix 'GLOBAL MIN-FIRMS FOLD REFUSED:'. CN-n-1 Step 3: a refusal text other than the min-firms prefix is a finding about the guard or the plant; keep the record, file a row, stop on AC1.",
  "world_is": "Measured 2026-10-14T14:59Z-15:02Z by one drive (r7_cn_n_1.py drive, one run into run/, after selftest OK and plan planted true). run/qa_run.json: status non-green, errors ['global'], a4_objects_built 12 of 16, writes 0, blocked-calls 0 (run/s3_ops.json blocked []). manifest_errors.global (exact first line): 'AssertionError: CROSS-AXIS COHERENCE GATE FAILED (global) -- REFUSING TO EMIT', then '(v) presence disagreement: 2 across 1 date(s)' naming two by_model lines on 2026-10-13 with model_value None and account_count set. run/qa_run.log: 'SCOPE FAILED (isolated): global -- AssertionError: CROSS-AXIS COHERENCE GATE FAILED (global)'; the string 'GLOBAL MIN-FIRMS FOLD REFUSED' does not appear. AC1 grade: 4 of 6 arms, rc=1 (N2 and N5 FAIL). AC2 served 4 of 4 and AC3 guard control 5 of 5 PASS. The min-firms guard is therefore not shown to run before the cross-axis gate in this build.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json (manifest_errors.global, status non-green, writes 0)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.log (line 'SCOPE FAILED (isolated): global -- AssertionError: CROSS-AXIS COHERENCE GATE FAILED')",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py (cmd_drive plant call, blank_counts=True at line 297)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py (build_all guard call order: guard_global_served_identity then guard_global_min_firms_fold, as recorded in MDPF_CANON-D1-W21-S2)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the re-seated worker. Not repaired here: the plant, the instrument, the guard and the consolidator are read-only for this order. The record is QA and not production evidence. Resolution owner: 2.0.0_SA_COO~D1 (decides whether the plant must also reach the presence gate, see MDPF_CANON-D1-W21-S2 and -S5). The order's status stays pending; AC1 is FAIL."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T15:04:10Z",
  "one_line": "Amendment 1 says the corrected plant blanks account_count with model_value, but on the re-seated drive the presence gate still read account_count set on the two blanked by_model lines.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-n-1 AMENDMENT 1 (issuer, 2026-10-14 ~15:0xZ): the plant now edits deep COPIES for the Global builder only and blanks the count with the value; a RAISED run records writes []. The corrected plant is expected to let the cross-axis presence gate read a clean one-firm day.",
  "world_is": "The worktree HEAD instrument calls plant_single_firm_pool(..., blank_counts=True) for the drive (r7_cn_n_1.py line 297) and the plant record reads planted true, lines_blanked 2, fold_lines 9, kept_firm cottonwood, blanked_firms inflection. Yet the run's cross-axis presence gate (v) reports the same two by_model lines with model_value None and account_count still set, so the count blanking did not reach the gate's read in this drive. The cause is not established here: the blanking is guarded by isinstance(account_count, list) at line 121, and that condition and the index mapping were not examined. This repeats the mechanism of MDPF_CANON-D1-W21-S2 on the corrected instrument.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py (plant_single_firm_pool lines 94-122, blank_counts guard at 121; cmd_drive call at 297)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json (plant record; manifest_errors.global presence disagreement)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.log (presence disagreement (v) block)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the re-seated worker as an observation of the premise, not a repair. The issuer owns the plant. Related: MDPF_CANON-D1-W21-S2 (same mechanism, first run) and MDPF_CANON-D1-W21-S4 (the AC1 consequence)."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S6",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T15:16:03Z",
  "one_line": "The third (last) QA drive was not refused by the min-firms guard: manifest errors.global carries the spine composition gate text, the guard prefix GLOBAL MIN-FIRMS FOLD REFUSED is absent from the log, and AC1 grades FAIL at 4 of 6 arms.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-n-1 Step 2 and Step 3 (AMENDMENT 2): the drive is expected to end status=non-green with errors=['global'] and the Global refusal to be the min-firms guard, prefix GLOBAL MIN-FIRMS FOLD REFUSED, naming the as-of and '1 firm(s)'; AC1 expects 6 of 6 arms.",
  "world_is": "The drive ran once (qa_run.json status non-green, errors ['global'], writes 0, blocked-calls 0, plant planted true, kept cottonwood, blanked inflection, 2 lines, 9 fold lines, as-of 2026-10-13). The recorded manifest_errors.global text is: 'SystemExit: GLOBAL COMPOSITION GATE FAILED: 0 partial-row, 0 headline-identity, 0 49F-leg, 0 inflection-leg, 1 band/total violation(s) across 496 dates -- refusing to emit (the P0 2026-07-22 class).' The log carries FATAL 2026-10-13 (sum of by_model cohort=model differs from model_aua beyond rounding-order tolerance) before that SCOPE FAILED line, and no GLOBAL MIN-FIRMS line. Order of execution in build_all: the Global build call is inside _fold (consolidator line 2833, invoked at 2836), and guard_global_min_firms_fold runs later at line 2943. The plant is applied inside the builder call (r7_cn_n_1.py lines 293-300), so the composition gate refused before the min-firms guard was reached. The composition mismatch is consistent with the plant editing model_value without the model_aua headline moving, which is not established here. AC3 (the guard control on unplanted and planted 2026-10-09 objects) passes 5 of 5, so the guard itself folds and refuses on a planted pool when called on it. AC1 grades 4 of 6 (N2 and N5 FAIL). AC2 serves 4 of 4 (identical snapshot before and after, 2 distinct call kinds, none a write).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json (manifest_errors.global text; status non-green; writes []; plant record)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.log (FATAL line and SCOPE FAILED global line near 15:14:25Z; QA PLANT line)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py@8e6711f9f3 (build_all _fold at lines 2825-2836; guard_global_min_firms_fold call at line 2943; _GLOBAL_FOLD_REFUSE prefix at line 2064)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py (planted_build_global lines 293-301; plant_single_firm_pool fill=0.0 at lines 94-126)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the third seat on the last drive of this order (AMENDMENT 2). No re-drive was made, per the order. The record is QA and not production evidence. Resolution owner: 2.0.0_SA_COO~D1 (decides whether the plant must sit ahead of the composition gate, or the guard arm must be driven by a different route). The order status stays pending. Related: MDPF_CANON-D1-W21-S2, -S4, -S5."
}
```

```json
{
  "id": "MDPF_CANON-D1-W21-S7",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~21",
  "surfaced_at": "2026-10-14T15:26:32Z",
  "one_line": "The QA drive of the refusal arm exited 0 with the expected record, but the interpreter printed two 'Exception ignored while finalizing file <__main__._Tee>' tracebacks (ValueError: I/O operation on closed file, in _Tee.flush) after the 'QA run done' line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CN-n-1 Step 2: the drive prints one 'QA run done' line and the run is expected to end with status=non-green, errors=['global'], writes=0, blocked-calls=0. The order does not name the process teardown output.",
  "world_is": "The drive printed the QA run done line (status=non-green errors=['global'] a4_objects_built=12 writes=0 blocked-calls=0), then two tracebacks from the instrument's stdout tee at teardown (ValueError: I/O operation on closed file, raised from _Tee.flush at r7_cn_n_1.py line 270). The process exit code was 0. qa_run.json and qa_run.log carry the expected record; the refusal text is the min-firms guard prefix; the three grade, served and guard criteria read from that record unchanged.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py@82308151da (class _Tee, flush at line 270)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json (status non-green, errors global, writes 0; the record the teardown did not change)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the fourth seat (0.9.0_WK_MDPF_CANON~21, AMENDMENT 3 drive). Observation of the instrument's teardown only; the record is complete and the run's exit is 0. The instrument is read-only for this order; resolution owner: 2.0.0_SA_COO~D1. The refusal itself matched the expected min-firms prefix (see the proof instance, AC1 6 of 6)."
}
```

```json
{
  "id": "MDPF_CANON-D1-W24-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~24",
  "surfaced_at": "2026-10-14T19:20:16Z",
  "one_line": "The face says read portal/CONTRIBUTING-BOXES.md before touching portal/, but that file is not on the candidate branch at its head 34cd12d2.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Face section 1 preamble and the portal rule: read portal/CONTRIBUTING-BOXES.md before any change under portal/. The base is the candidate branch cand/dell1/mdpf-canon-aua-trend-groups-and-as-of at head 34cd12d2.",
  "world_is": "git -C portal ls-tree HEAD lists no CONTRIBUTING-BOXES.md at 34cd12d2. The file exists at 07f065e6 (NFRA_DEVPLN DP-b-4) and is reachable from PROD and other cand/dell1 branches. The worker read it with git show from 07f065e6 after the edits and before the commit, read-only. Its rule is unchanged.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@34cd12d2 git ls-tree HEAD --name-only: no CONTRIBUTING-BOXES.md (read 2026-10-14 in the worktree C:/dev/wk-canon-r7-24/portal)",
      "portal@07f065e6 CONTRIBUTING-BOXES.md (introducing commit; git show read-only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by 0.9.0_WK_MDPF_CANON~24 on the CN-i-2 drive. Form only. Resolution owner: 2.0.0_SA_COO~D1."
}
```

```json
{
  "id": "MDPF_CANON-D1-W24-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~24",
  "surfaced_at": "2026-10-14T19:20:16Z",
  "one_line": "Face section 5.1 names git -C portal commit for the nested portal repository; CLAUDE rule 14a and the NEVER list refuse a bare git commit, so the commit went through safe-commit.sh run from the portal directory.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Face section 5.1 step 1: commit the four portal files with git -C <worktree>/portal commit --author ... -F <msgfile>. CLAUDE rule 14a: commit via .tools/safe-commit.sh; NEVER a bare git commit.",
  "world_is": "The commit was made with bash ../.tools/safe-commit.sh run from the portal directory, so the portal repository was the commit target. Same author string, a Write-tool message file, the four paths named. Result: commit 71ed7393 on wk-MDPF_CANON-24-portal, 4 files, 40 insertions, 3 deletions; msg-verify MATCH. No bare git commit was run.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@71ed7393 (LOCAL on wk-MDPF_CANON-24-portal), safe-commit output: committed, msg-verify MATCH len=1357",
      "CLAUDE.md rule 14a and the NEVER list: commit via safe-commit.sh, never a bare git commit"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by 0.9.0_WK_MDPF_CANON~24. The face's git -C form and the CLAUDE rule differ for a nested repo; the safe-commit form was taken. Resolution owner: 2.0.0_SA_COO~D1."
}
```

```json
{
  "id": "MDPF_CANON-D1-W24-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~24",
  "surfaced_at": "2026-10-14T19:20:16Z",
  "one_line": "The commit gates read none of the four .ts/.tsx portal files; the risk reflex answered PARTIAL_OR_BLIND on a stale danger map.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1",
  "spec_asserts": "CLAUDE rules 14 and 14a: every commit passes the commit gates. Face section 5.1: if a portal hook refuses, file a row. The face names no frontend gate and no typecheck.",
  "world_is": "The output of commit 71ed7393 reads: commit-gate WARN 'checked 0 of 4 file(s) -- NOTHING WAS CHECKED' (the gate reads only .py/.sh/.tf and org/projects JSON); comp-pulse risk-reflex ANSWER STATE PARTIAL_OR_BLIND, danger map STALE at 212.9h, scanned 0 of 4, and the tool ran from the base checkout's path because the portal carries no .tools. The four frontend files reached the repository with no gate read. The worker's own bun run typecheck (tsc -b --noEmit) returned rc=0; it is not a gate.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@71ed7393 safe-commit output: '[commit-gate] WARN: commit-gate checked 0 of 4 file(s) -- NOTHING WAS CHECKED' and '[risk-reflex] ANSWER STATE: PARTIAL_OR_BLIND'",
      "portal/package.json script typecheck = tsc -b --noEmit (read-only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: left alone, every portal .ts/.tsx commit passes the commit-time gate unread. The worker changed no gate (outside its paths). Disarm owner 2.0.0_SA_COO~D1 routes gate coverage for portal frontend files. Filed by 0.9.0_WK_MDPF_CANON~24."
}
```

```json
{
  "id": "MDPF_CANON-D1-W24-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~24",
  "surfaced_at": "2026-10-14T19:20:16Z",
  "one_line": "The face gives the new Trend detail note the class text-white/60, which the portal colour law lists as illegal on the canvas and on white panels.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Face section 1d(iii): the note paragraph className is '-mt-3 mb-4 text-xs text-white/60', verbatim. Portal CLAUDE.md colour law: text-white* is illegal on the canvas (#F4F6FA) and on white panels, legal only on the band (#0A1733).",
  "world_is": "The sibling window paragraph directly above the note, in the same Trend block of ModelPortfolios.tsx, carries the same text-white/60 idiom, so the note inherits its ground. The worker did not render and did not measure the ground the Trend block sits on. The face's class was kept verbatim.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@71ed7393 src/pages/ModelPortfolios.tsx: the added note paragraph carries className text-xs text-white/60 (the sibling window paragraph carries the same idiom)",
      "portal/CLAUDE.md section 'Color law' (read-only): text-white* illegal on canvas and white panels"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only. The judgment grader (AC4, round close) reads the rendered ground. Filed by 0.9.0_WK_MDPF_CANON~24."
}
```

```json
{
  "id": "MDPF_CANON-D1-S25",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T20:00:00Z",
  "one_line": "On the Model Portfolios page (Global, as-of 2026-10-13) the Client card reads $292.26M while the Client drill-down it opens reads $341.10M ($2.20M Supervised + $338.89M Unsupervised); the card is the one that adds to the $2.18B Total.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "3.0.0_SA_CVO read tmp/ui-walk/20261014T193640Z/shots/006--portfolios-select-0-Global-All-.png: Total $2.18B; Models $1.83B; SMAs $50.75M; Client $292.26M",
      "3.0.0_SA_CVO read tmp/ui-walk/20261014T193640Z/shots/014--portfolios-open-Client-Client-directed-.png: header $341.10M; Supervised $2.20M; Unsupervised $338.89M",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/CN_I_2_REPAIR_RENDER_20261014.md 'Observed, not caused by this repair' (the issuer saw it and filed no row)"
    ]
  },
  "spec_asserts": "One figure per category on one page and one as-of: a drill-down's header equals the card that opens it (the Total Assets breakdown; the drill-down's own footnote says the categories equal total AUA).",
  "world_is": "The two numbers differ by $48.84M on the same page and as-of. $1.83B + $50.75M + $292.26M is about the $2.18B Total, so the drill-down's $341.10M is the one that does not tie. The drill-down is client-facing on PROD today, independent of the CN-i-2 candidate (the repair touches only its colour). The cause is not read: the two figures may come from different category-views fields, or one may carry SMA assets the other subtracts.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1"
}
```

```json
{
  "id": "MDPF_CANON-D1-S26",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T20:05:00Z",
  "one_line": "round-close-check cannot see a re-grade: it sorts ADJUDICATION_v*.md as strings (v1, v10, v11, v12, v2 ...) and returns the FIRST CVO-kind verdict it finds, so a later MET for CN-i-1 AC4 can never replace D1-C-S73's NOT MET in v10.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/round-close-check.py:118-119 glob returns sorted(glob.glob(pattern)) (string order); grade_criterion returns on the first CVO-kind non-doer row with a verdict word",
      "3.0.0_SA_CVO round-close-check --project MDPF_CANON --round 7 after ADJUDICATION_v12 (HELD) was written: 'TO-CN-i-1 AC4 -> GRADED (adjudication row MDPF_CANON-D1-C-S73 ... (verdict NOT MET))'"
    ]
  },
  "spec_asserts": "Spine L9: the CVO's grade of a judgment criterion is the one round-close-check reads; a re-grade after a repair replaces the earlier verdict.",
  "world_is": "The first verdict in string-sorted file order wins, so a repaired criterion stays NOT MET in the gate forever, and a round that needs it MET cannot read MAY-CLOSE. String order also misplaces v10+ against v2..v9 for any project past nine adjudications.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "0.0.0_AB_MSTR~DELL1"
}
```

```json
{
  "id": "MDPF_CANON-D1-S27",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T20:55:00Z",
  "one_line": "Per-firm MDPF leaves are reachable by ANY authenticated login: /api/general/mdpf/* is rewritten to platinum/mdpf/* behind the JWT check alone, with no firm scoping, so a demo-tenant or partner login can fetch another firm's per-firm series (e.g. /api/general/mdpf/49financial/...) by URL.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-routes behaviors: '/api/general/*' -> S3-opal-data-portal-v2-json [AUTH] [ROUTER]; viewer-request auth-validator-edge, origin-request public-data-router",
      "infra/aws/lambda-edge/public-data-router/index.mjs:51-54: '/api/general/mdpf/' -> '/platinum/mdpf/' rewrite, no firm check",
      "infra/aws/lambda-edge/auth-validator-edge/aggregate_gate.mjs:24-27: the only firm gate on the /api/general/* paths is AGGREGATE_PATHS (opal_aggregate.json)",
      "portal origin/PROD src/pages/ModelPortfolios.tsx:240: the page interpolates the firmId into /api/general/mdpf/{firmId}/... (the client chooses the path)"
    ]
  },
  "spec_asserts": "Firm data separation (CLAUDE.md section 5; MDPF_CANON FWD-3): a partner or demo login sees no other firm's data; the CTO's v2.20 note (msg 5867) states the demo tenant 'cannot reach those values through the page or the API'.",
  "world_is": "From source, the separation is enforced only in the page (effectiveFirmId), not at the edge for the mdpf family: the per-firm leaves under platinum/mdpf/{firm}/ answer any valid JWT. NOT read: the deployed bytes of the two edge functions (read from repo source) and a live request with a partner token. v2.20's Global-leaf fold is correct in itself; this row is the pre-existing route gap its premise leans on.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "1.0.0_SA_CTO~DELL1"
}
```

```json
{
  "id": "MDPF_CANON-D1-W28-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~28",
  "surfaced_at": "2026-10-14T21:42:39Z",
  "one_line": "CN-q-1 commit refused by the LGIC naming limb: the new edge module infra/aws/lambda-edge/auth-validator-edge/mdpf_gate.mjs carries the firm names 49financial, inflection and cottonwood as literals (lines 40-42), refused as hand-kept carriers outside every permitted context; nothing committed on wk-MDPF_CANON-28; the three criteria pass on the uncommitted worktree.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh rc=1 at HEAD 0e60da2afb for infra/aws/lambda-edge/auth-validator-edge/{mdpf_gate.mjs,index.mjs,tests/mdpf_gate.spec.mjs}: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.'",
      "[naming-gate] NAMING REFUSE mdpf_gate.mjs:40 49financial -> lookup('49financial'); :41 inflection -> lookup('inflection'); :42 cottonwood -> lookup('cottonwood'); NAMING-GATE: REFUSE 3 graded (DENOMINATOR 3 path(s))",
      "git status after the refusal: index.mjs M (unstaged, 18 insertions), mdpf_gate.mjs and tests/mdpf_gate.spec.mjs untracked, git diff --cached empty",
      "harness r9_cn_q_1.py on the worktree (uncommitted): handler 14 of 14 arms exit=0; seam 5 of 5 arms exit=0; control 5 of 5 arms exit=0"
    ]
  },
  "spec_asserts": "Order CN-q-1 worker face: step 1 says mdpf_gate.mjs may copy the issuer reference verbatim and imports nothing; the firm map (49financial, inflection, cottonwood, demo to global) is the page's own map and is written as literal strings; section 3 grants write on exactly the three product files. No clause names a naming-gate lookup or a registry row.",
  "world_is": "The LGIC naming limb (ENFORCE) refuses the three firm-name literals in the new edge module and refuses the commit. The route its message names, lookup(), is the Python naming library, which the import-nothing .mjs edge module cannot call; a registry row or an R20 register entry lies outside the order's paths. The worker did not edit the gate, bypass it, or rename the literals.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Left ARMED by this row: the leak S27 (MDPF_CANON-D1-S27, disarm 1.0.0_SA_CTO~DELL1), which this cell closes once it lands. This row does not change S27's standing."
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "CN-i-3 site 2 (trendModelOrderWithNonModel) cannot take the recipe: PROD's line is a call argument with a trailing comma, so the Global Trend is left at the feature text there.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 src/pages/ModelPortfolios.tsx trendModelOrderWithNonModel (feature text, unchanged)",
      "git -C portal show 5ab67a65:src/pages/ModelPortfolios.tsx: line '() => [...trendModelOrder, 'Non-Model'],' (PROD)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 FAIL: 24 PROD line(s) removed; 16 missing at HEAD (this line among them)"
    ]
  },
  "spec_asserts": "Face recipe: Global takes PROD text, other scopes the feature text; each text on its own lines; ? and : on lines of their own (face section 1). Site 2: Global gets [...trendModelOrder, 'Non-Model'] (PROD line '() => [...trendModelOrder, 'Non-Model'],'), other scopes the feature's list.",
  "world_is": "The PROD line ends with a comma inside useMemo(...). A conditional whose ? and : sit on their own lines cannot carry that comma without a syntax error, so the site was NOT edited and keeps the feature list at every scope (portal@19494a76 ModelPortfolios.tsx, the useMemo beside 'const trendModelOrderWithNonModel'). Check P1 lists this line missing at HEAD.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-cut the site, or refuse portal 19494a76 as the CN-i-3 candidate until it is re-cut)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "CN-i-3 site 3 (timeSeriesData memo) cannot take the recipe: PROD's line is a return statement, so Global still gets the custom-model grouping.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 src/pages/ModelPortfolios.tsx timeSeriesData useMemo (feature text, unchanged)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 missing list includes the PROD return line"
    ]
  },
  "spec_asserts": "Face recipe: Global takes PROD text, other scopes the feature text; each text on its own lines; ? and : on lines of their own (face section 1). Site 3: Global gets rollBlendsIntoArchetypeSeries(timeSeriesDataRaw.by_model) alone; other scopes keep groupCustomModelsSeries(rolled, new Set(MODEL_ORDER)).",
  "world_is": "The PROD line 'return { ...timeSeriesDataRaw, by_model: rollBlendsIntoArchetypeSeries(timeSeriesDataRaw.by_model) }' starts with the return keyword, which cannot sit inside a ? : expression on its own line. The site was NOT edited (portal@19494a76, the timeSeriesData useMemo); Global still runs groupCustomModelsSeries there. Check P1 lists the line missing.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-cut the site, or refuse portal 19494a76 as the CN-i-3 candidate until it is re-cut)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "CN-i-3 site 4 (tooltip buckets) cannot take the recipe: PROD's line is a const declaration, so Global still runs presentTrendEntries in the tooltip.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 src/pages/ModelPortfolios.tsx renderTrendTooltip 'const buckets = presentTrendEntries(...)' (feature text, unchanged)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 missing list includes 'const buckets = payload.filter(...)'"
    ]
  },
  "spec_asserts": "Face recipe: Global takes PROD text, other scopes the feature text; each text on its own lines; ? and : on lines of their own (face section 1). Site 4: Global gets payload.filter((entry) => entry.dataKey !== 'interp_total'); other scopes keep presentTrendEntries(...).",
  "world_is": "The PROD line is 'const buckets = payload.filter(...)'. The declaration keyword and name cannot be placed inside a ? : branch on their own lines, and a block form is not the recipe. The site was NOT edited (portal@19494a76, renderTrendTooltip). Check P1 lists the line missing.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-cut the site, or refuse portal 19494a76 as the CN-i-3 candidate until it is re-cut)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "CN-i-3 site 8 (quarterly bars and daily area data points) cannot take the recipe: PROD and feature lines are assignment statements, so Global keeps the feature's data points.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 src/pages/ModelPortfolios.tsx bar and area data-point blocks (feature text, unchanged)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 missing list includes the PROD assignment lines and their comments"
    ]
  },
  "spec_asserts": "Face recipe: Global takes PROD text, other scopes the feature text; each text on its own lines; ? and : on lines of their own (face section 1). Site 8: Global gets PROD's nmKey, sma_additive and Client data-point assignments (the 'dataPoint[nmKey] =' and 'dataPoint['sma_additive'] = addPt?.smaAdditiveAua ?? null' lines, plus their PROD comments); other scopes keep the feature's.",
  "world_is": "Each PROD and feature line is a full assignment statement ('dataPoint[...] = ...'), and the feature's line is also a whole statement. No ? : expression on its own lines carries both, so both data-point sites (bars and area) were NOT edited. Global keeps the feature's Other AUA, ETF and Client values there. Check P1 lists 6 such lines missing (the two comment pairs and the four assignment lines).",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-cut the site, or refuse portal 19494a76 as the CN-i-3 candidate until it is re-cut)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S5",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "CN-i-3 site 10 (bar fill) cannot take the recipe: PROD's line is a JSX attribute, so Global keeps the feature colour on the bars.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 src/pages/ModelPortfolios.tsx Bar fill (feature text, unchanged)",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 missing list includes 'fill={modelColor?.primary || PALETTE.gray300}'"
    ]
  },
  "spec_asserts": "Face recipe: Global takes PROD text, other scopes the feature text; each text on its own lines; ? and : on lines of their own (face section 1). Site 10: Global gets fill={modelColor?.primary || PALETTE.gray300}; other scopes keep the feature's fill.",
  "world_is": "The PROD line 'fill={modelColor?.primary || PALETTE.gray300}' is a whole JSX attribute. Placing it inside a ? : branch would drop the fill= prefix; keeping the prefix would duplicate the whole Bar element, which is not the recipe. The site was NOT edited (portal@19494a76, the bar mount inside trendStackSeries.map). Check P1 lists the line missing.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-cut the site, or refuse portal 19494a76 as the CN-i-3 candidate until it is re-cut)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S6",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "The feature changed two Area colour statements the face's site list does not name; the recipe cannot carry them, so Global keeps the feature colour on the area chart.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C portal show 5ab67a65:src/pages/ModelPortfolios.tsx: 'const color = getModelColor(s.label)?.primary || PALETTE.blue400' and '... || PALETTE.gray300'",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 missing list includes both const color lines"
    ]
  },
  "spec_asserts": "Face recipe: Global takes PROD text, other scopes the feature text; each text on its own lines; ? and : on lines of their own (face section 1). The face names ten sites; the area chart's two 'const color = ...' statements (the gradient colour and the Area colour, PROD 'getModelColor(s.label)?.primary || PALETTE.blue400' and '... || PALETTE.gray300') are the same colour change as site 10 but are not in the list.",
  "world_is": "Both PROD colour statements are whole 'const color = ...' lines, the same shape as site 2 and 4, so the recipe cannot place them. They were NOT edited; check P1 lists both missing. Flagged here because the face's site list omits them.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-cut the site, or refuse portal 19494a76 as the CN-i-3 candidate until it is re-cut)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S7",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "The issuer's check P1 requires two PROD lines that the face's keep-list says to leave as the feature wrote them (the [scopeAumMetrics] dependency and the CategoryViewTree import), so AC1 cannot pass while the keep-list holds.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 src/pages/ModelPortfolios.tsx: '}, [scopeAumMetrics, dataAsOf])' and 'import { CategoryViewTree, l1ColorOf }'",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_3.py sites -> P1 missing list includes '}, [scopeAumMetrics])' and the PROD CategoryViewTree import"
    ]
  },
  "spec_asserts": "Face section 1: 'Leave every OTHER hunk of the diff alone: the imports for carriedAsOf/asOfLabel, ... the [scopeAumMetrics, dataAsOf] dependency'. Check P1: every PROD line the feature removed is present at HEAD.",
  "world_is": "PROD's '}, [scopeAumMetrics])' and 'import { CategoryViewTree } from '@/components/CategoryViewTree'' are removed hunks that the keep-list leaves in the feature's form (the dependency gains dataAsOf; the import gains l1ColorOf, which the feature's trendColorOf needs). P1 therefore reads these two lines missing with no Trend text left to restore. Both were kept, as the face says.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S8",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "The worker's worktree carries the pre-amendment CN-i-2 order (issued_to ~24, status complete); the re-cut order (issued_to ~25, status pending) is commit dafba4dbf3 and is not in this branch.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show 1f6fa7e8b6:org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.md (issued_to ~24, status complete)",
      "git show dafba4dbf3:org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.md (issued_to ~25, status pending)"
    ]
  },
  "spec_asserts": "The face is the re-cut order for ~25 at the path MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.md, status pending until AC1 and AC2 pass.",
  "world_is": "At the worker's outer HEAD 1f6fa7e8b6 the order file reads '<issued_to>0.9.0_WK_MDPF_CANON~24' and '<status>complete</status>'. 'git merge-base --is-ancestor dafba4dbf3 HEAD' is not an ancestor, and dafba4dbf3:<same path> reads issued_to ~25, owned cells CN-i-2 and CN-i-3, status pending. The worker used the face, and did not edit or flip the file (AC1 fails, so no flip). A 'complete' status on an open order would read as terminal to the L10 gate.",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~D1 (re-issue the order from the amended path or merge dafba4dbf3 into the worker branch)"
}
```

```json
{
  "id": "MDPF_CANON-D1-W25-S9",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~25",
  "surfaced_at": "2026-10-14T20:34:35Z",
  "one_line": "Two portal-route conflicts: the face's commit route (bare git -C commit) and branch name (wk-MDPF_CANON-25-portal) differ from the standing worker rule (safe-commit) and portal/CONTRIBUTING-BOXES.md (cand/<box>/<slug>).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@19494a76 (LOCAL on wk-MDPF_CANON-25-portal; author 0.9.0_WK_MDPF_CANON~25)",
      "portal/CONTRIBUTING-BOXES.md rules 1 and 4 (cand/<box>/<slug>, open-calls.py add)"
    ]
  },
  "spec_asserts": "Standing worker rule: every commit via .tools/safe-commit.sh. portal/CONTRIBUTING-BOXES.md: a portal feature is on cand/<box>/<slug>, cut from the last PROD release, registered with open-calls.py.",
  "world_is": "Face section 5.1 names 'git -C <portal> commit'; the portal commit 19494a76 was made that way (bare git, not safe-commit), and the branch is wk-MDPF_CANON-25-portal (a worker branch, cut from PROD plus the three feature commits). Nothing was pushed and nothing was registered. The issuer owns the approval register and the cand/ name.",
  "disposition": "UNDER_INVESTIGATION"
}
```
```json
{
  "id": "MDPF_CANON-D1-W27-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~27",
  "surfaced_at": "2026-10-14T21:47:51Z",
  "one_line": "CN-p-2 step 9 retires the Global Other AUA and its gates, but the period-end row filter (the plottedKeys block in ModelPortfolios.tsx) also read the retired hasGlobalEnterprise; it now reads timeSeriesData.isPerFirm, the same gate as the Non-Model show chain.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-2 section 1 step 9: the Bar and Area show gates become 'non_model shown only when timeSeriesData.isPerFirm'. The step names the show gates and the legend; it does not name the all-plotted-null row filter that also reads the retired constant.",
  "world_is": "The plottedKeys block (pre-edit ModelPortfolios.tsx line 2298, portal base f8c7d310) pushed Non-Model into the Global plotted key set on hasGlobalEnterprise, a constant step 9 deletes. Left in place, a Global Non-Model key would survive the row filter while the Global show gate no longer draws it. Changed to timeSeriesData.isPerFirm (one line). W3 of the wiring check requires the constant absent.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/ModelPortfolios.tsx@f8c7d310:2298 'if (timeSeriesData.isPerFirm || hasGlobalEnterprise) {'",
      "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-p-2.portal-variant1-trend-stitch-and-approved-edits.md@0e60da2afb (section 1, step 9)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the L7 worker on its own worktree branch; the surprise is the page text, not its significance."
}
```
```json
{
  "id": "MDPF_CANON-D1-W27-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~27",
  "surfaced_at": "2026-10-14T21:47:51Z",
  "one_line": "CN-p-2 step 11 renders the Variant 1 composition footnote with no scope gate, so it also shows on the per-firm views of an internal session; the module returns it for every Variant 1 call.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-2 step 11: '<p data-trend-composition>{compositionFootnote(trendMode)}</p>', each rendered only when its text is non-null; section 2 bound 8 forbids a per-scope fork. The module docstring for compositionFootnote says 'Internal sessions only: it names two partner firms'.",
  "world_is": "compositionFootnote('variant1') is non-null on every Variant 1 render. The composition sentence (Inflection enters 2026-05-15, Cottonwood 2026-05-28) therefore shows on the 49 Financial and Inflection per-firm views for internal sessions as well as on Global. Built literally as written; a Global-only gate is the issuer's decision.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/ref/cn_p_2_helpers.ts@0e60da2afb compositionFootnote, lines 150-155 (returns the text for variant1 with no scope argument)",
      "portal/src/pages/ModelPortfolios.tsx (worktree, the data-trend-composition paragraph under the detail note)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Display text only; the Variant 2 demo tenant gets null. Filed for the issuer to decide the scope."
}
```
```json
{
  "id": "MDPF_CANON-D1-W27-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~27",
  "surfaced_at": "2026-10-14T21:47:51Z",
  "one_line": "CN-p-2 step 4 says the Inflection series take 'the same mapping' as the 49 Financial series, but the primary-label filter would drop Inflection's Custom members; the Inflection mapping keeps every non-SMA member and folds it through groupCustomModelsSeries.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-2 step 4: firm49 keeps only labels in GLOBAL_PRIMARY_LABELS; inflectionCustom is 'the same mapping for the Inflection series', then rollBlendsIntoArchetypeSeries, then groupCustomModelsSeries(...)[CUSTOM_MODELS_LABEL].",
  "world_is": "Inflection's Custom Models value is the fold of its non-primary members, so a primary-label filter applied to Inflection would empty the series and the Variant 1 window 2026-05-15 .. 2026-07-19 would draw no Custom line. The worker applied the SMA-cohort exclusion to Inflection and no primary-label filter; 'the same mapping' is read as the cohort rule only.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/ref/cn_p_2_helpers.ts@0e60da2afb indexByPeriod(stitch.inflectionCustom) used for Custom inside the window",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_2.py@0e60da2afb V2 arm (Variant 1 draws Inflection's own series, 53)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The V2 arm passes on the built page, so the reading matches the issuer's check."
}
```

```json
{
  "id": "MDPF_CANON-D1-W26-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~26",
  "surfaced_at": "2026-10-14T21:43:21Z",
  "one_line": "CN-p-1 step 4 names a seven-line comment above the Muni tuple in SMA_MEMBERS; the comment at HEAD is eight lines. All eight were removed with the tuple and the one specified comment line was put in their place.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-1 step 4: delete the muni tuple and its seven-line comment above it; put ONE comment line in their place.",
  "world_is": "data/mdpf/scripts/gold/mdpf_category_registry.py@a9ebbe661e carries the muni comment on lines 349-356 (eight lines) above the tuple on line 357. The edit removed lines 349-357 and inserted the single specified line: 1446 to 1438 lines, CRLF kept, no other line touched.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/mdpf/scripts/gold/mdpf_category_registry.py@a9ebbe661e lines 349-357 read before the edit",
      "post-edit read: 1438 of 1438 lines CRLF; grep shows the single new muni comment line at 349"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A count mismatch only; the action matches the order's stated intent."
}
```

```json
{
  "id": "MDPF_CANON-D1-W26-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~26",
  "surfaced_at": "2026-10-14T21:43:21Z",
  "one_line": "A failed SMArtX read does not stop at the loader: build_all wraps the loader in _isolated, which turns the C2-SIBLING raise into None, and the or-fallback then builds Global with empty legs. The run goes non-green, but the order's never-an-absence rule is not enforced at the call site.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1",
  "spec_asserts": "TO CN-p-1 step 2: load_smartx_sma_legs: a denied or failed read is never an absence -- RuntimeError whose message STARTS C2-SIBLING FAIL-LOUD:. TO step 3: the loader is called through _isolated('global', ...) or ({}, None).",
  "world_is": "data/mdpf/scripts/gold/mdpf_gold_consolidator.py@a9ebbe661e (worktree edit, uncommitted): _isolated (about lines 2897-2909) catches the RuntimeError, records manifest errors['global'], logs SCOPE FAILED and returns None. The or-fallback then applies empty legs, so every pre-2026-05-18 trend group is None for that run. The manifest is non-green (ok = not manifest errors, about line 3366). NOT READ: whether the Global object is still published on a non-green run.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py _isolated definition, read in the worktree (about lines 2897-2909)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py build_all wiring, read in the worktree (lines 3059-3061)",
      "data/mdpf/scripts/gold/mdpf_gold_consolidator.py manifest ok line, read in the worktree (about line 3366)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Armed on the code's own scheduled path once deployed (CloudOps's deploy, not this order). Routed to the issuer, which owns the cell and the wiring decision."
}
```

```json
{
  "id": "MDPF_CANON-D1-W26-S3",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~26",
  "surfaced_at": "2026-10-14T21:43:21Z",
  "one_line": "Two comment lines in mdpf_category_registry.py still name muni after the Muni tuple is removed, including a denominator comment (3 of 6 determined). The order says not to touch any other line, so both are left as they are.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-1 step 4: do not touch SMA_BASIS_VERIFIED, the crosswalk or any other line of the registry.",
  "world_is": "data/mdpf/scripts/gold/mdpf_category_registry.py@a9ebbe661e after the edit: line 356 ('ground as muni ...') and line 364 ('# 3 of 6 determined, 3 UNVERIFIED (muni/idvz/pfde) ...') still name muni; the SMA_MEMBERS count is now 5.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "grep of the registry for muni in the worktree, after the edit: lines 349, 356, 364",
      "SMA_MEMBERS members after the edit read by the issuer's P5 arm: divz, idvz, pfde, pfoe, tax"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Stale comments only; no code path reads them. Left for the owner of the registry comments."
}
```

```json
{
  "id": "MDPF_CANON-D1-W26-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~26",
  "surfaced_at": "2026-10-14T22:05:41Z",
  "one_line": "TO CN-p-1 says the touched files are CRLF; at HEAD three of the four are LF (0 CRLF lines). Each file was edited with the endings it has, so the diff is not a line-ending rewrite.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-1 section 1 (code, preamble) and steps 4 and 5: the files mdpf_gold_consolidator.py, mdpf_category_registry.py and test_stratid_round2_inside_model.py are CRLF; keep their line endings.",
  "world_is": "At 92ecb84add: data/mdpf/scripts/gold/mdpf_gold_consolidator.py 0 of 3476 lines CRLF; data/mdpf/scripts/gold/mdpf_category_registry.py 0 of 1438 CRLF; data/mdpf/tests/stratid/test_stratid_round2_inside_model.py 0 of 136 CRLF; data/mdpf/tests/canon/test_global_trend_groups.py 153 of 153 CRLF (the file this order creates, from the first pass).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "byte count of CRLF pairs and newlines per file, read in the worktree at 92ecb84add before the edit (python, open(...,'rb'))",
      "post-edit byte count: consolidator wiring block edited with the Edit tool, no line-ending change; test (f) appended to the CRLF test file with CRLF endings (218 of 218 lines CRLF)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A premise mismatch only; no code path reads line endings. Kept as found."
}
```

```json
{
  "id": "MDPF_CANON-D1-W27-S4",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~27",
  "surfaced_at": "2026-10-15T01:26:11Z",
  "one_line": "CN-p-2 amendment 2 leaves the page comment at ModelPortfolios.tsx line 560 saying the Inflection blends are rolled first; the statement it describes no longer rolls them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-p-2 amendment 2 (section 0, the page edit): 'No other line of the page changes.'",
  "world_is": "The comment above inflectionCustom reads 'folded as the per-firm path folds them (blends rolled first)'. After the amendment-2 edit the statement builds inflectionCustom from the UNROLLED Inflection series, so the comment is inaccurate. Left as it is, because the order bounds the page to the one expression.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal@500af5e8 src/pages/ModelPortfolios.tsx lines 560-562 (read in the worktree after the edit): comment line 560 unchanged, statement line 562 now groupCustomModelsSeries(inflectionByModel, ...)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Comment-only; the issuer decides whether to correct it. No code path reads the comment."
}
```

```json
{
  "id": "MDPF_CANON-D1-S28",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~U7",
  "surfaced_at": "2026-10-15T02:39:20Z",
  "one_line": "After the CN-q-1 edge deploy, Lambda auth-validator-edge version 23 (the rollback target) reads a LastModified 17 minutes after the apply, with an unchanged CodeSha256 and no CloudTrail mutation of the function.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "ADHOC.canon-q1-edge-firm-gate-deploy L5e: version 23 still exists and its CodeSha256 equals the L1 before print; section 3f: only CodeSha256, LastModified and the version list of the function move.",
  "world_is": "get-function --qualifier 23 reads CodeSha256 sCxEV3p6ucK1iewCWQeqJaf0SHVURqOlj52dnE58WHo= (equal to the L1 print), State Active, LastModified 2026-10-14T23:22:22Z; the apply published version 24 at 23:05:26Z to 23:06:03Z. CloudTrail us-east-1 for 22:30Z to 02:40Z lists exactly one UpdateFunctionCode, one PublishVersion and one UpdateDistribution on this function, all from the apply; none at 23:22Z. The version-23 timestamp is unexplained; its code hash is the rollback proof and it holds.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda get-function-configuration --qualifier 23 and list-versions-by-function read 2026-10-15T02:3xZ",
      "aws cloudtrail lookup-events (UpdateFunctionCode20150331v2, PublishVersion20150331) for the window, function names read from requestParameters"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No act taken. Ledger mdpf-canon-edge-firm-gate L5 carries the same observation."
}
```

```json
{
  "id": "MDPF_CANON-D1-W29-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~29",
  "surfaced_at": "2026-10-15T15:14:53Z",
  "one_line": "The worker worktree C:/dev/wk-canon-r10-29 is a sparse checkout with no data/ tree on disk, so the two files CN-r-1 names as its write surface (data/mdpf/scripts/gold/mdpf_gold_consolidator.py and data/mdpf/tests/canon/test_global_trend_groups.py) are absent and the order cannot be executed in this tree.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-r-1 section 3 (paths) and the bar's first act: the worktree carries the paths the task order names; the order's write surface includes data/mdpf/scripts/gold/mdpf_gold_consolidator.py and data/mdpf/tests/canon/test_global_trend_groups.py.",
  "world_is": "Worktree wk-MDPF_CANON-29 at HEAD e729b642de has core.sparseCheckout=true with sparse-checkout list .tools, infra/logic/registry, lib; org/ and .tools/ are present on disk (first-act check passes); 82846 index entries carry skip-worktree; the data/ directory does not exist on disk although data/ holds 1999 tracked files at HEAD. Both named files are tracked at HEAD but absent on disk. The base checkout C:/dev/ajb_workspace tracks the consolidator at 7e0e6011ad (an ancestor of this HEAD). No criterion was run, no proof instance was written, and no sparse-checkout or other tree change was made.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-canon-r10-29 HEAD e729b642de: git config core.sparseCheckout = true; git sparse-checkout list = .tools, infra/logic/registry, lib; git ls-files -v skip-worktree count = 82846; test -d data = absent",
      "C:/dev/wk-canon-r10-29 HEAD e729b642de: git ls-tree HEAD data/ = 27 entries; git ls-files data = 1999; git status --short -- data = 0 lines; the consolidator and test paths are present in git ls-files and absent on disk",
      "C:/dev/ajb_workspace (base, box/dell1 e729b642de): git log -1 -- data/mdpf/scripts/gold/mdpf_gold_consolidator.py = 7e0e6011ad, which is an ancestor of worktree HEAD (merge-base --is-ancestor = YES)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Blocks CN-r-1 at its first criterion. Restoring the data/mdpf paths in the worktree (a sparse-checkout widen or a fresh worktree) is the issuer's or CloudOps's call; the worker did not rebuild or reconstruct the tree. No AWS touched; the deploy-side bounds are not engaged."
}
```

```json
{
  "id": "MDPF_CANON-D1-W30-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~30",
  "surfaced_at": "2026-10-15T15:15:20Z",
  "one_line": "CN-r-2 cannot start: infra/aws/terraform/opal-assets/ is tracked at HEAD but absent from this worktree, which is a cone-mode sparse checkout that omits infra/aws.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-r-2 first act and bar: confirm the worktree carries the paths the order names, else file a BLOCKING row and stop. Section 1 STEP 1-2: read and edit infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf and read infra/aws/terraform/modules/opal_name/main.tf in the worktree.",
  "world_is": "Worktree C:/dev/wk-canon-r10-30 (HEAD e729b642de, branch wk-MDPF_CANON-30) has core.sparseCheckout=true and core.sparseCheckoutCone=true. git sparse-checkout list gives .tools, infra/logic/registry, lib, org/devices, org/missions/D8/MDPF/MDPF_CANON, org/modules/graph, org/ref, org/standards. The directory infra/aws does not exist in the working tree (ls: cannot access 'infra/aws'), yet git ls-files lists 9204 files under infra/aws with the skip-worktree tag S and git status shows 0 changes there. The target .tf and the opal_name module are tracked at HEAD but not materialised, so neither can be read or edited here. No checkout, sparse-checkout change or rebuild was made, because the order forbids reconstruction.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git config --get core.sparseCheckout and core.sparseCheckoutCone both print true (worktree C:/dev/wk-canon-r10-30, read 2026-10-15T15:13Z to 15:15Z)",
      "git sparse-checkout list (same worktree) lists 8 cone patterns and no infra/aws entry",
      "ls -a infra/aws: No such file or directory; Read of infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf: File does not exist",
      "git ls-tree HEAD infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf gives blob 30f8f0cefe8e1e2afce1642ae3951ab306d41d6e; git ls-tree HEAD infra/aws/terraform/modules/opal_name/main.tf gives blob 4b8c018812ef2567c63a39549666a9d9f0d9b20f",
      "git ls-files -v infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf gives tag S (skip-worktree)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No act taken. CN-r-2 is not built or graded here: its three criteria were not run, and the order stays open with no proof instance. Remedy belongs to the issuer or COO: a worker worktree whose cone includes infra/aws, or a re-cut of the CN-r-2 paths."
}
```

```json
{
  "id": "MDPF_CANON-D1-W30-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~30",
  "surfaced_at": "2026-10-15T15:21:44Z",
  "one_line": "CN-r-2 order names a <status> flip to complete, but the worker face (lines 1-105) carries no <status> element to flip.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO CN-r-2 section 5 (line 102): flip this order's <status> to complete in the SAME commit as the proof instance, only when every criterion passes. The worker face is lines 1-105 and the record face is never read by this worker.",
  "world_is": "Lines 1-105 of MDPF_CANON.TO-CN-r-2.publisher-latest-json-read-grant.md carry no <status> element. The only occurrence of the word status in those lines is the instruction itself at line 102. All three criteria AC1-AC3 PASS and the proof instance validates, but there is no status field inside the worker face to write complete into.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "head -105 of the order, grep -n -i status (worktree C:/dev/wk-canon-r10-30, read 2026-10-15T15:21Z): one hit, line 102, the flip instruction; no <status> tag",
      "Read of the order lines 1-105: <paths> at lines 76-81, <proof_of_spec> at lines 88-92, the instruction block at lines 98-104; no <status> element in the face",
      "criteria AC1 AC2 AC3 PASS by output, proof-of-spec-check rc recorded in the instance commit"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No act taken on the flip: the order status is NOT written to complete. The record face is out of this worker's read set, so the status element is not located here. Remedy belongs to the issuer (2.0.0_SA_COO~D1): state where the <status> element lives or flip it on the issuer's side after the proof instance is read."
}
```

```json
{
  "id": "MDPF_CANON-D1-S29",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~D1",
  "surfaced_at": "2026-10-15T15:40:36Z",
  "one_line": "Global Trend Variant 2 (non-internal session) draws the model stack AND the carried Models band on the 9 carried dates after 2026-05-15, so the daily chart spikes to about $3.1B against a $1.77B Total; Variant 1 has 0 such rows.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (cuts the round-11 cell for portal/src/lib/trendGrouping.ts buildGlobalTrendRows Variant 2; the PROD push is client-facing and waits on Andrew via 1.0.0_SA_CTO~DELL1)",
  "spec_asserts": "PRD v2.22 override (d) and CN-p-2 AC4: Variant 2 draws one Models band before per-model detail begins (2026-05-15) and the model stack after it, and the groups partition the served Total.",
  "world_is": "Read on portal DEV e0b033253b (same trendGrouping.ts text as PROD c3b21a40e2) over the served Global aggregate-aua-timeseries (497 dates, frontier 2026-10-14): buildGlobalTrendRows(variant2) returns 9 rows at or after 2026-05-15 with modelsBand > 0 (2026-05-30, 05-31, 06-06, 06-07, 06-13, 06-14, 06-19, 06-20, 06-21), exactly the 9 carried_dates. Each carries the five model lines (sum 1,448M) AND modelsBand 1,349,270,858.88 (the 2026-05-14 value, carried), with clientSupervised 266.9M and etfStrategies 25.0M: stack about 3.09B against total 1,766,813,072.41. The headless render on a stubbed non-internal demo session showed four spikes at those dates. The round-9 variants record counted the band only on the 383 pre-detail rows and did not test carried dates after 2026-05-15. A non-internal Global viewer (MDPF_GLOBAL_VIEW_FIRMS) sees it on PROD today.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun run round9/checks/measure_real_variants.ts (DATA_DIR with the served Global object, UNROLLED=1) in portal at e0b03325: v2 rows after 2026-05-15 with modelsBand>0 = 9 of 497, all in carried_dates (9); printed row 2026-05-30 total 1766813072.41 modelsBand 1349270858.88",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/ITEM6_RENDERS_20261015.md section B (the render, words only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Issuer's own render and measure, not a worker row. Remedy: on a date at or after per-model detail begins, Variant 2 draws the model stack and drops modelsBand; one cell with a test over the real object (0 of 497 rows with both). Not fixed here."
}
```

```json
{
  "id": "MDPF_CANON-D1-W34-S1",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~34",
  "surfaced_at": "2026-10-19T14:53:45Z",
  "one_line": "The pre-commit risk reflex could not check the CN-s-7 diff: its danger map is STALE (91.0h old) and its build guard refused the linked worktree, so it scanned 0 of 2 files.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (issuer of the slot ~34 order; routes the stale danger map and the linked-worktree build guard to the tooling owner)",
  "spec_asserts": "TO-CN-s-7 section 5.1: commit the two code files through .tools/safe-commit.sh as one commit, the commit gate must pass.",
  "world_is": "safe-commit.sh committed 3d3d5ed5b9 and the commit gate passed, but the printed risk-reflex line read NOT-DECIDABLE, ANSWER STATE PARTIAL_OR_BLIND, WITHIN BUDGET scanned 0 of 2 file(s). The reason printed: git-dir C:/dev/ajb_workspace/.git/worktrees/wk-canon-s7-34 differs from git-common-dir C:/dev/ajb_workspace/.git at C:\\dev\\wk-canon-s7-34.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output at commit 3d3d5ed5b9 (worktree C:/dev/wk-canon-s7-34, branch wk-MDPF_CANON-34): '[risk-reflex] ANSWER STATE: PARTIAL_OR_BLIND' and '[risk-reflex] WITHIN BUDGET: scanned 0 of 2 file(s)'",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~34/ (the proof instance records the commit and its output)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only: the risk reflex is blind for linked worktrees on this box, so every worker commit here carries an unscanned risk check. The commit itself was not blocked."
}
```

```json
{
  "id": "MDPF_CANON-D1-W34-S2",
  "project": "MDPF_CANON",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_CANON~34",
  "surfaced_at": "2026-10-19T14:53:45Z",
  "one_line": "The commit gate printed client-data-check ABSENT (hashed account-id list not found), so commit 3d3d5ed5b9 was not checked for client account ids.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D1 (issuer of the slot ~34 order; routes the account-id hash list to this box, which has it at C:\\Users\\Test\\.opal\\account_id_hashes.txt or OPAL_ACCOUNT_ID_HASHES)",
  "spec_asserts": "TO-CN-s-7 section 5.1: commit through .tools/safe-commit.sh with the commit gate passing; the commit is the gate's denominator for the client-data check.",
  "world_is": "safe-commit.sh printed 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).' The commit landed (3d3d5ed5b9, 2 files, 19 insertions, 24 deletions).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output at commit 3d3d5ed5b9: 'WARN: client-data-check: hashed account-id list ABSENT' followed by the commit line '[wk-MDPF_CANON-34 3d3d5ed5b9]'",
      "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~34/ (the proof instance records the commit and its output)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only: this box lacks the hashed account-id list, so commits here are not client-data checked. The diff touches two code files with synthetic test numbers and no client data; no figure was read from the six leg files."
}
```
