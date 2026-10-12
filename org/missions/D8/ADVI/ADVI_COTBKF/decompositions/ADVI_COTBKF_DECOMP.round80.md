# ADVI_COTBKF decomposition -- ROUND 80 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-12T02:53Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-80 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_80_20261012.md` @7bfd7c4664 (msg 6406), answering `3.0.0_SA_CVO` REMEDIATION_v48 @222ab69461.
Section 3 is this round's rectangle: "two read cells, nothing built"; section 4: the correction list "is re-cut after item 2".
PRD v0.10 @4d488ab2f0, as the tool printed it at the cut: `ADMITTED`, ratified-text `SIGNED 3.0.0_SA_CVO current`.

**THE RULING ON ROW D2-S131 BINDS THIS DECOMPOSITION.** No rebuild of a holdings partition dated before 2026-06-08 for this firm; no
consumer attached to the minted table. Nothing is built, re-priced or re-minted this round. Nothing on dell2 fetches a price.

**Rule 24.** Domain: the two items of section 3 and the list of section 4 -> three cells.

## Measured constraints (issuer)

1. **Cell 1 is first and runs now.** A held, SERVED day carrying a split-sized error goes to the CTO the same hour (the analysis);
   the worker reports it first and the issuer carries it.
2. **Cell 2 is HELD ON AN EXTERNAL ACT:** dell1's demand queue landing the 15 funds' closes (request
   `ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012`, quoted at 23,340 cells, finish 2026-10-12, accepted from this side; whether and
   when it runs is dell1's). The issuer starts the cell when dell1 says the closes have landed, and amends the order with where
   they are if the code does not name it. It is a READ; "No re-mint is cut on it".
3. **The reviewer's wording rule binds cell 2** (CTO msg 6388): if no held fund split, the split-undone property rests on dell1's
   word alone and the record says that, never "the split arm passed".
4. **The list cell runs LAST,** after both.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cb-1` | row D2-W152-S1: the equities off the store row: held and served days, four ratios to the price paid, split dates, the cause | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~155` |
| `CB-cb-2` | when dell1's closes land: held trading days present of 20,718 per fund; the 14 funds with trades against the price paid from dell1's column | FWD-3 | LOCAL | none (held on dell1's landing, an external act) | `0.9.0_WK_ADVI_COTBKF~156` |
| `CB-cb-3` | the correction list re-cut: v0.10, the lander, the two reads | FWD-3 | LOCAL | CB-cb-1, CB-cb-2 | `0.9.0_WK_ADVI_COTBKF~157` |

**Fan-out:** `1 of 3 chains, cap 8` now (`CB-cb-1`); `CB-cb-2` starts on dell1's landing; `CB-cb-3` after both. `CB-cb-3` is a
DIRECT-ACT cell (LOCAL, mechanical only); the other two carry a judgment criterion and take L8 to L10.
