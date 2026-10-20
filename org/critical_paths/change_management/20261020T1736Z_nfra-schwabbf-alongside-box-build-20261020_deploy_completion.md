# Deploy Completion Record
**Date opened:** 2026-10-20T17:36:46.837240+00:00
**Status:** OPEN
**Deploy:** NFRA_SCHWABBF Alongside Schwab Box build: new Terraform root alongside-schwab-ec2 (17 adds + 1 import of schwab/alongside/sdd-credentials), 4 code files to S3, bootstrap, one reboot. Nothing existing is modified.
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply of the saved plan in infra/aws/terraform/alongside-schwab-ec2 via safe-apply (1 import, 17 add, 0 change, 0 destroy) | apply summary line + 0-diff plan exit 0 |  | OPEN |
| L2 | s3-prefix | opal-data-assets code/alongside-schwab-si2 four files | local sha256 and head-object sizes match |  | OPEN |
| L3 | activation | bootstrap.ps1 over SSM on the new instance + one reboot | every step OK and quser shows administrator console Active |  | OPEN |
| L4 | verify | RDP port-forward 13389 connects with zero ingress and four rules DISABLED | TCP connect result + describe-rule State DISABLED |  | OPEN |

## Log

- 20261020T173646Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 4 leg(s)
