# AMGT_CORPUS -- L5 decomposition v49.1 -- ROUND 49 (the round-48 analysis's enrichment list: every value under its own block's header -- period grids, case tables, an unread block with a why; a text cell by what it is; /14's redeploy; FWD-20's last served census)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-11 ~23:2xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-48 analysis `ledger/ROUND_ANALYSIS.round48.md` (msg 4158) and its ADDENDUM 1 (msg 4165: full width confirmed; period block vs case table
vs unread), over `3.0.0_SA_CVO` slug msg 4157 (ADJUDICATION_v63 @400c84ed5c). REALIZED 21 of 22; open FWD-20 (PARTIAL: C-S64 ARMED, C-S65 INERT).
Round 48's decomposition kept as `AMGT_CORPUS_DECOMP.round48.md`. v49.0 -> v49.1: the row class and field are `BLOCK` / `blocks` (not "case"), each block carries a `kind`.

## 0. What this round IS

| # | item (analysis s.3 and ADDENDUM 1) | cell | executor | risk |
|---|---|---|---|---|
| 1 | **C-S64, the reader.** Every value is served under the header row of ITS OWN BLOCK as the sheet wrote it: a block headed by periods is a PERIOD grid, a block headed by non-period words is a CASE table, a block whose header the reader cannot read is UNREAD (out of both, with a why); method /15 | `CRPS-ay-1` | worker `0.9.0_WK_AMGT_CORPUS~1` (lib) | LOCAL |
| 2 | **C-S64 the portal render, and C-S65.** The Model tab renders each served block under the sheet's own headers (an unread block as its labels and the why); a text cell prints by what it is (error token -> the why in words; the team's word verbatim; `--` only for an empty cell) | `CRPS-ay-2` | worker `0.9.0_WK_AMGT_CORPUS~2` (portal) | LOCAL |
| 3 | the /15 dossier write over the 95 names, its own never-widen pair, read leg v against /14 | `CRPS-ay-3` | the issuer's paired served act (after ay-1 merges) | SERVED |
| 4 | **the carried act:** the /14 redeploy of `opal-amgt-scoped-api`, AMGT_RESAPP round 99's first cell, under `NEVER_WIDEN_ROUND48_AX7` (CTO half SIGNED msg 4139). If `ay-3` reads Branch A before R1 cuts round 99, the CTO may rule that round 99 carries /15 in its place | `CRPS-ay-4` (carried; not this issuance's act) | `2.0.0_SA_COO~R1` / `0.7.0_AE_CloudOps~RA1` | SERVED |
| 5 | **FWD-20's last served census** on the live function and the DEV-built page: the BLOCK rows split three ways with their denominator, three browser walks (a second PERIOD block, a CASE block, a master template), 0 values under a header that is not their block's own; the issuer disarms C-S64 on that read | `CRPS-ay-5` | the issuer's read | LOCAL (read) |

**Chains:** `ay-1 -> ay-3 -> ay-4' -> ay-5`; `ay-2 -> ay-5` (the portal candidate is reviewed by the CTO before DEV); `ay-4` is carried. `fanout: 2 of 2 worker chains (ay-1, ay-2), cap 8`.
The two worker cells write disjoint surfaces (lib vs portal); they meet only at the served shape of section 1, which both faces state in full.

## 1. The served shape (the contract both worker faces carry; method `amgt-corpus-dossier/15`)

**Principle (CTO ADDENDUM 1).** Every value renders under the header row of ITS OWN BLOCK, as the sheet wrote it. A block whose header names periods (any years, quarters or `E`
forms) is a period grid aligned to THAT block's periods and is never made a "case table", even when its years differ from the main grid's. A block whose header names non-period
words is a case table under those words. A block whose header the reader cannot read stays out of both, with a why.

