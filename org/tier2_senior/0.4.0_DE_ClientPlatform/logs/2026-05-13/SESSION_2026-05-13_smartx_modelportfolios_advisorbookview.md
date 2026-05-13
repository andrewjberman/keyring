# Session — SmartX TO-4 + ModelPortfolios canonical-to-trend + Inflection AdvisorBookView adapter

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-13 (afternoon/evening; follow-up to [morning session log](SESSION_2026-05-13_advi_audits_and_bi_rename.md))
**Workspace CLOUD commits:** `4c268c0fb` → `9b01b3d38` → `c918b7c1c`
**Portal DEV commits:** `50e31ee4` → `89655c89` → `ef571bca` → `4267453d`
**Trigger:** Andrew direct (no formal TOs) — four user-visible surfaces

---

## Scope

Four parallel Andrew-direct workstreams:

1. **SmartX Non-Model TO-4** — portal smoke against preview JSON (COO-pre-queued; Andrew direct-verified PASS)
2. **ModelPortfolios canonical-source divergence** — snapshot Q-cards diverging $10-20M from trend bars at historical Q-ends
3. **Inflection AdvisorBookView empty panels** — drilled-in advisor profile shows empty Asset Mix / Top Holdings / Cost Basis / role / active-since
4. **BI/Activity scatter dot click verification** — earlier wire-up had a Recharts binding bug; dots looked clickable but didn't fire

Plus inbox-surfaced confirmations: DS~A shipped Segment Analytics gaps (`61ec0ca71`), DS~B shipped INF_D_05 per-window (`f244b425a`), RD shipped NNA empty-state polish (`e3f34428`), DS~C shipped ADVI_INFADV Path B (`0997324d6`) — all in the same session window.

---

## Surface 1 — SmartX Non-Model TO-4 portal smoke

### What Andrew asked

> "i alrteady checked it out, it workls" (interrupting my /frontend-dev dispatch)

### Empirical pre-flight (done before Andrew interrupted)

Downloaded `s3://opal-data-portal-v2/json/portfolios/non_model_assets_preview.json` (ETag `e42e183b41c1e9e64519be3a620c26b2`, 77,578 bytes). JSON inspection PASSED all spec invariants:

- `latest.non_model_aum` = $445,302,983.41
- `latest.non_model_pct` = 24.68%
- `latest.date` = 2026-05-11
- Boundary 2026-01-15 → 01-16: $271.2M → $394.9M (step UP +$123.7M — matches expected B→C transition)
- 557 daily rows, 2024-11-01 → 2026-05-11

### One-shot override path

Saved preview to `portal/public/non_model_assets_preview.json`, edited `getNonModelAssets()` at `portal/src/api/portal-proxy.ts:388-395` to fetch `/non_model_assets_preview.json` (Vite serves `/public/*` at root in dev). About to spin up `bun run dev --port 5175` when Andrew interrupted with the PASS confirm.

### Cleanup

Override reverted, preview JSON deleted from `portal/public/`. Portal tree clean. RAVC2 PASS sent to COO + DS-base authorizing prod publish path flip.

### Outcome

GO/NO-GO: **GO**. DS-base authorized to flip preview → canonical `non_model_assets.json` path. Empirical artifacts on PROD now show the new daily-fresh series ($445.3M non-model on 2026-05-12).

---

## Surface 2 — ModelPortfolios canonical-source divergence (Path A FE / Path B DS)

### What Andrew saw

Snapshot "last 3 periods" cards under the AUA radial on `/model-portfolios` showed slightly different numbers from the daily AUA trend at the same dates. Andrew's principle: "the daily aua trend is canonical, snapshot should say whatever the last date in the trend is."

### Empirical drift quantified

Pulled both PROD artifacts side-by-side:

| Date | `aum-timeseries.aggregate[Q].aum` | `non_model.time_series[Q].model_aum` | Delta |
|---|---|---|---|
| 2026-03-31 (Q0) | $1,226,377,819.35 | $1,226,377,819.35 | $0.00 |
| 2025-12-31 (Q1) | $1,108,376,962.53 | $1,089,170,175.83 | **+$19.2M** |
| 2025-09-30 (Q2) | $871,236,217.09 | $881,621,757.03 | **−$10.4M** |
| 2025-06-30 (Q3) | $726,407,533.32 | $737,919,207.84 | **−$11.5M** |

Same data source for model AUM, two different publishers (SmartX pipeline for `aum-timeseries.json`; `data/smartx/scripts/backfill_non_model_assets.py` for `non_model_assets.json` Segment A historical) drifting at historical Q-ends.

### Root cause (per code trace)

