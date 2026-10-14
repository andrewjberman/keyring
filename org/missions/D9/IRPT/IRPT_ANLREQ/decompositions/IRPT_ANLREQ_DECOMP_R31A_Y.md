# IRPT_ANLREQ -- decomposition, round 31A: THE RESIDENT APPLY SCRIPTS OF RELEASE 28, workstream YV round 31 (issuer 2.0.0_SA_COO~Y2)

**Input:** the release-28 pair is signed by both halves (COO blob `e9bb20d7fe`, CTO half @d3adae2fc8, CTO msg 7415: "Cut the applier orders"). The three Lambda legs (L2, L1, L3) need no new scripts: their apply orders rebuild from the recorded inputs, as the release-20 order did. The resident leg (L4) is run on a production host through Systems Manager by `0.7.0_AE_CloudOps~YC2`, and release 19 ran three scripts for it (`pre_read_r19.sh`, `install_r19.sh`, `rollback_r19.sh`, under `deliverables/2.0.0_SA_COO~Y2/release19/`). Release 28 has the tarball and the host script (`AR-y-300`) but not the wrappers or the separately staged package sums file. They are written against the old ones line by line.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-301` | `r31/pre_read_r28.sh`, `r31/install_r28.sh`, `r31/rollback_r28.sh`, the staged `irpt-resident-0485393f3a-r28.package.SHA256SUMS` (outside the repository), and `r31/RESIDENT_APPLY_SCRIPTS.json`; `bash -n` on each, a dry run of the sha256 gates with a one-byte change that must refuse; nothing is run on the host | the worker's record folder and the surprise channel file | LOCAL |

## Edges and chains

- One chain. The scripts' sha256 values go into the resident apply order `TO-APPLY-R28b` (issued to `~YC2` after this cell drains); the Lambda apply orders (`TO-APPLY-R28a`, `-R28c`) do not wait on it.

fanout: 1 of 1 chains, cap 8, reason: one author for three scripts that share their constants; splitting would let the constants drift.
