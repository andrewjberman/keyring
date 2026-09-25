# Deploy Completion Record
**Date opened:** 2026-09-25T16:36:24.529469+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL TO-MP-d-1: NARROW opal-gateway release c97839d7c8 (branch rel-nfra-mcportal-r2-gateway, worktree /c/tmp/mp-2-rel) to i-07dccb1615503ac99, serving Andrew dashboard. Ruling: org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.round1.md section 4 E4 (@667f442b8a). CENSUS: git diff --stat f1f0fc6780 c97839d7c8 -- infra/aws/ec2/opal-gateway = 9 files (app/admin_api.py app/admin_grants.py app/config.py app/owner_gate.py app/server.py deploy-to-ec2.sh tests/test_admin_grants.py tests/test_admin_round2.py tests/test_owner_gate.py), 0 outside 98ad7e253f+17b7e01c0f+d0ba96d27c+ece3aab4b5. BUNDLE: mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054. ROLLBACK (proven before the act): prior deployed_commit f1f0fc6780; a clean git-archive of f1f0fc6780 rebuilt with its own tar line, WITHOUT upload, is 69 of 69 members content-identical to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-f1f0fc6780.tar.gz (ETag 4a8b6016294ddfbb53c825606c77cdcc, == opal-gateway-latest.tar.gz before the act). Re-deploy command: git -C /c/tmp/mp-2 worktree add --detach /c/tmp/mp-2-rb f1f0fc6780 && cd /c/tmp/mp-2-rb && AGENT_NAME=0.9.0_WK_NFRA_MCPORTAL~2 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (rewrites .env without the three dashboard lines; files new in this release stay on disk inert). Blast radius: /opt/opal-gateway code + .env + opal-gateway.service restart on the one host, and the two S3 artifact keys; Terraform/ALB/role/secrets untouched.
**Authored by:** 0.9.0_WK_NFRA_MCPORTAL~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | mcportal@a3bff71 bundle build (bun install --frozen-lockfile + bun run build) in /c/tmp/mp-2-rel/mcportal | build rc=0 + dist/index.html present + bundle members in the artifact |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-c97839d7c8.tar.gz + opal-gateway-latest.tar.gz | s3api head-object ETag/size of both keys after upload |  | OPEN |
| L3 | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway SSM pull + opal-gateway.service restart | ssm:<id> Status=Success + md5 of the RUNNING path files == release tree + service active + /health 200 |  | OPEN |
| L4 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on wk-NFRA_MCPORTAL-2 (deployed_commit, mcportal_commit, release_note) | commit hash on wk-NFRA_MCPORTAL-2 |  | OPEN |

## Log

- 20260925T163624Z OPENED by 0.9.0_WK_NFRA_MCPORTAL~2 with 4 leg(s)
