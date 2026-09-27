# Never-widen sign-off packet -- WINDOW 12: K8, the FIRST real export, re-cut on the fixed page

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~13:3xZ.
**Walker:** `2.0.0_SA_COO~D` only. **Ledger (opened before any write):** `irpt-ui-walk-principal-w12-20260927`.

This packet is window 10's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W10_K8_EXPORT_20260927.md`, blob a15c2ffb, signed CTO
@4392c7ab8f and CRO @5e2f9b7ad4) with ONLY the deltas below. Every unnamed section reads as window 10's, including:
- K7 (ONE 49F ****9978 YTD read) and K8 (exactly ONE export POST, the receipt GETs, ONE download if READY), and
  their KEPT write set;
- the route classes, the interval (walk <= 60 min; the principal stays until the export is terminal; cap 120 min);
- the conditions named at signing: the HAR drops the /download response BODY, any local PDF lives only in gitignored
  tmp/, the %PDF and page-count audit reads the SERVED object (CTO 101825), and no new *.pdf, *.png or *.har enters
  git (CRO 101826).

## W12-1 -- why a re-cut

Window 10's K8 was not run. The page's Export preview refused client-side because its Performance fetch omitted
`selected_tenant`: 2 GETs at 06:25:22Z answered UNAVAILABLE/UNEXPECTED, and resolveBundle.ts:255 rethrew
(DSGN_IRPTV1-S20/S22). The fix is TO-IV-e-53 (97c08b21). It threads selectedTenant through the preview's
Performance request, and PrintEntry reads an optional `selected_tenant`, sending nothing when it is absent.

## W12-2 -- the page

Local portal DEV **1f149d69** (IV-e-53 + IV-e-54 + IV-e-58; tsc 0, lint 0, suite 912 pass / 27 skip / 6 fail, 0 new;
~D 101887), served by the main checkout at `localhost:5174`. It is local only, not on origin. ~D logs portal HEAD and
tracked status at walk start and end (window 9's byte-proof, CRO 101816).

## W12-3 -- the backend path is unchanged

The print path takes its firm from the render token (`firmId` = the grant's firm, `_render_identity/mint.py:180`);
the print URL carries no `selected_tenant` (`retained_export.py:89-100`; host allow-list `render_export.cjs:83`)
(P 101839 reply). Pins re-read at create: adapter `bOefL9nx..` with no plan and `IRPT_EVIDENCE_BUCKET` set;
`irpt-export-render` `ryEMGlRu..` with `IRPT_EXPORT_RENDER=on`; SSM document `irpt-export-render-run` v5;
irpt-status `bMMJ/bQ+5..`; irpt-directory-search `o1TXq5PH..`.

## What the halves sign against

This file's committed blob; window 10's text (a15c2ffb) and its signing conditions, as amended here; the page pin
1f149d69.
