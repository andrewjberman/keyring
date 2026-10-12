# Deploy Completion Record
**Date opened:** 2026-10-12T21:40:09.220268+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261012T214714Z
**Deploy:** irpt-performance-adapter (a Lambda; no ECS task family pulls the artifact): holdings_gold.py re-pin 05219b8444, CodeSha256 kMB8xCI9 -> abep4h7R, claim follows the excluded day status; rollback S3 version F.G7ZDSNMeGR4mwkm7hElyoh1tLuNpGf (content-sha256 kMB8xCI9, named before upload, 64 versions listed); TO-IB-pr-487, pair signed COO 21:03:15Z + CTO Branch A
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261012T214009Z OPENED by 0.7.0_AE_CloudOps~IB2 with 1 leg(s)
- 20261012T214714Z CLOSED -- REFUSED BY GATE before apply, world untouched: NOT APPLIED, stopped by this seat before the upload (row IRPT_BCKEND-D2-S112): the four direct-invoke arms need a sel_ selection record this seat can neither read (irpt-requests scan: AccessDenied kms:Decrypt) nor create under the grant. Done: rollback version F.G7ZDSNMeGR4mwkm7hElyoh1tLuNpGf named, source-map re-pin committed 3381c42f13, BUILD_ONLY digest abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0Hkdz
