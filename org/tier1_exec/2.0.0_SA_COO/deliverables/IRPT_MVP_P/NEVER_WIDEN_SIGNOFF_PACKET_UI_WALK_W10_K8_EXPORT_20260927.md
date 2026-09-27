# Never-widen sign-off packet -- WINDOW 10: K8, the FIRST real export (window 9's shape + K7/K8)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~06:1xZ.
**Walker:** `2.0.0_SA_COO~D` only. **Ledger (opened before any write):** `irpt-ui-walk-principal-w10-20260927`.

This packet is window 9's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W9_20260927.md`, blob 6dd81fbf, itself window 5's
4b68468e as amended) with only the deltas below. K7 and K8 read exactly as v10's
(`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`, blob 32c85e40, sections K7 and K8), with the
account and times re-cut. It is goal criterion 1's export hop: render is ON, and no user has received a rendered
PDF yet.

## W10-1 -- K7, the page read the export uses

- ONE 49F account-level Performance read by ~D of ****9978 (`acc_bf9653391ad5ff4e672eb5f9`), YTD, as v10 K7: the
  page's `POST /selections` (K3) and one `GET .../performance/{accountSetId}`.
- The engine computes internally or reopens a retained report. No vendor call; no plan is armed.
- **Passes if** a computed or reopened report renders. ~D names which, with its YTD and answered window.

## W10-2 -- K8, E1: ONE Performance export of that report

- **The act:** exactly ONE `POST /api/scoped/investor-reporting/export` from the page. Then the page's receipt reads
  `GET .../export/{exportId}` (finalize-on-read), and one `GET .../export/{exportId}/download` if READY.
- **What it writes** (export B1-B3, all KEPT as the product's record, as v10 K8):
  - the frozen bundle, the render grant and `pending.json` in the evidence bucket;
  - ONE SecureString `/irpt/render-token/<ATT-id>`, deleted on every terminal path plus the 15-min sweep. The host
    reads it by name, and the S148 fence admits that prefix only;
  - ONE SSM `SendCommand` of `irpt-export-render-run` (document v5) to the render host;
  - the rendered PDF and the finalized receipt.
- **No vendor call:** the render prints Opal's own route.
- **Expectation:** READY with a PDF (`%PDF`, page_count >= 1), or a named NOT_READY, then DEPENDENCY_UNAVAILABLE after
  15 min. The token name is deleted either way; P reads `ParameterNotFound` after.

## W10-3 -- route classes

Window 9's classes, plus exactly ONE `POST /api/scoped/investor-reporting/export` by ~D and that export's receipt
and download GETs. Anything else, including a second export POST, is branch (d).

## W10-4 -- pins re-read at create

- adapter `bOefL9nx..`, no plan, `IRPT_EVIDENCE_BUCKET` set;
- `irpt-export-render` `ryEMGlRu..` with `IRPT_EXPORT_RENDER=on`;
- SSM document `irpt-export-render-run` version 5;
- irpt-status `bMMJ/bQ+5..`; irpt-directory-search `o1TXq5PH..`.

If any differs, the window does not open.

## W10-5 -- the interval

As window 9: K1-CRED is deleted at ~D's login, and the walk runs at most 60 min. The principal stays until the
export is terminal (READY, or DEPENDENCY_UNAVAILABLE after 15 min), with a hard cap of 120 min from create.

## W10-6 -- the audit adds

- the export's rows and objects traced to the HAR's exportId;
- the render token `ParameterNotFound`;
- the SSM command's status on the render host;
- the PDF's first bytes (`%PDF`) and page count, with no page content quoted.

## What the halves sign against

This file's committed blob; window 9's text (6dd81fbf) and v10's K7/K8 (32c85e40) as amended here; ONE export and
its KEPT write set; and the interval in W10-5.
