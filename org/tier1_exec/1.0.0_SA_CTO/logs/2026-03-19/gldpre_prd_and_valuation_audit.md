# GLDPRE PRD, Valuation Audit, and Execution Coordination — 1.0.0_SA_CTO

**Date:** 2026-03-19/20
**Start Time:** session start (continuation from runtime eval session)
**End Time:** session end

## Objective

Diagnose the $42.9M AUA valuation gap between silver allocations and gold
client_performance, fix the root cause (scoped price override regression),
write the ADVI_GLDPRE PRD to unblock the full gold rerun, and coordinate
all agents through execution.

---

## Work Completed

### 1. Silver vs Gold AUA Reconciliation

Investigated the $42.9M gap between silver allocations ($1.593B) and gold
client_performance ($1.636B). Decomposed into three causes:

| Cause | Accounts | AUA Impact |
|---|---|---|
| Cash-only accounts (no positions in cube) | 72 | $2.16M missing from gold |
| Relationship ID remapping (counted under different IDs) | 28 | $14.5M reclassified, not missing |
| Pricing divergence (positions_cube * canonical_prices vs BD account_market_value) | All | ~$43M net (gold higher) |

### 2. BNP Mispricing Root Cause

Identified that BNP PARIBAS SA was priced at $96.63 (Yahoo Finance ticker
BNPQF — the real equity) instead of $0.75 (structured deposit). Single
position: 215,000 units = **$20.6M overvaluation**.

Root cause: `inject_scoped_overrides.py` generated override rows through
2026-03-17 only. `bd_price_update.py` ran on 2026-03-18 and inserted a
Yahoo row for 2026-03-18 with no competing override. The scoped override
script was manual, not integrated into the daily pipeline.

### 3. Scoped Price Override Fix (bd_price_update.py)

Integrated scoped overrides directly into `bd_price_update.py`:
- Added `scoped_override: -1` to `SOURCE_RANK` (highest priority)
- Added `_SCOPED_PRICE_OVERRIDES` registry (5 assets: BNP, Waldrop DAF,
  Destinations Large Cap/Intl, JPM structured note)
- Added `_SCOPED_OVERRIDE_MAP` lookup
- Modified `build_target_date_rows()` to check overrides first, before
  T1/T2/carry_forward cascade
- Updated `inject_scoped_overrides.py` to import from `bd_price_update.py`
  (single source of truth)
- Patched `canonical_prices.parquet` on S3: BNP Mar 18 corrected from
  $96.63 to $0.75

**These edits were lost during COO stash operations.** Recovered from stash
commit `b74ba2e8` and committed by COO at `a6b68032`.

### 4. Portal types.ts Restoration

Discovered that CLSUNI runtime commit `f0d9d01` had destroyed
`portal/src/pages/AdvisorIntelligence/types.ts` (1,397 lines → 17 lines).
This caused `hasTimeMachine` export missing error breaking the entire
Advisor Intelligence page. Restored from `f0d9d01^` and applied GLDPRE
4-class edits (alternatives field added to MixTimeseriesPoint,
FirmMixPeriodPoint, MixAssetClass).

Also found and fixed `ClientsTab.tsx` `deriveQuarterlyFromTimeseries` —
COO's stash pop left `structured_notes` and `other` lines referencing
fields that no longer exist on the 4-class types.

### 5. ADVI_GLDPRE PRD

Wrote PRD at `docs/architecture/ADVI_GLDPRE_PRD.md` (lost during stash
operations — content preserved in task orders and this log). Key decisions:

| Decision | Rationale |
|---|---|
| 4-class taxonomy: equity, fixed_income, alternatives, cash | Cash is residual (total - classified), guaranteeing sum = total by construction |
| Cash not independently classified | Positions_cube has no cash positions; residual approach prevents divergence |
| ETFClassifier for classification | Already deployed in Lambda (partners-api-v1.7.0); reads DynamoDB tables |
| Mix reads from firm_mix_views.json (06b), not timeseries_chart.json | timeseries_chart.json is written by an archived script not in the live pipeline |
| AUA total from client_performance, not independent positions_cube sum | Eliminates ~$7M divergence between Clients and Mix bar charts |

### 6. GLDPRE Task Order Issuance and Execution Coordination

Issued 3 task orders:

| Task Order | Agent | Scope | Status |
|---|---|---|---|
| GLDPRE.002 | 0.4.0_DS_ClientPlatform | 06b client_performance total substitution (WS2) | COMPLETE — `61f76c8b` |
| GLDPRE.005 | 0.6.0_AE_PartnerETL | Lambda deploy + EC2 S3 upload + full gold rerun | Phases 1-3 COMPLETE, Phase 4 EXECUTING |
| GLDPRE.006 | 0.4.0_DT_ClientPlatform | ClientsTab.tsx fix + portal DEV→PROD merge | Req 1-2 COMPLETE (`a466a7b`), GATED on gold rerun |

### 7. Validation of All Agent Work

Full code review of every GLDPRE commit:

