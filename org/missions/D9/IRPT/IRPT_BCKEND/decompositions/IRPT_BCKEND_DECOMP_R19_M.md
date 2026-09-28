# IRPT_BCKEND decomposition -- ROUND 19, WORKSTREAM ~M (2026-09-28, 2.0.0_SA_COO~M, on PRD ADDENDUM v0.18 @33ae74760b, CTO 102397)

Round 19's ~M rectangle is `STATUS~M.md` @e589729e6a's next-list, in its order. The thread is the Holdings journey
(FWD-5 backend half, goal criteria 1-3). Items 1-4 are cut now. Items 5-12 each wait on a named gate (item 1's result,
the enabled publication, the POSN fill, ~X's B1, ~D's C34) and are not cut for coverage alone. Base: CLOUD HEAD, which
carries the R4 Holdings code (bcf7a6adde) and every served ~M function's source (B3 read, MSTR 102400 / ~M reply).

| cell | next-list item | outcome served | risk | depends on |
|---|---|---|---|---|
| `IB-mr-1` | 1: R1 read-backs of the three HELD ledgers on the 2026-09-28 COT run | goal criterion 3 (COT soundness); clears or names the gate on items 7-8 | WORLD | none |
| `IB-mr-2` | 2-4: re-mint the three Holdings packages, one QA fire, fill the R4 ENABLE half | FWD-5 / goal criterion 3 (the cash rule reaches a publication) | WORLD | none |

Edges: none between the two cells (disjoint write sets; `IB-mr-2`'s steps are one chain inside one cell).
Sending the filled half to 1.0.0_SA_CTO and 4.0.0_SA_CRO is the issuer's act at the drain, never the worker's.
A FAIL on an R1 leg is graded and carried; its rollback or S173 re-point is the issuer's ruling at the drain.

Kept in its own file so the three workstreams write disjoint decomposition surfaces (the shared
`IRPT_BCKEND_DECOMP.md` carries ~P's section 13).
