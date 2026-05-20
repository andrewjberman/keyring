# YALP_MDSRC — YCharts Ticker Map + Universe-Wide Fidelity (v0.3-ready artifact)

**Date:** 2026-05-20 (overnight session)
**Author:** 0.1.0_DS_MarketIntelligence
**Companion to:** `docs/briefs/mdsrc-ycharts-master-reconnaissance-20260520.md`
**Purpose:** the portal-universe -> YCharts-symbol mapping table + a universe-wide data-fidelity check. Directly feeds the v0.3 migration implementation.
**Machine-readable map:** `docs/briefs/mdsrc-ycharts-ticker-map-20260520.csv`

---

## 1. Summary

The portal's market-data backbone is the DynamoDB `opal-portal-market-data` table — **71 entities** (53 INDEX, 11 BOND_INDEX, 7 COMMODITY). This artifact maps each to its YCharts symbol and validates the data against a live YCharts pull.

| | Count | |
|---|---|---|
| Mapped to YCharts symbol | **53 / 71** | full map in the CSV |
| — of which **high-fidelity** (1Y gap <= 6 pt vs portal) | **44 / 53 (83%)** | YCharts is a faithful substitute |
| — of which **variant-review needed** (gap 6–34 pt) | **9 / 53** | §3 — the variant-pinning problem, in action |
| Unmapped residue | **18 / 71** | §4 — needs manual mapping (commodities, crypto, ambiguous Bloomberg bonds) |

**Bottom line:** for 44 of 53 mapped tickers — including S&P 500, every Russell index, every GICS sector, MSCI EAFE/EM/USA, and the core Bloomberg bond indices — YCharts 1Y returns match the portal's current Bloomberg-pkl values within ~1–3 points (consistent with a 2-day as-of gap). **A YCharts-sourced market-data feed is data-equivalent for the bulk of the portal universe.** The 9 wide cases and the 18-ticker residue are the v0.3 implementation work — and they are exactly the variant-pinning risk the master brief flagged, now demonstrated concretely.

---

## 2. High-fidelity confirmation (44 tickers)

Across the 44 CLOSE tickers the 1Y gap is overwhelmingly 0–3 points, portal consistently a touch higher (consistent with the portal snapshot being 2 days stale vs the live YCharts pull). Sample:

| Portal name | YCharts | Portal 1Y | YCharts 1Y | Gap |
|---|---|---|---|---|
| S&P 500 | `^SPX` | +25.7% | +24.8% | 0.9 |
| Russell 2000 | `^RUT` | +33.1% | +32.2% | 0.9 |
| MSCI Emerging Markets | `^MSEM` | +45.4% | +44.0% | 1.4 |
| Information Technology (GICS) | `^SPXIFTS` | +44.6% | +43.6% | 1.0 |
| Bloomberg US Aggregate | `^BBUSATR` | +4.4% | +4.1% | 0.3 |
| MSCI EAFE | `^MSEAFE` | +22.4% | +21.2% | 1.3 |

This is the universe-scale confirmation of the master brief's Phase-C finding (which sampled 5 indices). It holds broadly.

---

## 3. Variant-review cases (9 tickers) — the variant-pinning problem, demonstrated

These 9 tickers diverge 6–34 pt. The mapping auto-picked *a* YCharts symbol of the right name family, but not necessarily the exact variant the portal tracks. This is the master brief's flagged #1 migration risk — here it is, concrete:

| Portal name | Auto-mapped | Portal 1Y | YCharts 1Y | Gap | Likely cause |
|---|---|---|---|---|---|
| Portal name | Auto-mapped | Portal 1Y | YCharts 1Y | Gap | Note |
|---|---|---|---|---|---|
| MSCI South Korea | `^MSKR` | +257.6% | +223.9% | 33.7 | The +257.6% portal value is *consistent with* a large-cap-tilted Korea variant — `^MSKRLCAP` (MSCI Korea Large Cap) reads +255.95% — vs plain MSCI Korea `^MSKR` at +223.9%. **Candidate, NOT confirmed** — see §3.1. |
| Communication Services | `^SPXCMSVS` | +68.6% | +43.6% | 25.0 | Probable mis-mapped GICS-sector variant. |
| S&P GSCI | `^GNX` | +43.6% | +63.5% | 19.9 | Commodity-index return-basis variant (GSCI Spot vs Excess Return vs Total Return are distinct series). |
| MSCI Japan | `^MSJP` | +43.4% | +31.8% | 11.7 | Name-matched but variant-divergent — the portal "MSCI Japan" is not YCharts' plain `^MSJP`. |
| MSCI India | `^MSIN` | -1.4% | -12.6% | 11.2 | As above. |
| MSCI Australia | `^MSAU` | +5.6% | +16.4% | 10.8 | As above. |
| MSCI Taiwan | `^MSTW` | +107.2% | +97.2% | 10.1 | As above; Taiwan very volatile. |
| MSCI South Africa | `^MSZA` | +33.8% | +42.2% | 8.4 | As above. |
| MSCI Switzerland | `^MSCH` | +10.9% | +17.4% | 6.5 | As above. |

