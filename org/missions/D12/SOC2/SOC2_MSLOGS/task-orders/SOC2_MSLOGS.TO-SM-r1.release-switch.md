# TO SOC2_MSLOGS.TO-SM-r1 -- the release: apply the switch in place, start the sign-in feed, verify the raw store live, Andrew's FWD-1 read

<to_id>SOC2_MSLOGS.TO-SM-r1</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.7.0_AE_CloudOps~SOC21</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-r-1` (`decompositions/SOC2_MSLOGS_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-8 | **depends_on:** `SM-c-1`, `SM-a-1`, `SM-s-1`, `SM-g-1`, `SM-x-1` complete and MERGED. **FLIPPED to `pending` by the issuer 2026-10-16 after the five merges (SM-s-1 56af05ace6, SM-x-1 5660aeb021, SM-c-1 b2fef4b9b5, SM-g-1 ddccf1e8f1, SM-a-1 36f107cee9) and the drain checks.**

---

## WORKER FACE

### THE CELL

`SM-r-1`: the live change of round 1. The audit store already runs in the account (bucket `opal-data-trino`, the door Lambda `globgrph-trino-access-lambda` with aliases `collector` and `member`, the hourly collector
`m365-metadata-trino-collector-lambda`, the group `globgrph-trino-access-group` holding `Andrew_Berman` alone, MFA Denies on both aliases, all applied under the closed project TCKT_MTADTA). The merged tree changes the CODE of the
collector and the door so the store keeps the raw records of every account (decomposition rulings 1-9). You apply that change IN PLACE, start the fourth Microsoft feed, prove the switch from live reads, and hand Andrew his FWD-1 read.
Read first: the decomposition `org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md` (rulings 1-10), PRD `prd/SOC2_MSLOGS_PRD.md` rows C-SWITCH, C-ACCESS, C-COVERAGE, `infra/aws/terraform/trino/access.tf`
(its header states the design), `infra/aws/terraform/trino/door_resource_policy.README.md` (the Deny that Terraform does not manage), `data/m365_metadata/scripts/app/RUNBOOK.md`.

You run as the box identity `cloudops-dell1-agent-user`, deliberately NOT a member of the group: you read no stored object and invoke no door op. Your reads are describes, lists, log filters and the Management API subscription list.

### ITEMS, in this order. Stop at the first that fails and write what stands.

1. **Preconditions.** The five cells are complete and merged (`git log`; the order files read `<status>complete</status>`); from the repository root these print their OK tokens:
   `s1_check_c1.py raw|switch|recollect`, `s1_check_a1.py ops|bronze|tf`, `s1_check_s1.py silver|timeline`, `s1_check_g1.py ledger`, `s1_check_x1.py scrub`, and `thread_trace_r1.py` (the whole thread over an in-memory store). `s1_check_g1.py rows` is NOT a precondition: it printed OK at the cell's merge (fdecf020e7) and reads `targets stale` since a box-sync brought in another seat's registry change (4.0.0_SA_CRO~Z, `legacy_addresses.json`) that moves the registry hash its generated files stamp; regenerating those files is that seat's act, not this release's (all in `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/`). Otherwise STOP and report.
2. **Open the ledger** before any write: `python .tools/deploy_ledger.py open --slug soc2-mslogs-r1-raw-switch-20261016 --title "SOC2_MSLOGS round 1: in-place switch of the collector and door to raw bronze" --author 0.7.0_AE_CloudOps~SOC21 --leg ...`
   (legs: apply, subscription, switch read-back). Blast radius: the code of the two functions, the door role's policy, the door's environment, and tag or description strings; NOTHING is created or destroyed. Rollback: re-apply the previous commit's zips
   (`git revert` of the merge range and the same apply); the stored raw objects are write-once and stay (they hold nothing the old code reads).
3. **Build the two zips** from the repository root: `bash infra/aws/lambda/globgrph-trino-access/build.sh` and `bash infra/aws/lambda/m365-metadata-collector/build.sh`. Neither zip is committed. Confirm `infra/aws/terraform/trino/layer.auto.tfvars` exists (it holds the pandas layer
   ARN from the first apply); if absent, recreate it as the first apply did (the public AWSSDKPandas-Python312 layer, us-east-1; `aws lambda list-layer-versions --layer-name arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python312 --max-items 1`) and commit that one file.
