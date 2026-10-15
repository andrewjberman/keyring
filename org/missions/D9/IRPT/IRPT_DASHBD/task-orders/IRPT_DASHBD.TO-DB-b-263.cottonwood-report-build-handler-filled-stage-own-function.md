# TO IRPT_DASHBD.TO-DB-b-263 -- the COTTONWOOD REPORT-BUILD HANDLER (round 131, workstream B-49F): the filled_report_values stage as its own firm-isolated Lambda handler for firm cottonwood, one invocation per owed day with a self-invoke chain, a start floor of 2026-07-10, no overwrite

<to_id>IRPT_DASHBD.TO-DB-b-263</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~214</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>131</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 131 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-CW_ROUND_127_20261015.md @e86dc1ea32 and the CTO decision msg 8348 ("a Cottonwood reporting-gold function in its own declaration ... reads ONLY Cottonwood gold plus the served model-series object, and writes ONLY Cottonwood's filled_report_values ... Use the per-day split, memory from a measurement, and the DB-b-232 reader") | **Decomp cell:** `DB-b-263` (decomposition section 129).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order adds a handler and its tests and runs no AWS call and no Terraform command. The Terraform root, the source-map entry, the IAM grants and the measured memory are the NEXT cells; nothing here is planned, applied or deployed.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-214` (branch `wk-IRPT_DASHBD-214`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~214/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~214/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The scheduled reporting-gold build is declared for 49 Financial's source only, so it neither reads Cottonwood's `account_dim` nor writes a Cottonwood report. One firm per principal is the fence's rule (`opal-data-cottonwood` admits only `*-cot-*` roles), so the Cottonwood report is built by its OWN function, not as a second firm inside the 49 Financial one. The module that builds the report, `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` (`frv`), is firm-generic and the Cottonwood reader `adapters/cottonwood_report_reader.py` (DB-b-232) is its Cottonwood adapter; `main()` of `frv` already builds the Cottonwood report end to end locally (read-only measurement by the issuer for 2026-07-10: 220 households, 285,398 rows over 117 members, four sibling tables absent as NO_SOURCE_YET). What is missing is the Lambda handler: the per-day entry, the guard against overwriting, the start floor, and the chain. The 49 Financial handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, the filled stage at lines 646 to 892) is the PATTERN to follow and is NOT to be edited or imported (it is bound to the producer module `account_return_daily` and to the 49 Financial declaration).

**The cell (`DB-b-263`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r131/p131_cothandler.py` (your three criteria; its PROBE script is the behavioural spec and its `CLOSURE` list is the bundle); the pattern, lines 646 to 892 of the 49 Financial handler above; `frv` (`adapter_for`, `read_gold_rows`, `select_households`, `build_document`, `to_rows`, `missing_words`, `load_model_module`, `COLUMNS`, `TABLE`, `RET`, `RET_COLS`, `MODEL_TABLE`, `CONTRACT_REL`); `adapters/cottonwood_report_reader.py`; `lib/trading_calendar.py` (`trading_days_between`).
2. **The handler** `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py`. It is packaged with the members of the checker's `CLOSURE` list at their repo paths and with `handler.py` at the bundle root: find the repo root the way the sibling `account-return-daily/handler.py` does (`_ROOT = _HERE if (_HERE / "lib" / "trading_calendar.py").exists() else _HERE.parents[4]`), put `data/assets/scripts/gold/irpt_reporting` and `lib` on `sys.path`, and import `filled_report_values as frv`, `opal_naming` and `trading_calendar as tc`. It imports NOTHING else from the repo (not `account_return_daily`, not the 49 Financial handler) and nothing third-party at import time except `pyarrow` (boto3 only inside functions). Module constants: `FIRM = "cottonwood"` and `FLOOR_DAY = "2026-07-10"` (a plain string constant). Behaviour, which the checker's probe measures:
   - **`lambda_handler(event, context=None, s3=None, lambda_client=None)`** returns a dict with a `result` key (the one-day result) and may hold `day`, `next`, `chain`. `s3` and `lambda_client` default to boto3 clients (created lazily, only when not injected).
   - **Event `{"day": "YYYY-MM-DD"}`** builds that one day. A day that is not a real ISO date, or is BEFORE `FLOOR_DAY`, raises `SystemExit("REFUSED: ...")` before ANY S3 or Lambda call. `{"day": ..., "dry_run": true}` builds the rows and writes nothing.
   - **Event `{}` (the scheduled fire)** takes the trading days after the newest landed `filled_report_values` partition (or from `FLOOR_DAY` when none) through the newest `account_return_daily` partition's day (at most 10, ascending, never a day before `FLOOR_DAY`: use `tc.trading_days_between`), builds the OLDEST owed day only, and chains the next (below).
   - **Reads, through a reader that has no write method:** the adapter `frv.adapter_for(FIRM, str(_ROOT), opal_naming)` (its guard refuses any other firm or table); the households from the newest `account_dim` partition (`ad.households(reader, None)`); the returns rows through `frv.read_gold_rows(reader, ad, frv.RET, frv.RET_COLS, accounts, every=True)`; the sibling tables the adapter lacks (`ad.has_table(t)` false) are NOT read, their members are the absent form `{t: frv.missing_words(t)}` in the source dict's `missing` key (see `frv.main()` lines 1037 to 1075 for the source dict's exact shape); the served model series through `frv.load_model_module(str(_ROOT)).read_served_series(reader)`. **Wrap the reader so the returns table's partition LISTING keeps only `date=` partitions at or after `FLOOR_DAY`:** the Commonwealth-era history (3,325 partitions) is never listed and so never opened (the issuer measured 384 s and 3,329 GETs for nothing without it).
   - **The day's rows:** for the households with an account present on the day (`frv.select_households(groups, present, len(groups))`), one `frv.build_document(...)` and one `frv.to_rows(doc, ref, FIRM, day, contract_version)` per household, exactly as `frv.main()` does. Call `frv.load_model_module`, `frv.build_document`, `frv.to_rows` and `frv.read_gold_rows` THROUGH THE MODULE OBJECT `frv` (the probe replaces `build_document`, `to_rows` and `load_model_module`).
   - **Writes, exactly one:** `s3.put_object(Bucket=..., Key=..., Body=<parquet bytes>)` of the day's rows at the builder address `opal_naming.address("irpt", FIRM, "gold", frv.TABLE, "date=<day>", "data.parquet")`, the parquet schema as `frv.write_parquet` builds it (`value_number` float64, every other `frv.COLUMNS` column string, columns in `frv.COLUMNS` order), built in memory with pyarrow (no `ard`, no `stream_to_parquet`, no file upload call). An empty day is refused by name and writes nothing. **A day whose `data.parquet` already exists (`head_object`; a 404 or NoSuchKey means absent, any other error is a failure) is a NO-OP returning `{"day": day, "skipped": "LANDED"}`: nothing is overwritten.** A failed day is printed `FILLED_SKIPPED <day> <reason>` and returned as `{"day": day, "failed": reason}`; the handler never raises out of a day's build.
   - **The chain:** after a real (not dry-run) day, if another day is owed after it and `context.invoked_function_arn` exists, call `lambda_client.invoke(FunctionName=<that ARN>, InvocationType="Event", Payload=json.dumps({"day": next}).encode("utf-8"))` ONCE (the only `InvocationType="Event"` in the file); a client error is printed `FILLED_CHAIN_FAILED` and returned, never raised. No owed next day, or no context: no invoke.
   - **Forbidden in the file:** any other firm's token or place (the checker reads the source for `49financial`, `49f`, `schwab`, `inflection`), any `delete_*`, `copy_object`, `upload_file*`, a second `put_object`.
