# YALP_MDSRC.V1A — 4-Bond Representative Bloomberg-Index Lookup

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — V1 addendum |
| Task Order | `YALP_MDSRC.V1A` (ds-4-bond-representative-ycharts-index) |
| By | `0.1.0_DS_MarketIntelligence` |
| Date | 2026-05-22 |
| Ruling | Andrew 2026-05-21 (via CTO), verbatim: *"we find a bloomberg index that is representative of those or very similar that ycharts does have, which ycharts surely can oblige."* Andrew rejected BOTH the ETF-proxy AND manual-Bloomberg. |
| Corrects | `docs/briefs/mdsrc-c2-pull-spec-prestage-20260521.csv` — the 4 maturity-band-bond rows (the superseded SHV/SHYG/STIP/TLT ETF-proxy resolution) |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO` |

---

## 1. Outcome — 1 resolved, 3 escalated

For each of the 4 Bloomberg maturity-band bonds, searched the YCharts entity surface
(`/search/suggest/main`, the A5-pinned endpoint, mchm seat) for the closest representative
Bloomberg bond index YCharts carries — 5 search rounds, ~50 queries. Result:

| Band | V1A outcome |
|---|---|
| Bloomberg 0-1 Year Treasury | **RESOLVED** → `Bloomberg US Treasury Bills 1-3 Month` (`^BBUTB13MTR`) |
| Bloomberg 0-5 Year High Yield | **ESCALATE** — no Bloomberg HY maturity-band index on YCharts |
| Bloomberg 0-5 Year TIPS | **ESCALATE** — no Bloomberg TIPS maturity-band index on YCharts |
| Bloomberg 20+ Year Treasury | **ESCALATE** — no Bloomberg pure-Treasury 20+/long maturity-band index on YCharts |

Per the V1A TO ("do NOT force a bad match; ESCALATE that band"), 3 of 4 bands escalate.

## 2. The structural finding — why 3 of 4 escalate

YCharts' **Bloomberg** maturity-segmented fixed-income coverage is narrow. The complete set
of Bloomberg maturity-band indices YCharts carries (mapped via the family-prefix searches,
round 5):

- **US Government/Credit family** — `Bloomberg US Government/Credit 1-3 Year` (`^BBUGCR13YT`)
  and `1-5 Year` (`^BBUGCR15YT`). Government **+ investment-grade credit** — not pure Treasury.
- **Municipal maturity bands** — 1-5yr, 1-10yr, 1-15yr.
- **`Bloomberg US Treasury Bills 1-3 Month`** (`^BBUTB13MTR`) — the only Treasury-pure
  maturity-segmented index.
- The broad parent families — `Bloomberg US Treasury`, `Bloomberg US Corporate High Yield`,
  `Bloomberg US TIPS (Series-L)`, `Bloomberg US Long Government/Credit` (all full-maturity).

There is **no** Bloomberg pure-Treasury intermediate/long maturity band, **no** Bloomberg
High Yield maturity band, and **no** Bloomberg TIPS maturity band on the YCharts surface
(confirmed-negative: `Bloomberg 1-3 Year Treasury`, `Bloomberg 1-5 Year Treasury`,
`Bloomberg Long Treasury`, `Bloomberg 20+ Year`, `Bloomberg 1-5 Year High Yield`,
`Bloomberg 0-5 TIPS`, `Bloomberg 1-10 Year TIPS` — all returned zero index hits).

The maturity-band indices YCharts **does** carry for these segments are **ICE-vendored**, not
Bloomberg: `ICE US Treasury 1-3 Year` (`^ICEUST13YT`), `ICE US Treasury 10-20 Year`
(`^ICEUT12YTR`), and `ICE US Treasury 20+ Year` (`^ICEUT2YTR`, already mapped in the
C2-prestage cross-vendor brief). Andrew's premise — that a representative *Bloomberg* index
exists on YCharts — holds only for the 0-1yr Treasury band; for HY-short, TIPS-short, and
20+yr-Treasury-pure, the YCharts maturity-band surface is ICE, not Bloomberg.

## 3. Band-by-band

### 3.1 Bloomberg 0-1 Year Treasury → RESOLVED

**Representative index:** `Bloomberg US Treasury Bills 1-3 Month` (`^BBUTB13MTR`).

**Representativeness basis:**
- *Credit quality* — exact match. Pure US Treasury (T-bills), zero credit risk, identical to
  the 0-1yr Treasury target.
- *Maturity-band overlap* — the 1-3 month bill segment sits **within** the 0-1yr (0-12mo)
  target band; it represents the ultra-short end of that band.
- *Residual basis* — the index omits the 3-12mo portion of the 0-1yr band, so it is shorter
  in average maturity than the full 0-1yr index. Yields track closely (the 1-3mo and 3-12mo
  T-bill segments move near-parallel except in steep-curve-inversion regimes).

**Depth-confirmed live (V1A AC3):** `fund_data.json` pull — HTTP 200, **7,285 daily points,
1997-05-19 → 2026-05-21, median inter-point gap 1.0 day.** ~29 years of clean daily history,
well past the portal ~6yr backbone. Artifact: `.runtmp/v1a_depth_bbutb13mtr.json`.

**Honest labeling** (carried into the corrected pull-spec): render as a representative index
— "Bloomberg US Treasury Bills 1-3 Month, representative of the 0-1yr Treasury band" — never
as the exact 0-1yr band.

### 3.2 Bloomberg 0-5 Year High Yield → ESCALATE

YCharts carries no Bloomberg HY maturity-band index — only the broad
`Bloomberg US Corporate High Yield` (`^BBUSCOHYTR`, full-maturity, average maturity well
beyond 5yr). Credit quality matches; **maturity does not** — the broad index has materially
longer duration than a 0-5yr short-duration HY target. Forcing it would be the "bad match"
the TO says not to force. No reasonable Bloomberg representative.

### 3.3 Bloomberg 0-5 Year TIPS → ESCALATE

YCharts carries no Bloomberg TIPS maturity-band index — only the broad
`Bloomberg US TIPS (Series-L)` (`^BBUTISTR`, full-maturity, average maturity ~7-8yr). Asset
class matches; **maturity does not** vs a 0-5yr short-TIPS target. No reasonable Bloomberg
representative.

### 3.4 Bloomberg 20+ Year Treasury → ESCALATE

YCharts carries no Bloomberg pure-Treasury 20+/long maturity-band index. The Bloomberg
Government/Credit maturity family tops out at 1-5yr. `Bloomberg US Long Government/Credit`
(`^BBUSLGCRTR`) is long-maturity (maturity dimension ~ok) but **includes investment-grade
corporate credit** — a credit-quality mismatch against a pure-Treasury target (it carries
credit-spread risk the pure-Treasury band does not). No clean Bloomberg representative.

## 4. The escalation — COO / Andrew ruling needed

For the 3 escalated bands (0-5yr HY, 0-5yr TIPS, 20+yr Treasury), Andrew's "representative
Bloomberg index on YCharts" cannot be met — YCharts' Bloomberg fixed-income coverage for
these segments is broad-parent-family only. The decision is COO/Andrew's, between:

- **(a) ICE cross-vendor maturity-band indices** — YCharts *does* carry maturity-segmented
  ICE indices (ICE US Treasury 1-3yr / 10-20yr / 20+yr; the C2-prestage cross-vendor brief
  `mdsrc-c2-bloomberg-ice-crossvendor-prestage-20260521.md` already mapped the 20+yr to
  `^ICEUT2YTR`). ICE indices give a *true maturity-band* match — better representativeness
  than a broad Bloomberg index — at the cost of being a different vendor. (Note: ICE has a
  Treasury and a TIPS 0-5yr index; ICE HY maturity bands need a confirmatory probe.)
- **(b) broad Bloomberg parent family** with an explicit maturity-representativeness caveat
  rendered on the portal (`Bloomberg US Corporate High Yield`, `Bloomberg US TIPS`,
  `Bloomberg US Long Government/Credit`) — keeps the Bloomberg vendor, accepts a maturity
  (and, for 20+yr, credit-quality) basis difference.
- **(c) keep these 3 on the Bloomberg pkl** — no YCharts migration for the 3 maturity-band
  bonds.

This brief does not pick — Andrew rejected the ETF-proxy and manual-Bloomberg; the
"representative Bloomberg index" path resolves only the 0-1yr band. The vendor-vs-fidelity
trade for the other 3 is a product/architectural call.

## 5. Pull-spec correction (AC4)

`docs/briefs/mdsrc-c2-pull-spec-prestage-20260521.csv` — the 4 maturity-band-bond rows
corrected: the superseded SHV/SHYG/STIP/TLT ETF-proxy resolution + the
`etf_proxy_disclosure` removed.

- Row 55 (0-1Yr Treasury): `^BBUTB13MTR`, `index`, `calcs=id:level`, verdict
  `meets-via-representative-Bloomberg-index`, readiness `READY`, representative-index
  honest-labeling note.
- Rows 56/57/60 (0-5Yr HY, 0-5Yr TIPS, 20+Yr Treasury): `yc_symbol` cleared, verdict
  `ESCALATED-V1A 2026-05-22` with the per-band finding, readiness
  `BLOCKED -- V1A escalation (COO/Andrew ruling)`.

## 6. Compiler Tools

V1A is a YCharts-entity sourcing task — no gold/portal/route/IAM/schema change; no comp-*
graph tool applies (per the TO `compiler_tools_mandate` note). Empirical self-checks:
Phase-1 — the resolved representative (`^BBUTB13MTR`) depth-confirmed live (HTTP 200, daily,
7,285 pts / ~29yr — PASS). Phase-2 — each of the 4 bands has a documented basis: 1 a
representativeness basis (maturity overlap + credit match + residual), 3 an explicit
no-representative-found escalation. PASS.

## 7. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — each of the 4 resolved to a representative Bloomberg index OR explicitly escalated | MET — 1 resolved (`^BBUTB13MTR`), 3 escalated as no-representative-found |
| AC2 — per band: representativeness basis documented (maturity overlap, credit match, residual) | MET — §3: the resolved band carries the full basis; the 3 escalated carry the per-band reason |
| AC3 — each chosen representative depth-confirmed live (HTTP 200, daily, adequate history) | MET — `^BBUTB13MTR`: HTTP 200, daily (gap 1.0d), 7,285 pts 1997-2026. The 3 escalated have no chosen index — AC3 N/A, escalated per AC1 |
| AC4 — the 4 C2 pull-spec rows corrected (ETF-proxy removed); brief committed; RAVC2 to COO + CC CTO | this brief + the pull-spec correction committed; RAVC2 on commit |
