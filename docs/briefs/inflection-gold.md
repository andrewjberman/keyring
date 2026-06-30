# Brief: Inflection — GOLD layer (end-to-end audit) + portal-feed addendum

**Author:** 3.0.0_SA_CVO (Andrew-direct, ADVI_BREAKS unified-flow audit) | **Date:** 2026-06-30
**Scope:** Inflection gold + the gold→portal serving path. Bronze = `inflection-bronze`; Silver = `inflection-silver`.
**Run vehicle:** `inf-gold-layer-runner` EC2 (c6a.4xlarge, i-0ed5afded2ebd4ed4) via `orion-gold-dispatch.sh` (~40 `INF_*` scripts; ~2h envelope).

---

## 1. Gold stage structure (the A/B/C/D DAG)

| Stage | Scripts | Produces |
|---|---|---|
| **A — dimensions** | INF_A_-1 txn_cache → A_00 accounts_dim → A_01 advisor_assignments → A_02 fee_rate_history → A_03 positions_cube → A_04 client_dimension | `gold/dimensions/*`, `gold/positions_cube/` |
| **B — holdings/lots** | **B_00 canonical_holdings** ← positions_mv → B_01 holdings_lots → B_01b classify_new → B_02 canonical_lots → B_03 account_gains | `gold/canonical/holdings_{date}.parquet`, `gold/lots/`, `gold/account_gains/` |
| **C — perf/nna/aua** | C_00 canonical_performance → C_01 canonical_nna → C_01b role_aua_backfill → **C_02 client_performance** → C_03 account_performance → C_04 validate_aua → C_05..C_09 (tax/mix/attribution/fee) | `gold/timeseries/client_performance.parquet`, `gold/canonical/`, ... |
| **D — platinum/served** | **D_00 portal_aggregates**, D_00b/c/d/e/f, D_02* advisor/client detail, D_03 composition, D_04b, **D_04 client_portal_summary**, INF_09, D_05/06/07/08 | `platinum/firm/*`, `platinum/advisors/{id}/*`, `platinum/clients/{id}/*` |

## 2. The TWO chains (the core orchestration finding)

```
 CHAIN_FULL (complete build):   pull→silver→ A_* → INF_B_00 (rebuilds holdings_{date}) → C_* → D_*   → fresh AUA
 CHAIN_INCREMENTAL (NIGHTLY) ★: pull→silver→ [SKIPS A/B/C — "assumes A/B/C gold outputs exist"] → D_*  → STALE AUA
```
The scheduled nightly runs **`CHAIN_INCREMENTAL`** (dispatch usage `--chain incremental`; the pervasive `INFETL.CHAININC` hardening; confirmed live by the missing scheduled 06-29 holdings partition). It refreshes `positions_mv` **silver** but **never runs `INF_B_00`**, so no fresh gold holdings partition is built. `INF_B_00` (holdings) is daily-volatile but the incremental chain treats it as a static "A/B/C output that exists." This is the architectural root of Defect 1.

## 3. The two served defects (consolidated; grounded)

**Defect 1 — STALE-PARTITION / wrong AUA (the +$1.72M; Andrew/COO D-axis).** `INF_D_04.load_latest_holdings()` (L401) picks `keys[-1]` = the MAX-date `gold/canonical/holdings_{date}.parquet`; `build_dashboard:826` `total_aua = holdings['market_value'].sum()`. Because the incremental chain skips B_00, the max partition on a normal night is **T-1**. Grounded numbers: `holdings_06-27` = `holdings_06-28` = **$202,711,894.29** (byte-identical stale); fresh `holdings_06-29` = **$200,987,115.59 = Orion $200.99M exactly** (only built by a DS manual full pull at 21:39Z, after the 14:34Z D-stage). Delta +$1,724,778.70 (+0.86%). **Not a computation error — a partition-selection/ordering defect.** Fix direction: rebuild current-day holdings in the incremental chain, OR select the partition matching `data_as_of` (fail loud if T-1), OR read AUA from fresh `positions_mv` silver. STATUS: open (DS verifying the self-heal track).

**Defect 2 — DUAL-WRITER CLOBBER (the freeze/stub) — FIXED.** `INF_D_00.portal_aggregates` (thin stub: `{firm_id,generated_at,data_as_of,total_aua(from client_performance),client_count}` = 132B) and `INF_D_04.client_portal_summary` (rich 28830B header) both wrote `platinum/firm/header_metrics.json`. Normally D_04 lands last; on 06-29 eve D_00 re-fired off-cadence (18:07/21:29/22:07Z) → thin stub won. **TO-2 (`b0224d8cb`, deployed, CVO-verified)** removed D_00's stub emit (D_04 sole writer) + added a D_04 shape gate (rejects payloads missing `firm_name`/`total{aua}`/`dates`). Served-artifact confirmation pending the next clean scheduled run.

## 4. Gold variance inventory (same disease, one layer deeper)

