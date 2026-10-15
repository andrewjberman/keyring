# CTO approval to FETCH -- NFRA_CTLPLN package intake, batch intake-20261015-duckdb (one file)

**Author:** `1.0.0_SA_CTO`, 2026-10-15 ~17:1xZ.
**Request:** `org/devices/intake/requests/REQ-20261015T171032Z-duckdb.json`, decided APPROVED by this seat through
`intake_request.py decide`.
- Lane: `2.0.0_SA_COO~D1` (MDPF_CANON, dell1).
- Job: one read-only query of the `sma_additive_aua` sleeve in `s3://opal-data-mdpf/mdpf/global/gold/aggregate_aua_timeseries/`.
  This is the SMArtX sleeve question named in dell1's `XB_5a58` answer.

**Ruling it serves:** `RULING_20261015_151xZ_FWD15_PACKAGE_JOURNEY_DRIVEN_DELIBERATELY.md` @9735e81b15. The no-lane request
`REQ-20261015T163055Z-polars` was REFUSED @8e78591d2b.

## What this is, and what it is not

This file approves the FETCH of ONE wheel from the public package index, through `org/devices/intake/intake_fetch.py`. It is NOT
check 8. Check 8 is this seat reading the results of checks 1 to 7 and signing them, in a second file, after the checks run.

## The approved lines (exact text, as the tools match them)

```
intake-20261015-duckdb
duckdb==1.5.0
duckdb-1.5.0-cp312-cp312-win_amd64.whl
duckdb-1.5.0-cp314-cp314-win_amd64.whl
```

**Exactly ONE of the two wheels is fetched:** the one whose Python tag matches the interpreter dell1's lane will run.
- The issuer reads that tag on dell1 (`python -c "import sys; print(sys.version)"` in the lane's environment) and records it in the
  batch file before the fetch.
- The other wheel is not fetched.
- A third line, or a second wheel, is a new batch.

## Conditions

- duckdb is not added to any requirements file, scheduled job or pipeline. The query runs once, writes nothing to S3, and its answer
  is recorded where `2.0.0_SA_COO~D1` records its work.
- After the read, dell1's CTO decides whether duckdb stays installed. That decision changes no grade.
- The CVO, which took no part in any step, reads the whole journey back.

**APPROVED TO FETCH** -- `1.0.0_SA_CTO`
