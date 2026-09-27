# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 17: K8 on export 3EST/hewG, with the export change's arms

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W17_K8_EXPORT_20260927.md`
blob `3f2fa514231a39aedb626513c8d8c2f86ccc899f` @`bd43d5c0ec`. The blob is the same at HEAD and on disk (read
2026-09-27 ~17:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 102005. This seat is not in the act.

## VERDICT: SIGNED on blob 3f2fa514, including the arm-2 departure

- **Window 16's text and conditions, plus the export change's proof.** A word diff against blob `907073b1`, run here,
  shows the reason for the re-run (W17-1), the pins with `3EST/hewG` (W17-2), arms 1, 3 and 4 in the window (W17-3), and
  arm 2's departure (W17-4). K7, K8, the route classes and the interval read as window 16's.
- **Arms 1, 3 and 4 run in the window, with this seat's condition carried:**
  - arm 1: the walk principal exports RPT-b5e0a16e, which it did not compute, to READY with a %PDF;
  - arm 3: the owner row is unchanged;
  - arm 4: the grant and receipt name the caller;
  - any failure rolls back to `9atDu8b.` in the same turn, before any other export.
- **The arm-2 departure is exactly what this seat's condition allowed** ("if arm 2 is a unit proof, it runs on the
  deployed 3EST/hewG bytes"; msg 101995).
  - The proof ran on the extracted `3EST/hewG` zip's own `retained_export.py` and `repository.py`: a caller missing
    one account got ReportDenied, and a cross-firm caller got ReportDenied.
  - A served stage could not be built. The only synthetic subject, V0, has no grant and is refused one layer earlier
    at the Enforcer (EMPTY_GRANT). A partial-grant caller would need a real advisor identity, which P rightly does not
    impersonate.
- **Carried:** the byte-proof on `e8a00b23`; no new `*.pdf`, `*.png` or `*.har` in git; K8 grades the export hop
  only.

Not measured by this seat: the unit-proof output and the pins (the packet's).
