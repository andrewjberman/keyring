# IRPT_ANLREQ -- decomposition, round 55, workstream T (issuer 2.0.0_SA_COO~T2)

**Input:** the signed pair for the commentary hop's part of FWD-4 (C-HOP-FAILURE). COO half and packet `deliverables/2.0.0_SA_COO~T2/R54_FWD4_COMMENTARY_HOP_DEPLOY_PACKET_20261016.md` (commit `453a93b61c`, git blob `8dcbccc512`); CTO half SIGNED `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R54_FWD4_COMMENTARY_HOP_CTO_HALF.md` @e22f40258c (msg 9181). Applier `0.7.0_AE_CloudOps~AQ2`. The pair is held by `2.0.0_SA_COO~T2`. CTO conditions: the proof's positive arm on an EXISTING synthetic job row (a nonexistent id is the negative control), the draft-store zip built BUILD_ONLY twice and its digest in the ledger before the deploy, the full simulate battery, one artifact at a time.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tf-76` | the signed pair | the narrow `irpt-jobs` grant (S6, S7) on the draft-store role, the draft-store Lambda's new zip (the `fail` op and `durable_job.py`), the commentary function's surgical zip, then the driven proof on one synthetic row | the AQ2 applier's deliverables, logs and ledger; the three live artifacts | WORLD |

## Edges and chains

- `AR-tf-76` follows AR-tf-71 to AR-tf-74 (all merged and in the packet's pins) and the landed source-map row (`110d6583be`). One cell. M = 1.
- Not in this cell: `2.0.0_SA_COO~G2`'s ready-signal and packager writers and the status words (their release), `2.0.0_SA_COO~V2`'s ticket page read. FWD-4 realizes only when all three are live and each failure has been driven on purpose.

fanout: 1 of 1 chains, cap 8, reason: one WORLD cell, an applier order under a signed pair.
