# ADVI_COTBKF decomposition -- ROUND 76 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T22:43Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-76 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_76_20261011.md` @8ae9f87cf2 (msg 5996), answering the round-75 slug (`3.0.0_SA_CVO` msg 5995)
and its grade file @0e95fc9cca. Section 3 is this round's rectangle: five items, one cell each.

**Where the project stands (the analysis, sections 1 and 2).** On the 12 purchase days the reviewer set the close against what the
custodian's own row shows was paid: the validated unadjusted close equals it on 12 of 12; the close the served table uses on 0 of
12, at a median of 0.76. "The served table marks those purchases at about three quarters of the cash paid, on the day they were
made. That is no longer a lead." Its limits: 12 purchases, 2 funds, 10 of 377 holders measured; 26 percent of the 936 purchase rows
of the 19 funds do not fit the unadjusted close, examined by nobody. **The instrument changes:** the reinvestment price reaches 34 of
270 fund series; the price paid on a trade reaches every fund ever bought or sold, from the custodian's own rows and with no fetch.
Nothing served has moved.

**Rule 24.** Domain: the five items of section 3 -> five cells. `CB-bx-3` depends on `CB-bx-1` and `CB-bx-2`; `CB-bx-5` (the list) on
the other four.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED, RE-MINTED, BUILT OR FETCHED.** "ONE issuance, on copies, counts and ratios only." No cell reads the
   bucket; cell 4 is arithmetic on the served copy and builds nothing.
2. **A front load makes a purchase's price paid sit above a right close.** So the fee cause of cell 1 decides what a failing row is
   in cell 3, and sales, which carry no front load, are the check on it in cells 1 and 2. Cell 3 waits for both.
3. **Cell 4 is the TRADE term only:** the cash of a trade against its shares at the served close, over the previous value. The
   holding carried at the served close is not revalued, and the record says so in its headline. It is independent of cell 1 by
   construction: its changes are split by the row's price fit, so a fee-sized gap is told from a quarter of the price.
4. **Three cells write a list, a rule or a quantity to a file before they look.** Cell 1 also runs one alternative order of its
   list, since order decided nine days in round 75.
5. **No account id leaves a worker's scratch.**
6. **The list entry's standing is carried without a new value in the `state` field:** `state` stays `OPEN`; the first words of
   `what` and the `lead` key carry "CONFIRMED ON 12, size open".
7. **The list cell runs LAST.**
8. **Owed by the CTO after cells 1 and 2, not a cell:** the fund-basis rule as a PRD addendum; the 2022 factor's addendum.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bx-1` | the 26 percent: the purchase rows of the 19 funds that miss the unadjusted close, a cause each from a closed list written first, under two orders | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~138` |
| `CB-bx-2` | the price-paid instrument over the whole table: the served close over amount per unit on every purchase and sale row of every fund, four bands, every denominator | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~139` |
| `CB-bx-3` | which funds: every fund series classed by its trade rows under a rule written first; set beside the reinvestment classes; the failing funds named | FWD-3 | LOCAL | CB-bx-1, CB-bx-2 | `0.9.0_WK_ADVI_COTBKF~140` |
| `CB-bx-4` | the return on trade days across every account: measured account-days changing by over 10 basis points when a trade is valued at what was paid | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~141` |
| `CB-bx-5` | the correction list brought current: the trade-day entry from a lead to confirmed on 12, size open | FWD-3 | LOCAL | CB-bx-1, CB-bx-2, CB-bx-3, CB-bx-4 | `0.9.0_WK_ADVI_COTBKF~142` |

**Fan-out:** `3 of 5 chains, cap 8` now; `CB-bx-3` starts when `CB-bx-1` and `CB-bx-2` drain; `CB-bx-5` when the other four have.
`CB-bx-5` is a DIRECT-ACT cell (LOCAL, mechanical only); the other four carry a judgment criterion and take L8 to L10.
