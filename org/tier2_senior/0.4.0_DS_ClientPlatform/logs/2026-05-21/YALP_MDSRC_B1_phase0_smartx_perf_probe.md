# YALP_MDSRC.B1 — Phase 0: SmartX-REST model-performance data-shape probe — 2026-05-21

**Agent:** 0.4.0_DS_ClientPlatform (base lane)
**TO:** YALP_MDSRC.B1.ds-smartx-rest-model-portfolio-performance-pull
**Branch:** CLOUD
**Status:** Phase 0 COMPLETE — verify-first probe done; a material data-shape finding surfaced to COO. Phase 1 HELD (pending the .002 coordination + COO's Phase-1 path ruling on the finding below).

## Phase 0 — what was probed

COO GO (2026-05-21 00:23Z / 00:28Z): run Phase 0 read-only without waiting on the
offline SXPL_RESTIN.002 owner (0.5.0_AE_OpalETL base, NOT REGISTERED). Phase 0
reused the canonical SmartX ROPC-JWT + Secrets Manager auth path via the committed
SXPL_RESTIN.001 harness `data/smartx/scripts/sxpl_restin_probe.py` (`get_credentials`
+ `mint_token` + `http_get`) — no parallel auth stood up. Read-only; 5 portal
models (ST/LTA/INT/LTC/UST), all 4 candidate SmartX model-performance endpoints
probed live against real data.

## Phase 0 — findings (the data-shape surprise, AC1)

| Endpoint | Cadence | Freshness | Verdict |
|---|---|---|---|
| `reportedmodels/{rmid}/historicalperformance` (TO-named) | **monthly** (date-gaps 28-31d, 1st-of-month) | **STALE** — last point 2025-03-01 (~14 months old); only 2-7 points/model | Unusable. `performanceValue` is a per-month return decimal (e.g. 0.0112 = +1.12%), but the series is monthly + stale. |
| `models/{id}/statistics` (TO-named) | live snapshot | **BUGGY** | `returns.today` is IDENTICAL across all 5 models ($13,007,331.76 / 0.978%); `returns.mtd/qtd/ytd` are 0.0 for 4 of 5 models. Cannot source per-model returns in its current state. |
| `enterprises/aum?modelid=` | **daily** | **FRESH** — to 2026-05-19, ~336-425 points/model | The only fresh daily series — but it is `closingEquity`, the model's total book market VALUE across all allocated accounts. It moves with BOTH market performance AND net allocation flows; consecutive ratio is NOT a clean TWR. (`totalAum` field is garbage — $29-134B; ignore. `closingEquity` per-day is the real per-model value.) |
| `performance.smartxadvisory.com/models/performance` | **monthly** | **FRESH** — `monthly_statistics` begin 2024-09-01 / end 2026-05-01 (current month) | The best-quality SmartX model-performance source: `trackedYearsForModels.{id}.months` = per-month return %, fresh through 2026-05; plus benchmark monthly + risk stats (`calculations`). Monthly cadence. |

**The crux — a cadence mismatch.** SmartX's model-PERFORMANCE data is fundamentally
**monthly** (`performance/models/performance` fresh-monthly; `historicalperformance`
stale-monthly). The only DAILY SmartX series is `enterprises/aum.closingEquity` — a
flow-contaminated VALUE series, not a return series.

But the portal model-portfolio performance surfaces B1 must feed are **daily /
sub-monthly**:
- `model_portfolio_timeseries.json` — a DAILY per-(date, model) `model_return` series.
- `model_portfolio_benchmarks.json` — `model` field per period including **1D** and
  **WTD** (sub-monthly).

The CURRENT source (yang `model.pkl`) IS daily. So a 1:1 move of the model-return
surfaces to SmartX would DOWNGRADE cadence from daily to monthly.

This is a genuine verify-first catch — the TO's two named endpoints
(`historicalperformance` + `statistics`) are respectively stale and buggy; the
viable SmartX perf source is `performance/models/performance` and it is monthly.

## Phase 0 — implication for B1 scope (surfaced to COO; not decided unilaterally)

Three paths, for COO/CTO to rule on (per the TO "surface any data-shape surprise
before building"):
- **A — Hybrid by cadence.** SmartX `performance/models/performance` (fresh monthly)
  sources the monthly+ periods of `model_portfolio_benchmarks.json` (1M/MTD/QTD/1Q/
  YTD/1Y/Since-Inception); `model.pkl` retained for the daily `model_portfolio_timeseries.json`
  + the 1D/WTD periods. Consistent with the TO already RETAINING model.pkl as the
  design view.
- **B — Derive daily from `enterprises/aum`.** Flow-adjust `closingEquity` to a daily
  model TWR — needs the allocation-flow data; daily flow-noise may swamp daily returns.
  Heavier; correctness risk.
- **C — B1 re-scope.** The SmartX move is a monthly-granularity move by nature; the
  portal daily surface stays model.pkl. B1 delivers SmartX-sourced monthly model
  performance.

WS-3 Q4 reconciliation (intellectual honesty): the WS-3 audit recommended SmartX
REST as the canonical model-performance source on endpoint PRESENCE (SXPL_RESTIN.001's
availability matrix). The verify-first probe refines that: SmartX's authoritative
model performance is **monthly-cadence**. SmartX remains the right *authoritative*
source (it is the managed-account system of record; YCharts is still a builder tool)
— but it cannot 1:1 source the portal's *daily* model-return surface. The Q4
direction holds; the cadence reality is new and material.

## Files

No code/artifact written in Phase 0 (read-only probe). Phase-0 evidence is this log
+ the live probe transcript.

## Compiler Tools

Phase-1 mandate (`comp-pipescript io` / `comp-iam service`) is a before-the-build
gate — not yet run; Phase 1 is HELD. Phase 0 is a read-only external-API probe — no
comp-* applies (SmartX REST is an external system; PRD §5 documented-none).

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | Phase-0 finding surfaced (SmartX model-perf is monthly-cadence; the daily portal surface cannot be 1:1 SmartX-sourced). Need a Phase-1 path ruling — A (hybrid by cadence) / B (derive daily from enterprises/aum) / C (re-scope to monthly). Also still need the .002 coordination cleared (0.5.0_AE_OpalETL offline). |
| **DS Base (self)** | On COO's Phase-1 ruling + the .002 coordination: run the Phase-1 compiler mandate + build the SmartX pull to the ruled scope. |
