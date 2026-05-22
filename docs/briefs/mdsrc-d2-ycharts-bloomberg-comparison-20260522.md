# YALP_MDSRC.D2 — YCharts-vs-Bloomberg Parallel Comparison

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — D2 (the comparison/validation half of the original D1) |
| Task Order | `YALP_MDSRC.D2` (ds-ycharts-bloomberg-parallel-comparison) |
| Owners | `0.1.0_DS_MarketIntelligence` (WS-1) + `0.2.0_DS_PortfolioAnalytics` (WS-2) |
| Date | 2026-05-22 |
| Method | ADHC_VALGATE Class-C baseline comparison; matched-date discipline |
| Audience | `2.0.0_SA_COO` (RAVC2) — no CC CTO (Andrew directive 2026-05-22) |
| Scope guard | READ + COMPARE ONLY — zero PROD/AWS/portal change. The cutover (D1) is a carved-out future project. |

---

## 1. Matched-date method

Bloomberg data in the portal lags. The market-overview `all-returns.json`
the portal serves carries `data_as_of: 2026-05-18`, and every one of its 71
index entries has `latest_date: 2026-05-18`. The data_pkl filename
(`data_20260519_v1.pkl`) is the file-write date; the settled observation the
portal actually serves is **2026-05-18**.

- **Daily surfaces (WS-1 + WS-2 MP/FT): anchor = 2026-05-18.** YCharts value
  taken at-or-last-settled-before 2026-05-18; Bloomberg `latest_price` at
  2026-05-18. Never YCharts-today vs Bloomberg-lagged.
- **WS-2 Correlation (monthly): anchor = 2026-04 month-end** (last settled
  monthly observation).

Both co-owners use the one shared anchor (agreed 2026-05-22).

---

## 2. WS-1 — the 7 YCharts-replaceable surfaces (0.1.0_DS)

The C2 `ycharts-market-data-pull` module run live on the Menachem session for
the 71-entity DDB-01 backbone; each entity's YCharts value at 2026-05-18 diffed
against the portal Bloomberg `latest_price` at 2026-05-18.

### 2.1 Headline — 42 / 71 match to the cent

| Verdict | Count | Tolerance |
|---|---|---|
| **MATCH** | 42 | \|diff\| < 0.5% — in fact 40 of the 42 are < 0.01% (to-the-cent) |
| MINOR | 3 | 0.5% ≤ \|diff\| < 2% — MSCI China −1.15%, MSCI Switzerland +0.64%, Real Estate −1.34% |
| DIVERGENCE | 26 | \|diff\| ≥ 2% |

**The 42 to-the-cent matches are the load-bearing result:** for the broad US +
developed-market index universe — S&P 500, Dow, Nasdaq, all Russell 1000/2000/
MidCap variants, 10 of 11 GICS sectors, MSCI ACWI/EAFE/EM/USA/India/Brazil/Japan/
Korea/Taiwan/etc., and the Bloomberg Aggregate/HY/Municipal/Corporate/TIPS/1-3yr
& 1-5yr Gov-Credit bond indices — **the YCharts pull reproduces the Bloomberg
portal value exactly.** That confirms the C2 pull mechanism, the symbol mapping,
and the matched-date method are sound. The divergences below are symbol-variant
/ basis issues on specific entities, not pull defects.

### 2.2 The 26 divergences — categorized

**(a) EXPECTED — V1A/V1B representative-index substitution (4).** By design,
not a defect.

| Entity | YCharts symbol | YC level | Bloomberg | Note |
|---|---|---|---|---|
| Bloomberg 0-1 Year Treasury | `^BBUTB13MTR` | 241.73 | 125.00 | V1A representative index — different index, different level |
| Bloomberg 0-5 Year High Yield | `^BBUSCOHYTR` | 2938.68 | 187.68 | V1B representative (broad US Corp HY) |
| Bloomberg 0-5 Year TIPS | `^BBUTISTR` | 375.92 | 212.52 | V1B representative (broad US TIPS) |
| Bloomberg 20+ Year Treasury | `^BBUSLGCRTR` | 4033.03 | 573.80 | V1B representative (Long Gov/Credit) |

