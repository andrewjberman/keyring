# TCKT_VNEXT round 3 -- L9 grade of TO-RUN-R3-tr1 AC2 (the fourth run of the FWD-1 journey)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T12:05:17Z. Row TCKT_VNEXT-D2-S39.
**Input:** `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R3_TR1.md @92c34457f2 (msg 4877)`. Graded on the applier's trace, which this seat read field by field, plus one live read of its own.

| limb of AC2 | verdict | evidence |
|---|---|---|
| the report is made from the filed file | **NOT MET** | The submission was accepted and queued. No read returned a finished report: 40 polls, each NOT_FOUND |
| the finished report opens from the same ticket | **NOT MET** | The hop that records the id on the ticket and the hop that opens the report did not run. No report id exists |
| one firm only | **Not graded here** | The census (82 routes armed, 0 off-list admits) is the applier's; this seat did not re-read it. It does not change the verdict |

**Verdict: TO-RUN-R3-tr1 AC2 NOT MET. FWD-1 is not realized by run 4.** The issuer reads it the same way.

## What run 4 did show

It is the first run past the submission. The service accepted the request and issued its own id, and the runner used that id. That
closes the fault of run 3. It is one instance.

## What nobody knows yet

- **What happened to the job.** NOT_FOUND cannot tell "not yet made" from "failed" or "never started". One fact from this seat: the
  generation dead-letter queue still reads 8, the count before the run, so the job had not been dead-lettered by the time of this
  grade. That rules out one ending and no other.
- **Whether the bound was long enough.** The run waited 20 minutes. No measured time for a real generation is cited.
- **The read path moved under the run.** irpt-status was rolled back from release 5 to revision 6 at 11:26:53Z, about 8 minutes into
  the 20 minutes of polling. Both builds answered NOT_FOUND, so it does not explain the result, but the run's precheck names a build
  that was not the one serving its last polls.

## Left behind

One upload, one accepted request and two completed tickets sit under a client firm as test artifacts. The filer row is due for
deletion after 13:19Z under the order's second step.
