# TO IRPT_DASHBD.TO-DB-b-328 -- APPLY the signed filled-report switch-on pair (packet sha256 `3248f3c4`): gates and live reads, ledger, the bundle, a code-only `safe-apply` and the OFF no-op probe, ONE `safe-apply` of the one variable, a dry run in seven shards, ONE canary, the mint leg and `~S2`'s V leg, the full pass in seven shards, the after-read (IB-pr-551 hop 2; CTO msgs 10294, 10295, 10307, 10331) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-328</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>FILLAPPLY</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_49F_FILLED_REPORT_SWITCH_ON_FIRST_PASS_COO_HALF.md` @a1e2575ac6 and CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_49F_FILLED_REPORT_SWITCH_ON_FIRST_PASS_CTO_HALF.md` @a824aebb24, both bound to the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_49F_FILLED_REPORT_SWITCH_ON_FIRST_PASS.md` (sha256 `3248f3c488fff06b00a165ee5a98da0bd0f509a013d23238dd8590af04290573`) | **Decomp cell:** `DB-b-328` (decomposition section 187).

**Risk class WORLD, client-facing documents:** a code change and ONE environment variable on `irpt-49f-reporting-publish-lambda`, then one new object per directory client at `client=<id>/filled_report.json`. Nothing else is written. Written documents STAY on a rollback (a delete needs a human).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet, both halves, the options code at `4d4cf3e2c4` and the read tools); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** **No client id, name, address, password, token or response body appears in any file, commit message, row, log line or message you send. The canary is named ONLY by the first 12 hex of the sha256 of its id; its id travels by broker to `2.0.0_SA_COO~S2` only.** Counts, hashes, statuses and words only.

