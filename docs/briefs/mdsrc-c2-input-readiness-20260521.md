# YALP_MDSRC — C2 Input-Readiness Cross-Check (C3 spec vs A3 P3 endpoint map)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` |
| Purpose | Pre-stage check: does the A3 P3 internal-API endpoint map cover the WS-2 input requirements C2 will build against? |
| Author | `0.2.0_DS_PortfolioAnalytics` (C3 author; C2 co-owner) |
| Date | 2026-05-21 |
| Audience | `0.1.0_DS_MarketIntelligence` (C2 owner) + `2.0.0_SA_COO` (RAVC2) |
| Dispatched by | COO (MCP `20260521T125509Z`) — parallel pre-stage so C2 launches clean behind C1 |
| Inputs cross-checked | `docs/briefs/mdsrc-ws2-c2-input-spec-20260520.{md,tsv}` (C3) vs `docs/briefs/mdsrc-ycharts-internal-api-mapping-20260520.tsv` (A3 P3, 35 rows) |

---

## 1. Verdict

**C2 input coverage is READY for the WS-2 surfaces, with 3 items to carry into the C2 build.**
The A3 P3 35-row endpoint map covers every WS-2 hybrid/replaceable surface my C3 spec
enumerated, the two documents' verdicts are fully consistent, and the requirement-side (C3)
and endpoint-side (A3 P3) compose cleanly. Three items below are not blockers — they are
known-unknowns C2 must not be surprised by mid-build.

**Verdict consistency (C3/WS-2 audit vs A3 P3) — all aligned:**

| Surface | C3 / WS-2 verdict | A3 P3 verdict | Match |
|---|---|---|---|
| WS2-MP-04 (ETF returns) | YCharts-replaceable | YCharts-replaceable | yes |
| WS2-MP-01/02/03 (benchmark legs) | hybrid | hybrid | yes |
| WS2-FT-02/03 (factor spreads) | hybrid | hybrid | yes |
| WS2-MP-05 (peer) | hybrid / methodology-bound | hybrid / methodology-gated | yes |
| WS2-FT-01, POS-01/02/03, CMA-01/02 | proprietary / Bloomberg-pkl-only | proprietary / Bloomberg-pkl-only | yes |

No verdict divergence between the WS-2 audit and the A3 internal-API mapping.

---

## 2. Coverage confirmed

Every WS-2 surface C2 builds a YCharts pull for has a corresponding A3 P3 row with an
internal endpoint + params + JSON path:

- **WS2-MP-01/02/03** — `/indices/table_data` (index-benchmark legs) + `/charts/fund_data.json`
  (ETF-benchmark legs) + `/charts/scatter_plot_data.json` POST (MP-03 risk/return scatter).
  C3's 9-series enumeration (3 constituent indices + 3 ETFs + 3 RFR tenors) maps onto these:
  the 3 indices (Bloomberg 0-1Y Treasury, Bloomberg Aggregate, MSCI ACWI) via `/indices/table_data`,
  the 3 ETFs (VGSH, AGG, ACWI) via `/charts/fund_data.json` (A3 P3 WS2-MP-04 confirms ETFs are
  served by the same generic entity-agnostic endpoint). Re-blend weights are in the
  `yang-model-portfolio-benchmarks` source (C3 §3.3) — unchanged.
- **WS2-MP-04** — `/charts/fund_data.json`, the cleanest pull (5 public ETFs).
- **WS2-FT-02/03** — `/charts/general_data.json` (public-index spread legs) — see Item 2.
- **WS2-MP-05** — `/calculations/metric_sets` + percentile metrics, methodology-gated — matches
  C3/WS-2's "peer is YCharts-sourceable only if Opal adopts the YCharts peer taxonomy."

---

## 3. Three items C2 must carry (not blockers — known-unknowns)

### Item 1 — Crude Oil correlation input: variant ambiguity, no A3 P3 row

