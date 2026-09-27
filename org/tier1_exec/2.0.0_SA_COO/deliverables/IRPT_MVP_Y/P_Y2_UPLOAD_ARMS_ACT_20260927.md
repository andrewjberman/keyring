# The Y2 upload arms still unproved live: XLSX template and Target Weight (acts for a future Analysis window)

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~21:4xZ. Y2 is live only for the Dollars CSV (window 15). The two remaining arms each
reuse window 15's exact chain: ONE login, P deletes the password, ONE K4, then ONE K5 Overview, with no retry. Each is
run by `live_walk/live_chain.py` with three new environment switches. Unset, it is window 15's Dollars CSV exactly (the
dry-run body hashes to `bb079cbf..`).

| Arm | Environment | File (this directory) | sha256 | Expected |
|---|---|---|---|---|
| XLSX template | `WALK_UPLOAD_FILE=../aapl-vnq-12.03.xlsx WALK_FILE_TYPE=xlsx` | `aapl-vnq-12.03.xlsx` (one sheet, `holdings_template`, Ticker/Dollars, AAPL 10.01, VNQ 2.02) | `f20f0c08..` | NORMALIZED 12.03, family ORIGINAL_HOLDINGS; Overview READY; status READY once irpt-status carries `P_TEMPLATE_STATUS_DATES_20260927.patch` |
| Target Weight | `WALK_UPLOAD_FILE=../aapl-vnq-target-weight.csv WALK_REFERENCE_NOTIONAL=1000` | `aapl-vnq-target-weight.csv` (Ticker/Target Weight, AAPL 0.6, VNQ 0.4) | `6227594d..` | NORMALIZED 1000.00, valuation basis REFERENCE_NOTIONAL (the report must not read it as actual AUM); Overview READY |

A file-type mismatch (`WALK_FILE_TYPE` against the file's extension) refuses before any POST.

## Offline checks on these exact files

- XLSX: the real intake `template_reader` reads sheet `holdings_template`, basis USD, **0 findings**, rows AAPL "10.01"
  and VNQ "2.02". Y's XLSX status proof (`prospect_dates._undated_template_xlsx`, @49f3393cb0) holds on it.
- Target Weight: the bytes equal the case `test_deferred_resolution.py::test_target_weights_carry_the_reference_notional_through_the_resident`
  proves (1 passed), a total of 1000 with basis REFERENCE_NOTIONAL. The reader reports TARGET_WEIGHT with 0 findings.
- `live_chain.py --dry` prints each K4 body (file scrubbed to its length), plus the K5 body validation, with no
  network call.

## Write set per arm (for the packet's halves)

The same as window 15's:
- the vendor: 1 holdings upload, 1 portfolio create, 1 report create, status and saved reads within window 15's
  bounds;
- Opal: one UPLOAD#/NORMALIZATION#/INPUT#, one analysis request, one job row, one REPORT#, and their retained
  artifacts.

The only difference is the input file and, for Target Weight, the `reference_notional` option.
