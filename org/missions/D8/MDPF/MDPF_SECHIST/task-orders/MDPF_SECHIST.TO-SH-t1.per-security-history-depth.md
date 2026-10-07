# TO MDPF_SECHIST.TO-SH-t1 -- round 1 SH-t-1: the ETF daily pull asks each new security for one year of history

<to_id>MDPF_SECHIST.TO-SH-t1</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~1</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `SH-t-1` (`decompositions/MDPF_SECHIST_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-1`. FWD-1: the morning after an Opal ETF first buys a security, an analyst opens it on the Positioning page and reads every return
window a year of history supports (1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y), with nobody having asked for a pull.

**Today, measured.** `integrations/bloomberg/pipeline/etf_daily_pull.py` (runs at site Z under the publisher's Python311, blpapi + boto3) derives its
universe from the newest `s3://opal-data-etfs/silver/holdings/` partition, then requests history for EVERY security over ONE window: the prior
manifest's `history_window_end` + 1 day to the as-of (lines 240-257). A security that joined the universe yesterday therefore gets one day.
CSCO and BX joined about 2026-09-18 and hold nine rows each; every window past WTD reads blank. The rows land in
`s3://opal-data-etfs/bbg/<asof>/history_topup.{csv,parquet}` (`put(hist, "history_topup")`, around line 377) with columns
`date, PX_LAST, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS, security` (`security` = `"<TICKER> US Equity"`, the label from `qmap`).
Positioning gold (`data/etfs/scripts/gold/etf_positioning_gold.py`, `load_history` line 731) reads every `bbg/<date>/history_topup.parquet`
for partition dates in the last 400 days PLUS the frozen per-ticker CSVs `bbg-testpull/tickers/<TICKER>/history.csv` (columns `date,price,return`),
keys rows by the first token of `security`, and does NOT filter a partition's rows by the partition date. `compute_returns` (line 855) needs a
series that STARTS at or before each window's start, so 1Y needs rows from one year before the as-of.

**Build (code and offline tests only; NO S3 write, NO Bloomberg call, NO run of `main()`):**
1. **The plan.** A pure function in `etf_daily_pull.py`, `history_backfill_plan(labels, earliest_held, asof, cap=50)`:
   - `labels`: the universe labels (`"<TICKER> US Equity"`); `earliest_held`: dict ticker -> earliest stored date (absent = nothing stored);
   - a ticker NEEDS depth when it has nothing stored or its earliest stored date is later than `asof - 365 days`;
   - each needing ticker gets the window `start = asof - 372 days` to `end = earliest_held - 1 day` (or `end = asof` when nothing is stored);
   - at most `cap` tickers are planned, oldest-needing first is not required; choose a deterministic order (sorted ticker) and return the rest
     as `capped`, so the next run takes them;
   - returns `{"backfill": {ticker: {"start": iso, "end": iso}}, "capped": [tickers], "needing_count": n}`.
2. **The coverage read.** A function `earliest_held_dates(s3, tickers, asof)` that returns ticker -> earliest stored date, reading:
   - every `bbg/<date>/history_topup.parquet` with a partition date within 400 days of `asof` (read only the `date` and `security`
     columns; key by the first token of `security`, upper-case, exactly as gold does);
   - `bbg-testpull/tickers/<TICKER>/history.csv` for the tickers asked about (one `list_objects_v2` over the prefix to find which exist, then
     read only those; the earliest `date` in the file).
   It must finish from dell1 in under 100 seconds against the live bucket; if it cannot, stop and file a row (see BOUNDS).
3. **The pull.** In `main()`, AFTER the production history and fund-daily requests succeed and BEFORE landing:
   - compute the plan from the derived universe;
   - request each planned ticker's window with the same `RET` fields and the same query identifier the universe uses (`qmap`; query by the
     identifier, label by `"<TICKER> US Equity"`), in groups of 20;
   - append the returned rows to `hist`, so they land in the same `history_topup` artifact (no new S3 address);
   - wrap the whole backfill (plan, coverage read and requests) in its OWN `try/except`: on any failure log
     `WARN: history backfill skipped: <error>` and carry on, so the leg's exit code is whatever the production pull earned (0 or 63), never 62;
   - record in the manifest: `history_backfill` (ticker -> start, end, rows returned), `history_backfill_capped` (list),
     `history_backfill_error` (string or null).
   Do not change `FUNDS`, `EXTRA_SECURITIES`, the production window, the exit-code contract or any existing manifest field.
4. **The read-only entry.** `plan_only()` at module level: it derives the universe exactly as `main()` does (reuse the code; factor the universe
   derivation into a function `derive_universe(s3)` that `main()` also calls, so they cannot drift), reads the coverage, computes the plan for
   `asof = BDay(-1)` as `main()` computes it, prints one line `HISTORY-PLAN <json>`, and returns
   `{"asof", "universe_count", "needing_count", "backfill", "capped", "written": []}`. It imports boto3 and pandas only, never `blp_client`,
   and writes nothing anywhere. `python etf_daily_pull.py` with no argument still runs `main()` unchanged.
5. **Tests** in the NEW file `integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py` (pytest; offline fakes for S3 and for
   `blp_client`; no network), with these exact names:
   - `test_plan_new_security_gets_one_year`: a ticker with nothing stored gets `start = asof - 372`, `end = asof`;
   - `test_plan_covered_security_not_requested`: a ticker whose earliest stored date is `asof - 400` is not planned; one at `asof - 300` is
     planned with `end = asof - 301`;
   - `test_plan_cap_bounds_count`: 60 needing tickers with `cap=50` plan 50 and return 10 as `capped`;
   - `test_backfill_failure_keeps_production_rc`: `main()` run against fakes where the production requests succeed and every backfill request
     raises; the exit code is 0, `history_topup` and the manifest are written, and the manifest's `history_backfill_error` is set.
     Fake `blp_client` by inserting a module object into `sys.modules` before `main()` imports it, and fake boto3's client the same way.
   Run a negative control on the last test: make the backfill block re-raise, show the test fails, restore it, and say so in your report.

### ACCEPTANCE

<criterion id="SH1-t1-AC1" cell_refs="SH-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R1_CHECKS/sh_t1_plan_tests.py</invocation><expect>PLAN-TESTS-OK</expect></criterion>
`SH1-t1-AC1` -- the four named tests pass: the plan's depth, its no-op on covered history, its cap, and the isolation of a failing backfill from the leg's exit code.

<criterion id="SH1-t1-AC2" cell_refs="SH-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R1_CHECKS/sh_t1_live_plan.py</invocation><expect>SEAM-OK</expect></criterion>
`SH1-t1-AC2` -- `plan_only()` against the real bucket (read only, from dell1's AWS profile) plans CSCO and BX each from at least 365 days before the
as-of, plans nothing deeper than 400 days, and writes nothing.

<expected_criteria>SH1-t1-AC1,SH1-t1-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base (2026-10-07): `PLAN-TESTS-BAD rc=4` (no test file), `SEAM-BAD no plan_only()`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No S3 write, no Bloomberg call, no run of `main()` against real services.** `plan_only()` is the only live read, and it reads.
- **SITE Z RUNS THE WORKING TREE**: this file is executed at site Z from its checkout. Your commit is a candidate on your branch; it reaches site
  Z only through the issuer's merge and the site Z owner's deploy. Never copy it anywhere.
- **No new S3 address or resource name** (rows ride `history_topup`). **No alert or monitor**: a WARN log line and a manifest field only.
- **Refusal clause.** If a criterion cannot be met as written (the coverage read cannot finish in 100 s, the live plan does not name CSCO or BX, or
  the isolation cannot be had without changing the exit contract), stop, write the reason in your report and a surprise row (id
  `MDPF_SECHIST-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) in the investigation file below, and do not weaken the check.

<paths>
integrations/bloomberg/pipeline/etf_daily_pull.py
integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP.md</decomp_doc> (round 1, the thread), cell `SH-t-1`.
<owned_cells>SH-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH1-t1-AC1, SH1-t1-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~1/MDPF_SECHIST.TO-SH-t1.per-security-history-depth.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SH1-t1-AC1,SH1-t1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the diff of `etf_daily_pull.py` (plan, coverage read, the isolated block, `derive_universe`, `plan_only`), the test output with the negative
control, the `HISTORY-PLAN` line from the live read (universe, needing, planned, capped, CSCO and BX windows), the coverage read's wall time, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the leg keeps its site Z daily task and schedule.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants nothing; the live read uses dell1's existing read on opal-data-etfs; site Z writes the same keys it writes today.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: LOCAL -- code and offline tests on the worker's branch; the site Z deploy is the issuer's WORLD act at the drain under a ledger entry and a never-widen half (decomposition, "The issuer's acts at the drain").
budget: at most 50 securities x about 260 rows = about 13,000 rows on the first run, under the 150,000-row daily figure in bbg_budget.py; the ledger wiring is enrichment 4 (C-BUDGET).
</preflight>

Source: PRD v0.1 @b4b995dc14 section 2 (THREAD) and S01; brief PART IV.5; decomposition round 1.
