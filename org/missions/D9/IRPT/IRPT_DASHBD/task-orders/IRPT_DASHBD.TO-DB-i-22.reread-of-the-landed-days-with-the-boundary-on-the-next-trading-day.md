# TO IRPT_DASHBD.TO-DB-i-22 -- the RE-READ: the Scope feed's landed days (two or more) run through the wrapper again with the boundary on the next trading day in place, each day's bronze manifest recounted, the boundary measure reporting its pair count; Inflection only, counts and verdict words only

<to_id>IRPT_DASHBD.TO-DB-i-22</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~320</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>133</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_132_20261019.md` @14e06e4b55 (msg 10703), enrichment E3: "Re-run the wrapper on the first two landed trading days with E1 in place; the boundary measure must report its pair count." Gated on `DB-i-20` merged and on a second landed day (this order is handed to its worker only when both hold).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-320`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/`. Your PRIVATE folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~320/` (create it). Never touch a path outside the `<paths>` block below and your private folder.

**Why.** Round 132 ran the round-129 run script on the Scope feed's first landed silver day: the wrapper's output matched the feed's own manifest, but one day cannot test the boundary measure (0 pairs) or the chain check. The boundary measure now pairs each landed day with the next TRADING day (cell `DB-i-20`, merged: `run_scope_feed_real.py` holds `next_trading_day`). This cell runs the same read again over every landed day, which is now two or more, so that the boundary measure reports its pair count on real rows. It is read-only against AWS (GET and LIST) and writes only to your private folder.

**Precondition.** At your first LIST of the silver table, if it lists FEWER THAN 2 partitions, STOP: write nothing, make no second attempt, report the count of partitions you listed. (The issuer hands you this order only when 2 or more have landed; the check is yours as well.)

