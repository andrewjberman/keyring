# E7 -- serve the chosen comparisons' names: what the code holds today (design note, reads only)

**Author:** `2.0.0_SA_COO~Y`, 2026-10-01 ~17:5xZ, written while held for the reboot (no code changed, nothing served).
**Order:** CTO rulings batch 98 items 1-3 @29a6581479 (msg 103913): serve the chosen comparisons' names from the
request's frozen keys and the catalogue's labels, never read back from the PDF; `2.0.0_SA_COO~D` then shows them.

## Measured

1. **The served read the page opens a request with** is `GET /api/scoped/investor-reporting/analysis/requests/{requestId}`,
   operation `analysis-request-read`, handler `irpt-status` (`ops/entry.py:178-180`, `:201`). It returns
   `OwnedRequestReader._public(record)` = `{identity, accepted_at}` only (`ops/owned_requests.py:119-129`).
2. **Its contract is closed:** `docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json` has
   `additionalProperties: false` and properties `identity`, `accepted_at`; the response schema
   `responses/analysis-request-read.response.schema.json` is also closed. A new field is a PUBLISHED contract change,
   consumer `IRPT_FNTEND`.
3. **The accepted record carries no names.** `irpt-requests` row for `REQ-a1d9abc0bc037ea3d9e4a7ed` (read 17:5xZ):
   record keys `accepted_at`, `browser_sha256`, `composition_ref`, `identity`, `owner`. The names live only in the
   frozen composition blob (`REQUEST_COMPOSITION`, 26,919 bytes for this request).
4. **The composition holds both halves E7 needs**: the browser's `comparison_keys` (`comp["browser"]`) and, per key,
   the frozen catalogue entry with `vendor_id` and `name` (`comp["resolved"]["comparison_catalog"]`); the case trace
   reads exactly these (`live_walk/case_trace.py:184-199`) and found them equal to the catalogue for this request.
5. **Today's read never fetches the blob:** `_materialize` only HEADs the composition reference
   (`owned_requests.py:102-106`). Serving names means one blob GET per request read, or a field written at
   acceptance.

## Two ways, one recommended

- **A (recommended): the request read fetches the frozen composition and projects `comparisons: [{key, label}]`**,
  in the browser's key order, empty for an Overview. The label is the frozen catalogue `name` (`Opal Short-Term`, `Opal Intermediate-Term` for this request, as the case
  trace read them). One blob GET per read, inside the
  reader's existing materialize/final bracket, so a changed or expired composition still refuses. Contract: one
  optional property on `OwnedAnalysisRequest` (array, max 5, items `{key, label}`, both strings, closed); history
  items stay `{identity, accepted_at}` (no blob GET per history row). Owner of the contract text: `1.0.0_SA_CTO`;
  of the page: `2.0.0_SA_COO~D`.
- **B: write the names onto the accepted record at acceptance.** No GET on read, but only for new requests; every
  existing request would need a backfill of an immutable record. Not recommended.

## Not known yet

- ~~Whether `irpt-status` may GET a composition blob~~ -- READ 17:5xZ: DESIRED yes. `infra/aws/terraform/investor-reporting/ops/iam.tf:72-87`,
  sid `ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly`, grants `s3:GetObject` and `s3:GetObjectVersion` on
  `irpt/<firm>/state/request_compositions/*` in the irpt product bucket, per enabled client firm. APPLIED is inferred,
  not read: the served status route's dates read (`ops/prospect_dates.py`) already reaches retained families under the
  same statement and answered READY for this lane's jobs today. One live read of the applied policy settles it.
- The served change rides a never-widen packet for `irpt-status` (whole bundle, both halves), separate from the
  resident's st10.
