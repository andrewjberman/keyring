# TO IRPT_DASHBD.TO-DB-f-2706 -- the COTTONWOOD TRANSACTION STAGE READS THE LATE-POSTING WINDOW, ONE cell: the handler reads the partitions D through D+14 trading days, keeps the rows whose business date is D, dedups on TransactionID, writes a day ONCE and only when its full window exists, runs on its OWN owed days at the scheduled fire, and reports the newest writable day; the CTO's msgs 10588, 10592 and 10597

<to_id>IRPT_DASHBD.TO-DB-f-2706</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2706</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>139</round>
<workstream>F2COTWINDOW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2COTWINDOW (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, msgs 10588 ("read partitions D through D+14 trading days, filter trade_date = D, and dedup on transaction_id"), 10592 and 10597 ("Write day D only once its full D..D+14 window exists (100 percent), and write it once ... The receipt names the newest writable day") | **Decomp cell:** `DB-f-2706` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md`, amendment 5) | **outcome_ref:** FWD-5 | **depends_on:** `DB-f-2605`, `DB-f-2606` (merged).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): code and tests in a branch; no AWS call, no Terraform command, no upload, no push. The build, the upload and the apply are later acts of the Cottonwood pair, after this cell and `2.0.0_SA_COO~D2`'s reader fix ship as ONE code release.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2706` (branch `wk-IRPT_DASHBD-2706`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2706/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS: make no AWS call** (the tests use fakes). No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why (measured).** The Cottonwood fact_transactions silver is a rolling 14-day period pull: a business day's rows sit in the partitions D through D+14 trading days and repeat across about ten of them (8,701 raw rows against 875 distinct TransactionIDs on one day). The stage built in `DB-f-2605` reads the ONE partition `date=D` and refuses the whole day when any row's business date is not D, so on the real silver it would skip 125 of 127 days. None of the 14 columns the producer reads varies across partitions for one TransactionID; same-partition rows sharing an id differ only in portfolio columns, so a dedup on `TransactionID` loses nothing the producer reads.

**The cell (`DB-f-2706`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotwindow.py` (your three criteria; its module docstring is the API spec; `Silver`, `FakeS3`, `Recorder` and the AC bodies are the exact behaviors; it has a `--selftest`), the issuer's REFERENCE sketch `checks/r139/p139_cotwindow_reference.py` (a patch that makes AC1 and AC2 pass: you write the production version in the handler's own style, with proper docstrings and no private-attribute reach if a small public helper in the producer is cleaner), `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (whole), `data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py` (`normalize_trn`, `emit_transaction_day`, `_day_of`) and the tests `infra/aws/lambda/investor-reporting/account-return-daily/tests/test_transaction_emission.py` and `test_handler.py`.
2. **The handler** (`handler.py`): add the module constant `TX_WINDOW = 14` and the functions `trading_lag(day, partition)` (trading days from `day` to `partition`, counted as `len(tc.trading_days_between(day, partition)) - 1`, `-1` when the partition is before the day), `window_end_day(day)`, `window_complete(day, newest_silver)` (true when the lag from `day` to the newest silver partition is at least 14), `newest_writable_day(newest_silver)` (the trading day 14 trading days before the last trading day on or before `newest_silver`), `transaction_owed_days(newest_landed, newest_silver, max_days=MAX_DAYS_PER_FIRE)` (nothing before `FLOOR_DAY`; exactly `[newest writable day]` when nothing has landed; otherwise the trading days after the newest landed day through the newest writable day, oldest first, at most `max_days`). Rewrite `transaction_frame(s3, reader, day)`: list the partitions with `reader.list_partitions("fact_transactions")`, read ONLY those with `0 <= trading_lag(day, p) <= TX_WINDOW`, concatenate, REFUSE (`SystemExit` naming `TransactionID`) when any row has a null or blank `TransactionID`, drop duplicates on `TransactionID` keeping the first in partition order, compute each row's business date by the producer's own rule (the first trading day on or after the Trade Date within the producer's window) and REFUSE when a row has no placeable Trade Date, and return only the rows whose business date is `day`. Rewrite `emit_transactions(s3, reader, days, upload)` (same signature and the same `(written, failed)` return, never raises): a day whose window is not complete (`window_complete` false for the newest silver partition) is NOT written and is recorded in `failed` with a reason containing the word `window`; a day whose `date=` partition already exists under the transaction gold prefix (listed through the producer's builder address, never a typed path) is NOT written and is recorded with a reason containing `already landed`; otherwise it is written through the producer as today (`upload=False` is the dry run).
3. **The wiring** (`lambda_handler`): the SCHEDULED fire (no `day` and no `days` key) runs the stage ONCE after the returns on `transaction_owed_days(<newest landed transaction day or None>, <newest silver partition>)`, not on the returns days; a `day`, `days` or `rewrite` event never runs the stage (its `transaction_rows` and `transaction_failed` are empty maps); the returned dict carries `transaction_window` = `{"newest_silver": ..., "newest_writable_day": ...}` on the scheduled fire and on the `transaction` event (it may be `None` otherwise); print one line `OWED_TRANSACTION: newest writable <day>, days [...]` on the scheduled fire. The `transaction` event (`_transaction_only`) keeps its validation, floor and cap and runs `emit_transactions` (so it too writes only full windows, once). Nothing in the returns path (`run_day`, `owed_days`, `_run`, `_rewrite`) changes.
4. **The tests** (the function's tests directory): bring `test_transaction_emission.py` and, if it fails, `test_handler.py` to the new rule so the directory reads GREEN (0 failed): the tests of the old behavior (the stage on every written returns day; one partition per day; a `days` event running the stage) are rewritten to the new rule, not deleted without a replacement. Add tests for each public function above, for the window reader against a fake silver (the late row at lag 14 kept, the row first seen at lag 15 excluded, other business days excluded, two lines sharing an id collapsed to one, a blank id refused), for the once-and-full-window rule, and for the scheduled fire and the three event kinds that never run the stage.
5. **The function-map entry:** the handler (and any bundled file you edit) is pinned in `infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json`. COMMIT THE CODE FIRST; then re-pin the entry's `staged_from` pin of each edited file to the commit that carried it and its new sha256, exactly as cell `DB-f-2606` did (read its commit `5f021a5859` and the entry); touch no other key of the entry and no other file of the folder.
6. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotwindow.py" . DBF139-6-AC1`, then `AC2`, then `AC3` (AC3 runs the tests directory and the round-138 bundle criteria `DBF138-6-AC1` to `AC3`). Write `RD_COTTONWOOD_WINDOW_FACTS_R139.json` in your folder: `claim` ("measured"), `tests_before`, `tests_after`, `tests_added`, `files_touched`, `pins_moved`.
7. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2706 <0.9.0_WK_IRPT_DASHBD~2706@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): the handler, its tests and any producer file in one commit; the entry's re-pin in a second; the record and the proof in a third.

<criterion id="DBF139-6-AC1" cell_refs="DB-f-2706" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotwindow.py" . DBF139-6-AC1</invocation><expect>DBF139-6-AC1 PASS</expect></criterion>
`DBF139-6-AC1` -- the window primitives (`window_end_day`, `window_complete`, `newest_writable_day`) read the calendar as stated, and `transaction_frame` returns exactly the deduped rows of the business day from the window partitions only (the late row at lag 14 kept, the lag 15 row and other business days excluded, no partition outside the window read, a blank TransactionID refused). Base: FAIL (no `TX_WINDOW`).
<criterion id="DBF139-6-AC2" cell_refs="DB-f-2706" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotwindow.py" . DBF139-6-AC2</invocation><expect>DBF139-6-AC2 PASS</expect></criterion>
`DBF139-6-AC2` -- `transaction_owed_days` returns the stated days (capped, floored, nothing landed gives the newest writable day only); `emit_transactions` writes a full-window day once with the deduped row count, names an incomplete window and an already landed day in `failed` without writing, and a dry run passes `upload` False. Base: FAIL (no `transaction_owed_days`).
<criterion id="DBF139-6-AC3" cell_refs="DB-f-2706" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotwindow.py" . DBF139-6-AC3</invocation><expect>DBF139-6-AC3 PASS</expect></criterion>
`DBF139-6-AC3` -- the scheduled fire runs the stage on the transaction owed days (not the returns days) and reports `transaction_window`; `day`, `days` and `rewrite` events never run the stage; the function's tests directory is green; and the function-map entry still pins the files it packages (`DBF138-6-AC1` to `AC3` PASS). Base: FAIL (no `trading_lag`).

<expected_criteria>DBF139-6-AC1, DBF139-6-AC2, DBF139-6-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the returns adapter (`cottonwood_bd_account_return_daily.py`), the rest of the producer chain, the checkers, Terraform, the registry.
- **AWS: none; no Terraform; no upload; no push.** No change to the returns path. Another cell (`2.0.0_SA_COO~D2`'s reader fix, task order `TO-DB-b-332`'s successor) edits the same function's adapter and the scheduled fire's rewrite step: on a conflict in `handler.py` file a BLOCKING row and stop; do not merge by hand.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker or an order sentence is wrong, file a BLOCKING row and stop. A literal the commit naming limb refuses is a BLOCKING row, not a workaround.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2706-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2706/
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/
infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json
data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2706.cottonwood-transaction-stage-reads-the-late-posting-window.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md</decomp_doc> round 139, workstream F2COTWINDOW (F-SHIP), cell `DB-f-2706`.
<owned_cells>DB-f-2706</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF139-6-AC1, DBF139-6-AC2, DBF139-6-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2706/IRPT_DASHBD.TO-DB-f-2706.cottonwood-transaction-stage-reads-the-late-posting-window.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2704/IRPT_DASHBD.TO-DB-f-2704.inf-pipeline-new-account-transaction-role-runner-assumes-it.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF139-6-AC1,DBF139-6-AC2,DBF139-6-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the pytest line before and after; the pins moved; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the edit is the Cottonwood landing function's transaction stage and its tests, nothing is deployed in this order; the later apply's blast radius is named in the Cottonwood packet's addendum.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed; nothing is deployed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF139-6-AC1 to AC3 FAIL at base, a reference handler put into the tree by the issuer made AC1 and AC2 PASS and AC3's wiring clauses PASS and was restored with git checkout, and the checker's pure helpers are exercised by its selftest (5 arms).
lane: the <paths> block IS the grant.
</preflight>
