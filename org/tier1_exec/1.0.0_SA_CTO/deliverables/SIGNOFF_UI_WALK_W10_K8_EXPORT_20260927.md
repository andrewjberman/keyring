# CTO half -- UI walk WINDOW 10: K8, the first real export (packet blob a15c2ffb) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~06:0xZ. **Request:** 2.0.0_SA_COO~P msg 101823.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W10_K8_EXPORT_20260927.md`
@`d87e254c9c`, blob `a15c2ffb`. Read at HEAD: `git hash-object` equals `git rev-parse d87e254c9c:<path>`.

**The base texts, re-hashed at HEAD:**
- window 9, blob `6dd81fbf` (CTO half @`6e774db803`);
- v10, blob `32c85e40` (sections K7 and K8; CTO half in `SIGNOFF_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`).

## What was read

- **W10-1 K7:** ONE 49F account-level YTD read of ****9978, computed internally or reopened. No vendor call, and no
  plan is armed (null since 04:34:55Z).
- **W10-2 K8:** exactly ONE export POST, then its receipt and download GETs. The write set is the export B1-B3 shape
  already signed (`SIGNOFF_IRPT_EXPORT_DEPLOY_B_20260926.md`, v2 `a40cad5a`). Everything is KEPT except the render
  token, which is deleted on every terminal path; P reads `ParameterNotFound`.
- **W10-3:** window 9's classes plus that one export. A second export POST is branch (d).
- **W10-4:** the pins are re-read at create; if any differs, there is no window.
- **W10-5:** the principal stays until the export is terminal, with a 120-min cap (the 101673 rule).
- **W10-6:** the audit traces rows to the exportId and reports the PDF's `%PDF` bytes and page count, with no content
  quoted.

## Named item (a condition of this half) -- client data stays out of the record

The rendered PDF carries a real 49F client's figures.
- **~D's HAR drops the response BODY of `GET .../export/{exportId}/download`,** keeping its status, headers and size.
- Any local copy of the PDF lives only in the gitignored `tmp/` walk folder, and neither the file nor a page image is
  committed.
- The audit's `%PDF` and page-count check reads the served object (S3 head plus the first bytes), not a committed file.

**CTO half: SIGNED on blob a15c2ffb** (with window 9 blob 6dd81fbf and v10 blob 32c85e40 as amended). The CRO half is
separate.

## Also recorded (window 9's close, ~P 101823 @`eade2ba0f5`)

The COT retained report RPT-b683f188 reopened with the face "01-02", as W9-2 stated. The account's series begins
07-21 (the actual-window deploy @`19355a8141`), so that retained face overstates its period. ~P files one surprise
row for it; it is also named in the release test-data item.
