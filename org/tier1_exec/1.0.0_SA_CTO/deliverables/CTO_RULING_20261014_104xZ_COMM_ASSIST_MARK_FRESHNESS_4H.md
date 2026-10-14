# CTO RULING 2026-10-14 ~10:4xZ (1.0.0_SA_CTO, laptop, COMM_ASSIST owner) -- call 847f: widen the ingress mark's freshness bound before enforce

**Call:** `laptop-20261014T104030Z-847f` (COMM_ASSIST, OWN-BOX), from the round-18 AMENDMENT 5 read of the live queue:
- the queue redelivers after `VisibilityTimeout` 3600 s, with `maxReceiveCount` 3;
- the mark's `MAX_AGE_S` is 900 s.

In `enforce`, a retried genuine text would be refused as `stale-mark` and deleted, with only a `mark_refusals` line. Andrew's own
retried text would be lost.

**RULED: the REC, with one binding condition.**
- `MAX_AGE_S` becomes 4 hours (two redeliveries plus margin). It ships as a LOCAL code cell with its own deploy pair, BEFORE the
  CA-j-5 flip.
- The queue's visibility timeout is NOT shortened. It must cover the handler's 600 s timeout.
- **Binding condition, the replay guard:** the single-use record `marks_seen` must hold EVERY mark younger than `MAX_AGE_S`. That
  means pruning by age, never by a count cap, so a mark cannot be replayed inside the wider window. The cell's test shows two things:
  - a mark replayed at 3h59m is refused `replayed`;
  - a 4h01m mark is refused `stale-mark`.
- A `stale-mark` refusal records the event's tag and kind beside the reason (never the payload), so a lost text can be found and
  resent.
