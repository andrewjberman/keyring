# TO IRPT_DASHBD.TO-DB-b-312 -- APPLY the signed 49 Financial reporting-publish pair (packet sha256 `e6af7a92148d`): gates and live reads, ledger, build-only hash, ONE new bundle version, plan 0/2/0, ONE `safe-apply`, the switch-OFF probe, ONE dry-run shard, the after-read (COO half signed @a30664edac; CTO half signed @6aaa28e481)

<to_id>IRPT_DASHBD.TO-DB-b-312</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PUB49FHOP2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_49F_REPORTING_PUBLISH_HOP2_READER_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_49F_REPORTING_PUBLISH_HOP2_READER_READ_GRANT_CTO_HALF.md` (both at the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_49F_REPORTING_PUBLISH_HOP2_READER_CODE_AND_READ_GRANT.md`, sha256 `e6af7a92148dcaefcfd8375f7421751636429c1e7a19b1de738db4d712d9d698`) | **Decomp cell:** `DB-b-312` (decomposition section 172).

**Risk class WORLD:** an artifact version, the function's code, and two policy entries (READ and LIST of one gold prefix) in a live account. The filled-report switch stays OFF; no served output moves.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet and both halves); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes, addresses and words only; never an account id.

**What this order does, in one paragraph.** The function `irpt-49f-reporting-publish-lambda` runs the 2026-10-16 bundle. The repo now carries the hop-2 reader (`read_filled_report_gold` with the account join and the minted ids) and the publisher's `validate_filled_report`, and the Terraform root's `locals.tf` already lists the filled prefix as a third READ and LIST prefix. You land the new bundle, apply the root once (the function's code and the role policy's two statements), prove the deployed code reads the switch as OFF, and prove an existing path still works.

