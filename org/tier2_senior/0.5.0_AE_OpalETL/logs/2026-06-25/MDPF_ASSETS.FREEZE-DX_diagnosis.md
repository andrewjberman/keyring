# MDPF_ASSETS.FREEZE-DX -- Diagnosis (opal_aggregate_aua served freeze)

**Agent:** 0.5.0_AE_OpalETL | **Date:** 2026-06-25 | **TO:** MDPF_ASSETS.FREEZE-DX
**Verify:** 3.0.0_SA_CVO | **Issued by:** 2.0.0_SA_COO (Andrew-direct)
**Status:** DIAGNOSIS COMPLETE -- root grounded, no MDPF-side fix; bd-fees restore routed to BD lane (CVO/0.6.0). Standing by on MDPF re-run/verify.

## Verdict (one line)

`opal_aggregate_aua` is frozen because the MDPF daily-chain **convergence gate correctly DEFERS** on a stale upstream -- **BD silver `fees`** (latest partition 2026-06-18, frozen since the 06-19 BD-49F break). **NOT an MDPF-side code break.** Downstream victim of the bd-fees freeze.

## 1. CHARACTERIZE (served-grounded)

- Served artifact: `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json`
- Last produced: **2026-06-23T14:59:23Z** (~49h, `comp-freshness artifact` = FAIL, default daily thresholds).
- Rollup `as_of` stopped advancing after 06-23 = the **deferred-gate signature**.
- Andrew's "frozen for days" = TRUE in effect: 2 trading days of missed forward updates (06-24, 06-25); the ROOT upstream (bd-fees) has been frozen since 06-19 (6 calendar days).

## 2. LOCALIZE the stuck stage (per-stage live freshness)

| Stage | Role | Latest state | Status |
|---|---|---|---|
| INF spine sentinel | TRIGGER (`pipeline-complete.json`) | 2026-06-25 15:00 (1.2h) | PASS -- firing daily |
| BD silver allocations | GATE input #1 | latest partition **2026-06-24** (written 06-25 09:50) | PASS -- **recovered** (0.6.0 P1) |
| **BD silver fees** | GATE input #2 | latest partition **2026-06-18.parquet** (written 06-19 18:17) | **FAIL -- frozen since 06-19; SOLE blocker** |
| MDPF served (aggregate_aua_timeseries.json) | output | 2026-06-23 14:59 | FAIL (downstream of fees) |

First-frozen stage = **BD silver fees**. Everything else is fresh; the MDPF chain itself never ran-and-failed -- it was never dispatched (gate deferred).

## 3. GROUND THE MECHANISM (Rule 22 -- source + runtime + partition ground-truth)

**SOURCE** -- `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py`:
- `:54-56` `BD_SILVER_PREFIXES = "silver/allocations,silver/fees"` -- **fees is a gate input**.
- `:158-179` `_check_bd_silver` -- for each prefix, latest `{YYYY-MM-DD}.parquet` partition stem vs `expected_last_trading_day`; `fresh = fresh and ok` (**ALL prefixes must pass, AND**).
- `:68` `BD_MAX_LAG_TRADING_DAYS = 2`.
- `:222-236` `if GATE_ENFORCE and not all_fresh: DEFER` (no dispatch). A stale on **either** prefix freezes MDPF.

**RUNTIME** -- CloudWatch `/aws/lambda/mdpf-daily-trigger` gate decisions:
- run_date **06-23**: fees `latest_partition: 2026-06-18, trading_days_behind: 2, fresh: true` -> `all_fresh: true` -> **dispatched** (= the last served output).
- run_date **06-24**: fees `behind: 3, fresh: false` -> `all_fresh: false` -> **DEFER** (first freeze day).
- run_date **06-25**: allocations `behind: 1, fresh: true` (recovered) + **fees `behind: 4, fresh: false`** -> `all_fresh: false` -> **DEFER**. Fees isolated as the sole `all_fresh:false` cause.

**PARTITION GROUND-TRUTH** (`aws s3 ls`):
- `silver/fees/` latest = `2026-06-18.parquet` (06-19 18:17). No 06-19 (Juneteenth/NYSE holiday), no 06-22/23/24.
- `silver/allocations/` latest = `2026-06-24.parquet` (06-25 09:50) -- recovered (with interior gaps 06-22/06-23, but gate keys on max partition only -> passes).

