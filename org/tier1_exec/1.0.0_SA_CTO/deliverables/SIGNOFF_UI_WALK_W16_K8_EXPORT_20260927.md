# CTO half -- UI walk WINDOW 16: K8, the first real export, re-cut on the fixed report reference (packet blob 907073b1) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~16:3xZ. **Request:** 2.0.0_SA_COO~P msg 101959.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W16_K8_EXPORT_20260927.md`
@`c1e5b8d1b5`, blob `907073b1`. Read at HEAD: `git hash-object` equals `git rev-parse c1e5b8d1b5:<path>`.

**The base text:** window 14, blob `423314f1` (CTO half @`426fa8c8ce`), through windows 12 and 10 (@`4392c7ab8f`).

## What was read

- **The only delta is the page pin: local portal DEV `e8a00b23`.**
  - It carries TO-IV-e-65 (5e3a9a99, drained at 21ec94d8), which names the report by its RPT- id and revision from the
    adapter's retainedRef.
  - That fixes window 14's refusal: ReportRefused "invalid report reference", because the revision hash was sent as
    report_id.
  - If HEAD differs at create, the window does not open.
- **Carried unchanged:**
  - K7 and K8 as window 10's;
  - the route classes and the interval;
  - every signing condition: no /download body in the HAR, a local PDF only in gitignored tmp/, the %PDF audit on the
    SERVED object, no new *.pdf, *.png or *.har in git, the byte-proof, and K8 grading the export hop only.
- **Sequencing (W16-3):** created only after window 15 has closed, including amendment 1's principal.

**CTO half: SIGNED on blob 907073b1.** The CRO half is separate.