C3 flagged **4** correlation crosswalk issues: 3 Treasury gaps **+ the "Crude Oil" variant
ambiguity**. A3 P3 explicitly carries the 3 Treasury gaps as rows `WS1-COR-TR1/TR2/TR3`
(`NEEDS-SYMBOL-LOOKUP`) — good. But the **Crude Oil ambiguity is not a distinct A3 P3 row**:
A3 P3's correlation coverage is `WS1-COR-01` ("59-ticker") + the 3 TR rows = 62; the 63rd
correlation index (`yang-generate-correlation` consumes a bare `Crude Oil`) is unaccounted.

The crosswalk has **`Crude Oil Brent` (`CO1 Comdty`)** AND **`Crude Oil WTI` (`CL1 Comdty`)** —
no bare `Crude Oil` row. **C2 action:** before pulling the correlation Crude Oil series,
confirm which variant `data_pkl/return_monthly`'s `Crude Oil` series actually is (almost
certainly WTI/CL1 for a US portal, but verify against the pkl) — and resolve it to one YCharts
symbol. Do NOT let it fall through as an unmapped string mid-build. Recommend A3/0.1.0_DS add
a `WS1-COR-CRUDE` row alongside the TR rows for parity.

### Item 2 — FT-02/03 "NEEDS-YANG-CONSULT": the consult artifact already exists — it is C5

A3 P3 marks `WS2-FT-02`/`WS2-FT-03` `NEEDS-YANG-CONSULT` ("FT factor-spread constituent index
pairs are model.pkl-precomputed (C3 finding) - Yang-source consult routed"). Correct — but the
**consult artifact is already written and committed**: `YALP_MDSRC.C5` —
`docs/briefs/mdsrc-c5-factor-pair-constituents-20260521.md` (commit `85836135a`), the 12-leg
factor-pair constituent **ratification packet** (6 pairs x 2 legs, each with proposed index +
Bloomberg ticker + crosswalk row + HIGH/MEDIUM/LOW confidence). It is with Andrew/Yang for
one-pass ratification.

**C2 action:** FT-02/03's constituent resolution path is **ratify C5**, not a fresh cold
consult. Once Andrew/Yang sign off C5, the 12 FT-02/03 constituent legs are known and C2
builds against the ratified packet. Recommend the A3 P3 `WS2-FT-02/03` rows be updated to
cite C5 as the resolution artifact (`status: NEEDS-C5-RATIFICATION`, not a generic
`NEEDS-YANG-CONSULT`). C2 should sequence FT-02/03 last, gated on C5 ratification.

### Item 3 — MP-03 RFR leg sources from FRED, not the YCharts pull

C3 enumerated MP-01/02/03's inputs as 3 index blends + 3 ETF blends + **3 RFR Treasury tenors
(1Y/5Y/10Y)**. A3 P3 routes the Treasury yield curve to **FRED** (`WS1-MAC-03`
"Treasury yield curve — already-FRED"). So the MP risk-free-rate leg is **FRED-sourced, not a
YCharts pull**. **C2 action:** C2's YCharts pull builds the index + ETF benchmark legs only;
the MP-03 `rfr` series comes from the FRED path (the F-chain), not from C2. C2 must not
mis-scope the rfr leg into the YCharts pull — wire it from the FRED-ingested series instead.

---

## 4. Handoff

- **To 0.1.0_DS (C2 owner):** C2's WS-2 input coverage is ready. Carry the 3 items above into
  the C2 build — none blocks the start; Items 1 and 3 are wire-time confirmations, Item 2
  sequences FT-02/03 behind C5 ratification. Recommend adding a `WS1-COR-CRUDE` row + updating
  the FT-02/03 rows to cite C5.
- **To COO:** C2-input-readiness pre-stage complete; C2 launches clean behind C1 with no
  input-spec surprise. RAVC2 on commit.
- No code; audit/cross-check only.
