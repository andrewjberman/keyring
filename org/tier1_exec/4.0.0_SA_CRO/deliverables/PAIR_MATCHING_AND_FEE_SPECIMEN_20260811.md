# TASK-1 FOLLOW-ONS -- THE PAIR-MATCHING ENGINE + THE TPFEE/SMFEE SPECIMEN VERIFY

**Author:** 4.0.0_SA_CRO · **2026-08-11, 0706-0720Z** · **archetype:** IMPLEMENT + VALIDATE
**Commission:** Andrew-direct ("Proceed with the pair-matching engine and the TPFEE/SMFEE specimen
verify") -- the two required rows COO converted from my task-1 flags.
**Engine:** `org/tier1_exec/4.0.0_SA_CRO/scripts/pair_match_engine.py` (re-runnable; measured over
the full 525-partition series, 2.98M rows). **PII: aggregates/rates only; description samples masked.**

## A. THE SPECIMEN VERIFY: **FEE-MANAGEMENT-INFERRED upgrades to VERIFIED** -- and it bought a boundary gift

Measured over the full series (not one specimen account -- the whole family, which is stronger):

| code | rows / accounts | detail description (vendor text) | pattern | implied ANNUAL rate (last-12m fees / current value) |
|---|---|---|---|---|
| **TPFEE** | 76,643 / 6,521 | DEBIT legs: **"TO ADVISOR"** (38,456) · CREDIT legs: **"FRM ########"** (38,187, masked) | 1 row/acct/month median, 23 months | median **92 bps** (q25-q75: 71-103) over 4,881 accounts |
| **SMFEE** | 40,073 / 6,867 | **"TO SEP ACCT MGR"** -- 100% DEBIT | 1 row/acct/month | median **34 bps** (q25-q75: 28-35) over 5,108 accounts |
| MGFEE (explicit control) | 1,103 / 192 | "MGMTFEE TO ADVISOR" / "MGMTFEE FRM ########" | same TO/FRM two-leg shape | median 77 bps |

**VERDICT: VERIFIED.** The vendor's own detail text names the payee class ("TO ADVISOR" / "TO SEP
ACCT MGR"), the cadence is monthly-per-account, and the implied rates sit exactly at advisory-fee
(≈92bps) and SMA-manager-fee (≈34bps) scale. The inference is no longer inferred -- COO's
fact-by-attrition risk is retired by measurement, and the classification table's two rows re-grade
FEE-MANAGEMENT-VERIFIED (@ this commit).

**THE BOUNDARY GIFT (unplanned, load-bearing for sec2):** TPFEE/MGFEE are TWO-LEG movements --
client accounts DEBIT "TO ADVISOR" and matching CREDIT legs land "FRM {client}" in **advisor
collection accounts that are INSIDE the 7,239-account book.** So the fee credit legs IDENTIFY the
advisor/firm operational accounts mechanically -- exactly the accounts the performance-portfolio
boundary must EXCLUDE from client composites. The boundary definition (feasibility refinement cell
2) just gained a measured discriminator: **an account receiving FRM-fee credits is a collection
account, not client AUM.**

## B. THE PAIR-MATCHING ENGINE: cash measured both ways; in-kind inverted my first read -- honestly

**CASH journals/transfers** (21,372 rows, $398.1M; $JNL/$TYPE/TOA-FC): matched on (date, |amount|)
cross-account with opposite DEBIT/CREDIT --
- **MATCHED -> INTERNAL (both legs in-book): 3,560 rows (16.7%) = $193.7M (48.7% BY VALUE)** --
  fewer, larger events; the count-vs-value gap is why both denominators are printed.
- **UNMATCHED -> EXTERNAL-BY-DEFAULT: 17,812 rows = $204.3M** (TOA $86.1M, $TYPE $68.3M, $JNL
  $50.0M) -- counterparty not in the book. Residual caveat carried: same-day-different-amount
  splits and >2-leg journals (213 groups) stay unmatched and are COUNTED, never silently INTERNAL.

**IN-KIND transfers** (21,524 rows; TOA/T-A/TYP/DEL/REC-IC): **my first matcher run reported 0.0%
and the mechanism check showed the instrument, not the estate:** `debit_credit` on IC rows carries
**LONG/SHORT** (position side, not direction) and quantities are unsigned -- a direction-keyed
matcher structurally cannot fire (the could-not-have-said-otherwise class, caught before
publication). The MEASURED fact underneath: **20,319 of 20,482 (date, cusip, qty) groups involve a
SINGLE account (99.2%) -- the in-kind family is structurally ONE-SIDED IN-BOOK,** i.e.
**EXTERNAL-dominant: ACAT-class migrations to/from custodians outside the book** (top securities =
the ETF names clients transfer in with). Direction (receive vs deliver) for one-sided events is NOT
derivable from this table alone -- **named follow-up: corroborate via next-day position delta
(dim_position) or fact_trn's fuller fields at build** (REC/DEL are explicit; TOA needs the
corroboration).

## WHAT THIS SETTLES FOR THE TWR BUILD

The CONDITIONAL-BY-COUNTERPARTY bucket is no longer a bucket -- it is: **$193.7M measured INTERNAL
(cash pairs) · $204.3M cash + ~$28.4M in-kind (txn-priced) EXTERNAL-BY-DEFAULT · one named
direction-resolution follow-up (in-kind one-sided events).** Everything the sec4 flow ledger needs
is now measured or named. The engine is committed and re-runnable; its unmatched output is the sec10
lineage's unresolved-flow count by construction.

## BOUNDARIES

Cash matching is exact-amount same-day (splits/fees-in-transit stay unmatched -- conservative
toward EXTERNAL, the safe direction per the standard); in-kind value uses txn price where present
($28.4M of $51.8M priced -- zero-price rows carry qty-only until the position-delta pass);
the advisor-collection-account roster derivable from FRM-legs is NOT enumerated here (a boundary
build task, one groupby); classification-table JSON re-graded in this commit (INFERRED->VERIFIED,
two rows). CVO cert rides its queue.
