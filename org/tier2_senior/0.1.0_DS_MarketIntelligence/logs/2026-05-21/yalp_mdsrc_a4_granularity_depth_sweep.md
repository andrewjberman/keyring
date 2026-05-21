# Session Log -- 0.1.0_DS_MarketIntelligence

**Date:** 2026-05-21
**Branch:** CLOUD
**Task Order:** YALP_MDSRC.A4 -- YCharts granularity+depth full-entity sweep (paired TO; DS = deliverable lead, 0.7.0_AE_CloudOps~A = paired AE / capture side)

---

## Summary

A4 verifies, per portal-tracked entity, the GRANULARITY + DEPTH the YCharts internal API actually delivers -- whether a YCharts pull can replace the Bloomberg data_pkl feed for that surface. A3 mapped the endpoints; A4 adds the granularity/depth dimension. Spot-probe baseline was n=1 (S&P 500 ~76yr daily); A4 is the full sweep.

## Phase 0 -- universe enumeration + symbol resolution (DS, no YCharts seat)

ENTITY UNIVERSE = 76 entities, enumerated:
- 53 INDEX -- DynamoDB opal-portal-market-data entity_type=INDEX (per the dc01d4b8a 71-row crosswalk).
- 11 BOND_INDEX -- entity_type=BOND_INDEX.
- 7 COMMODITY -- entity_type=COMMODITY (IN SCOPE per COO scoping decision).
- 5 ETF -- exact set resolved: BIL, VGSH, AGG, IVV, ACWI (source: infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/lambda_function.py:30-36 ETF_BENCHMARKS; output json/benchmarks/etf_returns.json). The TO's "~5 (confirm exact set)" is now concrete = 5.

SYMBOL RESOLUTION (crosswalk + A3-P4 corrections applied):
- 67 PROBE-READY -- YCharts symbol resolved, ready for the granularity/depth probe.
- 9 RESOLVE-FIRST -- need one symbol-resolution attempt before probing:
  - 5 securities-search: MSCI USA Size, Silver, Crude Oil Brent, Natural Gas, Copper (A3-P4 genuinely-unmapped).
  - 4 bbg-family-pin: Bloomberg 0-1 Yr Treasury, 0-5 Yr High Yield, 0-5 Yr TIPS, 20+ Yr Treasury (A3-P4 still-wide maturity-band variants).
- A3/A2 corrections applied: 7 MSCI-country LOC variants (^MS**L) for the A3-P4-confirmed wides (Australia/India/Japan/S.Africa/S.Korea/Switzerland/Taiwan); bond plain-USD symbols; ACWI ex US = ^MSACXUSL; Bitcoin/Ethereum/WTI/Gold = securities (BTC/ETH/WTI/GOLD).
- The 10 other MSCI single-country indices kept at crosswalk USD symbols -- variant choice is a C2 value-fidelity item; granularity/depth is variant-insensitive (USD/LOC of the same MSCI index share trading calendar + inception).

DELIVERABLE: docs/briefs/mdsrc-a4-entity-universe-20260521.csv -- 76 rows, columns entity_type,portal_name,bbg_ticker,yc_symbol,yc_kind,phase0_status,note.

## Phase 1 -- live capture (paired AE 0.7.0_AE_CloudOps~A)

~A calibrated on ^SPX then swept all 67 PROBE-READY entities via fund_data.json at maxPoints=100000. Capture: .runtmp/a4_capture/a4_sweep_capture.json (keyed by yc_symbol, exact URL per row) + a4_boundary.json.
- 31 captured HTTP 200 -- clean daily series.
- 36 returned HTTP 400 "no valid items" -- all 29 MSCI + all 7 Bloomberg-bond indices; they are not fund_data.json items, and their canonical endpoint general_data.json 403s on the session (fund_data.json/table_data 200 same run -> endpoint-gated, not seat eviction).
- 9 RESOLVE-FIRST -> blocked-pending-symbol (Batch 0, one attempt each, evidenced).
AC5: fund_data.json is the canonical C2 series endpoint; calc is entity-class-specific (level for ^-indices, price for securities/ETF); startDate/endDate ignored; granularity is maxPoints-driven.

## Phase 2 -- granularity/depth matrix + brief

Built docs/briefs/mdsrc-a4-granularity-depth-matrix-20260521.csv (76 rows) via .runtmp/a4_build_matrix.py.
Verdict tally: meets 29 + partial 2 + pending-C1 36 + blocked 9 = 76.
- 29 meets: clean daily, depth 12.2-96.4yr -- far exceeds the ~6yr DynamoDB backbone.
- 2 partial: BTC/ETH -- daily but only 1.8yr (YCharts crypto coverage starts 2024-07).
- 36 pending-C1-fresh-session-test: verdict hinges on base's C1 fresh-session general_data.json probe -- degraded-session (recoverable) vs entitlement-gap (stays-Bloomberg-pkl).
- 9 blocked-pending-symbol: C2 browser-in-loop securities-search (5) / Bloomberg->ICE cross-vendor decision (4).
Brief: docs/briefs/mdsrc-a4-granularity-depth-brief-20260521.md.

## Compiler Tools

A4 is a YCharts-internal-API investigation TO -- no comp-* graph tool covers the YCharts backend (per TO compiler_tools_mandate <note>). Structural self-checks:
- Phase-0 step 1 (universe count): observed 76 entities (53+11+7+5); ETF set concrete = 5. PASS.
- Phase-0 step 2 (crosswalk corrections): MSCI-country LOC variants + bond plain-USD symbols applied. PASS (moot for the 36 -- they 400 on fund_data.json regardless of variant).
- Phase-2 step (matrix row-count): 76 rows, one per Phase-0 entity, all columns populated, 9 blocked + 36 pending present as explicit rows. PASS -- 29+2+36+9=76.

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdsrc-a4-entity-universe-20260521.csv` | NEW (Phase 0) -- 76-entity universe + symbol resolution |
| `docs/briefs/mdsrc-a4-granularity-depth-matrix-20260521.csv` | NEW (Phase 2) -- per-entity granularity/depth matrix, 76 rows |
| `docs/briefs/mdsrc-a4-granularity-depth-brief-20260521.md` | NEW (Phase 2) -- the A4 brief |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/YALP_MDSRC.A4....md` | status in_progress -> complete |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-21/yalp_mdsrc_a4_granularity_depth_sweep.md` | this log |

## RAVC

| RAVC | From/To | Status |
|------|---------|--------|
| GO YALP_MDSRC.A4 (+ paired-TO amendment) | COO -> DS | RECEIVED |
| ACK + Phase 0 complete | DS -> COO | SENT |
| Phase 0 universe + capture spec | DS -> 0.7.0_AE_CloudOps~A | SENT |
| Capture handoff (31/67 + boundary) + 36-entity finding | 0.7.0_AE_CloudOps~A -> DS | RECEIVED |
| RAVC2 complete (matrix + brief; 36 provisional) | DS -> COO + CC CTO | SENT this closeout |

## Next Steps

1. [base 0.7.0_AE_CloudOps, C1 Phase 0] fresh-session general_data.json GET -- reports 200-vs-403 to DS + ~A + COO; resolves the 36-entity fork.
2. [follow-on] finalize the 36 provisional matrix rows on the C1 probe result -- either ~A re-captures (degraded-session) or they convert to confirmed stays-Bloomberg-pkl (entitlement gap). Recommend folding into C2's pre-build step.
3. [C2, 0.1.0_DS + 0.2.0_DS] consume the matrix to bound pulls; close the 9 blocked-pending-symbol via browser-in-loop search / cross-vendor decision.