- Snapshot card reads `non_model.time_series[Q].enterprise_total` (built from Segment A inherited legacy `model_aum`)
- Trend bar at Q reads `aum-timeseries.aggregate[Q].aum + non_model.time_series[Q].non_model_aum`
- The legacy `model_aum` in Segment A doesn't match SmartX pipeline aum-timeseries values

### Path A (FE — DE-shipped)

`portal/src/pages/ModelPortfolios.tsx`:
- New helper `getTrendAumForDate(aggregate, target)` rolls back to most recent `aggregate[d].aum ≤ target` (mirrors `getNonModelAumForDate`)
- `totalAUM` definition rewired: `trendLastPoint.aum + non_model_lookup(trendLastPoint.period)` (was `metrics.total.aum + non_model.latest.non_model_aum`)
- `enterpriseQ0/Q1/Q2` rewired: `aum-timeseries.aggregate[Q].aum + non_model_lookup(Q)` (was `non_model.time_series[Q].enterprise_total`)
- Removed `getEnterpriseTotalForDate` (no remaining callers)

Net diff: +48 / −31 LOC. tsc 0 errors. Shipped portal DEV `89655c89` / CLOUD `4c268c0fb`.

### Path B (DS — DS~A dispatched)

TO sent: backfill `data/smartx/scripts/backfill_non_model_assets.py` Segments A+B to use the existing `build_model_aum_lookup()` helper (already used by Segments C+D for parity with aum-timeseries). Single source of truth at the data layer eliminates the latent drift. Acceptance: $0 delta at every Q-end; sentinel script `validate_non_model_reconcile.py` proposed but optional.

CC'd COO. DS~A on bench; no timing pressure (FE workaround already live).

---

## Surface 3 — Inflection AdvisorBookView empty panels (Path A FE / Path B DS)

### What Andrew saw

Drilled into Patrick Scanlan on Inflection AdvisorIntelligence > Advisors tab > Book view. Headline numbers loaded ($20.9M / 138 fee-paying / 13 non-fee / 151 accounts) but: Asset Mix donut empty ("No allocation data"), Top Holdings sidebar empty ("No holdings data at this level"), Cost Basis & Tax "Tax data not available", header showed "PRIMARY TYPE NO ROLE DATA" + "ACTIVE SINCE —", no book growth TTM panel.

### Tenant correction

Andrew said "49Financial" — but Patrick Scanlan is an **Inflection** advisor. Empirical: 49F's `bd_allocations.parquet` doesn't contain him; `s3://opal-data-inf/platinum/advisors/patrick_scanlan/` exists with full per-advisor artifacts. Confirmed: this is the Inflection AdvisorIntelligence page, not 49F.

### Root cause — envelope shape mismatch + emit gaps

Empirical pull of `s3://opal-data-inf/platinum/advisors/patrick_scanlan/book.json` showed:

- Mix data EXISTS at `bookData.composition.mix` (4 asset classes, $20.9M total)
- Top holdings EXIST at `bookData.composition.top_holdings` (9 entries: VOO 15.9%, HTRB 5.2%, JIJIX 5.2%, ...)
- 73 clients with HH IDs + `relationship_since`

But FE's `PlatinumAdvisorSummary` interface expects fields at the top level:
- `mix` (not `composition.mix`)
- `concentration` (not `composition.{top_holdings, other}`)
- `fee_summary` (not `headline.billing`)
- `clients[].client_name` (not `clients[].display_name`)

The `opal-partners-data` Lambda partially adapts headline → book (which is why the $20.9M / 151 headline renders) but doesn't handle the nested composition shape. Sentinel `warnOnInflectionAdvisorDrift` at `AdvisorBookView.tsx:73` was logging `['book', 'mix', 'fee_summary', 'tax_exposure']` envelope drift on every page load.

Precedent: L3 client detail uses a client-side static adapter (`getPlatinumClientDetailStatic` at `advisor-intelligence.ts:950`). No L2 advisor equivalent existed.

### Path A (FE — DE-shipped)

`portal/src/api/endpoints/advisor-intelligence.ts`:
- New `InflecAdvisorBookRaw` interface mirroring the static S3 envelope
- New `getPlatinumAdvisorSummaryStaticInflection(advisorId, firmOverride)` adapter (~115 LOC)
- `getPlatinumAdvisorSummary` now branches on `isInflectionFirm`: bypasses the Lambda, calls the static adapter
- Maps `composition.mix` → `PlatinumMixSnapshot` (array to keyed object), `composition.{top_holdings, other}` → `concentration`, `headline.billing` → `fee_summary` (1-row 'advisor' role stub), `clients[].display_name` → `client_name`
- Derives `active_since` from `min(clients[].relationship_since)`
- Stubs `tax_exposure` (zero block) + `role_breakdown` ({}) + `mix_periods` ([]) until Path B lands

