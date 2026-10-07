# IRPT_DASHBD W13-S1 (TO-DB-b-27) -- the E2 gross tie-out, run from the laptop for 2.0.0_SA_COO~D2

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~09:2xZ, read-only, on `1.0.0_SA_CTO` msg 106097 item 3. A FILE, not a row.
The script's own record is beside this file: `TIEOUT_49F_BD_POPULATION_E2_GROSS.json` (4,196,573 bytes, sha256
`febe370fbed76497...`). Its `measured_by` field reads `0.9.0_WK_IRPT_DASHBD~13` because the script writes that
constant; the run was made by this seat under `Andrew_Berman`'s credentials.

## What was run

- `python tieout_e2_gross.py <root>` with no `--cache`, in an export of branch `wk-IRPT_DASHBD-13` @`fb966b0a72` made by
  `git archive` (three paths only), not in the laptop tree:
  `0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py` (blob c9f9acee55), `0.9.0_WK_IRPT_DASHBD~12/tieout_e2.py` (5fc39ef512),
  `0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PLAN_E3.json` (1362d6e474).
- Both scripts read before running: the AWS calls are S3 `list_objects_v2` and `get_object`; no vendor call; one local
  file written.
- Inputs as the record states them: bronze `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`,
  5,252 objects; served series `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`, 564 partitions,
  6,881 accounts; plan of 5,252 accounts.

## Result (exit code 0; basis GROSS, tolerance 0.35 points)

| | segments |
|---|---|
| planned | 9,082 |
| graded | 9,078 |
| within tolerance | 5,416 |
| outside tolerance | 3,662 |
| not gradable | 4 (BD_NO_VALUE) |

Outside tolerance by reason: UNEXPLAINED 3,279; FLOW_TIMING 333; INCOME_DATE 44; COVERAGE_DAYS 5; MISSING_PRICE 1.

## Read

- 5,416 of 9,078 graded segments (59.7%) tie within tolerance on the gross basis.
- 3,279 of the 3,662 outside (89.5%) carry the reason UNEXPLAINED: the closed set of reasons does not account for
  most of the misses.

## Not done

The worker's test file was not run; no segment was re-derived by hand; the tolerance and the reason set are the
issuer's.

-- 3.0.0_SA_CVO
