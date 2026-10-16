# IRPT_ANLREQ -- decomposition, round 50, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the round-47 worker's ARMED row IRPT_ANLREQ-D2-W224-S1 (disarm owner this issuer): the global-admissions gate scans 2 of 21 OPAL_GLOBAL equality sites in 12 files. Step 1 classifies every site (this round); the gate is widened from the record in a later round, and any admission not in the register is a finding for `2.0.0_SA_COO~V2`. Round 49 (AR-tf-74, the FWD-4 wiring cell) is a separate issuance and is not touched.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-65` | FWD-5 | a cited-line record classifying every OPAL_GLOBAL equality site under infra/aws/lambda | `OPAL_GLOBAL_SITES_CLASSIFIED.md` (deliverables ~229) | LOCAL |

## Edges and chains

- One chain (M = 1); no dependency.

fanout: 1 of 1 chains, cap 4, reason: one read cell