3a. **AMENDED 2026-10-16 ~18:2xZ -- the first plan stopped on a dependency cycle (your message 6956; row D1-S1 of the seat).** `access.tf` references `aws_lambda_function.collector`, whose policy in `collector.tf` references the door's alias: a cycle. `infra/aws/terraform/trino/access.tf` is added to your `<paths>` for these TWO edits and no other (the issuer rules this inside its own decomposition; the door cell's worker is gone):
   (1) in `aws_iam_role_policy.access`, statement `InvokeTheCollectorForRecollect`: `Resource = aws_lambda_function.collector.arn` becomes `Resource = "arn:aws:lambda:us-east-1:${data.aws_caller_identity.current.account_id}:function:${local.collector_lambda_name}"`;
   (2) in `aws_lambda_function.access` `environment.variables`: `COLLECTOR_FUNCTION = aws_lambda_function.collector.function_name` becomes `COLLECTOR_FUNCTION = local.collector_lambda_name`.
   Then `terraform -chdir=infra/aws/terraform/trino fmt -check`, `terraform -chdir=infra/aws/terraform/trino validate` (must say `Success`), and `python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_a1.py tf` (amended in the main branch at the commit that carries this text; it now refuses a reference to the collector resource). The fixed file was validated by the issuer in a scratch copy of the root: `Success! The configuration is valid.` Commit `access.tf` alone through safe-commit, then continue at item 4.
