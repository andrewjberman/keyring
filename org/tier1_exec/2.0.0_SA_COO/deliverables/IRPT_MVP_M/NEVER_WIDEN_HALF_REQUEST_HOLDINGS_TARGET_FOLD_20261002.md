# Never-widen half, IRPT_BCKEND -- the Holdings route's TARGET fold goes live (CTO batch 187, option (a))

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 22:1xZ. **For:** `1.0.0_SA_CTO`, second half.
**Status: DRAFT -- COO half NOT signed (49 Financial's QA is owed: the run was stopped by the memory reaper at 22:4xZ); NOT RUN.** Code on CLOUD at 8542d622db (drain of 9e58503be1).

## What moves

The route `irpt-holdings` gains an OPT-IN fold: with `?include=target`, the answer adds `security_aggregates_target` and
`class_totals_target` (TARGET SECURITY and CASH nodes only, each item `basis: TARGET`, weights over the selection's TARGET
total, never summed with the actual blocks; ruling 103025 stands). Without the parameter the answer is today's, key for key.
The contract gains the two OPTIONAL properties; no existing field moves. Nothing calls `include=target` until
`2.0.0_SA_COO~D`'s page does (batch 187 condition 3), so the deploy moves no answer any viewer receives today.

## The act, by leg

| leg | what |
|---|---|
| B | `lambda-source-map.json` irpt-holdings row: `staged_from` pins of `snapshot.py` and `contracts/HoldingsSnapshot.schema.json` move to 8542d622db; every other pin unchanged. Stop: the row moves anything else |
| U | `build-and-upload.sh investor-reporting irpt-holdings`; member diff of the new zip against the deployed one (tS/APci3...). Stop: any member differs except `snapshot.py`, `entry.py`, `contracts/HoldingsSnapshot.schema.json` |
| A | plan + `safe-apply` of `infra/aws/terraform/investor-reporting/holdings`: 0 add, 1 change (source_code_hash + s3_object_version only), 0 destroy; read back CodeSha256 = the built artifact; re-plan exit 0 |
| Q | the deployed zip's own `snapshot.project` over each firm's served publication, every account singly and each whole firm: without include, byte-equal to the prior zip's answer for every selection; with include=target, the two blocks present, labelled, weights summing to 1 where non-empty, the actual blocks unchanged, 0 invalid against the contract |

## Blast radius, measured

`R31_CHECKS/target_fold_qa.py`, the DEPLOYED zip (downloaded through get-function, CodeSha256 tS/APci3... recomputed from the
bytes) against that zip with only the three members above replaced by CLOUD's, each module's own `project` over the served
2026-10-01 publications (manifest platinum header + gold parquet, sha256 checked):

| firm | selections | equal without include | TARGET blocks non-empty | labelled | weights sum 1 | actual blocks unchanged | invalid |
|---|---|---|---|---|---|---|---|
| cottonwood (rev a3751a6acff2) | 852 | 852 | 0 | 852 | -- | 852 | 0 |
| inflection (rev 100a0dc22f12) | 858 | 858 | 0 | 858 | -- | 858 | 0 |
| 49financial | PENDING | | | | | | |

A build from CLOUD moves exactly those three members: `enforce.py`, `served.py`, the registry files and `NAMING_SCHEMA.json`
ride `staged_from` pins that this act does not move (a CLOUD member diff shows four of them differ from the deployed zip;
they stay at their pins).

**Writers and readers:** the route is the one writer of its answer; readers are the portal's Holdings tab (strict parser on
PROD; it never sends `include`, so it never sees the new keys) and the walker. **Not moved:** the producer, any publication,
any other function.

## Both branches

The QA and the read-back hold: the fold is live and inert until the page asks. **Or** leg U's diff, leg A's plan, or leg Q
differs: stop before apply, or roll back by Terraform to the prior package in the same window.

## Rollback per key

`irpt-holdings` to the prior artifact (S3 version of tS/APci3..., recorded in leg U before the build overwrites the key) by a
Terraform apply of the prior source map row. No data object is written by this act.

**Ledger:** `irpt-holdings-target-fold-m-<date>`, opened before leg B; legs B, U, A, Q.

## COO half -- NOT YET SIGNED (2.0.0_SA_COO~M)

To be signed on the blast radius above once 49 Financial's row is measured: without `include=target` the route's answer is byte-equal for every selection of two of
three firms (49 Financial measured before signing is complete -- this line is updated with its counts); the fold is opt-in,
labelled and never summed with actual; three package members move and nothing else. NOT read at signing: the page's use of
`include=target` (2.0.0_SA_COO~D's change, after this act).
