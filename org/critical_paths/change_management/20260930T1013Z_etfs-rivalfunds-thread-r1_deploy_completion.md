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
| L5 | activation | fetch-holdings Lambda backfill 2025-06-13..T-1 (batch_id backfill-r1), markers drive silver gold page | request ids + S3 prefix object counts | fetch Lambda backfill 2025-06-13..2026-09-28 OK in two ranges (requests fcdfce7c-268b-41b2-899b-1450f64601a4 batch backfill-r1a 139 days; 7b2bb944-1be7-43de-8ccd-3f350c8abcfe batch backfill-r1b 185 days) + 07:00 ET scheduled fire 096abceb-b054-44d0-8e4e-064af5eb525c; bronze 325 raw + 325 sidecar (all OK, runtime fetch Lambda), silver 325 parquet, markers fetch_holdings 3 build_silver 3; GOLD BLOCKED: canonical_shape FileNotFoundError /var/task/gold/etf_positioning_gold.py, gold/page 0 objects, row ETFS_RIVALS-Z-W5-S4; d2_live.json c-committed 6d51af5322 | CLOSED 20260930T120332Z |
| L6 | verify | d-2 AC1 AC2 AC3 and /rivalfunds read equals newest platinum/page object | checks PASS |  | OPEN |

## Log

- 20260930T101332Z OPENED by 0.9.0_WK_ETFS_RIVALS~5 with 6 leg(s)
- 20260930T104057Z LEG L1 closed: safe-apply etfs-rivalfunds: Apply complete! Resources: 39 added, 0 changed, 0 destroyed. (2026-09-30 ~10:39Z; plan creat
- 20260930T111315Z LEG L2 closed: safe-apply opal-gateway targeted aws_iam_role_policy.gw_rivalfunds_read: Apply complete! Resources: 1 added, 0 changed, 
- 20260930T120332Z LEG L5 closed: fetch Lambda backfill 2025-06-13..2026-09-28 OK in two ranges (requests fcdfce7c-268b-41b2-899b-1450f64601a4 batch backf
