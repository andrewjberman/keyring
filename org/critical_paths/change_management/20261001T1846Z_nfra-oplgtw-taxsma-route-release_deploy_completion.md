# Deploy Completion Record
**Date opened:** 2026-10-01T18:46:25.229194+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T185706Z
**Deploy:** NFRA_OPLGTW OG-tr-1 Tax SMA workbook route narrow gateway release, capability ON (train slot 6) on live 0a1d9079c6
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-<release sha>.tar.gz and -latest with git-ref=release sha | deploy's own upload success lines + head-object git-ref | deploy log: INFO uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-3a7d6a7dc8.tar.gz (+ latest); base guard equal 0a1d9079c6 at the early and immediately-before-upload reads (DEPLOY_BASE_REF=0a1d9079c682c640e619612f804257681c5db357, M3); head-object on -latest: git-ref 3a7d6a7dc85fe3c54a4b63b27b59055abc9adca7, ETag e1e72015, 472247 bytes, LastModified 2026-10-01T18:49:35Z; prior object opal-gateway-0a1d9079c6.tar.gz intact (ETag 6201fccf, 463612 bytes) | CLOSED 20261001T185705Z |
| install_verify | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway release 3a7d6a7dc8 on live 0a1d9079c6 | SSM deploy Success + /health 200 + shipped md5 == release + tools 65 -> 65 + .env 46 -> 48 keys (+TAXSMA_WORKBOOK_BEARER, +TAXSMA_WORKBOOK_IDENTITY) + ENABLED_INTEGRATIONS unchanged + /ms/* and /hx/* as before + M1 arm (mail and transcripts bearers read 401 UNAUTHORIZED_CAPABILITY on the Tax route) + tr.AC1.sh TAX ARMS 4 of 4 | deploy SSM 37cbcb93-774e-474e-96ff-bf7a73b1358b Success (OK taxsma-workbook bearer read host-side, non-empty, 64 characters; OK opal-gateway active; ENV_KEYS 46 -> 48); M1 compare SSM 242077e6-ac17-4430-99f7-d1ffb609eb4d BEFORE the upload: TRANSCRIPT_BEARER, MAIL_BEARER, OTP_BEARER (2 tokens), MS_INGEST_BEARER, GRAPH_READ_BEARER all DIFFER; verify SSM 934c4b09-22a2-47ec-9ad0-043ffb29e14d at 18:50:48Z (deploy returned 18:50:28Z): /health 200, 93 of 93 shipped files md5 == release bytes, tools 65 -> 65, .env 46 -> 48 keys (+TAXSMA_WORKBOOK_BEARER +TAXSMA_WORKBOOK_IDENTITY non-empty, other 46 unchanged), ENABLED_INTEGRATIONS unchanged, 8 probes as before, Tax route no-bearer 404 -> 401 UNAUTHORIZED_CAPABILITY, VERIFY PASS 8 of 8; M1 arm SSM 4bfd99ce-db7f-4a8b-9f3d-3e62a0e11ff7: mail and transcripts bearers each 401 UNAUTHORIZED_CAPABILITY; tr.AC1.sh (SSM a121a833-f7af-409f-b12b-4539f9adb818) TAX ARMS 4 of 4 RESULT: PASS, host module sha256 6acc3e8ce8952cdddea67f260814af4abe6bc055f8f9a4c8300b23f3e2a6ee70 | CLOSED 20261001T185705Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=release sha on wk-NFRA_OPLGTW-15-r8 | safe-commit hash + tr.AC2.sh PASS | safe-commit b49b3910738cdd9cf9cce7218c8673b6be65660a on wk-NFRA_OPLGTW-15-r8: EC2_MANIFEST.json services.opal-gateway deployed_commit=3a7d6a7dc85fe3c54a4b63b27b59055abc9adca7 previous=0a1d9079c682c640e619612f804257681c5db357 deployed_at 2026-10-01T18:50:02Z deployed_by 0.9.0_WK_NFRA_OPLGTW~15; tr.AC2.sh PASS read after this ledger close | CLOSED 20261001T185705Z |
| rollback_proven | verify | rollback tree /c/tmp/og-rb6 at 0a1d9079c6 with DEPLOY_BASE_REF=release sha (artifact 95 of 95 == live S3, built not uploaded; or executed if a verify fails) | rollback command named + artifact equality read | no rollback was needed (VERIFY 8 of 8, M1 arm 2 of 2, tr.AC1 4 of 4). Rollback tree /c/tmp/og-rb6 at 0a1d9079c682c640e619612f804257681c5db357 (clean, mcportal a3bff71ffa) rebuilt after the release: 463574 bytes, 95 files, equal file by file (diff -rq empty, 95 of 95) to the intact prior S3 object opal-gateway-0a1d9079c6.tar.gz (ETag 6201fccf, 463612 bytes). Re-deploy command: cd /c/tmp/og-rb6 && DEPLOY_BASE_REF=3a7d6a7dc85fe3c54a4b63b27b59055abc9adca7 HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (M2: blanking the identity is not a rollback) | CLOSED 20261001T185706Z |

## Log

- 20261001T184625Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
- 20261001T185705Z LEG upload closed: deploy log: INFO uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-3a7d6a7dc8.tar.gz (+ lat
- 20261001T185705Z LEG install_verify closed: deploy SSM 37cbcb93-774e-474e-96ff-bf7a73b1358b Success (OK taxsma-workbook bearer read host-side, non-empty, 64 charact
- 20261001T185705Z LEG manifest closed: safe-commit b49b3910738cdd9cf9cce7218c8673b6be65660a on wk-NFRA_OPLGTW-15-r8: EC2_MANIFEST.json services.opal-gateway de
- 20261001T185706Z LEG rollback_proven closed: no rollback was needed (VERIFY 8 of 8, M1 arm 2 of 2, tr.AC1 4 of 4). Rollback tree /c/tmp/og-rb6 at 0a1d9079c682c640e61
- 20261001T185706Z CLOSED -- all 4 legs proven
