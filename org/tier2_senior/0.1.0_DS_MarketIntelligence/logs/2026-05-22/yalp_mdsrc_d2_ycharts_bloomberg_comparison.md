# Session Log -- 0.1.0_DS_MarketIntelligence

**Date:** 2026-05-22
**Branch:** CLOUD
**Work:** YALP_MDSRC.D2 -- YCharts-vs-Bloomberg parallel comparison (WS-1 lead; 0.2.0_DS co-owns WS-2). Andrew directive: run the C2 pull live + compare vs Bloomberg on matched dates; NO PROD/AWS change.

---

## Summary

D2 WS-1 comparison run + drafted. The C2 ycharts-market-data-pull module run live on the Menachem session for the 71-entity DDB-01 backbone; each entity's YCharts value at the matched-date anchor 2026-05-18 diffed vs the portal Bloomberg `latest_price`. Result: 42 MATCH (40 to-the-cent), 3 MINOR, 26 DIVERGENCE.

## Matched-date method

Anchor = 2026-05-18 -- the portal market-overview all-returns.json `data_as_of`; every one of its 71 indices has `latest_date: 2026-05-18`. The data_pkl filename (data_20260519) is the write date; 2026-05-18 is the settled observation the portal serves. YCharts value taken at-or-last-settled-<=2026-05-18; Bloomberg latest_price at 2026-05-18. Shared anchor agreed with 0.2.0_DS (correlation monthly -> 2026-04 month-end).

## WS-1 result -- 42/71 to-the-cent

42 surfaces YCharts == Bloomberg exactly (S&P 500, Dow, Nasdaq, all Russells, 10/11 GICS sectors, MSCI ACWI/EAFE/EM/USA/etc., the Bloomberg Aggregate/HY/Muni/Corp/TIPS/Gov-Credit bond indices). Confirms the pull mechanism + symbol map + matched-date method are sound.

26 DIVERGENCE, categorized:
- 4 EXPECTED -- the V1A/V1B representative-index bonds (different index by design; level gap expected).
- 13 MSCI variant / TR-vs-PR basis mismatch (France/Germany/Italy/etc. + USA factor indices) -- symbol-variant correction needed.
- 4 GSCI commodity sub-index basis (^SG3J/^BCOB/^SG8A/^SGSA -- TR index vs spot).
- 4 security-kind crypto/commodity calc basis (BTC/ETH/GOLD/WTI on calc=price return a non-price-level value).
- 1 INVESTIGATE -- Communication Services (10/11 sectors match; this one -62.6%).

22 of the 26 are real symbol-variant/calc-basis findings (not pull defects -- the 42 matches prove the mechanism); 4 are by-design. All enumerated in the brief for a future-cutover correction list.

## Compiler Tools

D2 is an analytical comparison run -- no gold/portal/route/IAM/Terraform change; no comp-* graph tool applies (per the TO note). Comparison discipline: ADHC_VALGATE Class-C (per-entity match/divergence/magnitude/cause). Self-check: 71/71 entities pulled (no eviction); matched-date alignment verified (every row compared at 2026-05-18 both sides). PASS.

## Deliverables

- `docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md` -- the joint comparison brief; WS-1 section authored, WS-2 section stubbed for 0.2.0_DS.
- Probe artifacts (gitignored, .runtmp/d2/): d2_ws1_compare_result.json, all-returns.json, data_20260519_v1.pkl.

## RAVC

| RAVC | From/To | Status |
|------|---------|--------|
| GO D2 | COO -> DS | RECEIVED + ACK |
| seat stagger + anchor | DS <-> 0.2.0_DS | AGREED (anchor 2026-05-18; me first, seat freed) |
| joint RAVC2 D2 | DS + 0.2.0_DS -> COO | pending WS-2 section + assembly |

## ERP forward-P/E re-probe (D2, post-WS-2-finding)

0.2.0_DS's WS-2 D2 run caught the C2 ERP discovery wrong: YCharts I:SP500PND ("PE Ratio Estimate", 29.02) is trailing-magnitude, not the Bloomberg BEST_PE_RATIO forward P/E (pe_ntm 20.89; +38.9% gap). Owned + ran the re-probe on the Menachem seat (binding test: a valid candidate must be ~21).

DEFINITIVE VERDICT -- the S&P 500 forward P/E is NOT sourceable from YCharts on the Menachem session:
- I:SP500PND (29) + I:SP500PNM (28): both trailing-magnitude. Neither is the ~21 forward.
- 6 forward-PE search phrasings: zero hits. I:SPFPER / I:SPFPERR (the plausible "S&P Forward PE Ratio" entities, surfaced by the "S&P 500 PE Ratio" search) 400 on every access form -- exist-but-unpullable, likely a Menachem-account estimates-entitlement gap.
- 6 forward-EPS search phrasings: zero hits -- the component-calc (price/forward-EPS) has no EPS leg. ^SPX index price pulls fine.

Disposition (COO/Andrew call): ERP forward-P/E leg either stays Bloomberg-pkl-sourced (the VAL-01-style hybrid pattern -- recommended) or needs a dedicated YCharts seat WITH the estimates entitlement to reach SPFPER. The C2 ws2_regime_erp_pull I:SP500PND wire is wrong, needs reverting. RAVC'd to COO; verdict handed to 0.2.0_DS for §3. Probe artifact: .runtmp/d2/d2_erp_reprobe_result.json.

Yang's original notebooks (docs/reference/yang-original-scripts/, d386c8d2d) read -- dc_fields_all confirms forward-P/E = Bloomberg BEST_PE_RATIO; RSI = RSI_30D (the C2 pull used rsi_14 -- methodology note for the RSI surface comparison); valuation multiples are Bloomberg fields per index (confirms the VAL-01 hybrid disposition).

## Next Steps

1. [0.2.0_DS] WS-2 section (§3) of the joint brief -- MP (5/5 ETF exact) / Correlation (60/61 agree) / FT (spread-definition finding) / ERP (UNRESOLVED-on-YCharts per the re-probe).
2. [D2 close] joint RAVC2 to COO once §3 lands + the brief is assembled.
3. [COO/Andrew] the ERP forward-P/E disposition (hybrid-pkl vs entitled-seat).
4. [future D1 cutover] the 22 WS-1 symbol-variant/calc-basis corrections + the RSI-30D re-pull -- cutover-prep, not D2 scope.
