# Deploy Completion Record
**Date opened:** 2026-09-30T10:13:32.772457+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS round-1 live thread (RIV-d-2): etfs-rivalfunds apply, gateway read policy, gateway deploy, BASG backfill, fire
**Authored by:** 0.9.0_WK_ETFS_RIVALS~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas, roles, bucket notification EventBridge-only, 3 rules, 2 schedules) | apply output: Apply complete, 0 changed 0 destroyed | safe-apply etfs-rivalfunds: Apply complete! Resources: 39 added, 0 changed, 0 destroyed. (2026-09-30 ~10:39Z; plan create-only 39, EventBridge re-scan 144 rules 0 read errors 0 matches) | CLOSED 20260930T104057Z |
| L2 | activation | safe-apply gw_rivalfunds_read gateway-rivalfunds-read-policy (opal-gateway, create-only) | apply output: 1 added 0 changed 0 destroyed | safe-apply opal-gateway targeted aws_iam_role_policy.gw_rivalfunds_read: Apply complete! Resources: 1 added, 0 changed, 0 destroyed; live get-role-policy reads gateway-rivalfunds-read-policy on opal-gateway-role | CLOSED 20260930T111315Z |
| L3 | ec2-baked-asset | opal-gateway app rivalfunds_view.py rivalfunds_location.json gen_rivalfunds_location.py server.py via safe-ec2-deploy.sh | SSM sha256 of the running files equal HEAD (d-2.AC2) |  | OPEN |
| L4 | verify | gateway /healthz reads 200 after deploy | curl http code 200 |  | OPEN |
| L5 | activation | fetch-holdings Lambda backfill 2025-06-13..T-1 (batch_id backfill-r1), markers drive silver gold page | request ids + S3 prefix object counts |  | OPEN |
| L6 | verify | d-2 AC1 AC2 AC3 and /rivalfunds read equals newest platinum/page object | checks PASS |  | OPEN |

## Log

- 20260930T101332Z OPENED by 0.9.0_WK_ETFS_RIVALS~5 with 6 leg(s)
- 20260930T104057Z LEG L1 closed: safe-apply etfs-rivalfunds: Apply complete! Resources: 39 added, 0 changed, 0 destroyed. (2026-09-30 ~10:39Z; plan creat
- 20260930T111315Z LEG L2 closed: safe-apply opal-gateway targeted aws_iam_role_policy.gw_rivalfunds_read: Apply complete! Resources: 1 added, 0 changed, 
