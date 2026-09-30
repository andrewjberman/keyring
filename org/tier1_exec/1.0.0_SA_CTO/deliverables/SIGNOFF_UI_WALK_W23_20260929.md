# SIGN-OFF (1.0.0_SA_CTO half) -- UI walk window 23: one principal, one signed-in directory search (AD-10 step 1 A1)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W23_20260929.md`
@`c7f86d5205`, blob `033aeb03623dda03372a21539e121bb276c4f529` (2.0.0_SA_COO~P msg 102858). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~15:1xZ.

## Read at signing

- The blob hash was printed from `git rev-parse c7f86d5205:<packet>`, and it matches the ask.
- **The walked build is the served tree.** `git rev-parse 18899c96^{tree}` = `9a8f6c71^{tree}` = `8b18dbb79c...`, with
  origin/PROD at 9a8f6c71 and origin/DEV at 18899c96, read after a fetch. So a localhost:5174 read at DEV 18899c96 is
  a read of the PROD page code, and the walker stays inside Andrew's 2026-09-26 localhost guard.
- **Blast radius:** one sign-in and one GET-only search. The only writes are the principal's own login and refresh.
  Credoff follows sign-in, K1 is deleted within 30 min, and both are read back. The users census runs before and
  after. A field-set change or an `account_masks` appearance is a named FAIL, with the step-1 ledger's rollback keys.

## Condition (this half)

1. ~D records the portal commit its localhost build is running at the time of the read, not only the branch. If it is
   not 18899c96 or a commit with the same tree, the read is not A1's evidence.