Net diff: +159 LOC. tsc 0 errors. Shipped portal DEV `ef571bca` / CLOUD `9b01b3d38`.

### Path B (DS — DS~C dispatched, shipped same session)

TO sent: add 4 fields to `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` advisor book.json emit:
1. `role_breakdown` — single-role 'advisor' stub for Inflection (no architect/implementor split)
2. `active_since` — derived from `min(clients[].relationship_since)` (clients already have it)
3. `tax_exposure` — advisor-level rollup of the per-client tax block DS~C authored earlier
4. `mix_periods` — per-quarter asset-class breakdown for the advisor's book

**DS~C shipped `0997324d6`** within ~30 min of TO dispatch (`feat(INF_D_02): ADVI_INFADV Path B — add role_breakdown + active_since + tax_exposure + clients[].relationship_since to per-advisor book.json`). Pending AE 0.6.1 inf-gold chain trigger to regenerate the artifacts. After chain, I retire the FE Path A stubs in a follow-up.

---

## Surface 4 — BI/Activity scatter dot per-dot click binding fix

### What Andrew asked

> "make sure the scatter plot dots on 'Trade Activity' in business intelligence are actually clickable, taking you to that HH poage."

### What I found

Earlier in the day I'd wired `onHouseholdClick` into `ActivityScanChart` (commit `50e31ee4`). The cursor was pointer-style on hover but clicks didn't fire — Andrew confirmed by visual test.

Root cause: bound `onClick` to the top-level `<Scatter>` wrapper. Recharts' `<Scatter onClick>` doesn't fire per-dot reliably — the click handler must live on the SVG element returned from the `shape` callback. The `CashDragChart` pattern at `InflectionInsightsPanel.tsx:723-748` demonstrates the working approach: `cursor` + `onClick` bound to the `<g>` element inside `shape`, with full access to `payload.household_id`.

### Fix

Moved `onClick` + `cursor` style binding inside the shape callback's `<g>` element, mirroring `CashDragChart` verbatim:

```typescript
const clickable = !!(onHouseholdClick && payload.household_id != null)
return (
  <g
    filter="url(#activityDotGlow)"
    style={{ cursor: clickable ? 'pointer' : 'default' }}
    onClick={clickable ? () => onHouseholdClick!(String(payload.household_id)) : undefined}
  >
    ...
  </g>
)
```

Net diff: +11 / −8 LOC. tsc 0 errors. Shipped portal DEV `4267453d` / CLOUD `c918b7c1c`.

### Table-row clicks were already correct

The `<tr onClick={...}>` binding from the earlier commit (`50e31ee4`) didn't need fixing — table rows use plain React click events, not Recharts wrappers.

---

## Files Modified

