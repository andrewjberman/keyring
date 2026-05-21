# YALP_MDSRC.M1 — Enumerated Macro Data Contract

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.4 WS-C |
| Task Order | `YALP_MDSRC.M1` (dsa-macro-data-contract-enumerate-and-source-map) |
| Author | `0.2.0_DS_PortfolioAnalytics` (reassigned from `~A`; F1 brief consumed as documented reference) |
| Date | 2026-05-21 |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO`; handed to `0.1.0_DS_MarketIntelligence` (TO-M2 verifier) |
| Status | COMPLETE — contract authored; **NOT self-certified** (R5: verifier != author — M2 validates) |
| Companion | `docs/briefs/mdsrc-m1-macro-data-contract-20260521.tsv` (machine-readable 81-row contract) |

---

## 1. Purpose

For **every** indicator the `yang-generate-macro` Lambda renders on the portal Macroeconomics
page, map it to its authoritative non-Bloomberg source. The contract is the WS-C deliverable
behind Andrew's "cannot forget one" requirement — it is exhaustive against the deployed
`MACRO_GROUPS` enumeration, and it does **not self-certify**: every verdict is a *candidate*
claim handed to TO-M2 (`0.1.0_DS`, a different agent + pod) for independent verify-channel
validation. No row is marked "confirmed."

---

## 2. Method + the count

- **Enumeration source (authoritative):** `infra/aws/lambda/v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py`, the `MACRO_GROUPS` dict (lines 28-134). This is the deployed code — it, not the PRD prose, is the contract's frame.
- **Starting input:** the F1 Bloomberg->FRED macro-sourcing audit (`docs/briefs/mdsrc-fred-macro-sourcing-audit-20260520.md` + companion TSV) — the FRED-replaceable subset. M1 extends it from a FRED-only mapping to the full multi-source contract (FRED / BLS / BEA / Census / Treasury / originating body / YCharts / proprietary).
- **Sources evaluated per indicator:** FRED, BLS, BEA, US Census, US Treasury, the Federal Reserve, the originating private body (ISM, S&P Global, Conference Board, NFIB, AAII, NAHB, NAR, U. Michigan, ADP, CBOE, ICE), and YCharts.

### 2.1 The count — 81, not "~91"

The PRD §7 / the M1 TO estimate "~91 indicators." **The deployed `MACRO_GROUPS` has exactly
81** (12 groups). This contract is exhaustive against the deployed code = **81 rows, none
dropped** (AC1). The "~91" was an estimate; 81 is the verified figure. Per-group:

| # | Group | Indicators |
|---|---|---|
| 1 | Leading Indicator | 8 |
| 2 | Lagging Indicator | 7 |
| 3 | Financial Condition | 6 |
| 4 | Inflation | 8 |
| 5 | Labor Market | 9 |
| 6 | Consumer | 7 |
| 7 | Housing Market | 7 |
| 8 | Investor Sentiment | 7 |
| 9 | Treasury Yields | 10 |
| 10 | Credit Spread | 5 |
| 11 | Market Indicator | 2 |
| 12 | Currency | 5 |
| | **Total** | **81** |

**Served vs configured.** `MACRO_GROUPS` configures 81; `macro_data.json` *serves* 79. Two
are configured-but-not-served — `S&P CoreLogic CS Home Price MoM` (idx 52) and `MOVE`
(idx 76) — because they have no `data_pkl` row and `yang-generate-macro` does a silent
`continue` (F1 finding F1). Both are in this contract (marked `served = NO`) — the contract
maps what the code enumerates, exhaustively, irrespective of the pkl-feed gap.

### 2.2 Verdict space + how it is applied

The TO verdict space is `FRED-replaceable | BLS | BEA | Census | Treasury |
originating-body-direct | YCharts | stays-Bloomberg-proprietary`. Applied as follows:

- **`FRED-replaceable`** — the series (or an accepted proxy) is on the free FRED API. FRED is
  a *redistributor* of government data; the candidate-sources column always also names the
  *originating authority* (BLS / BEA / Census / Federal Reserve / DOL / Treasury / U. Michigan).
  FRED is the recommended channel for all of these because it is free, a single uniform API,
  and **already integrated in this pipeline twice** (`ingest_yield_curve_fred.py`,
  `opal-portal-volatility-fetcher`, `refresh-fred-cache`). The standalone `BLS / BEA / Census`
  verdicts are therefore *unused* — every government series here is on FRED; going direct to
  the agency would be strictly worse. They remain available to M2 if verification finds a FRED
  gap.
- **`Treasury`** — used once (idx 21, Net Long-Term TIC Flows): FRED's TIC coverage is thin;
  the US Treasury publishes TIC free at treasury.gov. Originating *government* body, direct.
- **`originating-body-direct`** — the authoritative source is a private body (ISM, S&P Global,
  Conference Board, NFIB, AAII, NAHB, NAR, U. Michigan, ADP). No free *government* source
  exists. Each such row also carries `YCharts-if-carried` as the practical automation channel
  (see §4 — the originating-body feed is typically licensed; a free press-release headline is
  not ingestion-ready).
- **`stays-Bloomberg-proprietary`** — no free, government, originating-body, or vendor source
  reproduces the metric (Bloomberg FCI, Fed NLP, Ted Spread, Bloomberg Aggregate OAS, DXY,
  MOVE). An honest terminal verdict — not a failure (TO context).
- **`YCharts`** — appears as a *candidate* on all 25 no-free-government-source rows; not used
  as a sole verdict because M1 cannot self-certify YCharts coverage (M2 verifies).

---

## 3. The contract — 81 rows

Full machine-readable contract: **`mdsrc-m1-macro-data-contract-20260521.tsv`** (columns:
`idx, group, indicator, bbg_ticker, what_it_is, native_frequency, served, fred_series_id,
candidate_authoritative_sources, sourcing_verdict, m2_verify_note`). The group-by-group
verdict summary follows; per-row detail (Bloomberg ticker, description, frequency, FRED series
ID, candidate sources, M2 verify note) is in the TSV.

### 3.1 Group 1 — Leading Indicator (8) — 0 FRED

| idx | Indicator | Verdict |
|---|---|---|
| 1 | Leading Index (Conference Board LEI) | originating-body-direct (CB) / YCharts-if-carried |
| 2 | PMI Manufacturing (ISM) | originating-body-direct (ISM) / YCharts-if-carried |
| 3 | PMI Services (ISM) | originating-body-direct (ISM) / YCharts-if-carried |
| 4 | S&P PMI Manufacturing | originating-body-direct (S&P Global) / YCharts-if-carried |
| 5 | S&P PMI Services | originating-body-direct (S&P Global) / YCharts-if-carried |
| 6 | ISM Manufacturing New Orders | originating-body-direct (ISM) / YCharts-if-carried |
| 7 | ISM Services New Orders | originating-body-direct (ISM) / YCharts-if-carried |
| 8 | NFIB Small Business Optimism | originating-body-direct (NFIB) / YCharts-if-carried |

The entire group is licensed survey data — no government source. ISM withdrew from FRED in
2016. This is one of the two all-proprietary groups (F1 finding).

### 3.2 Group 2 — Lagging Indicator (7) — 7 FRED

| idx | Indicator | Verdict |
|---|---|---|
| 9 | GDP QoQ | FRED-replaceable (A191RL1Q225SBEA / BEA) |
| 10 | Industrial Productivity MoM | FRED-replaceable (INDPRO units=pch / Fed G.17) |
| 11 | Durable Goods Orders MoM | FRED-replaceable (DGORDER units=pch / Census) |
| 12 | Factory Orders MoM | FRED-replaceable (AMTMNO units=pch / Census M3) |
| 13 | Capacity Utilization | FRED-replaceable (TCU / Fed G.17) |
| 14 | Business Inventories YoY | FRED-replaceable (BUSINV units=pc1 / Census) |
| 15 | Trade Balance | FRED-replaceable (BOPGSTB / BEA + Census) |

100% FRED-replaceable group.

### 3.3 Group 3 — Financial Condition (6) — 4 FRED, 1 Treasury, 1 proprietary

| idx | Indicator | Verdict |
|---|---|---|
| 16 | Bloomberg Financial Condition Index | **stays-Bloomberg-proprietary** (Chicago Fed NFCI is the substitute already on the page) |
| 17 | Chicago Fed Financial Condition Index | FRED-replaceable (NFCI / Chicago Fed) |
| 18 | Fed Fund Rate | FRED-replaceable (FEDFUNDS / Federal Reserve) |
| 19 | Fed Balance Sheet | FRED-replaceable (WALCL / Fed H.4.1) |
| 20 | Fed Balance Sheet as % of GDP | FRED-replaceable (WALCL/GDP computed) |
| 21 | Net Long Term TIC Flows | **Treasury** (US Treasury TIC, ticdata) |

### 3.4 Group 4 — Inflation (8) — 7 FRED, 1 originating-body

| idx | Indicator | Verdict |
|---|---|---|
| 22 | CPI MoM | FRED-replaceable (CPIAUCSL units=pch / BLS) |
| 23 | Core CPI MoM | FRED-replaceable (CPILFESL units=pch / BLS) |
| 24 | PCE MoM | FRED-replaceable (PCEPI units=pch / BEA) |
| 25 | Core PCE MoM | FRED-replaceable (PCEPILFE units=pch / BEA) |
| 26 | PPI MoM | FRED-replaceable (PPIFIS units=pch / BLS) |
| 27 | Unit Labor Cost YoY | FRED-replaceable (ULCNFB units=pc1 / BLS) |
| 28 | UMich 1 Year Inflation | FRED-replaceable (MICH / U. Michigan) |
| 29 | UMich 5-10 Year Inflation | **originating-body-direct** (U. Michigan — FRED carries only the 1-yr) |

### 3.5 Group 5 — Labor Market (9) — 8 FRED, 1 originating-body

| idx | Indicator | Verdict |
|---|---|---|
| 30 | Unemployment Rate | FRED-replaceable (UNRATE / BLS) |
| 31 | Initial Jobless Claims | FRED-replaceable (ICSA / DOL ETA) |
| 32 | Continuing Jobless Claims | FRED-replaceable (CCSA / DOL ETA) |
| 33 | US Job Openings | FRED-replaceable (JTSJOL / BLS JOLTS) |
| 34 | Nonfarm Payrolls | FRED-replaceable (PAYEMS units=chg / BLS) |
| 35 | ADP Employment Change | **originating-body-direct** (ADP) / YCharts-if-carried |
| 36 | Labor Force Participation Rate | FRED-replaceable (CIVPART / BLS) |
| 37 | Weekly Hours | FRED-replaceable (AWHAETP / BLS) |
| 38 | Hourly Earnings MoM | FRED-replaceable (CES0500000003 units=pch / BLS) |

### 3.6 Group 6 — Consumer (7) — 6 FRED, 1 originating-body

| idx | Indicator | Verdict |
|---|---|---|
| 39 | Retail Sales MoM | FRED-replaceable (RSAFS units=pch / Census) |
| 40 | Retail Sales ex Auto MoM | FRED-replaceable (RSFSXMV units=pch / Census) |
| 41 | Retail Sales ex Auto and Gas MoM | FRED-replaceable (MARTSSM44X72USS units=pch / Census) |
| 42 | UMich Consumer Sentiment | FRED-replaceable (UMCSENT / U. Michigan) |
| 43 | Conference Board Consumer Confidence | **originating-body-direct** (CB) / YCharts-if-carried |
| 44 | Consumer Credit YoY | FRED-replaceable (TOTALSL units=pc1 / Fed G.19) |
| 45 | Wards Total Vehicle Sales | FRED-replaceable (TOTALSA / BEA-Wards) |

### 3.7 Group 7 — Housing Market (7) — 5 FRED, 2 originating-body

| idx | Indicator | Verdict |
|---|---|---|
| 46 | NAHB Housing Market Index | **originating-body-direct** (NAHB) / YCharts-if-carried |
| 47 | New Home Sales | FRED-replaceable (HSN1F / Census) |
| 48 | Existing Home Sales | FRED-replaceable (EXHOSLUSM495S / NAR via FRED) |
| 49 | Pending Home Sales | **originating-body-direct** (NAR — FRED has Existing, not Pending) / YCharts-if-carried |
| 50 | Housing Starts | FRED-replaceable (HOUST / Census) |
| 51 | Building Permits | FRED-replaceable (PERMIT / Census) |
| 52 | S&P CoreLogic CS Home Price MoM | FRED-replaceable (CSUSHPINSA units=pch) — `served = NO` (config'd, dropped) |

Note idx 52: the TO context listed Case-Shiller among the expected proprietary residue, but
F1 established empirically that **S&P/CoreLogic licenses Case-Shiller TO FRED** — FRED carries
it free (`CSUSHPINSA`). The contract follows the empirical finding: FRED-replaceable. M2 to
confirm the exact series (20-City SA vs NSA).

### 3.8 Group 8 — Investor Sentiment (7) — 0 FRED

| idx | Indicator | Verdict |
|---|---|---|
| 53 | AAII Sentiment Bullish | originating-body-direct (AAII) / YCharts-if-carried |
| 54 | AAII Sentiment Neutral | originating-body-direct (AAII) / YCharts-if-carried |
| 55 | AAII Sentiment Bearish | originating-body-direct (AAII) / YCharts-if-carried |
| 56 | AAII Stock Allocation | originating-body-direct (AAII) / YCharts-if-carried |
| 57 | AAII Bond Allocation | originating-body-direct (AAII) / YCharts-if-carried |
| 58 | AAII Cash Allocation | originating-body-direct (AAII) / YCharts-if-carried |
| 59 | Fed NLP Sentiment | **stays-Bloomberg-proprietary** (no public/vendor source) |

The second all-proprietary group: AAII x6 (licensed survey; aaii.com semi-public) + Fed NLP
(genuine Bloomberg proprietary residue).

### 3.9 Group 9 — Treasury Yields (10) — 10 FRED

idx 60-69 — all ten tenors (1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y) — **FRED-replaceable**
(`DGS*` series; US Treasury CMT is the originating authority — also published free at
treasury.gov). Already proven in-pipeline by `yield_curve_fred.json`. 100% FRED.

### 3.10 Group 10 — Credit Spread (5) — 3 FRED-proxy, 2 proprietary

| idx | Indicator | Verdict |
|---|---|---|
| 70 | Ted Spread | **stays-Bloomberg-proprietary** (FRED TEDRATE discontinued 2022-01; BSBY-based) |
| 71 | AAA | FRED-replaceable (BAMLC0A1CAAA — ICE BofA proxy, MEDIUM fidelity) |
| 72 | IG | FRED-replaceable (BAMLC0A0CM — ICE BofA proxy; already cached by `refresh-fred-cache`) |
| 73 | AGG | **stays-Bloomberg-proprietary** (Bloomberg US Aggregate index OAS, licensed) |
| 74 | HY | FRED-replaceable (BAMLH0A0HYM2 — ICE BofA proxy; already cached) |

The three FRED-replaceable rows are **proxies** — ICE BofA OAS index families differ slightly
from Bloomberg index OAS. M2/the implementation TO must confirm the divergence is acceptable
for a heatmap-grade metric.

### 3.11 Group 11 — Market Indicator (2) — 1 FRED, 1 proprietary

| idx | Indicator | Verdict |
|---|---|---|
| 75 | VIX | FRED-replaceable (VIXCLS / CBOE — already used by `volatility_data.json`) |
| 76 | MOVE | **stays-Bloomberg-proprietary** (ICE-licensed) — `served = NO`; NOTE: `opal-portal-volatility-fetcher` already sources MOVE from Yahoo Finance `^MOVE` for the Volatility tab |

### 3.12 Group 12 — Currency (5) — 4 FRED, 1 proprietary

| idx | Indicator | Verdict |
|---|---|---|
| 77 | DXY | **stays-Bloomberg-proprietary** (ICE US Dollar Index, licensed; FRED DTWEXBGS is a different basket — NOT a drop-in) |
| 78 | EUR/USD | FRED-replaceable (DEXUSEU / Fed H.10) |
| 79 | USD/JPY | FRED-replaceable (DEXJPUS / Fed H.10) |
| 80 | GBP/USD | FRED-replaceable (DEXUSUK / Fed H.10) |
| 81 | USD/CNH | FRED-replaceable (DEXCHUS — onshore CNY proxy, MEDIUM fidelity) |

---

## 4. The proprietary-vs-replaceable split (AC3)

| Verdict | Count | % of 81 |
|---|---|---|
| FRED-replaceable | 55 | 68% |
| — of which clean (identical/transform) | 51 | |
| — of which proxy (MEDIUM fidelity: AAA, IG, HY, USD/CNH) | 4 | |
| Treasury (originating government body, direct) | 1 | 1% |
| originating-body-direct (private body; no free government source) | 19 | 23% |
| stays-Bloomberg-proprietary | 6 | 7% |
| **Total** | **81** | |

**The 25 indicators with NO free government source** (AC3 — every one explicitly resolved to
`YCharts-if-carried` or `stays-Bloomberg-proprietary`):

- **19 → originating-body-direct, YCharts-if-carried as the automation channel:** Leading
  Index, ISM PMI Mfg/Svc, S&P PMI Mfg/Svc, ISM New Orders Mfg/Svc, NFIB (8); UMich 5-10yr (1);
  ADP (1); Conf Board Consumer Confidence (1); NAHB (1); NAR Pending Home Sales (1);
  AAII x6 (6). The authoritative source is the originating private body, but its data feed is
  typically licensed and a free press-release headline is not ingestion-ready for an automated
  daily pull — so **YCharts-if-carried is the practical automation channel** for all 19. M2
  verifies (a) the originating-body feed terms and (b) whether YCharts carries each.
- **6 → stays-Bloomberg-proprietary** (no free, government, originating-body, or vendor
  reproduction): Bloomberg Financial Condition Index, Fed NLP Sentiment, Ted Spread, Bloomberg
  US Aggregate OAS, DXY, MOVE. Honest terminal verdicts. Two carry a documented partial
  off-Bloomberg path the implementation TO should weigh: Bloomberg FCI (Chicago Fed NFCI, a
  FRED-native financial-conditions index, is **already rendered on the same page** — idx 17),
  and MOVE (`opal-portal-volatility-fetcher` **already** sources it from Yahoo Finance
  `^MOVE`).

This 25-of-81 split matches the TO's expected "~25-30 proprietary" — confirming Andrew's
premise. The replaceable majority (55 FRED + 1 Treasury = 56, 69%) concentrates in the
government-data groups; the proprietary residue concentrates in the two licensed-survey groups
(Leading Indicator 8/8, Investor Sentiment 7/7 = 15 of the 25).

---

## 5. Not self-certified — handoff to TO-M2 (R5)

Per R5 (verifier != author) this contract is a set of **candidate** source claims. **No row is
marked "confirmed."** TO-M2 (`0.1.0_DS_MarketIntelligence` — a different agent and pod)
independently verify-channel-validates every row. The TSV's `m2_verify_note` column carries
the specific verification target per indicator. M2's verification priorities:

1. **FRED `units=` transforms (24 rows)** — confirm each `pch`/`pc1`/`chg` transform reproduces
   the Bloomberg pre-computed MoM/YoY/QoQ row (F1 probed values, not transforms, for most).
2. **FRED series-ID confirmation** — idx 12 (`AMTMNO` not `NEWORDER`), idx 21 (TIC — exact
   Treasury table), idx 41 (`MARTSSM44X72USS` ex-auto-and-gas), idx 52 (Case-Shiller 20-City
   SA vs NSA), idx 26 (`PPIFIS`).
3. **Proxy fidelity (4 rows)** — AAA/IG/HY ICE-BofA-vs-Bloomberg OAS divergence; USD/CNH
   onshore-vs-offshore yuan divergence — quantify and rule acceptable/not for the heatmap.
4. **YCharts coverage of the 19 originating-body rows** — does YCharts actually carry ISM,
   S&P Global PMI, Conference Board, NFIB, AAII (sentiment + allocation), NAHB, NAR Pending,
   UMich 5-10yr, ADP? This is the single biggest open question for the WS-C migration scope.
5. **Originating-body feed terms** — for any indicator where YCharts does not carry it, is the
   originating body's own feed free and machine-readable, or licensed-only.

---

## 6. Compiler Tools

| Phase | Mandate | Result |
|---|---|---|
| 1 | Confirm enumeration complete vs `yang-generate-macro` MACRO_GROUPS — none dropped | DONE — `MACRO_GROUPS` (lambda_function.py:28-134) direct-read; 12 groups, **81** indicators counted group-by-group; all 81 in the contract. F1's 79-row TSV was missing `MOVE` — added (idx 76). PRD "~91" reconciled to the verified 81 (§2.1). |
| 2 | `comp-platinum reverse json/macro/**` -> which components consume which groups | `comp-platinum reverse json/macro/macro_data.json` + `json/macro/**` — "no components found" (yang pages are comp-graph-thin, PRD §5; confirms F1). Serving path confirmed: CF `/api/general/*` -> S3 `opal-data-portal-v2`. Component map stands from F1 §2.1 — 4 components: `MacroHeatmap` (all 12 groups), `YieldCurveTab` (Treasury Yields), `VolatilityTab` (VIX/MOVE via `volatility_data.json`), `MacroTimeSeriesModal` (per-indicator drill-down). |
| 3 | Hand the contract to TO-M2 — M1 does NOT self-certify | DONE — §5; RAVC2 to COO triggers M2's GO. |

`comp-*` runs auto-logged via `.comp-graph/.agent_context` (TO_ID `YALP_MDSRC.M1`).

## 7. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — every MACRO_GROUPS indicator present; Phase-1 completeness check, none dropped | MET — 81/81, the deployed-code count (PRD "~91" reconciled, §2.1); per-row in the TSV |
| AC2 — per indicator: name, group, ticker, description, frequency, candidate source(s), verdict — all populated | MET — TSV all 11 columns populated for all 81 rows |
| AC3 — proprietary-vs-replaceable split explicit; every no-free-government-source indicator -> YCharts-if-carried or stays-Bloomberg-proprietary | MET — §4: 25 such indicators, each explicitly dispositioned (19 originating-body-direct + YCharts-if-carried; 6 stays-Bloomberg-proprietary) |
| AC4 — no row self-certified "confirmed" — verdicts are candidate claims for M2 | MET — §5; no "confirmed" anywhere; `m2_verify_note` per row |
| AC5 — committed contract; session-log Compiler Tools section; RAVC2 to COO + CC CTO; handed to M2 | this brief + TSV committed; session log; RAVC2 on commit |

## 8. Handoff

- The contract (this brief + TSV) is **TO-M2's input** — `0.1.0_DS_MarketIntelligence`
  independently validates every row's source claim through the verify channel.
- The implementation TO (downstream of M2) scopes the FRED macro-ingestion Lambda for the
  56 FRED/Treasury-replaceable indicators (F1 §5 already sketched this — pattern-identical to
  `ingest_yield_curve_fred.py`), and a separate decision on the 19 originating-body rows
  (gated on M2's YCharts-coverage finding — priority 4 in §5).
- RAVC2 to `2.0.0_SA_COO`, CC `1.0.0_SA_CTO`. The RAVC2 delivery triggers M2's GO.
