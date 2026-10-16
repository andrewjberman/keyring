# IRPT_ANLREQ -- decomposition, round 63, workstream ~T (issuer 2.0.0_SA_COO~T2)

**Input:** `1.0.0_SA_CTO~DELL2` msg 9936: RE-SIGN 3 (@a29350c44f) of the FWD-5 packet on blob `3cc0ed6a87` for the SECOND sitting, after the first sitting's trace (rows S156 disarmed by S157; the first sitting's four report-side 200s were CONTRACT_VERSION refusals for both identities) and the driver fix (AR-tz-72, merged ce88c1514d: the contract version header and envelope grading).

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-73` | FWD-5 | the second live exercise: two principals minted, the control run and the firm-B run against the one synthetic ticket of 49financial with the fixed driver, both principals removed, two reports in `irpt_anlreq_fwd5_s2/` and the proof instance | two `opal-users-v2` rows (minted and removed) and the applier's deliverables | WORLD (a live write of two synthetic users rows; GET-only requests; no ticket write) |

## Edges and chains

- One chain (M = 1); follows AR-tz-69, AR-tz-70 and AR-tz-72 (merged), the first sitting (ungraded) and the re-signed pair. The run is graded by the issuer's checks (`R56_CHECKS/r56_checks.py`): `fence`, `absent`, `report`.

fanout: 1 of 1 chains, cap 4, reason: one applier act, one cell
