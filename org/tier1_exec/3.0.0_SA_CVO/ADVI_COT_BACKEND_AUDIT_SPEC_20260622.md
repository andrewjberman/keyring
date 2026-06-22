# CVO Audit + Spec: Cottonwood (opal-data-cot) backend -> ADVI frontend readiness

**Author:** 3.0.0_SA_CVO | **2026-06-22** | **For:** Andrew + CTO (ADVI-COT frontend setup) | read-only audit.
**Grounding (Rule 22):** STATE claims read live vs S3/served (~17:00-18:00Z); MECHANISM/causal claims carry an explicit
`grounding:`; nothing inferred. Post-dates today's COTETL freeze-fix (5c80bf6ca, served-AUA advanced 06-09->06-18).

---

## 1. Executive summary

**The COT ADVI page is BUILT, WIRED, ACCESS-GATED, and (as of today's freeze-fix) DATA-FRESH to 06-18.** This is NOT a
greenfield setup -- it is an intentionally **Distribution-centric v1** (OUTCOME-B, ADVI_PRTORG.md 2026-06-09): COT has no
segmentable advisor dimension (2 founders ~= 96% of AUA), so all advisor/Books/leaderboard surfaces are *deliberately
disabled* for v1, flip-the-flags when the advisor dimension materializes. So most of "what we don't have" is
**deferred-by-design, not missing**. The real open items are a short FE-readiness checklist + non-v1-blocking backend debt.

---

## 2. Dimension 1 -- DAILY ETL (state: OPERATIONAL + FLOWING)

4-phase EventBridge chain (`cot-bd-session-trigger` Lambda, python3.11):
1. `cot-bd-session-daily` cron `0 2 * * ?` -> SSM `opal-cot-bd-session-fetch` on `cot-exporter` EC2 (i-0643a5bee8a8feabf, t3.small, **start-on-demand -- stopped between runs = NORMAL**).
2. SSM success -> mode=bronze-run.
3. S3 `_BRONZE_COMPLETE.json` -> mode=silver-run.
4. S3 `silver_complete.json` -> mode=gold-run -> `gold_dispatch.sh --chain full` (A_00..E_24).
- **STATE:** operational + flowing -- bronze @06-22, gold canonical @06-18 (live S3). Snapshot-first BD-native medallion.
- **Today's freeze-fix (grounding: SOURCE-CONFIRMED, git show 5c80bf6ca + my cert):** served firm-AUA was stuck at 06-09 (C_01/C_03 wired to the empty lots-FIFO account_gains chain); rewired to derive total_aua from the canonical_holdings snapshot -> advanced to 06-18. CERTIFIED CLEARED end-to-end today.

## 3. Dimension 2 -- BACKFILL / ARTIFACT STORE

**Backfill ceiling = 2026-04-22** (BD DataMining has no COT history before; transactions trade-dates start 04-22; the 03-09 silver file is a backfill-delivery, its trade-dates begin 04-22). **No deep history is obtainable** -- 04-22 is the floor.

| Layer / table | Coverage | State |
|---|---|---|
| bronze/ (BD session exports) | 06-13..06-22 (10 obj) | FRESH (raw recent; deep history in forwardfill_v2) |
| silver/transactions | 04-22..06-18 (trade-date) | FRESH (flows; nna basis) |
| silver/holdings, unrealized, allocations | ~06-08..06-18 | FRESH (the snapshot inputs) |
| **silver/prices** | 02-22..**06-07** (90 obj) | **STALE -- last write 06-09, 309h.** See flag-A. |
| gold/canonical/holdings, nna | 04-22..**06-18** (56d) | FRESH (the AUA + NNA chain) |
| gold/timeseries (account_performance), positions_cube | 04-22..**06-18** | FRESH |
| **gold/canonical/account_gains** | 04-23..**06-09** (308h) | DEAD-LOTS path, benign-UNCONSUMED (today's cert) |
| **gold/canonical/performance (C_00), nna_validation** | 04-23..**06-09** | STUCK at 06-09 (account_gains-dependent). See flag-B. |
| platinum/firm | 7 obj @06-18 | FRESH (the v1-served firm + distribution JSONs) |
| platinum/clients | 412 obj @06-18 | FRESH (per-client detail; lambda-routed, forward-only v1) |
| **platinum/advisors, platinum/accounts** | **EMPTY** | **BY DESIGN** (advisor/Books surfaces disabled v1 -- OUTCOME-B), NOT a gap |
| forwardfill_v2/{transactions,holdings,unrealized,realized,allocations} | txn 03-09; rest ~06-05..06-22 | the forward-filled daily store |

**Volume (STATE):** 694 accounts (D_00 707->694 relationship-filter: 13 unmapped excluded), 213 clients, **$395.30M firm AUA @06-18**.

## 4. Dimension 3 -- FE / ADVI PORTAL INTEGRATION (BUILT + WIRED)

The Cottonwood tenant is fully instantiated (created 2026-06-09 per ADVI_PRTORG.md Track 3 / §5-A, Andrew-direct):
- `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/` -- `layout.ts` (COTTONWOOD_LAYOUT), `index.tsx`, `constants.ts`, `roles.ts`.
- Registered: `_shared/hooks/useTenantLayout.ts` -> `cottonwood: COTTONWOOD_LAYOUT`.
- Access-gated: `firmAccess.ts` -- cottonwood route-set INCLUDES `/advisor-intelligence` + domain `cottonwood.com`.
- Backend: advisor-intelligence Lambda FIRM_CONFIG `cottonwood -> opal-data-cot/platinum`; lambdaScopeKey='cottonwood'; cottonwood **AC8 graceful-degrade** (degrades when `_meta.pmv_present===false`).
- Reachability: pipescript "mounted-reachable [CVO ground-truth]".

**v1 SCOPE (OUTCOME-B, intentional -- grounding: SOURCE-CONFIRMED, layout.ts comments + ADVI_PRTORG §5-A.1):**
- `routes.tabs = [{ id: 'distribution', label: 'Distribution', surface: 'admin' }]`, `defaultTab: distribution` -> **a single Distribution tab**.
- ENABLED: partnerAnalytics (defaultViewMode `geo`; allowed `aua`/`nna`/`geo`); distribution cohort `geo`; `gro` feature; auaDonut source `gold_aua`.
- DISABLED (no segmentable advisor dimension, 2 founders ~96% AUA): Advisors tab, Books tab, distribution cohorts `adv`+`ofc`, advisorPublicProfile, groDecomposition, roles.composition. "Flip the flags when the advisor dimension materializes -- zero structural change."
- **v1 CONSUMES:** platinum/firm/* (header_metrics, partner_analytics_{gran}, mix_summary, cumulative_chart, timeseries_overview/chart, dashboard) + gold/platinum/firm (cohort_a/cash_coverage) + geo/aua/nna distribution -- ALL @06-18 (fresh). So **the v1 page has fresh data today**.

## 5. WHAT WE HAVE (v1-ready)

- A built, wired, access-gated COT ADVI **Distribution-tab v1** consuming fresh @06-18 firm + geo/aua/nna distribution data.
- Daily ETL operational (4-phase, daily cron); the served-AUA freeze fixed + CERTIFIED today.
- Backfill 04-22 -> 06-18 for the entire AUA/NNA/distribution chain; 694 accounts / 213 clients / $395.30M AUA.
- Per-client detail (412 platinum/clients, lambda-routed) available as a forward-only handler.

## 6. WHAT WE DON'T HAVE

**(a) Deferred-by-design (OUTCOME-B -- NOT defects; flip-flags when the advisor dimension exists):**
- A segmentable advisor dimension; therefore: Advisors tab, Books tab, leaderboard, ADV + OFC distribution cohorts, advisor public profiles, GRO decomposition, role composition.
- platinum/advisors + platinum/accounts artifacts (the disabled surfaces' inputs).
- The fee-side (fee_earning_account_count=0 = cot fee-state; AUAFIX-L6 territory).

**(b) Real backend debt (non-v1-blocking -- the v1 distribution surface does not consume these):**
- `gold/canonical/performance` (C_00) + `nna_validation` STUCK at 06-09 (account_gains-dependent). flag-B.
- `silver/prices` STALE (stops 06-07). flag-A.
- `account_gains` dead-lots path (benign-unconsumed; documented future-cleanup).

## 7. Open MECHANISM questions (Rule 22 -- flagged for source-ground; none gate v1 today)

- **flag-A (silver/prices stale -> AUA?):** RESOLVED -- grounding: SOURCE-CONFIRMED. `B_00._build_canonical_from_snapshot` uses **BD-reported market_value** from the silver/holdings snapshot (`source='bd_snapshot'`, price=mv/units); the `canonical_prices` left-join is the Schwab/forward-fill path, NOT the cot snapshot path. So the v1 AUA is BD-mv-based, NOT prices-stale-affected. silver/prices-stale affects only the prices-dependent paths (C_00 performance) -> which are the already-stuck/disabled-surface paths. Backend hygiene, not v1-correctness.
- **flag-B (C_00 performance + nna_validation stuck 06-09 -> any v1 surface?):** RESOLVED -- grounding: SOURCE-CONFIRMED. The v1-served producers (D_00b.portal_timeseries et al.) read `canonical_nna` (@06-18) + `ACCOUNT_PERFORMANCE` (= gold/timeseries/account_performance, C_03, @06-18 FRESH) + monthly snapshot-mix + dimensions; NO `D_0*.py` reads `canonical_performance` (C_00) or `account_gains`. So the stuck-at-06-09 paths (C_00 performance, account_gains, nna_validation) are NOT consumed by ANY v1 surface -- they feed the DISABLED Books/perf surfaces only. **The v1 backend is data-clean.**
- **firmAccess users (the ONE remaining non-FE v1-readiness item):** the route-gate (`/advisor-intelligence`) + domain are wired; CONFIRM `opal-users-v2` has the intended COT users provisioned (the user-list is the companion to the route-gate) before declaring live-accessible. (DE/Andrew lane.)

## 8. Recommendation -- ADVI-COT frontend setup

**v1 BACKEND is COMPLETE + DATA-CLEAN** (built + wired + access-gated + data-fresh @06-18; both data-correctness flags A+B resolved -- the AUA is BD-mv-snapshot-based not prices-affected, and no v1 surface consumes the 06-09-stuck paths). The remaining v1-readiness items are OPERATIONAL/FE, not backend:
1. **FE render smoke-test** -- load the COT Distribution tab off the fresh 06-18 served data; confirm the geo/aua/nna panels + the partnerAnalytics geo-default render + the AC8 graceful-degrade behaves (DT/DE lane). (CVO can verify-channel served-vs-rendered once smoke-tested.)
2. **Confirm COT user-provisioning** in opal-users-v2 (firmId=cottonwood) -- the route-gate is wired; the user-list is the companion (DE/Andrew lane).
**Non-v1-blocking backend cleanup (none touch a v1 surface):** silver/prices feed (stale 06-07), the account_gains/C_00-performance/nna_validation stuck-paths, the fee-side (AUAFIX-L6) -- all feed deferred/disabled surfaces; deferred to the v2 advisor-dimension work.
**v2 (advisor dimension):** when COT's advisor dimension materializes, flip the OUTCOME-B layout flags (Advisors/Books/ADV-cohort) + stand up platinum/advisors+accounts -- zero FE structural change per the layout design.

-- 3.0.0_SA_CVO
