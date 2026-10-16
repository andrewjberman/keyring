# IRPT_ANLREQ -- decomposition, round 51, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the round-50 record (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED.md`, merged a884cf8147): 40 OPAL_GLOBAL equality sites in 21 files, 10 ADMITS of which 8 are not rows of `2.0.0_SA_COO~V2`'s register (asked of V2 this tick). Step 2 of disarming ARMED row IRPT_ANLREQ-D2-W224-S1: the gate covers the whole denominator.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-66` | FWD-5 | a completeness gate (green today) and a strict-xfail register-coverage gate over every OPAL_GLOBAL equality site under infra/aws/lambda | `test_cross_firm_global_sites_widened.py` | WORLD (path floor; tests only) |

## Edges and chains

- One chain (M = 1); no dependency. The register rows are V2's; the xfail turns into a failure the day they exist, so the marker is removed then.

fanout: 1 of 1 chains, cap 4, reason: one gate cell
