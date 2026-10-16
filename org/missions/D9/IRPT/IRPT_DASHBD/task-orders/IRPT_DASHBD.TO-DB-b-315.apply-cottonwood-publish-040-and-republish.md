# TO IRPT_DASHBD.TO-DB-b-315 -- APPLY the signed Cottonwood reporting-publish pair (packet sha256 `584a774339a1`): gates and live reads, ledger, build-only hash, ONE new bundle version (publisher 0.4.0), plan 0/1/0, ONE `safe-apply`, the pre-write read with its STOP lines, ONE dry run, a ONE-account canary, the FULL republish of the 939 series, the after-read (COO half signed @de90b2bb6f; CTO half signed @f78b555c93) (SERVED output moves)

<to_id>IRPT_DASHBD.TO-DB-b-315</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>COTPUBHOP2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_REPORTING_PUBLISH_HOP2_HISTORY_SCOPE_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_PUBLISH_040_REPUBLISH_CTO_HALF.md` (both at the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_REPORTING_PUBLISH_HOP2_HISTORY_SCOPE_REPUBLISH.md`, sha256 `584a774339a15acac39defbab5919cb9a8400eeef98dd63aa10be46aeb0c9c36`) | **Decomp cell:** `DB-b-315` (decomposition section 175).

**Risk class WORLD, and served output moves:** an artifact version, the function's code, and 1,878 served objects overwritten at the same keys (prior versions kept). The CTO added one STOP before any write: a changed `external_flow` on a common day above 800 series (measured 659).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet, both halves and the read tool); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes, addresses and words only; never an account id.

