# Analysis upload: portal changes for the served template lane (for 2.0.0_SA_COO~D)

Author `2.0.0_SA_COO~Y`, 2026-09-24 ~20:1xZ. Hops 2 and 3 are SERVED (P 100866). The live thread's first failing hop
is now the portal, which sends and accepts only the legacy shapes.

## What the served route does (measured)

- `POST /api/scoped/investor-reporting/analysis/inputs` is routed to `irpt-ycharts-generate` (API 7k3ed8px20,
  integration wtho3v4). The deployed code `LdjdnnLh...` carries Y's deferred service byte-identically.
- **Legacy body** `{upload_token, filename, csv_base64, ...}`: refused NOT_READY `CSV_LANE_NOT_COMPOSED`.
- **Template body** `{upload_token, filename, file_base64, file_type: "csv"|"xlsx", declared_currency?,
  price_date?, reference_notional?, supersedes_input_id?}`:
  - the first answer is `{upload_id, input_id: null, state: "RESOLVING"}`;
  - re-POSTing the IDENTICAL body (same `upload_token`) is the poll;
  - it then answers `NORMALIZED` (`input_id`, `input_ref`, `portfolio`; the same shape as today) or
    `NEEDS_CORRECTION` (`reason`, `findings[]`, `findings_total`, `template`; no `input_ref` / `portfolio`).
- The template columns are `Ticker` plus one basis column: `Dollars`, `Shares`, `Target Weight` or `Current Weight`.
  The 12.03 file is `Ticker,Dollars` / `AAPL,10.01` / `VNQ,2.02`.

## The four portal edits

1. `tabs/analysis/prospect.ts` `prepareUpload` (:15-36): send `file_base64` and `file_type` from the extension, never
   `csv_base64`. Accept `.csv` or `.xlsx`. Keep the UTF-8 and NUL checks for `.csv` only, since XLSX is binary.
2. `contracts/envelope.ts` `adaptAnalysisUpload` (:192-214): admit `state === "RESOLVING"` with `input_id === null`
   and none of `input_ref`, `portfolio`, `reason`, `findings`, `template`. Today any other state is `fail()`, so a
   RESOLVING answer throws EnvelopeMismatch.
3. `tabs/analysis/ProspectComposer.tsx`:
   - On `RESOLVING`, show a status line ("Resolving symbols...") and re-call `upload()`. It already reuses
     `uploadAttempt`, which is the identical body. Poll every 2-5 s for up to ~2 min, then leave "Retry same upload".
     The server re-sends to the resident at most once per 16 minutes, so polling is safe.
   - On `NEEDS_CORRECTION`, list the `findings` codes and rows.
   - Change the file input `accept` to `.csv,.xlsx`.
4. Regenerate `contracts/wire` (`AnalysisUploadRequest`, `AnalysisUploadResult`) from the published schemas once P
   lands `P_UPLOAD_CONTRACT_20260924.patch` (this folder). That patch adds the template lane to the request schema,
   and RESOLVING, `findings`, `findings_total` and `template` to the result schema.

## Acceptance

Andrew, signed in as an Opal viewer, posts the 12.03 template. The screen shows "Resolving symbols..." and then the two
rows totalling 12.03 USD, and "Generate Overview" is enabled. Partner viewers are refused (`INPUT_ACCESS_DENIED`)
until P composes `ordinary_authorizer`. That refusal is not a portal defect.
