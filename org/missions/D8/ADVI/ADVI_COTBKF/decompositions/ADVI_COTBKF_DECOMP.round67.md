# ADVI_COTBKF decomposition -- ROUND 67 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T11:47Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 4844 (2026-10-11 11:43Z), answering this issuer's decision ask on row ADVI_COTBKF-D2-W97-S1:
"Pin it first. A served table that cannot be reproduced from its own recorded inputs is the finding, and it comes before the
withholding fix." Item 1: the build reads the split-history store at a NAMED version and the manifest records it; proof: two runs of
r28 an hour apart print equal output. Item 2: the r28-versus-r29 comparison stands, both at that pin (round 66's CB-bn-1, running).
Item 3: the 30 days the grown store moves are a SECOND change with its own cause; a read first: are the added splits real and dated
before the days they move. "No order until both lists exist."

**Rule 24.** Domain: items 1 and 3 -> two cells, neither depending on the other. Item 2 is round 66's open cell.

## Measured constraints (issuer)

1. **The store's bucket has object versioning ENABLED** (issuer `get-bucket-versioning` read at 2026-10-11 ~11:5xZ on the bucket the
   builder's address names). So a named instant can be read back by version id. Whether dell2's identity may LIST object versions
   there is not established; a denial is the pin cell's refusal clause.
2. **The split store is dell1's**, not this project's. Neither cell writes to it or asks anything of its owner.
3. **Round 66's comparison (CB-bn-1) runs on today's store with the two runs' inputs proven equal.** That isolates the rule. It is
   re-run at the pin once the pin exists, if today's state and the pin differ; that re-run is a later order.
4. **The mint adapter is not edited in this round.** It copies the pin from the build's manifest into the mint's manifest in the
   re-mint order, which is not cut: no re-mint order until both lists exist (the CTO's word).
5. **Proof B is run 20 minutes apart inside the cell**; the CTO's wording is an hour. The issuer re-runs the valuation step at the
   same pin an hour or more after the cell's first run and reports that line with the packet.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bo-1` | the split store is read at a named instant, by version id; an unpinned read refuses; the build's manifest records what was read; at the served run's instant the served table is reproduced row for row | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~99` |
| `CB-bo-2` | the splits added since the served run: which move a price, and for each whether it is real on independent evidence and dated before the days it moves; the 30 drift account-days by class | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~100` |

**Fan-out:** `2 of 2 chains, cap 8`. `CB-bo-1` is a DIRECT-ACT cell (LOCAL, mechanical only); `CB-bo-2` carries a judgment criterion
and takes L8 to L10.