**Resolves the timeline nit** (0.6.0): the 06-23 served mtime is NOT a slipped dispatch. `BD_MAX_LAG=2` legitimately tolerated fees-06-18 for exactly 2 trading days (06-22 = +1, 06-23 = +2; 06-19 holiday excluded), then deferred from 06-24 (behind=3). The ~2-trading-day lag between the fees freeze (06-19) and the MDPF freeze (06-24 first defer) IS the `BD_MAX_LAG=2` window. No GATE toggle, no fees-check gap -- gate sound.

## 4. CROSS-LINK (confirmed)

MDPF is a **downstream victim** of the BD-49F 06-19 freeze, NOT independent -- and NOT fully covered by 0.6.0's P1:
- 0.6.0's DataMining-REST P1 (cookie keepalive + REST runner) restored `silver/allocations` (gate input #1).
- **fees is a SEPARATE feed**: `bd_fees` EC2 (i-0868fc7e7ebec26f2, Playwright scrape box, start-on-demand), `bd-fees-pipeline-trigger` cron(15 22 ? * MON-FRI), COO-flagged EXEMPT. NOT a DataMining REST table (no fees template in `opal-data-bd/code/bronze/templates/`). The P1 did not and could not restore fees.
- bd-fees state (0.6.0 char): trigger FIRES (4 weekday triggers 06-22/23/24/25), scrape-RUN produces ZERO new partitions since 06-19 -> the run is FAILING. Likely same BD-portal-auth root as the DataMining break, but the SCRAPE path (portal login, on Andrew's password/login-automation HOLD), a different producer. **INFERRED** until 0.6.0 grounds the last bd_fees run log.

## Proposed fix (scoped, NOT deployed -- no MDPF-side change)

- **PRIMARY (BD lane -> CVO/0.6.0):** restore the bd-fees feed so `silver/fees` lands a partition <=2 trading days fresh. NO MDPF code change -- the gate is correct. A force re-run would be WRONG (would emit a rollup off stale fees, the exact thing the gate prevents).
- **Caveat:** if the bd-fees scrape is password-hold-blocked (same surface as DataMining), interim options = (a) wait for the password hold to lift, or (b) a REST-fees source via 0.6.0's runner IF DataMining exposes a fees export -- a **CTO arch call**, not this TO.

## Re-run ownership (my lane, grounded)

Source: `mdpf-daily-dispatch.sh` (Stage 3 writes `aggregate_aua/{RUN_DATE}.json`; Stage 4 = full timeseries rebuild) + `build_aggregate_aua_timeseries.py:250-262` (`list_partitions` lists ALL existing per-date partitions; `build` iterates date-sorted -> rebuild reflects only partitions that EXIST).

- **GOING-FORWARD AUTO-RECOVERY = AUTOMATIC, ZERO-TOUCH.** Once `silver/fees` is <=2 trading days fresh, the next daily INF-sentinel ObjectCreated fires the trigger -> gate passes -> chain dispatches -> Stage 3 writes the date partition + Stage 4 rebuilds the timeseries -> served `opal_aggregate_aua` advances to the new latest point. No manual MDPF action, no code change. (Runner EC2 is start-on-demand, started by the Lambda.)
- **GAP-DAY BACKFILL (deferred 06-24/06-25 + any until recovery) = NOT automatic, OPTIONAL + MANUAL.** Those days wrote no per-date partition -> permanent holes in the daily trend until explicitly backfilled (re-invoke trigger with `event.run_date` per missing date). REQUIRES bd-fees to have backfilled its OWN partitions for those dates -- if bd-fees only resumes forward, accurate interior backfill is impossible (rolling forward to stale fees is what the gate prevents). Headline/latest auto-recovers regardless; interior trend-gap backfill is a secondary COO/Andrew decision gated on bd-fees historical backfill.

## Compiler Tools used

- `comp-which` (route the freshness question), `comp-glob` (locate producer + dispatch + trigger), `pipescript mdpf` (estate trace: event-driven convergence gate, served paths, frontend consumers), `comp-freshness artifact` (served + INF sentinel + BD allocations + BD fees per-stage freshness -- the localization), `comp-freshness --list` (registry coverage check -- no MDPF entry).
- Source-read (Read/Grep): `mdpf-daily-trigger/lambda_function.py` (gate mechanism), `mdpf-daily-dispatch.sh` (DAG + re-run behavior), `build_aggregate_aua_timeseries.py` (full-rebuild semantics).
- `aws s3 ls` (partition stems -- rail-checked: comp-freshness gives prefix mtime, not the partition-date stem the gate keys on) + `aws logs` via PowerShell (runtime gate decisions -- rail-checked: per-invocation gate decisions not exposed by any comp-tool; leading-`/` log group needs PowerShell per the MSYS gotcha).
