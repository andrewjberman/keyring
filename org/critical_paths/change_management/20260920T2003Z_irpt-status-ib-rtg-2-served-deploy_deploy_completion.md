# Deploy Completion Record
**Date opened:** 2026-09-20T20:03:00.150605+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T205455Z
**Deploy:** IRPT_BCKEND.TO-IB-rtg-2 -- deploy irpt-status, ops root, source_code_hash O3TyGqfqjiwZP9OSXmryonnAst+SbYMLzyuSGphOyCE= -> B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0= (packet blob 26360553eb7a66af4ea7c68d93f14e206e03ef60, both never-widen halves at HEAD)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/ops safe-apply -- module.irpt_status.aws_lambda_function.this update only | apply output + resource list | Apply complete! Resources: 0 added, 1 changed, 0 destroyed -- module.irpt_status.aws_lambda_function.this Modifications complete after 6s [id=irpt-status]; function_name=irpt-status, role_arn=arn:aws:iam::313476888478:role/irpt-status-role | CLOSED 20260920T202750Z |
| L2 | verify | post-apply CodeSha256 == B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0= | get-function-configuration CodeSha256 read | aws lambda get-function-configuration --function-name irpt-status --query CodeSha256 --output text -> B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0= (matches built sha, LastModified 2026-09-20T20:24:17.000+0000) | CLOSED 20260920T202750Z |
| L3 | verify | post-apply re-plan on ops root reads 0 changes | terraform plan output | terraform plan (ops root) post-apply -> No changes. Your infrastructure matches the configuration. | CLOSED 20260920T202751Z |
| L4 | verify | arm (e) live proof under irpt-status-role -- validated StatusEnvelope or NOT_FOUND, never UNSUPPORTED_OPERATION | battery output | battery_ib_rtg_2.py R73-AC1 PASS -- 4 of 4 arms hold (packet+halves, K-CODE post-apply, precondition, live proof); token IBR73-STATUS-LOADER-SERVES-ENVELOPE; live-principal ledger irpt-status-ib-rtg-2-live-principal CLOSED 3 of 3 legs; see IB-rtg-2_R73-AC1_battery_output.txt | CLOSED 20260920T205454Z |

## Log

- 20260920T200300Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
- 20260920T202750Z LEG L1 closed: Apply complete! Resources: 0 added, 1 changed, 0 destroyed -- module.irpt_status.aws_lambda_function.this Modifications 
- 20260920T202750Z LEG L2 closed: aws lambda get-function-configuration --function-name irpt-status --query CodeSha256 --output text -> B0AmyfRKxd4uMhcfok
- 20260920T202751Z LEG L3 closed: terraform plan (ops root) post-apply -> No changes. Your infrastructure matches the configuration.
- 20260920T205454Z LEG L4 closed: battery_ib_rtg_2.py R73-AC1 PASS -- 4 of 4 arms hold (packet+halves, K-CODE post-apply, precondition, live proof); token
- 20260920T205455Z CLOSED -- all 4 legs proven
