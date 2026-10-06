# Deploy Completion Record
**Date opened:** 2026-10-06T03:37:59.191543+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 73 AMGT-aw-7: TWO legs on opal-amgt-scoped-api -- code at 9d2b7b3d7c carrying aw-1/aw-2/aw-3/aw-5 (CHANGED 4, no ADDED), then the KEEP-PRIOR pool universe write to the NEW key universe/v1/2026-10-06.json from CLOUD at or after 1aa1d8f2df with no sec.gov call (fails closed). AMENDMENT 1: no grant leg -- aw-1 reads bloomberg/harvest/bronze/refdata/, which the role already holds (simulated allowed at signing). CTO conditions 1-6 @78ed2b6bc6, COO half @ea483704fe. Rollback for the pool is a RE-PUT of the 2026-09-16 bytes at the new key, NEVER an S3 delete, because readers take the newest dated key. The one open entry naming this function, amgt-corpus-r36-al5 (2.0.0_SA_COO~X, branch wk-oplgtw-15-r16 only), was ruled dead and non-blocking by the issuer at msg 29756 and is now measured dead across rounds 71, 72 and 73.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + open_deploys union over every live worktree + BEFORE state of the pool key + both named commits on CLOUD | CodeSha256 2lUlZomoyb2ttLBaQTg6l3ysfw2aEjZGD7mInm8J/WQ= and MemorySize 1769 unchanged; per-tree denominator printed for every live worktree with 0 unresolved; universe/v1/2026-10-06.json ABSENT with the prefix listing as the positive control; 9d2b7b3d7c and 1aa1d8f2df both ancestors of HEAD with a behaving negative control |  | OPEN |
| L1 | verify | CODE LEG build at 9d2b7b3d7c from a clean detached checkout, CONTENT-DIFF vs deployed 2lUlZomo | exactly CHANGED lib/research/api/scoped_amgt.py + lib/research/api/monthly_chatter.py + lib/research/print/render_pack.py + lib/research/harvest/publication_gold.py, ADDED none, REMOVED none; size under 262144000 B |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object |  | OPEN |
| L3 | activation | opal-amgt-scoped-api code-only safe-apply, then leadpanel_cold_warm.py --label after and the cold invokes' AMGT_PHASE log lines | full-plan show -json: exactly 1 update (the function), 0 destroy/route/gateway/IAM; memory 1769; live CodeSha256 = the new build; leadpanel after output and the AMGT_PHASE phase table captured into deliverables |  | OPEN |
| L4 | verify | the live /freshness route read, CTO condition 4, plus its warm latency on 3 calls | the pack clock carries a date for every name whose pack exists and no longer reads NEVER for 95 of 95; 3 warm /api/scoped/amgt/freshness calls timed and reported (a warm read over 2000 ms is a row, not a rollback) |  | OPEN |
| L5 | verify | POOL WRITE LEG: build_universe --as-of 2026-10-06 --write-pool to the NEW key universe/v1/2026-10-06.json, stored objects only | --dry-run first reads covered 95 of 95 with 0 regressions; no sec.gov call in the path; readback of the written object shows c52 0 regressions, the 13 prior decided form_expected values KEPT, covered names 95, and every new name carrying the absent shape with its provenance note; BEFORE state was ABSENT so this is a first mint, not an overwrite |  | OPEN |
| L6 | verify | AC1 c48/c49/c50 deployed, AC2 c52 local after the pool write, AC3 r72 c39-c45 + r71 c38 deployed | each criterion SERVED YES with exit=0; AC2 run --where local as the criterion literally states |  | OPEN |

## Log

- 20261006T033759Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
