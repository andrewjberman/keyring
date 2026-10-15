# TO IRPT_DASHBD.TO-DB-b-276 -- APPLY the signed Cottonwood report-build CODE-UPDATE pair for the chain cap (packet sha256 `0ba134ff507a`): step 0 gates and live reads, ledger legs, build-only hash, the MEMBER DIFF against LIVE (exactly `handler.py`), ONE new artifact version, plan 0/1/0, ONE `safe-apply`, the read-backs, three events that write nothing, the r139 ledger closed (COO half signed @06f471310e, CTO half signed @38966dc091, CTO msg 8682)

<to_id>IRPT_DASHBD.TO-DB-b-276</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>143</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_REPORTING_GOLD_CODE_UPDATE_CHAIN_CAP_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_REPORTING_GOLD_CODE_UPDATE_CHAIN_CAP_CTO_HALF.md` (both at the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_REPORTING_GOLD_CODE_UPDATE_CHAIN_CAP.md`, sha256 `0ba134ff507a525437ea18ca93d05f58963505cb8bc0b2454cbff789b044f6ae`) and the CTO's rounds 138-141 analysis @7fdfe4f6e6 (msg 8673) | **Decomp cell:** `DB-b-276` (decomposition section 141) | **outcome_ref:** FWD-1 | **depends_on:** `DB-b-274` (merged, the pin commit `24b4b16305`), `DB-b-272` (the live function) and both halves SIGNED.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying `24b4b16305` and the halves); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes, addresses and words only; never an account or household id.

**What this order does, in one paragraph.** The live function `irpt-cot-reporting-gold-lambda` runs the handler that chains to the END of the owed days (row `IRPT_DASHBD-D2-S95`, ARMED). Round 141 put a chain budget in the repo's handler; this order puts it in the function. You build the bundle, prove by a MEMBER DIFF against the live artifact that exactly one member, `handler.py`, differs, upload ONE new version of the existing key, run `terraform plan` (the root's first change plan), and, only if it reads EXACTLY 0 add / 1 change / 0 destroy on the one function with exactly two attributes changing, make ONE `safe-apply`. Then you invoke the function three times, synchronously; none of them writes an object. You enable NOTHING and delete NOTHING.

