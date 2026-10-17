# TCKT_EARLYWARN -- the one-cell decomposition (fast-path)

The project is FAST-PATH on Andrew-direct 2026-10-16 ~18:0xZ (it runs no L1-L10 and carries no PRD). The proof-of-spec checker and the pipeline
gate resolve a task order's cell references against a document that declares cell ids, and `project.json` declares none, so the issuer
declares the one cell of the deploy order here. This file is not a PRD, a battery or a round plan, and it adds no process.

| cell | what | order |
|---|---|---|
| `EWS-d-1` | the Client Ops Early Warning runtime deployed as ONE always-on container, read-only on the two Schwab silver prefixes, the cert secret only, nothing sends | `TCKT_EARLYWARN.TO-EWS-d1` |
| `EWS-d-2` | the container logs items opened per rule each pass and keeps its open-items store on ONE S3 prefix (role widened to that prefix only); the CTO's exercised read of EWS-d-1 (msg 7455) | `TCKT_EARLYWARN.TO-EWS-d2` |

Issuer: `2.0.0_SA_COO~Q1`, 2026-10-17 ~06:5xZ, on `0.7.0_AE_CloudOps~TM1`'s row TCKT_EARLYWARN-D1-S6 (msg 7399).
