# Deploy Completion Record
**Date opened:** 2026-09-20T15:50:08.960337+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T155110Z
**Deploy:** IRPT_BCKEND IB-rtg-3: K-CODE build -- irpt-performance-adapter rebuilt with the route_for id-space reconciliation
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | new VersionId latest + content-sha256 == built sha256 + read-back sha256(b64) == built + zip members 23/23 == committed blobs (1 differs: tenants.py, == worktree HEAD); prior version kept; function CodeSha256 unchanged (not applied) | BUILT from HEAD eee9094d47: irpt-performance-adapter.zip -> version M0E32HJhwg54I6jcU4g2e58Ktthey_51 (latest, 2026-09-20T15:27:03Z, 171542 bytes), content-sha256 == built W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=, independently re-downloaded and re-hashed equal; zip members 23 of 23, exactly 1 differs (tenants.py, new sha256 dbefe40e3c0d1f835f45783e5175f9816d8dc6654ab3e4b4e31c25fb7066a647 == worktree HEAD tenants.py); prior version 38i7y_iXZqvWIzUNetKnBxXxs9dAuOGF kept (== prior live CodeSha256 IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw=, confirmed via head-object on that version); function CodeSha256 unchanged (get-function-configuration read live, no apply run this pass) | CLOSED 20260920T155044Z |

## Log

- 20260920T155008Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 1 leg(s)
- 20260920T155044Z LEG L1 closed: BUILT from HEAD eee9094d47: irpt-performance-adapter.zip -> version M0E32HJhwg54I6jcU4g2e58Ktthey_51 (latest, 2026-09-20
- 20260920T155110Z CLOSED -- all 1 legs proven
