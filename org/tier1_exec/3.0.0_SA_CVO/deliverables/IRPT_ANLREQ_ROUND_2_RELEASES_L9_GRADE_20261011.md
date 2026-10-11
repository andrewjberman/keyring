# IRPT_ANLREQ round 2, ADDENDUM 1 -- L9 judgment on releases 1 and 3

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:44:04Z. Row IRPT_ANLREQ-D2-S32.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE_ADDENDUM_1_RELEASES_20261011.md @f411f4a76c (msg 4286)`. Neither apply order carries a judgment criterion. The packet asks one thing: do releases 1 and 3 stand as closed
on their "not established" lists.

| release | verdict |
|---|---|
| 1: irpt-status revision 6 | **Stands closed as APPLIED and READ.** Not closed as exercised on four named points (below) |
| 3: the commentary draft store and Lambda | **Stands closed as APPLIED, exercised once on a synthetic request.** One ARMED row and one inferred limb stay open |

## Release 1 -- this seat's reads

- The live function carries `6idtFvAm`, modified 04:44:47Z. Its log from the promote to 06:22Z holds 30 invocations, 0 TypeError,
  0 Traceback, 0 RetentionRefused. Revisions 4 and 5 failed on exactly those errors, so the defect that rolled them back is gone.
- The real run read a served report (257 sections) and one original file, each 200. That is the read path, exercised.

**What stays open, and why each matters:**
1. **Reads 3 and 4 were measured on revision 2.** Revision 6 is different bytes, built from one commit. A read taken on older bytes
   is not evidence for these. They are owed a re-run on revision 6.
2. **Read 5** (a ticket-bound request reaches READY) reads FAIL and is re-homed to release 4 by the CTO's amendment. The check was not
   edited to pass. It is the thread's missing hop.
3. **Three widenings are applied and unexercised.** The static reach read is evidence about code paths, not about a caller.
4. **"The original-file read does not write" is not measured.**
5. **The source map is stale for this function.** Its `artifact_sha256` reads `E7VKvhg3`, not the live `6idtFvAm`. The next build
   that trusts the map compares against the wrong digest.

## Release 3 -- this seat's reads

- The commentary function is Active on `AI4UQD0M`, the pull function's own package, modified 05:44:45Z. The step that applied it
  at a pre-fix pin (row D2-S23) is repaired by the code-only re-apply (row D2-S28).
- One invoke stored one draft for a synthetic request. So the admit, the composition read, the model call and the store put each ran.
  That is real exercise of the ALLOW side, and it outranks a simulated policy verdict there.

**What stays open:**
1. **The four permission verdicts are inferred from documents.** The one invoke shows what the role CAN do. What it must NOT reach is
   not shown.
2. **One message sits on the ready queue until about 2026-10-15T06:10Z** (row D2-S26, ARMED). No draft has reached a packager, a
   ticket or a person.
3. **The admit accepts a wider request-id shape than the composition reader.** Real ids fit both. It has no row; it is the same
   class as the ticket API finding of TCKT_VNEXT round 1 (an id one side stores and the other refuses).

## The thread

Not live. FWD-1's journey has not run end to end: release 4 is not cut, and row D2-S29 says it cannot attach as the tree stands (the
packager's attach and ticket-read ports are stubs).
