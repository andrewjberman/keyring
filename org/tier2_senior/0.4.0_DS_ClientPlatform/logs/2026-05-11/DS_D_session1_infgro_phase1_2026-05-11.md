# DS~D 2026-05-11 session 1 — ADVI_INFGRO Phase 1 (probe + recommendation)

## TL;DR

GO from COO (Andrew direct) for `ADVI_INFGRO` TWR research. Phase 1 = investigation only (no S3 writes, chain on HOLD per Andrew). Probed `GET /api/v1/Portfolio/Accounts/{accountId}/Performance`, confirmed shape, audited existing Inflection performance assets. Authored 1-page recommendation at `docs/briefs/data-scientist-infgro-phase1-recommendation.md` proposing a 3-TO chain (silver passthrough → gold integration → portal toggle) that uses Orion's exposed weekly TWR factor directly, skipping the BD-style 8-TO canonical_performance decomposition. RAVC4 to COO pending Andrew GO for Phase 2.

## Startup

| Step | Result |
|------|--------|
| `register_agent ~D` | PID 23200, broker connected |
| `check_inbox ~D` (broker + filesystem) | Empty → then URGENT GO from COO landed mid-session |
| `inbox-watch` | Tracked, run_in_background (PID via task ID b9sjfy64u live; prior b4dmt899o exited on COO GO delivery) |
| `.comp-graph/.agent_context` | `SERIAL=0.4.0_DS_ClientPlatform~D`, `TO_ID=ADVI_INFGRO.PHASE1` |
| Owned-paths hook | Already wired (idempotent) |

## Phase 1 — Endpoint Probe Result

Hand-picked account: `account_id=65`, household 448, advisor Peter Lee.

| Field | Value |
|---|---|
| HTTP | 200 OK |
| Wall | 2.072s |
| Body | 22,373 bytes JSON |
| `details` | 242 weekly factor points `{pkGroup, calcGrossOfFees, asOfDate, factor}`, 2021-10-01 → 2026-05-11 |
| `summaries` | **1 entry only** — `dateRangeName="period"` (inception-to-date), `performance=6.49%` annualized, `daysInPeriod=1681` |
| Other top-level | `pkGroup, fkParentGroup, fkBucket, fkEntity, grouping, fkGroupEntity, name, inceptionDate, calcFirstDayPerformance, calcGrossOfFees, includeAccruedInt, portfolios, benchmarks, assetGroupAssignments, statistics` |

**Important: corrects COO's hypothesis.** Endpoint does NOT return summaries pre-bucketed by QTD/YTD/1Y/3Y/5Y/inception. It returns ONE inception-to-date `period` summary + weekly `details` factors. Window-specific TWR (QTD/YTD/MAX) must be computed locally as `(factor_end / factor_start) - 1`. That's a one-line aggregation — same compute pattern Orion uses internally.

## Existing Inflection Performance Inventory

| Asset | Status | Note |
|---|---|---|
| `bronze/performance/2026-05-03.parquet` | Pulled but idle (no silver) | 305 clients × ~310 weeks = 94,057 rows, 2020-05-26 → 2026-05-02. Producer: `pull_inflection_performance_rest.py` (REST, client-grain). Persists `details` only, drops `summaries`. |
| `silver/api_dims/performance/snapshot_date=*` | Live, Rolling 3-Year only | 858 accounts; 528/858 (62%) have `twr_value`. Producer: `pull_inflection_performance_dim.py` (Envision ExcelReports, account-grain). Already wired to INF_D_00c / INF_D_02 / INF_D_04 as a Rolling 3-Year cross-check but never as the leaderboard GRO source. |
| `gold/canonical/canonical_performance_{date}.parquet` | Live | Daily account-level `growth = aua_change - net_nna` — dollar-domain, NOT a return-rate factor. Doesn't try to be TWR (docstring explicitly says no price_return decomposition). |

## Why the GRO Column is Wrong Today

Portal renders `entry.aua_growth_pct` at `AdvisorsTab.tsx:1024`. INF_D_00c.portal_leaderboard.py:406-449 computes it as `(total_aua / period_start_aua - 1.0) * 100`. That's AUA-delta %, contaminated by NNA inflows / outflows / re-titling. An advisor who took in $20M of net new assets sees an inflated GRO without any portfolio appreciation.

## Recommendation (full doc: `docs/briefs/data-scientist-infgro-phase1-recommendation.md`)

3-TO chain:

