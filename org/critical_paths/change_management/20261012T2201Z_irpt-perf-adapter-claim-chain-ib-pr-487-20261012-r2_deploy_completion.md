# Deploy Completion Record
**Date opened:** 2026-10-12T22:01:15.946839+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter (a Lambda; no ECS task family pulls the artifact; 22 worktrees read, none open names it): holdings_gold.py re-pin 05219b8444 (3381c42f13), CodeSha256 kMB8xCI9 -> abep4h7R; rollback S3 version F.G7ZDSNMeGR4mwkm7hElyoh1tLuNpGf (content-sha256 kMB8xCI9, named before upload, 64 versions listed); TO-IB-pr-487 AMENDMENT 1 @a4646f50ea, kept selections read before and after
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261012T220115Z OPENED by 0.7.0_AE_CloudOps~IB2 with 1 leg(s)
