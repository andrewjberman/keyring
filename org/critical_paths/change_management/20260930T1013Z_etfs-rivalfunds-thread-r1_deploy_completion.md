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
- 20260930T123300Z NOTE (0.9.0_WK_ETFS_RIVALS~5): L5's closing proof above says GOLD BLOCKED; superseded -- row W5-S4 fixed (commit 3eaa380467, safe-apply 0 added 5 changed 0 destroyed), sweep-r2 request cbff54d3-1926-45dc-a946-4d5932eb3fd3 OK: gold canonical_shape 325, trade_schedule 324, platinum/page 6, markers 3 each; AC1 and AC3 PASS
- 20260930T124300Z NOTE (0.9.0_WK_ETFS_RIVALS~5): LEG B (L3, L4, L6) STOPPED and left OPEN -- row ETFS_RIVALS-Z-W5-S8: EC2_MANIFEST deployed_commit moved 093fc247c6 -> 288fa78c93 (host equals it, 79 of 79); a 093fc247c6 deploy ref would revert 12 files of NFRA_MCPMSP's release. No deploy ref built, no gateway deploy, no deploy ref hash to record. Issuer decides the deploy base
- 20260930T125900Z NOTE (0.9.0_WK_ETFS_RIVALS~5): LEG B (L3, L4, L6) re-attempted under amendment 4 and STOPPED again, left OPEN -- row ETFS_RIVALS-Z-W5-S9: step 1 PASSED (BASE 288fa78c93e1c57be0ad7b8d6371c69145a69856 = manifest deployed_commit; host equals it 79 of 79, SSM 433b8c15-cf2b-4cb9-a0fe-b0a1d3bb123f; no open gateway ledger entry in 90 worktrees); step 2's git reset --hard BASE in the deploy-only worktree was DENIED by the permission system. No deploy ref re-pointed, built or deployed; the gateway is unchanged. AC1 and AC3 re-run at 12:56Z: PASS.
- 20260930T140700Z NOTE (0.9.0_WK_ETFS_RIVALS~5): LEG B (L3, L4, L6) STOPPED and left OPEN -- row ETFS_RIVALS-Z-W5-S12. Amendment 4 steps 4-5 run against the issuer's committed ref 4ce794642699e78a718b8154664e1428737f996a (BASE 288fa78c93 + the five key-16 files): step 4 PASSED twice (manifest deployed_commit 288fa78c93 on CLOUD HEAD; SSM sha256 of the host app tree equals BASE 76 of 76 files, commands c342d0ce-45be-410c-9421-c6013ddad1d2, 95d1accc-0a01-419e-abf8-cc00c91e47c9, bcd99cc2-7230-48d5-8c40-560c6c71b43c). Step 5 safe-ec2-deploy.sh from C:/tmp/wk-rivals-5gw: HALT-GATE refused rc=3 before Step 2 (IDENTITY UNRESOLVED, then with the serial file provisioned: SERIAL RESOLVES TO NO KNOWN AGENT, because the gate admits a 0.9.0_WK worker only while a non-terminal order issued_to it is in the committing tree's HEAD and the ref carries none). Nothing was built, uploaded or deployed; the gateway is unchanged (still BASE); no rollback needed. AC1 PASS, AC3 PASS re-run at ~14:04Z; AC2 FAIL (no gateway_deploy_commit).
