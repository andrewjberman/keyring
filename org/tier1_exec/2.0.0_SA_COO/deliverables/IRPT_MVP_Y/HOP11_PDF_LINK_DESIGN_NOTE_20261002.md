# Hop 11 -- the vendor PDF to the advisor: what the code holds today, and one way to close it (design note, reads only)

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~07:2xZ. **Order:** CTO rulings batch 61 item 8 ("the vendor PDF link (hop 11)", after
the catalogue and the resolve fix). **Trace:** `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md`
section 11 ("Close: one authorized same-origin download route for the retained vendor PDF and a link in the preview. Proof:
the bytes downloaded equal the retained PDF's sha256."). No code changed; nothing served; no vendor call.

## Measured

1. **Where the PDF is.** The resident retains the vendor PDF as family `ORIGINAL_VENDOR_PDF` (registry `irpt-x10-v1`:
   tier `state`, table `vendor_documents`, extension `pdf`) in `opal-data-irpt`, and the published `AnalysisReport` carries
   `release.protected_pdf_ref {storage_key, sha256, server_only: true}` (`resident_worker.py`; contract
   `_contracts/AnalysisReport.schema.json:270-294`, where `server_only` means "the reference never reaches the browser as a
   vendor URL").
2. **No route serves it.** `docs/contracts/investor-reporting/v1/routes.json` has no Analysis PDF route; the only download
   route is `GET export/{exportId}/download` (`irpt-export-render`).
3. **The estate's download pattern exists** (`export/download.py`, IB-s-14): the route RE-AUTHORIZES the viewer through
   `_authz.Enforcer.serve` on every call, then returns an OPAL-SIGNED, short-lived (`MAX_URL_TTL_SECONDS` 300) presigned
   S3 GET on the firm's own bucket -- never the bytes, never a vendor URL; `verify()` whitelists the host.
4. **`irpt-status` cannot sign for the PDF today.** Its applied sid `ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly`
   (`irpt-status-policy`, read 07:2xZ) grants `s3:GetObject`/`GetObjectVersion` on `analysis_reports`,
   `normalized_portfolios`, `original_holdings`, `prospect_inputs` and `request_compositions` -- not `vendor_documents`. A
   presigned URL carries its signer's permissions, so the route needs that one family added.
5. **The page renders no link.** PROD's adapter sets `protectedArtifact: null` (`portal adapt.ts:975`; the contract map at
   `:1594` notes `protected_pdf_ref` is server-only); the validator accepts an object `{artifactRef, ...}` when present
   (`validate.ts:421-423`). `VendorPdfPreview.tsx` prints a reference and a route as text.

## One way, recommended

- **Route:** `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/pdf` on `irpt-status`, the owner-read path
  the sections and request reads already use (`OwnedAnalysisReader`, `_final` re-read after I/O). It answers
  `{download_route: {url, expires_at}, sha256, byte_length}`: an Opal-signed URL (300 s) for the report's own
  `protected_pdf_ref.storage_key`, plus the hash the proof compares against. A job that is not READY, or a report without a
  retained PDF, answers by name with no URL.
- **Why this shape:** it reuses the export download's ordering (re-authorize, then sign) and its 300 s ceiling. The URL is
  Opal's own bucket, not a vendor URL, which is what `server_only` forbids. The bytes never pass through the function (no
  6 MB Lambda payload ceiling), and nothing new is written.
- **IAM:** `irpt-status-policy` gains `vendor_documents` among the families of the existing sid (same actions, per enabled
  firm). Terraform in `infra/aws/terraform/investor-reporting/ops/iam.tf` (this seat holds only its selector line).
- **Contract:** one new response schema for the route (closed), and the routes.json row `DECLARED` when served.
- **Page:** `2.0.0_SA_COO~D` turns the preview's text into a link that fetches the route and opens the URL.
- **Proof:** the route's URL is downloaded and its sha256 equals `protected_pdf_ref.sha256` for a READY report (the Overview
  `REQ-a69e5751` and the Multi-Comp `REQ-a1d9abc0` both have one); a foreign firm answers `FIRM_BINDING`.

## For the CTO to rule

1. The route's path and its answer shape (above), or another.
2. The IAM change's placement: an exact-file grant on `ops/iam.tf` for the one family, applied under the route's packet.
3. That a presigned URL on Opal's bucket satisfies `server_only` ("never reaches the browser as a vendor URL"), as the
   export download already does.

## Not known yet

- The retained PDFs' sizes (not needed by a presigned URL; read at the proof).
- Whether the PDF's key family is enabled for every client firm in `irpt-x10-v1` (the grant mirrors the existing sid's
  per-firm list).