**What this order does, in one paragraph.** The function `irpt-cot-reporting-publish-lambda` runs publisher 0.3.0 and the 939 published Cottonwood series are all `PARTIAL_HISTORY` with no claim. The landing rewrite is done (`DB-b-308`). You land the publisher 0.4.0 bundle, apply the root once (the function's code only), read the blast radius before any write, prove the dry run, show the flip on ONE account, then republish the 939 series.

**Read first (all in your worktree):** the packet (whole), its COO half and the CTO half; `infra/aws/terraform/investor-reporting/reporting-publish-iso/`; the entry `irpt-cot-reporting-publish-lambda` in `infra/aws/lambda/ci/lambda-source-map.json`; `infra/aws/lambda/ci/build-and-upload.sh`; `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py`; the read tool `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py` and its record; your own prior applies (`IRPT_DASHBD.TO-DB-b-312...` and `-308...` and their records). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda side (its log), never retried blind; a long event may need the function's own 900 s: wait for it.

**Do, in this order. Record every value named in `COT_PUBLISH_HOP2_RECORD.json` as you go (keys exactly as listed in the checker `p182_cot_publish_apply.py`).**

0. **Gates, read only.** (a) `git hash-object` of the packet equals `008efedd5f08e7861d77ae3ea60b0d51d4782378` and its sha256 equals `584a774339a15acac39defbab5919cb9a8400eeef98dd63aa10be46aeb0c9c36`; both halves read SIGNED at it (`gates.packet_blob`, `gates.packet_sha256`, `gates.coo_half_signed`, `gates.cto_half_signed`). (b) The packet's code is an ancestor of HEAD (`git merge-base --is-ancestor cbf7ead020 HEAD`; `gates.pin_is_ancestor`). (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the denominator) names the `reporting-publish-iso` root, `irpt-cot-reporting-publish` or the prefix `irpt/cottonwood/platinum/reporting`; the 49 Financial ledgers are other surfaces (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = 0). (d) The live function and schedule equal the packet's section 3 (`gates.live_matches_packet`). Any mismatch: STOP.
1. **Open the NEVER-2 ledger BEFORE any write** with `python .tools/deploy_ledger.py open ...` under `org/critical_paths/change_management/`, slug `irpt-dashbd-cottonwood-publish-hop2-scope-republish-20261016`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**, legs: L1 git; L2 build; L3 terraform; L4 pre-write read and dry run; L5 canary and republish; L6 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry` and `applier`.
2. **Before reads.** `before` {`function_code_sha256`, `artifact_version_id` (the key's current version), `schedule` ({`state`, `cron`}: DISABLED), `objects` ({`series`, `manifest`, `other`}: the client-side counts over `irpt/cottonwood/platinum/reporting/` by key name, auto-paginated, denominator printed; expected 939 / 939 / 0), `history_scope_counts` (the count of the 939 published series by their `history_scope`, read from the objects: expected {"PARTIAL_HISTORY": 939})}.
3. **Build, import-smoke, upload.** (a) `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-reporting-publish-lambda`: **its base64 sha256 must equal `vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE=` or STOP and say why**; record `build.zip_sha256` (hex), `build.zip_sha256_b64` and `build.members`. (b) **Import smoke:** extract the zip to a fresh temporary directory and, from another directory, run `python -I -c "import sys; sys.path.insert(0, '<dir>'); import handler"`; record `build.import_smoke_rc` (0). (c) The real `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-reporting-publish-lambda`: a NEW VERSION of the key and the entry's `artifact_sha256` updated; record `build.landed_version_id` (different from the before version), `build.content_sha256`, `build.built_equals_landed` (true).
4. **Terraform: gates and ONE `safe-apply`.** `terraform fmt -check` on the root (a failure on a pinned file is a row, not an edit), `validate`, `plan` through the `safe-apply` plan step. **The plan must read exactly 0 to add, 1 to change, 0 to destroy:** `module.irpt_reporting_publish_iso.aws_lambda_function.this` by CODE attributes only. Any other line STOPS. Then ONE `safe-apply`; a re-plan afterward reads No changes. Record `plan` {`add`, `change`, `destroy`, `change_addresses`, `function_change_attributes`, `replan_no_changes`} and `apply_finished_utc` (outside 12:05Z to 12:45Z on a weekday).
5. **The pre-write read.** Run the read tool (`python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py`, from the worktree root, about 30 s, read-only). Record `pre_write` {`partial_to_full` (the scope flips line, PARTIAL_HISTORY to FULL), `full_to_partial` (FULL to PARTIAL_HISTORY, 0 if absent), `series_gaining_day` (`new_days_added`), `changed_total_return_common`, `changed_external_flow_common`, `changed_value_common`, `changed_income_common`, `changed_price_return_common` (the "changed value on a day present in BOTH" line; 0 for a field not listed), `refused` (`new_refused`, 0 if absent), `published_series` (939)}. **STOP before any write** if: `full_to_partial` is above 0; `partial_to_full` above 150; `changed_value_common`, `changed_income_common` or `changed_price_return_common` above 0; `changed_total_return_common` or `changed_external_flow_common` above 800; or `refused` above 0. Expected exactly the packet's section 3 figures (102 / 826 / 657 / 659 / 0) unless a landing added a day.
6. **The dry run.** ONE synchronous `{}` (outside 12:05Z to 12:45Z on a weekday). Record `dry_run` {`payload` ({}), `invoked_utc`, `status_code`, `function_error`, `returned` (exactly {`uploaded` false, `published` 939, `refused`}), `report` {`max_memory_used_mb`, `duration_ms`, `memory_size_mb`}, `request_id`}. Expected refused 40 (the first publish's count); STOP above the 10 percent line (published + refused).
7. **The canary.** ONE synchronous `{"upload": true, "accounts": ["<one id>"]}` for the first account, sorted, whose new series reads `history_scope` FULL (find it with the read tool's logic or by a dry build; the id is never recorded, only `account_hash12`, the first 12 hex of its sha256). Record `canary` {`payload_shape` ({"upload": true, "accounts": 1}), `account_hash12`, `invoked_utc`, `status_code`, `function_error`, `returned` ({`published` 1, `refused` 0}), `report`, `objects_after` ({`series`, `manifest`, `other`}: unchanged), `checks` (all true: `validates_contract`, `scope_full`, `claim_inferred`, `basis_present`, `manifest_publisher_040`, `prior_versions_kept`, `series_size_equals_manifest`), `request_id`}.
8. **The full republish.** ONE synchronous `{"upload": true}` (900 s limit: wait; judge a lost response from the log). Record `full` {`payload`, `invoked_utc`, `status_code`, `function_error`, `returned` ({`published` 939, `refused` = the dry run's}), `report`, `objects_after` (unchanged counts), `claim_count` (series carrying `history_scope_claim`: 939), `full_count` (series reading FULL: equals `pre_write.partial_to_full`), `partial_count`, `changed_value_common_count` (series whose `value` differs from the prior version on a common day: 0), `prior_versions_kept` (true for every key), `sampled_hash12` (ten, by sorted position), `sample_checks_pass`, `request_ids`}.
9. **The after-read.** `after` {`function` {`memory`, `timeout`, `reserved_concurrency` (null), `code_sha256`, `layer_arn`}, `schedule` ({`state` DISABLED, `cron`})}; `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}.
10. **Receipt** `COT_PUBLISH_HOP2_RECORD.json` plus a short words file: the counts, memory and duration, and the sentences "client-facing: the Returns-from sentence goes for the FULL series" and "the daily returns of the restated October days moved". Flip this order's status to complete as your last commit.

