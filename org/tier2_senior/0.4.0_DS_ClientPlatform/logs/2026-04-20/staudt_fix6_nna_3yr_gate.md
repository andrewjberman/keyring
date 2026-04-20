# Session — STAUDT.FIX6: 3-Year NNA History Gate at Platinum Layer

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-20
**Started:** ~15:00 UTC (session resumed from compacted context)
**Status:** Phase 1 COMPLETE — committed b7a75374 + pushed. Phase 2 (portal smoke test) pending DT deploy + cache invalidation.

---

## Origin

ADVI_STAUDT.FIX6 TO dispatched by 2.0.0_SA_COO, CTO-approved (20260420T143914Z). Assigned to ~D lane based on ~D's prior synthesis of platinum NNA consumers and the full B/C/D propagation chain during ADVI_STAUDT.D work.

INV1 (AE) ruled: firm-level NNA/AUA ratio 4.28x at 2020-12-31 ($118.20M NNA vs $27.65M AUA) is driven by universe asymmetry — silver/transactions covers a wider account universe (669 accounts at 2020-12-31) than holdings_lots-derived AUA (228 accounts). 441 "flow-only" accounts carry house-default attribution (49F House, rel_id=0); real flows, no AUA stock counterpart. Ratio normalizes to 0.91x by 2024 as holdings coverage expanded.

FIX6 directive: cap NNA history display at 3 years rolling. INTERIM gate only — root-cause fix (Option B, nna_atomic/ schema expansion) is separate scope.

---

## Phase 0 — Surface Identification

**Compiler tool runs:**

| Tool | Command | Result |
|---|---|---|
| comp-pipescript | `io D_00b` | Writes `gold/artifacts/timeseries_chart.json` → consumed by D_04 |
| comp-pipescript | `io D_02` | Writes advisor/client gold artifacts; no direct platinum NNA write |
| comp-pipescript | `io D_04` | Reads `gold/artifacts/timeseries_chart.json`; writes `platinum/firm/timeseries_chart.json` + `platinum/advisors/{id}/timeseries.json` |
| comp-blast | `D_04` | No downstream consumers — terminal node |
| comp-blast | `timeseries_chart` | D_00b:build_timeseries_chart → gold/artifacts/timeseries_chart.json → D_04 |
| comp-cache | `collisions` | 4 shared React Query keys; none include date-range params — cache invalidation required |

**Key architectural finding:** `data/black_diamond/scripts/platinum/` does not exist. "Platinum" is exclusively an S3 output prefix written by `D_04.client_portal_summary.py`. D_04 IS the platinum layer.

**Gate surface selected: D_04**

Rationale:
- Single upstream-most script writing BOTH `platinum/firm/timeseries_chart.json` (firm NNA) and `platinum/advisors/{id}/timeseries.json` (advisor NNA) simultaneously
- Terminal node per comp-blast — no downstream gold consumers; safe to gate here
- D_00b rejected: gating there would truncate `gold/artifacts/timeseries_chart.json`, silently breaking D_04's `_aggregate_nna_to_periods()` period-differencing logic (quarterly/monthly/annual buckets computed via endpoint deltas)
- D_02 rejected: advisor-level only; misses firm NNA

**NNA data structures confirmed (live S3 reads):**

Firm (`timeseries_chart.json`): `nna.data`, `nna_ofc.data`, `nna_geo.data`, `nna_adv.data` — each a list of `{"date": "YYYY-MM-DD", ...}` starting 2020-01-02, 2,296 entries.

Advisor (`platinum/advisors/{id}/timeseries.json`): `data[]` flat list of `{"date": ..., "total_aua", "cum_inflows", "cum_outflows", "nna", ...}` — cumulative per advisor since `active_since`. Travis Penfield: 2,109 entries from 2020-07-07.

**Cache invalidation risk:** React Query keys `['advisor-intelligence', 'timeseries-overview', 'firmOverride']` and `['partner-analytics', 'granularity', 'firmOverride']` have no date-range param. Post-deploy stale cache will serve ungated (pre-2023) NNA until TTL. Flagged for DT coordination.

**Phase 0 MCP to COO:** 20260420T150139Z. Awaited go-signal.
**COO GO:** received 20260420T150139Z (delivered during Phase 1 commit cycle — already executing).

---

## Phase 1 — Implementation

**Files modified:** `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`

**Edit 1 — `build_firm_pass_throughs()` (L2492-2496):**

Applied 3-year rolling gate to all NNA timeseries in `timeseries_chart` before platinum write:
```python
_nna_cutoff = (datetime.today() - timedelta(days=3 * 365)).strftime('%Y-%m-%d')
for _nna_key in ('nna', 'nna_ofc', 'nna_geo', 'nna_adv'):
    _block = timeseries_chart.get(_nna_key)
    if isinstance(_block, dict) and 'data' in _block:
        _block['data'] = [r for r in _block['data'] if r.get('date', '') >= _nna_cutoff]
```

