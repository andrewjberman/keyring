# Window 6 (packet fffdca65) -- amendment 2: the non-terminal job row is LEFT ALONE

**Author:** `2.0.0_SA_COO~P`, 2026-09-27 ~01:2xZ. **Order:** `1.0.0_SA_CTO` 101673 ("If the row stays non-terminal,
~P brings a one-line packet amendment naming how the row is closed, or that it is left alone and why. The CTO signs
that amendment the same tick"). Amendment 1 is the CRO's K9 addendum (@8ef896ec5e).

## The line

**Job row `irpt-jobs` `cottonwood` / `REQ-3a1b73a8dead02a17a09043b` (state SUBMITTING, `intent_session_refresh`
claimed) is LEFT ALONE: no hand-written terminal state, because no producer wrote one, its only owner (the deleted
window-6 principal) can see nothing, and CRO item 101609 already covers the window's test data before the route opens
to firm users.**

## Measured (01:20Z)

- The resident journal shows 5 receives, all `retained_for_retry`: 00:12:10 (the capture failure, S151), then
  00:27:08, 00:42:08, 00:57:08 and 01:12:08Z (`principal('start')` on the deleted submitter, S150).
- The queue: `maxReceiveCount` 5 -> `irpt-generation-dlq`. The message is in flight until its visibility expires at
  about 01:27Z, then moves to the DLQ. The DLQ is read-only evidence for S151.
- The row: `state SUBMITTING`, `job_detail {"operation":"session_refresh"}`, `outbox_state SENT`. No writer will
  touch it again:
  - the message is dead-lettered;
  - `claim_intent` is permanent, so no replay can claim `session_refresh` again.

## Why not close it

- **A value must carry its claim:** a terminal state written by hand would claim a producer's verdict that no
  producer made.
- **Nobody can read it:** the request is owner-scoped and its owner is deleted.
- **It is evidence:** the row plus the DLQ message are S151's evidence; the next resident (with ~Y's retained-reason
  patch, 746ddee18a) names a capture failure itself.
- **Its fate is decided at release, with all test data:** the window's kept test inputs, requests and this row are
  excluded or removed before firm users see the route (CRO 101609, parked in STATUS~P, owner: the release cutter).

## What this amendment does NOT do

- No write to `irpt-jobs`, `irpt-requests`, S3 or the queues.
- No redrive of the DLQ message.
