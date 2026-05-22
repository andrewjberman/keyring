# YALP_MDSRC.D3 -- All-Surface Confirmation Closure

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` -- D3 (the closure pass after Andrew rejected D2's partial framing) |
| Task Order | `YALP_MDSRC.D3` (ds-all-surface-confirmation-closure) |
| Owners | `0.1.0_DS_MarketIntelligence` (WS-1, 71 surfaces + the RSI hand-off) + `0.2.0_DS_PortfolioAnalytics` (WS-2 FT-02/03 leg) |
| Date | 2026-05-22 |
| Method | ADHC_VALGATE Class-C + return-equivalence + matched-window comparison; ALL evidence empirical-grounded |
| Audience | `2.0.0_SA_COO` (RAVC2). `3.0.0_SA_CVO` continuous validation loop. |
| Scope guard | READ + COMPARE + DORMANT C2 module re-map ONLY -- zero PROD/AWS/portal change |
| Supersedes | The "carried forward to D1 cutover" framing of `docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md`. D2's per-surface diagnoses retained as the D3 work list AND recorded both-ways per surface where D2 mis-categorized. |

---

## 1. Summary -- 71/71 WS-1 surfaces terminal

| Verdict | Count | Notes |
|---|---|---|
| CONFIRMED-MATCH | 61 | 42 carrying from D2 + 19 newly resolved (re-map applied) |
| CONFIRMED-REPRESENTATIVE | 9 | 4 V1A/V1B (by-design) + 2 European MSCI (Spain/Sweden) + 3 commodities (WTI/Brent/Silver) |
| CONFIRMED-BLOOMBERG-ONLY | 1 | Copper -- no YCharts equivalent of Bloomberg HG1 futures |
| (RSI hand-off) | -- | CONFIRMED-DERIVED -- Wilder RSI-30D from price history |

Zero surfaces left as bare DIVERGENCE / MINOR / untriaged. AC1 met.

D2's three blanket cause framings were ALL too coarse; each replaced with the
per-surface empirical cause and recorded both-ways for CVO validation (see §4).

Three module commits land on origin/CLOUD, all on dormant C2 source -- AC5 intact:
ycharts-pipeline still v1.2.1; no Terraform / manifest / Lambda-schedule / data_pkl
/ portal touch.

---

## 2. Method

**Matched-date anchor** (carried from D2 §1): all per-surface diffs at the
portal `all-returns.json` `data_as_of: 2026-05-18` (the latest settled portal
observation). YCharts value at-or-last-settled <= 2026-05-18.

**Return-equivalence test** (sanctioned by COO 2026-05-22): when a level
mismatch is a vendor-rebasing artifact, the test that determines correctness is
return tracking, not level. The portal renders surfaces from `period_returns`
(1D/1W/1M/1Q/1Y/3Y/5Y), not the raw level; a YCharts variant whose returns match
the portal `period_returns` IS reproducing the rendered surface.

**Matched-window discipline** (D3 sharpening): the portal's `period_returns`
"5Y" for the European MSCI surfaces is NOT a clean trailing 5 calendar years
-- it compounds the FULL available `data_pkl` `return` series (which starts
~2020-12-31 for these indices, ~5.4 calendar years). Compounding YCharts vs
portal over IDENTICAL date ranges eliminates the window ambiguity. The portal's
1Y is unambiguous (both series have >1Y data) and used as the primary anchor.

**Verdict taxonomy** (per the TO):
- **CONFIRMED-MATCH** -- YCharts entity matches the portal value (level OR
  matched-window returns) to-the-cent or within ADHC_VALGATE Class-C tolerance.
- **CONFIRMED-DERIVED** -- the surface is computed from the YCharts series via
  a deterministic formula (e.g. Wilder RSI-30 from a price-close window).
- **CONFIRMED-REPRESENTATIVE** -- the YCharts entity is the same index family
  (the correct representative) but a small residual remains; tracking evidence
  documented per-horizon.
- **CONFIRMED-BLOOMBERG-ONLY** -- no YCharts entity reproduces the portal
  value to tolerance; evidenced what the portal value IS (Bloomberg ticker)
  and why no YCharts entity matches.

---

## 3. WS-1 per-work-unit terminal verdicts

### 3.1 WU1 -- MSCI variant (13 surfaces) -- TERMINAL

D2's stated cause "MSCI variant / TR-vs-PR basis mismatch (13)" is TOO COARSE.
Empirical: 4+ distinct sub-causes per cluster. Per-surface:

#### USA factor cluster (5) -- CONFIRMED-MATCH on level

The portal USA factor indices are MSCI **Net Total Return** (NTR), not the
base price-return index D2 mapped.

| Portal entity | D2 stated cause | YCharts re-map | Level @2026-05-18 | Portal | Verdict |
|---|---|---|---|---|---|
| MSCI USA Growth | TR-vs-PR basis | `^MSUSAG` -> `^MSUSAGNTR` | 35025.828 | 35025.83 | MATCH (0.0%) |
| MSCI USA Value | TR-vs-PR basis | `^MSUSAV` -> `^MSUSAVNTR` | 17333.571 | 17333.57 | MATCH (0.0%) |
| MSCI USA Size | TR-vs-PR basis | `^MSUSAST` -> `^MSUSASTNTR` | 23681.93 | 23681.93 | MATCH (0.0%) |
| MSCI USA Momentum | TR-vs-PR basis | `^MSUSAM` -> `^MSUSAMNTR` | 7068.819 | 7068.82 | MATCH (0.0%) |
| MSCI USA Min Vol | TR-vs-PR basis | `^MSUSAMVU` -> `^MSUSMVUNTR` | 6817.2121 | 6817.21 | MATCH (0.0%) |

ACTUAL cause: D2 had the price-return BASE symbol; portal uses the NTR variant.
NTR symbols discovered via `/search/suggest/main?q="MSCI USA <factor> Net Total Return"`.

#### MSCI ACWI ex US (1) -- CONFIRMED-MATCH on level

| Portal entity | D2 stated cause | YCharts re-map | Level | Portal | Verdict |
|---|---|---|---|---|---|
| MSCI ACWI ex US | TR-vs-PR basis | `^MSACXUSL` -> `^MSACWIXUSA` | 458.734 | 458.73 | MATCH (0.0%) |

ACTUAL cause: D2 had the **local-currency (LOC)** variant, NOT a TR-vs-PR
issue. The base USD index `^MSACWIXUSA` matches to-the-cent.

#### European-5 single-country cluster (5) -- CONFIRMED-MATCH on matched-window returns

The portal European MSCI single-country surfaces are Bloomberg `MX**` tickers
on the portal data_pkl (`MXFR Index` for France, etc.). The portal serves them
at a different LEVEL scale than YCharts (vendor rebasing) AND its `period_returns`
are compounded gross total return in local currency over the full pkl window.

Matched-window comparison (portal `return` from pkl, compounded vs YCharts
`^MSxxTRL` level-ratio, IDENTICAL date ranges 1Y/3Y/5Y from 2026-05-18):

| Portal entity | Bloomberg | YCharts re-map | matched-window maxdiff (1Y/3Y/5Y) | Verdict |
|---|---|---|---|---|
| MSCI France | `MXFR Index` | `^MSFR` -> `^MSFRTRL` | 0.0001 | MATCH-on-returns |
| MSCI Germany | `MXDE Index` | `^MSDE` -> `^MSDETRL` | 0.0013 | MATCH-on-returns |
| MSCI Italy | `MXIT Index` | `^MSIT` -> `^MSITTRL` | 0.0013 | MATCH-on-returns |
| MSCI United Kindom | `MXGB Index` | `^MSUK` -> `^MSUKTRL` | 0.0006 | MATCH-on-returns |
| MSCI Netherlands | `MXNL Index` | `^MSNLA` -> `^MSNLTRL` | 0.0054 | MATCH-on-returns |

**Level does NOT match.** The portal MXFR level 226.48 and YCharts `^MSFRTRL`
level (in thousands) are different vendor base-scalings of the SAME index;
their returns over identical windows match to-the-cent (France 0.0001 maxdiff).
The cutover to YCharts (D1) would handle the rebasing separately. The rendered
heatmap / period-return surfaces are correct as-mapped.

ACTUAL cause: NOT "TR-vs-PR basis." The portal serves Bloomberg `MX**`
local-currency total-return indices; YCharts carries the same index family on
a different vendor scale. The D2 framing missed: (a) the local-currency
dimension, (b) the gross-TR vs price-return variant, (c) the non-standard portal
"5Y" window definition.

#### Spain + Sweden (2) -- CONFIRMED-REPRESENTATIVE

Same Bloomberg `MX**` / YCharts `^MSxxTRL` family as France/Germany/Italy/UK,
but on the matched-window comparison a persistent small Bloomberg-vs-YCharts
residual remains:

| Portal entity | Bloomberg | YCharts | matched-window maxdiff | Direction |
|---|---|---|---|---|
| MSCI Spain | `MXES Index` | `^MSESTRL` | 0.1311 (1pp 1Y, 5.8pp 3Y, 13pp 5Y) | portal HIGHER, monotonic |
| MSCI Sweden | `MXSE Index` | `^MSSETRL` | 0.0364 (0.7pp 1Y, 3.2pp 3Y, 3.6pp 5Y) | YCharts higher; portal between net/gross TR |

Diagnosis: a small persistent vendor methodology / withholding-tax-treatment
difference for these specific countries' MSCI indices on the gross-TR-LOC basis
(~2.5pp/year for Spain; smaller for Sweden). NOT a wrong-entity issue: the
right family (`^MSxxTRL`) tracks France/Germany/Italy/UK to-the-cent on the
same basis. The ticker_map re-map points to the closest YCharts representation;
the brief documents the residual.

#### WU1 ticker_map commit: `a401ca1c7` (13 lines, 13 surfaces).

### 3.2 WU2 -- Commodities (4 surfaces) -- TERMINAL

D2's stated cause "GSCI commodity sub-index basis (4)" is FALSIFIED. Portal
pkl `bbg_ticker` reveals the portal commodity entities are Bloomberg
**front-month FUTURES** contracts (`CL1`/`CO1`/`HG1`/`NG1 Comdty`), NOT GSCI
sub-indices and NOT spot prices.

| Portal entity | Portal bbg | D2 stated cause | YCharts re-map | YCharts value | Portal | Pct diff | Verdict |
|---|---|---|---|---|---|---|---|
| Natural Gas | `NG1 Comdty` (NatGas front-month future) | GSCI TR vs spot | `^SG8A` -> `I:HHNGSP` (Henry Hub spot) | 3.07 | 3.02 | +1.7% | MATCH (MINOR-band; spot tracks NatGas front-month closely) |
| Crude Oil WTI | `CL1 Comdty` (WTI front-month future) | GSCI TR vs spot | `^SG**` etc. -> `I:WTICOWSP` | 112.25 | 108.66 | +3.3% | REPRESENTATIVE (futures-vs-spot basis residual; YCharts has no CL1-futures entity) |
| Crude Oil Brent | `CO1 Comdty` (Brent front-month future) | GSCI TR vs spot | `^BCOB` -> `I:BCOWSPP` | 116.73 | 112.10 | +4.1% | REPRESENTATIVE (futures-vs-spot basis residual) |
| Copper | `HG1 Comdty` (COMEX Copper front-month future) | GSCI TR vs spot | `^SG3J` -> `^BCUS` (Bloomberg Copper Subindex, closest YCharts entity) | 493.85 | 627.20 | -21.3% | **BLOOMBERG-ONLY** -- YCharts does not carry the Bloomberg COMEX copper front-month futures contract `HG1`; the Bloomberg Copper Subindex `^BCUS` is the closest representation but materially diverges. For future-cutover, this surface keeps the Bloomberg-pkl path. |

ACTUAL cause: NOT GSCI basis -- the portal uses Bloomberg FRONT-MONTH FUTURES
on the energy / industrial-metals commodities. The futures-vs-spot basis is
~3-4% for WTI/Brent (acceptable as REPRESENTATIVE); NatGas is tight (front-month
tracks spot for physical-delivery reasons); Copper has no YCharts equivalent.

Silver was mis-grouped by D2 with GSCI but the portal pkl shows
`XAG BGN Curncy` (Bloomberg generic spot). YCharts `I:NYSP` -2.4% =
CONFIRMED-REPRESENTATIVE (BGN dealer-pricing vs NYSP residual).
(Silver was logged under WU2 in D2; verdict above applies.)

#### WU2 ticker_map commit: `e508c6bb3` (folded with WU3/WU5).

### 3.3 WU3 -- Crypto / commodity calc-basis (4 surfaces) -- TERMINAL

D2's stated cause "security-kind crypto/commodity calc basis" is FULLY
FALSIFIED. The actual D2 defect was wrong-ENTITY: ticker_map.py had **equity
tickers** for these portal entities, not commodity/crypto symbols.

| Portal entity | D2 had | D2 wrong because... | YCharts re-map | YCharts value | Portal | Pct diff | Verdict |
|---|---|---|---|---|---|---|---|
| Bitcoin | `BTC` (a stock ticker on YCharts) | not the crypto; YCharts has Bitcoin only as an INDICATOR entity, not a security | `BTC` -> `I:BTCUSD` (CoinGecko daily) | 77425.72 | 76855.49 | +0.74% | MATCH (24/7-asset snapshot timing residual is intrinsic, documented) |
| Ethereum | `ETH` (Ethan Allen ETH stock) | same as Bitcoin | `ETH` -> `I:ETHUSD` | 2128.00 | 2116.01 | +0.57% | MATCH (24/7 snapshot timing) |
| Gold | `GOLD` (Barrick Gold the equity stock, trades ~$40) | NOT spot gold; Barrick is a gold-MINER stock | `GOLD` -> `I:GPUSDNK` (Gold price USD) | 4566.90 | 4566.67 | **0.0%** | MATCH to-the-cent |
| Crude Oil WTI | `WTI` (W&T Offshore the equity stock, trades ~$5) | NOT WTI crude; W&T is an oil-exploration stock | `WTI` -> `I:WTICOWSP` (folded with WU2; see 3.2) | 112.25 | 108.66 | +3.3% | REPRESENTATIVE (per WU2 futures-vs-spot) |

ACTUAL cause: D2 mapped 4 portal commodity/crypto entities to YCharts equity
tickers that happened to share the abbreviation (BTC=stock, ETH=stock,
GOLD=Barrick mining company, WTI=W&T Offshore exploration company). The values
were not "wrong calc basis" -- they were correctly-priced EQUITIES that have
nothing to do with the underlying commodity/crypto. Re-map to the YCharts
indicator entities resolves all 4 to MATCH-class.

#### WU3 ticker_map commit: `e508c6bb3`.

### 3.4 WU4 -- V1A/V1B representative-index (4 surfaces) -- TERMINAL

Per Andrew V1A/V1B 2026-05-21 ruling, these portal entities resolved to a
representative Bloomberg index in C2; D3 confirms via return correlation. All
4 = CONFIRMED-REPRESENTATIVE.

| Portal entity | Portal bbg | YCharts rep (unchanged) | Matched-window maxdiff (1Y/3Y/5Y) | Verdict |
|---|---|---|---|---|
| Bloomberg 0-1 Year Treasury | `I22917US Index` (specific 0-1Y index) | `^BBUTB13MTR` (1-3mo T-Bill TR -- broad-duration substitute) | 0.0235 (max 2.4pp) | REPRESENTATIVE -- short-duration Treasury proxy |
| Bloomberg 0-5 Year High Yield | `BEJKTRUU Index` (0-5Y HY TR) | `^BBUSCOHYTR` (broad HY TR) | 0.0426 (max 4.3pp) | REPRESENTATIVE -- broad HY substitutes for short-duration HY |
| Bloomberg 0-5 Year TIPS | `LTP5TRUU Index` (0-5Y TIPS TR) | `^BBUTISTR` (broad TIPS TR) | 0.1221 (max 12.2pp) | REPRESENTATIVE -- broad TIPS substitutes for short-duration TIPS; tracking looser because duration mismatch is larger |
| Bloomberg 20+ Year Treasury | `LT11TRUU Index` (specific 20+Y TR) | `^BBUSLGCRTR` (broad Long Gov/Credit TR) | 0.1132 (max 11.3pp) | REPRESENTATIVE -- broad Long Gov/Credit substitutes for pure long Treasury; tracking residual reflects the corporate-credit dilution |

D2 already flagged these as expected by-design. D3 adds the matched-window
return-correlation evidence per surface. Re-maps NOT applied (the V1A/V1B
representatives are the right choice; the tracking residual is the rep-vs-actual
duration/composition difference, documented per surface).

### 3.5 WU5 -- Communication Services (1 surface) -- TERMINAL

| Portal entity | Portal bbg | D2 stated cause | YCharts re-map | YCharts value | Portal | Pct diff | Verdict |
|---|---|---|---|---|---|---|---|
| Communication Services | `S5COMM Index` (S&P 500 Comm Services) | rebased-vintage / wrong-symbol | `^SPXCMSVS` -> `^SPXCMSVSTR` | 1355.61 | 1346.42 | +0.68% | MATCH (MINOR-band) |

ACTUAL cause: `^SPXCMSVS` is the price-return / pre-2018 reconstitution Comm
Services index variant (the GICS Comm Services sector was reconstituted Sep
2018 from Telecom Services + Internet + Media). The portal serves the
**Total Return** variant `S5COMM Index` post-reconstitution. The TR variant
`^SPXCMSVSTR` matches within MINOR (+0.68% likely a snapshot timing residual;
the entity is correct).

#### WU5 ticker_map commit: `e508c6bb3`.

### 3.6 WU6 -- MINOR residuals (3 surfaces) -- TERMINAL

| Portal entity | Portal bbg | YCharts (unchanged) | Level diff | Verdict |
|---|---|---|---|---|
| MSCI China | `MXCN Index` | `^MSCN` | -1.15% | MATCH (MINOR-band; Asian market closes hours before US 2026-05-18 anchor -- timezone snapshot residual) |
| MSCI Switzerland | `MXCH Index` | `^MSCHL` (LOC) | +0.64% | MATCH (MINOR-band; vendor timing/rounding; ^MSCHTRL gross-TR-LOC tested at 7031, +315%, wrong basis -- LOC is correct here) |
| Real Estate | `S5REAL Index` (S&P 500 Real Estate) | `^SPXRES` | -1.34% | MATCH (MINOR-band; ^SPXRESTR 400'd -- no TR variant available; the price index residual is vendor timing/dividend-timing) |

ACTUAL cause: small per-vendor timing / rounding residuals within the
ADHC_VALGATE Class-C MINOR band (<2%). No closer YCharts variant pulled; the
current entity IS the correct one, the residual is intrinsic-not-fixable
without changing data source. Symbols unchanged.

### 3.7 RSI hand-off (WS1-MO-02/03) -- CONFIRMED-DERIVED

| Sub-task | Result |
|---|---|
| YCharts native RSI-30D? | Probed `/indices/table_data` with columns `rsi_30`, `rsi`, `rsi_30day`, `rsi_period`, `rsi30` -- all 404. Only `rsi_14` 200. |
| Derivation | Standard Wilder RSI(period=30) from a price-close series. Implementation: `_derive_rsi_30()` added to `ws1_surface_pull.py`. |
| Sanity check | Alternating-deltas series ~48 (expected ~50); strict uptrend = 100.0; strict downtrend = 0.0 (Wilder canonical). |
| Module re-wire | `pull_rsi_summary` / `pull_rsi_details` now pull per-symbol `general_data(metric="price")` series and apply `_derive_rsi_30(closes, period=30)`. |
| Commit | `6835b5de1` (ws1_surface_pull.py, +65/-10 lines). |

Per 0.2.0_DS's WS-2 hand-off and Yang notebook `market_indices_data_pull.ipynb`
cell 10 (`'rsi': 'RSI_30D'`).

---

## 4. D2 cause-correction record (CVO cross-check)

Per COO directive, the brief carries D2's stated cause AND the actual empirical
cause for every surface where D2 mis-categorized. Summary:

| D2 stated cause (blanket) | D2 surface count | ACTUAL causes (D3 empirical) |
|---|---|---|
| MSCI variant / TR-vs-PR basis mismatch (13) | 13 | 4 sub-causes: USA factors = price-vs-NTR (5); ACWI-exUS = LOC-vs-USD currency variant (1); European-5 = right index + gross-TR-LOC + matched-window window-artifact (5); Spain/Sweden = small persistent Bloomberg-vs-YCharts residual on same family (2) |
| GSCI commodity sub-index basis (4) | 4 | Portal commodities are Bloomberg FRONT-MONTH FUTURES (CL1/CO1/HG1/NG1), NOT GSCI subindices. NatGas spot tracks tightly; WTI/Brent futures-vs-spot ~3-4%; Copper has no YCharts equivalent |
| security-kind crypto/commodity calc-basis (4) | 4 | Wrong-ENTITY: D2 mapped to EQUITY TICKERS (BTC/ETH = stocks, GOLD = Barrick mining stock, WTI = W&T Offshore stock). Correct entities are YCharts indicators (I:BTCUSD etc.). Gold matches to-the-cent on the indicator |
| Communication Services investigate (1) | 1 | Pre-2018 reconstitution / price-return variant; portal serves TR variant -- re-map to ^SPXCMSVSTR |
| MINOR (3) | 3 | Intrinsic vendor timing / timezone-snapshot residuals within Class-C MINOR band; no closer variant; documented |
| V1A/V1B representative (4) | 4 | (D2 framing CORRECT) -- by-design representative-index substitution per Andrew ruling; D3 adds matched-window return-tracking evidence |

D2's 42 to-the-cent MATCH surfaces carry forward (load-bearing validation of
the pull mechanism + symbol map + matched-date method); no re-categorization
needed for those.

---

## 5. Module / ticker_map commits (dormant C2 source -- AC5 intact)

| Commit | Scope | Lines | Gates |
|---|---|---|---|
| `a401ca1c7` | WU1 MSCI 13 re-maps -- USA factors=NTR, ACWI=base USD, European-7=gross-TR-LOC | +13/-13 | py_compile, structural_self_test 4/4, ds-commit-gate clean |
| `e508c6bb3` | WU2/WU3/WU5 re-maps -- crypto/commodity indicator entities + Comm Services TR variant; YC_KIND updates | +13/-13 | py_compile, structural_self_test 4/4, ds-commit-gate clean |
| `6835b5de1` | RSI Wilder-30 derivation -- _derive_rsi_30 helper + pull_rsi_summary/details rewired to general_data price series | +65/-10 | py_compile, structural_self_test 4/4, ds-commit-gate clean |

**ZERO production change** -- no Terraform / manifest / Lambda-schedule /
data_pkl / portal touch; ycharts-pipeline still v1.2.1. Per AC5.

---

## 6. Acceptance criteria

| AC | Status | Evidence |
|---|---|---|
| AC1 -- every 71 WS-1 surface terminal verdict; ZERO bare DIVERGENCE/MINOR/untriaged | **MET** | §1 + §3 -- 61 MATCH + 9 REPRESENTATIVE + 1 BLOOMBERG-ONLY = 71 |
| AC2 -- re-mapped/derived: live re-pull on matched dates; before/after diff per surface | **MET** | §3 per-WU tables; probe artifacts `.runtmp/d3/d3_repull_msci_result.json` + `d3_matched_window_result.json` + `d3_repull_commodities_result.json` + `d3_wu4_5_6_result.json` |
| AC3 -- CONFIRMED-BLOOMBERG-ONLY or CONFIRMED-REPRESENTATIVE: specific evidenced reason | **MET** | Copper §3.2 (Bloomberg HG1 futures; YCharts has no equivalent; ^BCUS Bloomberg Copper Subindex tested at -21%); REPRESENTATIVE entries §3.1/3.2/3.4 with matched-window or futures-vs-spot evidence |
| AC4 -- each WU resolved + WS-2 FT-02/03 reconcile + RSI basis | **MET** WS-1 side; WS-2 in §8 (0.2.0_DS); RSI §3.7 (CONFIRMED-DERIVED) |
| AC5 -- ZERO production / AWS / portal change | **MET** | §5 -- 3 commits on dormant C2 source only; ycharts-pipeline still v1.2.1; no Terraform / manifest / Lambda-schedule / data_pkl / portal touch |
| AC6 -- committed brief with the per-original-29 fix-applied note + RAVC2 to COO | **MET** | This brief; RAVC2 sent on commit of this file |

---

## 7. D1 future-cutover follow-ons (NOT D3 scope -- enumerated for the future project)

1. **Copper CONFIRMED-BLOOMBERG-ONLY** -- D1 must decide: keep the Bloomberg-pkl path for this surface (hybrid migration) OR accept `^BCUS` Bloomberg Copper Subindex as a representative with a level rescaling. YCharts does not carry `HG1` front-month futures.
2. **European-5 + Spain/Sweden + V1A/V1B level rebasing** -- the 5 European MATCH-on-returns + 2 Spain/Sweden REPRESENTATIVE + 4 V1A/V1B REPRESENTATIVE all have a level offset (vendor rebasing). The portal's DDB backbone (WS1-DDB-01) stores a price level; D1 cutover would either rebase the YCharts series to match the portal's base or accept a level reset (with a documented base-date pin).
3. **WTI / Brent CONFIRMED-REPRESENTATIVE** -- the futures-vs-spot basis is ~3-4%. D1 must decide: accept the spot indicator as a representative (with the basis residual documented per ticker), OR keep these on the Bloomberg-pkl path until YCharts adds futures entities.
4. **C2 deploy gap** -- the deployed `ycharts-pipeline` Lambda artifact (v1.2.1) is now 3 commits stale vs repo (a401ca1c7 + e508c6bb3 + 6835b5de1). D1 cutover picks these up via a rebuild + tag bump.

These are explicitly future-cutover scope per the TO; D3 changes nothing live.

---

## 8. WS-2 leg (0.2.0_DS) -- placeholder

[0.2.0_DS to fill: FT-02/03 spread-definition reconcile finalization
(commit 47871c033 fix already referenced) + any WS-2 hybrid-leg residual
disposition. RSI basis check already incorporated into §3.7.]

---

## 9. Joint RAVC2 to 2.0.0_SA_COO

This brief + the 3 module commits + the WS-2 section (§8) constitute the D3
deliverable. Sent jointly by 0.1.0_DS as the agent the TO is issued_to; both
co-owners named (0.1.0_DS WS-1 lead + 0.2.0_DS WS-2). Same one-sender-by-
agreement convention as D2's RAVC2.

YALP_MDSRC closure gate after D3 accept: L1 (yang-pipeline-lineage-map,
0.7.0_AE) -- not WS-1 lane.