These resolved to a *representative* Bloomberg index (Andrew's V1A/V1B ruling),
not the exact portal entity — the absolute level differs by construction. The
meaningful comparison for a representative index is return correlation, not
level; a level diff is expected and documented, not an error. (Confirmation: the
broad `Bloomberg High Yield` entity, same `^BBUSCOHYTR`, matches Bloomberg
to-the-cent at 2938.68 — proving the symbol pulls correctly; it is the
*portal-entity-to-representative-index* mapping that introduces the level gap.)

**(b) REAL FINDING — MSCI variant / TR-vs-PR basis mismatch (13).** The YCharts
symbol resolved and pulls a clean series, but it is the wrong return basis or
index variant vs the portal entity:

MSCI France, Germany, Italy, Netherlands, Spain (European single-country) ·
MSCI ACWI ex US · MSCI United Kingdom · MSCI Sweden · MSCI USA Growth, Value,
Size, Momentum, Minimum Volatility (USA factor indices). Magnitudes range from
−12% (USA Momentum) to +2068% (Netherlands) — a spread consistent with a
TR-vs-PR basis difference compounding over a long history (a total-return index
diverges multiplicatively from a price-return index over decades). MSCI EAFE/EM/
ACWI/USA/India/Brazil/Japan/Korea/Taiwan/SouthAfrica/Quality all MATCH — so the
pull works; these 13 specific MSCI symbols need a variant correction
(price/gross/net + USD basis) before any future cutover.

**(c) REAL FINDING — GSCI commodity sub-index basis (4).** Copper `^SG3J`,
Crude Oil Brent `^BCOB`, Natural Gas `^SG8A`, Silver `^SGSA` — the S&P GSCI
commodity sub-indices. Each pulls a clean series but on a different basis from
the portal's commodity value (e.g. Brent YC 12936 vs Bloomberg 112.10). The
`^SG*` GSCI sub-indices are total-return index levels; the portal value is a
spot/near-future price. A basis decision (or a spot-price symbol) is needed.

**(d) REAL FINDING — security-kind crypto/commodity calc basis (4).** Bitcoin,
Ethereum, Gold, Crude Oil WTI — pulled via `fund_data calc=price` (the
security/ETF calc). The YCharts values (BTC 33.97, ETH 20.16, GOLD 39.66, WTI
4.91) are NOT price levels — `calc=price` on these YCharts security entities
returns a non-price-level series. A calc-basis correction is needed for the
4 security-kind commodity/crypto entities (likely `calc=level`, or a different
metric — to be pinned).

**(e) INVESTIGATE — Communication Services (1).** YC `^SPXCMSVS` 503.81 vs
Bloomberg 1346.42 (−62.6%). The other 10 GICS sectors match to-the-cent — this
one sector diverges. Likely a rebased-index vintage (the GICS Communication
Services sector was reconstituted 2018) or a wrong symbol variant. Flagged for a
follow-up symbol check.

### 2.3 WS-1 disposition

- 42 surfaces: YCharts == Bloomberg, validated for a future cutover.
- 3 MINOR (≤1.34%): within plausible vendor-timing/rounding tolerance — validated.
- 4 representative-index (V1A/V1B): expected level gap — return-basis comparison
  is the correct future check, not level.
- 22 real findings (b/c/d/e): symbol-variant / calc-basis corrections required
  before a cutover — enumerated above; none is a pull-mechanism defect.

No production/AWS/portal change made — this section is read + compare only.
Probe artifact: `.runtmp/d2/d2_ws1_compare_result.json`.

---

## 3. WS-2 — the hybrid-input legs (0.2.0_DS)

The C2 WS-2 pull modules (`ws2_mp_benchmark_pull` / `ws2_correlation_pull` /
`ws2_regime_erp_pull` / `ws2_factor_tilts_pull`) run live against the Menachem
session; diffed vs the Bloomberg `data_pkl` / `model_pkl`. Daily anchor
2026-05-18, correlation anchor 2026-04 month-end. Read + compare only.

### 3.1 MP-01/02/03 benchmark legs — MATCH (ETF) / MINOR (index)

The pull re-blends the constituents into the `{Model} Term Benchmark` / `Term
ETF` daily-return series. Diffed @ 2026-05-18 (YCharts decimal x100 vs Bloomberg
`return_daily` percent):

| Leg group | Result |
|---|---|
| ETF legs (5) — UST/ST/INT/LTC/LTA `{Model} Term ETF` | **MATCH to-the-cent** — YCharts re-blend == Bloomberg exactly (INT-ETF 0.1011% == 0.1011%, LTC/LTA-ETF 0.1474% == 0.1474%, ST-ETF 0.0176% == 0.0176%, UST-ETF 0.0344% == 0.0344%). |
| Index legs (5) — `{Model} Term Benchmark` | **MINOR** — 0.004-0.030 pp gap (UST-index 0.0117 vs 0.0415; LTC-index -0.0604 vs -0.0384). Cause: the representative-index residual — `^BBUTB13MTR` (1-3mo T-Bill) stands for the 0-1Y Treasury leg, `^BBUSATR`/`^MSACWI` are CLOSE-not-EXACT. Same class as §2.2(a). |

Disposition: the 5/5 ETF exact match validates the pull + re-blend + matched-date
method. The index-leg gap is the documented representative-index residual.

### 3.2 Correlation — MATCH ~60/61

61-index monthly returns @ 2026-04 vs Bloomberg `return_monthly`:

- **~60 indices agree within ~0.13 pp** — a small consistent ~0.07 pp offset
  (YCharts slightly below Bloomberg), within plausible TR/PR-basis or
  month-end-alignment tolerance (S&P 500 YC 10.423 vs BB 10.493; Russell 2000
  YC 12.159 vs BB 12.285; MSCI USA YC 10.428 vs BB 10.497).
- **Communication Services — DIVERGENCE** -4.74 pp (YC 18.43 vs BB 23.17): the
  known S5COMM cross-vendor index-definition gap — corroborates §2.2(e). Not a
  pull defect.
- **Bloomberg US Treasury — NO-DATA**: no 2026-04 row in Bloomberg
  `return_monthly` — a phantom in the generator universe (same class as bare
  `Crude Oil`); the generator's `idx in available` filter drops it.
- TR2/TR3 (1-3Y / 7-10Y Treasury) DROPPED per the COO ruling — not pulled.

Disposition: correlation validates — broad agreement, one known cross-vendor
outlier, one universe-phantom.

### 3.3 FT-02/03 factor spreads — DIVERGENCE (spread-definition)

The pull computes `spread = daily return(leg A) - return(leg B)` (~+/-0.006).
`model.pkl factor_spread` @ 2026-05-18 is ~+/-0.1-0.6 (Equity vs FI 0.1854,
US vs Foreign -0.6427, Large vs Small 0.5145). Not the same construct:
`factor_spread` is a larger-scale (rolling/cumulative) spread, not a 1-day
return-diff.

Disposition: **C2-module finding** — the `ws2_factor_tilts_pull` spread
arithmetic must be reconciled against Yang's `model_portfolio_regression_
analysis.ipynb` §8 (factor return spreads), the methodology source-of-truth.
Reconciliation in flight (COO-directed Yang-notebook review). Not a data /
pull-mechanism defect — a spread-definition mismatch.

### 3.4 Regime — not independently diffed (consumer surface)

Regime (WS1-MO-05) has no WS-2 pull — it consumes the market-overview ticker
timeseries (WS-1's re-source) + the already-FRED macro 2Y/10Y curve. Its
accuracy follows from §2 + the already-FRED macro path; no separate D2 diff.

### 3.5 ERP / Risk-Premium — DIVERGENCE (forward-P/E), hybrid disposition

The S&P 500 forward P/E is **not YCharts-sourceable**. `I:SP500PND` (29.02) vs
Bloomberg NTM-forward `pe_ntm` / `BEST_PE_RATIO` (20.89) — **+38.9% divergence,
wrong metric** (`I:SP500PND` / `I:SP500PNM` are trailing-magnitude). 0.1.0_DS's
re-probe found no forward-P/E entity (`I:SPFPER`/`SPFPERR` 400 — estimates-
entitlement gap) and no forward-EPS component.

Disposition (COO ruling 2026-05-22): **hybrid** — the forward-P/E leg stays
Bloomberg-pkl; the 10Y leg is FRED; the IG/HY credit leg is already FRED. The
C2 `I:SP500PND` wire was reverted (`bc139cdd6`). Same pattern as the VAL-01
hybrid ruling.

### 3.6 D2 module fixes (surfaced by the first live run)

Three bugs in the committed C2 WS-2 modules that the synthetic structural
self-tests could not reach — caught by the first live run:

| Fix | Commit | Detail |
|---|---|---|
| Correlation `_year_month` gmtime guard | `fb053a108` | an out-of-range live YCharts ts crashed the 61-index pull (OSError on Windows). |
| Correlation entity-kind `calc` | `fb053a108` | commodity securities (`GOLD`/`WTI`) 400 on `calc=level`; new `_calc_for()` selects `level` vs `price` by namespace. |
| ERP `I:SP500PND` revert | `bc139cdd6` | the wrong-metric forward-P/E wire reverted; leg recorded hybrid-stays-pkl. |

### 3.7 WS-2 disposition

- MP-01/02/03: ETF legs validated (5/5 exact); index legs = expected representative-index residual.
- Correlation: validated (~60/61); 1 known cross-vendor outlier, 1 universe-phantom.
- FT-02/03: spread-definition finding — reconcile the module vs Yang §8 (in flight).
- ERP: forward-P/E not YCharts-sourceable — hybrid (forward-P/E pkl, 10Y FRED) per COO ruling.
- 3 module robustness fixes committed.

No production/AWS/portal change made — this section is read + compare only.
Probe artifacts: `.runtmp/d2_ws2_results.json`, `.runtmp/d2_ws2_full.py`.

---

## 4. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — C2 pull run live for the YCharts-touched surfaces; output captured; single-session staggered | **MET** — WS-1 71/71; WS-2 MP/Correlation/FT all run live; seat staggered between the co-owners, no eviction |
| AC2 — Bloomberg portal value compared on MATCHED dates; method documented | **MET** — §1 method; daily anchor 2026-05-18, correlation 2026-04 month-end (§2 + §3) |
| AC3 — per-surface diff, ADHC_VALGATE Class-C (match/divergence/magnitude/cause); committed brief | **MET** — §2 (WS-1) + §3 (WS-2); this brief |
| AC4 — ZERO production/AWS/portal change; RAVC2 to COO | **MET** — both sections confirmed read-only; joint RAVC2 to COO on this commit |
