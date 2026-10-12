# IRPT_ANLREQ -- decomposition, round 16, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** PRD v0.4 @4b1447e2cc (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`): CONTRACT C-STOREDINPUT and the ROUND-16 ENRICHMENT LIST, five items in order; ratified-text
half signed @60d5149e31 with two additions the CTO took (msg 6304): a test that pins the reader's output on the fixtures to its
version constant; and the count comes to the CTO BEFORE the re-land is cut, with one more column (for each stored input the new
reader would turn back, whether a report has been generated from it and when last).

**Thread:** FWD-1 is not live. Nothing of the upload check is on the trunk (reverted @114c77fb01).

## How the five items map

| item | carrier |
|---|---|
| 1. the count FIRST, read-only | cell `AR-y-161` builds the counting script and proves it offline; the count itself is ONE read-only Tier-2 order the issuer cuts to the seat that holds the decrypt, in the next served-read window; its result goes to the CTO, who rules what is done about each turned-back input |
| 2. the reader's re-land on C-STOREDINPUT, with the reviewer's two repairs and the version-pin test | cell `AR-y-162`, NOT SPAWNED until the count is with the CTO and it has ruled (msg 6304: "before the re-land is cut") |
| 3. row `TCKT_VNEXT-D2-S48`: one read, then a cell | the read is cell `AR-y-163`; the cell is cut from it at the next issuance, on the CTO's rule |
| 4a. `commentary_sent` on the ticket page | cell `AR-y-164` builds the display and the one-time control on a portal candidate; the control's first LIVE press is its own pair, the issuer's, not this cell |
| 4b. arm F2 on the original-file route | the read the CTO named first (the route's rule and trusted headers; which instrument they allow) is cell `AR-y-165`; the arm and its pair are the issuer's, written on it |
| 5. not cut | SUBTOTAL, SUM, ALL (parked); the form sending `commentary_requested` (waits on IRPT_BCKEND's release) |

**Standing, not a cell (row `IRPT_ANLREQ-D2-W53-S9`, owner this seat):** no rebuild of `irpt-ycharts-generate` is cut by any lane until
each of its four unpinned members is pinned or released under its own pair.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-161` | a read-only counting script, proven offline on synthetic stored inputs: stored inputs by lane; template inputs the NEW reader would read differently, by cause; for each turned-back input whether a report was generated from it and when last. Counts and dates only | the worker's deliverables | LOCAL |
| `AR-y-162` | the reader's findings, words and first answer re-landed ON C-STOREDINPUT: the stored template records the reader's version; `read_input` compares only on an equal version; the two repairs of row `IRPT_ANLREQ-D2-S64`; a test that pins the reader's fixture output to its version | `infra/aws/lambda/investor-reporting/intake/template_reader.py`, `infra/aws/lambda/investor-reporting/intake/uploads.py`, `infra/aws/lambda/investor-reporting/ops/status.py`, intake test files | WORLD (the path's floor; BUILT, not released) |
| `AR-y-163` | a read: the internal firm reader, what it returns for a caller with no users row, a disabled row, an active row; every route it guards; the shape TCKT_VNEXT round 7 used | the worker's deliverables | LOCAL |
| `AR-y-164` | the ticket panel shows who sent the final commentary and when; a control, offered only when a draft exists and nothing is recorded, that asks for confirmation and then posts once with no body; words for each refusal | portal `src/pages/TicketCenter/`, one function in `src/api/endpoints/tickets.ts` | LOCAL |
| `AR-y-165` | a read: the original-file route's rule, its owner check, its trusted headers, and which instrument can shape a caller as another firm's client without writing anything | the worker's deliverables | LOCAL |

## Edges and chains

- `AR-y-161` -> (the issuer's count order, the CTO's ruling) -> `AR-y-162`: one queue, slot ~52.
- `AR-y-163`, `AR-y-164`, `AR-y-165` have no edge. M = 4 chains: {161, 162}, {163}, {164}, {165}.

fanout: 4 of 4 chains, cap 8, reason: four independent chains; `AR-y-162` waits on the count and the CTO's ruling.
