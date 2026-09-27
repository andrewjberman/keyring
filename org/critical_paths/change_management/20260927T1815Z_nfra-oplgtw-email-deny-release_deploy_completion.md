# Deploy Completion Record
**Date opened:** 2026-09-27T18:15:09.444629+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T191151Z
**Deploy:** NFRA_OPLGTW OG-e-2: narrow opal-gateway release of OG-e-1's email-keyed deny guard
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~8
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (fe94911257, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI | INFO: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-fe94911257.tar.gz (+ latest); built from /c/tmp/og-rel HEAD fe94911257c2c3c4845f5dfa8bb8128804cd05ec with mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054 (INFO: building mcportal @ a3bff71ffa...); artifact 392K; halt gate 186 pending messages passed with HALT_ACK=1 (act 18:30:46Z-18:44:29Z, wrapper rc=0). | CLOSED 20260927T191121Z |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box /health 200 within 90s + on-box md5 of app/{access_state,data_entitlement,server,token_broker}.py = fe94911257's bytes 4/4 + on-host tool-name list AFTER=46 sorted diff vs BEFORE EMPTY + ENABLED_INTEGRATIONS unchanged | ssm:2ae27f67-2842-4c5f-9ab4-a68d859d07f0 OK: deploy Success; on-box (wrapper's own smoke, within its restart loop): OK: opal-gateway active, /health {"ok":true}, AS metadata serves, /mcp unauth 401. Restart confirmed via systemctl show ActiveEnterTimestamp 2026-09-27 18:43:56 UTC (ssm:822648a2-5d61-47cd-be87-db2006ba1bba). Independent verify ssm:822648a2-5d61-47cd-be87-db2006ba1bba (dispatched 18:50:03Z, restart+375s -- late per row NFRA_OPLGTW-Z-W8-S2): health=200; md5 4/4 = fe94911257's bytes (access_state.py 6d2c021b7f1c126dcb78325103e53400, data_entitlement.py 964504343c24d412a266da74e7108e69, server.py 1339aca9648e88ed754edcf902b7af26, token_broker.py aa08edc2a4c4d349b7c6b2d87b83729e); on-host tool-name list AFTER = 46 (same sorted 46 names as BEFORE ssm:29bd1824-f1dd-43ad-8cd3-3e5a4ffd45e1; diff EMPTY); ENABLED_INTEGRATIONS before and after = 'ycharts opal_portal globgrph' unchanged. NOT rolled back. | CLOSED 20260927T191122Z |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=fe94911257 full hash, previous_deployed_commit=110d93fb73 full hash, mcportal_commit unchanged, release_note naming CLOUD's unreleased gateway commits, committed on wk-NFRA_OPLGTW-8-e2 | the safe-commit hash | commit b7ced70bfe on wk-NFRA_OPLGTW-8-e2: EC2_MANIFEST.json services.opal-gateway deployed_commit=fe94911257c2c3c4845f5dfa8bb8128804cd05ec, previous_deployed_commit=110d93fb7395d36b7bf7af82119b89b5a839cb65, deployed_at=2026-09-27T18:43:56Z, deployed_by=0.9.0_WK_NFRA_OPLGTW~8, mcportal_commit unchanged. Recorded by hand on an LF copy (0 CR). The wrapper's auto-commit on rel-nfra-oplgtw-email-deny was refused at the naming-gate (89 pre-existing findings), left UNLANDED in /c/tmp/og-rel. | CLOSED 20260927T191122Z |
| L6 | verify | rollback to 110d93fb73 proven before the act without uploading: clean base tree /c/tmp/og-rb (HEAD 110d93fb73, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); rollback command cd /c/tmp/og-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + identical-file count against live | /c/tmp/og-rb HEAD=110d93fb7395d36b7bf7af82119b89b5a839cb65 clean (mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); rollback artifact opal-gateway-110d93fb73.tar.gz 397077 bytes proven 79 of 79 files IDENTICAL against live BEFORE the act (per Phase A step 6). Redeploy: cd /c/tmp/og-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh. NOT exercised -- the act succeeded on fe94911257 (all L2/AC verify conditions PASS), so rollback was not invoked. | CLOSED 20260927T191122Z |

## Log

- 20260927T181509Z OPENED by 0.9.0_WK_NFRA_OPLGTW~8 with 4 leg(s)
- 20260927T191121Z LEG L1 closed: INFO: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-fe94911257.tar.gz (+ latest); built
- 20260927T191122Z LEG L2 closed: ssm:2ae27f67-2842-4c5f-9ab4-a68d859d07f0 OK: deploy Success; on-box (wrapper's own smoke, within its restart loop): OK: 
- 20260927T191122Z LEG L3 closed: commit b7ced70bfe on wk-NFRA_OPLGTW-8-e2: EC2_MANIFEST.json services.opal-gateway deployed_commit=fe94911257c2c3c4845f5d
- 20260927T191122Z LEG L6 closed: /c/tmp/og-rb HEAD=110d93fb7395d36b7bf7af82119b89b5a839cb65 clean (mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); ro
- 20260927T191151Z CLOSED -- all 4 legs proven
