# Never-widen sign-off packet -- irpt-export-render: a pending receipt answers RUNNING, per R11

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-28 ~00:3xZ.
**Rulings:** 1.0.0_SA_CTO 102223 (S27 (b)), 102227 (after the freeze), 102237 (R11 signed: CVO @ab453f59ed, wording
@25f7581ded). **Ledger (opened before any write):** `irpt-export-receipt-running-20260928` (U1 closed).
**Apply:** after MSTR's 03:00-05:00Z freeze.

## 1. What window 19 found (row DSGN_IRPTV1-S27)

The page's single receipt read of a pending export (`exr_9f785460`) answered UNAVAILABLE/NOT_READY with no data, and
the page stopped polling. R2 makes QUEUED and RUNNING the only pending states; UNAVAILABLE is a refusal.

## 2. The change (backend 5c0185fee2; `export/entry.py` only in the zip)

`export_receipt` returns `{"_no_data": True, "_status": {state RUNNING, ...}}` in two cases:
- the `exr_` pointer is BUILDING: reason **EXPORT_BUILDING**;
- the EXP export has no PDF yet: reason **EXPORT_RENDERING**.

The status carries the handle in `operation.revision`, `source_dates` with `source_completion_date` null, and the
default action.

Unchanged:
- UNAVAILABLE stays for real refusals: out of scope, not found, FAILED, TIMED_OUT and BINDING_MISMATCH.
- A READY receipt is unchanged.
- `export_download` still refuses NOT_READY for a pending export: a download authorizes a finished artifact, and R11
  covers the receipt route only.

`served.response_envelope` already admits a data-less answer only for QUEUED or RUNNING (`served.py:344`).

**Tests** (export 121 passed):
- the two pending assertions now expect RUNNING (BUILDING, then RENDERING), and the download stays refused;
- NEW: the served pending envelope validates against R11's `export-receipt.response.schema.json`.
- Negative control: the same envelope FAILS the pre-R11 schema with `'data' is a required property`.

## 3. The artifact and the move

| | live | new |
|---|---|---|
| irpt-export-render CodeSha256 | `Ulim/gmf..` (S3 version JgYVUcWE.) | `BORQ2shb..` (S3 version O1Vu8CyD.) |

- **Census:** 59 -> 59; ONLY `entry.py` differs. The zip packages no response schema.
- **Built-zip cold-start smoke** (~Y's `zip_cold_start_smoke.py`, the export receipt route): PASS. The live zip also
  passes; the smoke guards cold start, while the RUNNING behaviour is proven by the tests.
- **Dry plan** (export root): 0/1/0, code only. Rollback: restore S3 version JgYVUcWE. (Ulim/gmf) as latest and
  re-apply.

## 4. Blast radius -- both branches

- **A pending receipt read:** UNAVAILABLE NOT_READY -> RUNNING (EXPORT_BUILDING / EXPORT_RENDERING), with no data.
  - Before: the page stops.
  - After: the page's existing poll continues, with ~D's S27 page fix (TO-IV-e-78) naming any real refusal.
- **Every other receipt answer** (READY, refused, FAILED, TIMED_OUT) and the download route: unchanged.
- **Reachable:** the walk windows' export reads only.

## 5. Apply protocol (CRO 102250)

1. A LIVE before-read, ahead of the apply: one receipt read of an existing `exr_` handle (`exr_9f785460`, SUBMITTED,
   no PDF). Before, it reads UNAVAILABLE/NOT_READY; after, it must read RUNNING EXPORT_RENDERING or the named
   RenderTimedOut it has become.
2. safe-apply, then the live CodeSha256 read back and a cold-start invoke (Init Duration, no FunctionError).
3. The same read after. Any unnamed difference means a same-turn rollback.

## What the halves sign against

This file's committed blob; backend 5c0185fee2; artifact BORQ2shb with its census, smoke, 0/1/0 plan and rollback;
the apply protocol in section 5.
