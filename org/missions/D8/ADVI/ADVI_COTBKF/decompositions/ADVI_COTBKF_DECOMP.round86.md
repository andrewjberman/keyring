# ADVI_COTBKF decomposition -- ROUND 86 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the acceleration round

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL1`'s UN-PARK and acceleration ruling, `ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` @f984c02191, which answers
crossbox ORDER `XB-20261015T173406Z-d896` (`4.0.0_SA_CRO~DELL2`, revision 2). Authority, Andrew-direct 2026-10-15 ~17:3xZ, VERBATIM:
"Yeah I want to accelerate this project, I am fine with pushing yahoo finance harder, as well." and "Active accounts should get BBG pricing exclusively,
inactive accounts are fine with yahoo finance, that is probably the most reasonable way to handle these."
PRD v0.10, no addendum yet (the CTO lands one at L10 if the price-source contract needs it). Round 85 read MAY-CLOSE (`round-close-check.py`, GRADED PASS).

**Ruling items this round serves:** 1 (the first cell rebuilds the lost round-85 scripts) and 2 (the active set's full Bloomberg need, in cells, with a finish date,
ordered by value held). Item 3 (the inactive accounts' securities for the Yahoo leg), items 4 and 5 (labels, the porting test) and the Yahoo half of item 6 belong to
`2.0.0_SA_COO~Q1` (MDPF_DEMQUE): Q1's cell `DQ-t-64` (`MDPF_DEMQUE.TO-DQ-t64`, issued 2026-10-15 to worker `~56`) already measures the inactive-only set against the
Yahoo request cap, so a cell here would duplicate it. This round does NOT cut it; the COO~C1 reads Q1's census at the drain.

**Rule 24.** Domain: the ruling's items 1 to 3 and 6. Subtraction from the ruling's numbered items: item 1 -> CB-ch-1; item 2 -> CB-ch-2; item 6's Bloomberg-series
baseline -> CB-ch-2; item 3 and item 6's Yahoo baseline -> `DQ-t-64` (MDPF_DEMQUE, Q1's write surface); items 4 and 5 -> MDPF_DEMQUE. Uncovered members inside this
project: none.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ch-1` | the round-85 build scripts rewritten from `ACTIVE_SET_V2_RECORD`, committed, re-run from the commit; both files re-hash equal to `5cef7ab0...` and `0783f088...` | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~169` |
| `CB-ch-2` | the active set's full Bloomberg need: every non-cash CUSIP of V2 not already in the B1 or failed-14 requests, at option C depth, in cells; the day rate; the finish date; the order by value held, cut into one-day request slices | FWD-3 | LOCAL | none (reads the committed V2 file) | `0.9.0_WK_ADVI_COTBKF~170` |

**Fan-out:** `2 of 2 chains, cap 8`. No edge: ch-2 reads the committed V2 file by its pin, not ch-1's output (V2 is the pinned truth; ch-1 reproduces it). Write sets are disjoint
(one deliverables folder and one new script pair each). Both are read-only on S3 and on the vendor side: no draw, no `draw_hold` change, no request filed in the
DEMQUE tree by a worker. Filing the slices is the ISSUER's act at the drain.

**Hookups at the merge (the issuer's, one commit):** none expected; the new scripts are standalone.