**Read first (all in your worktree):** the packet (whole, sections 1 to 10) and its COO half; the CTO half (its answers); `infra/aws/terraform/investor-reporting/reporting-gold-iso/` and the module `infra/aws/terraform/modules/yang-lambda/main.tf` (the data source `aws_s3_object.artifact` gives `version_id` and the `content-sha256` metadata, so a new artifact version is exactly a 0/1/0 plan on `aws_lambda_function.this`); `infra/aws/lambda/ci/lambda-source-map.json` entry `irpt-cot-reporting-gold-lambda`; `infra/aws/lambda/ci/build-and-upload.sh`; the handler `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` (`_chain_left`, `chain_next`, `lambda_handler`); your own prior record `COT_REPORT_APPLY_RECORD.json` of order `IRPT_DASHBD.TO-DB-b-272...` and its ledger. **Lessons of the last apply, applied here:** `--cli-read-timeout 0` on every invoke; the CLI default of 60 s loses synchronous responses; the artifact key is read from the source map, never typed from this order; write into the source map only the one `artifact_sha256` field the upload script updates; **copy the safe-apply gate footprint into your ledger entry BEFORE you remove any worktree** (the CTO's term: the r139 apply left none).

**Do, in this order. Record every value named in `COT_CODE_UPDATE_RECORD.json` as you go.**

0. **Gates, read only.** (a) `git hash-object` of the packet equals the blob recorded in the CTO half and its sha256 equals `0ba134ff507a525437ea18ca93d05f58963505cb8bc0b2454cbff789b044f6ae`; both halves read SIGNED at it (`gates.packet_blob`, `gates.packet_sha256`, `gates.coo_half_signed`, `gates.cto_half_signed`). (b) `git merge-base --is-ancestor 24b4b16305 HEAD` is true (`gates.pin_is_ancestor`). (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the denominator) names the `reporting-gold-iso` root, `irpt-cot-reporting-gold` or the prefix `irpt/cottonwood/gold/filled_report_values`, EXCEPT the open r139 ledger `irpt-dashbd-cottonwood-reporting-gold-20261015`, which this order reuses and closes; any OTHER open one is a STOP (`gates.one_change_at_a_time` {`worktrees_read`, `open_markers_naming_this_surface` (the count of OTHERS, 0)}). (d) **LIVE, now (`gates.live_matches_packet`):** the function's `CodeSha256` equals `8pQOR3TN3iicEFV53N7Cs0yeensgZhPDd7zEwTZO3Z4=`; the artifact key holds exactly ONE version; the schedule `irpt-cot-reporting-gold-daily` is DISABLED; the filled prefix holds 65 objects.
1. **Reuse the ledger, new legs, BEFORE any write.** `python .tools/deploy_ledger.py` on `irpt-dashbd-cottonwood-reporting-gold-20261015` (its sentinel is merged on trunk): legs L6 git (the tree commit and the sha256 of `handler.py`, expected first 12 hex `398d0b996d3d`), L7 build and member diff, L8 terraform (the plan 0/1/0, then the apply), L9 after-read (the three events). Commit the leg opening at once. Record `ledger_entry` (the slug).
2. **Before reads.** `before` {`code_sha256` (the function's, equal to step 0(d)), `artifact_version_id` (the key's one version), `artifact_versions` (1), `filled_objects` (a fresh LIST count: 65), `schedule_state` ("DISABLED")}.
3. **Build, the MEMBER DIFF, upload.** (a) `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-reporting-gold-lambda`: the zip is built, its base64 sha256 printed, nothing uploaded; **it must equal `7FYx8sPkt0I25tZ8POS3HIueH0lJ99aGjppTky9E7DE=` or STOP and say why**; record `build.zip_sha256` (hex) and `build.zip_sha256_b64`. (b) **The member diff against LIVE:** download the LIVE artifact's current version (the version named by `before.artifact_version_id`), unzip it and the built zip to two fresh temporary directories, compare the member LISTS and every member's sha256. **It must read the same member list and EXACTLY ONE differing member, `handler.py`; anything else is a STOP before the upload.** Record `build.member_diff` {`live_members`, `new_members`, `differing` (["handler.py"])}. (c) The real `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-reporting-gold-lambda`: it writes ONE new version of the existing key (the old one stays) and updates the entry's `artifact_sha256` only; record `build.landed_version_id` (a NEW id, not the live one), `build.content_sha256` (hex sha256 of the landed object's bytes) and `build.built_equals_landed`. Commit the source-map change (the entry's `artifact_sha256` only).
4. **fmt, validate, plan, under the repo's route.** `.tools/terraform.exe` on `infra/aws/terraform/investor-reporting/reporting-gold-iso/`: `fmt -check`, `init`, `validate`, a saved `plan`. **The plan must read EXACTLY** 0 to add, 1 to change, 0 to destroy, the one change being `module.irpt_reporting_gold_iso.aws_lambda_function.this`, and the attributes that change being EXACTLY `s3_object_version` and `source_code_hash` (an in-place update; any other attribute, a replacement, or any other resource is a STOP). Record `plan` {`add` 0, `change` 1, `destroy` 0, `addresses` (the one address as the plan prints it), `attributes` (["s3_object_version", "source_code_hash"]), `replan_no_changes`}.
5. **ONE `safe-apply`** from the saved plan (`.tools/safe-apply.sh`; never a bare `terraform apply`, never `aws lambda update-function-code`). **Copy the gate footprint into the ledger entry now.** Read back: the function (`MemorySize` 1024, `Timeout` 900, `Handler` `handler.lambda_handler`, `Runtime` `python3.12`, the execution role, `CodeSha256` equal to `build.zip_sha256_b64`, no reserved concurrency, no environment variable, the one layer ARN), the schedule (`DISABLED`, `cron(15 9 ? * MON-FRI *)`, America/New_York). A post-apply plan must read `No changes` (`plan.replan_no_changes` true). Stamp the deploy as your earlier applies do. Record `apply_finished_utc` and `after` {`function` {`memory`, `timeout`, `reserved_concurrency` (null), `handler`, `runtime`, `code_sha256`, `layer_arn`, `environment` (null)}, `schedule` {`state`, `cron`}}.
6. **Act 3: three synchronous events that write nothing.** Only if steps 0 to 5 all passed. Each `aws lambda invoke --cli-read-timeout 0`, `--invocation-type RequestResponse`, `--log-type Tail`; ONE invocation each; no retry. (a) payload exactly `{}`: expect `result.skipped` `NOTHING_OWED`. (b) payload exactly `{"day": "2026-10-14", "dry_run": true}`: expect 200, `result.skipped` `LANDED` and `chain.invoked` false (or no chain). (c) payload exactly `{"day": "2026-10-14", "chain_left": 10}`: expect a FUNCTION ERROR whose message names `chain_left` and `REFUSED` (the one expected error). Record `events` {`empty`, `landed_dry_run`, `refused`}, each {`payload`, `invoked_utc`, `invocation_type` "RequestResponse", `status_code` (200), `function_error` (null for the first two, the error type for the third), `returned` (the response body for the first two; null for the third), `request_id`} plus `max_memory_used_mb` (from the tail's REPORT line) for the first two and `error_text` (the error message, no ids) for the third. **STOP at once** on any other function error, a `Max Memory Used` above 717 MB, or a LIST of the filled prefix that reads other than 65 objects or shows an object newer than `apply_finished_utc`. Record `filled_after` {`objects` (65), `newest_after_apply` (false)}.
7. **Close the r139 ledger** `irpt-dashbd-cottonwood-reporting-gold-20261015` with the repo's route (after the after-read, naming this pair's packet sha256); record `r139_ledger_closed` true and `gate_footprint_in_ledger` true. **NO enable, NO other invoke, NO delete.** Stale OPEN marker copies on other worktrees are named, never closed.

Write `COT_CODE_UPDATE_RECORD.json` in your folder with exactly: `claim` ("measured"); `gates`; `ledger_entry`; `before`; `build` {`zip_sha256`, `zip_sha256_b64`, `member_diff`, `landed_version_id`, `content_sha256`, `built_equals_landed`}; `plan`; `apply_finished_utc`; `after`; `events`; `filled_after`; `r139_ledger_closed`; `gate_footprint_in_ledger`; `reads` {`vendor_calls` 0, `secret_reads` 0}. Counts, dates, keys, hashes, addresses and words only.

<criterion id="DBC143-1-AC1" cell_refs="DB-b-276"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r143/p143_codeupdate.py" . DBC143-1-AC1</invocation><expect>DBC143-1-AC1 PASS</expect></criterion>
`DBC143-1-AC1` -- the packet's bytes and sha256 are the signed ones and both halves read SIGNED at it; the step-0 gates are recorded true with the worktree denominator; the ledger entry exists; the live state before equals the packet's section 3; the build's sha256 equals the packet's, the member diff against LIVE reads the same member list and exactly one differing member, `handler.py`, and the landed object is a NEW version holding the built bytes; the plan read exactly 0 add / 1 change / 0 destroy on the one function with exactly the two attributes and the post-apply plan read No changes. Base: FAIL (no record).
<criterion id="DBC143-2-AC1" cell_refs="DB-b-276"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r143/p143_codeupdate.py" . DBC143-2-AC1</invocation><expect>DBC143-2-AC1 PASS</expect></criterion>
`DBC143-2-AC1` -- FRESH live reads by the checker: the function reads memory 1024, timeout 900, handler `handler.lambda_handler`, runtime python3.12, the execution role, no reserved concurrency, no environment variable, a `CodeSha256` equal to the landed zip's and exactly one layer; the schedule is DISABLED with the packet's cron and zone; the artifact key holds both the previous version and the landed one with the landed one current (nothing deleted); the record's events clauses hold. Base: FAIL (no record).
<criterion id="DBC143-3-AC1" cell_refs="DB-b-276"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r143/p143_codeupdate.py" . DBC143-3-AC1</invocation><expect>DBC143-3-AC1 PASS</expect></criterion>
`DBC143-3-AC1` -- fresh reads: the filled prefix still holds exactly 65 objects and none is newer than the apply; no REPORT line in the function's log group reads above 717 MB and one equals the empty event's recorded value; the three events read as the packet states (NOTHING_OWED; LANDED with no chain; one refused event naming `chain_left` and REFUSED); the r139 ledger's open marker is gone (the ledger is closed). Base: FAIL (no record).

<expected_criteria>DBC143-1-AC1, DBC143-2-AC1, DBC143-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the ONE bundle upload (a NEW version of the existing key), the ONE Terraform apply (`safe-apply`) changing the one function, and the three invokes of Act 3 (none writes an object). **NO other invoke; NO `day` event but the two named; NO write to any gold object; NO enable of the schedule; NO other resource; NO deletion of any object, version or file (the previous artifact version stays); NO `update-function-code`; NO bare `terraform apply`.** If a rollback is needed the revert is a new pair that repoints the function at the previous artifact version, with the CTO's word.
- **Read-only:** `get-function-configuration`, `get-function-concurrency`, `scheduler get-schedule`, S3 head/get/list of the artifact bucket (including `list-object-versions`) and the gold prefixes, `logs filter-log-events`, `terraform fmt/init/validate/plan`.
- **Refusal clause.** STOP and report, writing nothing further, on any of: the packet's bytes or a half differ or do not read SIGNED; an open ledger or marker other than the r139 one naming this surface; the live state differing from the packet's section 3; the build line differing from the packet's value; the member diff reading anything but `handler.py`; a plan with any change count other than 0/1/0, an address other than the one function, an attribute beyond the two, or a replacement; the post-apply plan not reading No changes; after any event, a stop condition of step 6. After the apply, a STOP is reported with the state left as it is.
- **Row ids** are `IRPT_DASHBD-D2-DB2-S<k>` (the next free `k`); file a row for anything odd and keep working. Commit with `.tools/safe-commit.sh`. ASCII only. **Report once, under 150 words; report each STOP at once.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-276.apply-cottonwood-reporting-gold-code-update-chain-cap-signed-pair.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 141 (round 143, workstream B-49F), cell `DB-b-276`.
<owned_cells>DB-b-276</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC143-1-AC1, DBC143-2-AC1, DBC143-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-b-276.apply-cottonwood-reporting-gold-code-update-chain-cap-signed-pair.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC143-1-AC1,DBC143-2-AC1,DBC143-3-AC1` BEFORE any flip; pin each artifact row to the commit that carried it. Run each criterion under `timeout 300` from the repository root and record the output and exit code verbatim.
</proof_of_spec>

**REPORT:** once, under 150 words: the three criteria's last lines; the member diff's result; the plan's counts and attributes; the function's `CodeSha256` after; the three events' outcomes; the filled prefix count; the ledger state; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the apply changes ONE existing function's code (an in-place update of two attributes) and creates one new artifact object version; no gold object is written. The blast radius is the signed pair's, read by both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role, policy or grant changes; the plan must read one function change only, and the live role policy was read back by the round-139 apply.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; no served page changes (the filled prefix has no established reader).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is DISABLED and is not touched; step 5 and the criteria read its state.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the three criteria FAIL at base (no record) and recount from fresh Lambda, S3, scheduler and log reads; the record clauses are exercised by the checker's self-test (one green and 47 red arms).
</preflight>
