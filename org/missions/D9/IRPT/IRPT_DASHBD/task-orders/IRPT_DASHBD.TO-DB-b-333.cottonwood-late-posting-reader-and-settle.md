# TO IRPT_DASHBD.TO-DB-b-333 -- the Cottonwood LATE-POSTING READER: the account-return derivation counts each TransactionID once over the partitions from the window's first day through the 14th trading day after its last day, a day with no partition of its own is present when rows dated it post later, and each scheduled fire settles the landed day 14 trading days back through the rewrite path (CTO rulings after dell1's finding, msg 7612; surprise row IRPT_DASHBD-D2-S137) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-333</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~259</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>LATEWIN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** LATEWIN, round 150 | **Ordered by:** the CTO's rulings (the reader fix, msgs 10587 and 10591; the late-posting window, msg 10598) on the issuer's measured finding (row `IRPT_DASHBD-D2-S137`: trade date 2026-07-24 appears in 19 `fact_transactions` partitions as 3,328 rows against 277 distinct TransactionIDs, so the landed gold external flows are inflated 8 to 13 times) | **Decomp cell:** `DB-b-333` (decomposition section 194).

**Risk class WORLD (the gate's floor for a path under `infra/`):** in fact code and tests in a workspace worktree; nothing is deployed, applied or written to AWS by this cell. The code reaches the function only in a later signed release (folded with ~F2's transaction stage, order `TO-DB-f-2706`), after which ONE all-days rewrite pair repairs the gold.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-259` (branch `wk-IRPT_DASHBD-259`, a FULL checkout cut from the current `box/dell2`). Work only there; never push. Python and pytest are on the PATH; the repo's line endings are LF; ASCII only in code, tests and records. No AWS call: every test uses fakes. Counts, hashes and words only in anything you write.

**What is wrong (read these first, whole):** `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` -- `derive` (the line `trans_parts = [p for p in reader.list_partitions("fact_transactions") if p >= start]` and the loop after it), `window_flows`, `presence_hold`, `run_day`; `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` -- `owed_days`, `_run`, `_rewrite`, `lambda_handler`; the three existing test files of these (`data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py` and `test_cottonwood_rewrite.py`, `infra/aws/lambda/investor-reporting/account-return-daily/tests/test_handler.py` and `test_transaction_emission.py`); the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p199_cot_late_window.py` and its probe `.../p199_probe_late_window.py` (the tests the checker runs against your code: read it, it states the behaviour exactly). The silver `fact_transactions` partitions are ROLLING pulls: a trade appears in many partitions and can first post in a LATER partition than its trade date. `derive` sums every row of every later partition, so a repeated trade is counted many times.

