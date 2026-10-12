# Deploy Completion Record
**Date opened:** 2026-10-12T22:01:15.946839+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261012T220804Z
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
- 20261012T220804Z CLOSED -- REFUSED BY GATE before apply, world untouched: NOT APPLIED, stopped by this seat before the upload (row IRPT_BCKEND-D2-S113): 0 of 9 kept refs reads through the deployed function (8 PathARetiredForFirm, 1 VendorEgressRefused; 10 invokes, 0 persisted). Nothing-created reads 2026-10-12T22:07:17Z: S3 versions of investor-reporting/irpt-performance-adapter.zip 64 listed, latest F.G7ZDSN unchanged (the same list read 64 and F.G7ZDSN at the resume p
