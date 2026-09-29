# Deploy Completion Record
**Date opened:** 2026-09-29T04:12:42.209304+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-a-2: grant writer apply, branch=sub (gateway line keys=email,exp,family_name,given_name,iss,name,picture,sub). Owner key supplied via TF_VAR only, never recorded. ROLLBACK (all 7 resources new): safe-apply-gated targeted destroy in infra/aws/terraform/opal-gateway of aws_lambda_function.mcportal_grant_writer, aws_lambda_layer_version.mcportal_grant_writer_deps, aws_iam_role.mcportal_grant_writer, aws_iam_role_policy.mcportal_grant_writer_access_state, aws_dynamodb_table.mcportal_grant_changes (deletion_protection must be lifted first), aws_iam_role_policy.gw_read_mcportal_grant_changes, aws_iam_role_policy.gw_invoke_mcportal_grant_writer
**Authored by:** 0.9.0_WK_NFRA_MCPORTAL~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | layer build: PyJWT 2.13.0 cryptography 49.0.0 cffi 2.1.0 pycparser 3.0 manylinux2014 cp312 | zip sha256 + member count | layer zip sha256=a0ef01c5c9c6f443.. 180 members, wheels PyJWT-2.13.0 cryptography-49.0.0 cffi-2.1.0 pycparser-3.0 (manylinux2014_x86_64 cp312) | CLOSED 20260929T041610Z |
| L2 | verify | staged package build (build_package.py) | staged dir listing | build_package.py staged 11 files under .build/staged, lambda_function.py at root | CLOSED 20260929T041611Z |
| L3 | activation | safe-apply targeted apply of mcportal_grant_writer.tf resources (7 add, 0 change, 0 destroy) | apply complete line |  | OPEN |
| L4 | verify | live no-header invoke -> REFUSED NO-OWNER-HEADER + record in table | invoke output |  | OPEN |

## Log

- 20260929T041242Z OPENED by 0.9.0_WK_NFRA_MCPORTAL~1 with 4 leg(s)
- 20260929T041610Z LEG L1 closed: layer zip sha256=a0ef01c5c9c6f443.. 180 members, wheels PyJWT-2.13.0 cryptography-49.0.0 cffi-2.1.0 pycparser-3.0 (manyl
- 20260929T041611Z LEG L2 closed: build_package.py staged 11 files under .build/staged, lambda_function.py at root
