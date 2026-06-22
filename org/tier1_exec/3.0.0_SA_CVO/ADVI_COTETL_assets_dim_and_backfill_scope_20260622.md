# ADVI_COTETL: Daily Assets-Dim + Full Backfill -- scope (CVO, Andrew-direct "do all of the above")

**Author:** 3.0.0_SA_CVO | **2026-06-22** | **For:** COO decomposition -> DS/AE TOs; CVO verifies. | Rule-22-grounded.
**Origin:** Andrew-direct -- the Assets_Dim investigation (null MV/Units on his BD re-download) + "add a daily assets dim" + "every table from 4/22 backfill."

## 1. Findings (grounded)

- **"Assets_Dim" = the cot holdings/snapshot BD template (id 226355, Andrew-built)** -- per-account x per-asset positions (Market Value, Units, + asset attributes AssetID/Ticker/CUSIP/etc.), daily, CurrentDay. It feeds `silver/holdings -> canonical/holdings -> the $395.30M AUA`. grounding: SOURCE-CONFIRMED (holdings.json:6 names it; silver/holdings schema matches the download's 19 cols).
- **The null MV/Units on Andrew's manual re-download = a BD-UI-context artifact, NOT a data problem.** grounding: SOURCE-CONFIRMED -- our PIPELINE `silver/holdings` (latest 06-18, 10,714 rows) has market_value/units populated (1.7% null = cash edge-cases); the re-download (Assets_Dim (1).xlsx, 10,736 rows) has them 100% null. MV/Units are date+activity-context measures (inf's equivalent uses `activityOptionId=1`=Ending MV + `dateRangeId=6`); a raw UI re-download drops that context -> attributes populate (date-independent), MV/Units null. Pipeline data is sound.
- **Inflection already has the clean dedicated pattern:** `data/inf/manual_api/create_assets_dim_query.py` (creates the BD "Assets Dim" saved query, activityOptionId=1=Ending MV) + `data/inf/scripts/silver/build_assets_dim.py` (silver builder). cot's equivalent currently exists only implicitly as the holdings feed.
- **Backfill state (served-grounded):** transactions 04-22->06-18 (FULL); realized **06-01->06-17 only** (GAP: 402 sell-side txns exist 05-04->05-31 with no ingested realized); holdings/canonical 04-22->06-18 (served, recent raw snapshots only 06-08->); BD onboarding ceiling ~04-22 (no deeper history).

## 2. WORK ITEM A -- Daily Assets-Dim (DS; port the inf pattern)

Stand up a first-class daily cot **`assets_dim`** (per-account x per-asset positions: MV, Units, asset attributes) as a named ETL table, not just the implicit holdings feed:
- Port inf's `create_assets_dim_query.py` + `build_assets_dim.py` to cot, sourced from the existing Assets_Dim/holdings template 226355; ensure `activityOptionId=1` (Ending MV) so MV/Units populate.
- OPTION (DS/COO call): also a deduped **gold securities-master dim** (one row per AssetID: ticker/cusip/name/asset-class/expense-ratio/cash-equiv) if a true asset-attribute DIM is wanted alongside the positions table.
- CVO verify: the daily assets_dim lands with MV/Units populated (the pipeline value, not the UI-download null) + reconciles to the holdings/AUA.

## 3. WORK ITEM B -- Full backfill from 04-22 (DS pulls; AE session)

| Table | Action |
|---|---|
| transactions | HAVE (04-22->06-18) -- no action |
| realized | BACKFILL 05-04->05-31 (qt3, Custom + date-range; PIT-feasible -- sells confirmed in that window) |
| holdings / Assets_Dim | TEST historical snapshot lookback (Custom + past dates + activityOptionId=1). Banked caveat: the holdings export pins to CurrentDay -> lookback may return current-day. Feasibility-probe first, then backfill what works. |
| allocations (qt5), unrealized (qt4) | TEST the lookback (Andrew expects current-state-only / not PIT). Backfill only what's feasible; document what isn't. |

No silent caps: whatever lookback is NOT feasible, document it (so "backfilled" doesn't overstate coverage).

## 4. DEPENDENCY -- fresh BD session (AE) + a probe-script fix

- The stored BD session is **idle-dead** (keepalive 401, token-mint empty {} -- ~5h idle past the 30-60min TTL; the 20h expires_at is not the real limit). ALL live work (the assets_dim build, the backfill pulls, the lookback tests) needs a **fresh session via the cot-exporter EC2 `cot_bd_session_fetch.py`** (AE: start the EC2 + SSM the session-fetch -> fresh session in SM `blackdiamond/cot/session`).
- The existing `data/cot/scripts/bronze/cot_backfill_date_probe.py` is **BUGGY** -- uses `dateRangeType="DateRange"` + ISO dates (400s); the proven form is `"Custom"` + MM/DD/YYYY (per the S3 templates). Fix before use for the lookback probes.

## 5. Routing / ownership

- **COO:** decompose into TOs.
- **DS (0.4.0_DS_ClientPlatform):** Work Item A (assets_dim build), Work Item B (realized backfill + the lookback tests + backfill-what's-feasible), the probe-script fix.
- **AE (0.7.0_AE_CloudOps):** the fresh-session refresh (EC2 session-fetch) -- the gating dependency for all live work.
- **CVO (3.0.0_SA_CVO):** verify each -- the assets_dim MV/Units populated + reconciling; the backfill completeness (per-dataset earliest dates, no overstated coverage); the lookback-test results (feasible vs not, documented).

-- 3.0.0_SA_CVO
