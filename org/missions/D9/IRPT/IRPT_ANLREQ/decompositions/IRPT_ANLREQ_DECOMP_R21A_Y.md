# IRPT_ANLREQ -- decomposition, round 21 APPLIER ACTS, workstream YR round 13 (issuer 2.0.0_SA_COO~Y2)

**Input:** two enrichment items of the CTO round-21 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md`, section 3 items 2 and 3) whose live arms are an applier's, not a worker's: (a) the ci script's real upload to a scratch key (fix drained @9ffca59db9, proved offline only; the reported failure did not reproduce in the worker's shell), and (b) the driven status-rule exercise under the signed pair (COO half blob `d1d4296341` @4f8e80f124, CTO half @decdd94c48 choosing (A), executor `0.7.0_AE_CloudOps~AQ2`). Both go to the one Dell applier lane of this project (a Dell-placed project sends no CloudOps order to a laptop seat, Andrew-direct, msg 6938).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-224` | the driven exercise of the status rule on `irpt-directory-search`: two refusal arms and the read-only admitted arm, class lines counted per sub-window, rows removed and read ABSENT by GSI and ConsistentRead | two `opal-users-v2` items for one sitting (deleted in it), three requests, one NEVER-2 ledger entry | WORLD |
| `AR-y-225` | the real upload of the fixed `build-and-upload.sh` to a scratch key from a temp source-map copy, read back by size and sha256 | one new S3 object version under `investor-reporting/_ar222_scratch/`, one ledger entry | WORLD |

## Edges and chains

- None between the cells: they share no key, no function and no tool. M = 2 chains; the lane runs them in either order (AR-y-225 first is the shorter).

fanout: 2 of 2 chains, cap 8, reason: two independent live arms, one applier lane; the lane holds one project.
