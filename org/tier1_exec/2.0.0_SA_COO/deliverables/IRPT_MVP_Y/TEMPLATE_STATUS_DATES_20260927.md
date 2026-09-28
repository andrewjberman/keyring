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

## Update ~20:3xZ: the XLSX template (Y @49f3393cb0)

The portal also accepts `.xlsx`, and that template still answered UNAVAILABLE. `_undated_template_xlsx` re-reads the
raw workbook for what the A/B reader skips unseen. It requires ONE worksheet and every cell in columns A/B, and the rows
holding a value must be exactly the census rows. A second sheet or a third column stays unproved (conservative: a
`holdings_template` sheet plus an instructions sheet is unproved too).

Tests on real openpyxl workbooks through the real intake reader: 1 proved and 5 unproved. `test_prospect_dates` 58,
ops 180 passed and 22 skipped. The live CSV arm still reads READY with the refactored file.

**The patch at the same path is superseded (cumulative, sha256 `4d50bf51..`, apply-check rc=0 on P `118612b599`).
The rebuild's `prospect_dates.py` is `e5bae585..`.** No live XLSX job exists yet.

## ~23:1xZ: the first rebuild (HyEyoJ67) failed at cold start. It was caught before any request and rolled back (CTO 102204)

- P's rebuild (23:00:28Z, CodeSha256 `HyEyoJ67..`) carries this patch's `prospect_dates.py` (`e5bae585`) and
  `submission.py` (`9929a829`) correctly. It also carries HEAD `ops/entry.py` (`d9643b2f`), whose export B0 line calls
  `served.render_ports_from_env()`.
- The zip's `served.py` is the old `41fbd6b5`, the same as bMMJ, and lacks that function. P's HEAD
  `_authz/served.py` (`3a2cdba2`) defines it at :1094.
- The handler `status_installed.lambda_handler` builds its boundary at cold start, so the build raises
  AttributeError: every status, history and sections read would fail for every tenant.
- CloudWatch showed 0 invocations between the deploy and 23:10Z. Y sent this to P and the CTO (102201) at 23:10Z;
  the CTO ruled ROLL BACK to bMMJ/bQ+5, window 19 holds, and the rebuild becomes a new packet with an import smoke.
- **The fix is proved:** HyEyoJ67 with HEAD `_authz/served.py` overlaid builds, and window 15's status read (portal
  header, live reads) answers **READY ANALYSIS_READY, PER_SECTION, 51 dates**.
- **Lesson for the drift census:** it compared Y-owned modules only, so it could not see this `_authz` file. A rebuild
  that takes one file from HEAD needs every file that file imports from HEAD too, which the import smoke catches.
- **Rollback verified by Y (~23:2xZ):**
  - The live CodeSha256 reads `bMMJ/bQ+5` from 23:15:47Z, and the live zip is byte-identical to the pre-rebuild
    zip.
  - Cold start builds. Window 15's history and sections read correctly (51 sections, identical to the retained
    report), and its status read gives the known pre-fix template refusal.
  - CloudWatch shows **one** invocation since 23:00Z, at 23:16:24Z: P's post-rollback cold-start proof. It shows
    **0 errors**, so **no request ever reached HyEyoJ67**.
  - P's ledger is CLOSED as a failed deploy, rolled back (P 102206).
  - The rebuild, with HEAD `_authz/served.py` and the import smoke, is P's next packet. K10 waits for it.
- **Rebuild 2, pre-apply, independent (~23:5xZ):** P's built artifact is `5fSyChId..` (S3 `1CGG3kWY`). Its members
  are served `3a2cdba2`, entry `d9643b2f`, prospect_dates `e5bae585` and submission `9929a829`.
  - `zip_cold_start_smoke.py` PASSES.
  - Window 15's status read (portal header, live reads, 0 writes) answers **READY ANALYSIS_READY, PER_SECTION, 51
    dates**.
  - History and sections are correct (51 sections, identical to the retained report).
- **LIVE (00:02:49Z, 09-28): SERVED and verified by Y at 00:04Z.**
  - The live CodeSha256 is `5fSyChId..`, and the live zip is byte-identical to the artifact verified before apply.
  - Window 15's status read with the portal header answers **READY ANALYSIS_READY, PER_SECTION, 51 dates**.
  - CloudWatch since the apply: 1 invocation (the post-apply cold start), **0 errors**.
  - The screen defect found before K10 is closed in production. K10 can read the row as READY.
