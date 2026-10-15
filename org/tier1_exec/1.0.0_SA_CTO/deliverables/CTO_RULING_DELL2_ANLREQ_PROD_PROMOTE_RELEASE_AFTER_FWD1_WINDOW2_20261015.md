# CTO RULING -- release the IRPT_ANLREQ PROD promote (469b + c8c3) after FWD-1 window 2 (2026-10-15 ~17:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Asked by:** `2.0.0_SA_COO~Y2`, msg 8514.

**Measured by window 2** (applier `0.7.0_AE_CloudOps~AQ2`, `A_RUN_FWD1_R2.txt`):
- The ledger is CLOSED and the guard refused nothing.
- The test user reads ABSENT twice.
- A staff filing produced ticket TCK-20261015-944c84f8, and request REQ-d47252fe74634d0c5cdd8067 was ACCEPTED live with
  `commentary_requested` true. That is IB-pr-456's acceptance, exercised.
- The chain then stopped: 0 of 4 attachments, one `commentary_ready` message in flight, and the packager secret not read.

**RULED: YES. The hold is released, and the DT order may promote 469b and c8c3 to portal PROD.**
- The hold guarded one risk: that c8c3 breaks every PROD filing at intake. Window 2 measured that risk away.
- The page is Opal-internal (ruling 2402), and Andrew approved this promote (CRO record @cb91dbe30a, item 1).

**Conditions:**
1. **The attachment chain is tracked separately** by `~Y2`'s read-only order TO-READ-FWD1R2 (the resident's journal). It is not a condition
   of the promote.
2. **If that read shows the stall is CAUSED by `commentary_requested`** (the commentary path blocking the package), c8c3 is reverted on PROD
   the same turn, on `~Y2`'s word (the DT's rollback: revert merge). The hint (469b) stays.
3. **The promote receipt says the state in words for Andrew's test:** "a staff filing reaches acceptance; the package attachments are not yet
   delivered (being read)". No receipt implies an end-to-end pass.
4. **Row S204 (`~P2`) disarms on window 2's acceptance read.** `~P2` closes it, citing `A_RUN_FWD1_R2.txt`.

-- 1.0.0_SA_CTO~DELL2
