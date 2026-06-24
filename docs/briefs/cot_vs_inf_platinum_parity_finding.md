# Cottonwood vs Inflection — platinum artifact parity (snapshot-pipeline verification)

**By:** 0.4.0_DS_ClientPlatform · **2026-06-24** · Andrew-direct (verify cot's snapshot-native served output is real + complete vs inf's reference). **Grounded:** validate-on-served (boto3 reads of opal-data-cot / opal-data-inf platinum/).

## TL;DR
cot's served output is **REAL** (genuine Cottonwood data, correct for its history). **Most apparent gaps are EXPLAINED** by two facts: (1) Cottonwood is **newly onboarded** — gold spans only **2026-04-22..06-23 (~2 months, 58 daily dates)**, so short time-series are legit, not truncated; (2) cot has **no advisor assignments** (`header_metrics.by_architect=['Unassigned']`), explaining the absent advisor tree + leaderboard. **BUT a real residue remains**: current-snapshot-computable analytics that exist in inf and are empty/missing in cot despite cot having 58 days of holdings snapshots → a genuine cot-pipeline gap to fix.

## Type-level (firm/ dashboard artifacts): inf ~32 vs cot 10
**cot HAS (10):** clients-tab-slim, cumulative_chart, dashboard, header_metrics, mix_summary, partner_analytics_{annual,monthly,quarterly}, timeseries_chart, timeseries_overview.

**cot MISSING vs inf — classified:**
- **Legit-absent (snapshot-native, no transaction-engine/canonical-prices/NNA — per Andrew):** advisor_nna_canonical, nmec_nmnc_nna, activity_scan(+1y/max/qtd/ytd), cash_drag(+variants). These need the txn-flow/NNA path cot deliberately doesn't run.
- **Legit-absent (no advisor dimension — all Unassigned):** the entire `platinum/advisors/{adv}/` tree (inf: book/composition/timeseries/summary/top_holdings/nna per advisor x4), leaderboard, header_metrics by_architect detail.
- **SUSPICIOUS-absent (current-snapshot-computable, cot has the holdings to build them, yet missing):** `top_holdings`, `concentration_risk`, `firm_composition`, `firm_concentrations`, `client_directory`, full `clients_tab` (cot has slim only), `fee_efficiency`. These don't need history or advisors — they're current-holdings rollups cot SHOULD produce.

## Content-level spot-check (artifacts cot DOES have)
Real data, but several sub-objects empty/null that are POPULATED in inf and computable from cot's current snapshot:
- **mix_summary:** cot `mix_periods=[]` (history-ok), but `concentration={}` EMPTY + `composition=null` — these are CURRENT-snapshot computations → should populate. **GAP.**
- **header_metrics:** core KPIs present (aua, nna_*, counts) + real; missing `account_distribution` (inf: 792 records) + `radial_12m` — account_distribution is snapshot-computable. **GAP.**
- **timeseries_overview / timeseries_chart:** cot 1-3 points vs inf 25-91 — **LEGIT** (2-month history); `mix` empty here ties to the mix_summary gap.
- **partner_analytics_monthly:** cot 267KB, real, 4 periods (`periods`+`views`) vs inf 74 monthly `rows` — fewer periods is **LEGIT** (short history); structure differs but not hollow.

## Verdict
- **NOT silently-faked/degraded across the board** — cot's core served analytics (AUA, NNA-top-level, mix-current, partner_analytics, timeseries) are real and correct for a ~2-month-old, advisor-unassigned firm.
- **REAL GAPS to fix (cot-pipeline, snapshot-computable, not explained by history/advisors):** mix_summary `concentration`/`composition` empty; missing `top_holdings`, `concentration_risk`, `firm_composition`/`firm_concentrations`, `client_directory`, full `clients_tab`, `account_distribution` in header_metrics. The snapshot pipeline produces the time-series + AUA + top-level mix but NOT the current-holdings DETAIL analytics.
- **Data-completeness question (separate):** cot all-Unassigned advisors — is Cottonwood's advisor-assignment dimension meant to be loaded? If yes, that's a silver/dimension gap upstream of the missing advisor tree.

## Routing
cot-pipeline owner (via CTO/COO): the snapshot-computable-but-missing current analytics (concentration/composition/top_holdings/concentration_risk/firm_composition/client_directory). The stale C_00/C_02 dispatch refs (separate finding, comp-orphans) are the legit snapshot-native leftovers. Advisor-assignment completeness = a data question for Andrew/COO.
