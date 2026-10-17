# TO IRPT_DASHBD.TO-DB-f-2605 -- the COTTONWOOD LANDING HANDLER EMITS THE TRANSACTION DAY, ONE cell: `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` gains the guarded `account_transaction_cottonwood` import, `transaction_frame`, `emit_transactions` (never raises), the stage as the LAST step of the scheduled/day/days path for the written days, a transaction-only event, and a new test file; the CTO's XA-20261016T224156Z-3c21 (msg 10002)

<to_id>IRPT_DASHBD.TO-DB-f-2605</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2605</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>F2COTHD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2COTHD (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, XA-20261016T224156Z-3c21 (RULED 23:02:55Z; msg 10002): host the landing function; condition (ii) "the stage runs AFTER the returns-day write is committed and its failure cannot alter or roll back account_return_daily (read back: a planted stage failure leaves that day's returns byte-equal)"; the CTO's acceptance of the round 138 list (msg 10145, item 1) | **Decomp cell:** `DB-f-2605` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md`, "Cells 4 and 5") | **outcome_ref:** FWD-5 | **depends_on:** none (the producer `data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py` is on the trunk).

**Risk class WORLD** is the floor of the path below (`infra/` path): code and offline tests in a branch. No AWS call, no Terraform, no upload, no push. The bundle (the function-map entry's members), the plan, the apply and every run are later acts.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2605` (branch `wk-IRPT_DASHBD-2605`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2605/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS: make no AWS call.** No client data is read or recorded (tests use made-up frames). Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The Cottonwood `account_transaction` table is produced by `account_transaction_cottonwood.py` from one day of the Black Diamond `fact_transactions` silver. The CTO ruled the landing function the host (the last stage of the function that writes the firm's returns day). Its role already reads that silver; the stage needs only the code.

**The cell (`DB-f-2605`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_handler.py` (your three criteria; its `BEHAVIOUR` script, `behaviour_problems`, `wiring_problems`, `source_problems` and the AC3 test clauses are the exact spec; it has a `--selftest`); the handler `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (whole) and its tests directory (16 tests pass at the base); the producer `data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py` (`normalize_trn`, `emit_transaction_day`, `SOURCE_COLUMNS`) and the adapter the handler already imports for the Black Diamond silver (`cottonwood_bd_account_return_daily.py`, its silver reader); and, as the MODEL of the same shape on the sister function, `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` (`at49` guarded import, `transaction_frame`, `emit_transactions`, the transaction-only backfill stage).
2. **The edit: the handler only** (one source file; plus the new test file), ASCII, no new dependency:
   - the GUARDED import: `import account_transaction_cottonwood as atc` in a try/except that sets `atc = None` and `ATC_IMPORT_ERROR` (a one-line text) on failure; the function must still run its returns path when the producer is not importable.
   - `transaction_frame(s3, reader, day)`: that day's Black Diamond `fact_transactions` partition read through the adapter's silver reader (the same reader the returns path uses), as a frame.
   - `emit_transactions(s3, reader, days, upload)`: for each day, `atc.normalize_trn(frame, "cottonwood")` then `atc.emit_transaction_day(s3, rows, "cottonwood", day, upload=upload)`; returns `(written, failed)` = `({day: rows}, {day: "<ExceptionType>: <text up to 300>"})`; it NEVER raises (catch `Exception` and `SystemExit` per day), prints `TRANSACTION_SKIPPED <day> <reason>` for a failed day, and fails every day with the import error's text when `atc is None`.
   - the scheduled/`day`/`days` path calls `emit_transactions` ONCE, AFTER every `run_day` has run, for the days actually WRITTEN (not held), and adds `transaction_rows` and `transaction_failed` to its result WITHOUT changing the existing keys (`ok`, `days`, `results`, `held`); a planted stage failure leaves those four keys byte-equal to a clean run.
   - a transaction-only event `{"transaction": {"start": "<day>", "end": "<day>"}}` (exactly those two keys; no `day`/`days`/`rewrite` with it): the trading days of the range, validated by the handler's existing floor and `MAX_BACKFILL_DAYS` rules (a day before `FLOOR_DAY`, more than the cap, or start after end is refused BEFORE any call), `dry_run` honoured (upload False), `run_day` never called; the result carries `transaction: true`, `days`, `transaction_rows`, `transaction_failed`.
   - the `rewrite` path and `_run` / `_rewrite` stay exactly as they are (they must not call `emit_transactions`).
3. **The tests:** a NEW file `infra/aws/lambda/investor-reporting/account-return-daily/tests/test_transaction_emission.py` with at least 14 tests, offline, whose names between them contain the words guarded, import, emit, skipped, never, upload, dry, held, planted, byte, order, rewrite, transaction_only and floor (the checker's AC3 reads them); the 16 existing tests stay as they are and must still pass.
4. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_handler.py" . DBF138-5-AC1`, then `AC2`, then `AC3`. Write `RD_COT_HANDLER_FACTS_R138.json` in your folder: `claim` ("measured"), `tests_added`, `tests_total`, `files_touched` (2), `other_files_touched` (0).
5. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2605 <0.9.0_WK_IRPT_DASHBD~2605@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): the handler and the new tests in one commit, the record and the proof in a second.

<criterion id="DBF138-5-AC1" cell_refs="DB-f-2605" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_handler.py" . DBF138-5-AC1</invocation><expect>DBF138-5-AC1 PASS</expect></criterion>
`DBF138-5-AC1` -- the guarded import, `transaction_frame` and `emit_transactions` exist and behave: each day written through `emit_transaction_day(upload=...)`, a refused or raising day skipped with `TRANSACTION_SKIPPED`, nothing raises, a non-importable producer fails every day with its error, and the transaction-only event runs the stage alone and refuses a bad range before any call. Base: FAIL (no `transaction_frame`).
<criterion id="DBF138-5-AC2" cell_refs="DB-f-2605" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_handler.py" . DBF138-5-AC2</invocation><expect>DBF138-5-AC2 PASS</expect></criterion>
`DBF138-5-AC2` -- the wiring: the scheduled/day/days path runs every `run_day` first and `emit_transactions` once after, for the written days only; a planted stage failure leaves the returns result byte-equal; the rewrite path never runs the stage. Base: FAIL (no `transaction_frame`).
<criterion id="DBF138-5-AC3" cell_refs="DB-f-2605" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_handler.py" . DBF138-5-AC3</invocation><expect>DBF138-5-AC3 PASS</expect></criterion>
`DBF138-5-AC3` -- the new test file holds at least 14 tests whose names carry the required words, and the whole tests directory passes. Base: FAIL (no new test file).

<expected_criteria>DBF138-5-AC1, DBF138-5-AC2, DBF138-5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, the adapter, every other handler, the bundle map, the Terraform roots, the checker.
- **AWS: none; no Terraform; no push.** No change to the function-map entry, `lambda-source-map` files, or any bundle member (the bundle cell is a later order).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker or an order sentence is wrong, file a BLOCKING row and stop. If `handler.py` at your worktree's HEAD differs from the one this order was cut against (check `git log -3 -- <handler>`), say so in your report.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2605-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2605/
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/test_transaction_emission.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2605.cottonwood-landing-handler-emits-the-transaction-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md</decomp_doc> round 138, workstream F2COTHD (F-SHIP), cell `DB-f-2605`.
<owned_cells>DB-f-2605</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF138-5-AC1, DBF138-5-AC2, DBF138-5-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2605/IRPT_DASHBD.TO-DB-f-2605.cottonwood-landing-handler-emits-the-transaction-day.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2603/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF138-5-AC1,DBF138-5-AC2,DBF138-5-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the pytest line (passed count); the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the edit is one handler and a new test file, nothing deployed; the handler's callers are the function's schedule and the DB-b-308 rewrite events (read by the issuer in the sizing read), and the rewrite path is kept untouched by criterion.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is changed here; the one new grant (a write on the new prefix) is cell DB-f-2604, and the sizing read found the role already reads the silver.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed; nothing is deployed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF138-5-AC1 to AC3 FAIL at base, a reference implementation in a scratch sibling directory made the source, behaviour and wiring clauses of the checker pass against today's handler (run by the issuer and removed), and the checker's pure helpers are exercised by its selftest (9 arms).
lane: the <paths> block IS the grant.
</preflight>
