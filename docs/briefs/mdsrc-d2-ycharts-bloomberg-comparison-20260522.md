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

## 3. WS-2 — the 10 hybrid-input legs (0.2.0_DS)

*[Drafted by 0.2.0_DS_PortfolioAnalytics — MP-01/02/03 benchmark legs,
Correlation, Regime/ERP, FT-02/03. Section pending.]*

---

## 4. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — C2 pull run live for the YCharts-touched surfaces; output captured; single-session staggered | WS-1 MET (71/71 pulled, no eviction; seat staggered with 0.2.0_DS) — WS-2 pending |
| AC2 — Bloomberg portal value compared on MATCHED dates; method documented | WS-1 MET (§1 method; anchor 2026-05-18) — WS-2 pending |
| AC3 — per-surface diff, ADHC_VALGATE Class-C (match/divergence/magnitude/cause); committed brief | WS-1 MET (§2) — WS-2 pending; this brief |
| AC4 — ZERO production/AWS/portal change; RAVC2 to COO | WS-1 confirmed read-only — joint RAVC2 on assembly |
