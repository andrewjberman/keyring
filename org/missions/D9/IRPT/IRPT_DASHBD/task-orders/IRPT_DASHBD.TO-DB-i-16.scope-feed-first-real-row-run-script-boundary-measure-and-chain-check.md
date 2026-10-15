# TO IRPT_DASHBD.TO-DB-i-16 -- the FIRST-REAL-ROW RUN SCRIPT: the feed's silver through the GET-only reader into the round-127 wrapper, a PRIVATE local output directory, the Orion boundary measure (startValue(t+1) against endValue(t)) and a 238-to-365-day chain check; built and tested on fixtures; no S3 write, no vendor call

<to_id>IRPT_DASHBD.TO-DB-i-16</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~316</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>129</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_127_20261015.md` ADDENDUM 1 (msg 8736, open call dell2-20261015T223117Z-5df4 ruled yes; the CTO wrote "round 128", which is the cause-claim line, so this is round 129): "the GET-only reader feeds run() into a private local directory. Print the startValue(t+1) vs endValue(t) count and max difference, plus the 238-365 day chain check. No S3 write, no vendor call. The real run stays a same-day act once the feed's first silver lands."

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-316`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/`. Never touch a path outside the `<paths>` block below.

**Why.** The Scope feed (built by another seat) will land its first silver partitions soon. Rounds 123 to 127 built `adapt()` and `run()` on fixtures. The first run on REAL rows must be a same-day act, with its measurements ready, so this order builds the script that does it and proves it on fixtures. The real silver does not exist yet: the script must say so plainly (a result, not an error) when it finds none.

**What you build (two files, no more).**
1. `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py`: standard library, `pandas`, `pyarrow`, the estate's `inflection_account_dim` as `iad`, `inflection_account_return_daily` as `iar`, the round-127 wrapper `inflection_scope_feed_run` and `lib/trading_calendar.py`. Find the repository root and set `sys.path` as the template `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/tieout_basis_variants.py` does (`_find_root`, then the adapters directory).
2. `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/test_run_scope_feed_real.py`: pytest, synthetic rows only, at least 8 tests, one named `test_mutant_...`.

**Read first (read only).** `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py` (`run(silver, dim_frame, trading_days, firm, method_version, out_dir)` and its run record); `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` (`InflectionSilverReader`: `list_partitions`, `read_parquet`, `latest_partition`, `reads`; `build_account_dim(holdings, roster)`; `FIRM`); `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py` (`ORION_SILVER`); `data/inf/manual_api/pull_inflection_scope_account_returns.py` (the feed's silver columns and its table name `scope_account_returns`); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r129/p129_realrow.py` (its `FakeReader`, fixtures and whitelists ARE the specification; read it first and run `python -I <it> --selftest`).

**The cell (`DB-i-16`).** Text of the owned cell: *"The first-real-row run script: from the Scope feed's silver partitions read through the GET-only reader, call the round-127 wrapper into a private local directory, print the Orion boundary measure and a 238-to-365-day chain check as counts, and say NO_SILVER_YET or STOPPED_AT_CAP as results; tested on fixtures; no S3 write and no vendor call."*

### The functions (module level; the checker imports them by these names)

