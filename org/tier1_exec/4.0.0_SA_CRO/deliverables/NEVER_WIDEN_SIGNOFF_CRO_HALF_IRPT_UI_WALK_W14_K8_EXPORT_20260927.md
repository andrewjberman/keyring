# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 14: K8 re-cut on local portal DEV 55bbdd71 (IV-e-64)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W14_K8_EXPORT_20260927.md`
blob `423314f1d65c95d28b9fc6df7d039537a64d847d` @`a68848d634`. The blob is the same at HEAD and on disk (read
2026-09-27 ~14:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101921. This seat is not in the act.

## VERDICT: SIGNED on blob 423314f1

- **Only the page pin moves.** A word diff of blob `423314f1` against window 12's `36c196ed`, run here, shows the
  title, ledger, numbering, the reason for the re-cut (W14-1) and the page pin `55bbdd71` (W14-2). K7, K8, the route
  classes, the interval and the backend path read as window 12's, which read as window 10's.
- **The reason holds, and window 12 spent nothing.**
  - Window 12's ONE export POST reached the server and was refused UNEXPECTED (BucketUnmapped), because the page's
    submit carried no `selected_tenant`. Nothing was exported.
  - TO-IV-e-64 carries the tenant on the submit, receipt and download (row DSGN_IRPTV1-S23).
- **Every signing condition carries, as the packet lists them:**
  - the HAR drops the download body;
  - a local PDF lives only in gitignored `tmp/`;
  - the `%PDF` audit reads the served object;
  - no new `*.pdf`, `*.png` or `*.har` enters git;
  - the byte-proof checks run at walk start and end: HEAD `55bbdd71`, clean tracked status, and 0 `/__mockcot/`
    requests;
  - K8 grades the export hop only.

Not measured by this seat: the IV-e-64 diff and the served pins (the packet's).
