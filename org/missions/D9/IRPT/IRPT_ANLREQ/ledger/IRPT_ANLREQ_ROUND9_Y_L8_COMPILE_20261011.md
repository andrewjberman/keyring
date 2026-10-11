# IRPT_ANLREQ rounds 8 and 9, workstream Y -- L8 COMPILE: the commentary drafter's READY gate is built, granted and LIVE (release 6)

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Decompositions: `decompositions/IRPT_ANLREQ_DECOMP_R8_Y.md`, `..._R9_Y.md`.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 9` after the last flip (061532cf9c): 10 orders in scope, 9 complete,
proof_ok 9, proof_bad 0, verdict MAY-CLOSE (which order is the tenth was not read).

Claim words: MEASURED = this seat ran or read it; RECORD = an applier's or worker's committed record this seat opened; INHERITED = read
by another seat and relayed.

## 1. State at this compile

- **LIVE, the first thing from rounds 3 to 9 on a service:** `irpt-commentary-composition-read-lambda` runs
  `DbvBUxTGlCsdG4htVOhbI4NBxBMNbmjD6BLpMGu2Yo4=` (MEASURED ~17:0xZ), the READY gate with it, and its role holds the grant the gate needs.
- **Not on a product path:** no event source feeds the commentary drafter, so nothing but the release's own after-reads has passed the
  gate. Thread `n`.
- Unchanged: irpt-status is revision 6 (`6idtFvAm`); release 5's return, now carrying the ticket binding, waits on the portal history
  reader AND the portal reason set reaching PROD, which is Andrew's word.

## 2. Round 8 -- TO-AR-y-81, the gate (CTO msg 5133), merged @5117ad5c1d

A request whose job does not read READY, or has no job row, gets no composition: the refusal `UNAVAILABLE`, before any artifact is read.
The gate is in the composition read, the one port every path into the drafter uses (queue, non-queue, mixed: RECORD, the worker's
design record `deliverables/0.9.0_WK_IRPT_ANLREQ~52/r8/READY_GATE_DESIGN.json`); the drafter is unchanged and records a refused read as
`failed` with no draft and nothing sent. MEASURED: the five named tests pass; `reports/tests` 186 and `data/transcripts/scripts/tests`
451 pass. RECORD: `ops` 313 passed; `_contracts` 2 failed, the base count.
**What the merge did that this seat did not foresee:** the gated file is an unpinned member of the function's source-map entry, so the
merge armed a rebuild hazard (code without its grant): row `IRPT_ANLREQ-D2-S53`. The CTO ruled the disarm an ORDER, not a pin (msg 5208).

## 3. Round 9 -- TO-AR-y-91, the grant and the release census, merged @eba5acba8f

- Grant, Terraform text: the jobs table added to the role's `GetItem` statement (same `LeadingKeys` condition) and to its kms
  table-name context. RECORD (worker, from files): the jobs table's partition key is the tenant; same KMS key; `tables.jobs` exported.
  `terraform fmt -check` was never run by anyone; the applier's plan was its first parse and read one resource to change.
- Census (`deliverables/0.9.0_WK_IRPT_ANLREQ~53/r9/COMPOSITION_READ_RELEASE_CENSUS.json`, blob f5167ebd9f): the live package
  downloaded once and hashed, 16 members; the live gated file byte-equal to commit `20534db618`; trunk build `DbvBUxTG` twice
  (and once by this seat); 3 members differ from live (the gate; `repository.py` and `retention.py`, both read INERT, inferred).

## 4. Release 6 -- pair signed on both halves, applied, complete

Pair: `deliverables/2.0.0_SA_COO~Y2/release6/NEVER_WIDEN_PAIR_ANLREQ_RELEASE6_COMPOSITION_READ_READY_GATE.md` (blob 5e56a253f7); CTO half
@6d3aac1d65 (msg 5241). Order: `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-Y6.composition-read-ready-gate-dell2.md`
(complete @061532cf9c). MEASURED by this seat on the applier's committed files: `APPLY6-LIVE-OK`, `APPLY6-RECORD-OK`, proof VALID.
RECORD (`deliverables/irpt_anlreq_r6/R6_apply_record.json`, applier msg 5401):

| step | result |
|---|---|
| the grant | plan 1 resource; read back with both tables in both statements |
| G2, a READY request on the OLD code after the grant | OK |
| the code | build `DbvBUxTG`, plan 1 resource, re-plan 0 |
| A1, the same request on the new code | OK, the sha256 and key names identical to G2 |
| A2, the request whose job reads RECEIVED | `UNAVAILABLE` -- a measured change: the same request drafted through this function at 06:09Z |
| A3, a request that does not exist | `UNAVAILABLE`, as before |
| rollback | none; the ledger closed; the map entry states the release |

**Said in words (CTO condition 2):** the build used `BAU_PARITY_SKIP=1`, the parity check OFF.
**The apply stopped twice before any write, both times correctly:** (1) the applier held no request with a READY job; (2) dell2 cannot
read a job row at all (`kms:Decrypt` on the IRPT key is denied to its identity, and the jobs table shares the requests table's key).
THIS SEAT'S DEFECTS: the order required a READY request and gave no way to find one; AMENDMENT 1 then told the applier to read the row
itself without knowing it could. The laptop reader read the rows under a read-only order (TO-READS-Y6, complete @377a66ab0f):
14 of 14 READY. So the READY request's job state in the apply record is INHERITED, and the record says so.

## 5. A count the CTO asked for (msg 4955), measured by the laptop under TO-READS-Y6

51 accepted requests of 1904 items: 6 store a `ticket_id` (all 49financial), 45 do not (49financial 5, cottonwood 39, inflection 1),
0 unreadable. Written into the release-5 re-release packet (revision 3) as the baseline for the ticket binding.

## 6. Rows

| row | class | disposition |
|---|---|---|
| IRPT_ANLREQ-D2-S53 | BLOCKING, was ARMED | disarmed by `IRPT_ANLREQ-D2-S54` on the release's after-reads |
| IRPT_ANLREQ-D2-S34 | OBSERVATION | the parity-skip build: a cell in this seat's next issuance (CTO msg 5241), with the entry's four unpinned members (the class of rows S45 and S53) |
| IRPT_ANLREQ-D2-S26 | ARMED | unchanged: one test message on the commentary-ready queue until about 2026-10-15T06:10Z. With the gate live, a NEW hand-built invoke for that request drafts nothing; the message already on the queue is untouched. Workstream G's attach release reads it before binding (CTO msg 4972, cell 3) |

## 7. For L9

No judgment criterion was cut on these orders. What a reviewer may grade on its own reading: whether "LIVE" in section 1 should carry
the words "and unexercised by any product path" wherever it is repeated; and whether A1 equal to G2 on ONE request is enough to call
two unexercised members inert.
