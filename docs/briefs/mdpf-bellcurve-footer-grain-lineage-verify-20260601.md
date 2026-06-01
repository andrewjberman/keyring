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

## CORRECTIONS (DS~B 2026-06-01, post TO-B emit) — record-accuracy
Two corrections from DS~B (producer owner) to the lineage above; my GRAIN/SCOPE findings stand, these refine the producer + arithmetic:
1. **PRODUCER (corrects this brief's §"Lineage" + PRD §2):** `json/mdpf/{firm}/account-distribution.json` (what the footer reads) is produced by **`data/smartx/scripts/compute_per_firm_account_distribution.py`** (49F + inflection) + **`compute_account_distribution.py`** (global) — NOT `09/INF_09.generate_partner_analytics.py` (those publish `partner_analytics.json` (NNA) on opal-data-inf, a different artifact). DS~B confirmed empirically (served shape + source `eclipse model_portfolio_accounts` + period match compute_per_firm exactly). So the PRD §2 + my original producer attribution were wrong; the fix lands in compute_per_firm_account_distribution.py (DS~B emitted the field there).
2. **ARITHMETIC (refines the TO-B verify):** `active_accounts_count` is TOTAL active = funded + unfunded. So `active(405) = funded(account_count=400) + excluded_unfunded(5)`; **excluded = active − funded = 5**; accounts-grain total = 405 (NOT 410 as I'd added). `account_count(400)` is the FUNDED (histogram/bell-curve) count, not clients-grain. FE reads `excluded_unfunded_count` directly (confirmed).
3. **49F status:** DATA-blocked, not code-pending — DS~B added the field to the 49F path but the upload was anti-regression-guard-skipped (smartx_allocations 202606 = unvalued $0 shell -> 0 funded -> would regress 6838->0). 49F emits once 202606 is valued OR producer selects latest-funded-period. Plus DS~B owned-paths-blocked (data/smartx/** = AE lane) -> routed to COO. So my "extend 09" ask was misdirected (right producer = compute_per_firm; 49F path already coded, data+lane-blocked).

## Compiler Tools
- N/A — read-only lineage verify of live served JSON + FE source trace (no gold/portal edit). comp-* applies when DS edits the producer (then comp-pipescript io on the gold script).
