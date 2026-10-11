# ADVI_COTBKF decomposition -- ROUND 68 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T13:28Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_68_20261011.md` @b3a272fffc (msg 5008), answering `3.0.0_SA_CVO` REMEDIATION_v38 @931dc9ea93.
Section 3 is this round's rectangle: five items, one cell each, in its order.

**Where the project stands (the analysis, section 1).** Three judgments MET; CB66bn1-AC2 NOT MET on one limb (the comparison was not at
the pin). **Nothing served moves in round 68.** No re-mint list exists; a re-mint comes under its own pair, after this round.

**Rule 24.** Domain: the five items of section 3 -> five cells. `CB-bp-4` depends on `CB-bp-1` (the chain runs clean) and `CB-bp-3`
(the spin-off result); the other four depend on nothing.

## Measured constraints (issuer)

1. **The spin-off claims change nothing at the served instant's pin.** At `2026-10-09T11:52:52Z` the split store lists 32 partitions (round 67's
   Proof A log and version listing); the four events landed 2026-10-10. So `CB-bp-4`, which the analysis words "with item 3's result
   applied", needs no mechanism to apply a claim: it confirms the four are absent at that pin and says so. A mechanism that honours a
   per-event claim is needed only for a mint at a LATER pin; that is not in the analysis's list and is NOT cut. It is stated to the CTO
   in the issuance.
2. **"The custodian's own price" may not exist before any of the four events.** A round-64 worker's record gives the custodian's
   mark store (the gold canonical holdings) a date range of 2026-06-08 to 2026-10-06, and the events are dated 2020 to 2025. The
   issuer has not read that store. `CB-bp-3` establishes which print is the custodian's and its range first; the ruling's own outcome
   for no held date is UNAPPLIED, named.
3. **The outlier set is 179, not 178.** Round 65's threshold table reads 179 measured rows above 10 percent on a base of 100.00 or
   more (57 above 100 percent, 122 from 10 to 100 percent). The analysis's 178 is 56 + 122: it leaves out the one day round 65 classed
   FORM. `CB-bp-5` classes all 179 and re-places that day independently.
4. **The five report inputs carry account ids.** `CB-bp-1` rebuilds them by a named step or prints a NOT AVAILABLE line; it does not
   commit them into the tree, where the project's own scan would refuse them.
5. **The mint adapter builds from the FWD-3 tables.** Whether a FWD-3 manifest is reachable from where `build` reads them is for
   `CB-bp-2` to report; it adds an argument if not.
6. **No served write, no re-mint, no vendor call, nothing written remotely in this round.**

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bp-1` | the regrade completes from a clean checkout with no extra flag; the as-traded price input is reproducible | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~101` |
| `CB-bp-2` | the mint adapter carries the split-store pin into the mint's manifest; `--apply` refuses without it; the verify of today's table is unchanged | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~102` |
| `CB-bp-3` | the four spin-off events: the reconstruction with the factor and without it against the custodian's own price; a claim per event | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~103` |
| `CB-bp-4` | `method_r29` against the served table at the served instant's pin, from a clean checkout; the dates a re-mint would replace | FWD-3 | LOCAL | CB-bp-1, CB-bp-3 | `0.9.0_WK_ADVI_COTBKF~104` |
| `CB-bp-5` | the 179 measured days above 10 percent on a base of 100.00 or more, classed by cause, the unclassed remainder printed | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~105` |

**Fan-out:** `4 of 5 chains, cap 8` now; `CB-bp-4` starts when its two dependencies drain. `CB-bp-1` and `CB-bp-2` are DIRECT-ACT cells
(LOCAL, mechanical only); `CB-bp-3`, `CB-bp-4` and `CB-bp-5` carry a judgment criterion and take L8 to L10.
