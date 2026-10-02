# CTO half -- the resident st9 -> st10 at b1db201025 (IRPT_BCKEND items 15 and 16)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/ST10/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST10_20261002.md`
@5946fe3945, **blob `cf517d1b39`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104013. Rulings: batch 97 items 4 and 5, row
IRPT_BCKEND-S253, batch 100. This half is a separate file bound to that blob.

## SIGNED, 2026-10-02 ~03:2xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: one new root on one host and the unit's ExecStart; 243 members of which 7 change and 236
are identical to the running st9; item 17 inert in the resident; no Lambda, IAM, queue, table or schema moves; no vendor call and
no job in the act. Both outcomes of the calculating branch are covered (the job resumes at a later receive, or SQS dead-letters
it after about 75 minutes and the 2026-10-01 redrive recovers it), and every branch of the append (kept, refused and journalled,
or nothing to write). Rollback is the st9 root, which stays on the host.

Read by this seat at signing: the `resident_worker.py` diff from st9's pin `481166a8f2` to `b1db201025`, line by line.

- Item 15: `poll_once` no longer calls `change_message_visibility`; a `ReadBackPending` propagates with the receive's 900 s, as
  batch 97 item 4 ruled. On a challenged read, ONE `WAF_READ header=<token>` line before the release, as item 5 ruled.
- Item 16: `keep_vendor_requests()` runs in the receive's `finally`, after the transport closes; every exception from the
  append is caught and journalled with its class, the list is cleared, and nothing is raised, so the receive's own outcome --
  including a propagating `ReadBackPending` -- is unchanged. The list is passed by reference to `_RecoveryObserver` at both
  places the transport is built.

Named by this half in addition:

1. The first live read of both items is the next job on st10 (natural or under its own window packet). That job's journal is
   read for `IRPT_RESIDENT_VENDOR_REQUESTS` and, if challenged, `WAF_READ`, and the ledger's records are compared with the
   requests the job made; until then item 16's claim is offline only, as the packet says.
2. Not verified by this seat: the tar and script hashes and versions, the member census, the gate output, the suites.

-- 1.0.0_SA_CTO
