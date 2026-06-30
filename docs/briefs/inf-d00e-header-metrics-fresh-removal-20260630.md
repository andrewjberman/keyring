# BRIEF: Remove INF_D_00e / header_metrics_fresh -- superseded freeze workaround (single-writer cleanup)

**Date:** 2026-06-30 | **Author:** 0.4.0_DS_ClientPlatform~A | **For:** 2.0.0_SA_COO (dispatch the FE lane)
**Type:** cross-lane coordination (backend DS + frontend DE) | **Andrew-directed** (verify-then-remove)
**Lanes:** BACKEND = 0.4.0_DS_ClientPlatform~A (in progress, this brief's author). FRONTEND = 0.4.0_DE_ClientPlatform (Andrew is instantiating; COO to MCP).

## Why (verified, grounded)
`header_metrics_fresh.json`, emitted by **INF_D_00e.fresh_header_supplement.py**, was the "frozen-but-fresh" WORKAROUND
(ADHC_BPMVH): show a fresh bronze-pmv-derived headline AUA while the canonical `header_metrics.json` was frozen. That
freeze ROOT-CAUSE is now fixed (ADVI_BREAKS **TO-2**, tonight): INF_D_00's 132B stub emit dropped -> **INF_D_04 is the
sole writer** of `platinum/firm/header_metrics.json`, which is now reliably fresh ($202,125,678.08, `data_as_of`
advancing, CTO-verified). The ADVI_BREAKS PRD also flags `header_metrics_fresh`'s **"false freshness honesty defect"
(INF_D_00 family)**. So the workaround has no remaining problem to solve + carries a known defect -> remove. Andrew:
"the only writer of header metrics was supposed to be D04; D00e was a race-condition extraneous thing."

Verification (so the FE lane is precise):
- `header_metrics_fresh` is STILL FE-rendered: `portal/src/.../PartnerAnalytics.tsx:30` imports + `:158` calls
  `getHeaderMetricsFresh()` -- the AdvisorIntelligence **headline AUA tile** ("fresh takes precedence for the headline
  tile only"). So a bare backend delete would BLANK that tile -- hence the 2-part change.
- The TO-6 freeze-monitor (`opal-globgrph-freeze-monitor`) is a READ-ONLY detection/ALARM, NOT a freshness-number
  producer -- it does not replace `header_metrics_fresh`; the canonical `header_metrics.json` does (now that it's fresh).
- INF_D_00e's 2nd output `_meta/reconciliation_summary_{date}.json` is NOT separately consumed (INF_B_00 writes a
  distinct `_holdings` variant; ADHC_BPMVH marked it "optional") -> stops with INF_D_00e, no consumer impact.

## The 2-part change (must align)

### BACKEND -- 0.4.0_DS_ClientPlatform~A (IN PROGRESS, this session)
- Remove `INF_D_00e` from `data/inf/scripts/gold/orion-gold-dispatch.sh`: CHAIN_COMPUTE (L336), CHAIN_INCREMENTAL
  (L341), CHAIN_GOLD_D (L348), the 2 gold-cd lists (L1080/L1087), + the catalog entry (L262).
- `git rm` `INF_D_00e.fresh_header_supplement.py` (dead after chain removal). Stops emitting `header_metrics_fresh.json`
  + `reconciliation_summary_{date}.json`.
- (Back out a small OUTPUT_PREFIX stage-edit I'd added to INF_D_00e for the rebuild -- moot once it's removed.)
- Existing `header_metrics_fresh.json` in S3 stays until a cleanup delete (Andrew-confirm per destructive-delete rule);
  it just stops being refreshed.

### FRONTEND -- 0.4.0_DE_ClientPlatform (COO to dispatch)
- `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`: repoint the headline AUA tile from
  `getHeaderMetricsFresh()` -> `getHeaderMetrics()` (the canonical, now-reliably-fresh `header_metrics.json` ->
  `total.aua`). Same number (~$202.13M), from the single canonical source.
- `portal/src/api/endpoints/advisor-intelligence.ts`: remove the now-dead `getHeaderMetricsFresh()` fn (L434) +
  `HeaderMetricsFreshResponse` type (its only caller is the tile above). Portal **DEV** branch.

## Alignment / sequencing
The FE repoint makes the headline tile read the canonical fresh number INSTEAD of the soon-going-stale `_fresh`. So:
the headline tile is never left showing a stale `_fresh` after the backend stops emitting it. No NUMBER change (both
~$202.13M) = transparent; but it IS a served-surface source change -> CVO spot-check the tile renders the canonical
fresh AUA. Reinforces single-writer-per-served-key (kills the `_fresh`/INF_D_00 family entirely).

## Gates
- never-widen: transparent (same value, canonical source) -- CVO spot-check; COO/CTO awareness (served-surface source change).
- The backend removal folds into the inf refactor dispatch (already being re-staged); no separate prod risk (the .sh is
  not auto-deployed; reaches the runner via the normal cutover). The FE is its own DEV->PROD portal promote (DT lane).
