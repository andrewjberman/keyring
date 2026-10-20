# Deploy Completion Record
**Date opened:** 2026-10-20T21:36:34.021515+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T223213Z
**Deploy:** NFRA_SCHWABBF Alongside box (TO-AL-r3 at pin a51bd5cad5f): 1 add (secret schwab/alongside/vnc-credentials, metadata only) and 1 in-place change (aws_iam_role_policy.alongside_inline), 0 destroyed; four S3 code uploads; refresh of the box's code copies. Replaces nfra-schwabbf-alongside-role-state-tier-20261020, which was closed unapplied.
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply of the saved plan in infra/aws/terraform/alongside-schwab-ec2 via safe-apply (1 add, 1 change, 0 destroy) | apply summary line + 0-diff plan exit 0 + get-role-policy and describe-secret after | Apply complete! Resources: 1 added, 1 changed, 0 destroyed. post-apply plan -detailed-exitcode 0; live policy read back: no OpsWrite/MetaPullsWrite, StateTierWrite 8 resources PutObject, AlongsideBoxSecretsWrite 2 ARNs; vnc-credentials exists with no version (r3/after.txt) | CLOSED 20261020T214356Z |
| L2 | s3-prefix | opal-data-assets code/alongside-schwab-si2 four files | local sha256 printed, head-object sizes | 4 files uploaded to s3://opal-data-assets/code/alongside-schwab-si2/ from pin a51bd5cad5f; sha256 printed; head-object sizes 8994/408/9860/51664 equal local (r3/upload.txt) | CLOSED 20261020T223212Z |
| L3 | ec2-baked-asset | sdd-daily-pull.ps1 sdd-entitlements.ps1 bootstrap.ps1 refreshed on i-0825aa0ed88342d67 | on-box Get-FileHash equals local sha256 for each | box copies refreshed over SSM; on-box Get-FileHash equals local for sdd-daily-pull.ps1 648e93fa..., sdd-entitlements.ps1 a317f016..., bootstrap.ps1 0afdf5be...; keep-console.ps1 890e4dd0... equal (r3/hash_compare.txt). bootstrap, entitlement script and puller NOT run | CLOSED 20261020T223212Z |

## Log

- 20261020T213634Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261020T214356Z LEG L1 closed: Apply complete! Resources: 1 added, 1 changed, 0 destroyed. post-apply plan -detailed-exitcode 0; live policy read back:
- 20261020T223212Z LEG L2 closed: 4 files uploaded to s3://opal-data-assets/code/alongside-schwab-si2/ from pin a51bd5cad5f; sha256 printed; head-object s
- 20261020T223212Z LEG L3 closed: box copies refreshed over SSM; on-box Get-FileHash equals local for sdd-daily-pull.ps1 648e93fa..., sdd-entitlements.ps1
- 20261020T223213Z CLOSED -- all 3 legs proven
