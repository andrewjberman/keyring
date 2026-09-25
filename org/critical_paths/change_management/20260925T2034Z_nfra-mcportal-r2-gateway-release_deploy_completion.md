# Deploy Completion Record
**Date opened:** 2026-09-25T20:34:43.107632+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL TO-MP-d-1 RETRY (amended 1fdb3ed8ab + 894cf33916): NARROW opal-gateway release 1f7128201a (branch rel-nfra-mcportal-r2-gateway-2, worktree /c/tmp/mp-2-rel2, base f1f0fc6780 = the DEPLOYED commit per ruling @75117e60d6) to i-07dccb1615503ac99, serving Andrew's dashboard. NEVER the failed branch rel-nfra-mcportal-r2-gateway (c97839d7c8). Ruling: org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.round1.md section 4 E4; privacy sign-off org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/1.0.0_SA_CTO~O/RULING_MP-d-1_RELEASE_SIGNOFF_20260925.md @384fd85543. CENSUS: git diff --stat f1f0fc6780 1f7128201a -- infra/aws/ec2/opal-gateway = 9 files (app/admin_api.py app/admin_grants.py app/config.py app/owner_gate.py app/server.py deploy-to-ec2.sh tests/test_admin_grants.py tests/test_admin_round2.py tests/test_owner_gate.py), all NFRA_MCPORTAL's. BUNDLE: mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054. RENDER GATE 4a(i): release .env printf rendered locally with 9 markers derived from the script's own argument list -> 9 of 9 on their own keys, 0 misaligned, 26 keys, DASHBOARD_OWNER_EMAILS + GRANT_WRITER_FUNCTION_NAME + MCPORTAL_CHANGES_TABLE 3 of 3 present. ROLLBACK (proven before the act): clean detached f1f0fc6780 worktree /c/tmp/mp-2-rb (0 dirty paths) rebuilt with its own tar line WITHOUT upload = 69 of 69 members content-identical (diff -r rc=0; planted-change control rc=1) to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-f1f0fc6780.tar.gz (285888 bytes, ETag 4a7d215b70ce86075f838b22a6135766); md5 app/server.py app/tools.py app/config.py 3 of 3 == the RUNNING host. Re-deploy command: cd /c/tmp/mp-2-rb && AGENT_NAME=0.9.0_WK_NFRA_MCPORTAL~2 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (rewrites the 23-key f1f0fc6780 .env; release-only files stay on disk inert). TRIGGER 4a(ii): /health not 200 within 90 s of the SSM restart -> that command at once. BEFORE 4a(iii): ssm:1657bf5e-c955-4539-9221-cfbae1a11ff5 read-only on-box, service venv + .env, 45 registered tool names; active since 2026-09-25 17:31:22 UTC, /health 200, .env 23 keys. Blast radius: /opt/opal-gateway code + .env + opal-gateway.service restart on the one host, and the two S3 artifact keys; Terraform/ALB/role/secrets untouched.
**Authored by:** 0.9.0_WK_NFRA_MCPORTAL~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | mcportal@a3bff71 bundle build (bun install + bun run build) in /c/tmp/mp-2-rel2/mcportal | build rc=0 + dist/index.html present + bundle members in the artifact |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-1f7128201a.tar.gz + opal-gateway-latest.tar.gz | s3api head-object ETag/size of both keys after upload |  | OPEN |
| L3 | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway SSM pull + opal-gateway.service restart | ssm:<id> Status=Success + /health 200 within 90 s + md5 of RUNNING path files == release tree + AFTER tool list == BEFORE (45, empty difference) |  | OPEN |
| L4 | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway on wk-NFRA_MCPORTAL-2 (deployed_commit, mcportal_commit, release_note) | commit hash on wk-NFRA_MCPORTAL-2 |  | OPEN |

## Log

- 20260925T203443Z OPENED by 0.9.0_WK_NFRA_MCPORTAL~2 with 4 leg(s)
