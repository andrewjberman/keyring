# MDLP_DISTFIX — Phase 0 Investigation Findings (DE-confirmed vs LIVE served artifacts)

**Author:** 0.4.0_DE_ClientPlatform (lead investigator, Andrew-named)
**Date:** 2026-06-05
**Phase:** 0 — INVESTIGATION ONLY (no fix shipped; confirm root-causes vs live served artifacts before any tier-owner fix)
**PRD:** `docs/architecture/MDLP_DISTFIX_PRD.md` (1.0.0_SA_CTO, commit `54a980467`)
**Verify discipline:** every conclusion below is confirmed against the **actual served artifact** (S3 body + LastModified), not a partial proxy. No manufactured pipeline runs (NFRA cost-governance C1).

---

## TL;DR — all 3 root-causes CONFIRMED; 2 of 3 are SHARPER/different than the PRD hypothesis

| Issue | PRD hypothesis | DE finding vs served | Δ from PRD |
|---|---|---|---|
| **I1** | "Global" pinned to 49F/SmartX, not a true cross-partner aggregate | **CONFIRMED, exactly.** Global == 49F to the cent | matches |
| **I2** | upstream SmartX June-valuation staleness + funded-period fallback; "generated_at regenerates fresh daily" | **CONFIRMED stale — but the real cause is bigger: the smartx-exporter EC2 pipeline has been STOPPED since June 1 (disabled EventBridge trigger).** Artifacts genuinely 4 days stale; the FE timestamp is HONEST (not a print bug) | **PRD's "regenerates daily" is FALSIFIED**; cause is a dead pipeline, not (only) funded-period fallback |
| **I3** | percentile-on-`vals>0` vs $1K histogram floor asymmetry; producer = `INF_D_07a` / shared helper | **CONFIRMED dust — but producer is `INF_D_04._build_geo_view`, and its percentiles are RAW `quantile()` (not even `vals>0`-filtered).** | **producer is INF_D_04 not INF_D_07a/D_01; asymmetry is worse than hypothesized** |

---

## I1 — "Global Unit" is the SmartX/49F book, NOT a cross-partner aggregate — CONFIRMED

**Served evidence (2026-06-05):**

| View | Artifact (served) | account_count | total_aum | p10 | min |
|---|---|---|---|---|---|
| **Global** | `s3://opal-data-portal-v2/json/portfolios/account-distribution.json` | **6,838** | **$1,379,701,688.62** | 7,252.47 | 176.39 |
| **49 Financial** | `s3://opal-data-portal-v2/json/mdpf/49financial/account-distribution.json` | **6,838** | **$1,379,701,688.62** | 7,252.47 | 176.39 |
| **Inflection** | `s3://opal-data-portal-v2/json/mdpf/inflection/account-distribution.json` | 400 | $96,601,199.67 | 17,669.73 | 1,036.76 |

Global and 49F are **byte-identical** (count, AUM-to-the-cent, every percentile, min). A true cross-partner union would be **≥ 7,238 accounts / ≥ $1.476B** (49F 6,838 + Inflection 400; plus any other partners). Instead Global **== 49F exactly**.

**Producer mechanism (root cause):** `data/smartx/.../compute_account_distribution.py` (and its deployed twin `infra/aws/ec2/smartx-exporter/.../compute_account_distribution.py`) computes **ONE distribution over the entire SmartX parquet** (`smartx_allocations.parquet`). It emits `total` + `by_model` (keyed by AssetClass) — **no partner dimension at all**. SmartX ≈ entirely the 49F model-portfolio book, so the single artifact ≈ 49F's 6,838. The FE `getAccountDistribution()` (no firmId) reads this global artifact for the Global view; the per-firm 49F slice is derived from the same SmartX source → identical. Inflection's 400 come from a **separate orion path** (`getAccountDistributionByFirm('inflection')`, served by `opal-data-inf`) and are **never folded into a "Global" superset**.

The AUA donut differs ($1.81B Global vs $1.69B 49F per screenshot) because it is sourced/scoped from a **separate partner-aware artifact** (aum-metrics/timeseries), while the holdings bell-curve + Total Holdings are the single non-partner-scoped distribution. Matches the PRD symptom exactly.

### >> FORK for I1 (product call → Andrew) <<
- **(A) True aggregate:** make Global a real cross-partner union of the holdings distribution (SmartX-49F ∪ orion-Inflection ∪ others). Requires a new aggregation step that unions per-account AUA across the smartx + orion sources before computing the distribution. Higher effort; needs a cross-bucket producer.
- **(B) Honest relabel:** if "Global" is intended to mean only the SmartX-model book, relabel so it doesn't read as an all-partner superset (e.g. "Model Portfolios (SmartX)" / "49 Financial book").
- DE recommendation to surface: this is genuinely a product-definition call. Evidence above is decisive that today it is **NOT** an all-partner aggregate.

