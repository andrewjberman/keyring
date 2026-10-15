# TO IRPT_DASHBD.TO-DB-b-253 -- APPLY the signed hop-1 pair (packet sha256 `2f25b84dc85c`): step 0 gates and live reads, ledger, build and import-smoke the bundle, upload it, plan 0/2/0, ONE `safe-apply`, the read-backs, NO invoke, the ledger left OPEN (COO half signed @2959d224ad, CTO half signed @c07129fed1, CTO msg 8235)

<to_id>IRPT_DASHBD.TO-DB-b-253</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>124</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_HOP1_FILLED_REPORT_VALUES_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_HOP1_FILLED_REPORT_VALUES_CTO_HALF.md` (both at the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_HOP1_FILLED_REPORT_VALUES_STAGE.md`, sha256 `2f25b84dc85c1592801783ae23113e13c2686bad54b9fa6460ea6d353ac2635e`), and the CTO's rulings of rounds 120 to 123 (msg 8235: unqualified ARN accepted, no backfill in this act, default retry, plan 0/2/0) | **Decomp cell:** `DB-b-253` (decomposition section 122) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** DB-b-250 (merged @00e325c0bb), `DB-b-243`, `DB-b-247` (merged) and both halves SIGNED.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying `00e325c0bb` and the halves); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes, addresses and words only.

**What this order does, in one paragraph.** The 49 Financial reporting-gold function `irpt-49f-reporting-gold-lambda` runs five gold tables per daily fire. The repo now carries, merged, a sixth stage (`filled_report_values`, one invocation per owed day, self-invoking), three explicit IAM grants for it, one `lambda:InvokeFunction` statement on its own ARN, and `memory_size = 8192`. You build and upload its bundle, run `terraform plan` (the first time Terraform reads these files), and, only if the plan reads EXACTLY 0 add / 2 change / 0 destroy on the two addresses below, make ONE `safe-apply`. You invoke NOTHING: the first scheduled 07:41 America/New_York fire after the apply is the proof, read by the issuer.

**Read first (all in your worktree):** the packet (whole: sections 1 to 8) and its COO half; the CTO half (its section 7 answers); `infra/aws/terraform/investor-reporting/reporting-gold/` (`iam.tf`, `locals.tf`, `lambda.tf`, `schedule.tf`); `infra/aws/lambda/ci/lambda-source-map.json` entry `irpt-49f-reporting-gold-lambda` (`files`, `staged_from`, the three new members with `pin` and `sha256` null); `infra/aws/lambda/ci/build-and-upload.sh` (the BUILD_ONLY mode and what it updates); the model of your own prior apply, `org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-20.apply-cottonwood-account-dim-signed-pair.md` and your record `deliverables/0.7.0_AE_CloudOps~DB2/ACCOUNT_DIM_APPLY_RECORD.json` (ledger, build, plan, one safe-apply, read-backs).

**Do, in this order. Record every value named in `HOP1_APPLY_RECORD.json` as you go.**

