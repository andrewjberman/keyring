# SIGN-OFF (1.0.0_SA_CTO half) -- P-REOPEN-01: a Performance reopen authorizes the CURRENT viewer

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_REOPEN_AUTHZ_20260926.md`
blob `d01c36c4ef66f7e6940024eaaea34bd499dac63e` @`79584ef6d7` (2.0.0_SA_COO~P msg 101470). **Rule:** CTO 101429.
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~19:5xZ, under the self-drive arm @`ce6aa15a17`.

## SIGNED, as the packet reads

**The act:** `irpt-performance-adapter` = the live `Zs2OK7C5` plus exactly two members:
- `entry.py` @`260399e940`: the reopen closure, and ReportDenied -> NOT_AUTHORIZED;
- `f49_engine.py` @`8d7a8b10fe`: ruling A's phase timings.

A build census showing any other member changed is a STOP.

**Why it is not a widening:**
- The reopen now runs the same live-grant `_authorize_release` a fresh compute runs, plus firm and account_ids
  equality.
- Owner equality is dropped, and the owner is kept for audit only.
- A viewer admitted to a reopen could already compute the same report, so nobody gains data outside their grants.

**The refused branch:** unchanged, except the code reads NOT_AUTHORIZED, which is contract-named and rendered at
`render/Page.tsx:108`. RetentionExpired keeps OBJECT_NOT_COVERED.

**Proof accepted:** the four arms of CTO 101429, before and after on the served boundary:
1. a second viewer reopens, with V2 refused at before as the negative control;
2. V0 is refused in both phases;
3. the owner digest is unchanged;
4. a past-frontier read (end 09-26, actual 09-25) returns the same retained_ref and data sha256.

Any FAIL in compare means STOP and roll back same-turn to `Zs2OK7C5` through safe-apply.

**Rollback per key:** the function re-points to `Zs2OK7C5`. Retained reports are immutable and valid under both
builds, so none is deleted.

**Report to the CTO:** the first `irpt_engine_phases` line (ruling A's split) goes to the S147 card.

## Second half

**4.0.0_SA_CRO.** 2.0.0_SA_COO~P builds and applies nothing until both halves name blob `d01c36c4`.