---

## I2 — Distribution + metrics genuinely stale since June 1 — REAL pipeline outage, FE timestamp is HONEST — CONFIRMED (reframed)

**Served freshness evidence (2026-06-05, today = Jun 5):**

| Artifact | `last_updated`/`generated_at` | S3 LastModified | Status |
|---|---|---|---|
| `json/portfolios/account-distribution.json` (Global dist) | generated_at `2026-06-01T20:54` | **Mon 01 Jun 2026 20:54** | STALE 4d |
| `json/mdpf/49financial/account-distribution.json` | generated_at `2026-06-01T20:38` | (June 1) | STALE 4d |
| `json/mdpf/inflection/account-distribution.json` | generated_at `2026-06-01T20:38` | (June 1) | STALE 4d |
| `json/portfolios/aum-metrics.json` (**FE footer `last_updated`**) | `2026-06-01T14:16` | **Mon 01 Jun 2026 14:16** | STALE 4d |
| `json/portfolios/aum-timeseries.json` (AUA/AUM area chart) | — | **Fri 05 Jun 2026 15:03** | **FRESH (today)** |

**Root cause (decisive):** the **`smartx-exporter` EC2 (`i-06ebcb27395eb3f49`) is STOPPED** — StateTransitionReason "User initiated / Client.InstanceInitiatedShutdown" (the pipeline self-shuts-down after export to save cost). The EventBridge trigger that starts it, **`smartx-daily-export-trigger` (`cron(0 14 ? * MON-FRI *)`), is DISABLED** (also `smartx-model-monthly-pull-daily` DISABLED). The instance LaunchTime `2026-06-01T14:00:59` **exactly matches** that 14:00-UTC cron — it last fired Mon June 1, ran `run_smartx_pipeline.py` (step 5/6 = `compute_account_distribution.py --upload` + `compute_per_firm_account_distribution.py --upload`), uploaded, self-shutdown — and has not started since because the rule is disabled.

**Therefore:** `aum-metrics` + all three `account-distribution` artifacts are produced by this dead pipeline → frozen June 1. The FE footer renders `metricsData.last_updated` (`ModelPortfolios.tsx:388/1189/1641`) = `aum-metrics.last_updated` = **June 1** → **"not updated since June 1" is LITERALLY CORRECT and reflects REAL staleness, not a print bug.** The AUA/AUM time-series Andrew sees updating daily is a **different artifact** (`aum-timeseries.json`, fresh today, fed by a separate Lambda/yang path) — exactly the split the PRD predicted.

**PRD correction:** the PRD's framing ("producer correctly falls back to last funded snapshot ≈ June 1, **generated_at regenerates fresh daily**") is **falsified by the served data** — generated_at is frozen at June 1; the producer is NOT running daily. The funded-period fallback (`period=202605`, May) is real in code but is a **secondary/latent** layer — it would make data-as-of lag *even after* a restart if June EndMarketVals are still $0, but it is NOT the cause of today's June-1 symptom.

### >> FORK for I2 (cost/product call → Andrew; cloud-ops fix) <<
- **Why is the trigger disabled?** Likely intentional during the NFRA cost-audit (memory `feedback_no_adhoc_gold_runs_validate_on_scheduled_nightly` — cost-governance is a standing constraint). This needs an explicit ruling, not a silent re-enable.
- **(A) Restore freshness:** AE/cloud-ops re-enable `smartx-daily-export-trigger` (+ confirm the instance start→run→self-shutdown cycle works). Restores daily distribution/metrics. Has the EC2 runtime cost the disable was presumably avoiding.
- **(B) Accept a lower cadence + make staleness visible:** keep the trigger off / on a reduced schedule and fix the **display** so a stale as-of is obvious (show "data as-of {funded period}" distinct from "generated {date}", and/or a staleness badge when generated_at lags > N days). Independent of the cadence decision, this display-disambiguation is worth doing so a future outage is visible rather than silently read as fresh.
- DE note: (A) and (B) are not mutually exclusive — recommend (A) to fix the outage **and** (B) for resilience. The cadence/cost knob is the genuine Andrew call.

---

## I3 — ADVI Inflection "Account Sizes By State" P10 dust — CONFIRMED; producer + asymmetry sharper than PRD

