# Before K10: window 15's READY job reads wrong on status-job; fixed on the Y branch, and the rebuild is P's

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~19:5xZ. Case: `cottonwood` / `REQ-67e12718..` (READY, `RPT-5288c06d..`), from the
TEMPLATE_UPLOAD lane.

## What the portal would see

The portal sends `X-IRPT-Status-Dates: prospect-v1` on every status-job read (`portal/.../fixtures/wire/requests/
status-job.request.json`). The history view reads each row's status, then opens the row's sections
(`tabs/analysis/OwnedRequestHistory.tsx`).

Measured on the served `irpt-status` zip (CodeSha256 `bMMJ/bQ+5..`), with live reads as an Opal viewer, that header,
and 0 writes:

| Package | status-job for window 15 |
|---|---|
| as served | **refused**: public `INVALID_INPUT`, internal `DATE_SOURCE_OWNER_BINDING` |
| + P HEAD's `submission.py` (sha256 `9929a829..`, the generate zip's) | `UNAVAILABLE ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE` |
| + that `submission.py` + Y's `prospect_dates.py` (`70079fcf..`; re-run with `e5bae585..`, the same) | **`READY ANALYSIS_READY`**, `date_basis PER_SECTION`, 51 section dates |

The sections read already serves all 51 sections, identical to the retained report, and so does the history list. As
served, the row state shows "unavailable" and the job-status panel fails.

## Causes

1. **Packaging (P):** the served zip's `submission.py` predates the template-lane owner fix.
   - `input_repository_owner` adds `account_ids`/`prospect_input_id` for `CSV_UPLOAD` only.
   - P's HEAD and the generate zip use `PROSPECT_UPLOAD_LANES`.
2. **The date proof (Y, `ops/prospect_dates.py`):** it proved only the CSV_UPLOAD lane, so every template job read
   UNAVAILABLE even when bound.

## The fix (Y @6998d0acff; `P_TEMPLATE_STATUS_DATES_20260927.patch`, apply-check rc=0 on P `118612b599`)

`_undated_template_csv` is a positive proof for the v2 two-column CSV template.
- **Headers:** Ticker/Symbol, with a basis of Dollars, Target Weight or Current Weight. Shares is priced, so it is out.
- **Raw re-read:** every row must be exactly two cells. A date in column C would otherwise be dropped unseen by the
  A/B reader.
- **Cells:** every non-blank row must be the census's own cells, with no formula, invalid cell, finding, price or
  price_date.
- **Digest:** the file's digest must equal the template's `content_sha256`.
- **Reach:** `input()` reads the original as `ORIGINAL_HOLDINGS` under the same bindings. XLSX answers "unavailable"
  without reading the original, and nothing new refuses.

Tests:
- `test_prospect_dates` 52 passed. The new tests are the live shape; 10 refusal arms; and `input()` for CSV proved,
  dated CSV None, and XLSX None with no original read.
- ops suite 174 passed, 22 skipped. ruff clean.

## To serve it (P, with its own ledger and never-widen halves: the public status answer moves)

Rebuild `irpt-status` from P's HEAD plus this patch. The zip must carry `submission.py` `9929a829..` and
`prospect_dates.py` `e5bae585..`. Re-run the three arms above on the new zip; the third is the expectation.

## Update ~20:4xZ: the XLSX template (Y @49f3393cb0)

The portal also accepts `.xlsx`, and that template still answered UNAVAILABLE. `_undated_template_xlsx` re-reads the
raw workbook for what the A/B reader skips unseen. It requires ONE worksheet and every cell in columns A/B, and the rows
holding a value must be exactly the census rows. A second sheet or a third column stays unproved (conservative: a
`holdings_template` sheet plus an instructions sheet is unproved too).

Tests on real openpyxl workbooks through the real intake reader: 1 proved and 5 unproved. `test_prospect_dates` 58,
ops 180 passed and 22 skipped. The live CSV arm still reads READY with the refactored file.

**The patch at the same path is superseded (cumulative, sha256 `4d50bf51..`, apply-check rc=0 on P `118612b599`).
The rebuild's `prospect_dates.py` is `e5bae585..`.** No live XLSX job exists yet.