0. **Gates, read only.** (a) `git hash-object` of the packet equals the blob recorded in the COO half's tree and its sha256 equals `2f25b84dc85c1592801783ae23113e13c2686bad54b9fa6460ea6d353ac2635e` (`gates.packet_blob`, `gates.packet_sha256`); both halves read SIGNED at it (`gates.coo_half_signed`, `gates.cto_half_signed`). (b) `git merge-base --is-ancestor 00e325c0bb HEAD` is true (`gates.pin_is_ancestor`). (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the denominator) names the reporting-gold root, `irpt-49f-reporting-gold` or `filled_report_values`; any one open is a STOP (`gates.one_change_at_a_time` {`worktrees_read`, `open_markers_naming_this_surface`}). (d) **LIVE, now (`gates.live_matches_packet`):** the function `irpt-49f-reporting-gold-lambda` reads `MemorySize` 3008, `Timeout` 900, `CodeSha256` `J6M/92MhjYM/0kKoYRQwR0ah68DizcvnkVSE6o24udg=`; the role policy `irpt-49f-reporting-gold-policy` holds exactly the seven statements the packet's section 2 names; the schedule reads `cron(41 7 ? * MON-FRI *)` America/New_York ENABLED. Any difference is a STOP.
1. **Open the NEVER-2 ledger BEFORE any write** with `python .tools/deploy_ledger.py open ...` under `org/critical_paths/change_management/`, slug `irpt-dashbd-hop1-filled-report-values-20261015`, legs: the artifact upload; the plan; the one `safe-apply`; the read-backs; and the first scheduled fire's verify (a leg that stays OPEN for the issuer). Commit its `.open_deploys` sentinel at once. Record `ledger_entry` (the slug).
2. **Before reads.** `before.function` {`memory`, `timeout`, `code_sha256`}; `before.policy_sids` (the seven sids, by name); `before.schedule` {`state`, `cron`}; `before.filled_prefix_objects` (a fresh LIST of `irpt/49financial/gold/filled_report_values/` in `opal-data-49financial`, the prefix from `lib/opal_naming.py address()`; the packet expects 0); `before.artifact_previous.version_id` (the version id of the current artifact object `investor-reporting/irpt-49f-reporting-gold-lambda.zip` in `opal-313476888478-lambda-artifacts`, which has versioning Enabled: the rollback target).
3. **Build, import-smoke, upload.** (a) `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-49f-reporting-gold-lambda`: the zip is built, its base64 sha256 printed, nothing uploaded; record `build.zip_sha256` (hex of the zip's sha256), `build.zip_sha256_b64` (base64 of the same digest, the form Lambda reports) and `build.members` (the zip's member list: it must hold `handler.py` and the three new members at their `packaged_as` paths). (b) **Import smoke:** extract that zip to a fresh temporary directory and, from another directory, run `python -I -c "import sys; sys.path.insert(0, '<dir>'); import handler; assert handler.frv is not None and handler.FRV_IMPORT_ERROR is None"`; record `build.import_smoke_rc` (must be 0; a failure is a STOP before upload). (c) Only then the real `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-49f-reporting-gold-lambda`: it writes ONE new object version at the artifact key and records `artifact_sha256` and the three new members' `pin` and `sha256` in the source map; record `build.landed_version_id`, `build.content_sha256` (hex sha256 of the landed object's bytes) and `build.built_equals_landed` (true when the landed bytes equal the BUILD_ONLY zip's). Commit the source-map change (the entry's `artifact_sha256`, the three members' pins and hashes: nothing else in the file moves).
4. **fmt, validate, plan, under the repo's route.** `.tools/terraform.exe` on the root `infra/aws/terraform/investor-reporting/reporting-gold/`: `fmt -check`, `init`, `validate`, a saved `plan`. **The plan must read EXACTLY** 0 to add, 2 to change, 0 to destroy, the two changes being `module.irpt_reporting_gold.aws_lambda_function.this` (`memory_size` 3008 to 8192 and the code hash to the new artifact version) and `aws_iam_role_policy.irpt_reporting_gold` (four new statements and the sixth write prefix). Record `plan` {`add`, `change`, `destroy`, `addresses` (the two), `memory_line` (the plan's own line for the memory change), `policy_words` (the new statement ids as the plan prints them, and that the write list gains `filled_report_values`)}. Any other add or change, any destroy, any attribute change beyond those named (a changed role, handler, runtime, timeout, layer, environment or schedule), is a STOP.
5. **ONE `safe-apply`** from the saved plan (`.tools/safe-apply.sh`; never a bare `terraform apply`, never `aws lambda update-function-code`). Read back: the function (`MemorySize` 8192, `Timeout` 900, `Handler` `handler.lambda_handler`, `Runtime` `python3.12`, the role, `CodeSha256` equal to `build.zip_sha256_b64`), the role policy (eleven statements: the seven plus `ReadTheServedModelSeriesObjectOnly`, `ListExactlyTheHouseholdCrosswalkPrefix`, `ReadTheHouseholdCrosswalkOnly`, `InvokeOwnFunctionOnly`; the one PutObject statement lists six prefixes, `filled_report_values` among them), the schedule unchanged. A post-apply plan must read `No changes` (`plan.replan_no_changes` true). Stamp the deploy as the model does. Record `apply_finished_utc` (`YYYY-MM-DDTHH:MM:SSZ`, just AFTER the apply and read-backs) and `after` {`function` {`memory`, `timeout`, `code_sha256`}, `policy_sids`, `schedule` {`state`, `cron`}, `filled_prefix_objects` (a fresh LIST: the apply writes none; expect 0)}.
6. **NO INVOKE.** Not the function, not a dry-run event, not a `day` event: a `day` event is a write and needs the CTO's word, and a dry run proves nothing. Record `invoke` {`count` 0}.
7. **Do NOT close the ledger.** The first scheduled 07:41 America/New_York fire on a trading day after the apply is the verify leg, read by the issuer from that invocation's REPORT line (`Max Memory Used`, duration) and the new partition. Record `ledger_closed` false. Stale OPEN marker copies on other worktrees are named, never closed.

Write `HOP1_APPLY_RECORD.json` in your folder with exactly: `claim` ("measured"); `gates` {`packet_blob`, `packet_sha256`, `coo_half_signed`, `cto_half_signed`, `pin_is_ancestor`, `one_change_at_a_time`, `live_matches_packet`}; `ledger_entry`; `before` {`function`, `policy_sids`, `schedule`, `filled_prefix_objects`, `artifact_previous` {`version_id`}}; `build` {`zip_sha256`, `zip_sha256_b64`, `members`, `import_smoke_rc`, `landed_version_id`, `content_sha256`, `built_equals_landed`}; `plan` {`add`, `change`, `destroy`, `addresses`, `memory_line`, `policy_words`, `replan_no_changes`}; `apply_finished_utc`; `after` {`function`, `policy_sids`, `schedule`, `filled_prefix_objects`}; `invoke`; `ledger_closed`; `reads` {`vendor_calls` 0, `secret_reads` 0}. Counts, dates, keys, hashes, addresses and words only.

