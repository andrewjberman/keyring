# Schwab TRN_NNA Coverage Gap — Methodology Note

**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Supersedes:** acceptance criterion #3 of `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md`
**Status:** Decision-point — Andrew + CTO

---

## TL;DR

The ±15% PDF parity band in the brief's AC#3 is **not achievable with a transaction-based
classifier**. Schwab's PDF NNA is computed via a position-delta method, not a TRN-row sum.
Our current Layer B (shipped `bea387a9`) is the best transaction-based estimate; the
remaining gap is structural. Recommend: (a) ship as-is for DS Phase 6 integration, (b) document
the scope clearly in the contract, (c) defer total-firm-NNA parity to a follow-up
position-delta workstream that uses RPS silver.

---

## Evidence

Schwab's 49 Financial Business Review Dashboard May 2025 PDF (`C:\Users\AndrewBerman\Downloads\...`)
glossary (p. 4):

> NNA includes **Cash, TOA and FDIC**.
> Market Impact: the **remaining difference in asset balance change YoY** that was not
> attributable to new/existing NNA funding.

That phrasing is a position-delta method: Schwab measures CY vs PY asset balances, subtracts
a market-movement estimate, calls the remainder NNA. It is **not** a sum over labelled TRN rows.

## Our TRN-based classifier coverage

Current Layer B rules (`convert_schwab_trn_to_nna_silver.py`) vs PDF `Inflows`:

| Month | PoC inflow | PDF inflow | Coverage | Verdict (±15%) |
|-------|-----------:|-----------:|---------:|:---------------|
| 2024-07 | $19.91M | $43.40M | 45.9% | FAIL |
| 2024-08 | $27.86M | $40.90M | 68.1% | PARTIAL |
| 2024-09 | $15.94M | $23.80M | 67.0% | PARTIAL |
| 2024-10 | $59.19M | $69.50M | 85.2% | PARTIAL |
| 2024-11 | $20.38M | $28.90M | 70.5% | FAIL |
| 2024-12 | $73.66M | $81.80M | 90.1% | PASS |

Outflow coverage runs 65–94%; generally closer because outflows are mostly cash (WIRE / CHECK / IRS_WH).

## Where the unclassified dollars go

Diagnostic on Jul 2024 Layer A (`/tmp/schwab_diag/*.py`):

- `TRADES` ($402M) — correctly excluded (securities trades, not NNA).
- `AUTO BANK SWEEP BKSWP / BRSWP` ($32.8M each, $0.001M net) — sweep round-trip; correctly excluded.
- `TRF BTWN SCH` journals — filter matches 0 rows (pattern never appears in data).
- **`SECURITY TRANSFERS` (1,490 rows, gross_amount=$0)** — in-kind ACAT rows where Schwab stores quantity but price=0. Classifier drops them.
- Everything else combined (`JOURNAL`, `STOP CHECK`, `CDMT`, `PDRTN`, `NON-QUAL DIV`, etc.) = $0.79M — noise.

## Price-join test (would including in-kind TOA close the gap?)

I joined `SECURITY TRANSFERS / tran_code=TOA` rows against RPS silver `closing_price` on
`(cusip, trade_date)` to dollarize them:

| Month | Classifier only | + in-kind Q×P | PDF | Over/under |
|-------|----------------:|--------------:|----:|:-----------|
| 2024-07 | $19.91M (46%) | $60.74M (140%) | $43.40M | **+$17.3M overshoot** |
| 2024-10 | $59.19M (85%) | $110.23M (159%) | $69.50M | **+$40.7M overshoot** |
| 2024-12 | $73.66M (90%) | $177.92M (218%) | $81.80M | **+$96.1M overshoot** |

Blowing past the PDF by 2x+ on heavy-ACAT months. Interpretation: many SECURITY TRANSFERS/TOA
rows are intra-client re-registrations (trust ↔ personal), share-class conversions, or other
non-NNA re-titling — all captured under the same tran_code. Without Schwab's proprietary
"is this new money" flag (which isn't in the TRN file), we can't cleanly separate them.

**Naive price-join is worse than leaving the category out.**

## Conclusion

- The Layer B classifier is correct on what it covers (cash-equivalent flows — wires,
  MoneyLink, deposits, check movement, cash-component ACATs, IRS withholding).
- The classifier systematically undercounts vs Schwab PDF because Schwab's methodology
  includes in-kind ACATs valued at market, which the TRN file itself cannot dollarize
  unambiguously without a "new money" flag we don't receive.
- Schwab's PDF number is best matched by a **position-delta method** on RPS silver:
  `NNA = (EoM_market_value − BoM_market_value) − market_impact`.

---

## Decision Options

### (A) Ship as-is for DS Phase 6 integration [RECOMMENDED]

- Layer B stays as it is (`bea387a9`). DS Phase 6 (`C_01.canonical_nna.py` 6-tag merge)
  proceeds: `bd` / `bd_lagged` / `bd_delayed` / `schwab_imputed` / `bd_diff_flagged` / `bd_only`.
- **Value prop preserved:** DS Phase 6's purpose is imputation of BD's missing transactions —
  high-signal cash/wire/ACH events with known dollar values. All 4 top-missing Dec 2024
  events (Jessica Lindsey $20.1M, Stoneridge $17.4M, Petty Trent $6.2M, Petty Mary $3.75M)
  are captured cleanly in Layer B.
- **AC#3 revised:** reframe from "match Schwab PDF ±15%" to "capture Schwab-visible
  cash/wire inflows that BD silver missed." That's the real business value.
- **Contract updated** to state Layer B scope clearly: covers cash-equivalent flows only,
  **does not** reproduce total-firm NNA per Schwab's position-delta definition.
- Follow-up TO (separate): position-delta NNA from RPS silver for firm-level reconciliation.

### (B) Build position-delta NNA now

- New silver layer `03_silver/NNA_POS/` computed from RPS deltas + market-move subtraction.
- Bigger engineering effort (need a per-account per-period price-change attribution model);
  depends on deciding how to estimate market impact per Schwab's undocumented methodology.
- Would block DS Phase 6 behind this new work.

### (C) Leave AC#3 as-is and keep tuning

- Tried exhaustively; diminishing returns. Price-join overshoots by 2x; other lever candidates
  (intra-Schwab filter widening, additional tran_code inclusions) move the needle <$1M.
- Not recommended.

---

## Recommendation

Ship (A). Unblock DS Phase 6 immediately. Open a separate TO for position-delta NNA
(scoped vs market-impact methodology) when firm-NNA parity reporting becomes a portal need.
