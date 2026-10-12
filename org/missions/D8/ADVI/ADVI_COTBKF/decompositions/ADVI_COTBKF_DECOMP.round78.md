# ADVI_COTBKF decomposition -- ROUND 78 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-12T01:02Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-78 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_78_20261012.md` @e5d2fc8e59 (msg 6229; the hash read by this seat from the file's own history),
answering `3.0.0_SA_CVO` msg 6228 and REMEDIATION_v46 @d389aa8f85. Section 3 is this round's rectangle.

**Where the project stands (the analysis, sections 1 and 2).** 19 readers of the price store; one serves a value built from the
store's close, on its no-snapshot branch only; 47 such partitions (2026-04-22 to 2026-06-07) are served; on those dates the store's
close is the traded price. "No served figure carries the error today." **Row D2-S131 (BLOCKING, INERT) is accepted, and a ruling is
in force:** "neither act is cut, by any lane, until the fund basis is fixed and proven. No rebuild of a holdings partition dated
before 2026-06-08 for this firm; no consumer is attached to the minted table. This is a ruling on what is cut, read by the issuer;
nothing is built to enforce it."

**THE RULING BINDS THIS DECOMPOSITION.** No cell of this round, and no cell this issuer cuts until the row is lifted, rebuilds a
holdings partition dated before 2026-06-08 for this firm or attaches a consumer to the minted table. "Nothing is built this round."

**Rule 24.** Domain: section 3 lists two items of work and one prohibition (item 3: nothing is built). Two cells for the two items.
A third cell, the correction list, is the ISSUER'S addition and is said to be: section 3 names no list item, but the list is the
tracked place a seat reads what is open, and the ruling in force belongs in it the round it is given. Its item 1 words the causes
cell as "the list cell now running": no cell was running when the analysis arrived (round 77 was fully drained), and this seat
reads the phrase as the closed-list cell of round 76 carried to completion. Both readings are stated here for the CTO.

## Measured constraints (issuer)

1. **NOTHING IS BUILT, APPLIED, SERVED, RE-MINTED OR FETCHED.** Cell 1 reads local copies only. Cell 2 reads code, local copies and
   at most one store object for this firm, read-only.
2. **The flat-charge reading is tested, not adopted.** Round 76 read its seven dollar figures off the rows it explains. Cell 1
   fixes them in a file first and tests them on units that did not suggest them (the substituted funds' trades, and failing funds
   outside round 76's nineteen), against shifted constants and a uniform expectation.
3. **The cache is not the store.** Round 77 found an unadjusted close for all 15 funds in a vendor cache on one box. Cell 2 asks
   whether the STORE a build reads holds one, in which field, on which dates.
4. **Three places write a rule or a test first:** the test and closed list (cell 1); cell 2 reads and writes no rule.
5. **The list cell runs LAST.**
6. **Owed by the CTO on items 1 and 2, not a cell:** the PRD addendum that names the price basis per fund class, makes the minted
   table carry its basis in a field a reader can reject on, and states the proof; and the 2022 factor's addendum.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bz-1` | the causes of the trades that do not reproduce the price paid, to completion: the flat-charge reading stated first and tested on held-out units; every unit still off given a cause | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~148` |
| `CB-bz-2` | for each of the 15 funds, the store's field that holds the unadjusted close, and whether it is present for every date the back-fill reads; the fifteenth named with what it lacks | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~149` |
| `CB-bz-3` | the correction list brought current: the ruling in force, the causes, the store's field (the issuer's addition) | FWD-3 | LOCAL | CB-bz-1, CB-bz-2 | `0.9.0_WK_ADVI_COTBKF~150` |

**Fan-out:** `2 of 3 chains, cap 8` now; `CB-bz-3` starts when the other two have drained. `CB-bz-3` is a DIRECT-ACT cell (LOCAL,
mechanical only); the other two carry a judgment criterion and take L8 to L10.