| Axis | Today | Unified target |
|---|---|---|
| **Output layout** | 15 gold prefixes (`canonical/`, `holdings/`, `lots/`, `account_gains/`, `dimensions/`, `timeseries/`, `views/`, `artifacts/`, `positions_cube/`, `classification/`, `cache/`, ...). `holdings_{date}.parquet` sits under `gold/canonical/` (not `gold/holdings/`, which holds lots-era output) | consistent, predictable gold key scheme |
| **Partition selection** | `load_latest_holdings()` = MAX-date (lexicographic `keys[-1]`), NOT `data_as_of`-matched → silently serves T-1 if today's partition is missing | select by `data_as_of`; fail loud on mismatch |
| **Two chains** | FULL vs INCREMENTAL; nightly = incremental which skips the daily-volatile B_00 | one chain that always rebuilds current-day holdings before D |
| **Served-key writers** | Defect-2 dual-writer now single (D_04) post-TO-2; verify no other D-script writes a shared served key | single-writer per served key + shape gate (TO-2 pattern) |

## 5. Served artifacts (what gold lands in platinum)

- `platinum/firm/*` — header_metrics.json (D_04 rich, sole writer post-TO-2), clients_tab.json (D_00), dashboard.json, timeseries_overview.json, partner_analytics_{monthly,quarterly,annual}.json, cumulative_chart.json, leaderboard, mix, plus windowed variants (`*_1y/_qtd/_ytd/_max`).
- `platinum/advisors/{advisor_key}/*` — book.json, summary, top_holdings, timeseries, composition, mix (D_02*).
- `platinum/clients/{relationship_id}/*` — summary, views, composition, mix_timeseries, concentration (D_04).

---

## ADDENDUM — how gold artifacts feed the portal

```
 inf-gold-layer-runner EC2 (end of gold run)
        │  writes gold/meta/pipeline-complete.json
        ▼  (S3 ObjectCreated)
 inf-portal-publisher λ  ── reads gold parquets + silver dims → generates platinum/firm/*.json
        │  async-invokes at handler START ▼
 inf-portal-advisor-publisher λ ── iterates gold/dimensions/advisor_assignments.parquet
        │                            → platinum/advisors/{advisor_key}/*.json (book.json, ...)
        ▼
 platinum/{firm,advisors,clients}/*.json  (served objects in opal-data-inf)
        │
        ▼  GET /api/scoped/advisor-intelligence/...
 CloudFront EVTSA9VEHNZVH
        ▼  origin-request (λ@Edge)
 shared-advisor-router  ── FIRM_BUCKET_MAP: inflection → opal-data-inf ; S3-direct read of platinum/*
        ▼  origin-response (λ@Edge): Cache-Control 60s + JSON-error envelope
 shared-advisor-router-response
        ▼
 portal/src/api/endpoints/advisor-intelligence.ts → AdvisorIntelligence components
   getHeaderMetrics()       → platinum/firm/header_metrics.json   (firm AUA / NNA / by-architect / radial)
   getTimeseriesOverview()  → platinum/firm/timeseries_overview.json
   getPartnerAnalytics()    → platinum/firm/partner_analytics_{granularity}.json
   getCumulativeChart()     → platinum/firm/cumulative_chart.json
   clients-tab / advisors/{id}/* / clients/{id}/*  → the drill-downs
```

**Addendum flags (for the unified flow):**
1. **Possible third dual-writer.** The gold D-scripts write `platinum/firm/*` directly on the EC2, AND `inf-portal-publisher` "generates all platinum/firm/*.json." Confirm whether they write disjoint files or overlap — a D-script-vs-publisher overlap would be the same single-writer hazard as Defect 2 (RESIDUAL — confirm before the rewrite).
2. **A re-pathed endpoint scar.** `getHeaderMetrics()` was re-pointed (PORTALSWEEP, ADVI_NNAATTR) from a DEAD `artifacts/summary/header_metrics.json` to the LIVE `platinum/firm/header_metrics.json` — evidence the served-key topology has drifted before; the unified flow should pin one canonical served key per metric.
3. The serving path itself (CloudFront + 2 λ@Edge + FIRM_BUCKET_MAP) is shared across all 3 firms and is sound; the firm-specific work is entirely in the per-firm bucket's gold→platinum production.

## Unified-flow implication (capstone)

Across bronze→silver→gold, Inflection shows **one recurring disease at every layer**: a unified path that exists but was forked — bronze (2 pull layers, 3 layouts, duplicate pull scripts), silver (unified converter + standalone forks + duplicate converters + 2 layouts), gold (2 chains, max-date vs as_of partition selection, dual-writers). The single-machine unified flow Andrew described — **EC2 pulls all dims → one datestamped bronze → one converter dispatch → one partitioned silver → one chain that always rebuilds current-day holdings → D single-writers with shape gates → publish** — collapses all of it, and Inflection's small book makes one-machine end-to-end feasible (it already runs there). Both live defects are gold-boundary artifacts of the forking; the unified flow removes the conditions that created them.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| read orion-gold-dispatch.sh (CHAIN_FULL/INCREMENTAL) | the gold DAG + the two-chain finding | PASS |
| read INF_D_00 / INF_D_04 + live S3 holdings partition sums (boto3) | the two defects, grounded to the dollar | PASS (rail-checked) |
| read inf-portal-publisher / advisor-publisher + advisor-intelligence.ts | the gold→portal addendum | PASS |

— 3.0.0_SA_CVO
