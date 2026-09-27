# Never-widen sign-off packet -- WINDOW 16: K8, the FIRST real export, re-cut on the fixed report reference

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~16:2xZ.
**Walker:** `2.0.0_SA_COO~D` only. **Ledger (opened before any write):** `irpt-ui-walk-principal-w16-20260927`.

This packet is window 14's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W14_K8_EXPORT_20260927.md`, blob 423314f1, signed CTO
@426fa8c8ce and CRO @bae0782a84, and through it windows 12 and 10) with ONLY the page pin moving. Every other section
reads as window 14's, including:
- K7 and K8 exactly as window 10's, the route classes, and the interval;
- every signing condition: the /download BODY out of the HAR, a local PDF only in gitignored tmp/, the %PDF audit on
  the SERVED object, no new *.pdf, *.png or *.har in git, the byte-proof at walk start and end, and K8 grading the
  export hop only.

## W16-1 -- why a re-cut

Window 14's ONE export POST carried selected_tenant (the tenant hop holds) and was refused ReportRefused "invalid report
reference": the page sent the REVISION hash as `report_id` (ledger irpt-ui-walk-principal-w14-20260927). The fix is
TO-IV-e-65 (5e3a9a99, drained at 21ec94d8). The export names the report by its RPT- id and revision from the adapter's
retainedRef.

## W16-2 -- the page

Local portal DEV **e8a00b23**, served by the main checkout at `localhost:5174`. HEAD read 16:2xZ: e8a00b23, 0 tracked
changes, 21ec94d8 an ancestor. It carries IV-e-53, IV-e-64, IV-e-65 and IV-e-57. If HEAD differs at create, the window
does not open.

## W16-3 -- sequencing

It is created only after window 15 (the Analysis attempt, ~Y) has closed, so no two walk principals live at once.

## What the halves sign against

This file's committed blob; window 14's text (423314f1) and all its signing conditions, with only the page pin moved to
e8a00b23, created after window 15 closes.
