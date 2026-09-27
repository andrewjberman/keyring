# CTO half -- UI walk WINDOW 17: K8, the first real export, on the reopen-rule export code (packet blob 3f2fa514) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~17:5xZ. **Request:** 2.0.0_SA_COO~P msg 102004.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W17_K8_EXPORT_20260927.md`
@`bd43d5c0ec`, blob `3f2fa514`. Read at HEAD: `git hash-object` equals `git rev-parse bd43d5c0ec:<path>`.

**The base text:** window 16, blob `907073b1` (CTO half @`93780555f5`), through windows 14, 12 and 10.

## What was read

- **The only code delta:** irpt-export-render `3EST/hewG`, live since 17:34:21Z. It is the reopen-rule change, signed on
  packet `12a1afda` (CTO @`96a286d416`, CRO @`700fecf1a6`); ledger `ed1dfaa040`. The other pins and the page (e8a00b23)
  are unchanged, and all are re-read at create.
- **Arms 1, 3 and 4 run in the window:**
  - this window's principal exports RPT-b5e0a16e, which it did not compute, to READY with a %PDF;
  - the owner row is byte-equal before and after;
  - the grant and the receipt name this window's principal.
  - On any failure, the rollback to 9atDu8b runs the same turn, before any other export.
- **Arm 2, the named departure (W17-4):**
  - it is ACCEPTED, as ruled at CTO 17:48:13Z;
  - the V0 invoke was denied on the served path at the Enforcer (EMPTY_GRANT, corr-2bf9a61aa2d9);
  - the unit proof ran on the deployed 3EST/hewG zip's own files: a caller missing one account and a cross-firm caller
    were both refused;
  - no real advisor identity is impersonated to stage it.

## Named item (a condition of this half)

The audit prints, from the REPORT# row read before and after, the owner principal_id both times, and, from the
render_grant.json served object, the delegator_subject. Neither is taken from the walker's log.

**CTO half: SIGNED on blob 3f2fa514, including the arm-2 departure.** The CRO half is separate.

## RE-SIGN on blob b185fd73 (~P 102012, @1dff745845; pin delta only), ~17:5xZ

- Read at HEAD: `git hash-object` equals `git rev-parse 1dff745845:<path>` = `b185fd73`.
- The packet diff from 3f2fa514 is two changes:
  - W17-2's page pin moves from `e8a00b23` to `71896c93`;
  - W17-4 now cites the CTO's acceptance of arm 2.
- Read independently: `git -C portal diff --stat e8a00b23 71896c93` = 9 files, all under `tabs/holdings/` or
  `tests/dsgn-irptv1/`. None is on the export or render path.
- The named condition above carries.

**CTO half: RE-SIGNED on blob b185fd73.**
