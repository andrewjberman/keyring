# Session Log -- ADVI_INFGRO.009 Method-Y windowed pull + INF_C_02 fix

**Agent:** 0.4.0_DS_ClientPlatform (DS~C lane)
**Date:** 2026-05-18
**TO:** ADVI_INFGRO.009 (dsc-infc02-twr-factor-rebuild-method-y), issued by 2.0.0_SA_COO
**Project:** ADVI_INFGRO
**Ruling:** CTO Method-Y ruling 2026-05-18 (on the INFGRO.008 escalation)

---

## Current State

Phase 0 (probe) + Phase 1 (code) COMPLETE and deployed. Phase 2 NOT yet
materialized -- the 2026-05-18 16:28Z INF chain ran INF_C_02 on the OLD
pre-windowed perf bronze (it synced ~15:32Z, before the 4e64b254 windowed
puller reached code/gold/+code/bronze/ at ~16:18Z). A clean full INF chain
re-run is AUTHORIZED by COO (2026-05-18) and is being coordinated with AE 0.7.0.
AC5 verification + RAVC2 follow that re-run. See Post-chain finding below.

---

## Phase 0 -- PROBE (read-only)

### Step 1 -- bronze/performance summaries block: NOT a usable series

INFGRO.002 (f39550d99) added 6 `summary_*` columns to the bronze schema, but (a)
no live bronze partition carries them (the puller change never reached the
runner), and (b) more fundamentally `summary_performance_pct` is the
inception-to-date ANNUALIZED TWR -- the same defective quantity as `factor`,
not per-period or window returns. Step 1 yields no usable authoritative series.

### Step 2 -- Orion endpoint capability probe: Method Y VIABLE

Thin read-only probe (COO-approved option (a), ~10 calls, 2 clients) of
`GET /api/v1/Portfolio/Clients/{id}/Performance`:

- The endpoint accepts `startDate` / `endDate` params. (`annualize=false`,
  `periodType`, `dateRange` are all IGNORED -- the date RANGE is the only lever.)
- With a date range, `details[]` is a cumulative-growth factor series rebased to
  the window start. Granularity + annualization depend on window length:
  - period <= ~1yr -> DAILY details; `factor` is the TRUE non-annualized period
    return. QTD window (137 daily details) -> +3.39%; 1Y (365 daily) -> +10.51%;
    30d -> +0.69%.
  - period > 1yr -> `factor` ANNUALIZED (3Y -> +7.6%/yr; 6yr -> +5.6%/yr),
    granularity coarsens (3yr = 3-day step, 6yr = weekly).
  - all windows return in 1-2s -- the "5y+ timeout" limit does not bite sub-year.

**The bug, exact:** `pull_inflection_performance_rest.py` called the endpoint
with NO date params -> implicit inception-to-date (>1yr) window -> `factor` came
back ANNUALIZED. INF_C_02 then misread the annualized series as a
cumulative-growth factor. The "no-params" puller design is the upstream origin
of ADVI_INFGRO Finding A + Finding B.

**Proof:** QTD-window `detail[-1].factor` +3.39% matched HH 167's AUA-implied
YTD +3.46% to 0.07pp.

Emission-shape decision: PER-PERIOD daily series (the TO default). INF_C_02's
decomposition needs per-period daily returns intrinsically; INFGRO.007's
`_window_twr_two_axis` chain-link produces all 5 leaderboard windows from it.
CTO architectural flag NOT triggered -- INF_D_00c consumer unchanged. CTO + COO
both confirmed.

---

## Phase 1 -- IMPLEMENTATION

### 1a -- windowed puller (`pull_inflection_performance_rest.py`)

Rewritten to pull abutting sub-year (`CHUNK_DAYS = 300`) `startDate`/`endDate`
windows from inception to today. Each window returns DAILY non-annualized
details; within-window daily returns (`r = factor[i]/factor[i-1] - 1`) are
chain-linked into ONE continuous daily cumulative-growth index from inception
(`factor[inception] = 1.0`, `factor[d] = factor[d-1]*(1+r_d)`). Abutting windows
share their boundary date so the daily series is gap-free. The "no date params /
HARD LIMIT" docstring constraint -- the defect origin -- is removed. The 6
`summary_*` columns (annualized, unconsumed) are dropped.

**Verified** (2-client dry-run smoke + cross-check): stitched YTD matches the
API's own window `summary.performance` to **0.0000pp** (client 18); inception-to
-date growth +71.06% (vs the old annualized-rate factor ending ~1.09); integrity
check -- all clients anchored at factor 1.0, zero non-positive factors.

### 1c -- INF_C_02 `_build_daily_factor_table`

Rewritten: with a continuous daily index the per-day TWR factor is the exact
consecutive ratio `twr_factor_period[d] / twr_factor_period[d-1]` (inception:
1.0). The weekly-Nth-root geometric spread (ADVI_INFGRO.003) is removed -- it
was correct only for a weekly *cumulative* input. Vectorized (groupby-shift),
which also removes a ~668K-row Python loop. INFGRO.007's `_window_twr_two_axis`
is NOT touched.

**Verified:** on the new daily continuous data, `PRODUCT(daily_factor)` over a
window equals the window's cumulative factor ratio exactly (client 18: PROD
1.710626 == expected; YTD PROD 1.057217 == expected).

### Deploy

| Artifact | Commit | S3 | Verify |
|----------|--------|-----|--------|
| pull_inflection_performance_rest.py | 38410e1dd | s3://opal-data-inf/code/manual_api/ | sha256 4e64b254 working-tree == S3 |
| INF_C_02.client_performance.py | 38410e1dd | s3://opal-data-inf/code/gold/ | safe-deploy gate PASS (working-tree == S3) |