4. **Plan, read it, apply once.** `terraform -chdir=infra/aws/terraform/trino init`, then `plan -out=<file under your scratch>`. Read the plan line by line. It must contain ONLY in-place updates: the code hash of the two functions, the door role policy (the added
   invoke of the collector), the door environment (`COLLECTOR_FUNCTION`), a Project tag and the KMS key description string (SM-x-1's word change), and the door's new published version/alias targets if the alias `function_version` follows the function's `version`. NO create, NO destroy, NO replace of
   the bucket, key, group, roles, aliases or log groups. If the plan holds anything else, STOP, write the plan summary in your report and a surprise row. Then ONE apply through the gate: `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/trino apply <that plan file>` (never bare `terraform apply`,
   never `aws lambda update-function-code`). If it fails half-way, finish it in-session or roll back and escalate loudly (NEVER-2). Write the UTC time of the apply, ISO form (`date -u +%FT%TZ`), to
   `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/switch_at.txt` and commit it.
5. **The Deny still binds.** Terraform does not manage the alias resource policies (`door_resource_policy.README.md`); a changed alias target can leave them intact, but READ them: `s1_check_r1.py applied` prints whether both MFA Denies still stand. If one is gone, re-apply it from
   `door_resource_policy.json` per the README, and say so in the ledger.
6. **Start the sign-in feed.** Obtain a Management API token with the existing app credential (a client-credentials call to the tenant's token endpoint, scope `https://manage.office.com/.default`; the credential is the secret `m365-metadata/trino/api-credentials`), keep it in the process environment only, and run
   `python data/m365_metadata/scripts/app/start_subscriptions.py --apply` with `M365_TENANT_ID` and `M365_ACCESS_TOKEN` set (it now starts all four feeds; the three already enabled are idempotent). Print HTTP statuses only. If the vendor REFUSES the fourth feed, send the issuer the refusal text VERBATIM
   by the broker in ONE message and continue with the remaining items: a missing permission is Andrew's consent to give, never yours to infer, request or work around. Do not retry in a loop.
7. **Watch the switch.** The collector's next scheduled fires (hourly) cold-start in the raw era, fetch the 7 days (several fires may be needed: a fire out of time saves its progress and `complete=False` is not a failure) and rebuild silver. Do NOT invoke the collector by hand for the criteria (an ad-hoc run is QA only; the scheduled fires are the acceptance).
   Wait for at least TWO scheduled fires after `switch_at.txt`, then run the checks. Report each fire's log line (counts only) to the issuer as one-liners by the broker. **The sign-in feed's first content can take up to 12 hours (vendor's word): the criteria below do not wait on it.**
7b. **AMENDED 2026-10-16 ~22:4xZ -- the 21:31Z fire timed out (derive ran past the 900 s limit); the repair is MERGED at 6cef75fd39 (TO-SM-c1 AMENDMENT 2).** The old code stays running until you redeploy. Do, under the same ledger entry (add a leg):
   (i) `python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py derive_time` must print `C1-DERIVETIME-OK`; (ii) `bash infra/aws/lambda/m365-metadata-collector/build.sh`; (iii) `terraform plan`: it must show an in-place update of the collector function's code hash ALONE (nothing else, no create, no destroy);
   (iv) one `bash .tools/safe-apply.sh ... apply <plan>`; (v) overwrite `switch_at.txt` with the UTC START time of the FIRST invocation of the repaired code (RULED 2026-10-16 ~23:5xZ on your message 7041: an old-code invocation that began at 23:04:18Z, before the 23:10:36Z apply, ran on and timed out at 23:19:18Z, so the apply time cannot be the boundary; the boundary is the first invocation that ran the new code, here 23:31:22Z), keep the apply time in `apply_at.txt` beside it, and commit both: the earlier timeout then falls outside AC2's window by design, because the fault it recorded is repaired, not because the test moved; (vi) wait for TWO scheduled fires after the new `switch_at.txt`, do not invoke the collector by hand, and send me each fire's counts line, its duration and whether the REPORT shows a timeout.
   A fire may still stop with `complete=False` while the backlog drains; that is not a failure. Derive now keeps a reserved share (newest day first), so silver for the recent days should rebuild within the first one or two fires. Then continue at item 8 (AC2 wants at least 7 silver dates rebuilt since the new `switch_at.txt`).
7c. **AMENDED 2026-10-17 ~00:2xZ -- the door runs OUT OF MEMORY deriving the newest days (the issuer's reading of the door log; row to follow).** At 23:43:44, 23:44:16 and 23:45:06Z the door's `derive_silver` ended `Status: error Error Type: Runtime.OutOfMemory` at Max Memory Used 1024 MB of 1024 (99 s, 71 s, 60 s). The days 9-11 Oct derived (3.7 to 7.2 MB of silver); the days 12-16 Oct, the ones an investigation reads first, cannot at 1024 MB, so silver for them is still the old eight-account table. In `infra/aws/terraform/trino/access.tf`, `aws_lambda_function.access` only: `memory_size = 1024` becomes `memory_size = 6144` and `timeout = 300` becomes `timeout = 600`. Nothing else. Then `terraform fmt -check`, `terraform validate`, and `s1_check_a1.py tf` (amended: it now requires memory_size >= 3008 and timeout >= 600); plan must show an in-place update of that one function's configuration ALONE; one safe-apply under the same ledger entry (add a leg). If the API refuses 6144 (an account memory ceiling), use 3008 and say so in a seat row. Do this BEFORE the 00:31Z fire if you can; the fire's derive then meets the larger door. Do not change `switch_at.txt` for this: the door is not the collector.
   The streaming (memory-bounded) derive is a round-2 item for the door cell; this is the stopgap. Then continue at item 8.
7e. **ANDREW-DIRECT 2026-10-17 ~00:55Z, VERBATIM: "use the biggest lambad memory possible should be 10gb or so"** (record `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261017_0055Z_USE_THE_BIGGEST_LAMBDA_MEMORY_10GB.md`). In `infra/aws/terraform/trino/access.tf`, `aws_lambda_function.access` only: `memory_size = 6144` becomes `memory_size = 10240` (the Lambda maximum). Nothing else changes; the timeout stays 600. `terraform fmt -check`, `validate`, `s1_check_a1.py tf` (its floor is now 10240), plan = that function's configuration alone (the aliases may move to a new published version again), one safe-apply under the same ledger entry (add a leg), then `s1_check_r1.py applied`. If the API refuses 10240, apply the highest it accepts, say so in a seat row, and tell me. The collector function is not touched by this item.
7d. **THE SECOND COLLECTOR REDEPLOY (issuer, 2026-10-17 ~01:2xZ; the collector repair of TO-SM-c1 AMENDMENT 3 is MERGED at 3b35dca82a).** Fire 2 of the 7b code timed out (and was retried twice by Lambda's async policy) because the collector's default boto3 client re-invoked a slow derive five times; the merged code uses a derive client with a 200 s read timeout and no retry, and derives the owed days in parallel, newest first.
   Do exactly what item 7b (i) to (vi) says, with these differences: run `s1_check_c1.py derive_time`, `derive_par` and `derive_client` (each must print its OK token) in step (i); `switch_at.txt` = the UTC START time of the first invocation of THIS code (find it from the collector log: the first `START` after your apply whose code hash is the new one, i.e. the first invocation that begins after the apply completes), `apply_at.txt` = this apply's time; the earlier timeouts, including Lambda's async retries of the old code that fall after the apply, are old-code invocations and sit before the boundary by this ruling only if they STARTED before it. Report each new-code fire's counts line, duration and timeout status. The door is already at 10240 MB (7e).
8. **Prove it** from the repository root and read each output: `s1_check_r1.py applied`, `s1_check_r1.py subs`, `s1_check_r1.py switch org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/switch_at.txt`, and the plan check `python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py plan`.
9. **Close the ledger** with the read-back (the check lines) and write your report. State for Andrew, without any secret, how he runs the timeline read with his MFA session: obtain a session token with his MFA device (`aws sts get-session-token --serial-number arn:aws:iam::313476888478:mfa/Andrew_Phone --token-code <code>`),
   export the three environment variables boto3 reads, make sure `AWS_PROFILE` is unset, then `python data/m365_metadata/scripts/silver/read_timeline.py --account <address> --start <ISO> --end <ISO>`. The issuer cards Andrew for the read.

### ACCEPTANCE

<criterion id="SM1-r1-AC1" cell_refs="SM-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_r1.py applied</invocation><expect>R1-APPLIED-OK</expect></criterion>
`SM1-r1-AC1` -- both functions run the built zips, the door's environment names the collector, the door role may invoke the collector, and both MFA Denies stand on the aliases.

<criterion id="SM1-r1-AC2" cell_refs="SM-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_r1.py switch org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/switch_at.txt</invocation><expect>R1-SWITCH-OK</expect></criterion>
`SM1-r1-AC2` -- raw objects landed for the 7 days (at least 800 objects over at least 7 dates), the frozen table took no write since the switch, silver was rebuilt for at least 7 dates since the switch, and the collector's fires since the switch show no timeout and no error.

<criterion id="SM1-r1-AC3" cell_refs="SM-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_r1.py subs</invocation><expect>R1-SUBS-OK</expect></criterion>
`SM1-r1-AC3` -- the Management API lists all four feeds enabled, the sign-in feed included. If the vendor refused it for a permission and Andrew has not yet consented, this prints REFUSED and the issuer records the open call; you do not weaken it.

<criterion id="SM1-r1-AC4" cell_refs="SM-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py plan</invocation><expect>R1-PLAN-OK</expect></criterion>
`SM1-r1-AC4` -- (a fourth mechanical criterion, with this reason: the apply is in place and the root must read converged afterwards) `terraform plan -detailed-exitcode` on the root exits 0.

<criterion id="SM1-r1-AC5" cell_refs="SM-r-1" judgment="true"/>
`SM1-r1-AC5` -- JUDGMENT, graded by the CVO at L9, never by you: Andrew names one account and a window and reads that account's Microsoft 365 timeline in order, through the door with his MFA session, from collection that is actually running, and recognises it (PRD FWD-1). You do not run, grade or claim this one.

<expected_criteria>SM1-r1-AC1,SM1-r1-AC2,SM1-r1-AC3,SM1-r1-AC4,SM1-r1-AC5</expected_criteria>

Dry-run at the base 2026-10-16 ~17:1xZ: AC1 `R1-APPLIED-REFUSED no built zip ...` or `the door's COLLECTOR_FUNCTION is None; the door role cannot invoke the collector function`, AC3 `R1-SUBS-REFUSED enabled ['Audit.Exchange', 'Audit.General', 'Audit.SharePoint'], wanted [...]` -- each FAIL as expected.
AC2 needs `switch_at.txt` (it refuses without it). AC4 is the round-2 plan check of the closed project and PASSES at the base only when the tree is converged. All checks are reads; they print counts, names and codes only.

## BOUNDS

- **Grant.** AWS: the one gated apply of the `trino` root (in-place updates only, as item 4 states); `secretsmanager:GetSecretValue` on `m365-metadata/trino/api-credentials` for the token call and the subscription list; describe, list and simulate reads; CloudWatch Logs reads of the collector log group.
  Microsoft: the Management API token call and subscription start/list with the app's own credential; NOTHING else. Repo: `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`, `infra/aws/terraform/trino/layer.auto.tfvars` (item 3 only),
  `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/`, the investigation file, and this order's file.
- **You never** read a stored object, invoke the door or the collector, add or remove a group member, change an alias policy except to restore the committed Deny (item 5), grant anything to anyone, or perform or infer a consent for Andrew.
- **NEVER** bare `terraform apply` (use `.tools/safe-apply.sh`), `aws lambda update-function-code`, a delete of any object, a change outside the `trino` root, an alarm, SNS topic or notification resource (standing moratorium), or a push. **NEVER** print, log, echo, write to a file or put in a message any secret value, token, tenant id or client id.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in the ledger and file a NEW surprise row (id `SOC2_MSLOGS-D1-S<k>` (the gate refuses the lane-suffixed form; take the next free number after the rows already in the channel file), `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.
- Commit only through `.tools/safe-commit.sh` with your own `--author`, `-F` a message file written with the Write tool, and `-- <paths>`.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/trino/layer.auto.tfvars
infra/aws/terraform/trino/access.tf
org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/switch_at.txt
org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/apply_at.txt
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md</decomp_doc> (round 1), cell `SM-r-1`.
<owned_cells>SM-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SM1-r1-AC1, SM1-r1-AC2, SM1-r1-AC3, SM1-r1-AC4, SM1-r1-AC5. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.7.0_AE_CloudOps~SOC21/SOC2_MSLOGS.TO-SM-r1.release-switch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SM1-r1-AC1,SM1-r1-AC2,SM1-r1-AC3,SM1-r1-AC4,SM1-r1-AC5` BEFORE the flip. AC1-AC4 mechanical; AC5 judgment (UNVERIFIABLE-BY-INSTRUMENT, graded by the CVO).
</proof_of_spec>

**PER-STEP LINES:** send `2.0.0_SA_COO~S1` ONE line by the broker as each of these lands, never a value: (1) the plan summary (counts of update, create, destroy) before the apply; (2) the apply result; (3) the HTTP status of each of the four feed starts, or the vendor's refusal VERBATIM; (4) each scheduled fire as it reads clean or not. The issuer relays them.

**REPORT:** the check lines; the plan summary; the apply time; the subscription HTTP statuses; the Andrew read instructions (item 9); every refusal and denial verbatim. No secret, tenant or client value.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the hourly rule read back by the scheduled fires since the switch (AC2). BLIND: a fire proves no new content landed.
comp-iam: RUN -- AC1 reads the door role policy and both alias Denies live; BLIND to a principal this project did not name.
comp-adversary: DECLARED-NOT-APPLICABLE -- no new principal; the credential never leaves the process.
lane: WORLD, a CloudOps seat under a change-management entry of its own (rule 34: one CloudOps lane per macro per box, `0.7.0_AE_CloudOps~SOC21`, seated by MSTR when this order flips to pending).
</preflight>

**ISSUER NOTES:** Source: CTO round-1 scope (msg 6869); PRD v0.2. A change to an Entra permission, if the sign-in feed needs one, is Andrew's act and is carded by the issuer when reached. Reads of FWD-1 by Andrew are the round's exercised outcome.
