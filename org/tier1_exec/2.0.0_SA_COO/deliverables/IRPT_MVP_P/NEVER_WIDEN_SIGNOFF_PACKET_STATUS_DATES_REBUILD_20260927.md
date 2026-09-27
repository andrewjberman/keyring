# Never-widen sign-off packet -- irpt-status rebuild: the template status dates, HEAD submission.py, the render_ports line

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~22:5xZ.
**Asked by:** ~Y 102050, 102067 and 102087 (before K10: served irpt-status refuses window 15's READY job on the
portal's status read). **Ledger (opened before any write):** `irpt-status-dates-rebuild-20260927` (U1 closed).

## 1. What changes -- exactly the three files ~Y's SERVED_DRIFT_CENSUS_20260927.md named

| member | live sha256 | new sha256 | source |
|---|---|---|---|
| submission.py | 5460fcdc | 9929a829 | HEAD's (PROSPECT_UPLOAD_LANES) |
| prospect_dates.py | 8ffe01a5 | e5bae585 | backend c296cdff9c (~Y P_TEMPLATE_STATUS_DATES, 4d50bf51.., cumulative) |
| entry.py | 9da6a1a6 | d9643b2f | HEAD's (`render_ports=_entry.render_ports_from_env()`, bd52efb246) |

- Artifact `bMMJ/bQ+5..` -> `HyEyoJ67..` (S3 version zswWyPDn.). Census: 43 -> 43; only those three differ.
- ops suite: 180 passed / 22 skipped.
- Dry plan (ops root): **0/1/0**, code only. Rollback: re-apply at S3 version 7xPCOM83. (bMMJ/bQ+5).

## 2. Blast radius -- both branches

- **The prospect status-dates read** (the portal sends X-IRPT-Status-Dates: prospect-v1). ~Y measured all three
  states on the live reads:
  - served today: REFUSED, DATE_SOURCE_OWNER_BINDING;
  - with HEAD's submission.py alone: UNAVAILABLE, DATE_BASIS;
  - with both files: READY ANALYSIS_READY PER_SECTION, 51 dates.
  - A CSV or one-sheet A/B XLSX template reads READY. A second sheet or a third column stays "unavailable", never
    refused.
- **render_ports: INERT on this function.** irpt-status's env has no `IRPT_EVIDENCE_BUCKET` (read live:
  IRPT_DIRECTORY_BUCKET_MAP, IRPT_DIRECTORY_KEY, IRPT_JOBS_TABLE, IRPT_REQUESTS_TABLE), so
  `served.render_ports_from_env()` returns None (`_authz/served.py:1102-1103`). Every RENDER_DELEGATE status read
  refuses, exactly as today.
- **Every other status answer is unchanged.** Reachable today: the walk windows' status reads only.

## 3. Proof

K10 in the next Analysis/page window: window 15's READY job (REQ-67e12718) reads READY on the portal's status read
(ledger A1).

## What the halves sign against

This file's committed blob; the three members and the artifact with its census, 0/1/0 plan and rollback; the blast
radius in section 2.
