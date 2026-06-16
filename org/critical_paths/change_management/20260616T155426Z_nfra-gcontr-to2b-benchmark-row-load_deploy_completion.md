# Deploy-completion ledger -- NFRA_GCONTR.TO-2b benchmark contract row load (in-VPC)

**class:** deploy_completion
**status:** CLOSED COMPLETE
**opened:** 20260616T155426Z
**closed:** 20260616T1608Z (benchmark row LIVE + ratified, BOTH axes verified; period_defs-wipe bug found in L5 + root-fixed + corrected in-session)
**owner:** 0.7.0_AE_CloudOps
**project / TO:** NFRA_GCONTR / TO-2b (--load-contracts row-writer; COO-GO'd 154801Z)
**authorization:** COO GO TO-2b 154801Z + Andrew SEV1 sign-off on benchmark-model-portfolios (COO 155144Z); CVO row f3334f112
**code commit:** 11efd80ef (loader)

## What
Rebuild the derive image with --load-contracts, then load the ANDREW-RATIFIED
benchmark-model-portfolios SEV1 contract row (CVO YAML) into globgrph.graph_contracts
in-VPC: append-only (no other rows touched), stamp ratified_at = the authoring Nessie
commit hash. Then run the BMKAUD T1 joint-acceptance replay end-to-end.

## Legs -- ALL LANDED
- [x] L1: image rebuild (CodeBuild 5fdd33bf nope -> the loader builds: 2d457728 [load], 90cceb00 [fix]) -> ECR :latest SUCCEEDED
- [x] L2: CVO YAML -> s3://opal-313476888478-globgrph/contracts/graph_contracts.yaml
- [x] L3: in-VPC --dry-run (task b248af89) -> SAFETY GATE fired: PENDING benchmark row SKIPPED (needs --stamp-ratified); 0 writes
- [x] L4: in-VPC real load --stamp-ratified (task 26c9ce57) exit 0 -> CONTRACTS_APPENDED, ratified_at stamped 516a4da5...
- [x] L5: VERIFY caught a BUG: period_defs landed EMPTY (restamp read-back map->list-of-tuples wiped it). Root-fixed (commit 48580c99f: single-write, ratified_at pinned pre-write, no read-back; +--overwrite; +WRITE_VERIFY). CORRECTION re-load --overwrite (task 1b49e9ab) exit 0 -> CONTRACTS_OVERWRITTEN, WRITE_VERIFY period_defs=11, ratified_at=6f21c75c..., 1 row (no dup)
- [x] L6: JOINT ACCEPTANCE -- BMKAUD T1 replay on the CORRECTED live row -> Q2 UNSANCTIONED (added_forbidden=[smartx-model-monthly-pull]); baseline=WATCH (no false-positive). BMKAUD-catch DEMONSTRATED end-to-end.

## Closure evidence (two-axis accepted)
- POLICY/STRUCTURE limb: LIVE -- canonical_writer=yang-pipeline-lambda-role, forbidden_writers(4), ratified_by=[Andrew], ratified_at=6f21c75ca78040ee... (real Nessie hash). Q2 catch fires.
- VALUE limb: period_defs = 11 keys StaticTable-verified incl 1M="trailing-1-calendar-month -> as-of" (the BMKAUD assertion) + _rfr_tenor/_return_basis. Actual loaded keys sent to CVO for byte-verify.
- code: loader 11efd80ef + fix 48580c99f; image via CodeBuild 90cceb00. SERVED/StaticTable-verified, not rc=0.

## Close criteria
benchmark row LIVE + ratified (ratified_at = real hash) on Nessie main, StaticTable-verified;
BMKAUD-catch demonstrated. Then status -> CLOSED COMPLETE + RAVC2 COO+CTO.

## Rollback
Append-only on a 0-row table; if the row mis-loads, the contract_id can be overwritten/retired
via a Nessie commit (active=false) -- recoverable, no data path touched.
