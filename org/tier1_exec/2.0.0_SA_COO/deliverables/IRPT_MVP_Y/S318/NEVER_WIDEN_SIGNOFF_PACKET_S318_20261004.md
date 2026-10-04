# Never-widen sign-off packet -- S318 (CTO batch 243, option b): irpt-status proves the YCharts holdings template undated when its only cells outside A/B are the template's pinned boilerplate

**For:** `1.0.0_SA_CTO` (CTO half; batch 243: "this seat signs on receipt"). **Author and operator:** `2.0.0_SA_COO~Y`,
2026-10-04 ~23:4xZ.

**Why:** rows IRPT_BCKEND-S318 and S321 (@07bb047d22). Every READY analysis of the YCharts holdings template (the easy file
Andrew's clients fill) reads "Unavailable -- analysis status date basis unavailable" on the page. The cause, measured
offline: the template has 7 text cells outside columns A/B (a notes label, an instructions paragraph and column labels),
plus 1,233 empty styled cells. `_undated_template_xlsx` refused any cell outside A/B.

**Ledger:** `irpt-s318-boilerplate-20261004` (U1 closes on this packet's artifact; D1 and V1 are open). **One move:** the
irpt-status code. No IAM, route, table, schema or contract changes.

## 1. What ships

**The code:** `780c86d763`, merged `7100c2f432`; the irpt-status row was repinned at `7100c2f432` (`4fac1fefb2`); artifact row
`00742606d3`, merged `615ee9b611`.

`ops/prospect_dates.py`, `_undated_template_xlsx`:
- The template's own boilerplate is admitted by POSITION and EXACT TEXT. Each of the 7 cells is pinned by
  address and the sha256 of its text, and the set by `_TEMPLATE_BOILERPLATE_SET_SHA256` (`badb2606..`). The text itself is
  not in git.
- A cell outside A/B with no value, inline string or formula is admitted.
- Any other valued cell outside A/B refuses: an unpinned address, a formula, a number, a date serial or a boolean.
- A pinned cell whose text differs refuses and prints `IRPT_PROSPECT_DATES_TEMPLATE_CHANGED cell=<addr>`. A pin set that
  does not match its hash prints `IRPT_PROSPECT_DATES_BOILERPLATE_PINS_CHANGED` and refuses.
- Row equality is graded on the A/B values against the census. A plain A/B workbook is proved exactly as before.

**The artifact (U1):**
- `irpt-status.zip`, version `jVkDK9v6qfVw12iBAWcSbGgO9paauYtD`, 348,612 bytes, sha256
  `XPta1UMJzLzB+Ba1Yn+KraRRZmxxo6R0/N50sNNN3q8=`.
- Built LF from `4fac1fefb2`. Built zip vs the pin's bundle: 49 members, 0 differ, 0 CRLF.
- **Census vs live `hC6Pramt..`** (`CENSUS_S318_VS_LIVE_20261004.json`): identical 46, changed 3, added 0, removed 0.
  - `prospect_dates.py`: this change.
  - `infra/logic/registry/reporting_policies.json`: the additive row `irpt-ycdgen-research` (c6c3c0b674).
  - `infra/logic/registry/systems.json`: the additive NFRA_SPRINTWIN systems row (4201d79857).

  The two registry files move under the whole-bundle rule. Each adds a row, and no row irpt-status reads changes.
- **Cold-start smoke PASS** on the built bytes (`ZIP_COLD_START_SMOKE_S318_20261004.txt`): status, request-read and
  sections routes; the build answers; every first-party module comes from the zip.

**Targeted plan** (`plan_s318_d1.txt`): `module.irpt_status.aws_lambda_function.this` is updated in place, 0 to add, 1 to
change, 0 to destroy. Only `s3_object_version` `In5BnMbP..` -> `jVkDK9v6..` and `source_code_hash` `hC6Pramt..` -> `XPta1UMJ..`
change.

## 2. Writers and readers

- **Writer of "this XLSX template input is undated": ONE**, `_undated_template_xlsx`.
- **Its one reader** is `RetainedProspectDates.input()` (`prospect_dates.py:296`), read only by `owned_status.py:46`: the
  status route's date basis for a prospect analysis.
- **Both branches, from the rule itself:**
  - Only the pinned boilerplate outside A/B: proved undated. The analysis reads READY with `date_basis` UNDATED_INPUT,
    or one business date when every section is dated (`derive`, unchanged).
  - Any other valued cell outside A/B: unavailable, as today.

## 3. Blast radius

| input | after |
|---|---|
| the YCharts holdings template (Y-4, Y-5 and any client's copy with the same boilerplate) | READY with its date basis (was Unavailable) |
| a plain two-column XLSX | unchanged (proved) |
| an XLSX with a third column, a date anywhere outside A/B, a second sheet, a formula, or changed boilerplate text | unchanged (unavailable) |
| CSV lanes, dated sections, every other route of irpt-status | unchanged (`prospect_dates.py` is the only code change) |

## 4. Proofs

- `ops/tests/test_prospect_dates.py`: 65 passed. The new tests cover:
  - boilerplate only: proved;
  - a styled empty cell: proved;
  - boilerplate plus one valued cell: refused;
  - changed text: refused, with the named line;
  - a moved cell: refused;
  - a changed pin set: refused, loud;
  - the served pins match their set hash.
- **Offline on the real files** (read in memory; no client text or figure printed): Y-5's and Y-4's frozen documents, with
  their uploaded bytes (sha256 equal to `template.content_sha256`), prove undated. **Negative control:** the same Y-5 file
  on the base reads False.

## 5. Rollback, per key

Re-promote S3 version `In5BnMbPSWafGWf16g4CasBPJRhM.Ykl` (`hC6Pramt..`, live now) with one targeted safe-apply. Read back
CodeSha256 `hC6Pramt..`.

## 6. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read, STOP on any difference:** irpt-status CodeSha256 is `hC6Pramt..`.
3. **D1:** a fresh targeted plan (1 to change, code only); ONE `HALT_ACK=1 safe-apply`; CodeSha256 read back `XPta1UMJ..`.
4. **V1:** the status route read for REQ-a618aa83 (Y-5) as its owner, or `2.0.0_SA_COO~D`'s page row. It reads READY with
   its date basis, not "Unavailable". Then the recorder (`record-terraform-deploy.sh --function irpt-status`) runs, and the
   ledger and S318 close.
