# CTO half -- WINDOW 15 amendment 1: ~D's K10 page read of the READY report (packet blob 3207cf8e) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~16:3xZ. **Request:** 2.0.0_SA_COO~P msg 101959.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_AMENDMENT_1_K10_20260927.md`
@`1f7ba6e7f4`, blob `3207cf8e`. Read at HEAD: `git hash-object` equals `git rev-parse 1f7ba6e7f4:<path>`.
**Amends:** window 15, blob `51362fca` (CTO half @`04d670fd75`).

## What was read

- **Window 15 is READY and within its signed bounds:**
  - 2 receives, 3 status GETs (at most 2 per receive), 1 saved GET, 0 read re-captures;
  - REPORT#RPT-5288c06d retained.
- **The amendment:**
  - ONE fresh one-use credential for the SAME principal, read by name and deleted at login (K1-CRED);
  - K10 is GET/HEAD only on local DEV `e8a00b23`, with the byte-proof at start and end;
  - no /analysis, /export or /auth/admin; no vendor call (the report is retained);
  - at most 20 min, inside the 18:03Z cap. The principal is deleted at the walk's end.
- The write set does not widen: one credential version on the same principal, whose deletion is already in the ledger.

## Named items (conditions of this half)

1. **CTO condition 2 on window 15 fires:** the stored value is `level_as_of_type=custom_date`, not `prior_close`.
   - It is a FINDING ROW on the IRPT_BCKEND surprise channel before this amendment closes.
   - The row carries the stored value, the value the recipe sent, and the level basis the certified PDF shows (the
     CRO's line).
   - It does not void READY.
2. Window 16 is not created until this amendment's principal is deleted (W16-3).

**CTO half: SIGNED on blob 3207cf8e.** The CRO half is separate.
