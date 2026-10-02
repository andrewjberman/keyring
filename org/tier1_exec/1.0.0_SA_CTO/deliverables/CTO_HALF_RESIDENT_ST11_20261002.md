# CTO half -- st11: the resident st10 -> st11 at 4f68a17d3a (a BUSY resolve no longer spends itself) and sqs:SendMessage (IRPT_BCKEND)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/ST11/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST11_20261002.md` @2e0cbd5c36,
**blob `d0243e9bb1`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104102. Rulings: batch 120 items 1-4, batch 121. This half is a
separate file bound to that blob.

## SIGNED, 2026-10-02 ~07:2xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: I1, exactly one added action (`sqs:SendMessage`) on the one existing resource of sid
`ConsumeTheGenerationQueue`, by a targeted plan whose only change it is; D1, one new root on one host, 243 members of which 8 change
and 2 change behaviour in the resident (`resident_worker.py`, `resolution_broker.py`). Every branch of a `resolve_upload` receive is
stated before and after; only the OPERATION_BUSY branch changes. No vendor call and no job in the act. Rollback per move.

Read by this seat at signing: the `resident_worker.py` diff from st10's pin `b1db201025` to `4f68a17d3a`.
- A BUSY receive SENDS one fresh copy delayed by the lease's retry-after (clamped 1..900, 60 when absent) and then DELETES the received
  one; past `requested_at` + 3600 s it ends the row `RESOLVE_PROVIDER_BUSY` with action `CORRECT`, deletes, and sends nothing.
- The busy branch requires a numeric `requested_at`; without one the receive falls to the unchanged bounded-retry path, so a row
  that cannot prove its deadline cannot enter the re-send chain. That is the right fallback.
- Send before delete: a failed send leaves the received message to return by itself.

**Batch 121's ask is met:** the deadline is anchored on `requested_at`, which no re-send or redrive moves; each receive sends one
and deletes one; the deadline end sends nothing; the offline test drives SQS's own count past the deadline with nothing
dead-lettered, and the three new tests fail on st10's worker (negative control).

Named by this half in addition:
1. The served words for `RESOLVE_PROVIDER_BUSY` ride the next generate and irpt-status bundles (item 19); until then the page shows
   the code with action `CORRECT`. Accepted: the user is no longer told to replace a good file.
2. The live proof (an upload during another job's generation reads NORMALIZED after it) waits on a live YCharts session, which waits
   on Andrew's own sign-in through the CAPTCHA (batch 120 item 7). The ledger closes at V1, the install's read-back; the live
   proof is the next window's, under its own packet.
3. Not verified by this seat: the gate output, the tar and script hashes, the suites' runs, the targeted plan's run.

-- 1.0.0_SA_CTO
