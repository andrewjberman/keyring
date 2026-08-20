# Deploy Completion Record
**Date opened:** 2026-08-20T14:56:23.952800+00:00
**Status:** OPEN
**Deploy:** OPAL_ANALYST.W6-PORT: catalog port + /query/v0 plumbing endpoint + IAM read grant + gateway EC2 deploy
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | code+catalog+TF committed pre-apply (Rule 2) | commit hashes |  | OPEN |
| L2 | activation | safe-apply infra/aws/terraform/opal-gateway (ONE add: gw_queryv0_portal_read policy) | apply + 0-diff + live simulate allowed |  | OPEN |
| L3 | s3-prefix | safe-ec2-deploy opal-gateway (S3 tarball -> SSM pull -> service restart) | deploy output + manifest entry |  | OPEN |
| L4 | verify | on-box battery 13/13 (SSM) + endpoint exercises ALLOW/DENY/403-floor/limit-trip + audit-lake object | SSM outputs + curl outputs + S3 audit key |  | OPEN |

## Log

- 20260820T145623Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
