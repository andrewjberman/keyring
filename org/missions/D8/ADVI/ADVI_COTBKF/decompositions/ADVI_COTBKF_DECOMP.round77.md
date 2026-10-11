# ADVI_COTBKF decomposition -- ROUND 77 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T23:47Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-77 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` @1101e06fcd (msg 6154; the hash read by this seat from the file's own history),
answering the round-76 slug (`3.0.0_SA_CVO` msg 6152) and its grade file @d299fd357a. Section 3 is this round's rectangle: four
items, one cell each, "the first cell before anything else".

**Where the project stands (the analysis, sections 1 and 2).** The price-paid instrument was reproduced by the reviewer figure for
figure. Funds whose price the build did NOT replace: more than 20 percent off the price paid on 3,205 of 3,614 trades, on purchases
and sales alike: "It is the close." Funds whose price the build DID replace: within 1 percent on 10,411 of 10,636. **"A close at
three quarters of the traded price is a LEVEL error":** every value and every weight built from it is low by the same proportion on
every day. The question before any size: **is a value or a weight built from the affected close SERVED to anyone, and where.** This
project's own table is read by nothing released; the PRICE STORE the closes sit in is not this project's alone.

**Rule 24.** Domain: the four items of section 3 -> four cells. `CB-by-3` depends on `CB-by-1` (it sizes only what the census finds
served); `CB-by-4` (the list) on the other three.

## Measured constraints (issuer)

1. **NOTHING IS FETCHED, SERVED OR RE-MINTED** (the analysis's own last line of section 3). Cells 1 and 3 READ: code in the
   workspace and the portal, the dependency graph, and at most one served value per serving reader, for this project's firm.
2. **Another firm's data is never opened.** The price store may have readers that serve other firms. The census records that such
   a reader exists, with its class and owner read from the code; it reads no other firm's data.
3. **A reader that serves a figure from an affected close is filed as a row the same hour,** naming its owner (section 3 item 1).
   The worker cannot message; the row is the carrier, and the issuer relays the row to the CTO when the worker reports. Whether a
   client firm sees such a figure is told to Andrew by the CTO (section 5), not by a cell.
4. **The census prints its denominators.** Its zero is not an absence until the tool's census verb has run on the path; what it
   cannot see is part of the record.
5. **Cell 3 may come back empty.** If no reader serves from an affected close, nothing is sized, and that is a complete result.
6. **The merge of two list entries loses nothing:** both extents are carried under labelled keys and the evidence and unreconciled
   counts are printed before and after.
7. **Owed by the CTO after cell 1, not a cell:** the fund-basis addendum; the 2022 factor's addendum.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-by-1` | who reads the affected closes: the store and key of the 15 failing funds; every reader in the workspace and the portal, classed, with its owner; one read per serving reader | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~143` |
| `CB-by-2` | the 15 failing funds listed: trades read, median ratio, whether an unadjusted close is already held and whether it reproduces the price paid | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~144` |
| `CB-by-3` | the level error sized where the census finds a served reader, and only there: account-days and the share of value | FWD-3 | LOCAL | CB-by-1 | `0.9.0_WK_ADVI_COTBKF~145` |
| `CB-by-4` | the correction list: the trade-day entry and the holdings entry merged into one defect, an adjusted close used as a price | FWD-3 | LOCAL | CB-by-1, CB-by-2, CB-by-3 | `0.9.0_WK_ADVI_COTBKF~146` |

**Fan-out:** `2 of 4 chains, cap 8` now; `CB-by-3` starts when `CB-by-1` drains; `CB-by-4` when the other three have. `CB-by-2` and
`CB-by-4` are DIRECT-ACT cells (LOCAL, mechanical only); the other two carry a judgment criterion and take L8 to L10.
