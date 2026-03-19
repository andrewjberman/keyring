# Startup Ground Truth Correction — 2.0.0_SA_COO

**Date:** 2026-03-19

## Corrections Applied (4)

| Document | Old State | Corrected State |
|----------|-----------|-----------------|
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_MVP318.005.rd-consolidated-overview-panel.md` | status: pending | status: complete — ConsolidatedOverviewPanel committed to portal DEV at 62143e7, CLOUD pointer updated at a8b1c3e8 |
| `org/projects/ADVI_MVPLVL.json` | phase: "Only remaining: DT portal DEV->PROD merge" | Updated: MVPLVL.007+.008 newly issued (DS advisor endpoints + open_lots canonicalization), WS5 DE chart windows also pending before merge |
| `org/projects/REGISTRY.md` | ADVI_MVPLVL row: stale phase description | Updated with .007+.008 pending + MVP318 WS5 gate |
| `deliverables/delivery_status.md` | Last updated 2026-03-17; missing all 2026-03-18 activity | Updated with full 2026-03-18 work: DS MVP318.001 COMPLETE, DT bd-v2.19.2+partners-api-v1.4.0 deployed, RD ConsolidatedOverviewPanel done, AE script 07 + ETF fix, DE MIXV2 WS4+WS5, new MVPLVL.007+.008 |

## State Found (2026-03-18 activity)

### ADVI_MVP318
- DS 001 COMPLETE: eb70758d (bd-portal-publisher MVPLVL.006), a3903a03 (advisor-publisher D4+WS3a), 6234d50c (opal-partners-data WS3c), fec1f7e4 (WS1 geo fix)
- DT WS1-A diagnostic: Root Cause A (BD country='United States' not 'USA') confirmed
- DT bd-v2.19.0: bd-portal-advisor-publisher (D4+WS3a) + bd-portal-publisher (MVPLVL.006)
- DT bd-v2.19.1: bd-portal-publisher WS1 geo fix (fec1f7e4)
- DT bd-v2.19.2: API Gateway routes for firm+advisor partners endpoints (f8597824)
- DT partners-api-v1.4.0: opal-partners-data advisor routes (WS3d)
- AE: Script 07 isolation run (b2119882) -- geo parquet rebuilt, TX $900.8M in 49 states
- AE: ETF ticker fix in silver scripts (b69d1ae6), canonical_prices rebuilt
- WS6 gate status: WS4 DONE (RD portal DEV 62143e7) | WS5 PENDING (DE ADVI_MVP318.004 req 3)

### ADVI_MVPLVL
- RD committed ConsolidatedOverviewPanel + open-lots grouping to portal DEV (62143e7)
- CLOUD pointer updated at a8b1c3e8
- RD issued two NEW task orders to DS and DE (via a8b1c3e8 CLOUD commit):
  - MVPLVL.007 (DS): advisor-level AUA + mix timeseries endpoints for L2 quarterly bar in ConsolidatedOverviewPanel
  - MVPLVL.008 (DS): open_lots field canonicalization (current_units->quantity, accrued_gain->unrealized_gain)
- MVPLVL project JSON phase was stale -- corrected
- Portal merge gate is now: DS .007+.008 + MVP318 WS5 (DE chart windows) + DT execute merge

### ADVI_MIXV2
- DE 005 (MIXV2 WS4+WS5): cbb9d38 (firm mix chart) + fcb95c7 (ClientDetailPage wiring) on portal DEV
- DT 004: partners-api-v1.3.0 deployed (pct fix + firm/advisor mix-views endpoints)
- AE 003 (06b EC2 deploy + gold run): in_progress per task order status

### ADVI_ADVTV2
- DS committed: 8ef1da9b
- EC2 deploy done: 72c03d2a
- DT ADVTV2.002 (FULL gold run): still pending -- will be batched into MVP318.003 AE gold run

## Task Orders Verified Current

| Task Order | Status | Evidence |
|-----------|--------|----------|
| ADVI_MVP318.001 DS | complete | DS self-marked; confirmed by 4 CLOUD commits |
| ADVI_MVP318.002 DT | in_progress | WS1-deploy+WS2+WS3b+WS3d DONE; WS6 still pending |
| ADVI_MVP318.003 AE | pending | No AE full gold run log found for 2026-03-18 |
| ADVI_MVP318.004 DE | pending | DE 2026-03-18 session was MIXV2 only; MVP318 WS3e+WS5 not done |
| ADVI_MVP318.005 RD | complete (corrected from pending) | portal DEV 62143e7 + CLOUD a8b1c3e8 |
| ADVI_MVPLVL.005 DT | pending | Portal DEV->PROD merge not done |
| ADVI_MVPLVL.007 DS | pending | Just issued; no DS work yet |
| ADVI_MVPLVL.008 DS | pending | Just issued; no DS work yet |
| ADVI_ADVTV2.002 DT | pending | No DT gold run log found |
| ADVI_MIXV2.003 AE | in_progress | AE started but full 06b gold run not confirmed complete |

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

4 documents corrected. Startup audit complete.

Priority queue for this session:
1. **AE MVP318.003** -- FULL gold run is UNBLOCKED (bd-portal-advisor-publisher at bd-v2.19.0, gate cleared). AE should run now.
2. **DE MVP318.004** -- WS3e (advisor types+API functions) + WS5 (chart windows). WS3e gate cleared (partners-api-v1.4.0 live).
3. **DS MVPLVL.007+.008** -- New task orders from RD. WS3c commit (6234d50c) is the backend for .007. DS may need to verify existing endpoints suffice or add new ones.
4. **DT portal WS6** -- Will unlock once DE MVP318 WS5 + (optionally) DS MVPLVL.007+.008 complete.

## Next Steps

1. **[0.6.0_AE_PartnerETL] Execute MVP318.003 FULL gold run** -- gate cleared (DT bd-portal-advisor-publisher @ bd-v2.19.0). Batches ADVTV2.002 + MIXV2.003 + WS5 script 10.
2. **[0.4.0_DE_ClientPlatform] Execute MVP318.004** -- WS3e advisor types+functions + WS5 chart windows. Gate cleared.
3. **[0.4.0_DS_ClientPlatform] Execute MVPLVL.007+.008** -- advisor endpoint verification + open_lots field fixes.
4. **[0.4.0_DT_ClientPlatform] Portal DEV->PROD merge (WS6)** -- after DE MVP318 WS5 committed to portal DEV.
5. **[2.0.0_SA_COO] Confirm WS6 gate once DE MVP318.004 req 3 is committed** -- then green-light DT for merge.