3. **Tests** in `infra/aws/lambda/investor-reporting/reporting-gold-cot/tests/test_*.py` (at least eight tests, `pytest` passing from the repo root), with a FAKE S3 and a fake Lambda client defined in the tests (no network, no `moto`): the one-day event puts once at the right key with the right columns; a landed day is skipped; a dry run puts nothing; a day before the floor and a malformed day refuse with no call; a returns partition before the floor is never opened (fixture one history partition); the scheduled path runs the oldest owed day and chains once with `Event` to the context's ARN; the last owed day chains nothing; the served model series is read through the reader. The tests name `cottonwood` and never another firm. They may patch `frv.build_document` and `frv.to_rows` with small stubs.
4. **Facts record** `RD_COT_REPORT_HANDLER_FACTS_R131.json` in your folder with EXACTLY these fields: `reads` (["account_dim", "account_return_daily", "model_series"]); `writes` (["filled_report_values"]); `floor_day` ("2026-07-10"); `bundle_members` (the sorted list of the repo paths in the checker's `CLOSURE` constant); `events` (["day", "dry_run", "scheduled"]); `words` (one paragraph, 80 to 1800 characters: what the handler does, what the floor removes, what is NOT proven: no memory or time on the Lambda runtime, no plan, no deploy, the join-key overlap beyond the fixtures).

<criterion id="DB131-1-AC1" cell_refs="DB-b-263"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r131/p131_cothandler.py" . DB131-1-AC1</invocation><expect>DB131-1-AC1 PASS</expect></criterion>
`DB131-1-AC1` -- the handler's source: its import-time third-party imports are only pyarrow, boto3 and botocore; it names no other firm; it holds exactly one `put_object` and no delete, copy or upload call; exactly one asynchronous self-invoke; `FLOOR_DAY` is the string 2026-07-10; it defines `lambda_handler`; and the worker's own commits touch only the handler directory, the deliverables folder, the investigation file and this order.
<criterion id="DB131-1-AC2" cell_refs="DB-b-263"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r131/p131_cothandler.py" . DB131-1-AC2</invocation><expect>DB131-1-AC2 PASS</expect></criterion>
`DB131-1-AC2` -- the checker stages the handler as it will be packaged (the `CLOSURE` members at their paths, the handler at the root) and runs it in a child interpreter against a fake S3 holding a Cottonwood `account_dim`, three returns partitions (one before the floor) and the served series object: one put at the builder address with the filled table's parquet; no key before the floor opened; no key outside the three Cottonwood tables, the filled prefix and the one served object touched; a landed day skipped with no put; a dry run with no put; a before-floor day and a malformed day refused with zero calls; the scheduled path runs the oldest owed day with one put and ONE `Event` self-invoke of the context's ARN carrying the next day; the last owed day chains nothing.
<criterion id="DB131-1-AC3" cell_refs="DB-b-263"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r131/p131_cothandler.py" . DB131-1-AC3</invocation><expect>DB131-1-AC3 PASS</expect></criterion>
`DB131-1-AC3` -- the worker's tests pass under pytest (at least one passes, none fails), name cottonwood and no other firm; the probe passes again; and the facts record has exactly the form of step 4 with its lists equal to the checker's recount.

<expected_criteria>DB131-1-AC1,DB131-1-AC2,DB131-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `filled_report_values.py`, the adapters, the 49 Financial handler, `lib/`, the registry, every Terraform file, the source map, the contract, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fakes; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push, no secret read. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic (account ids like `A1`, household ids like `HH1`).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `frv` or the adapter cannot be used as described, record it, file a BLOCKING row and stop; do not edit them.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W214-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-gold-cot/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~214/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-263.cottonwood-report-build-handler-filled-stage-own-function.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 129 (round 131, workstream B-49F), cell `DB-b-263`.
<owned_cells>DB-b-263</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB131-1-AC1, DB131-1-AC2, DB131-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~214/IRPT_DASHBD.TO-DB-b-263.cottonwood-report-build-handler-filled-stage-own-function.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB131-1-AC1,DB131-1-AC2,DB131-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the handler's functions in one line each; the test count; how the floor is applied; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a handler, its tests and a facts record in a branch; nothing is wired to AWS, packaged, planned, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes; the IAM grants for the function are the next cell and are derived from this handler's measured reads and writes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probe was validated by the issuer against a scratch reference handler (green) and six mutants (no floor, overwrite, dry-run put, synchronous chain, another firm, not-oldest: all red); its static and facts clauses by its self-test.
lane: the <paths> block IS the grant.
</preflight>