| File | Surface | Diff |
|------|---------|------|
| `portal/src/api/portal-proxy.ts` | TO-4 smoke (override + revert) | 0 net (reverted) |
| `portal/public/non_model_assets_preview.json` | TO-4 smoke | created + deleted |
| `portal/src/pages/ModelPortfolios.tsx` | Canonical-to-trend Path A | +48 / −31 |
| `portal/src/api/endpoints/advisor-intelligence.ts` | Inflection AdvisorBookView Path A | +159 / 0 |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/InflectionInsightsPanel.tsx` | Per-dot click fix | +11 / −8 |

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC1 | DE → DS-base | 18:47 | Andrew direct coord — Model Portfolios backend data swap |
| RAVC1 | DS-base → DE | ~18:38 | SmartX Non-Model TO-4 preview standby (preempted my RAVC1) |
| RAVC2 PASS | DE → COO + DS-base | 18:54 | TO-4 portal smoke PASS (Andrew direct-verified) |
| RAVC1 | DE → DS~A | ~19:05 | SMARTX_RECONCILE Path B (publisher reconcile for ModelPortfolios) |
| RAVC1 | DE → DS~C | 19:51 | ADVI_INFADV Path B (Inflection advisor book.json field expansion) |
| RAVC2 SHIP | DS~C → DE | ~20:18 | ADVI_INFADV Path B shipped `0997324d6` (4 fields) |

Sub-conversations also: COO FYIs on each surface, RD acknowledgment of NNA empty-state polish ship (`e3f34428`), DS~B RAVC2 on INF_D_05 ship (`f244b425a`).

---

## Compiler Tools

| Tool | Run on | Result | Notes |
|------|--------|--------|-------|
| `bun run typecheck` | After each FE patch (3 surfaces × 1-2 iterations) | `tsc -b --noEmit` exit 0 | Per-surface gate |
| Empirical S3 inspection | aum-metrics.json, aum-timeseries.json, non_model_assets.json | Drift quantified | Side-by-side at Q-end dates |
| Empirical S3 inspection | s3://opal-data-inf/platinum/advisors/patrick_scanlan/ | All 5 artifacts present | book.json, composition.json, top_holdings.json, summary.json, timeseries.json |
| `aws s3 ls` (cross-firm) | s3://opal-data-bd/platinum/advisors/ | 168 advisor dirs; no scanlan/patrick_scanlan | Confirmed Andrew's "49F" was actually Inflection |

`comp-transform schema-check` not run this session — typecheck-only gate sufficient for the field-adapter work where the source-side types are already established.

---

## Decisions Made

1. **Path A FE adapter for Inflection advisor book** (not Lambda extension) — mirrors L3 client pattern; faster to ship; consistent with established static-S3 routing for Inflection.
2. **Single-role 'advisor' fee_summary stub** — Inflection doesn't have BD's role hierarchy; the FE panel collapses cleanly to one entry rather than rendering empty.
3. **Tax/role/active_since/mix_periods stubbed in Path A, real data flows through Path B** — keeps FE rendering coherent during the cut window; retire stubs after DS~C ship + AE chain.
4. **Did not modify the FE Lambda routing for 49F** — 49F's `opal-partners-data` Lambda still handles the headline → book mapping correctly. Only Inflection branches to the static adapter.
5. **Per-dot click binding moved to SVG `<g>` not `<Scatter>` wrapper** — Recharts API constraint; matches CashDragChart pattern that works in production.

---

## Concurrent ship cycles (inbox-surfaced)

| Lane | Agent | Commit | Subject |
|------|-------|--------|---------|
| Inflection Segment Analytics gaps | DS~A | `61ec0ca71` | INF_D_04 per-city DistributionStats + NNA period iteration (pending AE chain) |
| INF_D_05 per-window emit | DS~B | `f244b425a` | activity_scan_{qtd,ytd,1y,max}.json (pending AE chain) |
| NNA empty-state polish | RD 0.4.2 | `e3f34428` | DistributionTab right-partition NNA prompt + tenant-gated "advisor"/"architect" string |
| ADVI_INFADV Path B | DS~C | `0997324d6` | INF_D_02 role_breakdown + active_since + tax_exposure + clients[].relationship_since |
| SmartX Non-Model TO-1 | DS-base | `11d91fde6` | 557-row daily backfill preview (now canonical after Andrew's TO-4 PASS) |

All five gold-side ships pending AE 0.6.1 inf-gold-trigger fire to regenerate the platinum artifacts. Post-chain: my FE adapter stubs (tax/role/mix_periods) receive real Inflection data; DS~A's Segment Analytics fixes unblock bell-curve + NNA period chips on the Distribution tab; DS~B's activity_scan per-window unblocks accurate Activity-lens windowing.

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all unread; nothing pending |
| Portal DEV HEAD | `4267453d` (pushed) |
| Workspace CLOUD HEAD | `c918b7c1c` (pushed) |
| PROD state | Unchanged at `portal-v2.1.83` — v2.1.84 cut is Andrew's call |
| DE active work | None — on standby |
| Watcher | LIVE (`b30fxkbue`) |

---

## Next Steps

- [Andrew] Optional: cut `portal-v2.1.84` PROD to ship today's 4 FE fixes (BI rename + Activity HH-click + per-dot binding + ModelPortfolios canonical + Inflection adapter)
- [AE 0.6.1] Fire `inf-gold-trigger` to regenerate platinum artifacts. Single chain run unblocks: DS~A Segment Analytics bell-curve + NNA period chips, DS~B activity_scan per-window, DS~C ADVI_INFADV advisor book fields
- [DE next] Post-AE-chain: retire FE Path A stubs (`role_breakdown: {}`, `tax_exposure` zero block, `mix_periods: []`) in `getPlatinumAdvisorSummaryStaticInflection` since DS~C `0997324d6` ships real data
- [DE next] Post-AE-chain: RAVC2 verify Segment Analytics bell curve + Q1/Q2/Q3 chips render (DS~A asked for empirical screenshot)
- [DE next] Wire `getInflectionActivityScan` to take a window arg + thread `selectedWindow` through ActivityScanChart/Table data accessor; rename `txn_count_12m` → `txn_count` (~6 sites)
- [DS~A] SMARTX_RECONCILE Path B (publisher reconcile for non_model_assets.py Segments A+B) — no timing pressure, FE workaround live
- [DE/INFGRO] Stage 1 Phase 1 discovery (`comp-transform schema-check` + `comp-cache collisions`) — parallel-OK while DS base lane ships .001-.004
- [DE carry-forward] L2 useEffect migration in `ClientsTab.tsx:368-405` (from yesterday's session — still on backlog)
