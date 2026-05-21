# YALP_MDSRC.C5 — Factor-Pair Constituent Ratification Packet

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` |
| Task Order | `YALP_MDSRC.C5` — WS-2 factor-pair constituent ratification proposal |
| Author | `0.2.0_DS_PortfolioAnalytics` (WS-2 / portfolio-analytics specialist) |
| Date | 2026-05-21 |
| Audience | **Andrew / Yang — ratification sign-off** (one-pass); RAVC2 to `2.0.0_SA_COO` CC `1.0.0_SA_CTO` |
| Status | **PROPOSED — pending Andrew/Yang ratification.** Not a decision. |
| Feeds | `YALP_MDSRC.C2` FT-02/03 build (pre-clears the C3-Finding-2 Phase-0 prerequisite) |

---

## 1. What this packet is — and is not

C3 Finding 2 established that the 6 Opal factor spreads (the FT-02/03 surfaces) are
**pre-computed inside Yang's manual `model.pkl` build** — the yang generator consumes the
finished `factor_spread` columns and does **not** expose the constituent index behind each
leg. C2's FT-02/03 build needs those constituents.

The 6 factor-pair **NAMES** are known (CTO-confirmed — `FACTOR_NAMES`,
`yang-generate-factor-tilts/lambda_function.py:32-35`): `Equity vs FI`, `Growth vs Value`,
`US vs Foreign`, `Large vs Small`, `Agg vs Short`, `HY vs Agg`. The constituent index
**ticker per leg** is not in the repo.

This packet **proposes** the most-likely constituent index for each of the **12 legs**
(6 pairs x 2), with a Bloomberg ticker, a dc01d4b8a-crosswalk anchor, reasoning, and a
confidence flag — so Andrew or Yang can **ratify or correct it in one pass** rather than C2
serializing behind a cold consult. **It is a proposal. The ratification is Andrew's / Yang's.**

**How to use this packet:** for each leg, either tick the proposed pick or write the correct
index in the "Yang correction" column. The 10 HIGH/MEDIUM legs are very likely right; the
**2 legs that genuinely need Yang's eye are the `Agg vs Short` "Short" leg (LOW) and the
broad-equity-benchmark choice in `Equity vs FI` (MEDIUM)** — §3 calls them out.

---

## 2. Method & evidence

- **Generator source:** `yang-generate-factor-tilts/lambda_function.py` — `FACTOR_NAMES` (the
  6 pair names) + `factor_spread` is consumed pre-computed. `comp-pipescript io` on the
  generator returned "not a comp-graph node" (per PRD §5); source-read substituted.
- **Index universe:** the proposed constituents are drawn only from indices Yang actually
  carries in `data_pkl` — cross-checked against the `yang-generate-correlation`
  `MARKET_OVERVIEW_INDICES` list (63 indices) and the dc01d4b8a crosswalk
  (`mdsrc-ycharts-ticker-map-20260520.csv`, 71 rows). Every proposed leg below resolves to a
  real crosswalk row — so once ratified, C2 has the Bloomberg ticker AND the pending YCharts
  symbol immediately.
- **Corroborating signal:** the Opal SAA/TAA `views.json` (`yang-generate-cma`) carries the
  conceptually-matching house-view pairs — "Equities vs Fixed Income", "Growth vs Value",
  "U.S. vs International", "Duration (Long vs Short)", "Credit (IG vs HY)" — confirming the
  factor pairs are Opal's standard asset-class spreads, not exotic constructs. This supports
  the semantic-standard reasoning below but does not pin tickers.
- **Reasoning basis:** each pick is the **semantically standard** index for the leg,
  preferring (a) indices the Opal model benchmark blends already use, (b) methodology-matched
  pairs (same index family on both legs), (c) indices present in `data_pkl`.

---

## 3. The 12-leg ratification packet

Confidence key: **HIGH** = semantically unambiguous, one standard answer · **MEDIUM** = a
strong pick with one plausible alternative · **LOW** = genuinely needs Yang to confirm.

### Pair 1 — `Equity vs FI`  (broad equity return minus aggregate-bond return)

| Leg | Proposed index | Bloomberg ticker | Crosswalk row | Confidence | Reasoning / alternative |
|---|---|---|---|---|---|
| Equity | **MSCI ACWI** | `MXWD Index` | INDEX / MSCI ACWI | **MEDIUM** | The Opal model benchmark blends are built on **MSCI ACWI** as the equity component ("85% Bloomberg Agg / 15% MSCI ACWI" etc., `yang-model-portfolio-benchmarks` INDEX_COMPOSITIONS) — a factor spread consistent with the benchmark would use the same equity index. **Alternative: S&P 500 (`SPX Index`)** if the factor is intended US-only. |
| FI | **Bloomberg Aggregate** | `LBUSTRUU Index` | BOND_INDEX / Bloomberg Aggregate | **HIGH** | The Opal benchmark blends use Bloomberg Aggregate as the fixed-income component; "FI" in an Opal asset-class spread is unambiguously the Agg. |

### Pair 2 — `Growth vs Value`  (US large-cap growth minus value)

| Leg | Proposed index | Bloomberg ticker | Crosswalk row | Confidence | Reasoning / alternative |
|---|---|---|---|---|---|
| Growth | **Russell 1000 Growth** | `RLG Index` | INDEX / Russell 1000 Growth | **MEDIUM** | Russell 1000 Growth/Value is the textbook US large-cap growth/value pair and is present in `data_pkl` + the crosswalk. **Alternative: MSCI USA Growth (`M1US000G Index`)** — plausible given the model's MSCI-centric benchmarking; ratify whichever family Yang's `model.pkl` uses. |
| Value | **Russell 1000 Value** | `RLV Index` | INDEX / Russell 1000 Value | **MEDIUM** | Methodology-matched partner to the Growth leg. **Alternative: MSCI USA Value (`M1US000V Index`)** — must match whichever family the Growth leg uses (do not mix Russell + MSCI). |

### Pair 3 — `US vs Foreign`  (US equity minus ex-US equity)

| Leg | Proposed index | Bloomberg ticker | Crosswalk row | Confidence | Reasoning / alternative |
|---|---|---|---|---|---|
| US | **MSCI USA** | `MXUS Index` | INDEX / MSCI USA | **MEDIUM** | MSCI USA / MSCI ACWI ex US is the **methodology-matched** US-vs-rest pair (MSCI USA is exactly the US slice of MSCI ACWI). **Alternative: S&P 500 (`SPX Index`)**. |
| Foreign | **MSCI ACWI ex US** | `MXWDU Index` | INDEX / MSCI ACWI ex US | **MEDIUM** | "Foreign" as the complete ex-US opportunity set (includes EM + Canada). **Alternative: MSCI EAFE (`MXEA Index`)** — narrower (developed ex-US/Canada only); ratify per Yang's intent. Pairs with the US leg. |

### Pair 4 — `Large vs Small`  (US large-cap minus small-cap)

| Leg | Proposed index | Bloomberg ticker | Crosswalk row | Confidence | Reasoning / alternative |
|---|---|---|---|---|---|
| Large | **Russell 1000** | `RIY Index` | INDEX / Russell 1000 | **HIGH** | Russell 1000 + Russell 2000 is THE canonical, methodology-matched large/small pair (together = Russell 3000). **Alternative: S&P 500 (`SPX Index`)** — only if Yang deliberately mismatched the families (unlikely). |
| Small | **Russell 2000** | `RTY Index` | INDEX / Russell 2000 | **HIGH** | Russell 2000 is the unambiguous US small-cap benchmark; the only small-cap index in `data_pkl`. |

### Pair 5 — `Agg vs Short`  (aggregate-duration bond minus short-duration bond)

| Leg | Proposed index | Bloomberg ticker | Crosswalk row | Confidence | Reasoning / alternative |
|---|---|---|---|---|---|
| Agg | **Bloomberg Aggregate** | `LBUSTRUU Index` | BOND_INDEX / Bloomberg Aggregate | **HIGH** | "Agg" is unambiguously the Bloomberg US Aggregate (intermediate ~6yr duration). |
| Short | **Bloomberg 1-3 Year Gov/Credit** | `LGC3TRUU Index` | BOND_INDEX / Bloomberg 1-3 Year Gov/Credit | **LOW** | A duration spread; "Short" is genuinely ambiguous. 1-3 Year Gov/Credit matches the Agg's Gov+Credit composition (a clean duration-only spread). **Alternatives: Bloomberg 1-5 Year Gov/Credit (`LD04TRUU Index`)** or **Bloomberg 0-1 Year Treasury (`I22917US Index`)**. **This leg most needs Yang's confirmation** — the choice changes the spread's duration gap materially. |

### Pair 6 — `HY vs Agg`  (high-yield credit minus investment-grade aggregate)

| Leg | Proposed index | Bloomberg ticker | Crosswalk row | Confidence | Reasoning / alternative |
|---|---|---|---|---|---|
| HY | **Bloomberg High Yield** | `LF98TRUU Index` | BOND_INDEX / Bloomberg High Yield | **HIGH** | "HY" is unambiguously the Bloomberg US Corporate High Yield index. (The factor migrated from "HY vs IG" — `HY vs Agg` uses the Agg as the IG proxy.) |
| Agg | **Bloomberg Aggregate** | `LBUSTRUU Index` | BOND_INDEX / Bloomberg Aggregate | **HIGH** | The IG-credit reference leg; the migration note ("HY vs IG" -> "HY vs Agg") confirms the Aggregate is the intended IG proxy. |

---

## 4. Summary & sign-off

| Pair | Leg A | Leg B | Lowest-confidence leg |
|---|---|---|---|
| Equity vs FI | MSCI ACWI (`MXWD`) | Bloomberg Aggregate (`LBUSTRUU`) | Equity leg — MEDIUM (ACWI vs S&P 500) |
| Growth vs Value | Russell 1000 Growth (`RLG`) | Russell 1000 Value (`RLV`) | both MEDIUM (Russell vs MSCI family) |
| US vs Foreign | MSCI USA (`MXUS`) | MSCI ACWI ex US (`MXWDU`) | both MEDIUM (Foreign: ACWI-ex-US vs EAFE) |
| Large vs Small | Russell 1000 (`RIY`) | Russell 2000 (`RTY`) | both HIGH |
| Agg vs Short | Bloomberg Aggregate (`LBUSTRUU`) | Bloomberg 1-3Y Gov/Credit (`LGC3TRUU`) | Short leg — **LOW** |
| HY vs Agg | Bloomberg High Yield (`LF98TRUU`) | Bloomberg Aggregate (`LBUSTRUU`) | both HIGH |

**Confidence tally:** 6 HIGH legs, 5 MEDIUM legs, 1 LOW leg.

**The two legs to look at hardest, Andrew/Yang:**
1. **`Agg vs Short` — the "Short" leg (LOW).** 1-3Y Gov/Credit vs 1-5Y Gov/Credit vs
   0-1Y Treasury — the pick changes the spread's duration gap. Yang's call.
2. **`Equity vs FI` — the equity leg (MEDIUM).** MSCI ACWI (matches the model benchmark) vs
   S&P 500 (US-only). One quick confirm.

The other 10 legs are semantically standard; a tick-through ratifies them. Every proposed
index resolves to a real dc01d4b8a crosswalk row, so on ratification C2 has the Bloomberg
ticker immediately and the YCharts symbol follows from A3's mapping.

**Once ratified:** this 12-leg table becomes the C2 FT-02/03 build spec — C2 pulls the 9
distinct constituent indices (MSCI ACWI, Bloomberg Aggregate, Russell 1000 Growth, Russell
1000 Value, MSCI USA, MSCI ACWI ex US, Russell 1000, Russell 2000, Bloomberg High Yield,
Bloomberg 1-3Y Gov/Credit — 10 distinct, several reused across pairs) and computes the 6
spreads, replacing the pre-computed `model.pkl/factor_spread`.

---

## 5. Compiler Tools

| Phase | `<run>` | Result | vs `<expect>` |
|---|---|---|---|
| 1 | `comp-pipescript io yang-generate-factor-tilts` | "Unknown script" — not a comp-graph node (yang generators off the comp-pipescript graph, PRD §5) | `<if_mismatch>` fallback — source read of `yang-generate-factor-tilts` (`FACTOR_NAMES` + `factor_spread` handling); index universe cross-checked vs `yang-generate-correlation` + the dc01d4b8a crosswalk. Documented §2. |
| 2 | none (proposal doc, no code) | No `.py` authored | MATCH — documented-none |
| 3 | none (confidence-flagged table = self-validation) | §3/§4 checked vs AC1-AC3 | MATCH — documented-none |

`comp-pipescript` run auto-logged to `org/compiler-tools-log.md` via `.comp-graph/.agent_context`
(TO_ID `YALP_MDSRC.C5`).

## 6. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — all 12 legs proposed: index name + Bloomberg ticker + crosswalk row + reasoning | MET — §3 |
| AC2 — HIGH/MEDIUM/LOW per leg; MEDIUM/LOW legs name alternatives | MET — §3, §4 (6 HIGH / 5 MEDIUM / 1 LOW; alternatives named) |
| AC3 — committed ratification-packet brief, framed "proposed pending ratification", pushed to origin/CLOUD + session log + RAVC2 | brief committed + pushed; framed PROPOSED throughout; session log; RAVC2 to COO CC CTO |
