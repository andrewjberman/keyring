# MDPF Bell-Curve Unfunded-Footer — Grain/Scope Lineage Verify (TO-A)

**Author:** 0.4.0_DE_ClientPlatform · **Date:** 2026-06-01 · **archetype:** VALIDATE (sec: TRACE, DIAGNOSE)
**Dispatch:** COO [DRIVE-GO] TO-A (gate for DS TO-B), CTO PRD mdpf-bellcurve-unfunded-footer-lineage-prd-20260601.md
**Verdict:** 6639 REPRODUCED to the integer. Root cause = primarily a **SCOPE mismatch** (GLOBAL metrics − PER-FIRM distribution), compounded by a **grain** mismatch (inflection distribution = clients-grain). The PRD's "accounts−clients grain" is a real secondary factor; the dominant, pinned mechanism is scope.

## Lineage (FE subtraction -> served feeds -> producers)
- **Footer calc (FE, ModelPortfolios.tsx):** total L1043 `(metricsData.total.account_count) - (activeDistribution.total.account_count)`; per-model L1009 analogous.
- **metricsData** = `getAUMMetrics()` -> `/api/general/portfolios/aum-metrics.json` -> S3 `json/portfolios/aum-metrics.json`. **GLOBAL scope** (no `firm_id`, no per-firm breakdown; only `total` + `by_model`). Source: SmartX aum-metrics.
- **activeDistribution** = `isPerFirm ? perFirmDistribution : distributionData`:
  - global -> `getAccountDistribution()` -> `json/portfolios/account-distribution.json`
  - per-firm -> `getAccountDistributionByFirm(firmId)` -> `json/mdpf/{firmId}/account-distribution.json` (producer `09.generate_partner_analytics.py` for 49/global, **`INF_09.generate_partner_analytics.py` for inflection**).

## Reproduced numbers (live served feeds, 2026-06-01)
- **X = metrics.total.account_count = 7039** (GLOBAL, all-firms).
- Y_distribution.total.account_count: global=**7025**, 49financial=**6838**, inflection=**400**.
- Footer = X - Y:
  - Global: 7039 - 7025 = **14** (PRD 14 ✓)
  - 49financial: 7039 - 6838 = **201** (PRD 201 ✓)
  - Inflection: 7039 - **400** = **6639** (PRD 6639 ✓✓)
- **PIN: 6639 = 7039 (metrics.total.account_count, GLOBAL) − 400 (json/mdpf/inflection/account-distribution.json total.account_count).**

## Root-cause (refines the PRD)
1. **SCOPE (dominant):** the metrics numerator is GLOBAL (7039, all firms) while the distribution denominator is PER-FIRM. So per-firm footers compute `global_accounts − firm_distribution`:
   - Global = global−global = 14 (genuinely correct).
   - 49 = global(7039) − 49(6838) = 201 — **coincidentally plausible ONLY because 49 ≈ 97% of global accounts**; this is NOT a true per-firm 49 count. The scope bug affects 49 too, just MASKED.
   - Inflection = global(7039) − inflection(400) = 6639 — exposed (inflection is ~6% of global).
2. **GRAIN (secondary, compounding):** per-firm distributions are NOT additive to global (49 6838 + inf 400 = 7238 ≠ global 7025), and the in-code note (`AdvisorIntelligence/_shared/tabs/DistributionTab.tsx:175`: "Inflection: distribution.total.count is client count, not accounts"; L3366: "Inflection returns 295 clients, not 548 accounts") confirms `INF_09`'s `account_count` is clients-grain, not accounts.
3. **No per-firm accounts-grain count exists in any served feed** — metrics is global-only; the per-firm `aggregate-aua-timeseries.json` carries AUA values but NO account count. So the FE subtraction CANNOT be made correct by a scope-fix alone (there is no per-firm `account_count` numerator to substitute).

## Wrong-grain/scope feeds (for DS TO-B)
- **metrics (aum-metrics.json):** wrong SCOPE for a per-firm footer (global-only; no per-firm account_count emitted).
- **INF_09.generate_partner_analytics distribution:** wrong GRAIN (`account_count` = clients, not accounts) for inflection.
=> Neither feed provides a per-firm accounts-grain count. **A scope-fix alone is not possible from current feeds.**

## Recommendation (gates TO-B)
PRD option **(b) is necessary, not just preferred**: the producer (DS) should emit, **per firm, at accounts grain**, the excluded-unfunded count directly — i.e. count newly-opened $0-balance ACCOUNTS per firm — as an explicit field the FE renders (no cross-feed subtraction). Alternatively emit BOTH a per-firm total-accounts count AND a per-firm funded(bell-curve)-accounts count, both accounts-grain, so the FE difference is valid per firm. Option (a) (align grains) is insufficient unless it ALSO adds a per-firm accounts-grain metrics numerator (which doesn't exist today). TO-C (RD FE-guard) correctly suppresses the cross-grain number meanwhile.

## TO-A acceptance (COO's 4 asks)
1. Grain confirmed: metrics=GLOBAL accounts (7039, no per-firm); inflection distribution=per-firm 400, clients-grain (per :175 + non-additivity). Mismatch = SCOPE + grain.
2. 6639 reproduced to the integer: X=7039 (metrics.total.account_count), Y=400 (inflection dist total.account_count).
3. Wrong feed pinned: BOTH — metrics global-scope + INF_09 distribution clients-grain; no per-firm accounts-grain count exists.
4. 49/Global: 14 is genuinely correct (global−global); **201 is coincidentally-plausible (global−49, masked by 49≈global), NOT a true per-firm count** — refines the PRD claim that 49 is clean accounts−accounts.

## Compiler Tools
- N/A — read-only lineage verify of live served JSON + FE source trace (no gold/portal edit). comp-* applies when DS edits the producer (then comp-pipescript io on the gold script).
