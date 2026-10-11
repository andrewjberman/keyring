# IRPT_YCDGEN round 13 -- decomposition: the nine are reconciled by record, under a pair, with nothing deleted

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_13_20261011.md` @7fa981f907, section 3
(four items). It answers `3.0.0_SA_CVO`'s ADJUDICATION_v12 @8de2ce7fc9. No PRD addendum in the analysis; one is owed by the
CTO and is written against this round's packet. The sitting is not asked.

## The nine, as measured so far

Eight messages on `irpt-generation-dlq` (the laptop's inventory @f2053cfdd8, row IRPT_YCDGEN-D2-S49): 2 for cottonwood, 6 for
49financial, sent 2026-10-07T18:07Z to 2026-10-09T14:59Z, every job RECEIVED with outbox SENT, no reason on any record. One
message on `outlook-global-commentary-draft-commentary-ready-queue` (the laptop's read @87e2151436): `commentary_ready` for
49financial, request REQ-4b5155ac2ea9467ab771b414, sent 2026-10-11T06:10:50Z; that request is also the eighth dead letter.
So nine messages name EIGHT requests.

NOT measured: each request's owner (owner values did not leave the laptop), and why each job failed (a job record holds no
reason; the cause, if it is anywhere, is in the host journal of those days).

## Cells (round 13)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-13` | ~G2 (direct; reads by the applier and by the laptop's executor) | 1 | The reconciliation packet: each of the nine named by request id, with its job state, its request's owner class and firm, the cause where the journal states one, and the closed record proposed for it (FAILED, a closed code, a class, no message). WRITTEN, NOT APPLIED, with the COO half; nothing purged, redriven or deleted |
| `YCD-b-13` | IRPT_ANLREQ workstream ~G (this seat) | 2 | Attach cell 1 is merged @fb4aaf8fa2. Attach cell 2, the packager's users row and credential, as its own pair in that project |
| `YCD-c-13` | held | 3 | Attach cell 4, the binding, is NOT cut until `YCD-a-13`'s pair has accounted for the waiting commentary-ready message |
| `YCD-d-13` | ~G2 (release, under its own pair) | 4 | st32, in the st31 form from a trunk pin, when IRPT_BCKEND's capture-diagnosis cell is built. The first sign-in after it is one request on the CTO's word |

## Dependencies

- `YCD-a-13` needs two reads it cannot make itself: the host journal for the eight request ids (the applier, read only) and
  each request's owner class and firm (the laptop's executor, behind the key no dell2 seat decrypts with).
- `YCD-d-13` waits on another project's build. `YCD-c-13` waits on `YCD-a-13`.

## Not cells

- **A purge, a redrive or a delete of any of the nine.** A purge is unrecoverable and would need Andrew's word; the ruling
  does not spend one. The messages stay until their retention ends.
- **Any request down the YCharts path** by a seat (CTO msg 4917).
- Parked as before: the one-equity store row, fund allocations, the 70 rule-less elements.

## Four-postulate record

(i) Domain: the analysis's four items, one cell each. (ii) One packet, one pair in another project, one held cell, one
release. (iii) One intent: every message that waits on a queue the resident reads, or will read, has a record that says what
it is. (iv) What this round does NOT move by its own act: any message, any queue, any job row. The packet proposes writes;
it makes none.

fanout: 0 tree orders; the reads are apply orders and a cross-box call.

## AMENDMENT 1 (2026-10-11, the issuer, inside its own decomposition): `YCD-d-13` is un-parked and gains one build order

IRPT_BCKEND's capture cell is built and drained @231219c1f4 (`2.0.0_SA_COO~P2` msg 5171), so `YCD-d-13` no longer waits.
`1.0.0_SA_CTO~DELL2` msg 5179 names three things st32's packet carries beyond st31's; the second, the worker stamps
`cause_claim` "measured" (PRD ADDENDUM v0.12), is one line that is not yet built. It is cut as ONE order under this cell,
`IRPT_YCDGEN.TO-YCD-d-13.worker-stamps-cause-claim-measured`, issued to `0.9.0_WK_IRPT_YCDGEN~16`, `<risk>WORLD</risk>`; the same order repairs two stale tests (row IRPT_YCDGEN-D2-S57). The cell is otherwise as
written: st32 in the st31 form from a trunk pin, cut AFTER that order is merged. fanout: 1 of 1 chains, cap 8. Gate limb:
`to-pipeline-gate.py` graded the new order at this commit.
