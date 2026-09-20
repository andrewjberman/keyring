# Deploy Completion Record
**Date opened:** 2026-09-20T20:03:00.150605+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtg-2 -- deploy irpt-status, ops root, source_code_hash O3TyGqfqjiwZP9OSXmryonnAst+SbYMLzyuSGphOyCE= -> B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0= (packet blob 26360553eb7a66af4ea7c68d93f14e206e03ef60, both never-widen halves at HEAD)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/ops safe-apply -- module.irpt_status.aws_lambda_function.this update only | apply output + resource list |  | OPEN |
| L2 | verify | post-apply CodeSha256 == B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0= | get-function-configuration CodeSha256 read |  | OPEN |
| L3 | verify | post-apply re-plan on ops root reads 0 changes | terraform plan output |  | OPEN |
| L4 | verify | arm (e) live proof under irpt-status-role -- validated StatusEnvelope or NOT_FOUND, never UNSUPPORTED_OPERATION | battery output |  | OPEN |

## Log

- 20260920T200300Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
