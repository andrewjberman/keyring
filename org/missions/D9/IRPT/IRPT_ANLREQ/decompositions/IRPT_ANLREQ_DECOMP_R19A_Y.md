# IRPT_ANLREQ -- decomposition, round 19 APPLY LEGS, round 8, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** the two-leg never-widen pair for the template reader's release, COO half blob `2140b9352c` and CTO half SIGNED @6facbbb2d3 (CTO msg 6802): resident FIRST (`0.7.0_AE_CloudOps~YC2`), then the Lambda (`0.7.0_AE_CloudOps~IB2`; `~AR2` is not registered). The window's stored-input recount (R0d) is a laptop read.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-204` | the stored-input recount at the window (R0d / S35), by the seat that holds the decrypt | the laptop applier's deliverables | WORLD (read-only) |
| `AR-y-205` | the resident root `0485393f3a-r19` installed on the host and read back (P1, D2, V1) | the resident applier's deliverables and its ledger | WORLD |
| `AR-y-206` | the Lambda `irpt-ycharts-generate` released at CodeSha256 `bNPCG2Oe...` and read back (L1 to L3), the source-map record | the Lambda applier's deliverables, its ledger, the source map | WORLD |

## Edges and chains

- `AR-y-204` -> `AR-y-205` -> `AR-y-206` (the recount precedes the first act; the Lambda starts only after the resident's V1 is green). M = 1 chain of 3.

fanout: 1 of 1 chains, cap 8, reason: three sequential apply legs under one signed pair; each has its own applier.
