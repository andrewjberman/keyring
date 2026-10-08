# ADVI_COTBKF decomposition -- ROUND 18 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-08 ~02:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-17 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_17_20261008.md` @0ae2f15e5c (msg 1185):
the ruling on D2-W35-S2 (a zero or negative prior-day value reads BLANK, `NON_POSITIVE_BASE`; its month UNGRADED) and E1 the rule
applied and re-graded, E2 the document index re-applied with page counts (SERVED, a pair), E3 the remaining flow-month DIFF classed.

**Rule 24.** Domain: E1-E3. One cell per item; MECE over the list.

## Measured constraints

1. The end rule blanks only a zero base (`ZERO_BASE`); about 26,903 days follow a negative prior-day value (row W35-S2).
2. The served index's `page_count` is 0 or null on all 11,119 rows; `page_counts.csv` (round 17, ~36) holds 11,087 counts and 32
   unreadable with reasons. The builder (`commonwealth_document_index.py`) applies with `--apply`, the issuer's act.
3. Graded flow months: 242 MATCH of 937, median |diff| 6.3 points; timing and tax withholding ruled out (round 17).

## The cells

| cell | item | serves | risk | slot |
|---|---|---|---|---|
| `CB-r-1` | E1: the non-positive-base rule in the end rule, re-graded before and after | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~37` |
| `CB-r-2` | E2: the index builder fills `page_count` from the counts; a local rebuild diffed against the SERVED index (only `page_count` moves) | FWD-5 | SERVED | `0.9.0_WK_ADVI_COTBKF~38` |
| `CB-r-3` | E3: every DIFF flow month classed by flow type and size; the largest class named with three accounts; no fix | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~39` |

**The E2 apply** is the issuer's act after the drain, under a never-widen pair (COO half by this seat, CTO half by
`1.0.0_SA_CTO~DELL2`), pins re-read at the apply, ledger opened and closed (the round-13 pattern). The worker never applies.

**Dependencies:** none between cells; write sets are disjoint (E1 the returns module, E2 the index builder, E3 a new analysis
script). E3 reads the chain as it stands at the cut. **Fan-out:** `3 of 3 chains, cap 8`.
