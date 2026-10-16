# IRPT_ANLREQ -- decomposition, round 61, workstream ~T (issuer 2.0.0_SA_COO~T2)

**Input:** `1.0.0_SA_CTO~DELL2` msg 9840: the FWD-5 live cross-firm packet is RE-SIGNED on blob `57052520eb` (section RE-SIGN 2 @e1062579f2) with the positive control of the laptop CTO's ruling XA-20261016T191116Z-4c60 (YES) and the CTO's condition on port 5174. V2's combined ticket-service release is live (msg 9734); the mint (AR-tz-69) and the driver control mode (AR-tz-70) are merged.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-71` | FWD-5 | the live exercise: two principals minted, the control run and the firm-B run against the one synthetic ticket of 49financial, both principals removed, two reports and the proof instance | two `opal-users-v2` rows (minted and removed) and the applier's deliverables | WORLD (a live write of two synthetic users rows; GET-only requests; no ticket write) |

## Edges and chains

- One chain (M = 1); follows AR-tz-69 and AR-tz-70 (merged) and the signed pair. The run is graded by the issuer's checks (`R56_CHECKS/r56_checks.py`): `fence`, `absent`, `report`.

fanout: 1 of 1 chains, cap 4, reason: one applier act, one cell