Deployed state is a self-consistent matched pair -- corrected INF_C_02 requires
the corrected puller (corrected INF_C_02 on the old annualized bronze would
still be broken). Both deployed, so any INF chain run now produces correct output.

---

## Phase 1b -- backfill

Folded into the Phase 2 chain run: the puller is chain step `INF_API_PULL_PERF`
(`orion-gold-dispatch.sh:196`, `--upload`), so the full INF chain run does the
full-history windowed re-pull itself. No separate local backfill.

---

## Phase 2 -- chain run + AC5 verify (PENDING)

Awaiting the COO/AE-coordinated full INF gold chain run (`mode=full`). It
co-lands INFGRO.007 + BIWNDW.002 + INFGRO.009 in one run. AE runs it after a
hard-gate timeout check (the corrected puller does ~2,500 windowed calls,
~30-40min -- a ~6-8x-longer `INF_API_PULL_PERF` step). Post-run AC5: window TWRs
correct in ABSOLUTE scale + epsilon no longer dominant (PRD section 8.5 a+b).

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `comp-pipescript io` (Step 1, INFGRO.008) | bronze/performance schema | bronze carries only client_id/date/factor; no summaries block deployed -- documented from the f39550d99 commit + live S3 inspection. |
| Orion endpoint capability probe (Step 2) | /Portfolio/Clients/{id}/Performance | startDate/endDate accepted; sub-year window -> daily non-annualized factor. Method Y viable. |
| `comp-pipescript io` (Phase 0 mandate) | INF_C_02.client_performance.py | READS accounts_dimension_latest + client_performance.parquet (append self-read); WRITES gold/timeseries/client_performance.parquet -> INF_C_04, INF_C_06, INF_D_00, INF_D_00b, INF_D_00d, INF_D_04, INF_D_05a. No COLUMN GAPS. I/O surface unchanged by the 1c edit (internal-only change to `_build_daily_factor_table`). |
| `ds-commit-gate.sh` | puller + INF_C_02 | Both PASS (py_compile + AST + ruff py39). |
| `comp-pipescript deployed` | INF_C_02 | N/A -- tool is BD-bucket-scoped; orion deploy verified by direct sha256 (working-tree == S3) + safe-deploy gate PASS. |

---

## Files Modified

| File | Change |
|------|--------|
| data/orion/manual_api/pull_inflection_performance_rest.py | Rewritten to sub-year windowed pulls + continuous daily cumulative-growth-index stitching. Removed the no-date-params HARD LIMIT + the 6 unconsumed annualized summary_* columns. |
| data/orion/scripts/gold/INF_C_02.client_performance.py | `_build_daily_factor_table` rewritten to the exact consecutive-ratio of the continuous daily index; weekly-Nth-root spread removed; vectorized. |

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **AE 0.7.0** | Run ONE full INF gold chain (`mode=full`) post timeout-check -- co-lands .007/.002/.009. Ping on completion (CC COO). |
| **DS~C (self)** | On the ping: AC4 (.007 leaderboard tells) + BIWNDW.002 (1Y/3Y coverage) + AC5 (.009 absolute-scale TWRs + non-dominant epsilon) verification, all off the one post-run leaderboard.json. Three separate RAVC2s. |
| **COO 2.0.0 / CTO 1.0.0** | Three RAVC2s (one per TO). INFGRO.005 partner-facing unblocks when the post-run leaderboard clears PRD section 8.5 (a)+(b). |

---

## Post-chain finding (2026-05-18) -- chain 16:28Z did NOT carry INFGRO.009

Verified the materialized `platinum/firm/leaderboard.json` (generated 16:26Z).
INFGRO.009 did NOT materialize -- the chain ran INF_C_02 on the old perf bronze.
Empirical proof:

- `bronze/performance/2026-05-18.parquet` IS the windowed INFGRO.009 output
  (3.3MB, daily continuous, ~1594 rows/client, factor 0..170, no summary_*
  cols) -- but written **17:49Z**, i.e. 88 minutes AFTER INF_C_02 produced
  `gold/timeseries/client_performance.parquet` at 16:21Z. INF_C_02 could not
  have read it.
- `silver/api_dims/performance/snapshot_date=2026-05-18/data.parquet` = 59KB,
  written 12:51Z -- the old thin annualized shape.
- leaderboard `firm_epsilon_$` YTD = 71.6% of the AUA-growth decomposition --
  EXACTLY the INFGRO.008 pre-fix Finding B number, unchanged.

Root: the chain synced ~15:32Z; the 4e64b254 windowed puller only reached
code/gold/+code/bronze/ at ~16:18Z (the AE SYNC-COLLISION b95fa3a6 clobber had
diverged those prefixes; restored this session). The chain's INF_API_PULL_PERF
ran old code.

Disposition: COO AUTHORIZED one clean full INF chain re-run (2026-05-18).
Everything is staged -- 4e64b254 uniform on all 3 puller prefixes, corrected
INF_C_02 on code/gold/. AC5 (a) absolute-scale TWRs + (b) epsilon-not-dominant
get verified on the re-run leaderboard; RAVC2 follows. TO stays pending.

Compiler tools: `comp-pipescript deployed` is BD-bucket-scoped (N/A for orion);
puller S3 parity verified by direct sha256 -- 4e64b254 uniform on code/gold/,
code/manual_api/, code/bronze/.
| **COO 2.0.0** | Follow-up (not scope-crept): INF_C_03.performance_canonical.py docstring + `period_basis` constant still say "weekly" -- now stale (bronze factor is daily continuous). 2-line opportunistic fix; flagging, not touching, per INFGRO.009's 1a/1b/1c scope. |
