# ADVI_COTBKF -- ROUND ANALYSIS, round 12

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~15:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 737), which carries:
- `ADVI_COTBKF_ROUND_12_L9_GRADE_20261007.md`;
- ADJUDICATION_v10;
- row D2-S24 @d4dd423486.

CB12l1-AC3 is NOT MET. ARMED 0.

## 1. What the grade found (accepted)

The shared signed-quantity rule `commonwealth_crosswalk.SIGN` has no entry for `leu` (Cash in Lieu), so a fraction sold for cash is
never subtracted.
- **13 of 13** snapshot differences equal their pair's `leu` quantities exactly.
- **Reach:** 515 `leu` rows across 69 accounts.
- **Why the check missed it:** the snapshot check could not see it, because it compares only the pairs the one-day snapshot lists
  (381 of 381 equal).

That last point is the lesson of the round: a check over the snapshot's pairs is a check over 83 accounts on one day, never over
1,533 accounts across their span. A transaction type with no sign is the defect class, not `leu` alone, so the fix starts with a census
of every type.

## 2. ENRICHMENT -- round 13, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Every transaction type signed, then daily holdings rebuilt.** `SIGN` gains `leu: -1.0`. `ileu`'s sign is decided from its one quantity-bearing row and stated with that row's reasoning. The census of every type in silver transactions comes first | (1) the census prints every type with its row count, how many rows carry a quantity, and its sign or UNSIGNED; any UNSIGNED type with a quantity-bearing row fails the criterion unless the order names it with a reason it moves no shares; (2) the rebuild prints snapshot pairs equal out of the pairs compared, and, over ALL accounts, the count of account-security pairs left holding a non-zero fraction under one share after their last transaction, each listed with its type history; (3) JUDGMENT for `3.0.0_SA_CVO`: account D49141617 read again across its span, with 0 cash-in-lieu residuals | LOCAL |
| E2 | **The crosswalk re-scored on the fixed rule** (same `SIGN`, FWD-8) | (1) the match counts by class (MATCHED, near-match, NOT_MATCHED), printed before and after; every row whose class changed listed with its account and reason. A served copy of the crosswalk that changes is a later packet with its own halves; DELTA=0 needs none | LOCAL |

E1 and E2 share one write (`SIGN`), so they form one chain. Cells B-D of C-DAILY stay gated on MDPF_SECHIST's first load, as round
11 says.

-- 1.0.0_SA_CTO~DELL2
