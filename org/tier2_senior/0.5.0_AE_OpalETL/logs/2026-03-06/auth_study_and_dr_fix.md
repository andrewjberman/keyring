# Auth Study + DataRefresh saa_excel Fix — 0.5.0_AE_OpalETL

**Date:** 2026-03-06
**Start Time:** 15:00
**End Time:** 15:30

## Objective

1. Study the full auth setup and save as architecture document in AE deliverables.
2. Run through the data-refresh pipeline end to end.
3. Fix the 400 "No recognized file types" error for xlsx uploads.

---

## Root Cause of 400 Error

`POST /api/scoped/data-refresh/trigger` returns:
```
{"error": "No recognized file types uploaded. Expected: data*.pkl, model*.pkl,
 *cma*.xlsx, *peer*.xlsx, *attribution*.xlsx, *regression*.csv"}
```

Source: `handle_trigger()` in `infra/aws/lambda/data_refresh/lambda_function.py`
calls `generate_manifest_from_files()` which auto-detects file types from filenames.

**Gap:** The yang-pipeline trigger Lambda's `FILE_TYPE_CONFIG` includes `saa_excel`
(pattern: `Opal SAA YYYYMMDD vN.xlsx`, frequency: monthly) but `generate_manifest_from_files`
did not have a detection branch for `saa` in xlsx filenames. Any SAA Excel uploaded
through the DataRefresh page would fail at trigger time with this 400.

---

## Fix Applied

`infra/aws/lambda/data_refresh/lambda_function.py` — added to the `.xlsx` detection block:

```python
elif 'saa' in filename_lower:
    file_type = 'saa_excel'
```

Also updated the error hint message to include `*saa*.xlsx`.

---

## Auth Architecture Document

Written to: `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/auth_architecture.md`

Covers:
- Full auth stack (custom JWT RS256, NOT Cognito)
- opal-users-v2 DynamoDB schema (key schema, GSIs, fields)
- opal-partner-49financial table (ADVI J1/J2/J3 context)
- JWT structure (access + refresh tokens, all claims including ADVI advisor fields)
- Auth handler routes + login/refresh flows
- Portal authorizer permission model (Dev/internal vs advisor+admin vs advisor+user)
- API route families (general/scoped/private)
- 401 refresh mutex in api-client.ts
- DataRefresh + SSCN pipeline endpoint reference

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit lambda_function.py — add saa_excel to generate_manifest_from_files | Done |
| 2 | Write auth_architecture.md | Done |
| 3 | Commit both changes | `db3770bd` 0.5.0_AE_OpalETL: data-refresh -- add saa_excel + auth architecture doc |
| 4 | build-and-upload.sh other opal-data-refresh-api | SHA256: `9jGMyN7q8733U95I/ddSXYfOUQgnLaRkdSuKCSbXIJo=` (16K) |
| 5 | Commit source map | `af5b2a91` ci: upload artifacts other/opal-data-refresh-api [skip ci] |
| 6 | terraform plan (other) | 1 to change (Lambda code/version) |
| 7 | terraform apply (other) | 1 changed |
| 8 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 9 | record-terraform-deploy.sh other --version other-v1.3.0 | `c908ba08` ci: record deploy other @ af5b2a91 |
| 10 | Tag + push | `other-v1.3.0`, pushed to origin CLOUD |

---

## Auth Architecture Findings (Summary)

| Topic | Finding |
|-------|---------|
| Auth system | Custom JWT RS256 — NOT Cognito |
| Password hashing | bcryptjs 12 rounds (~150ms latency at login — explains perceived slowness) |
| Refresh token transport | HttpOnly cookie only (not body/header) |
| Access token transport | localStorage → Authorization: Bearer header |
| Token TTLs | Access: 15min, Refresh: 7 days (not rotated on refresh) |
| Partner identity | opal-partner-49financial, keyed by email, read at login/refresh for advisor-intelligence users |
| Portal authorizer | Lambda authorizer, passes firmId/advisorKey/advisorRole to Lambda context (ADVI J3) |
| API routing | /auth/* → auth handler direct API GW; /api/general/* → portal-proxy via CloudFront; /api/scoped/* → data-refresh-api via Lambda authorizer |
| 401 mutex | Single refresh promise in api-client.ts — all concurrent 401s wait on same refresh |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| other | `other-v1.3.0` | `af5b2a91` (source/artifacts), `c908ba08` (record) |

---

## Status

COMPLETE. Both deliverables done:
1. `auth_architecture.md` written and committed.
2. `saa_excel` fix deployed to `opal-data-refresh-api` at `other-v1.3.0`.

---

## Notes

- The DataRefresh UI correctly separates DataRefresh uploads (yang pipeline, pkl/xlsx/csv)
  from SSCN uploads (security_scanner/uploads/, FactSet Screening xlsx).
  The Screening_*.xlsx file is NOT a DataRefresh file — it goes through the SSCN endpoint
  (`POST /security-scanner/upload-url`). Do not upload Screening xlsx through DataRefresh.
- The yang trigger's FILE_TYPE_CONFIG and data-refresh lambda's generate_manifest_from_files
  should stay in sync. If new file types are added to yang's FILE_TYPE_CONFIG in the future,
  add corresponding detection to generate_manifest_from_files as well.
