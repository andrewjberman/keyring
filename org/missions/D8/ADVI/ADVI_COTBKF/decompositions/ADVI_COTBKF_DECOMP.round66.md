# ADVI_COTBKF decomposition -- ROUND 66 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T11:10Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 4734 (2026-10-11 10:37Z), item 2: "Before any re-mint order: run r28 and r29 over all 3,325
days and print how many account-days change, three ways"; item 3: the re-mint covers exactly those days, under its own pair, capture
first; and msg 4772: the default stays `method_r28` until the CTO's addendum, written on this comparison. And on the issuer's own row
ADVI_COTBKF-D2-S113: the silver suite is red at the base on the account-id scan.

**Rule 24.** Domain: the two items above -> two cells, neither depending on the other (the comparison changes no tracked code; the
repair touches two test files).

## Measured constraints (issuer)

1. **`method_r29` is in the tree, selectable, not the default** (drained @803e5f2c14; issuer read of the default line at the base).
   The comparison names both legs explicitly.
2. **Nothing is served, re-minted or written remotely in this round.** The re-mint order and its pair come after the CTO reads the
   comparison.
3. **The comparison is gated by a positive control:** the r28 re-run must reproduce the served local table row for row before any
   difference is attributed to the rule.
4. **The suite is red at the base** (1 failed, 839 passed, 12 skipped; issuer run @5c27b0b1a5): 76 CUSIPs in the two price-request
   lists have an account id's shape; 0 are account ids. The repair keeps the set limb strict and bars path exclusion.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bn-1` | re-run the build locally under `method_r28` (control) and `method_r29`; class every account-day; list the changed dates; trace each change to its origin | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~97` |
| `CB-bn-2` | the account-id scan sets aside a shape hit that is a declared security identifier in a declared security list, never a set hit; the suite green | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~98` |

**Fan-out:** `2 of 2 chains, cap 8`. `CB-bn-2` is a DIRECT-ACT cell (LOCAL, mechanical only); `CB-bn-1` carries a judgment criterion
and takes L8 to L10.
