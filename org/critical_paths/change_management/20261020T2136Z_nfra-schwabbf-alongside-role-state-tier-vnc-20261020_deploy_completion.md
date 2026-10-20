# Deploy Completion Record
**Date opened:** 2026-10-20T21:36:34.021515+00:00
**Status:** OPEN
**Deploy:** NFRA_SCHWABBF Alongside box (TO-AL-r3 at pin a51bd5cad5f): 1 add (secret schwab/alongside/vnc-credentials, metadata only) and 1 in-place change (aws_iam_role_policy.alongside_inline), 0 destroyed; four S3 code uploads; refresh of the box's code copies. Replaces nfra-schwabbf-alongside-role-state-tier-20261020, which was closed unapplied.
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply of the saved plan in infra/aws/terraform/alongside-schwab-ec2 via safe-apply (1 add, 1 change, 0 destroy) | apply summary line + 0-diff plan exit 0 + get-role-policy and describe-secret after |  | OPEN |
| L2 | s3-prefix | opal-data-assets code/alongside-schwab-si2 four files | local sha256 printed, head-object sizes |  | OPEN |
| L3 | ec2-baked-asset | sdd-daily-pull.ps1 sdd-entitlements.ps1 bootstrap.ps1 refreshed on i-0825aa0ed88342d67 | on-box Get-FileHash equals local sha256 for each |  | OPEN |

## Log

- 20261020T213634Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