**Parent repo (CLOUD):**
- `3ede9fc4` — WS1+WS3: 06b ETFClassifier + Lambda mix.json. Verified: classify_holding/classify_series delegate to ETFClassifier, _MIX_ASSET_CLASSES 3-class, compute_period_views cash residual, Lambda line 1056 changed. Clean.
- `a6b68032` — Scoped price overrides restored. Verified: SOURCE_RANK, _SCOPED_PRICE_OVERRIDES, _SCOPED_OVERRIDE_MAP, build_target_date_rows override-first. Clean.
- `61f76c8b` — WS2: client_performance total substitution. Verified on CLOUD.

**Portal (DEV):**
- `a4f71d7` — WS4+WS5: types.ts restoration + 4-class PartnerAnalytics. Verified: FIRM_MIX_COLORS 4-class, firmMixChartData maps alternatives, stacked bar keys 4-class, hasTimeMachine present.
- `a466a7b` — ClientsTab.tsx fix. Verified: deriveQuarterlyFromTimeseries has exactly 4 class lines.

**Issues found and fixed in AE task order (GLDPRE.005):**

| # | Severity | Issue | Fix |
|---|---|---|---|
| 1 | Bug | `--full` should be `full` (positional arg) | Fixed in req 5 |
| 3 | Critical | Missing `lib/__init__.py` S3 upload | Added to req 2 |
| 4 | Critical | bd_price_update.py edits lost in stash | Committed at a6b68032 |
| 5 | Minor | EC2 manual pull redundant (run_gold_layer.sh auto-syncs) | Removed |
| 6 | Bug | timeseries_chart.json S3 path wrong bucket | Corrected to opal-data-bd |
| 7 | Bug | Phase 3 gate referenced script 09 (WS2 actually went into 06b) | Gate rewritten, marked CLEARED |

### 8. Project Registration

- Created `org/projects/ADVI_GLDPRE.json`
- Added ADVI_GLDPRE row to REGISTRY.md Active Projects
- Updated ADVI_GLDRST as blocked by GLDPRE
- Updated CTO prompt.md dashboard (session 6)
- Ground truth corrections: ADVI_GLDRST added to registry, pipeline tags updated

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Scoped overrides integrated into bd_price_update.py, not separate script | Prevents timing gap where Yahoo price can win on dates the override script hasn't covered |
| WS2 targets 06b (not script 09) | firm_mix_views.json is what the Mix stacked bar chart reads; script 09 writes header_metrics which is a different UI element |
| Cash is residual, not classified | Guarantees Mix total = Clients total by construction; positions_cube has no cash positions anyway |
| timeseries_chart.json left as-is | Written by archived script 08; not in live pipeline; unrelated to Mix stacked bars |
| Full gold rerun satisfies GLDPRE + MIXV2.003 + MVP318.003 | All three need a full run; GLDPRE's 4-class change supersedes the others |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/black_diamond/scripts/silver/bd_price_update.py` | Scoped override integration | Yes — `a6b68032` |
| `data/black_diamond/scripts/silver/inject_scoped_overrides.py` | Import from bd_price_update | Yes — `a6b68032` |
| `org/projects/ADVI_GLDPRE.json` | Created | Yes — `5c56e271` (part of COO commit) |
| `org/projects/REGISTRY.md` | GLDPRE + GLDRST rows | Yes |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | Dashboard updated to session 6 | Yes |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_GLDPRE.002.ws2-aua-mix.md` | Created (v3) | Local only |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_GLDPRE.006.dt-portal-commit-and-merge.md` | Created | Local only |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_GLDPRE.005.ae-deploy-and-gold-run.md` | Updated (Phase 3 gate, script 09 refs) | Local only |
| `canonical_prices.parquet` (S3) | BNP Mar 18 patched $96.63→$0.75 | S3 direct |

---

## Current State

**Status:** IN PROGRESS
**Active branch:** CLOUD

All GLDPRE code is committed and deployed. Lambda at partners-api-v1.8.0.
Gold scripts uploaded to S3 (06b with WS1+WS2, lib/etf_classifier.py,
lib/__init__.py). AE executing Phase 4 (full gold rerun) on
bd-gold-layer-runner EC2. Portal DEV has all fixes pushed. DT gated on
gold rerun verification before DEV→PROD merge.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Complete Phase 4 (full gold rerun) and run
   acceptance checks (req 6). Update EC2_MANIFEST.json (req 7).
2. **[0.4.0_DT_ClientPlatform]** After AE confirms gold rerun success:
   portal DEV→PROD merge + deploy-manual.sh + submodule pointer update.
3. **[1.0.0_SA_CTO]** Verify portal Mix bars match Clients bars on PROD.
   Close GLDPRE. Unblock GLDRST.

**Do NOT:**
- Merge portal to PROD before AE confirms gold rerun passes all checks
- Re-run inject_scoped_overrides.py separately — bd_price_update.py now handles overrides inline
- Treat GLDPRE as complete until portal is deployed and Mix/Clients bar parity is verified
