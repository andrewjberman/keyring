# Deploy Completion Record
**Date opened:** 2026-09-28T23:14:01.300644+00:00
**Status:** OPEN
**Deploy:** Portal total-return boundaries and trailing-window consistency
**Authored by:** 4.0.0_SA_CRO~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| SOURCE | verify | Local source commit and deterministic artifacts | commit and artifact hashes; no push authorized |  | OPEN |
| OUTPUT | verify | Positioning, aggregate, ETF returns S3 outputs | version IDs and independent calculation comparison |  | OPEN |
| CACHE | verify | Portal CloudFront cache | completed scoped invalidation |  | OPEN |
| PARITY | verify | Post-deploy Terraform and live source | zero-diff scoped plan and downloaded code parity |  | OPEN |
| yang-generate-positioning | tf-lambda | module.generate_positioning.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| yang-generate-etf-returns | tf-lambda | module.generate_etf_returns.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260928T231401Z OPENED by 4.0.0_SA_CRO~I with 6 leg(s)
