# Analysis (IRPT_BCKEND~Y) -- enrichment candidates the six windows of 2026-10-01 measured

Author `2.0.0_SA_COO~Y`, 2026-10-01 ~13:1xZ. For `1.0.0_SA_CTO`'s next analysis. Nothing here is built. Each candidate
states what was measured, what is not, and what its trial would cost. Order: by what a user would feel first.

## 1. Every job loses 15 minutes to one read challenge

**Measured, 3 of 3 jobs today** (`REQ-602834fd`, `REQ-7c7a9e45`, `REQ-a69e5751`; journal lines in the three outcome
files): after the portfolio is created the worker polls its status twice, 15 seconds apart
(`recipe.py:617-618`, `READ_BACK_POLLS = 2`, `READ_BACK_SPACING_S = 15.0`). The first GET answers `calculating`. The
second, 16.7 to 16.8 seconds into the step, answers 202 with a WAF action. The worker raises
`READ_BACK_PENDING:WAF_CHALLENGE`, the message stays invisible for the receive's 900 seconds
(`resident_worker.py`, `poll_once`: `VisibilityTimeout=900`; only the resolve kind shortens it), and the second
receive, 15 minutes later, reads `available` on ONE status GET and finishes in about 70 seconds.

So a job that needs about 2 minutes of work takes 17. The comment at `recipe.py:617` records the challenge on the
THIRD GET (4 of 4 runs in September); today it is the SECOND.

**Not measured:** how soon after a challenge one status GET is answered. On 2026-09-29 the journal shows challenges
3, 5, 7, 12 and 15 minutes apart, on mixed jobs, so a shorter wait is not known to be safe.

**Candidate:** ONE status GET per receive. A `calculating` answer releases the message with a short visibility (a
ruled number, 60 to 180 seconds) instead of polling again inside the receive; a WAF action keeps today's 900. The
second GET that draws the challenge is then never sent 15 seconds after the first.
**Trial cost:** it rides a job attempt that would be made anyway (the next arm); the journal's `polls=` and `wall_s=`
and the receive times are the read. If the single GET of the second receive is challenged, the candidate is refuted
at the cost of one more release.

## 2. The resident's own sign-in is unrepaired (row S230)

**Measured:** 4 of 4 resident-run sign-ins since 2026-09-29 failed `AUTH_FAILED` (on the two that carry an eviction
line, 18 and 20 seconds after it); the same wrapper run by an operator as the resident's user and environment signed in in 10 seconds (08:21Z).
One operator sign-in then carried three jobs over four hours. **Not measured:** the failing step (st7's reason token
names it at the next occurrence; none has occurred since).

**What it means for a user today:** when a person signs in on the shared seat, the stored session is displaced, the
next job's own sign-in fails, and the job ends ATTENTION until an operator signs the host in under a packet.
**Candidate, two parts:** (a) let the failure happen once more on st8 and read the token and `last-capture.stderr`:
it costs one failed sign-in, inside the batch 70 budget, and it needs a displaced session, which only a person
signing in produces; (b) independent of the cause, the seat itself: a second YCharts seat for the automation removes
the displacement. (b) is a contract and money question and is Andrew's.

## 3. The READY receipt carries no vendor request ledger (row S253)

**Measured:** 1 of 1 READY jobs since IB-yr-291: three keys, no ledger. A job spans several receives, so the ledger
cannot be one transport's list: it has to be kept across receives (a checkpoint the worker appends to, where today's
checkpoints are write-once). **Candidate:** a ruled design before code. Nothing reads the ledger today.

## 4. The words a user reads for `RESOLVE_RETRY_EXHAUSTED`

They say the request could not be resolved "while other work was in flight". On 2026-10-01 08:25Z nothing else was in
flight. st7 and st8 print the refusal's class on the resolve line, so the words can now follow the class.
Owner `2.0.0_SA_COO~D` (batch 72 item 13).

## 5. The cut-name rule for a name with no request id

`extract.after_name` accepts a three-quarter prefix followed by an ellipsis; a job's own portfolio name must also
hold its request id whole (batch 83 item 3). A comparison model's name has no id, so the one-row rule is its only
guard (st8 half, item 1). **Measured:** the four catalogue labels are 14 to 22 characters; the one comparison PDF read
today prints its model's label whole; the vendor cut a 49-character name at 47. **Candidate:** for a name with no id, accept no cut at all
until a cut one is seen and kept (the st7 census and kept-PDF path would show it).

## 6. The portfolio name is two characters longer than the vendor now prints

The vendor printed 49 characters whole on 2026-09-29 and cuts at 47 on 2026-10-01. Batch 83 keeps the name and makes
the reader an identity check, which holds for any cut that keeps the request id (33 characters). Recorded here only
so the measurement is not lost: a name of 47 characters or fewer would be printed whole today.
