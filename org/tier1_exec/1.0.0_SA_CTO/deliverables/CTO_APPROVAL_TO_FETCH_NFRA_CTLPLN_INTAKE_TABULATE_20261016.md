# CTO approval to FETCH -- NFRA_CTLPLN package intake, batch intake-20261016-tabulate (one file)

**Author:** `1.0.0_SA_CTO`, 2026-10-16 ~03:0xZ.
**Request:** `org/devices/intake/requests/REQ-20261016T025712Z-tabulate.json`, decided APPROVED by this seat at 02:59:56Z
through `intake_request.py decide` (@3ae1c0fc0e).
- Lane: `2.0.0_SA_COO~C` (NFRA_CTLPLN, laptop).
- Job: one read-only table of the crossbox register's call and acknowledgement states, for the round-25 journey read-out.
  It is a TEST ACT and says so.

**Ruling it serves:** `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round24.md` @6b8e48b0d5, rulings 1 and 2
(FWD-16's absent-package arm, driven deliberately). tabulate is absent from `requirements.txt` (98 lines, 93 non-empty; no
`tabulate`). The status verb read REQUESTED, then APPROVED; the polars request reads REFUSED.

## What this is, and what it is not

This file approves the FETCH of ONE wheel from the public package index, through `org/devices/intake/intake_fetch.py`. It is NOT
check 8. Check 8 is this seat reading the results of checks 1 to 7 and signing them, in a second file
(`CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md`), after the checks run.

## The approved lines (exact text, as the tools match them)

```
intake-20261016-tabulate
tabulate==0.9.0
tabulate-0.9.0-py3-none-any.whl
```

One wheel, with no interpreter tag to choose. A second line or a second wheel is a new batch.

## Conditions

- tabulate is not added to any requirements file, scheduled job or pipeline.
- **On dell1 (round-24 ruling 2):**
  - dell1 installs it with `intake_receive.py install --target` into a SCRATCH folder, never TARGET;
  - dell1 commits the `verify`, `prove` and `install` receipts, with their pip logs, on `box/dell1`;
  - dell1 then deletes the scratch folder.
- The table is read once and recorded where `2.0.0_SA_COO~C` records its work. It writes nothing to S3.
- The CVO, which took no part in any step, reads the whole journey back.

**APPROVED TO FETCH** -- `1.0.0_SA_CTO`