**Measured population** (the issuer's reference reader over the stored workbooks, nothing written; `evidence/r49_case_scope_census_20261011.txt`): the defect sits on all 32 own sheets
and all 63 master templates, 3,103 rows, and outside those rows no label, number or value moves. The CVO's 62 rows on 13 names are the text-separator subset.

**A BLOCK row** is a counted row (label + two or more numbers; the reader's existing rule) after the sheet's period header, that the period grid would misread, meeting (a) or (b):
- (a) **a value under another header.** A value cell in a period column of the row lies in a column whose most recent HEADER RUN above it (a raw sheet row's run of three or more
  adjacent period labels: integer years rising by exactly one, or text forms `2026E`, `FY26`, `1Q26`, `Q1 2026`, `2026Q1`, `1H26`, `H1 2026`) carries a period other than the period
  header's year in that column. A run that repeats the period header's years changes nothing. A control row (`EQY_FUND_YEAR`, `*_OVERRIDE`) is never a header and never a BLOCK row.
- (b) **a label inside the period columns.** A period column of the row holds a text cell that has at least one letter, does not start with `#`, is not one of `NA`, `N/A`, `NM`, `n/a`
  (any case), and is not a range such as `2.5%-3.1%` or `12.4x-15.6x` (it does not match `^[0-9.,%x -]+$`).
A row with only error tokens (`#N/A`, `#VALUE!`, `#N/A N/A`), `NA`/`NM` words or ranges in its period columns and every figure under the period header stays a FIGURE row, byte for byte.

**A block** is the band a BLOCK row belongs to: from its topmost header-like raw row (a TITLE row: every non-empty cell is text; or a YEARS row: a header run) that is adjacent above and is
not a counted row, down through the contiguous BLOCK rows and the non-blank uncounted rows after them, ending at the first blank raw row or at a counted row that is not a BLOCK row.
A BLOCK row with no header-like row adjacent above joins the block before it when no counted row lies between them. A block holds no counted row of another class.

**A block's kind:** `case` when one of its uncounted rows is a TITLE HEADER (two or more non-empty cells, every one a word: alphabetic text, not an error token, not `NA`/`NM`, not a
range, not a period label); else `period` when one of its rows is a YEARS row; else `unread`.

```
team_sheet (a class own_new / own_model / master name that has at least one BLOCK row; a name with none is UNCHANGED, key for key)
  row_classes[i]      "BLOCK" for each BLOCK row (FIGURE / HEADING / CONTROL as today)
  row_values[i], row_formats[i]   null for a BLOCK row
  row_counts          the three round-46 keys as today, PLUS "BLOCK": <n> only when n > 0; the values sum to len(rows)
  blocks              present ONLY when there is at least one BLOCK row; a list in sheet order:
    { "first_row": <1-based sheet row>, "last_row": <1-based>,
      "kind": "period" | "case" | "unread",
      "why": null | "The sheet gives these values no column header the reader can read, so they are not shown."   (the words, for unread only),
      "withheld": <count of numeric cells of body rows that have no header-like cell above them in their column within the block; each is served as null>,
      "columns": ["B","C",...],                         # column letters, leftmost to rightmost non-empty cell over the block's rows; [] for unread
      "rows": [ { "row_number": <1-based>,
                  "kind": "title" | "years" | "body",    # years: a header run; title: every non-empty cell is text; body: otherwise
                  "block_row": <true when this raw row is one of the BLOCK rows above>,
                  "cells": [ null | { "v": <the saved value verbatim: number or text>, "f": <the cell's Excel number format, numbers only> } per column ]   # [] for unread
              } ] }
```
Every raw row `first_row..last_row` that has a non-empty cell is listed, in order; a blank raw row is not. Values are read as the reader's `_verbatim` reads them. `row_numbers[i]`
of a BLOCK row is its sheet row, and that row appears once, with `block_row` true, in exactly one block. A master answer keeps its class and blocks but carries no figure: a numeric
cell that is not part of a header run is null.

**The portal** reads `blocks` and `row_classes` `"BLOCK"`; a payload without `blocks` builds the sheet it builds today, byte for byte. An unread block prints its rows' labels and its
`why`, never a value.

## 2. The reads (what each prints)

- **ay-3 leg v** (`checks/round49/ay3_diff.py`, the issuer's): every field of every name classed against /14; CHANGED on `team_sheet` only; DROPPED 0; per name the BLOCK row count, the
  blocks by kind and the withheld cells; every row outside the BLOCK rows byte-equal to /14; the 62 text-separator rows all BLOCK; the stored field equals a fresh `rows_for`.
- **ay-5** prints, on the live function and the DEV-built page: the capture's CodeSha256 and LastModified; the FIGURE rows by source (the round-48 census); the BLOCK rows split
  period / case / unread with the denominator; **values rendered under a header that is not their block's own: 0**; the text cells by class (error / word / empty) and none unclassed;
  the `aw4_compare` line at the served method; and three browser walks (a second PERIOD block, a CASE block, a master template).

## 3. Not in round 49

The 10 files in 6 unresolved folders; vocabulary growth; the PROD release of the portal (Andrew's `e7f2`, the av-2 hold stands until FWD-20 reads REALIZED on DEV); the payload duplicate
(routed to AMGT_RESAPP, CTO msg 4113); the long label column and the clipped table (C-S66, accepted); any change to the 13:00Z fire.
