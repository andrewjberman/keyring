# TO MDPF_SECHIST.TO-SH-t1 -- round 1 SH-t-1: the ETF daily pull asks each new security for one year of history

<to_id>MDPF_SECHIST.TO-SH-t1</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~1</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
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

## AMENDMENT 1 (2.0.0_SA_COO~H1, 2026-10-07 ~08:0xZ) -- the backfill draws on the one Bloomberg budget ledger (C-BUDGET; CTO half REFUSED @451db20b50)

The order re-opens (`<status>` pending). The first pass drained @099e082db2 (worker commit 5433813cf6; AC1 4 passed, AC2 `SEAM-OK planned=15`).
Read the first pass's code at HEAD: `history_backfill_plan`, `earliest_held_dates`, `plan_only`, and the backfill block in `main()` (it starts after the
fund-daily request and ends at `WARN: history backfill skipped`). Keep all of it; this amendment adds the ledger.

**Why.** `1.0.0_SA_CTO~DELL1` refused the CTO never-widen half for the site Z deploy
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECHIST_SH_T1_SITEZ_DEPLOY_20261007.md`): the PRD's ratified contract C-BUDGET says
"History pulls and backfills draw on the same ledger, under the production reserve; a backfill is paid once per security and yields to production."
`data/etfs/scripts/rivalfunds/bbg_budget.py` is that ledger, on the same site Z terminal. Its lines 3-4: on 2026-10-05 about 175k rows of local backfill
"exhausted the Terminal's daily capacity and blocked the 07:00 ET production pulls." A backfill leg that spends without recording makes `spent(today)` read low
for every other backfill on the box.

**The ledger (read only; never edit it or `bbg_budget.json`).** `bbg_budget.py` exposes `config()` (`bbg_budget.json`: `daily_ceiling_rows` 150000,
`production_reserve_rows` 30000), `spent(day=None)` (rows recorded for the UTC day; absent ledger = 0), `record(mode, rows, batch_id)` (appends one line, never
raises) and `ledger_dir()` (honours the env var `RIVALFUNDS_BBG_BUDGET_DIR`; under pytest a temp dir). Its `check_backfill(plan, today)` takes a
`{date: [funds]}` plan priced per fund-date, which does not fit a per-security plan, so apply THE SAME RULE directly.

**Change (in this order's existing write set; `bbg_budget.py` is read, imported, never edited):**
1. Import the module from `<REPO>/data/etfs/scripts/rivalfunds` (put that directory on `sys.path` inside the backfill block, the way the file already puts
   `integrations/bloomberg/mcp` on it for `blp_client`; `REPO` is the existing constant). An import failure is a failure of the block: branch B.
2. A pure function `history_backfill_rows_estimate(plan)`: the sum over planned tickers of the weekdays (Mon-Fri) from `start` to `end` inclusive.
3. In the backfill block, BEFORE any Bloomberg request: `limit = daily_ceiling_rows - production_reserve_rows` from `bbg_budget.config()`,
   `used = bbg_budget.spent()`; if `used + estimate > limit`, raise into the block's existing `except`, so it logs `WARN: history backfill skipped: budget ...`
   (name the estimate, the rows left and the limit), sets `history_backfill_error`, fetches nothing, records nothing, and the exit code is what production earned.
   An unreadable `bbg_budget.json` refuses the backfill (the opposite of `check_backfill`'s choice for its own collector: here an unbudgeted backfill is the
   hazard, and refusing it costs one day of depth, never a production pull).
4. AFTER the requests: `bbg_budget.record("backfill", <rows returned across all groups>, "etf_history_backfill_<asof>")`, also when some groups failed
   (record what was returned before the failure, then let the block's `except` run). Add `history_backfill_budget` to the manifest:
   `{"estimate", "limit", "spent_before", "recorded"}` (null when the block never reached the check).
5. NEW test, exact name `test_backfill_budget_refusal_and_record`, in `integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py`, with
   `RIVALFUNDS_BBG_BUDGET_DIR` pointed at a pytest `tmp_path`, `main()` against the existing fakes:
   - arm 1, ledger pre-filled to the limit (one `record("backfill", 120000, "prefill")` line): no backfill request reaches the fake Bloomberg, the exit code is 0,
     `history_topup` and the manifest are written, `history_backfill_error` names the budget, and the ledger holds only the prefill line;
   - arm 2, empty ledger: the backfill runs, and the ledger gains exactly one `"mode": "backfill"` line whose `rows` equals the rows the fake returned.
   Negative control: remove the check (keep the record), show arm 1 fails, restore. Say so in your report.
6. Nothing else moves: not the plan rule, the cap, the production window, the exit contract or the existing manifest fields.

**Criteria.** AC1's check now also requires `test_backfill_budget_refusal_and_record` PASSED (`R1_CHECKS/sh_t1_plan_tests.py`; dry-run at HEAD @a984cc37d2:
`PLAN-TESTS-BAD not-passed=test_backfill_budget_refusal_and_record`, FAIL as expected). AC2 is unchanged and must still read `SEAM-OK`.
Gate limb: none graded this modification (LIMB 6 fires on new orders only; the order declares no `<placeholders>`).
