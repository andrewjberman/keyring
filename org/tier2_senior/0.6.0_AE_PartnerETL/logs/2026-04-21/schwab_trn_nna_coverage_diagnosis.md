# Session Log — Schwab TRN_NNA Coverage Gap Diagnosis

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21 (afternoon, post-ingestion commit `bea387a9`)
**Continues from:** `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/schwab_trn_nna_ingestion.md`

---

## Purpose

Andrew directed: "continue from your last session log with regard to sorting out the TRN_NNA
enrichment process." Last session shipped Layer A + Layer B (`bea387a9`) with parity harness
showing 2/6 months PASS vs the brief's AC#3 ±15% band. This session diagnoses why and decides
next action.

## Investigation

### 1. Diagnosed classified vs dropped Jul 2024 Layer A

149,838 rows, $510.38M gross. Kept 2,058 rows / $29.71M as NNA (inflow $19.91M + outflow $9.80M).
Top dropped buckets:

| Bucket | Rows | Gross |
|--------|-----:|------:|
| TRADE | 57,635 | $401.8M (correct drop) |
| BKSWP/BRSWP matched pair | 41,536 | $32.8M each, $0.001M net (correct drop) |
| DIV / interest / journal / fee / sweep | — | — (correct drops) |
| TRF BTWN SCH journals | — | filter matches **0 rows** (pattern doesn't appear in data) |
| **SECURITY TRANSFERS (1,490 rows)** | 1,490 | gross=$0.00, Q×P=$5.30M |

"Unknown" bucket (neither classified nor excluded) = $0.79M. Classifier isn't the gap source.

### 2. Hypothesis: in-kind ACATs with zero-price rows

SECURITY TRANSFERS / tran_code=TOA: rows store `quantity > 0`, `price = 0`, `gross_amount = 0`.
Schwab values these on their side using EoD price for NNA calculation; the TRN file itself
does not dollarize them.

### 3. Tested: price-join against RPS silver

Joined `SECURITY TRANSFERS/TOA` rows to `silver/RPS/.../closing_price` on `(cusip, trade_date)`:

| Month | Classifier only | + price-joined in-kind | PDF | Result |
|-------|----------------:|-----------------------:|----:|:------|
| 2024-07 | $19.91M (46%) | $60.74M (140%) | $43.40M | +$17.3M overshoot |
| 2024-10 | $59.19M (85%) | $110.23M (159%) | $69.50M | +$40.7M overshoot |
| 2024-12 | $73.66M (90%) | $177.92M (218%) | $81.80M | +$96.1M overshoot |

Same tran_code (TOA) covers intra-client re-registrations and share-class conversions —
Schwab excludes those from NNA without a "new money" flag that isn't in the TRN file.

### 4. Methodology root cause (from Schwab PDF glossary, p. 4)

> NNA includes Cash, TOA and FDIC.
> Market Impact: the remaining difference in asset balance change YoY that was not
> attributable to new/existing NNA funding.

Schwab computes NNA via position-delta (`CY − PY − market_impact`), not a TRN-row sum.
Our classifier is correct for cash-equivalent NNA; the gap is structural.

### 5. Coverage-correct reframe

The brief's AC#3 (±15% PDF parity) is unachievable by design. Reframe AC: Layer B captures
Schwab-visible cash/wire inflows that BD silver misses — **that's** the DS Phase 6 value.
The top 4 Dec 2024 missing-inflow events (Jessica Lindsey $20.1M, Stoneridge $17.4M, Petty
Trent $6.23M, Petty Mary $3.75M) all present in Layer B with stable `schwab_txn_key`.

## Artifacts

| Path | Action | Notes |
|------|--------|-------|
| `docs/briefs/ae-schwab-trn-nna-coverage-gap-methodology.md` | **New** | Diagnosis + 3 decision options + recommendation |
| `docs/data/schwab_trn_nna_contract.md` | **Updated** | Added "Scope — what Layer B covers (and does not)" section; replaced 85-90% parity claim with honest coverage table and methodology caveat |
| `/tmp/schwab_diag/*.py` | Diagnostics | 6 scripts — Jul gap breakdown, scope check, transfer hunt, price-join test, RPS schema inspection. Temp only. |

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| Diagnosis | N/A — read-only S3 parquet analysis; no pipeline mutation, no Lambda/EC2 deploy, no IAM change | comp-pipescript/iam/routes not applicable to this investigation scope |

Scope was pure coverage diagnosis and doc updates. No gold script changed, no runner touched.

## Current State

- Layer A + Layer B shipped `bea397a9`, 496 + 494 partitions (prior session)
- Parity harness output unchanged; interpretation now documented as methodology-bound
- Schema contract explicitly states Layer B scope and coverage expectation
- Methodology brief written for CTO/Andrew decision

## Next Steps

1. **[Andrew + 1.0.0_CTO]** Decide A/B/C in the methodology brief:
   - (A) Ship as-is → unblock DS Phase 6 now, document scope. **Recommended.**
   - (B) Build position-delta NNA from RPS silver now (blocks Phase 6).
   - (C) Keep tuning TRN classifier (not recommended; diminishing returns).
2. **[0.6.0_AE]** On (A) GO: MCP DS with "Layer B ready as-is, scope documented" +
   CTO brief link; hand off Phase 6 execution (C_01 6-tag merge with `schwab_txn_key`
   anti-double-count).
3. **[0.6.0_AE, if (A) accepted]** Future TO draft: position-delta NNA from RPS silver
   for total-firm reconciliation (separate workstream, not blocking Phase 6).
4. **[Housekeeping]** Drop the stale `TRF BTWN SCH` intra-Schwab filter from the contract
   doc since it matches zero rows — replace with a note that intra-Schwab exclusion is not
   separately labeled in our TRN corpus.

## Incidents / Lessons

1. **AC#3 was unachievable by design.** The brief claimed 85-90% parity from the PoC — it's
   real for some months but misleading overall. Future briefs with ACs against vendor-computed
   numbers should first confirm the vendor's methodology is compatible.
2. **Price-join on in-kind transfers overshoots by 2×+.** Same tran_code covers both NNA and
   non-NNA rows. Classifier tuning cannot distinguish them without a flag we don't receive.
