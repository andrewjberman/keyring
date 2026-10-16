# TO IRPT_DASHBD.TO-DB-f-2201 -- the FWD-5 49 FINANCIAL GOLD HANDLER EMITS THE TRANSACTION DAY, ONE CELL (W1): the reporting-gold Lambda's handler imports `account_transaction` guarded, reads each day's fact_trn partition, runs the producer and writes the day, last in the scheduled fire and in backfill, never stopping the stages before it; the CTO's round-135 analysis, item 1 (msg 9837, W1)

<to_id>IRPT_DASHBD.TO-DB-f-2201</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2201</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>136</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-135 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_135_20261016.md` @8d48df1751, msg 9837): the round-136 list is the issuer's, in order; item 1 is the 49 Financial transaction wiring, W1 the handler emission | **Rows:** IRPT_DASHBD-D2-W2201-S<k> | **Decomp cell:** `DB-f-2201` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R136_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

**Risk class WORLD** is the floor of the path below (`infra/` path): code in a branch, offline tests; no Terraform command, no AWS call, no push. The bundle, the plan, the apply and the first write are the applier's under a later signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2201` (branch `wk-IRPT_DASHBD-2201`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2201/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. Offline tests only (stubs and fakes). **You have NO AWS in this order: make no AWS call of any kind.** No real client, household or account id, no client figure and no security name anywhere; test accounts, symbols and dates are made up. Write files with the Write or Edit tool, not shell heredocs (backslash sequences break in the shell). Do not grep or find recursively over the repo; read named files.

**Why.** The 49 Financial gold Lambda (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) writes five tables plus the filled-report values for the days a fire owes: it computes the returns day, then emits the class, activity, lot and filled-report days. The transaction producer (`data/assets/scripts/gold/irpt_reporting/account_transaction.py`: `normalize_trn(frame, firm)` and `emit_transaction_day(s3, rows, firm, day, *, upload)`, contract 0.5.1) is on the trunk and wired to nothing. This cell wires it into the handler as the LAST stage, so a failure in it can never stop what the stages before it write.

**The inputs (read, never edited).** The handler itself (read it whole; the model stages are `emit_classes`, `emit_lots`, `filled_write`; the module-level context `_CLASS_CONTEXT` that `compute()` leaves, with the source entry `src` (`bucket`, `transactions_prefix`) and `trn_days`; `ard.partition_days`); the producer module and its words file; `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (find its function that reads one custodian day of `fact_trn` and reuse it: no new S3 listing or reading code); the existing tests in `infra/aws/lambda/investor-reporting/reporting-gold/tests/` (their harness patches `h.ard`, `h._gold_location` and others; `test_class_table_emission.py` is the model); the issuer's plan `deliverables/2.0.0_SA_COO~F2/R135_49F_TRANSACTION_WIRING_PLAN.md`; the checker `deliverables/2.0.0_SA_COO~F2/checks/r136/p136_handler.py` (**read it first; its BEHAVIOUR script is the exact contract of `emit_transactions`; its reason lines tell you what to fix; it has a `--selftest`**).

**The cell (`DB-f-2201`), in this order; commit after each of steps 2 and 4.**

1. **The guarded import.** Beside the other guarded imports: `import account_transaction as at49` in a try/except that sets `at49 = None` and `AT49_IMPORT_ERROR = "<type>: <text up to 200 chars>"` on failure and `AT49_IMPORT_ERROR = None` on success (the same form as `acd`/`ACD_IMPORT_ERROR`).
2. **The stage.**
   - `transaction_frame(s3, firm, day)` returns ONE pandas frame: the day's `fact_trn` partition with the columns the producer reads (`account_transaction.SOURCE_COLUMNS` and what `normalize_trn` needs), through the reader `account_return_daily` already has, using the source entry the handler's `compute()` context holds (`_CLASS_CONTEXT["src"]`) or, when that is None, the declared source the handler reads the same way (`ard.declared_sources` and `ard.source_entry`). It reads one partition; it lists nothing new.
   - `emit_transactions(s3, firm, days, upload)` returns `(written, failed)`: for each day in sorted order, `rows = at49.normalize_trn(frame, firm)` then `res = at49.emit_transaction_day(s3, rows, firm, day, upload=upload)`, `written[day] = res["rows"]`. It NEVER raises: any `Exception` or `SystemExit` for a day is `failed[day] = "<type>: <text up to 300 chars>"` and the line `  TRANSACTION_SKIPPED <day> <reason>` is printed; the other days still run. When `at49` is None every day fails with `AT49_IMPORT_ERROR`'s text. A day that landed prints `  <day> transaction rows=<n> LANDED` (or `DRY` when `upload` is false), like `emit_classes`.
3. **The wiring.** In the scheduled `run`, call it ONCE, AFTER the filled-report stage, for `sorted(written)` with `upload=not dry_run`, and add `"transaction_rows"` and `"transaction_failed"` to the returned dict. In `run_backfill`, call it ONCE after `filled_write`, same days and upload, same two keys in the returned dict. NOT in the lots-only branch of `run_backfill`, NOT in `run_day_event`, NOT in the local CLI. Change nothing else in the handler: every existing key, order and call stays.
4. **Tests** `infra/aws/lambda/investor-reporting/reporting-gold/tests/test_transaction_emission.py`: at least 14 tests with names containing `guarded`, `import`, `emit`, `skipped`, `never`, `upload`, `dry`, `scheduled`, `backfill`, `failure`, `order` and `lots`: the guarded import (a failing import leaves `at49` None and records the error), the emission per day, a refused day skipped and printed, an emit that raises, a partition that cannot be read, no raise ever, `upload=False` reaching the producer, the scheduled fire calls it after the filled stage and returns the two keys, a transaction failure leaves the returns, class, lots and filled results unchanged, the backfill calls it after the filled stage, the lots-only backfill does not, and the one-day filled event does not. Where a test needs the handler's heavy stages, patch them as the existing tests do. **Twelve existing tests in `test_activity_lot_emission.py`, `test_class_catch_up.py` and `test_class_table_emission.py` fail at the base** (the fakes lack `as_of` after a later handler change); they are PRE-EXISTING and outside your grant: do not edit them, file ONE observation row naming them, and make sure your own harness does not inherit the defect.
5. **Mutants** (temporary, reverted): (a) call `emit_transactions` BEFORE the filled stage in `run`: at least one test fails; (b) let an exception in `emit_transactions` propagate (remove the catch): at least one test fails. Say which test failed each.

<criterion id="DBF136-1-AC1" cell_refs="DB-f-2201" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_handler.py" . DBF136-1-AC1</invocation><expect>DBF136-1-AC1 PASS</expect></criterion>
`DBF136-1-AC1` -- the emission function, run by the checker with stubs: each day's rows go through `emit_transaction_day(upload=...)` and come back as `({day: rows}, {})`; a day the producer refuses, a day whose emit raises and a day whose partition cannot be read are skipped, printed as `TRANSACTION_SKIPPED <day>` and leave the other days written; a producer that did not import fails every day with the import error's text; no days return `({}, {})`; nothing raises. Base: FAIL (no function).
<criterion id="DBF136-1-AC2" cell_refs="DB-f-2201" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_handler.py" . DBF136-1-AC2</invocation><expect>DBF136-1-AC2 PASS</expect></criterion>
`DBF136-1-AC2` -- the wiring, read from the handler's syntax tree: the guarded import and its error constant; `run` and `run_backfill` each call `emit_transactions` exactly once, after their filled-report stage, and return `transaction_rows` and `transaction_failed`; `run_day_event`, the stage functions of the earlier tables and the lots-only branch do not call it. Base: FAIL.
<criterion id="DBF136-1-AC3" cell_refs="DB-f-2201" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_handler.py" . DBF136-1-AC3</invocation><expect>DBF136-1-AC3 PASS</expect></criterion>
`DBF136-1-AC3` -- the new test file holds at least 14 tests with the named words, and the whole tests directory shows no failure beyond the twelve pre-existing ones the issuer recorded (`checks/r136/handler_tests_base_failures.txt`). Base: FAIL (no test file).
<criterion id="DBF136-1-J1" cell_refs="DB-f-2201" judgment="true">JUDGMENT, graded only by 3.0.0_SA_CVO at L9, never self-graded: the CVO compares **20 sampled rows of the Inflection producer's output drawn FRESH after the merge from the ONE newest Orion snapshot** (the issuer's `tools/sample_inflection_latest_snapshot.py`, seed 135, one forced rolled line) **against the source rows by their NATURAL KEY**, field by field for the 19 columns, with the one-snapshot census printed beside it (rows per status, Complete rows, duplicate keys, the Reversed keys derived from that snapshot, the producer's rows out, and zero source lines on more than one emitted day), and the S6 print "N of 96" from the launcher's report. Committed form: the snapshot day, the key hashes and the non-figure results.</criterion>
<criterion id="DBF136-1-J2" cell_refs="DB-f-2201" judgment="true">JUDGMENT, graded only by 3.0.0_SA_CVO at L9, never self-graded: the CVO compares **20 sampled rows of the 49 Financial producer's output, drawn FRESH after the merge** (the issuer's `tools/sample_49f_producer_rows.py`), **against the source rows by their NATURAL KEY**, field by field for the 19 columns, including the per-row business-date claim; the sample includes at least one of the lines whose trade date falls on a non-trading day (`inferred`) and at least one `measured` line. Drawn and committed as for J1.</criterion>

<expected_criteria>DBF136-1-AC1,DBF136-1-AC2,DBF136-1-AC3,DBF136-1-J1,DBF136-1-J2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, the words file, `account_return_daily.py`, the other handler tests, every Terraform file, the source map.
- **AWS: none.** **NOT WIRED INTO THE FUNCTION'S BUNDLE OR ROLE.** The bundle members and the write grant are two sibling orders; the apply is the applier's.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2201-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES (the file is shared and append-only). Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2201/
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_transaction_emission.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2201.fwd5-49f-gold-handler-emits-the-transaction-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R136_F.md</decomp_doc> round 136, workstream ~F2 (F-SHIP), cell `DB-f-2201`.
<owned_cells>DB-f-2201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF136-1-AC1, DBF136-1-AC2, DBF136-1-AC3 (mechanical); DBF136-1-J1, DBF136-1-J2 (judgment, the CVO's). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2201/IRPT_DASHBD.TO-DB-f-2201.fwd5-49f-gold-handler-emits-the-transaction-day.proof_of_spec.json`
(copy the shape of the instance at `deliverables/0.9.0_WK_IRPT_DASHBD~2101/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DBF136-1-AC1,DBF136-1-AC2,DBF136-1-AC3 --governing-order <this order>` (run from the repo root, the order path repo-relative) BEFORE you finish; pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** your final message, once: each mechanical criterion's last line; the new test count and the result of the whole tests directory (passed, failed, and the failed ids that are not among the twelve); the two mutants and which test failed each; the commit hash(es); anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: code in a branch and offline tests; nothing is deployed, scheduled or run, and the function's bundle and role are not changed by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed here (the write prefix is the sibling order DB-f-2202); the worker has no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF136-1-AC1 to AC3 FAIL at base, the checker's helpers are exercised by its self-test (6 arms) and a reference implementation in a scratch copy of the handler passed its behaviour and wiring clauses.
lane: the <paths> block IS the grant.
</preflight>
