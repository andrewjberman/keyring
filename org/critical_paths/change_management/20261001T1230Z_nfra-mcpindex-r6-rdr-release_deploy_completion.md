# Deploy Completion Record
**Date opened:** 2026-10-01T12:30:08.432657+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-8 PHASE B: slot-4 opal-gateway release (discover reads silver_datasets + G-RDR internal-reader routing) on live ref daa56d81ac -- release 01845e91cf / deploy-only e3567ce5f7 (gateway tree 7d222e01f6); no Terraform, no .env key; consumers of the artifact: the single opal-gateway EC2 host i-07dccb1615503ac99 only; rollback /c/tmp/mx-rb11
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~22
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | live ref re-read BY REF before the first act: S3 opal-gateway-latest git-ref metadata + CLOUD EC2_MANIFEST services.opal-gateway.deployed_commit; must be daa56d81ac7c91795f1a9c47b2c2430cb3879e24 else STOP | both reads printed equal | 2026-10-01T12:22:37Z read BY REF: s3api head-object opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-latest.tar.gz Metadata git-ref = daa56d81ac7c91795f1a9c47b2c2430cb3879e24 (LastModified 10:43:27Z, ETag b78383f9...); newest keys -latest and -daa56d81ac; CLOUD c6e376360e EC2_MANIFEST services.opal-gateway.deployed_commit = daa56d81ac7c91795f1a9c47b2c2430cb3879e24 (10:43:56Z). Equal to the pin. | CLOSED 20261001T123036Z |
| L2 | s3-prefix | upload deploy-only tree e3567ce5f7 gateway tarball from /c/tmp/mx-dep11 to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with DEPLOY_BASE_REF=daa56d81ac (guard at upload) and OG_MAIL_SENDER_TABLE supplied in the shell (3 items 67 chars, never printed) | deploy output line uploaded ...-e3567ce5f7 (+ latest), both base guards equal |  | OPEN |
| L3 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 | SSM Status=Success + ssm:<command_id> + host sha256 of all 94 files equal the deployed artifact |  | OPEN |
| L4 | verify | read-back: r8.AC2 PASS; .env keys 46==46; MAIL_SENDER_TABLE SET 3 items/67 chars before+after; INTERNAL_READER_ROLE_ARN present; tools 65==65; host==94-file artifact; git-ref e3567ce5f7 on both S3 objects; A1 (3 KNOWN_FIRMS no silver match, OPAL_INTERNAL routed); e1z.AC1.sh unrouted=0 | each line recorded with output |  | OPEN |
| L5 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=e3567ce5f788f45195bec065f4d2fc5a68a38cd3 previous=daa56d81ac (own edit; no foreign manifest commit merged), committed on wk-nfra_mcpindex-6-22 | safe-commit hash |  | OPEN |

## Log

- 20261001T123008Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~22 with 5 leg(s)
- 20261001T123036Z LEG L1 closed: 2026-10-01T12:22:37Z read BY REF: s3api head-object opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-lat
