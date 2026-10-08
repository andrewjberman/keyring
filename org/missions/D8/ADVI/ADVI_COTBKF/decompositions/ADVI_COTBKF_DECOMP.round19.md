# ADVI_COTBKF decomposition -- ROUND 19 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-08 ~09:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-18 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_18_20261008.md` @04b347e9ea (msg 1237):
the ruling on D2-W39-S1 (the FDIC sweep is cash; its buys and sells are INTERNAL; sweeps come from a declared, versioned list with a
source per CUSIP; a security not on the list is never cash) and E1, the list and the rule, re-graded.

**Rule 24.** Domain: E1. One cell.

## Measured constraints

1. A withdrawal is delivered as an `lo` of CFNCASH plus a same-day `sl` of the FDIC sweep for the same amount; the value drops twice
   the flow in 74 of 106 single-`lo` months of the largest DIFF class (round 18, row W39-S1).
2. Cash today is `commonwealth_crosswalk.is_cash`, a prefix rule (`FDIC*` or `CFNCASH`). The ruling replaces inference with a
   declared list for the returns chain. The crosswalk's own use is left untouched: it serves the applied crosswalk table.
3. Round 18's real run: 1,685 MATCH / 1,931 DIFF / 78,977 UNGRADABLE.

## The cell

| cell | item | serves | risk | slot |
|---|---|---|---|---|
| `CB-s-1` | E1: `commonwealth_sweeps.py` (declared list + rejected candidates); sweep buys and sells INTERNAL and the sweep counted as cash in the valuation and returns; re-grade before and after, the 74 months named, a no-sweep control | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~40` |

**Fan-out:** `1 of 1 chains, cap 8`.
