# Never-widen sign-off packet -- WINDOW 14: K8, the FIRST real export, re-cut on the fixed submit

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~14:5xZ.
**Walker:** `2.0.0_SA_COO~D` only. **Ledger (opened before any write):** `irpt-ui-walk-principal-w14-20260927`.
**Numbering:** window 14 is this export re-cut. The next Analysis attempt becomes window 15.

This packet is window 12's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W12_K8_EXPORT_20260927.md`, blob 36c196ed, signed CTO
@0fe93a1b92 and CRO @377a66b6de, itself window 10's a15c2ffb) with ONLY the page pin moving. Every other section reads
as window 12's, including K7 and K8 exactly as window 10's, the route classes, the interval, and every signing condition:
- the HAR drops the /download BODY;
- any local PDF lives only in gitignored tmp/;
- the %PDF audit reads the SERVED object;
- no new *.pdf, *.png or *.har enters git;
- the byte-proof checks at walk start and end;
- K8 grades the export hop only.

## W14-1 -- why a re-cut

Window 12's ONE export POST reached the server and was refused (UNEXPECTED, BucketUnmapped), because the SUBMIT carried
no `selected_tenant` (buildSubmitRequest, submit.ts:64-78). Nothing was exported (ledger
irpt-ui-walk-principal-w12-20260927). The fix is TO-IV-e-64 (512e3ba1, drained at 55bbdd71). It carries selectedTenant on
the export submit, receipt and download (row DSGN_IRPTV1-S23).

## W14-2 -- the page

Local portal DEV **55bbdd71**, served by the main checkout at `localhost:5174` (HEAD read 14:5xZ: 55bbdd71, 0 tracked
changes). It carries IV-e-53 (the preview) and IV-e-64 (the submit, receipt and download). If HEAD differs at create, the
window does not open.

## W14-3 -- backend unchanged

As W12-3: the pins are re-read at create, and the print path takes its firm from the render token.

## What the halves sign against

This file's committed blob; window 12's text (36c196ed) and all its signing conditions, with only the page pin moved to
55bbdd71.