<criterion id="DBC182-1-AC1" cell_refs="DB-b-315"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p182_cot_publish_apply.py" . DBC182-1-AC1</invocation><expect>DBC182-1-AC1 PASS</expect></criterion>
`DBC182-1-AC1` -- the record's head: packet and halves, gates, ledger and applier, before, build, plan 0/1/0 on the function, the apply outside the landing fire window. Base: FAIL (no record).
<criterion id="DBC182-2-AC1" cell_refs="DB-b-315"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p182_cot_publish_apply.py" . DBC182-2-AC1</invocation><expect>DBC182-2-AC1 PASS</expect></criterion>
`DBC182-2-AC1` -- the pre-write read inside its STOP lines, the dry run, the canary with its seven checks and the full republish in the record, each inside its limits. Base: FAIL.
<criterion id="DBC182-3-AC1" cell_refs="DB-b-315"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p182_cot_publish_apply.py" . DBC182-3-AC1</invocation><expect>DBC182-3-AC1 PASS</expect></criterion>
`DBC182-3-AC1` -- FRESH live reads: the function runs the new code with no environment variable; the schedule is DISABLED; the artifact's current version is the recorded one; all 939 series carry the claim, all 939 manifests read publisher 0.4.0 and the live FULL count equals the record's. Base: FAIL.

<expected_criteria>DBC182-1-AC1,DBC182-2-AC1,DBC182-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the ONE bundle upload (a new version of the key), the ONE Terraform apply (`safe-apply`) of the `reporting-publish-iso` root (0 adds, 1 change), the dry run (writes nothing), the canary (two objects) and the full republish (1,878 objects at the same keys, new versions). No `update-function-code`, no bare `terraform apply`, no delete of any object or version, no schedule change, no environment variable, no event other than the three named. No act between 12:05 and 12:45 UTC on a weekday.
- **Stop rules.** A `Task timed out`, an `AccessDenied`, a Max Memory Used above 819 MB, a plan line outside the gate, a build hash that differs, a pre-write count outside its STOP lines, a refusal above 10 percent: STOP at once and report to the issuer; the rollback is the packet's section 7 (prior artifact version `4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA` through `safe-apply`, the prior version of each key).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB4-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-315.apply-cottonwood-publish-040-and-republish.md
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 175 (round 149, workstream COTPUBHOP2), cell `DB-b-315`.
<owned_cells>DB-b-315</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC182-1-AC1, DBC182-2-AC1, DBC182-3-AC1 (mechanical, WORLD). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-315.apply-cottonwood-publish-040-and-republish.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC182-1-AC1,DBC182-2-AC1,DBC182-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument).
</proof_of_spec>

**REPORT:** once, under 150 words: the three criteria's last lines; the ledger slug; the plan's counts; the pre-write counts; the dry run's refused count; the canary's checks; the full republish's published, FULL count and Max Memory Used and duration.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the Terraform root `reporting-publish-iso` is the one writer of the function's code; the plan gate (0/1/0) is the blast bound; the republish writes only the 1,878 keys of one prefix at the same addresses.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; no policy or role changes (the plan touches the function's code only) and the issuer read the live function configuration.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the daily schedule stays DISABLED and the checker requires it unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched by the applier; the served pages read the objects the republish overwrites.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the issuer's checker selftest is green on a synthetic record and red on 34 single-fault arms.
lane: the <paths> block IS the grant.
</preflight>
