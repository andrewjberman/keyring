# DS~D 2026-05-11 session 2 — ADVI_INFGRO Phase 1.5 deep endpoint probe

## TL;DR

Andrew direct override (via COO 2026-05-11T210255Z): deep endpoint exploration on `/Accounts/{id}/Performance` to confirm whether Orion exposes pre-bucketed period summaries before he goes to HAR capture. Stage −1 txn audit (CTO-routed) was rerouted to DS~C. Ran a 46-probe matrix + 11-probe window confirmation. **PARTIAL-FOUND:** `startDate` + `endDate` query parameters ARE accepted and Orion returns window-specific annualized TWR per call. **Andrew can skip the HAR capture.** RAVC4 sent at 21:10:08Z.

## Pivot

| Time | Event |
|------|-------|
| 21:04:07Z | RAVC2 ACK'd CTO Stage −1 audit; pulled 2 sample silver/transactions partitions, ID'd type cols (`activity_category` + `type_desc`) |
| 21:05:30Z | COO dual-dispatch reroute: deep endpoint probe = priority 1 (Andrew live); Stage −1 → DS~C |
| 21:05:30Z | RAVC2 ACK'd reroute; pivoted in same turn |
| 21:10:08Z | RAVC4 — PARTIAL-FOUND |

Total Phase 1.5 wall: ~5 min from pivot to RAVC4.

## Probe matrix — 46 probes total

| Section | 200 | 4xx | Note |
|--------:|----:|----:|-----|
| **A. Query params on `/Accounts/{id}/Performance`** | 17 | 1 (405 HEAD) | All query params silently ignored EXCEPT `startDate`+`endDate` (and `asOfDate` doesn't filter when alone) |
| **B. Sibling paths under `/Accounts/{id}/*`** | 1 | 12 | Only `/Accounts/{id}` root (account metadata). `PerformanceDetail`, `PerformanceSummary`, `PerformanceSummaries`, `Returns`, `Performance/{QTD,YTD,Periods,Summaries,Details,Index}`, `Statistics`, `TWR` — ALL 404 HTML |
| **C. Client-grain comparison** | 3 | 3 | Same shape — `summaries=1 [period]`. No asymmetry. |
| **D. Schema discovery** | 0 | 8 | `swagger.json`, `openapi.json`, `schema`, `/api/v1`, `/api/v1/help`, `/swagger`, `/openapi.json`, `/swagger/index.html` — ALL 404 |

Full matrix: `.runtmp/infgro_deep_probe/matrix.json`.

## Window confirmation — empirical TWR per window (account 65)

| Window | startDate | endDate | summaries[0].performance | days | details cadence |
|--------|-----------|---------|----------------|------|------|
| MAX (no params) | (none) | (none) | **6.4910%** | 1681 | 242 weekly |
| YTD | 2026-01-01 | 2026-05-11 | **2.5050%** | 129 | 131 **daily** |
| QTD | 2026-04-01 | 2026-05-11 | **6.5786%** | 39 | 41 daily |
| 1Y | 2025-05-11 | 2026-05-11 | **15.7608%** | 364 | 366 daily |
| 3Y | 2023-05-11 | 2026-05-11 | **11.8727%** | 1095 | 158 weekly |
| 5Y (pre-inception start) | 2021-05-11 | 2026-05-11 | 6.4910% | 1681 | 242 weekly | bounds to inception |
| inception_to_2024 | 2020-01-01 | 2024-12-31 | 4.8405% | 1187 | 171 weekly |
| asOfDate-only | (none, asOfDate=2026-04-01) | — | 6.4910% | 1681 | 242 weekly | `asOfDate` alone is IGNORED |

Details cadence adapts: short windows return daily; long windows return weekly. Both are valid TWR factor series. `annualize=true` is default — YTD's 2.50% appears already annualized over 129 days. `annualize=false` not yet probed (flagged for Andrew).

Per-call wall: ~1.5s. 858 accounts × 4 windows = 3,432 calls at ~50 RPS (well under empirical 300 RPS ceiling) ≈ 70s total.

## Architectural implication for Phase 2

Phase 1's 3-TO chain stands. The SILVER builder has two implementation options:

| Option | Calls per account | Local compute | Tradeoff |
|--------|------------------:|--------------|---------|
| **ALPHA (one-call)** | 1 (no params) | window TWR computed locally as `factor_end / factor_start − 1` | 4x fewer API calls; full weekly history available for time-series rendering. Trust the math vs Orion's. |
| **BETA (per-window)** | 4 (QTD/YTD/MAX + 1Y if added) | none — read Orion `summaries[0].performance` directly | 4x more API calls; zero risk of local-math divergence from Orion's canonical TWR. |

Recommendation: **ALPHA primary, BETA as one cross-validation call at firm-grain** (or against `silver/api_dims/performance` Rolling-3Y twr_value). Best of both. The Phase 1 brief 3-TO chain unchanged in shape; SILVER builder now has account-grain weekly TWR as an additional input option (client-grain remains primary because puller is already running).

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| N/A — pure REST endpoint exploration; no source-script edits | — | — |

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_D_session2_infgro_phase1_5_deep_probe_2026-05-11.md` | NEW — this log |
| `.runtmp/infgro_deep_probe.py` | NEW (transient) — 46-probe matrix script |
| `.runtmp/infgro_window_confirm.py` | NEW (transient) — 11-probe window confirmation |
| `.runtmp/infgro_deep_probe/matrix.json` | NEW (transient) — full 46-probe matrix |
| `.runtmp/infgro_deep_probe/window_*.json` | NEW (transient) — 8 windowed payloads |
| `.runtmp/infgro_txn_sample1.parquet`, `infgro_txn_sample2.parquet` | NEW (transient) — Stage −1 samples (left for DS~C reuse) |

## Next Steps

1. **[COO]** RAVC4 sent — PARTIAL-FOUND result. Andrew can skip HAR capture.
2. **[Self]** STANDBY per COO direction — Phase 2 GO gated on Andrew's 4 questions + DS~C Stage −1 audit + AUA-error all-clear.
3. **[Self optional]** If Andrew wants `annualize=false` confirmation, run a one-line probe (~30s).
4. **[Phase 2 — when GO'd]** SILVER builder now has the choice of ALPHA / BETA / hybrid implementation. Andrew + CTO PRD §3 will pick.