**Read first (read only).**
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~319/live_read.py` and `SCOPE_LIVE_READ_R132.json`: the round-132 script and record this cell repeats. Your script is a new file, `reread.py`; you may copy its structure, not its output.
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py` (`run_real`, `measure_boundary`, `next_trading_day`, `TABLE_URI`): import `run_real` from it by path, do not edit it.
- `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` (`InflectionSilverReader`: `list_partitions`, `read_parquet`, `_split`, `_api`, `reads`; `build_account_dim`; `FIRM`) and `inflection_account_return_daily.py` (`ORION_SILVER`).
- `data/inf/manual_api/pull_inflection_scope_account_returns.py` (the bronze envelope: `feed_addresses`, `calls[].row_count`, `universe_rows`, `households_failed`, `households_without_id`, an integer count; the bronze object is `scope.json.gz`).
- `lib/trading_calendar.py` (`trading_days_between`).
- The checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_reread.py` (it calls the round-132 checker `r132/p132_live.py` on your record and adds the pair-count recount; read both first and run `python -I <it> --selftest`).

**The cell (`DB-i-22`).**
1. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/reread.py`, the only code this cell adds. It builds `reader = iad.InflectionSilverReader()`, imports `run_real` from the round-129 script, takes trading days from `lib.trading_calendar` (`trading_days_between` returning ISO strings), and defines NO weekday helper of its own. It holds no write call, no vendor call, no credential and no `s3://` literal (addresses from `feed_addresses` / `TABLE_URI`).
2. **The real run.** `dim_ids` = `iad.build_account_dim(<latest fact_positions frame>, <latest fact_assets frame>).column("account_id").to_pylist()` (as in the round-129 script's `main`). Call `run_real(reader, <private out dir>, dim_ids, <trading-days function>, iad.FIRM, 0)` with the output directory INSIDE your private folder and not yet existing. Its return value is the `run` record. If its status is `NO_SILVER_YET` or `STOPPED_AT_CAP`, STOP: write the record with that status and report; do not widen the cap and do not retry.
3. **The manifest read.** For each landed day (the `date=<day>` partitions of the silver table), read that day's bronze envelope through the same reader (list the bronze table prefix with `list_partitions`, read `date=<day>/scope.json.gz` with `reader._api().get_object(...)` after `reader._split(<uri>)`, count each GET in your own read counter) and keep ONLY: `universe_rows`, the length of `households_failed`, the list of `calls[].row_count`, and the integer `households_without_id`. Never keep a response body.
4. **The private extract** `reread_extract.json` in your private folder: `{"days": {"<iso day>": {"silver_rows": int, "universe_rows": int, "households_failed": int, "call_row_counts": [int, ...], "households_without_id": int}}, "boundary_rows": {"<sha256 of the account id string>|<iso day>": [status, start_market_value, end_market_value]}}` where `boundary_rows` holds one entry per row of every landed silver partition (status is the row's `status`; the two values are floats or null).
5. **The record** `SCOPE_REREAD_R133.json` in your folder with EXACTLY the keys of the round-132 checker's `REC_KEYS` (the same as `SCOPE_LIVE_READ_R132.json`): `script` {`file`, `sha256`}; `extract` {`path` (absolute, private), `sha256`}; `run` (the `run_real` return value, unchanged); `days_total`, `days_manifest_agree`, `days_manifest_disagree`, `days_with_failed_households`, `trading_days_in_window` (recount from the extract); `expected_rows`; `rows_accounted`; `verdict`; `reads`; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false; `basis_words` (words, at least 200 characters: how many days landed; how the silver row counts compare with the manifest per day, as counts; ABSENT rows per reason class; **how many boundary pairs, how many equal, and the maximum relative difference in basis points**; the chain check's status; what this does not establish; NO value, NO date, NO account or household id). No run of 8 or more digits except in a `sha256` value or a `path` / `file` field; no date and no partition name anywhere in the record.
6. **Do not fix.** If the wrapper refuses the real silver, or the manifest disagrees, or the boundary measure reads a large difference, that IS the result: record it with its verdict and a surprise row; never edit the wrapper, the run script or the feed, never choose another window, never retry with a changed rule.

<criterion id="DBI133-3-AC1" cell_refs="DB-i-22"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_reread.py" . DBI133-3-AC1</invocation><expect>DBI133-3-AC1 PASS</expect></criterion>
`DBI133-3-AC1` -- everything the round-132 checker grades on a record (complete, no identifier or date, the script a tracked file hashed as recorded with no write, vendor-call or credential token, the extract's hash equal, run status `RAN`, the day count, the per-day agreement with the bronze manifest, the trading-day count from `lib/trading_calendar.py`, accounts x trading days = PRESENT + ABSENT, `trading_days_unaccounted` 0, no write, no push, no deploy), and in addition: two or more landed days; the module that ran holds `next_trading_day`; the boundary measure reports at least 1 pair and its pairs, equal count and maximum difference equal the checker's recount from `boundary_rows`. Base: FAIL (no record).

<expected_criteria>DBI133-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and your private folder. Everything else is read, never edited, including the adapter, the wrapper, the run script, the feed script, `lib/`, `infra/` and every issuer check.
- **Reads only.** GET and LIST through `InflectionSilverReader` (and its `_api().get_object` for the bronze objects, after `_split`). No S3 write, no vendor call, no secret read, no push, no deploy. Read cap: 400 (LIST pages plus GETs); a cap hit is a recorded result, never widened.
- **Client data.** The silver, the bronze, the wrapper's output and the extract are private; the repo, rows and your report carry counts and verdict words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W320-S<k>` (continue the numbering your first order used), `surfaced_at` from `date -u +%FT%TZ` at filing; append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-22.reread-of-the-landed-days-with-the-boundary-on-the-next-trading-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 19, cell `DB-i-22`.
<owned_cells>DB-i-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI133-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/IRPT_DASHBD.TO-DB-i-22.reread-of-the-landed-days-with-the-boundary-on-the-next-trading-day.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI133-3-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the run status; the number of landed days; days whose silver count agrees with the manifest and days that do not (counts); rows PRESENT and ABSENT and the ABSENT count per reason class; the boundary pairs, pairs equal and maximum difference in basis points, and the chain check status, as the run record states them; the S3 reads made; row ids. No token, no client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: GET and LIST of Opal's own Orion silver and bronze through the round-108 reader (the granted prefixes and principal rounds 108 to 132 used); no new principal or grant, no write.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI133-3-AC1 FAILS at base (no record), and the checker's self-test builds a GOOD record from the feed's own writer and the reference boundary module (PASS) and nine mutants (pairs overstated, pairs_equal overstated, a changed maximum difference, zero pairs reported, the module without next_trading_day, one landed day only, a changed boundary row, a wrong verdict, a date in the record), each FAIL.
</preflight>
