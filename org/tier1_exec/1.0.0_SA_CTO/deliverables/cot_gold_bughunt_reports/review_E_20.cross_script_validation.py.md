# REVIEW -- E_20.cross_script_validation.py

- script: `data/cot/scripts/gold/E_20.cross_script_validation.py`
- verdict: **issues-found**
- runs_in_incremental: False
- findings: 6

## Finding 1 -- [medium/other/both]
- **Location:** `compare_counts() line 240 + lines 219/226/233 collected but unused`
- **Mechanism:** compare_counts computes four account_count values (A_00.account_count L202, C_02.account_count L219, C_07.account_count L226, D_00.account_count L233) but the discrepancy loop at L240 filters only `'relationship_count' in k`, so account_count is NEVER cross-checked. Only relationship_count is compared. compare_nna similarly only compares C_01.nna_txn vs C_02.nna_daily, and compare_fee returns [] unconditionally. The docstring (L6) explicitly lists account_count as a metric this script validates.
- **Failure scenario:** COT served state where C_07.account_team reports 480 unique account_ids but A_00.accounts_dimension reports 500 (a real 20-account inconsistency the tool exists to catch). The script logs both counts, but because no account_count comparison is wired in, it prints 'ALL METRICS CONSISTENT (within $1 tolerance)' and returns status=PASS / exit 0. A genuine served inconsistency is silently passed.
- **Proposed fix:** Add an account_count cross-check mirroring the relationship_count block: `acct_sources = {k:v for k,v in results.items() if 'account_count' in k}` and flag `max-min > 0`. Similarly reconsider whether fee comparisons should be strict.

## Finding 2 -- [medium/other/both]
- **Location:** `main() L314+L325-328 -> compare_aua/compare_nna/compare_counts/compare_fee (target_date param never referenced)`
- **Mechanism:** `--date` is parsed into args.date and passed as target_date to every compare_* function, but not one function body ever references target_date. Every metric is always pulled at each source's own 'latest' (either `_latest_partition` lexicographic-last parquet, or `df['date'].max()` on the monolithic timeseries). The advertised `--date YYYY-MM-DD` usage (docstring L14) is a complete no-op.
- **Failure scenario:** An operator investigating a specific historical day runs `python3 E_20.cross_script_validation.py --date 2026-04-05`. The flag is silently ignored; the script compares each source's latest partition (e.g. 2026-04-07) and reports/PASSes on the wrong date, leading the operator to a false conclusion about 2026-04-05 consistency.
- **Proposed fix:** Either implement target_date (filter the monolithic frames to that date and select `<prefix>/<date>.parquet` for partitioned sources) or remove the `--date` argument and its docstring usage so it cannot mislead.

## Finding 3 -- [medium/incremental-full-break/both]
- **Location:** `compare_aua() L101-138 (mixed 'latest' notions across sources)`
- **Mechanism:** AUA is gathered from B_03/C_00 via `_latest_partition` (lexicographically-last dated parquet under a prefix), from C_02/C_03 via `df['date'].max()` on a monolithic timeseries, and from D_00 header_metrics (its own data_as_of). Nothing forces a common as-of date across these sources, and firm AUA legitimately moves with market drift day to day. When producers advance on different cadences (exactly the incremental case: some partitions refresh, some monolithic timeseries do not), AUA is compared across DIFFERENT dates.
- **Failure scenario:** B_03/C_00 have a fresh 2026-04-07 partition while the C_02 client_performance monolith was last rebuilt 2026-04-04. Firm AUA differs by ordinary market drift (easily >> $1 tolerance). _check_discrepancies flags a spurious multi-hundred-million-dollar 'DISCREPANCY', all_discrepancies is non-empty, and main() returns exit 1 / status=FAIL though nothing is actually wrong.
- **Proposed fix:** Resolve a single as-of date up front (e.g. min of all sources' latest available dates, or the requested --date once implemented) and read every source at that exact date; skip/annotate any source that cannot supply it rather than comparing across dates.

## Finding 4 -- [medium/schema-column/both]
- **Location:** `unguarded df['<col>'] access: L106/L115 aua_current, L123/131 total_aua, L202-203 account_id/relationship_id, L210 relationship_id, L219 num_accounts, L226 account_id, L262 fee_bps, L274-275 total_aua/implied_daily_fee`
- **Mechanism:** Reads are guarded (`_read_s3` returns None on any exception and callers null-check), but column access after a SUCCESSFUL read is fully unguarded. COT was cloned from the bd/49F pipeline; several producers/schemas differ (per context, C_00/C_02 producers are not even present in the local tree). If a served COT artifact exists but lacks or renames an expected column, `df['col']` raises KeyError, which is NOT caught (the try/except lives only inside _read_s3), so the compare_* function and main() abort with a traceback.
- **Failure scenario:** COT's gold/timeseries/client_performance.parquet exists (so _read_s3 returns a non-None frame) but does not carry a `num_accounts` column (a bd-specific field). Line 219 `int(latest['num_accounts'].sum())` raises KeyError -> uncaught -> main() exits non-zero with a stack trace and produces no validation report.
- **Proposed fix:** Guard each column access (`if 'num_accounts' in latest.columns:` per the existing daily_inflow pattern) or wrap each source block in try/except that records a skipped-source note, so one schema drift degrades gracefully instead of aborting the whole diagnostic.

## Finding 5 -- [low/empty-null-handling/both]
- **Location:** `compare_aua() L124 and L132: latest["date"].iloc[0].date()`
- **Mechanism:** If a monolithic timeseries parquet is read successfully but has 0 rows, `df['date'].max()` is NaT, `df[df['date']==NaT]` yields an empty frame, `latest['total_aua'].sum()` is a harmless 0.0, but the log line `latest["date"].iloc[0].date()` indexes position 0 of an empty Series -> IndexError, uncaught -> aborts the diagnostic.
- **Failure scenario:** gold/timeseries/client_performance.parquet (or account_performance.parquet) is present but empty (0 rows) — e.g. a first build or an upstream filter that emptied it. _read_s3 returns an empty DataFrame (not None, so the guard passes), and line 124 raises IndexError before any summary is produced.
- **Proposed fix:** After computing `latest`, guard with `if not latest.empty:` before dereferencing `.iloc[0]` (and before adding the source to results), or format the date label from `df['date'].max()` directly with a NaT check.

## Finding 6 -- [low/numeric-sign-units/both]
- **Location:** `compare_nna() L171 (C_02.nna_daily = daily_inflow - daily_outflow) vs L155 (C_01.nna_txn)`
- **Mechanism:** The C_01 vs C_02 daily-NNA cross-check assumes C_02's `daily_outflow` is stored as a POSITIVE magnitude so that net = inflow - outflow. If C_02 stores outflow with a negative sign convention (outflows as negatives), the correct net is inflow + outflow and this subtraction double-counts outflow, producing a large spurious diff. The C_02 producer is not in the local tree, so the sign convention cannot be confirmed here.
- **Failure scenario:** C_02 client_performance stores daily_outflow = -500,000 (negative convention) with daily_inflow = 800,000; true NNA = +300,000. Line 171 computes 800,000 - (-500,000) = 1,300,000, which diverges from C_01.nna_txn (+300,000) by 1,000,000 >> tolerance, flagging a false NNA discrepancy and FAIL.
- **Proposed fix:** Confirm the C_02 daily_outflow sign convention against the served artifact; compute nna_daily consistently with that convention (e.g. `daily_inflow + daily_outflow` if outflow is signed negative), or derive both sides from the same signed net field.
