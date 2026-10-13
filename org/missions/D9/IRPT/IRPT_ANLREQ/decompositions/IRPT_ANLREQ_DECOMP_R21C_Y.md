# IRPT_ANLREQ -- decomposition, round 21 CI SCRIPT SECOND LIVE ARM, workstream YR round 17 (issuer 2.0.0_SA_COO~Y2)

**Input:** `AR-y-229` is drained (@25e92d4daa; script blob `eba6dc3da9`): the two head-object reads take stdout alone as the value. Its proof is offline. The first live arm (`TO-SCRATCH-R21`, applier `0.7.0_AE_CloudOps~AQ2`, msg 7019) failed on the stderr merge this cell removes, so the fix is proved on the real CLI and shim only by a second real run to a scratch key.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-231` | the real upload of the fixed `build-and-upload.sh` to a scratch key from a temp source-map copy in a worktree made as in the first run (so the shim WARN reproduces), read back by size and sha256; the exit code and the verify line | one new S3 object version under `investor-reporting/_ar222_scratch/`, one ledger entry | WORLD |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one live arm on one scratch prefix.