1. **`ADVI_INFGRO.SILVER`** — Promote `bronze/performance/` → `silver/performance/client_weekly_twr/snapshot_date=*` via new `build_client_weekly_twr.py` invoked by `convert_orion_api_to_silver.py`. Light transform only.
2. **`ADVI_INFGRO.GOLD`** — In `INF_D_00c.portal_leaderboard.py`, compute AUA-weighted per-advisor TWR for QTD/YTD/MAX from weekly factors. Emit new field `twr_pct` (or `gro_pct`) alongside existing `aua_growth_pct`. Coverage gate at 80% (mirrors ADVI_INFTGT.TO-1b three-guard).
3. **`ADVI_INFGRO.PORTAL`** — Inflection-only flag-gated swap on `AdvisorsTab.tsx`: when `firm_id === "inflection"`, render `entry.twr_pct` instead of `entry.aua_growth_pct`. 49F's BD-side leaderboard unchanged.

Resolutions: TWR (not MWR — Orion exposes only TWR factors), QTD/YTD/MAX (mirror leaderboard's `available_windows`), AUA-weighted (industry-default for composites, GIPS-aligned), client-grain primary with account-grain endpoint validated as Phase 2.5 enhancement for D_02 drill-down.

## What This Avoids

The BD-side decomposition pattern (`C_00.canonical_performance.py`): price_return + realized_gl per FIFO closing lot + income decomposition — 8+ TOs of reconstruction work. Orion exposes TWR directly; we use it. Andrew's instinct on this is right.

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io INF_C_00` | Group I order 220. READS accounts_dimension. WRITES (none detected — actual writes go to gold/canonical/canonical_performance_{date}.parquet but use dynamic key formatting that escapes the static analyzer). |
| `comp-pipescript io INF_C_02` | Group I order 250. WRITES gold/timeseries/client_performance.parquet → INF_C_04, INF_C_06, INF_D_00, INF_D_00b, INF_D_00d, INF_D_04. |
| `comp-pipescript io INF_C_03` | Group I order 260. WRITES gold/timeseries/account_performance.parquet → INF_C_01b, INF_C_07. |
| `comp-pipescript io INF_D_00c` | **Tool can't resolve INF_D_00c despite suggesting it in the "Did you mean" list.** Tracked as a `comp-pipescript` name-resolution gap. Not blocking — read INF_D_00c.portal_leaderboard.py directly to identify the GRO source (line 406-449, field `aua_growth_pct`). |
| `comp-platinum reverse leaderboard` | Found BD-side producer (D_04). Inflection's parallel leaderboard.json producer (INF_D_00c → s3://opal-data-inf/platinum/firm/leaderboard.json) not indexed in comp-graph yet. Read script + leaderboard JSON directly. |

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/data-scientist-infgro-phase1-recommendation.md` | NEW — Phase 1 recommendation (1-page brief) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_D_session1_infgro_phase1_2026-05-11.md` | NEW — this log |
| `.runtmp/infgro_probe_account_perf.py` | NEW (transient) — Phase 1 probe script |
| `.runtmp/infgro_probe_account_perf.json` | NEW (transient) — full probe payload |
| `.runtmp/infgro_bronze_perf.parquet` | NEW (transient) — bronze sample |
| `.runtmp/infgro_silver_perf.parquet` | NEW (transient) — silver sample |
| `.runtmp/infgro_inflection_leaderboard.json` | NEW (transient) — leaderboard sample |

## Next Steps

1. **[COO]** RAVC4 with recommendation + 3-TO chain proposal. Awaits Andrew GO for Phase 2.
2. **[Self]** Hold for Andrew GO on Phase 2. Watchdog mode in the meantime.
3. **[Phase 2 — when GO'd]** Author `ADVI_INFGRO.SILVER.ds-build-client-weekly-twr.md` task order (mechanically safe to land — silver-only, no chain rerun needed). Gold + portal TOs gated on DS~B's AUA-error all-clear.

## Open Questions Surfaced for Andrew

1. Window basis: QTD / YTD / MAX (recommended) or add Rolling 1Y / 3Y / 5Y?
2. Coverage threshold: 80% (mirrors ADVI_INFTGT.TO-1b three-guard)?
3. Net-of-fees confirmation (recommended — matches silver/api_dims/performance's Rolling 3-Year semantics).
4. Phase 2.5 account-grain puller: ship now or defer until D_02 drill-down need surfaces?
