# Deploy Completion Record
**Date opened:** 2026-10-01T01:30:06.854523+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-t-2 PHASE B: principal-keyed tier and auth-hardening gateway release rel-nfra-oplgtw-tier-auth d61fde4693 on live 42c52ed4d9 (15 gateway files, +2 .env keys MASTER_ADMIN_PRINCIPALS and WRITE_CAPABLE_PRINCIPALS, principal values from PART_D_RECORD_20260930.md @205c2e7f6c never in the repo); order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-t-2.tier-auth-release.md A1+A2; halves CTO @51df60aa1a and CVO @045f6886d9; issuer GO 2.0.0_SA_COO~O 2026-10-01 ~01:20Z. POST-RELEASE TIER READS, two named sessions: (a) ADMIN read = issuer 2.0.0_SA_COO~O own opal-gateway MCP session signed in as the admin principal, must audit MASTER_ADMIN; (b) K2 read = Opal_Agent Claude session on opal-gateway-bbg (Andrew Analyst window, launch-v2.ps1) signed in as the Opal Bloomberg principal, must audit STANDARD_EMPLOYEE. Either read other than required, or (b) absent 8 minutes after deployed_at, rolls back from /c/tmp/og-rb2 (42c52ed4d9 bytes) with DEPLOY_BASE_REF=d61fde46933221e8afbac7418f06d7525d3347c8 and closes ROLLED BACK.
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~12
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | upload release d61fde4693 gateway tarball from /c/tmp/og-rel2 to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with DEPLOY_BASE_REF=42c52ed4d9e834b0f1cf4f96eb83f9b0f7a183df after the 13-file host md5 re-read equals 42c52ed4d9 bytes (K1) | the deploy-to-ec2.sh INFO: uploaded line naming opal-gateway-d61fde4693.tar.gz plus both base-guard INFO lines |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99, then K3 read-back and the two tier reads (a) ADMIN session and (b) K2 Opal Bloomberg session | SSM Status=Success + /health 200 + md5 of shipped files == release bytes + tool list AFTER == BEFORE (58, sorted diff empty) + ENABLED_INTEGRATIONS unchanged (6 ids) + FIRM_ROLE_ARNS present + .env 33->35 keys + tier read (a) MASTER_ADMIN + tier read (b) STANDARD_EMPLOYEE (tier, tool, UTC only) |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=d61fde4693 full sha, previous_deployed_commit=42c52ed4d9 full sha, deployed_at, deployed_by, mcportal_commit unchanged, release_note, committed on wk-NFRA_OPLGTW-12-t2 | the safe-commit hash |  | OPEN |
| L4 | verify | rollback proven: /c/tmp/og-rb2 at 42c52ed4d9 with mcportal a3bff71ffa, artifact equal to the live S3 artifact; if a rollback runs, its re-verify (/health 200, md5 == 42c52ed4d9 bytes) | 87 of 87 files identical to the live artifact (PHASE A, ANNOUNCE_OG-t-2.md) or the rollback re-verify output |  | OPEN |

## Log

- 20261001T013006Z OPENED by 0.9.0_WK_NFRA_OPLGTW~12 with 4 leg(s)