- `TABLE_URI = iar.ORION_SILVER + "scope_account_returns"`.
- `measure_boundary(silver)` -> `(pairs, pairs_equal, max_rel_diff_bp)`. `silver` is a dict `{partition name: pandas.DataFrame}` of feed rows. Over all rows, key each row by `(str(int(account_id)), day)`. A PAIR is a RETURNED row on calendar day `d` with a non-null `end_market_value` and a RETURNED row for the same account on `d + 1` with a non-null `start_market_value`. For each pair `diff = abs(end(d) - start(d+1))`; `pairs_equal` counts `diff <= 0.005`; the relative difference is `diff / max(abs(start(d+1)), 1e-9) * 1e4` (basis points) and `max_rel_diff_bp` is the largest, rounded to 2 decimals, or `None` when there are no pairs. NaN means null.
- `chain_check(table_rows, silver, trading_days, start, end)` -> dict `{"status", "window_calendar_days", "accounts_checked", "accounts_matching", "max_abs_diff_bp"}`. `table_rows` are the written table rows (dicts); `start` and `end` are ISO days. `window_calendar_days` = days from `start` to `end` inclusive. If it is under 238 -> status `WINDOW_TOO_SHORT`, 0, 0, None. Otherwise, for each account whose PRESENT rows cover EVERY trading day of `trading_days` inside `[start, end]`: `table_chain` = the product of `1 + total_return_daily` over those rows; `silver_chain` = the product of the silver `daily_factor` of the account's RETURNED rows over the calendar days from `start` to the last such trading day (a missing day counts as factor 1.0); `diff_bp = abs(table_chain - silver_chain) * 1e4`. An account MATCHES when `diff_bp <= 1e-6`. Status `OK` when every checked account matches, `MISMATCH` otherwise, `NO_COMPLETE_ACCOUNT` when none is checked; `max_abs_diff_bp` is the largest `diff_bp` rounded to 9 decimals (None when none checked).
- `run_real(reader, out_dir, dim_ids, trading_days_fn, firm, method_version, max_reads=400)` -> record dict.
  1. `parts = reader.list_partitions(TABLE_URI)`. If empty -> return `{"status": "NO_SILVER_YET", "partitions_listed": 0, "s3_reads": reader.reads}` and write NOTHING (not `out_dir`).
  2. If `1 + len(parts) > max_reads` -> return `{"status": "STOPPED_AT_CAP", "partitions_listed": len(parts), "s3_reads": reader.reads}` having made only the LIST; write nothing.
  3. Read every partition: `reader.read_parquet(TABLE_URI + "/" + name + "/data.parquet")`. `days` = the sorted distinct `day` values; `tdays = list(trading_days_fn(days[0], days[-1]))` (ISO strings).
  4. Call `inflection_scope_feed_run.run(silver, pandas.DataFrame({"account_id": [str(a) for a in dim_ids]}), tdays, firm, method_version, out_dir)`. A refusal (`ValueError`, for example a non-empty `out_dir`) propagates unchanged.
  5. `measure_boundary(silver)`; read the written `date=*/data.parquet` partitions back with pyarrow into row dicts; `chain_check(rows, silver, tdays, days[0], min(days[-1], days[0] + 364 days))`.
  6. Return EXACTLY these keys: `status` `RAN`, `contract_version`, `partitions_read`, `s3_reads` (`reader.reads`), `calendar_days_read`, `calendar_days_incomplete`, `rows_present`, `rows_absent`, `absent_by_reason`, `accounts_in_feed`, `accounts_mapped`, `accounts_unmapped`, `trading_days_unaccounted`, `market_value_eod_claim_counts` (the wrapper's run-record values), `boundary` {`pairs`, `pairs_equal`, `max_rel_diff_bp`}, `chain` (the chain_check dict), `method_version_used` (the argument), `out_dir_private` true. No date, no account id and no dollar figure appears in it.
- `main(argv=None)`: `argparse` with `--out-dir` and `--record`. Build `reader = iad.InflectionSilverReader()`; the dimension ids come from the estate's own builder as the round-108 module documents it: `iad.build_account_dim(<latest fact_positions frame>, <latest fact_assets frame>)` read with `reader.latest_partition(iar.ORION_SILVER + "fact_positions")` and `... "fact_assets"`, then `.column("account_id").to_pylist()`; `trading_days_fn` is `lib/trading_calendar.py`'s `trading_days_between` returning ISO strings; `firm` is `iad.FIRM`; `method_version` is 0 (a PRIVATE measurement run: no `dim_return_method` row exists for an Orion return, and the record says `method_version_used` 0). Call `run_real`, write the record as ASCII JSON (`indent=2`, `sort_keys=True`, trailing newline) to `--record`, print its `status`, return 0. The real `main` is NOT exercised by the checker or by you (the silver does not exist yet); keep it short and make sure it imports.

### The tests

Your own `FakeReader` (list_partitions, read_parquet, latest_partition, a `reads` counter) and your own synthetic world (not the checker's). Cover: the RAN record's keys and counts on a small feed; NO_SILVER_YET writes nothing and reads once; STOPPED_AT_CAP makes only the LIST; a non-empty `out_dir` is refused; the boundary measure with equal, unequal, NaN and missing-neighbour pairs; the chain check OK, MISMATCH (an altered row), WINDOW_TOO_SHORT and NO_COMPLETE_ACCOUNT; and `test_mutant_...`: take `run_scope_feed_real.py`'s source text, change ONE rule (for example the 238-day floor), execute the mutated source, and assert its output differs on your 7-day case. ASCII only. Run `python -I -m pytest -q <your test file>` until green.

<criterion id="DBI129-1-AC1" cell_refs="DB-i-16"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r129/p129_realrow.py" . DBI129-1-AC1</invocation><expect>DBI129-1-AC1 PASS</expect></criterion>
`DBI129-1-AC1` -- `run_real()` on fixtures: the RAN record equals the wrapper's golden counts (7 partitions, 17 PRESENT and 11 ABSENT rows, 8 reads); no silver reads NO_SILVER_YET with one read and no directory; a read cap reads STOPPED_AT_CAP with only the LIST and no directory; a non-empty output directory is refused. Base: FAIL (no script).

<criterion id="DBI129-1-AC2" cell_refs="DB-i-16"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r129/p129_realrow.py" . DBI129-1-AC2</invocation><expect>DBI129-1-AC2 PASS</expect></criterion>
`DBI129-1-AC2` -- the measures: the boundary fixture reads 2 pairs, 1 equal, 100.0 bp; a feed with no end values reads 0 pairs and None; the 299-day chain reads OK for 1 of 1 account with a difference within 1e-6 bp; an altered row reads MISMATCH; a 7-day window reads WINDOW_TOO_SHORT. Base: FAIL (no script).

<criterion id="DBI129-1-AC3" cell_refs="DB-i-16"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r129/p129_realrow.py" . DBI129-1-AC3</invocation><expect>DBI129-1-AC3 PASS</expect></criterion>
`DBI129-1-AC3` -- the script imports no AWS client, network or socket module, holds no write, invoke, vendor or credential token and no `s3://` literal, builds its reader from `InflectionSilverReader`, defines `main`, `run_real`, `measure_boundary` and `chain_check`; the RAN record's keys equal the whitelist with no date and no 8-digit run; and your test file passes with at least 8 tests and names a mutant test. Base: FAIL (no script).

<expected_criteria>DBI129-1-AC1,DBI129-1-AC2,DBI129-1-AC3</expected_criteria>

**What the chain check is NOT.** It compares the table's chained rows with the product of the silver's own daily factors (a consistency check of the adapter and wrapper on real rows). Comparing with Orion's REPORTED period return needs a vendor call and a window the backfill provides; it is outside this script, and your report says so.

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the adapters, the wrapper, `lib/`, `infra/`, the feed script, the template and every issuer check.
- **No S3 write, no vendor call, no secret.** The script reads the feed's silver and the dimension's two silver tables through the GET-only reader, and writes only to the private directory it is handed and to the record file it is handed. Nothing is run against real data in this order.
- **Client data.** None. Every row in your tests is synthetic; no run of 8 or more digits in anything you write except a `sha256` value or a path. Your tests write only to pytest's temp area.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A rule that seems wrong, or a case the rules do not cover, is a surprise ROW and you keep the rule as written.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W316-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-16.scope-feed-first-real-row-run-script-boundary-measure-and-chain-check.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 15, cell `DB-i-16`.
<owned_cells>DB-i-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI129-1-AC1, DBI129-1-AC2, DBI129-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/IRPT_DASHBD.TO-DB-i-16.scope-feed-first-real-row-run-script-boundary-measure-and-chain-check.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI129-1-AC1,DBI129-1-AC2,DBI129-1-AC3` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the number of tests passed; any case the rules did not cover (as row ids); the line count of the script; and the sentence that the chain check is a consistency check against the silver's own factors. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one new script and its test file in the order's own folder; nothing is wired, scheduled, served or deployed, and nothing is run on real data in this order.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the script's main reads the Orion silver through the round-108 GET-only reader (granted prefixes, the principal rounds 108 to 111 and 126 used); no new principal or grant, no write; it is not run here.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; all three criteria FAIL at base (no script), the checker passed a reference script on all three, and eight single-rule mutants of it (NO_SILVER_YET writing a directory, the read cap ignored, the boundary basis-point factor wrong, the chain check always OK, the 238-day floor dropped, a boto3 import, a date in the record, a write token) each failed the checker before the cut.
</preflight>