**Read first (all in your worktree):** the packet (whole), both halves; `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (the FILLED-REPORT-A block: `_filled_options`, `filled_report_fire`, `run_filled_report`); `infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf` and `iam.tf`; the function-map entry `infra/aws/lambda/ci/function-map/irpt-49f-reporting-publish-lambda.json`; `infra/aws/lambda/ci/build-and-upload.sh`; your own earlier applies (`IRPT_DASHBD.TO-DB-b-312...` and `-323...`) and the mint helpers `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` and `.../0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py`; the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p194_filled_pass_apply.py` (the record's exact keys). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda log, never retried blind; an invoke response is read for counts and the log's REPORT line only; no act in a weekday fire window (12:05 to 13:15 UTC); the sequence is the packet's, and a STOP line stops the pair.

**Do, in this order. Record every value named in `FILLED_PASS_APPLY_RECORD.json` as you go.**

0. **Gates, read only.** (a) The packet's sha256 equals the one above (`gates.packet_sha256`); both halves read SIGNED at it. (b) The options code is an ancestor of HEAD (`git merge-base --is-ancestor 4d4cf3e2c4 HEAD`). (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (print the denominator) has an OPEN LEG on `irpt-49f-reporting-publish-lambda`, the root `reporting-publish`, or the prefix `irpt/49financial/platinum/reporting` (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = the count of open legs on this surface, 0). (d) The live state equals the packet's section 2 (`gates.live_matches_packet`). Any mismatch: STOP.
1. **Open the NEVER-2 ledger BEFORE any write:** `python .tools/deploy_ledger.py open ...`, slug `irpt-dashbd-49f-filled-report-switch-on-first-pass-20261017`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**; legs: L1 git; L2 build; L3 terraform (code, switch); L4 dry run; L5 canary and V leg; L6 full pass; L7 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry`.
2. **Before reads** `before` {`code_sha256` (the function's live CodeSha256: expected `s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM=`), `artifact_version_id` (the key's current version: expected `oXM0wQg8revg3asMHOhpbz1gPDnXaatK`), `env_keys` (sorted names only: expected []), `schedules` (the three schedule names, all ENABLED), `series_prefixes` (the `account=` prefixes by one delimiter listing, auto-paginated), `summary_objects` (`client=*/summary.json` objects), `filled_objects` (`client=*/filled_report.json`, expected 0), `other_objects` (every other key), `role_policy_hash16` (first 16 hex of the sha256 of the role policy `irpt-49f-reporting-publish-policy` JSON, sorted keys, compact separators: expected `e6a7e585f3021a05`)}; counts client-side over every page of `irpt/49financial/platinum/reporting/` in `opal-data-49financial`, denominator printed.
3. **Act 1 -- the bundle.** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-49f-reporting-publish-lambda`: **its base64 sha256 must equal `4SF81dqnVu8rqP3xT0dWtQ8br1w9hvjQft/0knAtaic=` (17 members) or STOP and say why.** Then the real build-and-upload: a NEW VERSION of the key and the entry's `artifact_sha256` updated (commit that one field with your receipt). Record `build` {`zip_sha256_b64`, `members`, `landed_version_id`}.
4. **Act 2 -- code only.** `terraform fmt -check`, `validate`, the `safe-apply` plan step on `infra/aws/terraform/investor-reporting/reporting-publish/`. **The plan must read exactly 0 to add, 1 to change, 0 to destroy:** `module.irpt_reporting_publish.aws_lambda_function.this` by CODE attributes only. Any other line STOPS. ONE `safe-apply`; a re-plan afterward reads No changes. Record `plans.code`. **Probe:** one synchronous `{"filled_report": true, "clients": ["cli_PROBE"], "shard": 99, "shards": 7}` with the switch still OFF: the response must be EXACTLY `{"enabled": false, "clients": 0, "written": 0, "not_available": [], "refused": []}` or STOP. Record `probe_off` {`response`, `payload_shape` "clients+shard+shards"}.
5. **Act 3 -- the switch.** Read each of the three schedules' target INPUT (read only) and record `schedule_inputs` {`checked` 3, `none_contains_filled_report`}; if any contains a `filled_report` event, STOP. Then add the one environment line to `reporting-publish/lambda.tf` in your worktree (`environment_variables = { FILLED_REPORT_PASS = "1" }` on the yang-lambda module call; read the module's variable name first) and ONE `safe-apply`: **exactly 0 to add, 1 to change, 0 to destroy**, the same function by its ENVIRONMENT only. A re-plan reads No changes. Record `plans.switch`. Commit the `lambda.tf` line with the receipt.
6. **Act 4 -- the dry run.** Read the directory's client count (the Cottonwood-style `read_directory` for the firm 49financial, counts only). Then seven synchronous events `{"filled_report": true, "dry_run": true, "shard": k, "shards": 7}`, k = 0..6. Per shard record `{shard, clients, written (the would-be count), not_available (a count), refused (a count), max_memory_mb, duration_s}` from the response and the REPORT line. **STOP** on a timeout, an `AccessDenied`, Max Memory above 819 MB, a duration above 240 s, `enabled` false, or refused above 10 percent of the clients. The object count of the reporting prefix is read before and after the seven events and must be EQUAL. Record `dry_run` {`directory_clients`, `shards`, `objects_before`, `objects_after`}.
7. **Act 5 -- the canary.** Choose the first client, in sorted order, whose single-client dry run (`{"filled_report": true, "clients": ["<id>"], "dry_run": true}`) reads `written` 1, `not_available` 0, `refused` 0. Run ONE `{"filled_report": true, "clients": ["<id>"]}`. The object `irpt/49financial/platinum/reporting/client=<id>/filled_report.json` must exist (head), validate against the contract (`publisher.validate_filled_report` on the read-back, in memory), and the prefix must gain exactly 1 object. Record `canary` {`client_digest12`, `dry_run_written` 1, `clients` 1, `written` 1, `object_exists`, `validates`, `prefix_gain`}. **Send the canary id to `2.0.0_SA_COO~S2` by ONE broker message** (subject "canary client for the V leg") and nowhere else.
8. **Act 6 -- the mint leg and `~S2`'s V leg.** Mint two synthetic principals in `opal-users-v2` with `@opal.invalid` addresses, recorded by their 12-hex digests: CANARY-VIEWER (scoped to the canary client's accounts) and CONTROL-VIEWER (the same firm, without that client), with the helper family above (read-back required; passwords generated in memory, on STDIN only, never argv, a file, a log or a message except the sign-in hand-over to `~S2`). Sign both in and hand the SESSIONS to `~S2` by broker, never a file. `~S2` grades its steps (1) the object exists, (2) the route answers 200 with a body whose sha256 equals the object's for CANARY-VIEWER and a coverage refusal for CONTROL-VIEWER, (3) one export renders a bundle whose filled body equals the same sha256, and tells you by broker. **If a covering and a non-covering principal cannot be scoped without hand-typing a user-to-advisor link or using a credential no seat holds, mint nothing, say why in `notes`, and record `s2_step2` "OWED".** Then REMOVE both rows and read each ABSENT twice (a minute apart). A `~S2` grade of LEAK (CONTROL-VIEWER reading the body) STOPS the pair before step 9, after both rows are removed. Record `v_leg` {`principals` (two 12-hex digests; when nothing was minted, two zero-digests `000000000000`, `s2_step2` "OWED" and the reason in `notes`), `signins_ok`, `s2_step1`, `s2_step2`, `s2_step3`, `leak`, `removed`, `absent_reads` (two entries {`gsi`, `consistent`})}.
9. **Act 7 -- the full pass.** Seven synchronous events `{"filled_report": true, "shard": k, "shards": 7}`, k = 0..6 (the canary is rewritten once, as a new version of the same key). Per shard the same fields as step 6. **The seven `clients`, `written`, `not_available` and `refused` must equal the dry run's sums** or STOP. Record `full` {`shards`, `written_total`, `objects_before` (read just before the first event), `objects_after` (just after the last)}: the prefix must gain exactly the dry run's would-be total minus 1.
10. **Act 8 -- the after-read and the receipt.** `after` {`function` {`code_sha256`, `memory_mb`, `timeout_s`, `env_keys` (expected ["FILLED_REPORT_PASS"]), `layer` (the layer ARN's name:version), `reserved_concurrency` (null)}, `role_policy_hash16` (equal), `schedules` (three names, ENABLED), `series_prefixes`, `summary_objects`, `filled_objects`, `other_objects` (read again: series, summary and other EQUAL to before; filled equal to the full pass's written total)}; `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}; `notes` (words: counts, the memory and duration of the largest event, the sentences "the page has not been looked at" and "a viewer covering a client can now read that client's filled report through the live route"). Write `FILLED_PASS_APPLY_RECORD.json` and flip this order's status to complete as your last commit.

<criterion id="DBC194-1-AC1" cell_refs="DB-b-328"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p194_filled_pass_apply.py" . DBC194-1-AC1</invocation><expect>DBC194-1-AC1 PASS</expect></criterion>
`DBC194-1-AC1` -- the record: both halves signed at the packet's sha256, the ledger, the build hash, the two plans at 0/1/0 with clean re-plans, the exact OFF no-op, the dry run and the full pass reconciling shard by shard, the canary, the V leg, no id. Base: FAIL (no record).
<criterion id="DBC194-2-AC1" cell_refs="DB-b-328"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p194_filled_pass_apply.py" . DBC194-2-AC1</invocation><expect>DBC194-2-AC1 PASS</expect></criterion>
`DBC194-2-AC1` -- FRESH live reads: the function runs the bundle with exactly the one environment variable `FILLED_REPORT_PASS=1`; the role policy is the packet's pre-state; the three schedules' inputs carry no filled_report event. Base: FAIL.
<criterion id="DBC194-3-AC1" cell_refs="DB-b-328"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p194_filled_pass_apply.py" . DBC194-3-AC1</invocation><expect>DBC194-3-AC1 PASS</expect></criterion>
`DBC194-3-AC1` -- FRESH live reads of the data prefix: the filled objects equal the full pass's written total, the summary and other counts are unchanged, and a sample of the written documents validates against the contract (the checker validates them itself). Base: FAIL.

<expected_criteria>DBC194-1-AC1,DBC194-2-AC1,DBC194-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the artifact upload (a new version), the TWO `safe-apply`s of `reporting-publish` (0/1/0 each: code, then the one variable), the synthetic invokes of the pass (the dry run writes nothing; the canary writes ONE object; the full pass writes the rest), and the two minted users rows (written and removed). No `update-function-code`, no bare `terraform apply`, no delete of any object or version, no schedule or role change, no environment variable but `FILLED_REPORT_PASS`.
- **Stop rules.** A `Task timed out`, an `AccessDenied`, a Max Memory Used above 819 MB, a duration above 240 s, a plan line outside a gate, a build hash that differs, the Act 2 probe returning anything but the exact OFF no-op, a dry run or full-pass response outside its stop lines, a canary that fails validation, a refused count above 10 percent, a `~S2` grade of LEAK: STOP at once and report to the issuer. The rollback is the packet's section 6 (revert the one environment line and `safe-apply`; point the entry back to artifact version `oXM0wQg8revg3asMHOhpbz1gPDnXaatK`; written documents stay).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB9-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-328.apply-49f-filled-report-switch-on-and-first-pass.md
infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf
infra/aws/lambda/ci/function-map/irpt-49f-reporting-publish-lambda.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 187 (round 150, workstream FILLAPPLY), cell `DB-b-328`.
<owned_cells>DB-b-328</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC194-1-AC1, DBC194-2-AC1, DBC194-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-328.apply-49f-filled-report-switch-on-and-first-pass.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC194-1-AC1,DBC194-2-AC1,DBC194-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the plan lines, the dry run and full pass totals by count, the canary's digest, the V leg's three grades, the memory and duration of the largest event, and what is NOT proven. Counts and words only. Tell the issuer at once when the canary is written (the V leg waits on it) and when step 10 is done.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the Terraform root is the writer of the function's code and environment; the two plan gates (0/1/0 each) are the blast bound; the only data written is one new key per directory client.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes; the issuer read the live role policy (8 statements, hash recorded) and it already holds the write and read rights the pass needs.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the three schedules are read and their inputs recorded.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched by the applier.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record), the checker selftest is red on 58 single-fault arms, and its data clause validates a sample of the written documents against the contract itself.
lane: the <paths> block IS the grant.
</preflight>
