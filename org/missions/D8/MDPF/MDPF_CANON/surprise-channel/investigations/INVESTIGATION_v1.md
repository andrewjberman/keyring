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
