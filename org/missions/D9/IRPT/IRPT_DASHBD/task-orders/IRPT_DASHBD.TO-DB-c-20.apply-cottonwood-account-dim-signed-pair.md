# TO IRPT_DASHBD.TO-DB-c-20 -- APPLY the signed pair DB-c-19 (blob `ed09e2768f`): step 0 live reads, ledger, build and package-test the zip, upload it, plan, ONE `safe-apply` creating the Cottonwood `account_dim` function, roles and DISABLED schedule, ONE invoke for 2026-10-13, the after-read, then the schedule ENABLED (COO half signed @d405648eff, CTO half signed @055825367e, CTO msg 8218)

<to_id>IRPT_DASHBD.TO-DB-c-20</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_DB-c-19_R123_ACCOUNT_DIM_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_DB-c-19_R123_ACCOUNT_DIM_CTO_HALF.md` (both at packet blob `ed09e2768fd13983291ceafbed44ddd54ac69e13`, sha256 `d42272a594a228e4dd3351f8be9e8d7da1b0a6d7417a8baeffd3925f91db6ee5`), and the CTO's decision C (msg 8167) | **Decomp cell:** `DB-c-20` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 12) | **outcome_ref:** FWD-2, FWD-11, FWD-15 | **depends_on:** DB-c-16, DB-c-17, DB-c-18 (merged @c4d2b97165, @f54c662ab0, @a5929fb06e) and DB-c-19 (merged @a4a8375b21); both halves SIGNED.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, so it carries `a4a8375b21` and `d405648eff`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes, addresses and words only.

**What this order does, in one paragraph.** The Cottonwood `account_dim` gold table has a built, tested and packaged producer (a Lambda that reads two Black Diamond silver partitions and writes ONE gold key) and no live resource. The repo carries its Terraform root `infra/aws/terraform/investor-reporting/account-dim/` (seven resources, the schedule created DISABLED) and its source-map entry `irpt-cot-account-dim-lambda`. You upload its zip, apply the root, invoke the function ONCE for 2026-10-13, check the one key it wrote, and only then enable the schedule. The pair authorises that sequence and nothing wider.

**Read first (all in your worktree):** the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~412/NEVER_WIDEN_PACKET_DB-c-19_R123_ACCOUNT_DIM.md` (whole: Change set, Function, Catch-up first, Keys written, Both branches, Rollback, Questions) and its reads `ACCOUNT_DIM_PACKET_READS_R123.json`; both halves (the CTO half answers the packet's eleven questions); the Terraform root's five files; the Lambda `infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py`; the model of your own prior apply, `org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-9.apply-cottonwood-holdings-performance-signed-pair.md` and your record `deliverables/0.7.0_AE_CloudOps~DB2/COTTONWOOD_APPLY_RECORD_R2.json` (ledger, build, compare, plan, one safe-apply, read-backs, the ENABLE step). Read `infra/aws/terraform/modules/yang-lambda/main.tf`: the function takes its code from the S3 object at `artifact_key` (a `data.aws_s3_object` read at plan), so the zip must be uploaded BEFORE the plan.

**Do, in this order. Record every value named in `ACCOUNT_DIM_APPLY_RECORD.json` as you go.**

0. **Gates, read only (the CTO half's step 0 is part of this).** (a) `git hash-object` the packet equals `ed09e2768fd13983291ceafbed44ddd54ac69e13` (`gates.packet_blob`); both halves read SIGNED at it (`gates.coo_half_signed`, `gates.cto_half_signed`). (b) `git merge-base --is-ancestor a4a8375b21 HEAD` is true. (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the denominator) names `account-dim`, `account_dim` or `irpt-cot-account-dim`; any one open is a STOP. (d) **LIVE, now:** read the bucket policy of `opal-data-cottonwood` (the `DenyForeignFirmPrincipals` fence): the planned execution role name `irpt-cot-account-dim-role` matches a principal it admits (`role/*-cot-*`) and no deny names the `account_dim` prefix (`gates.role_name_matches_cot`, `gates.bucket_policy_admits_role`); and read the layer `irpt-performance-native-layer` (`lambda get-layer-version`, the version the root's data source resolves): it exists (`gates.layer_exists`). Either missing or not matching is a STOP before any write.
1. **Open the NEVER-2 ledger BEFORE any write** with `python .tools/deploy_ledger.py open ...` under `org/critical_paths/change_management/`, naming legs: the artifact upload; the one `safe-apply` creating the seven resources; the one invoke; the after-read; the ENABLE apply; and the first scheduled fire's after-read (a leg that stays OPEN for the issuer). The ledger names the function `irpt-cot-account-dim-lambda`, the role `irpt-cot-account-dim-role`, the schedule `irpt-cot-account-dim-daily` and the artifact object. Commit its `.open_deploys` sentinel at once. Record `ledger_entry` (the slug).
2. **Before reads.** The function, both roles and the schedule do NOT exist (`ResourceNotFoundException` / `NoSuchEntity`; record `before.resources_absent`); the `account_dim` gold prefix holds 0 objects (a fresh LIST; record `before.account_dim_objects`); a LIST of each other gold prefix under `irpt/cottonwood/gold/` (record, per prefix, its object count and newest key in `before.other_gold_prefixes`: the after-read compares against it).
3. **Build, package-test, upload.** (a) `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-account-dim-lambda`: the zip is built, its sha256 printed, nothing uploaded; record `build.zip_sha256` and `build.members` (the zip's member list: it must hold `lambda_function.py` and the 14 staged members of the source-map entry, at their `packaged_as` paths). (b) `ADCOT_ZIP_PATH=<that zip> python -m pytest -q infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_package_resolves.py`; record `build.package_test_rc` (must be 0; a failure is a STOP before upload). (c) Only then the real `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-account-dim-lambda`: it writes ONE new object, `investor-reporting/irpt-cot-account-dim-lambda.zip`, in the lambda-artifacts bucket and records `artifact_sha256` for the entry in the source map; record `build.landed_version_id`, `build.content_sha256` and `build.built_equals_landed` (true when the landed object's content sha256 equals the BUILD_ONLY zip's). Commit the source-map change (the entry's `artifact_sha256` only; the naming gate admits it).
4. **fmt, validate, plan, under the repo's route.** `.tools/terraform.exe` on the root `infra/aws/terraform/investor-reporting/account-dim/`: `fmt -check`, `init`, `validate`, a saved `plan`. **The plan must read** exactly 7 adds, every address containing `irpt_account_dim` (the function and its log group, the execution role and its policy, the scheduler role and its policy, the schedule), the schedule's state `DISABLED`, 0 changes and 0 destroys. Record `plan` {`add`, `add_addresses`, `change`, `destroy`, `retry_policy_words` (the effective scheduler retry policy the plan prints; the CTO half accepts the defaults)}. Any other add, any change, any destroy, or an `ENABLED` state is a STOP.
5. **ONE `safe-apply`** from the saved plan. Read back: the function (`Handler` `lambda_function.lambda_handler`, `Runtime` `python3.12`, the role `irpt-cot-account-dim-role`, the layer attached), both roles, the schedule (`DISABLED`). A post-apply plan must read `No changes` (`plan.replan_no_changes`). Stamp the deploy as the model does. Record `apply_started_utc` as the UTC instant just BEFORE the invoke (step 6), `YYYY-MM-DDTHH:MM:SSZ`.
6. **The ONE invoke.** The only invoke this order permits is of `irpt-cot-account-dim-lambda` with the event `{"date": "2026-10-13"}`, ONCE. Record `invoke` {`date`, `count` (1), `landed` (true or false), `response_words` (the response's fields, no value beyond counts and the key list)}. No second invoke, no dry-run invoke of a different date, no retry: a failure goes to Both branches of the packet (absent silver or any raise: STOP, the schedule stays DISABLED, the resources stay; an `StreamWriteUnverified` raise: the CTO half's answer 7, read the object left at the key, valid parquet with the expected columns and row count is ACCEPTED and recorded, otherwise report and do nothing: its removal is Andrew's delete; never overwrite it through another path).
7. **The after-read.** (a) A fresh LIST of the `account_dim` gold prefix: EXACTLY one key, `irpt/cottonwood/gold/account_dim/date=2026-10-13/data.parquet`, with `LastModified` at or after `apply_started_utc`; record `after.keys`, `after.size`, `after.etag` (from head-object). (b) Read the parquet back: `after.rows` (its row count) and `after.schema_hash`, computed by the method in `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json` (`schema_hash_basis`), equal to that file's `schema_hash` (`after.schema_hash_equals_contract`). (c) The two silver partitions of 2026-10-13 still exist and the partition counts equal the packet's reads (`after.silver_unchanged`). (d) Every other gold prefix under `irpt/cottonwood/gold/` shows no key written by THIS act: compare with `before.other_gold_prefixes`, accounting for the 08:15 holdings-performance scheduled fire if the window spans it (record the comparison in words as `after.other_prefixes_unchanged`, true when only that scheduled fire moved a key). Any miss is a STOP: the schedule is NOT enabled.
8. **ENABLE, only now.** Edit `infra/aws/terraform/investor-reporting/account-dim/schedule.tf`: the single line `state = "DISABLED"` becomes `state = "ENABLED"`; nothing else in the file moves (the file's comments may keep the word ENABLED only where the order of the original text did; the line is the only change). Commit that change. A plan must read `0 to add, 1 to change, 0 to destroy` (the schedule); record `enable.plan` {`add`, `change`, `destroy`} and `enable.after_read_before_enable` (true). ONE `safe-apply`; read back the schedule: `ENABLED`, `cron(45 8 ? * MON-FRI *)`, `America/New_York`, target the function.
9. **Do NOT close the ledger.** The first scheduled fire's after-read is the issuer's: the next 08:45 New York fire after the apply computes T-1 from its own clock and writes one new key or returns a named hold. Record `ledger_closed` false. Stale OPEN marker copies on other worktrees are named, never closed.

Write `ACCOUNT_DIM_APPLY_RECORD.json` in your folder with exactly: `claim` ("measured"); `gates` {`packet_blob`, `coo_half_signed`, `cto_half_signed`, `role_name_matches_cot`, `bucket_policy_admits_role`, `layer_exists`}; `ledger_entry`; `before` {`resources_absent` {`function`, `role`, `scheduler_role`, `schedule`}, `account_dim_objects`, `other_gold_prefixes`}; `build` {`zip_sha256`, `members`, `package_test_rc`, `landed_version_id`, `content_sha256`, `built_equals_landed`}; `plan` {`add`, `add_addresses`, `change`, `destroy`, `retry_policy_words`, `replan_no_changes`}; `apply_started_utc`; `invoke`; `after` {`keys`, `size`, `etag`, `rows`, `schema_hash`, `schema_hash_equals_contract`, `silver_unchanged`, `other_prefixes_unchanged`}; `enable` {`plan` {`add`, `change`, `destroy`}, `after_read_before_enable`}; `ledger_closed`; `reads` {`vendor_calls` 0, `secret_reads` 0}. Counts, dates, keys, hashes, addresses and words only.

<criterion id="DBC125-1-AC1" cell_refs="DB-c-20"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r125/p125_bcw.py" . DBC125-1-AC1</invocation><expect>DBC125-1-AC1 PASS</expect></criterion>
`DBC125-1-AC1` -- the packet blob is the signed one and both halves read SIGNED at it; the step-0 gates are recorded true; the ledger entry exists and names the function; the build record shows the package test rc 0 and the landed zip equal to the built zip; the plan added exactly 7 resources, all `irpt_account_dim`, changed and destroyed none, and the post-apply plan read No changes. Base: FAIL (no record).

<criterion id="DBC125-2-AC1" cell_refs="DB-c-20"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r125/p125_bcw.py" . DBC125-2-AC1</invocation><expect>DBC125-2-AC1 PASS</expect></criterion>
`DBC125-2-AC1` -- fresh reads: the `account_dim` gold prefix holds exactly the one key `date=2026-10-13/data.parquet` (builder `address()` output), its size and ETag equal the record, it was written inside the apply window, its parquet reads back with the recorded row count and a schema hash equal to the contract's, and the invoke count was 1. Base: FAIL (no record).

<criterion id="DBC125-3-AC1" cell_refs="DB-c-20"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r125/p125_bcw.py" . DBC125-3-AC1</invocation><expect>DBC125-3-AC1 PASS</expect></criterion>
`DBC125-3-AC1` -- fresh live reads: the function exists with handler `lambda_function.lambda_handler`, runtime `python3.12`, the role `irpt-cot-account-dim-role` and a layer; the schedule is ENABLED at `cron(45 8 ? * MON-FRI *)` `America/New_York` and targets the function; the enable step was a 0/1/0 plan after the after-read; the ledger was not closed. Base: FAIL (no record).

<expected_criteria>DBC125-1-AC1, DBC125-2-AC1, DBC125-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **The signed act, and nothing wider.** Writes to AWS: the ONE zip upload (the artifact key above), the Terraform applies (two `safe-apply` runs: the create set, then the one-line ENABLE), and the ONE gold key written by the function's single invoke (`irpt/cottonwood/gold/account_dim/date=2026-10-13/data.parquet` in `opal-data-cottonwood`). **NO other invoke, NO second invoke, NO invoke with another date; NO write of any other key or table; NO backfill; NO change to the holdings-performance function, schedule, role or root; NO schedule, IAM or permission change beyond the plan's seven adds; NO deletion of any object or file (deletes are Andrew's, registered as ONE call with the exact key only if a rollback is needed); NO change to `account_return_daily`, to `sources.json` or to the portal.** Plans and applies run through `.tools/safe-apply.sh` only (never a bare `terraform apply`, never `aws lambda update-function-code`).
- **Read-only:** bucket policy get, `lambda get-layer-version`, `get-function-configuration`, `iam get-role`, scheduler `get-schedule`, S3 head/get/list of the gold prefixes and the silver partitions, `terraform fmt/init/validate/plan`.
- **Refusal clause.** STOP and report, writing nothing further, on any of: the packet blob differs; a half does not read SIGNED at it; an open ledger or marker naming this surface; the bucket fence not admitting the role name, or the layer absent; the package test failing; a plan with an add outside `irpt_account_dim`, a count other than 7, any change, any destroy or an ENABLED schedule; an invoke that raises (the packet's Both branches then govern: nothing is retried); more than one key under the `account_dim` prefix; a date other than 2026-10-13. After the apply, a STOP is reported with the state left as it is: the rollback is Andrew's delete and the schedule stays DISABLED.
- **Row ids** are `IRPT_DASHBD-D2-DB2-S<k>` (the next free `k`); file a row for anything odd and keep working. Commit with `.tools/safe-commit.sh`. ASCII only. **Report once, under 150 words; report each STOP at once.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-20.apply-cottonwood-account-dim-signed-pair.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/investor-reporting/account-dim/schedule.tf
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 12, cell `DB-c-20`.
<owned_cells>DB-c-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC125-1-AC1, DBC125-2-AC1, DBC125-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-c-20.apply-cottonwood-account-dim-signed-pair.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC125-1-AC1,DBC125-2-AC1,DBC125-3-AC1` BEFORE any flip; pin each artifact row to the commit that carried it. Run each criterion under `timeout 120` from the repository root and record the output and exit code verbatim.
</proof_of_spec>

**REPORT:** once, under 150 words: the three criteria's last lines; the ledger slug; the plan's add count; the invoke's result and the one key; the schedule's state; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: no resource is deleted or rewired; the act is additive: seven new resources, one artifact object and one gold key. The blast radius is the signed pair's, read by both halves; the new root has its own state key and touches no other root.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the execution role and the scheduler role do not exist yet (NoSuchEntity, read by the worker of DB-c-19), so comp-iam has no principal to read; the CTO half read the fence of the gold bucket and step 0 re-reads it live. The applier runs comp-iam gaps on the new role after the apply (step 5 read-backs).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; no served page is changed by the act (the one reader of the table is an internal reporting build that takes the newest partition).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the new schedule does not exist yet (ResourceNotFoundException, read by the worker of DB-c-19); it is created DISABLED and enabled only after the after-read; no other schedule changes.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the three criteria FAIL at base (no record) and recount from fresh Lambda, scheduler and S3 reads.
</preflight>
