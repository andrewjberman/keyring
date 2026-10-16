# Cross-adjudication submission -- row dell2-20261016T190526Z-c8f2 (1.0.0_SA_CTO~DELL2)

## Context

IRPT_ANLREQ FWD-5: a live cross-firm exercise on DEV. One transient firm-B principal (cottonwood, `allowedFirmIds` [cottonwood], zero
entitlement rows, 3-hour TTL) tries every listed GET on ONE synthetic 49financial ticket; every call must be REFUSED. Then the principal is
removed and read ABSENT. There is no write to any ticket, request or job.

## Position

Yes, already signed by this seat: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_FWD5_LIVE_CROSS_FIRM_RUN_CTO_HALF.md`
@32dbd895e3, on packet blob `5fbb9aaf24`. Firm B = cottonwood. Applier IB2. The run reuses Andrew's localhost:5174 smoke server and never stops
it. Any LEAK stops at once and removes the principal first.

## Why it gave pause

The scope tool reads it CROSS-BOX: `opal-users-v2` is shared, and the run reads a second firm's surface.

### Ambiguity

None. It is the same transient-principal shape as XA-f98b, with the firm scope ruled in msg 9670.

### Out of pattern

The pattern is a staff test user. Here the user is scoped to a client firm (cottonwood) on purpose, to prove the fence.

### Other solutions

- An offline test only: already done (25 and 23 tests pass). FWD-5's DONE WHEN asks for a seat-driven live exercise.
- A real firm-B login: it would put a person's account into a security test. Worse.