**Read first (all in your worktree):** the packet (whole), its COO half and the CTO half; `infra/aws/terraform/investor-reporting/reporting-publish/` (`lambda.tf`, `iam.tf`, `locals.tf`, `main.tf`, `schedule.tf`); the entry `irpt-49f-reporting-publish-lambda` in `infra/aws/lambda/ci/lambda-source-map.json` (its `artifact_s3_key` read from the map, never typed); `infra/aws/lambda/ci/build-and-upload.sh`; `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (`filled_report_fire`, `lambda_handler`); your own prior applies (`IRPT_DASHBD.TO-DB-b-298...` and its record). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda side (its log), never retried blind; the checker recomputes policy statement hashes with `json.dumps(statement, sort_keys=True, separators=(",", ":"))`.

**Do, in this order. Record every value named in `PUB49F_HOP2_READER_RECORD.json` as you go (keys exactly as listed in the checker `p179_pub49f_hop2_apply.py`).**

0. **Gates, read only.** (a) `git hash-object` of the packet equals `c12b711739d8f5f2528ee05265543bc51a3d8ee3` and its sha256 equals `e6af7a92148dcaefcfd8375f7421751636429c1e7a19b1de738db4d712d9d698`; both halves read SIGNED at it (`gates.packet_blob`, `gates.packet_sha256`, `gates.coo_half_signed`, `gates.cto_half_signed`). (b) The packet's code is an ancestor of HEAD (`git merge-base --is-ancestor 4aca09a82d HEAD`; `gates.pin_is_ancestor`). (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the denominator) names the `reporting-publish` root, `irpt-49f-reporting-publish` or the prefix `irpt/49financial/platinum/reporting`; the Cottonwood ledger is another root (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = 0). (d) The live function and policy equal the packet's section 3 (`gates.live_matches_packet`). Any mismatch: STOP.
1. **Open the NEVER-2 ledger BEFORE any write** with `python .tools/deploy_ledger.py open ...` under `org/critical_paths/change_management/`, slug `irpt-dashbd-49f-publish-hop2-reader-readgrant-20261016`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**, legs: L1 git; L2 build; L3 terraform; L4 probe; L5 dry run; L6 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry` and `applier`.
2. **Before reads.** `before` {`function_code_sha256`, `artifact_version_id` (the key's current version), `policy` (the sha256, full 64 hex, of each statement's canonical JSON, keyed by sid: eight entries), `schedules` ({name: {`state`, `cron`}} for `irpt-49f-reporting-publish-daily` and `irpt-49f-reporting-publish-summaries-daily`), `platinum` ({`objects`, `versions`}: the client-side counts of `list_objects_v2` and `list_object_versions` over `irpt/49financial/platinum/reporting/`, auto-paginated, denominator printed), `filled_prefix_objects` (the count of objects under `irpt/49financial/gold/filled_report_values/`, printed before Act 3)}. **The packet's section 3 called the 18,257 objects the filled prefix's: they are the platinum prefix's (CTO half correction); the filled prefix held one partition.**
3. **Build, import-smoke, upload.** (a) `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-49f-reporting-publish-lambda`: **its base64 sha256 must equal `s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM=` or STOP and say why**; record `build.zip_sha256` (hex), `build.zip_sha256_b64` and `build.members` (must hold `handler.py` and `publisher.py`). (b) **Import smoke:** extract the zip to a fresh temporary directory and, from another directory, run `python -I -c "import sys; sys.path.insert(0, '<dir>'); import handler"`; record `build.import_smoke_rc` (0). (c) The real `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-49f-reporting-publish-lambda`: a NEW VERSION of the key and the entry's `artifact_sha256` updated; record `build.landed_version_id` (different from the before version), `build.content_sha256`, `build.built_equals_landed` (true).
4. **Terraform: gates and ONE `safe-apply`.** `terraform fmt -check` on the root (a failure on a pinned file is a row, not an edit), `validate`, `plan` through the `safe-apply` plan step. **The plan must read exactly 0 to add, 2 to change, 0 to destroy:** `module.irpt_reporting_publish.aws_lambda_function.this` by CODE attributes only, and `aws_iam_role_policy.irpt_reporting_publish` (two statements). Any other line STOPS. Then ONE `safe-apply`; a re-plan afterward reads No changes. Record `plan` {`add`, `change`, `destroy`, `change_addresses`, `function_change_attributes`, `replan_no_changes`} and `apply_finished_utc` (outside 12:05Z to 13:15Z on a weekday).
5. **The probe.** ONE synchronous `{"filled_report": true}`. **The answer must be exactly** `{"enabled": false, "clients": 0, "written": 0, "not_available": [], "refused": []}`. Record `probe` {`payload`, `invoked_utc`, `status_code`, `function_error`, `returned`, `report` {`max_memory_used_mb`, `duration_ms`, `memory_size_mb`}, `request_id`}. Anything else: STOP.
6. **The dry-run shard.** ONE synchronous `{"dry_run": true, "shard": 0, "shards": 7}`. Record `dry_run` with the same keys; `returned` is exactly {`ok`, `accounts`, `refused_count`} (counts, never an id). Expected ok true, about 990 accounts, 0 refused, Max Memory Used at most 819 MB and duration at most 240 s.
7. **The after-read.** `after` {`function` {`memory`, `timeout`, `reserved_concurrency` (null), `code_sha256`, `layer_arn`}, `policy` (the eight statement hashes by sid: the two named ones differ from before, the other six equal), `schedules` (equal to before)}; `platinum_after` ({`objects`, `versions`}, equal to before); `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}.
8. **Receipt** `PUB49F_HOP2_READER_RECORD.json` plus a short words file: the counts, memory and duration, and the sentences "the reader has not run against the real partition" and "the switch is off". Flip this order's status to complete as your last commit.

<criterion id="DBC179-1-AC1" cell_refs="DB-b-312"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p179_pub49f_hop2_apply.py" . DBC179-1-AC1</invocation><expect>DBC179-1-AC1 PASS</expect></criterion>
`DBC179-1-AC1` -- the record's head: packet and halves, gates, ledger and applier, before, build, plan 0/2/0 with the two named addresses, the apply outside the fire window. Base: FAIL (no record).
<criterion id="DBC179-2-AC1" cell_refs="DB-b-312"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p179_pub49f_hop2_apply.py" . DBC179-2-AC1</invocation><expect>DBC179-2-AC1 PASS</expect></criterion>
`DBC179-2-AC1` -- FRESH live reads: the function runs the new code with no environment variable and no reserved concurrency; the policy's List and Read statements carry exactly the one added prefix and six statements are unchanged; both schedules ENABLED; the artifact's current version is the recorded one. Base: FAIL.
<criterion id="DBC179-3-AC1" cell_refs="DB-b-312"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p179_pub49f_hop2_apply.py" . DBC179-3-AC1</invocation><expect>DBC179-3-AC1 PASS</expect></criterion>
`DBC179-3-AC1` -- the probe answered the exact switch-OFF no-op, the dry-run shard returned ok with 0 refusals inside the limits, and the platinum object and version counts are unchanged. Base: FAIL.

<expected_criteria>DBC179-1-AC1,DBC179-2-AC1,DBC179-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the ONE bundle upload (a new version of the key), the ONE Terraform apply (`safe-apply`) of the `reporting-publish` root (0 adds, 2 changes), and the two invokes of steps 5 and 6 (neither writes). No `update-function-code`, no bare `terraform apply`, no delete of any object or version, no schedule change, no environment variable (the switch stays OFF), no event other than the two named. No act between 12:05 and 13:15 UTC on a weekday.
- **Stop rules.** A `Task timed out`, an `AccessDenied`, a Max Memory Used above 819 MB, a plan line outside the gate, a build hash that differs, or a probe answer other than the exact one: STOP at once and report to the issuer; the rollback is the prior artifact version `41lfCmfJWyvHbzqC3VtGeHVm6VJ4gRZb` and the prior `locals.tf`, both through `safe-apply`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB3-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-312.apply-49f-publish-hop2-reader-and-read-grant.md
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 172 (round 149, workstream PUB49FHOP2), cell `DB-b-312`.
<owned_cells>DB-b-312</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC179-1-AC1, DBC179-2-AC1, DBC179-3-AC1 (mechanical, WORLD). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-312.apply-49f-publish-hop2-reader-and-read-grant.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC179-1-AC1,DBC179-2-AC1,DBC179-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument).
</proof_of_spec>

**REPORT:** once, under 150 words: the three criteria's last lines; the ledger slug; the plan's counts; the function's memory, layer and `CodeSha256` after; the probe's answer; the dry run's Max Memory Used and duration; the platinum and filled-prefix counts.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED -- reason: the Terraform root `reporting-publish` is the one writer of the function's code and the role policy; the plan gate (0/2/0) is the blast bound; the applier reads the plan before the apply.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the issuer read the live role policy with get-role-policy (eight statements) and the applier re-reads it; the role gains READ and LIST of one gold prefix of the firm's own bucket, no write, no new principal; the plan gate (0/2/0) bounds it.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the applier reads both schedules before and after and the checker requires them unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the issuer's checker selftest is green on a synthetic record and red on 26 single-fault arms.
lane: the <paths> block IS the grant.
</preflight>
