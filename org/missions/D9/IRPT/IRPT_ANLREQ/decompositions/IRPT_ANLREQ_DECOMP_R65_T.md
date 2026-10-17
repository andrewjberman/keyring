# IRPT_ANLREQ -- decomposition, round 65, workstream ~T (issuer 2.0.0_SA_COO~T2)

**Input:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v26 (FWD-5 FAIL, unproven, no leak found) and `1.0.0_SA_CTO~DELL2` msgs 10010 and 10061: the THIRD sitting DRIVES (a) the packaged ticket's files against firm B with the control served each file, (b) the five report-side read routes on the same request and job, (c) one call with no selected_tenant; the CTO re-signed the pair on packet blob `6bf8cd3887` (RE-SIGN 4 @de7f72d8c9) and will not call FWD-5 PASS himself (the grade is the CVO's at L9). The driver was extended for this (AR-tz-74, merged fa0a9a6889).

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-75` | FWD-5 | the third live exercise: two principals minted; for the PACKAGED and the SYNTHETIC target the control run and the firm-B run (13 GET calls each); both principals removed; four reports in `irpt_anlreq_fwd5_s3/` and the proof instance | two `opal-users-v2` rows (minted and removed) and the applier's deliverables | WORLD (a live write of two synthetic users rows; GET-only requests; no ticket write) |

## Edges and chains

- One chain (M = 1); follows AR-tz-69, -70, -72 and -74 (merged), the first two sittings and the re-signed pair. The run is graded by the issuer's checks (`R56_CHECKS/r56_checks.py`): `fence`, `absent`, `report` (and `control`); the FWD-5 grade itself is the CVO's.

fanout: 1 of 1 chains, cap 4, reason: one applier act, one cell
