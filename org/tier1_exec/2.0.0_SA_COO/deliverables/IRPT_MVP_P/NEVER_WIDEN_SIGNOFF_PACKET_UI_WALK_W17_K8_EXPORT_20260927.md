# Never-widen sign-off packet -- WINDOW 17: K8, the FIRST real export, on the reopen-rule export code

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~17:5xZ.
**Walker:** `2.0.0_SA_COO~D` only. **Ledgers (opened before any write):** `irpt-ui-walk-principal-w17-20260927`, plus the
open A1 of `irpt-export-reopen-rule-20260927`.

This packet is window 16's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W16_K8_EXPORT_20260927.md`, blob 907073b1, signed CTO
@93780555f5 and CRO @ff6622ce41, and through it windows 14, 12 and 10) with ONLY the deltas below. Every other section reads
as window 16's, including:
- K7 and K8 exactly as window 10's (ONE 49F ****9978 YTD read, ONE export POST, the receipt GETs, ONE download if READY), the
  route classes and the interval;
- every signing condition: the /download BODY out of the HAR, a local PDF only in gitignored tmp/, the %PDF audit on the
  SERVED object, no new *.pdf, *.png or *.har in git, the byte-proof at walk start and end, and K8 grading the export hop only.

## W17-1 -- why a re-run

Window 16's ONE export POST carried the tenant and the correct report reference (IV-e-53, 64 and 65 all held). It was refused
ReportDenied because the export admitted ONLY the report's owner principal, while K7 reopens a report an earlier window's
principal computed. CTO 101991 ruled (a): a caller who may view a report may export it. That change is SERVED:
irpt-export-render **3EST/hewG** since 17:34:21Z (backend f92445392d; packet 12a1afda, both halves; ledger
irpt-export-reopen-rule-20260927, D1 closed, A1 open for this window).

## W17-2 -- the pins, re-read at create

- irpt-export-render `3EST/hewG..` with `IRPT_EXPORT_RENDER=on`, and the SSM document irpt-export-render-run v5;
- adapter `bOefL9nx..` with no plan and `IRPT_EVIDENCE_BUCKET` set; irpt-status `bMMJ/bQ+5..`; irpt-directory-search
  `o1TXq5PH..`;
- the page: local portal DEV `e8a00b23`, 0 tracked changes.

If any differs, the window does not open.

## W17-3 -- the export change's arms, run in this window (CTO 101994 condition 3, CRO 101995)

1. **Arm 1:** this window's principal exports RPT-b5e0a16e, which it did NOT compute (an earlier window's principal owns
   it). The expected result is a receipt that finalizes READY with a %PDF.
2. **Arm 3:** the report's owner row is unchanged: the REPORT# row's owner principal_id before equals after.
3. **Arm 4:** the render grant (`firms/49financial/generations/exr_*/render_grant.json`) and the receipt name THIS window's
   principal as the delegator, never the original owner.

**On any arm failing** (a caller admitted who should not be, or a grant naming the owner), P rolls irpt-export-render back to
S3 version 9atDu8b. (ryEMGlRu) in the same turn, before any other export (CRO 101995).

## W17-4 -- arm 2, a NAMED DEPARTURE (CTO 101994 condition 2)

A direct invoke of 3EST/hewG as a caller missing one account could not be staged:
- the only synthetic subject without a real identity, V0 (a 49F advisor with no grant), is refused one layer EARLIER, at the
  Entry's Enforcer (AuthzError EMPTY_GRANT, public NOT_AUTHORIZED, corr-2bf9a61aa2d9);
- a "missing ONE account" caller needs a real advisor identity holding partial grants, which P does not impersonate.

In its place, the unit proof ran ON THE DEPLOYED BYTES (the extracted 3EST/hewG zip's own retained_export.py and
repository.py):
- arm 1 admitted, with the owner unchanged and the grant naming the caller;
- a caller missing one account got ReportDenied;
- a cross-firm caller got ReportDenied.

**The CTO's half is asked again on this departure.**

## What the halves sign against

This file's committed blob; window 16's text (907073b1) and all its conditions; the export code 3EST/hewG; arms 1, 3 and 4
in this window with the same-turn rollback; and arm 2's named departure.
