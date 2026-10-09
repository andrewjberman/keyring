# Deploy Completion Record
**Date opened:** 2026-10-09T17:43:47.903363+00:00
**Status:** OPEN
**Deploy:** MDPF_STRATID round 2 + ST-w-7: Cottonwood OUTSIDE, held-out stated, unidentified list on the slice
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | data/mdpf/scripts/gold/mdpf_gold_consolidator.py | s3 sha256 == git show <merge> |  | OPEN |
| L2 | s3-prefix | data/mdpf/scripts/gold/mdpf_category_registry.py | s3 sha256 == git show <merge> |  | OPEN |
| L3 | s3-prefix | data/assets/scripts/gold/build_cottonwood_mdpf_slice.py | s3 sha256 == git show <merge> |  | OPEN |
| L4 | verify | next scheduled mdpf-scheduled-floor fire | issuer's r2_run_read.py prints R2-RUN-READ PASS |  | OPEN |
| mdpf-gold-lambda | tf-lambda | aws_lambda_function.mdpf_gold | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T174347Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 5 leg(s)
