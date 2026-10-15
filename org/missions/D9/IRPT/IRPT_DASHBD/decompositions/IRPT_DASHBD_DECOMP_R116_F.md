# IRPT_DASHBD round 116 -- workstream ~F2 (F-SHIP) decomposition: the filled-report export wire conformed to the server's names

Issuer `2.0.0_SA_COO~F2`, 2026-10-15 ~06:0xZ. Gate key: `<round>116</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 116**.

**Answers:** the CTO's ruling on call f50a (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_F50A_FILLED_REPORT_EXPORT_PIN_SERVER_SIDE_20261015.md`, msg 8105): the server pins the filled
object at submit and "the portal's export wire (`~F2`) sends the client id only". The record behind the call is `deliverables/2.0.0_SA_COO~F2/EXPORT_PIN_SEAM_R116.md` @d24953671c.

## What was measured

Round 115's proposed wire (`performance_source: {path: 'FILLED_REPORT', client_id}`) carries no pin field, so the ruling needs no removal. It does not match the server's merged names: the server's
freeze tests feed `{"filled_report_source": {source_kind, client_id, ...}}` and `FILLED_REPORT_KIND = "filled_report"`. `~P2` builds the submit handler's call in a build amendment, and a page that
sends the server's own names is the one that needs no translation there. The cut is three source files and one test file on the candidate branch.

## Cell

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The WIRE: the page sends `filled_report_source: {source_kind: 'filled_report', client_id}` at the top level of the submitted `wireBundle` and nothing else; no `performance_source` for a filled export; `filledReportSource.ts`, `submit.ts`, `ExportButton.tsx` and the round-115 export test updated | `DB-f-505` | FWD-21 | LOCAL (portal branch only, never pushed), DIRECT-ACT (about 50 lines of source; one cell; no L8 to L10, the close is the issuer's one real run) | none | R116-F-A |

**Decisions inside this decomposition (the issuer's, stated):** (a) the field is a sibling of `performance_source` on the submitted body, the place the server's freeze reads a source from; the exact
request location is `~P2`'s to confirm when its handler lands, and a different location is a one-line change in `submit.ts`; (b) round 115's checker `p115_export.py` AC1 names the token `FILLED_REPORT`, which
this cell removes: that token list is amended in the same commit to the new names (`filled_report`, `filled_report_source`), recorded in the commit, so the criterion the round-115 candidate "passes at its own head"
still reads true at the head that is registered; (c) no pin field is added anywhere (the ruling); (d) the cell is direct-act: it is under the size floor, LOCAL, one cell.

**Four-postulate record.** (i) Domain: three files in `export/` and one test file, portal branch only. (ii) Same grain: one request body. (iii) One intent: the page names the client and the server pins. (iv) Not moved: the
tab, the reader, the print, `index.tsx`, the route, the contract, every PATH A and PATH B body.

**Chain read.** M = 1. N = 1.

fanout: 1 of 1 chains, cap 8, portal_ref: `cand/dell2/irpt-default-performance-report` (506a2302d74ee95d7bbcf9d3dd73ab72ef1a2c2a), reason: one direct-act cell with a single write set. Worker `0.9.0_WK_IRPT_DASHBD~505` (`DB-f-505`, worker-light).

| criterion | invocation | base reading |
|---|---|---|
| DBF116-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r116/p116_wire.py . DBF116-1-AC1` | FAIL (no file on the main tree; on the candidate head `source_kind` is absent) |
| DBF116-1-AC2 | `... p116_wire.py . DBF116-1-AC2` | FAIL (no change from the candidate head) |