**Served evidence — `s3://opal-data-inf/platinum/firm/partner_analytics_monthly.json` → `views.geo.<period>.distribution.total.percentiles` (LastModified Fri 05 Jun 2026 14:49 — this surface IS fresh):**

| period | p10 | p25 | p50 | p75 | p90 | min |
|---|---|---|---|---|---|---|
| m1 | **$123.87** | 19,798 | 84,180 | 252,067 | 671,537 | **0.00** |
| m2 | **$1,100** | 20,254 | 85,661 | 251,673 | 649,443 | **0.00** |
| m3 | 6,196 | 27,042 | 91,219 | 259,372 | 662,275 | 0.01 |

m1's p25/p50/p75/p90 ($19.8K/$84.2K/$252K/$671K) **exactly match the screenshot** ($19K/$84.1K/$252K/$670K) → this is the right surface. **P10 is the dust outlier** (the screenshot's $8.42 is the live "current" period; the phenomenon is identical — `min` = $0.00 confirms sub-$1K/near-zero accounts in the series).

**Exact producer (CORRECTION to PRD):** not `INF_D_07a` / `D_01` — it is **`data/orion/scripts/gold/INF_D_04.client_portal_summary.py`, `_build_geo_view`** (the "Account Sizes By State" geo view), written to `opal-data-inf/platinum/firm/partner_analytics_{monthly,quarterly,annual}.json`. Lineage mirror: bd **`D_04.client_portal_summary.py`** ↔ orion **`INF_D_04`** (the file comment at `INF_D_04:210` states "Mirrors BD D_04._calculate_distribution_stats exactly").

**The asymmetry (worse than hypothesized):** `_build_geo_view` computes the displayed percentiles as **raw `aua_series.quantile(0.10..0.90)` directly on the merged `aua` column** — `INF_D_04.py:2360-2366` (by_segment) and `:2380-2386` (total). This has **NO `vals>0` filter and NO $1K floor at all** (hence `min=0.00`). Meanwhile the histogram block (`_compute_histogram_block`, `INF_D_04.py:158/186`) **DOES floor at $1K** (`min_val = max(float(vals.min()), 1_000)`). → histogram hides dust in the $1K bin; percentile lands on it.

Note the related (but distinct) `_calc_distribution_stats_adv` (`INF_D_04.py:207`, the ADVI advisor-summary `account_distribution`, mirroring bd `D_01.calculate_distribution_stats` `D_01:572`) at least filters `vals = vals[vals > 0]` (`:214`) — but **still has no $1K floor on its percentiles** (`:245` `vals.quantile(0.10)`) while flooring its histogram (`:225`). Same asymmetry class, in two places.

**Critical fix-scoping point:** the dust P10 on the geo surface comes from the **inline raw quantiles in `_build_geo_view`**, which **bypass `_calc_distribution_stats_adv` entirely**. So fixing only a shared `calculate_distribution_stats` helper would **NOT** fix the "Account Sizes By State" panel unless `_build_geo_view` is **refactored to route its by_segment + total percentiles through that shared helper**.

### Andrew-directed fix (from PRD — for the fix phase, not now):
1. **Threshold = accounts ≥ $1,000** applied to the **percentile input** (matching the histogram floor) — eliminates dust P10.
2. **Single SHARED floored-percentile helper** spanning **49F (bd)** + **Inflection (orion)** — no per-partner duplication. The shared helper must be imported/used by **all** of: bd `D_01.calculate_distribution_stats`, bd `D_04._calculate_distribution_stats`, orion `INF_D_04._calc_distribution_stats_adv`, **and `INF_D_04._build_geo_view`** (route its inline geo quantiles through it). Respect the bd/orion repo split (a shared util both import, or one canonical impl).
3. **Tier discipline (Rule 17):** this dust/materiality filtering is business-logic → **gold** tier (where it already lives), not silver.
4. **Acceptance:** P10 corrects to a sensible ≥$1K funded value (P25/Median/P75/P90 ~unchanged); identical computation path proven on BOTH 49F + Inflection; served-verified on both surfaces; visual smoke gate.

---

## Routing
- DE confirmation complete (this phase). **Tier-owner fixes route AFTER COO decompose + Andrew's I1/I2 fork rulings.** Suggested owners (per PRD): **DS** for the gold producers (I3 shared helper + `_build_geo_view` refactor; I1 aggregate producer if fork→A), **AE/cloud-ops** for I2 (re-enable `smartx-daily-export-trigger` / pipeline cadence), **RD/FE** for I1 relabel (if fork→B) + I2 timestamp-display disambiguation.
- Visual smoke gate (Andrew or /frontend-dev) on corrected surfaces before close.
