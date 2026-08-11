# BUILD TASK 1 -- THE SCHWAB TRANSACTION-CODE CLASSIFICATION TABLE + THE MATERIALITY VERDICT

**Author:** 4.0.0_SA_CRO · **2026-08-11, 0650-0705Z** · **archetype:** IMPLEMENT + VALIDATE
**Commission:** Andrew-direct ("Proceed with build task 1, the transaction code classification
table"), executing the GIPS feasibility run's task 1 under COO's task-1-first-and-alone ruling.
**Machine table (the artifact):** `SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json` beside this
file -- 187 code rows (tran_srcde x tr_cd x sb_cd), each carrying counts, |gross| and in-kind
magnitudes, date range, vendor category/description, the assigned partition, the RULE that assigned
it, and the rationale. **Universe: the FULL 525-partition series (2,982,720 rows, 2024-07-08 ..
2026-08-07) -- not a sample.** Code-level aggregates only; no account values.

## THE MATERIALITY VERDICT: **THE GIPS CONDITIONAL CLEARS**

The feasibility run's single conditional was: unresolved transaction codes are a hard stop if
material. Measured over the full window, after classification:

| Partition | codes | rows | cash \|gross\| | in-kind (qty x close) |
|---|---|---|---|---|
| INTERNAL | 125 | 2,773,011 | $7,517,495,920 | $10,530,057,049 |
| EXTERNAL-IN | 13 | 16,838 | $847,966,764 | -- |
| EXTERNAL-OUT | 8 | 14,942 | $559,586,250 | -- |
| EXTERNAL (direction per-code at build) | 5 | 2,694 | $3,266,959 | -- |
| CONDITIONAL-BY-COUNTERPARTY (resolution-ruled) | 10 | 51,272 | $398,052,362 | $2,661,368,216 |
| FEE-MANAGEMENT (explicit) | 5 | 4,552 | $1,881,590 | -- |
| FEE-MANAGEMENT-**INFERRED** (TPFEE/SMFEE) | 2 | 116,716 | $55,506,184 | -- |
| FEE-ADMIN | 9 | 2,597 | $34,305 | -- |
| **UNRESOLVED (incl. pending-specimen)** | **10** | **98** | **$3,183,473** | $0 |

**UNRESOLVED = 0.178% of book value ($1.789B, dim_balance 2026-08-07) and 0.226% of the 25-month
external-flow magnitude ($1.41B), spread over 98 rows in 10 low-frequency adjustment codes** (DPAJ,
DPINS-FC, AS1CR, DPCSH, ADJ, four dividend-adjustment singletons, WLES). Under any reasonable
ex-ante threshold this is IMMATERIAL -- **the hard-stop does not fire, and the GIPS DAILY-TWR
verdict @e323c1cfac stands unconditioned.** Per COO's sequencing ruling, the four waiting
refinement cells are now unblocked on a premise that held.

## WHAT THE FULL-SERIES BUILD CORRECTED (each a trap now documented in the table)

1. **The day sample undercounted the code universe 7.5x** -- 21 source codes on 2026-08-07 vs
   **157 across the series** (187 code x tr x sb rows). A sample-built table would have been badly
   incomplete; the full pull (64MB) was the right call.
2. **The vendor category is a FIRST CUT, not a classifier** -- the feasibility run's "near-1:1"
   reading sharpens: ~680K AUTO-BANK-SWEEP rows sit inside 'Deposits and Withdrawals' but are
   INTERNAL by the standard's own boundary rule (sweep/cash accounts are inside the portfolio), and
   the management-fee family hides in 'Deposits and Withdrawals'/'OTHER'. **Classification is BY
   CODE; category would have inflated external flows by billions.**
3. **The money column is `gross_amount`** -- `net_amount` populates ONLY trades + reinvestments
   (measured: $0.00 net on 1.9M cash rows). A build reading net_amount for flows computes zero
   external flow, silently. In-kind (Security Transfers) carry $0 in BOTH -- valued qty x
   same-date close per the standard's sec4, computed per-row in the table.
4. **Reinvestments are the EMPTY category** (RID/RIDA, 482K rows) -- vendor leaves category blank;
   the standard classifies reinvestment INTERNAL explicitly.

## THE TWO HONEST FLAGS RIDING THE TABLE

- **TPFEE/SMFEE = FEE-MANAGEMENT-INFERRED** ($55.5M / 116,716 rows -- the largest fee family):
  vendor description EMPTY; classified by code-name family, adjacency to the explicit MGFEE
  "ADVISOR FEE" codes, and magnitude plausibility (~$22M/yr on a $1.8B book = advisory-fee scale).
  **INFERRED-STRONG, specimen-verify at build** (one account's rows vs its billing schedule --
  cheap). If refuted they re-partition and materiality re-runs; even a full re-partition to
  EXTERNAL would be 3.9% of external magnitude -- it changes gross-vs-net returns, not feasibility.
- **CONDITIONAL-BY-COUNTERPARTY is resolution-RULED, not unresolved** -- the transfer/journal
  family ($398M cash + $2.66B in-kind: $JNL/$TYPE journals, TOA/T-A/TYP account transfers, DEL/REC
  in-kind moves) classifies PER EVENT by the boundary test: swb_from/to where populated, else
  cross-account pair-match on (date, amount/qty, +/-), extended to household boundaries by the
  fact_fam parse. **At this magnitude the pair-matching engine is a REQUIRED build component**, and
  the standard itself mandates exactly this (classify relative to the boundary, never from the
  label).

## HOW THE TABLE IS CONSUMED

The JSON is the machine artifact: `partition` is the coordinate axis (EXTERNAL-* / INTERNAL /
FEE-* / CONDITIONAL-BY-COUNTERPARTY / UNRESOLVED-*), `rule` + `rationale` carry the grounding,
INFERRED flags are in-band. The TWR engine's flow-ledger stage (standard sec4) filters
EXTERNAL-* + resolved-CONDITIONAL as CF(t); FEE-MANAGEMENT drives the gross/net pair (sec8);
UNRESOLVED rows surface in the sec10 lineage counts. Unknown future codes fail LOUD into
UNRESOLVED -- the table is a first-match rule list, not a frozen roster, and new codes inherit the
materiality discipline. Generated by `build_classification.py` (rule set in-file, re-runnable
against any partition range; preserved in scratchpad, promotable to the archetype's tree when COO
decomposes the build).

## BOUNDARIES

Classification rationale grounds on the standard's sec4 lists + vendor code descriptions + measured
magnitudes; 10 codes stay honestly UNRESOLVED pending specimens rather than force-fitted. The
in-kind valuation uses same-date closing_price (zero-price rows would understate -- unmeasured on
this pass, one check at build). Direction (in/out) for the 5 generic-EXTERNAL codes resolves
per-code at build via debit_credit. The gross-vs-net fee treatment of FEE-ADMIN classes is a sec8
POLICY choice for Andrew/CTO at build, not made here. This table is the CLASSIFICATION artifact;
wiring it into a TWR engine is the build lane's work under the archetype trigger.
