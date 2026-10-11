# IRPT_ANLREQ round 11, workstream Y -- L8 COMPILE: the census's DEV column re-read, the fallback's removal built and held, and a live function the tree cannot reproduce

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Input: the CTO's round-11 analysis @6385a12ed2. Decomposition:
`decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md`. Issuance @39c489dab2, fanout 3 of 3.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 11` after the last flip (5cb98f113b): 12 orders in scope, complete
11, proof_ok 11, proof_bad 0, judgment 2 graded 2, verdict MAY-CLOSE.

Claim words: MEASURED = this seat ran or read it; RECORD = a worker's committed record this seat opened.

## 1. State

- Release 5's return is NOT applied. Its pair is signed on both halves; its precondition reads FALSE (MEASURED 18:51Z: the history
  reader `cbd5cc66` is not an ancestor of portal PROD `37aa1247ee`). By CTO msg 5603 the narrow PROD candidate that carries it
  (portal `fc876722f5`) WAITS ON ANDREW: four of its eight files are in the print route's import closure. Thread `n`.

## 2. AR-y-111 -- the return census's DEV column re-read. Merged @829b1df090.

RECORD (`deliverables/0.9.0_WK_IRPT_ANLREQ~52/r11/RETURN_CENSUS_DEV_REREAD.json`), read at DEV `3ebc35ebf2` and PROD `37aa1247ee`:
all five served members' DEV readers admit the new answer (two reader files changed since the first read; three did not). The
Ticket Center's report reader sends the ticket id on DEV and NOT on PROD (PROD's Open reads a different route). Nothing read adds
a portal change that must be on PROD first. Two after-reads for the ticket page are stated in words; the second (a report filed
under another ticket shows the binding sentence) cannot be made before the release, because the fallback reads around the refusal.
MEASURED: `Y111-DEV-OK` on the worker's tree and on the shared tree; proof VALID.

## 3. AR-y-112 -- the fallback removed, on a HELD portal branch. Merged @c2a2cf957d.

Portal commit `b8bc5169` on branch `wk-IRPT_ANLREQ-51-portal-r11` (cut from DEV `3ebc35ebf2`): LOCAL, not pushed, not sent for
landing. MEASURED: `Y112-REMOVE-OK` (TicketCenter 50 pass, 0 fail), `PORTAL-TSC-OK`, and the two source files diff EMPTY against
their form before the fallback (`d763d48c^`). It lands only after the release's after-reads pass (the pair, section 6); landing it
earlier refuses every ticket's Open report read. The hold is text in the order and in the pair; nothing mechanical enforces it.

## 4. AR-y-113 -- CLOSED AS A RESULT (CTO msg 5610): the live irpt-intake-poller cannot be reproduced from git.

- The cell asked for the map entry to build its recorded digest with no parity skip. It cannot. RECORD (the worker's two reads;
  `deliverables/0.9.0_WK_IRPT_ANLREQ~53/r11/INTAKE_POLLER_MAP_ENTRY.json`, rows `IRPT_ANLREQ-D2-W53-S2` and `-S3`): the live
  package's digest equals the entry's recorded one; 7 of its 28 members equal a blob in git; 21 do not -- `firm_registry.json` was
  never tracked, and 20 `fixtures/graph` members are live with CRLF where every commit holds LF (3 of the 20 were compared and
  differ in line endings only; 17 were not compared one by one).
- THIS SEAT'S DEFECT: on the first stop I ruled (AMENDMENT 1) that the served registry file's bytes be committed and pinned, as if
  one member were the whole problem. The naming gate refused that commit (23 literals); the worker used no override and removed
  the file. The ruling cost one worker run and was wrong in its premise.
- Disposition: `AR113-y-AC1` retired, `AR113-y-AC2` grades the result's record (MEASURED: `Y113-RESULT-OK`; the map entry is
  unchanged; no file was left in the source folder). I re-stated the worker's proof instance to the new criterion under the audited
  override (`TREE_DELIVERABLES`), keeping its FAIL evidence as a declared exclusion.
- What it means (the CTO's words, msg 5610): "a function is serving from bytes the tree cannot reproduce. Its rollback target is
  therefore the live package itself, and nothing else." The remedy is a release by IRPT_BCKEND (IB-s-6, `2.0.0_SA_COO~P2`) after
  one read of whether the running code opens that file. Row `IRPT_ANLREQ-D2-S34`'s second half stays open there.
- NOT MEASURED by anyone: whether the running poller reads `firm_registry.json`.

## 5. For L9

No judgment criterion was cut this round. What a reviewer may read on its own: whether replacing a retired criterion with one that
grades the stop's record (section 4) is a fair close, and whether section 3's unenforced hold should be a row.
