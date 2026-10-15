# TO IRPT_DASHBD.TO-DB-b-257 -- the Cottonwood landing root made READY for its pair (round 126, workstream B-49F): memory 1024 MB from the round-125 measurement, the source-map entry's 15 staged members pinned and hashed with its Terraform fields filled, and a BUILD-ONLY package proven equal to its sources

<to_id>IRPT_DASHBD.TO-DB-b-257</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~210</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>126</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 126 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-126 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_126_20261015.md @2cf3e13682`: "The Cottonwood landing packet ... at 1,024 MB (from the measurement, not the sibling)").

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order edits one Terraform file and one JSON map and runs no Terraform command, no AWS call and no upload.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-210` (branch `wk-IRPT_DASHBD-210`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~210/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~210/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The landing function's root (`infra/aws/terraform/investor-reporting/account-return-daily/`) is merged and unapplied. Three things stand between it and a signed pair: its `memory_size` is 8192 (copied from the 49 Financial sibling) while this function's own measurement (round 125, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~208/RD_COT_MEMORY_R125.json`) chose 1024; its source-map entry `irpt-cot-account-return-daily-lambda` has `pin: null` and `sha256: null` on all 15 staged members and `tf_file: null` (the builder refuses an entry whose `tf_file` does not name the pipeline: `ERROR: No zip-based functions found for pipeline 'investor-reporting'`); and no one has shown the package it builds holds exactly the declared members. A pin is a FULL 40-hex commit id (a moving ref is refused); the applier must not have to write them.

**The cell (`DB-b-257`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_landing.py` (your three criteria; every clause and the record's exact form are in it); `infra/aws/terraform/investor-reporting/account-return-daily/lambda.tf` (its sizing comment); the entry `irpt-cot-account-return-daily-lambda` in `infra/aws/lambda/ci/lambda-source-map.json` and the entry `irpt-cot-account-dim-lambda` beside it (its Terraform fields and pins are the form to follow); `infra/aws/lambda/ci/build-and-upload.sh` (the `BUILD_ONLY` mode and its pin and hash gate); `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~195/RD_CW_LANDING_FACTS_R120.json` (the five builder names).
2. **Memory.** In `lambda.tf` change `memory_size = 8192` to `memory_size = 1024` and NOTHING else in code (timeout stays 900, reserved concurrency stays 1). Rewrite the sizing comment's memory paragraph so it states the measurement (the measured peak in MB from the record, the two days, the 70 percent rule, 1024 MB the smallest standard size under it), cites `RD_COT_MEMORY_R125` by that name, and no longer says the peak is unmeasured. Comments only otherwise; no other root file changes.
3. **The entry.** In the source map change ONLY the entry `irpt-cot-account-return-daily-lambda`, and in it only these keys: for each of the 15 `staged_from` members set `pin` to the full 40-hex id of the most recent commit that changed that member (`git log -1 --format=%H -- <repo_path>`) and `sha256` to the hex SHA-256 of the member's bytes at that commit (`git show <pin>:<repo_path>`), which must equal its bytes at HEAD; set `tf_file` to `infra/aws/terraform/investor-reporting/account-return-daily/lambda.tf`, `tf_resource` to `module.irpt_account_return_daily.aws_lambda_function.this`, `iam_role` to the builder name of the execution role (the second name in the landing record); replace `_staged_from_note` and `_tf_note` with one honest sentence each saying the pins and fields were written by this order and the applier writes nothing. Keep key order, indentation and every other entry, key and line byte for byte (the file loses 0 other lines). Commit the source-map change BEFORE running the build, because the build reads committed source.
4. **The build-only package.** Run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-account-return-daily-lambda` from your worktree root. It uploads nothing and writes no map field; it prints `BUILD_ONLY: <zip> sha256=<base64>`. If it refuses, report its exact error and stop.
5. **Record** `RD_COT_LANDING_FACTS_R126.json` in your folder with EXACTLY these fields: `firm` ("cottonwood"); `names` (the five builder names in the landing record's order); `memory_mb` (1024); `peak_rss_mb` (the measured peak, from the record); `members` (the count of the entry's `files` list); `build_only_sha256` (the base64 the build printed); `plan_expected` ({"add": 7, "change": 0, "destroy": 0, "claim": "inferred"}); `pins_written_by` ("0.9.0_WK_IRPT_DASHBD~210"); `words` (one paragraph, 80 to 1500 characters: what changed, what the build proved, what is NOT proven: no plan, no apply, no upload, no invoke).

<criterion id="DB126-1-AC1" cell_refs="DB-b-257"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_landing.py" . DB126-1-AC1</invocation><expect>DB126-1-AC1 PASS</expect></criterion>
`DB126-1-AC1` -- `lambda.tf` carries `memory_size = 1024` with `timeout = 900` and `reserved_concurrent_executions = 1` kept; against the order's first commit the only code line removed is `memory_size = 8192` and the only one added is `memory_size = 1024`; the comment cites `RD_COT_MEMORY_R125`, states the measured peak and no longer says "unmeasured"; every other file of the root is byte-equal to the base.
<criterion id="DB126-1-AC2" cell_refs="DB-b-257"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_landing.py" . DB126-1-AC2</invocation><expect>DB126-1-AC2 PASS</expect></criterion>
`DB126-1-AC2` -- in the source map every other function entry and top-level key is unchanged; in the entry only `staged_from`, `tf_file`, `tf_resource`, `iam_role` and the two notes differ; all 15 members keep their identity and gain a 40-hex `pin` that is an ancestor of HEAD and a 64-hex `sha256` equal to the hash of `git show <pin>:<path>` and of the file at HEAD; the three Terraform fields equal the values of step 3.
<criterion id="DB126-1-AC3" cell_refs="DB-b-257"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_landing.py" . DB126-1-AC3</invocation><expect>DB126-1-AC3 PASS</expect></criterion>
`DB126-1-AC3` -- the checker runs the build-only command itself: it exits 0 and prints its line; the zip holds exactly the entry's `files` (handler.py at its root, the 15 members at their repo paths) and every member's bytes equal its source at HEAD; the record has exactly the form of step 5, its five names equal the builder's, its `build_only_sha256` equals the checker's own build and no run of 8 or more digits stands outside the exempt fields.

<expected_criteria>DB126-1-AC1,DB126-1-AC2,DB126-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the other root files, the handler, the adapter, the registry, every other source-map entry, the build script, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files and git history. Writes: the repo files of the grant and your private folder. The build-only run writes a zip under a temporary directory only. No Terraform command, no AWS call, no upload, no push, no invoke, no secret read.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the build refuses, or a member's bytes at its last-changing commit differ from HEAD, record it, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W210-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/account-return-daily/lambda.tf
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~210/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-257.cottonwood-landing-root-memory-1024-pins-and-build-only-package.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 124 (round 126, workstream B-49F), cell `DB-b-257`.
<owned_cells>DB-b-257</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB126-1-AC1, DB126-1-AC2, DB126-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~210/IRPT_DASHBD.TO-DB-b-257.cottonwood-landing-root-memory-1024-pins-and-build-only-package.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB126-1-AC1,DB126-1-AC2,DB126-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the measured peak and the line the comment states; the 15 pins (count of distinct commits, none printed beyond a count); the build-only line's member count and sha256; the existing lines you changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one Terraform file and one source-map entry edited in a branch; nothing is planned, applied, uploaded, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes; the memory edit is a repo line and the pair that applies it is a later, signed act.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (FAIL as expected), exercised by its self-test (memory, entry, package and facts arms) and by a scratch reference implementation run through the build-only package.
lane: the <paths> block IS the grant.
</preflight>
