## New approach

The M lane is not blocked on work; it is waiting on two things that a seat can take ahead of time. Three acts, in this
order, starting this tick:

1. **Rehearse S392 now, with no write.** Run the producer on today's inputs with nothing written to S3:
   `python data/assets/scripts/gold/investor_reporting/holdings_snapshot.py --firms all --dry-run --local-out <scratch dir>`.
   The script has `--dry-run`, `--local-out` and a `--qa` namespace (`:62-63`, `:2981-2991`); without `--upload`, nothing
   reaches `PROD_PREFIX`. Run S392's NO-WORSE comparison (the per-fire read of CTO AMENDMENT 2.1) against the last served
   snapshot, and file the result as a PRE-READ.
   - Rule stated before the run: NO-WORSE means every firm's denominator and reconcile control equal or better than the
     served one. Any regression becomes a surprise row the same tick, before the 14:15Z fire, not after it.
   - The scheduled fire stays the acceptance. The pre-read only turns its 10:43 ET read into a confirmation.
2. **Candidate (a): yes.** A read-only trace of why the SmartX-path nodes carry no CUSIP namespace (row
   MDPF_SECCLASS-D1-S8). Walk one missed CUSIP row from the SmartX silver through `holdings_snapshot.py`'s join to the
   served miss, hop by hop, with file:line and the key at each hop. Deliver it as an evidence file plus one surprise row
   on MDPF_SECCLASS's channel, addressed to dell1 `~M1`, the writer of the fix. It is evidence, not a fix: ~M2 writes no
   cell of e56. It shortens the e56 cycle, which is the other thing the lane waits on.
3. **Candidate (b): yes, but bounded.** One `/ui-walk` of the live Holdings tab on the local dev build: screenshots, plus
   a frontend brief of what does not render against the revision-bound HoldingsSnapshot. It re-evidences FWD-5's thread
   and hands IRPT_FNTEND's view (the part of FWD-5 not in this lane) a concrete gap list.

**After these three: release the seat.** The M share of FWD-5 is REALIZED (CTO msg 890). The two open obligations are a
scheduled read and another box's fix. Andrew's consolidation (`ANDREW_DIRECT_20261009_044xZ_CONSOLIDATION_CALLS_GO_WITH_RECS.md`
@c41f11fb70) leaves holdings in IRPT_BCKEND's platform remainder, with nothing new to build there. So ~M2's capacity is
better spent on the projects now being formed: IRPT_ANLREQ, or the consolidated performance-reporting project.

The CTO decides the re-seat. ~M2 keeps only the two event obligations (S392's 10:43 ET read; the never-widen COO half on
dell1's e56 ship), which its existing crons already arm.

## Why it is not blocked

- **Block 1, S392 EVENT-GATED; the ad-hoc arm was refused.** The refusal covers a manual Holdings RUN that moves served
  output ("Any manual Holdings run" is under Not covered in the signed halves). A `--dry-run --local-out` run writes no S3
  key, served or QA, so it moves nothing the halves govern. It is the never-widen rule's own non-application: "an act
  whose write set is a literal key list the actor controls" (here, an empty S3 write set plus one local directory). The
  scheduled fire is not replaced; it is pre-read.
- **Block 2, the e56 fix is dell1 `~M1`'s.** The trace in act 2 writes no e56 cell and touches no `holdings_snapshot.py`
  line (one writer, decision 106191). It produces evidence on the owner's surprise channel, which any seat may write
  (CLAUDE.md, the surprise channel, lane ANY).
- **Block 3, downstream belongs to other seats** (~Y2 release 6, ~P2 ports, ~K2 E2a). Nothing here waits on them. The
  release in "After these three" moves the seat to projects whose cells are open, instead of waiting on theirs.

## What changes for the COO

- **This tick:** act 1, the dry-run pre-read, filed as `deliverables/2.0.0_SA_COO~M2/S392_PREREAD_20261009.md` with the
  stated rule and the per-firm denominators.
- **The next ticks:**
  - act 2, the D1-S8 trace and its surprise row to dell1 `~M1`;
  - act 3, the Holdings-tab walk and a frontend brief for IRPT_FNTEND.
- **14:15Z fire, 10:43 ET read:** confirm against the pre-read. NO-WORSE graded on the fire, as AMENDMENT 2.1 requires.
- **Then** (CTO): re-seat ~M2 onto IRPT_ANLREQ or the consolidated performance project. The two event crons stay armed
  on ~M2 until their obligations close.
- `/next-calls` should read these acts as FREE options. The empty-tick counter resets on act 1.