### 3.1 Variant resolution cannot be reverse-engineered from return-matching (methodological finding)

An obvious-looking shortcut — for each wide case, search the 33,997-member YCharts MSCI family for the variant whose 1Y return is *closest* to the portal's — was attempted and **fails**. With ~34k candidates, some index always has a coincidentally-matching return: a closest-1Y search returned "MSCI Japan" -> "MSCI AC Pacific **Ex Japan** SMID Cap" and "MSCI Brazil" -> "MSCI Emerging Markets Latin America **ex Brazil**" — spurious matches of the *opposite* index. Return-matching across a large family overfits.

**Consequence:** the fidelity check is a sound *verification* gate (does a name-derived mapping hold?) but it **cannot be the *derivation* method** for variant selection. The correct mapping authority is the **yang-pipeline's own source-side ticker definitions** — the exact MSCI/Bloomberg variant codes that Yang's `data_pkl` Bloomberg export uses. Those codes (in the yang-pipeline config / Yang's Bloomberg terminal export) tell you *which* MSCI Japan / Korea / GSCI variant the portal actually tracks; YCharts is then queried for that specific variant and the fidelity check confirms. **Derivation source (yang-pipeline ticker codes) is not the same as the verification gate (fidelity check)** — conflating them produces nonsense.

So even the `^MSKRLCAP` Korea remap above is a *candidate* (plausible by name + number), not a confirmed mapping — confirmation requires the yang-pipeline source-side code for that ticker.

**Pattern:** the 9 wide cases are single-country MSCI / commodity / sector indices that share a *name* with a YCharts index but are a different *variant*. **Implication for v0.3:** the 71-row mapping must be derived from the yang-pipeline ticker definitions, then fidelity-verified — not name-matched-and-hoped. An automated name-match silently mis-maps ~17% of the universe by 6–34 points.

---

## 4. Unmapped residue (18 tickers) — v0.3 manual mapping

Not cleanly auto-mappable from the YCharts index families captured this session:

| Type | Tickers | Why unmapped / path |
|---|---|---|
| COMMODITY (6) | Gold, Silver, Copper, Crude Oil WTI, Crude Oil Brent, Natural Gas | YCharts commodities are not in an `indexFamily`; they sit under a different symbol scheme (commodity spot / futures). Needs a YCharts commodity-symbol lookup. |
| INDEX — crypto (2) | Bitcoin, Ethereum | YCharts crypto symbols — separate asset class. |
| BOND_INDEX (8) | Bloomberg 0-1 Yr Treasury, 20+ Yr Treasury, 1-3 Yr Gov/Credit, 1-5 Yr Gov/Credit, 0-5 Yr High Yield, 0-5 Yr TIPS, Bloomberg TIPS, Bloomberg High Yield | The 506-member Bloomberg family carries dozens of currency/hedged/maturity variants; the portal's short names need pinning to the exact USD-unhedged US variant. Tractable, but per-name judgment — exactly the variant-review discipline of §3. |
| INDEX (2) | MSCI ACWI ex US, MSCI USA Size | "MSCI ACWI ex US" -> "MSCI ACWI Ex USA" exists; "MSCI USA Size" has no clean YCharts equivalent of that exact name — needs vendor confirmation. |

None of these are blockers — they are v0.3 implementation tasks. The commodities + crypto (8 tickers) are the genuinely different-structure cases; the 10 bond/MSCI ones are name-variant pinning.

---

## 5. Recommendation for v0.3

1. The 71-row mapping table must be **derived from the yang-pipeline's source-side ticker definitions** — the exact MSCI/Bloomberg variant codes Yang's `data_pkl` Bloomberg export uses — NOT name-matched against YCharts and hoped (§3.1). Obtaining those codes (yang-pipeline config + Yang's Bloomberg export setup; AE 0.5.0 is the YALP-pipeline consult) is a prerequisite v0.3 task. The CSV here is a **starting draft** (53 rows, 44 fidelity-verified-close), not the final.
2. MSCI South Korea: the portal value indicates a large-cap-tilted Korea variant (`^MSKRLCAP` is the candidate, +255.95% vs plain `^MSKR` +223.9%) — confirm against the yang-pipeline source code, do not assume.
3. For each migrated ticker, the v0.3 acceptance test is this fidelity check: pull YCharts for the *derived* symbol, compare to the portal's current value, require the gap within an as-of-adjusted tolerance. The check VERIFIES a mapping; it does not DERIVE one.
4. Confirm with YCharts (alongside the API quote) that commodity + crypto symbols — and the index families generally — are in the API tier (the `pycharts` SDK shows no index client; §master-brief §6).

The map CSV (`mdsrc-ycharts-ticker-map-20260520.csv`) is the machine-readable companion — **71 rows** (the full portal universe): `entity_type, portal_name, bbg_ticker, ycharts_symbol_draft, ycharts_label_draft, portal_1Y_pct, ycharts_1Y_pct, gap_pt, fidelity`.

---

## 6. UNLOCK — the authoritative source-side ticker codes were found (no need to ask Yang)

§3.1 / §5 said the variant mapping must come from "the yang-pipeline's source-side ticker definitions" and treated obtaining them as an open v0.3 dependency requiring Yang / an AE 0.5.0 consult. **They were already in S3.** Yang's `data_pkl` (`s3://opal-data-portal-v2/benchmarks/data_20260519_v1.pkl`) — the raw Bloomberg export the whole portal market-data layer is built from — carries a **`bbg_ticker` column**. Its `return_daily` DataFrame is `[date, index_name, bbg_ticker, price, return, price_return]`.

**Every one of the 71 portal entities now has its exact Bloomberg ticker** (in the rebuilt CSV). Examples:

| Portal name | Bloomberg ticker | What it definitively is |
|---|---|---|
| MSCI South Korea | `MXKR Index` | the standard MSCI Korea index (resolves the §3 ambiguity — it is NOT a "Large Cap" variant; `^MSKRLCAP` was a wrong candidate) |
| Communication Services | `S5COMM Index` | S&P 500 Communication Services GICS sector index |
| Bloomberg Aggregate | `LBUSTRUU Index` | Bloomberg US Aggregate, Total Return, Unhedged USD (`TRUU` suffix) |
| S&P GSCI | `SPGSCI Index` | S&P GSCI (the headline index) |
| Gold / Bitcoin | `XAU BGN Curncy` / `XBTUSD BGN Curncy` | Bloomberg spot quotes |
| Crude Oil WTI | `CL1 Comdty` | front-month WTI future |

**This converts the project's #1 risk from open to tractable.** The v0.3 mapping task is no longer "guess which MSCI/commodity variant the portal tracks" — it is the **deterministic** task "map a known Bloomberg ticker to its YCharts equivalent." Each Bloomberg ticker identifies exactly one index; YCharts' crosswalk for Bloomberg tickers (or a per-ticker lookup) closes it, and the §2 fidelity check verifies.

**Two further wins from the same file:**
- The `data_pkl` `return_daily` has **both `return` and `price_return`** columns — the total-return-vs-price-return basis question (§3 / master brief §5) is resolved at the source: the pipeline carries both; v0.3 simply pins which column the portal heatmap consumes and queries the matching YCharts metric.
- `return_monthly` carries the valuation columns (`dy, eps_ltm, eps_ntm, ev_sales, pb, pe_ltm, pe_ntm, pfcf, lt_growth`) — the Valuation page's exact source fields, also Bloomberg-ticker-keyed.

**Revised §5 recommendation #1:** the v0.3 mapping is built from the `bbg_ticker` column of `data_pkl` (committed here as the CSV's `bbg_ticker` field) crosswalked to YCharts — a bounded, deterministic, fidelity-verifiable task. The "ask Yang" dependency is removed.
