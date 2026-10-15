# TO IRPT_DASHBD.TO-DB-b-247 -- the PER-DAY SELF-INVOKE SPLIT of the hop-1 `filled_report_values` stage (round 122, workstream B-49F): the scheduled fire runs the earlier stages and the OLDEST owed filled day, then invokes ITSELF asynchronously with the next owed day until none is owed; an invocation carrying a `day` runs exactly that day (a landed day is a no-op) and chains the next; the role gains `lambda:InvokeFunction` on its own ARN only; LOCAL build, nothing planned, applied or deployed

<to_id>IRPT_DASHBD.TO-DB-b-247</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~201</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 122 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-122 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_122_20261015.md @e690365741`: "B: one invocation per owed day. The scheduled fire computes the owed days, processes the oldest, and asynchronously invokes ITSELF with `{"day": <next>}` until none is owed. The new grant is `lambda:InvokeFunction` on its own ARN only. A day already landed is a no-op, so a duplicated chain link writes nothing") | **Rows:** IRPT_DASHBD-D2-W201-S<k> | **Decomp cell:** `DB-b-247` (decomposition section 120) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none (chunking inside a day, if `DB-b-246` says CHUNK, is a later cell)

**Risk class WORLD** is the floor of the paths below (an `infra/` path): this order edits a handler and Terraform files and runs no Terraform command and no AWS call; the plan and the apply are another seat's act under a signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-201` (branch `wk-IRPT_DASHBD-201`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~201/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~201/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 121 measured the hop-1 `filled_report_values` stage at 848 s for a ten-day fire (OWN_INVOCATION, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/RD_STAGE_MEASURED_R121.json`), so it cannot share the 07:41 fire's 900 s timeout. The CTO ruled shape B: each owed day is its own invocation of the SAME function. Today `run()` in `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` calls `filled_stage(...)` after the lots stage. This cell replaces that with the oldest-owed-day-then-chain behaviour, adds the event that runs one day, and adds the one IAM statement the self-invoke needs. Memory per day is measured by `DB-b-246` in the same round; a chunk rule, if needed, is added later, so build the day as the stage builds it today.

**The cell (`DB-b-247`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_split.py` (your three criteria; its docstring, the AST, test-name, HCL and facts clauses); the handler (`run`, `lambda_handler`, `filled_stage`, `filled_write`, `filled_inputs`, `_filled_location`, `class_owed_days`, `newest_landed_day`, `population_accounts`, `newest_accounts`, `account_set`, `MAX_DAYS_PER_FIRE`) and its tests directory (copy the style of `tests/test_filled_report_values_stage.py`); `iam.tf` and `locals.tf` of `infra/aws/terraform/investor-reporting/reporting-gold/` (the existing statements, how `OwnLogStreamOnly` builds the function's own ARN part from `module.irpt_reporting_gold_lambda_name.name`).
2. **The handler** (ADDITIVE: at most 10 existing lines may change; `filled_stage` stays defined but `run()` no longer calls it). Exact names, because the checker reads them:
   - `filled_population(s3, firm)`: the `accounts` list the scheduled stage uses today (the way `run()` builds it from `population_accounts` and `newest_accounts`), factored so both paths share it.
   - `owed_filled_days(s3, firm, written)`: the filled days owed, oldest first, by the same catch-up rule the class and lots stages use (`class_owed_days` over the newest landed filled partition and the days this fire wrote), at most `MAX_DAYS_PER_FIRE`.
   - `run_filled_day(s3, firm, day, accounts, upload)`: builds and writes ONE day through the existing `filled_write(s3, firm, [day], accounts, upload)`; if that day's `data.parquet` already exists it is a NO-OP and returns `{"day": day, "skipped": "LANDED"}`; it never raises (a failure is returned and printed as `FILLED_SKIPPED`).
   - `invoke_next_day(lambda_client, function_arn, next_day)`: when `next_day` is None it makes NO call; otherwise it calls `lambda_client.invoke(FunctionName=function_arn, InvocationType="Event", Payload=json.dumps({"day": next_day}).encode("utf-8"))`; any client error is caught, printed, and returned as `{"invoked": False, "error": ...}`; it never raises.
   - `filled_day_event(event)`: the ISO day when `event` has a `"day"` key (a real date, else `SystemExit("REFUSED ...")`) and has no `backfill` key; otherwise None.
   - `run(s3, today, event=None, workers=12, chain=None)`: after the lots stage, instead of `filled_stage`, compute `owed_filled_days`, run the OLDEST with `run_filled_day`, and when `chain` (a pair `(lambda_client, function_arn)`) is given and a next owed day exists, call `invoke_next_day` for it; the returned dict keeps the `filled_rows`, `filled_failed` and `filled_catch_up` keys.
   - `lambda_handler(event, context=None)`: an event for which `filled_day_event` is not None runs ONLY that day (no earlier stage): population via `filled_population`, `run_filled_day`, then `owed_filled_days` and `invoke_next_day` for the next one; any other event goes through `run` as today, with `chain=(boto3.client("lambda"), context.invoked_function_arn)` when a context with that attribute is given and `chain=None` otherwise (a local run never invokes). The function name is never typed.
3. **Tests** `infra/aws/lambda/investor-reporting/reporting-gold/tests/test_filled_per_day.py`, at least 8, no network, fake clients: a landed day is a no-op and writes nothing; the oldest owed day runs first; the chain stops when none is owed (no invoke call); the invoke uses `InvocationType` `Event`; the payload carries the day; a malformed `day` event is refused; a day event runs no earlier stage; `run` no longer calls `filled_stage`; a `chain` of None never invokes. The whole tests directory passes (105 earlier plus yours, at least 113).
4. **Terraform** (`iam.tf`, and `locals.tf` only if you need a local; additive; at most 2 existing lines may change): ONE new statement, sid `InvokeOwnFunctionOnly`, `actions = ["lambda:InvokeFunction"]` exactly, `resources` = the function's own ARN built as `OwnLogStreamOnly` builds its log-group ARN: `arn:aws:lambda:us-east-1:${data.aws_caller_identity.current.account_id}:function:${module.irpt_reporting_gold_lambda_name.name}` (the name from the builder module, never typed). No wildcard, no other `lambda:` action, nothing else.
5. **The facts record** `RD_SPLIT_FACTS_R122.json` in your folder with EXACTLY these fields: `handler` {`file`, `functions_added` (includes the five names), `event_key` ("day"), `invocation_type` ("Event"), `words`}; `behavior` {`oldest_first`, `noop_when_landed`, `chain_stops_when_none_owed`, `scheduled_runs_earlier_stages`, `day_event_skips_earlier_stages` (all five true), `words`}; `iam` {`file`, `statement_id`, `action` ("lambda:InvokeFunction"), `resource_form` (words: how the ARN is built), `words`}; `expected_plan` {`to_add` 0, `to_change` 2, `to_destroy` 0, `resources` (exactly `aws_iam_role_policy.irpt_reporting_gold` and `module.irpt_reporting_gold.aws_lambda_function.this`), `words`}; `tests` {`file`, `new_tests`, `dir_total`}; `files_changed` (the handler, the new test file, `iam.tf` and `locals.tf` if changed, each {`file`, `sha256` (of the bytes at your final commit), `kind`}); `words`; `claim` ("inferred": nothing was planned); `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `resources` field.

<criterion id="DB122-2-AC1" cell_refs="DB-b-247"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_split.py" . DB122-2-AC1</invocation><expect>DB122-2-AC1 PASS</expect></criterion>
`DB122-2-AC1` -- the handler defines the five functions; `run()` calls `owed_filled_days` and `run_filled_day` and no longer calls `filled_stage`; `invoke_next_day` invokes with `InvocationType` Event and a payload with the day key; `lambda_handler` reads the event through `filled_day_event`; the new test file holds at least 8 tests whose names cover the landed no-op, the chain stop, the event and the payload; the whole handler tests directory passes with at least 113 tests. Base: FAIL (the functions are missing).
<criterion id="DB122-2-AC2" cell_refs="DB-b-247"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_split.py" . DB122-2-AC2</invocation><expect>DB122-2-AC2 PASS</expect></criterion>
`DB122-2-AC2` -- `iam.tf` gains exactly one new statement with the single action `lambda:InvokeFunction`, no wildcard, the only statement carrying a `lambda:` action; its resource is a function ARN built from `module.irpt_reporting_gold_lambda_name`; in the worker's own commits `iam.tf` gains at least 8 lines and loses at most 2, and no other Terraform file than `iam.tf` and `locals.tf` changes. Base: FAIL (no statement).
<criterion id="DB122-2-AC3" cell_refs="DB-b-247"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_split.py" . DB122-2-AC3</invocation><expect>DB122-2-AC3 PASS</expect></criterion>
`DB122-2-AC3` -- `RD_SPLIT_FACTS_R122.json` has exactly the form of step 5 and its files hash as recorded; the handler change is additive in the worker's own commits (gains at least 60 lines, loses at most 10); nothing else under `infra/`, `data/`, `lib/` or `org/standards/` changes in them. Base: FAIL (no record).

<expected_criteria>DB122-2-AC1,DB122-2-AC2,DB122-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the module, the producers, every other test and Terraform file, `lambda.tf` (the timeout and memory are NOT changed here), the source map, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fake clients; no network, no AWS call, no Terraform command, no S3, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the 105 earlier handler tests cannot all pass after your edit, or the invoke cannot be written without a typed function name, file a BLOCKING row with the numbers and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W201-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-15, on worker row W201-S3; gate limb: a modification of an existing order, placeholders NONE, no criterion id or cell changes).** Step 2 requires `run()` to stop calling the shared `filled_stage`, and the existing test `FilledStageTests.test_stage_runs_after_the_class_and_lot_stages` in `tests/test_filled_report_values_stage.py` pins exactly that call. The order was wrong to demand both unchanged. That ONE test file is now in the grant for ONE change: update that single test so it asserts the new behaviour (after the class and lots stages `run()` calls `owed_filled_days` and `run_filled_day`, and does not call `filled_stage`); every other test of that file stays byte-identical. The whole tests directory must still pass with at least 113 tests (the updated test counts as an earlier test). Record the change in the facts record's `files_changed` (the file's `kind` is "test updated") and in `words`.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_filled_per_day.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_filled_report_values_stage.py
infra/aws/terraform/investor-reporting/reporting-gold/iam.tf
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~201/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-247.per-day-self-invoke-split-of-the-hop-1-filled-stage.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 120 (round 122, workstream B-49F), cell `DB-b-247`.
<owned_cells>DB-b-247</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB122-2-AC1, DB122-2-AC2, DB122-2-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~201/IRPT_DASHBD.TO-DB-b-247.per-day-self-invoke-split-of-the-hop-1-filled-stage.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB122-2-AC1,DB122-2-AC2,DB122-2-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the five functions and where `run` and `lambda_handler` use them; the existing lines you changed; the one IAM statement; the expected plan; the test counts; what you could not check without Terraform and AWS. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a handler, its tests, two Terraform files and a facts record in a branch; nothing is planned, applied, scheduled or deployed, and the apply is another seat's act under a signed never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; iam.tf gains one lambda:InvokeFunction statement on the function's own ARN; it takes effect only at the applier's apply, under the pair.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (the functions are missing) and exercised by its self-test (AST, test-name, HCL and facts arms).
lane: the <paths> block IS the grant.
</preflight>