**Edit 2 — `build_advisor_summaries()` (L611-612, L719-722):**

Compute `_nna_cutoff` once before the advisor loop; filter `ts_data['data']` via shallow copy before appending to advisor platinum write batch:
```python
_nna_cutoff = (datetime.today() - timedelta(days=3 * 365)).strftime('%Y-%m-%d')
# ... in loop:
ts_gated = dict(ts_data)
if 'data' in ts_gated:
    ts_gated['data'] = [r for r in ts_gated['data'] if r.get('date', '') >= _nna_cutoff]
items.append((ts_gated, f'platinum/advisors/{aid}/timeseries.json'))
```

`datetime` and `timedelta` were already imported at line 75. No new imports required.

AUA fields: NOT filtered. `aua.data` in timeseries_chart, advisor `total_aua`, and all AUA period data in summary.json are untouched per TO guardrail.

**Unit test (live S3 simulation, 2026-04-20 run):**

Cutoff: **2023-04-21** (today - 1,095 days)

| Surface | Before | After | Oldest | Assertion |
|---|---|---|---|---|
| nna.data | 2,296 | 1,091 | 2023-04-21 | PASS |
| nna_ofc.data | 2,296 | 1,091 | 2023-04-21 | PASS |
| nna_geo.data | 2,296 | 1,091 | 2023-04-21 | PASS |
| nna_adv.data | 2,296 | 1,091 | 2023-04-21 | PASS |
| advisor travis_penfield | 2,109 | 1,091 | 2023-04-21 | PASS |

**Gate test: PASS.** Pre-2023 data excluded; AUA unaffected.

**Deploy state:**

| Step | Result |
|---|---|
| Commit SHA | b7a75374 |
| Author | 0.4.0_DS_ClientPlatform~D |
| Branch | CLOUD |
| Push | origin/CLOUD up to date (75ee5877 with evidence file update) |
| Evidence file | data/black_diamond/diagnostics/STAUDT/FIX6/fix_to_6_evidence.md |

---

## MCP Trail

| Time (UTC) | To | Subject |
|---|---|---|
| 20260420T150139Z | 2.0.0_SA_COO | Phase 0 surface selection — D_04, requesting GO |
| 20260420T150818Z | 2.0.0_SA_COO | Phase 1 DONE — commit b7a75374, gate test PASS |
| 20260420T150829Z | 0.1.0_DT_MarketIntelligence | Cache invalidation required — 2 React Query keys at deploy |

COO responses:
- 20260420T150139Z: Phase 0 APPROVED — GO Phase 1. Surface rationale confirmed airtight. Cache note absorbed; DT handles at deploy cycle.

---

## Current State

- Gate code committed (b7a75374) and pushed to CLOUD.
- Evidence file fully populated through Phase 1 (data/black_diamond/diagnostics/STAUDT/FIX6/fix_to_6_evidence.md).
- DT MCP'd with React Query key cache invalidation specifics for deploy cycle.
- Phase 2 (portal smoke test) blocked on DT deploy + cache flush.

## Phase 2 Smoke Test Checklist (for ~D or DT post-deploy)

- [ ] Firm-level NNA timeseries widget: oldest visible date >= today - 3yr (rolling)
- [ ] Advisor-level NNA timeseries widget: oldest visible date >= today - 3yr
- [ ] AUA stock display: unchanged on all pages
- [ ] Portal loads without error on firm timeseries page and advisor timeseries drilldown
- [ ] Pre-2023 NNA NOT visible on any widget
- [ ] Cache invalidated for keys `['advisor-intelligence', 'timeseries-overview', 'firmOverride']` and `['partner-analytics', 'granularity', 'firmOverride']`

## Next Steps

- [0.1.0_DT_MarketIntelligence] Deploy D_04 from CLOUD b7a75374. Run D_04 against prod gold artifacts. Invalidate React Query cache keys per MCP. MCP ~D with deploy completion.
- [~D] On DT completion MCP: run Phase 2 portal smoke test. MCP COO with RAVC close (deploy SHA + smoke test evidence).
- [2.0.0_SA_COO] After ~D Phase 2 close: determine whether FIX6 is retained post-Option B (UX choice — pre-2023 NNA is sparse) or rolled back.

## Do NOT

- Do NOT touch D_00b, D_02, or nna_atomic/ — those are Option B's scope.
- Do NOT gate AUA fields — explicitly out of scope per TO guardrail.
- Do NOT push portal-layer changes — DT owns portal deploy.
- Do NOT invalidate cache directly — DT handles per COO instruction.