<criterion id="DBB123-1-AC1" cell_refs="DB-b-253"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_hop1apply.py" . DBB123-1-AC1</invocation><expect>DBB123-1-AC1 PASS</expect></criterion>
`DBB123-1-AC1` -- the packet's bytes and sha256 are the signed ones and both halves read SIGNED at it; the step-0 gates are recorded true with the worktree denominator; the ledger entry exists; the before state equals the packet's section 2; the bundle's zip holds `handler.py` and the three new members, the import smoke rc is 0 and the landed bytes equal the built zip; the plan read exactly 0 add / 2 change / 0 destroy on the two addresses with the memory line 3008 to 8192, and the post-apply plan read No changes. Base: FAIL (no record).
<criterion id="DBB123-2-AC1" cell_refs="DB-b-253"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_hop1apply.py" . DBB123-2-AC1</invocation><expect>DBB123-2-AC1 PASS</expect></criterion>
`DBB123-2-AC1` -- FRESH live reads by the checker: the function reads memory 8192, timeout 900, handler `handler.lambda_handler`, runtime python3.12, the role, and a `CodeSha256` equal to the landed zip's; the role policy holds exactly the eleven statement ids and its one PutObject statement lists six prefixes incl. `filled_report_values`; the schedule is unchanged (ENABLED, `cron(41 7 ? * MON-FRI *)`, America/New_York). Base: FAIL (no record).
<criterion id="DBB123-3-AC1" cell_refs="DB-b-253"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_hop1apply.py" . DBB123-3-AC1</invocation><expect>DBB123-3-AC1 PASS</expect></criterion>
`DBB123-3-AC1` -- fresh reads: no key under `irpt/49financial/gold/filled_report_values/` was written before the apply finished (a key written by a LATER scheduled fire is expected and passes); the record's invoke count is 0; the ledger's open marker exists (the ledger was not closed). Base: FAIL (no record).

<expected_criteria>DBB123-1-AC1, DBB123-2-AC1, DBB123-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **The signed act, and nothing wider.** Writes to AWS: the ONE bundle upload (a new version of the artifact key), and the ONE Terraform apply (`safe-apply`) of the reporting-gold root creating no resource and changing the two named. **NO invoke of any kind; NO write of any gold object; NO change to the schedule, the role's trust, the timeout, the handler, the runtime, the layers or the environment; NO other root; NO deletion of any object or file; NO `update-function-code`; NO bare `terraform apply`.** If a rollback is needed the revert is a second `safe-apply` of reverted files and the previous artifact version (`before.artifact_previous.version_id`), by the issuer's word.
- **Read-only:** `get-function-configuration`, `iam get-role-policy`, scheduler `get-schedule`, S3 head/get/list of the artifact bucket and the gold prefixes, `terraform fmt/init/validate/plan`.
- **Refusal clause.** STOP and report, writing nothing further, on any of: the packet's bytes or a half differ or do not read SIGNED; an open ledger or marker naming this surface; the live state differing from the packet's section 2; the import smoke failing; a plan with any add, a change count other than 2, any destroy, an address other than the two, or a changed attribute beyond those named; the post-apply plan not reading No changes. After the apply, a STOP is reported with the state left as it is.
- **Row ids** are `IRPT_DASHBD-D2-DB2-S<k>` (the next free `k`); file a row for anything odd and keep working. Commit with `.tools/safe-commit.sh`. ASCII only. **Report once, under 150 words; report each STOP at once.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-253.apply-hop-1-filled-report-values-signed-pair.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 122 (round 124, workstream B-49F), cell `DB-b-253`.
<owned_cells>DB-b-253</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBB123-1-AC1, DBB123-2-AC1, DBB123-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-b-253.apply-hop-1-filled-report-values-signed-pair.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBB123-1-AC1,DBB123-2-AC1,DBB123-3-AC1` BEFORE any flip; pin each artifact row to the commit that carried it. Run each criterion under `timeout 120` from the repository root and record the output and exit code verbatim.
</proof_of_spec>

**REPORT:** once, under 150 words: the three criteria's last lines; the ledger slug; the plan's counts; the function's memory and `CodeSha256` after; the policy's statement count; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: no resource is created, deleted or rewired; the act changes two existing resources in place (the function's memory and code, the role policy's statements). The blast radius is the signed pair's, read by both halves; the root and its state key are the existing ones.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the packet's section 1 lists the four new statements and the extended write list with their derived ARNs, each recounted by the issuer's checkers (rounds 121 and 122); the live role is read in step 0 and the policy again in step 5, and the CTO half accepted the grants.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; no served page changes (the new gold prefix has no reader yet).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the existing schedule is not changed; step 0 and step 5 read it and any difference is a STOP.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the three criteria FAIL at base (no record) and recount from fresh Lambda, IAM, scheduler and S3 reads.
</preflight>
