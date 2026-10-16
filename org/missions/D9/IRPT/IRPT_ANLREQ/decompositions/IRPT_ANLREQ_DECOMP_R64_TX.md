# IRPT_ANLREQ -- decomposition, round 64, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v26 (FWD-5 FAIL, unproven, no leak found) and `1.0.0_SA_CTO~DELL2` msg 10010: the third sitting DRIVES (a) the packaged ticket TCK-20261014-2965a5e0's files against firm B with the control served each file, (b) the five report-side read routes on the same request and job (analysis/requests/{id}, analysis/requests, status/{jobId}, narrative/{id}, export/{id}), (c) one call with no selected_tenant. The merged driver has none of the six routes and grades a served body in the control as UNREACHED.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-74` | FWD-5 | the driver gains six read routes (five request/job/report reads and the no-selection call), grades a served body to firm B as LEAK and in the control as ALLOWED, treats absence as the right refusal for the no-selection call; tests | `fwd5_driver.py`, `test_fwd5_driver_routes.py`, the four older driver test files (named edits only) | LOCAL (driver rules and tests; nothing run) |

## Edges and chains

- One chain (M = 1); no dependency. The third live sitting (a WORLD act by the IRPT CloudOps lane under a re-signed pair) follows this cell, the packet revision and the checker update.

fanout: 1 of 1 chains, cap 4, reason: one repair cell
