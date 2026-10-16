# ADVI_COTBKF decomposition -- ROUND 103 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- the Bloomberg-history fill, measured; the month categories made disjoint

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the CTO's grade of the round-102 census (msg 6633; `ledger/ROUND_ANALYSIS.round102.md`): FWD-3 is REALIZED on ACCEPT's terms (0 blanks lack a reason; the 93.7% blank rate, 98.3% of it UNPRICED, is stated beside it); 5 of 9 outcomes are REALIZED. Round 103:

1. "One read-only cell: which of the 3,059 listed securities came back priced from Bloomberg history, and how many of the 15,973,399 UNPRICED holding-days those closes cover. If any, the next round rebuilds under a pair."
2. "D1-S18: make the month categories disjoint."

**What the issuer measured first.** (a) Disjoint months: `deliverables/2.0.0_SA_COO~C1/cy2_month_partition.py` assigns every UNGRADABLE account-month to exactly one category: no daily returns 116; blank days all UNPRICED and no reported-side clause 72,184; blank days with at least one other reason and no reported-side clause 1,563; blank days with a reported-side clause 3,818; reported-side clause only 941; other 0; sum 78,622. So if every UNPRICED blank day were filled, at most 72,184 months could grade (the earlier range of 70,943 to 74,791 in row D1-S18 was an estimate; this is exact). (b) Bloomberg: the issuer's `cy1_bbg_coverage_check.py` re-counts the closes in the store a worker names and joins them to the unpriced holding-days; run against an empty prefix it prints objects=0 and 0 covered of 15,973,399, so a zero is a clean answer, not an error. Where returned Bloomberg history lives is for the worker to find and name from the DEMQUE and SECHIST records; round 102 found that no committed record carries a per-security outcome.

**Two cells, two chains, disjoint write sets** (each writes only its own deliverables folder and its own channel rows; no shared file).

**Rule 24.** Domain: the CTO's two round-103 items. Subtraction: item 1 -> `CB-cy-1`; item 2 -> `CB-cy-2`. Uncovered here by design: any rebuild or fill (the CTO: "if any, the next round rebuilds under a pair"), any Bloomberg pull (only through their queue, on Andrew's word), the CTO's grade.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cy-1` | read-only LOCAL: find where returned Bloomberg price history lives for Cottonwood, count what is there (objects, securities, points), say which of the 3,059 listed securities came back priced, and how many of the 15,973,399 unpriced holding-days and of the 4,371 unpriced securities those closes cover; no Bloomberg call | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~192` |
| `CB-cy-2` | read-only LOCAL: the UNGRADABLE months as disjoint categories, the overlap matrix of the clauses, and the exact upper bound of months a fill of every UNPRICED day could grade | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~193` |

**Fan-out (to state at the cut):** `2 of 2 chains, cap 8`.
