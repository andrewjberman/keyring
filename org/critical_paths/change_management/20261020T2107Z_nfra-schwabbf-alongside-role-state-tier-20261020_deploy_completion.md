# Deploy Completion Record
**Date opened:** 2026-10-20T21:07:17.705690+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T213633Z
**Deploy:** NFRA_SCHWABBF Alongside box: in-place update of the role inline policy aws_iam_role_policy.alongside_inline (two master-scope statements out, StateTierWrite in), three S3 code uploads (four files), refresh of the box's code copies. No resource added or destroyed.
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply of the saved plan in infra/aws/terraform/alongside-schwab-ec2 via safe-apply (0 add, 1 change, 0 destroy) | apply summary line + 0-diff plan exit 0 + get-role-policy after | NOT APPLIED -- SUPERSEDED: order re-pinned to a51bd5cad5f (adds secret schwab/alongside/vnc-credentials), so this entry's manifest was wrong; replaced by nfra-schwabbf-alongside-role-state-tier-vnc-20261020. Nothing landed under this entry. | CLOSED 20261020T213633Z |
| L2 | s3-prefix | opal-data-assets code/alongside-schwab-si2 four files | local sha256 printed, head-object sizes | NOT APPLIED -- SUPERSEDED: order re-pinned to a51bd5cad5f (adds secret schwab/alongside/vnc-credentials), so this entry's manifest was wrong; replaced by nfra-schwabbf-alongside-role-state-tier-vnc-20261020. Nothing landed under this entry. | CLOSED 20261020T213633Z |
| L3 | ec2-baked-asset | sdd-daily-pull.ps1 sdd-entitlements.ps1 bootstrap.ps1 refreshed on i-0825aa0ed88342d67 | on-box Get-FileHash equals local sha256 for each | NOT APPLIED -- SUPERSEDED: order re-pinned to a51bd5cad5f (adds secret schwab/alongside/vnc-credentials), so this entry's manifest was wrong; replaced by nfra-schwabbf-alongside-role-state-tier-vnc-20261020. Nothing landed under this entry. | CLOSED 20261020T213633Z |

## Log

- 20261020T210717Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261020T211405Z HELD-PRE-APPLY gate=external/COO msg 110030: TO-AL-r3 to be re-pinned (AL-r4 needs the vnc secret created by 
- 20261020T213633Z HOLD RELEASED -> OPEN
- 20261020T213633Z LEG L1 closed: NOT APPLIED -- SUPERSEDED: order re-pinned to a51bd5cad5f (adds secret schwab/alongside/vnc-credentials), so this entry'
- 20261020T213633Z LEG L2 closed: NOT APPLIED -- SUPERSEDED: order re-pinned to a51bd5cad5f (adds secret schwab/alongside/vnc-credentials), so this entry'
- 20261020T213633Z LEG L3 closed: NOT APPLIED -- SUPERSEDED: order re-pinned to a51bd5cad5f (adds secret schwab/alongside/vnc-credentials), so this entry'
- 20261020T213633Z CLOSED -- all 3 legs proven