**The cell (`DB-b-333`). Four changes and one test file.**
1. **The window.** Add `LATE_WINDOW_TRADING_DAYS = 14` and a helper `shift_trading_days(day_iso, n)` (the trading day n trading days after (n >= 0) or before (n < 0) the trading day, through `trading_calendar`), and a helper `transaction_partitions(reader, start, end)` returning the `fact_transactions` partitions `p` with `start <= p <= `(the 14th trading day after `end`). `derive` reads exactly those partitions, no later one.
2. **The dedup.** In `derive`, count each `TransactionID` ONCE: when the same id appears in several partitions the LATER partition's copy replaces an earlier one (a dict keyed by the id, filled in ascending partition order). A row with no `TransactionID` is kept as its own row. The census counts and `window_flows` run over the deduplicated rows. The function signatures, the returned shapes and every existing column stay as they are.
3. **The presence.** `presence_hold(reader, day)` keeps its present rule (a `fact_transactions` partition named `day` makes the day present) and ADDS: when no partition of that day exists, the day is present if a row whose `Trade Date` (read with `parse_trade_date`) is that day exists in the partitions from `day` through the 14th trading day after it. Otherwise the day is held with a reason that starts `HOLD` and names `fact_transactions`.
4. **The settle (handler).** Add `SETTLE_LAG_TRADING_DAYS = 14` and a function `settle_days(s3, owed)` returning the sorted landed days a scheduled fire settles: for each owed day, the day 14 trading days earlier, when it is at or after `FLOOR_DAY`, is landed (`landed_days` of the gold prefix), is not itself in `owed` and is not already in the result. In `lambda_handler`, a SCHEDULED fire (no `day`, `days`, `rewrite` or `transaction` key) ALSO rewrites each of those days, one at a time through `_run(s3, reader, [day], upload, rewrite=True)`, AFTER the owed days and the transaction stage, with the same `upload` (a dry run writes nothing). It NEVER raises: a day that fails is recorded under `settle_failed[day] = "<type>: <text>"` and printed as `SETTLE_FAILED <day> <text>`, and an error in naming the days records `settle_failed["*"]`. The returned dict keeps every present key and, ONLY for a scheduled fire, gains `settled` ({day: that day's result}) and `settle_failed`. An explicit `day` or `days` event settles nothing and carries neither key. Edit `lambda_handler` ONLY at: the new constant and function above `_clients`; one line after `_clients(...)` that records whether the fire is scheduled; and the tail (the `return`, which becomes a dict `out` plus the two keys). Do NOT touch `transaction_frame`, `emit_transactions`, `_transaction_only`, `owed_days` or `_rewrite` (another seat's cell edits the transaction stage).
5. **Your test file** `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_late_window.py` (the name starts exactly so; pytest, fakes, no network; the words `TransactionID`, `dedup` and `settle` appear in it). Cover, with your own synthetic partitions: a trade repeated in many rolling partitions counts once; the later copy wins; a trade that first posts in a later partition inside the window counts; a partition after the 14th trading day is not read; `presence_hold` for an absent own-partition day (rows dated it in a later partition: present; only beyond the window or none: held); `settle_days` (the 14-back day, not landed, before the floor, the owed day itself, a duplicate); a scheduled fire's settle (writes the back day's keys and the owed day's keys and no other; a dry run writes nothing); an explicit `day` event settles nothing; a settle failure leaves `results` byte-equal to a clean run; and a day written early (few partitions) then rewritten at the full window equals the independent sum of its distinct ids. Update the fixtures of the existing tests ONLY where a changed rule forces it (they should pass unchanged; the old rule "a partition named the day is present" is kept).
6. **Files you may change:** the adapter, the handler, the four existing test files above (only where forced) and your new test file. Nothing else; no fixture file; no script; no schema; no Terraform. At most 150 changed lines in the adapter and 120 in the handler.
7. **Run the checks yourself from your worktree root** (the checker reads the branch point as `git merge-base HEAD box/dell2`): the three invocations below. AC3 also reads S3 READ-ONLY from this box (a live derivation of 2026-07-24 against today's silver compared with an independent deduplicated sum; it needs the box's AWS access and takes a minute or two). Commit your files with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~259 <0.9.0_WK_IRPT_DASHBD~259@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer; READ the whole gate output; `.tools/commit-gate.sh` runs on `.py` files: py_compile, ds-precommit, ruff).
8. **Record** `RD_LATE_WINDOW_FACTS_R150.json` in your folder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~259/`) with EXACTLY these fields: `branch` ("wk-IRPT_DASHBD-259"); `head` (your last workspace commit, 40 hex); `files_changed` (sorted repo paths); `lines_changed` ({"adapter": n, "handler": n}); `tests_added` (the new test file name); `live` ({"distinct_flow_ids": n, "accounts_compared": n, "raw_sum_inflated_accounts": n}, copied from the checker's AC3 output line); `words` (one paragraph, 80 to 1800 characters: what changed and why, what the live check showed, and what is NOT proven: nothing is deployed, the gold is not rewritten, the 49 Financial and Inflection derivations are untouched).

<criterion id="DBC199-1-AC1" cell_refs="DB-b-333"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p199_cot_late_window.py" C:/dev/wk-irpt-dashbd-259 DBC199-1-AC1</invocation><expect>DBC199-1-AC1 PASS</expect></criterion>
`DBC199-1-AC1` -- the diff and the source: only the adapter, the handler, the four named test files and the new test file changed since the branch point, within the line caps; the adapter reads TransactionID; the handler settles through the rewrite path. Base: FAIL.
<criterion id="DBC199-2-AC1" cell_refs="DB-b-333"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p199_cot_late_window.py" C:/dev/wk-irpt-dashbd-259 DBC199-2-AC1</invocation><expect>DBC199-2-AC1 PASS</expect></criterion>
`DBC199-2-AC1` -- the behaviour: the cell's own test file passes and the issuer's probe (16 tests, copied into the tests directory by the checker, run and deleted) passes against your code. Base: FAIL (12 of the 16 fail on the unfixed code).
<criterion id="DBC199-3-AC1" cell_refs="DB-b-333"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p199_cot_late_window.py" C:/dev/wk-irpt-dashbd-259 DBC199-3-AC1</invocation><expect>DBC199-3-AC1 PASS</expect></criterion>
`DBC199-3-AC1` -- the proof: the existing adapter, rewrite and handler suites and the cell's tests pass; ruff is clean on the two files; and a LIVE read-only derivation of 2026-07-24 equals an independent deduplicated sum while the raw sum differs (the control). Base: FAIL (the cell's test file is missing, and the live derivation differs on 30 accounts).

<expected_criteria>DBC199-1-AC1,DBC199-2-AC1,DBC199-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the repo the write set of step 6. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files and, in the checker's AC3 only, S3 (read only). Writes: your worktree and the workspace folder and files named below. No AWS write, no Terraform, no push, no deploy.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W259-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~259/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-333.cottonwood-late-posting-reader-and-settle.md
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_rewrite.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_late_window.py
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/test_handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/test_transaction_emission.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 194 (round 150, workstream LATEWIN), cell `DB-b-333`.
<owned_cells>DB-b-333</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC199-1-AC1, DBC199-2-AC1, DBC199-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~259/IRPT_DASHBD.TO-DB-b-333.cottonwood-late-posting-reader-and-settle.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC199-1-AC1,DBC199-2-AC1,DBC199-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; your last workspace commit (git read); the change in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: code and tests in a workspace worktree; no plan, no apply, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the criteria FAIL at base, the issuer's probe passes 16 of 16 on the issuer's reference edit and fails 12 of 16 on the unfixed code, and 19 single-fault mutants of the reference are each refused (the live clause passes on the reference and fails on the base).
lane: the <paths> block and the CTO's rulings ARE the grant.
</preflight>
