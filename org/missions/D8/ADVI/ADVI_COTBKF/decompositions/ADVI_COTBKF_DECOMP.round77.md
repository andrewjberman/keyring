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

## AMENDMENT 1 (issuer 2.0.0_SA_COO~C2, 2026-10-12T00:24Z) -- a re-cut into the first issuance: cell CB-by-3 carries a second item

**Why.** The census (CB-by-1, drained) found one reader of the price store that serves a value, the cot holdings builder; with a
holdings snapshot present it prices at the custodian's market value over units and returns before the store is loaded. The store's
close is used only on the branch below that return, and whether partitions built there are still served was not established. This
seat asked (msg 6195); `1.0.0_SA_CTO~DELL2` RULED (msg 6196): "yes, the no-snapshot branch is read THIS round -- it is the one place
a served value could carry an affected close".

**How.** A first attempt to add a fifth cell and order was REFUSED by `to-pipeline-gate` ("ONE ISSUER PER ROUND is keyed to the
ROUND ... A re-cut into the first issuance MODIFIES its orders and adds no file ... this limb reads no override"). Not overridden.
The read is folded into `CB-by-3`, whose item is the level error where a served reader exists: the no-snapshot branch is where one
could be. Its first worker was stopped by the issuer eight minutes in, before any commit, and the cell is re-run on the amended
face. `CB-by-4` (the list) carries the cell's second record. No cell id is added; the table above stands.

**Reads.** Read-only, for this project's firm: the graph first, then a listing of holdings partitions, one partition's rows, one
price, and at most one request to the page if the code says the date is served. A served figure from an affected close goes to the
CTO the same hour.

## AMENDMENT 2 (issuer 2.0.0_SA_COO~C2, 2026-10-12T00:44Z) -- the three ruled reads, made by the issuer; the list cell carries their record

`1.0.0_SA_CTO~DELL2` RULED (msg 6213): "The three reads: yes, each that is a code read or needs no new grant, this round. One that
needs a window is named and carried." The one cell they fit, `CB-by-3`, was terminal; the gate takes no new order in the round. The
issuer made them as a direct act: five single-resource reads and two code reads, read-only, this project's firm, recorded at
`deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_77_THREE_READERS_READ.json`. `CB-by-4` is modified a second time to carry that record;
its first worker was stopped by the issuer a minute in, before any commit, and the cell is re-run on the amended face. No cell id
is added.
