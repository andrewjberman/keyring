# IRPT_ANLREQ -- decomposition, round 66, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v27 (FWD-5 still FAIL, unproven: the packaged leg has no served control) and `1.0.0_SA_CTO~DELL2` msg 10104: sitting 4, after FWD-1 window 5, adds (1) the request's owner-admitted identity served each packaged file in the same sitting, (2) working controls with REAL ids on request-history, narrative and the no-selection call (no stand-ins), (3) GET tickets/metrics; the write routes are outside FWD-5's DONE WHEN. The merged driver uses the request id as a stand-in for the report id and the export id, and has no metrics route.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-76` | FWD-5 | the driver takes `--report-id` and `--export-id` (a run without them leaves the two routes UNREACHED) and drives `GET /api/scoped/tickets/metrics`; tests | `fwd5_driver.py`, `test_fwd5_driver_real_ids.py`, the five older driver test files (named edits only) | LOCAL (driver inputs, one route and tests; nothing run) |

## Edges and chains

- One chain (M = 1); no dependency. The fourth sitting (a WORLD act by the IRPT CloudOps lane under a re-signed pair) follows this cell, FWD-1 window 5's packaged ticket, the owner-rule measure and the checker/packet update.

fanout: 1 of 1 chains, cap 4, reason: one repair cell
