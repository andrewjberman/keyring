# Deploy Completion Record
**Date opened:** 2026-10-01T12:30:08.432657+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T133010Z
**Deploy:** NFRA_MCPINDEX MX-r-8 PHASE B: slot-4 opal-gateway release (discover reads silver_datasets + G-RDR internal-reader routing) on live ref daa56d81ac -- release 01845e91cf / deploy-only e3567ce5f7 (gateway tree 7d222e01f6); no Terraform, no .env key; consumers of the artifact: the single opal-gateway EC2 host i-07dccb1615503ac99 only; rollback /c/tmp/mx-rb11
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~22
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | live ref re-read BY REF before the first act: S3 opal-gateway-latest git-ref metadata + CLOUD EC2_MANIFEST services.opal-gateway.deployed_commit; must be daa56d81ac7c91795f1a9c47b2c2430cb3879e24 else STOP | both reads printed equal | 2026-10-01T12:22:37Z read BY REF: s3api head-object opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-latest.tar.gz Metadata git-ref = daa56d81ac7c91795f1a9c47b2c2430cb3879e24 (LastModified 10:43:27Z, ETag b78383f9...); newest keys -latest and -daa56d81ac; CLOUD c6e376360e EC2_MANIFEST services.opal-gateway.deployed_commit = daa56d81ac7c91795f1a9c47b2c2430cb3879e24 (10:43:56Z). Equal to the pin. | CLOSED 20261001T123036Z |
| L2 | s3-prefix | upload deploy-only tree e3567ce5f7 gateway tarball from /c/tmp/mx-dep11 to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with DEPLOY_BASE_REF=daa56d81ac (guard at upload) and OG_MAIL_SENDER_TABLE supplied in the shell (3 items 67 chars, never printed) | deploy output line uploaded ...-e3567ce5f7 (+ latest), both base guards equal | 2026-10-01T12:36Z safe-ec2-deploy.sh opal-gateway from /c/tmp/mx-dep11 (e3567ce5f7), DEPLOY_BASE_REF=daa56d81ac7c91795f1a9c47b2c2430cb3879e24: base guard [early] and [immediately-before-upload] both declared == live ref daa56d81ac; INFO: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-e3567ce5f7.tar.gz (+ latest); OG_MAIL_SENDER_TABLE 3 items 67 chars, never printed. Record: probes_r8/deploy_PHASEB_scrubbed.txt | CLOSED 20261001T133009Z |
| L3 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 | SSM Status=Success + ssm:<command_id> + host sha256 of all 94 files equal the deployed artifact | SSM ssm:b4d4af51-a13d-4246-b9df-223d93aea423 Success on i-07dccb1615503ac99 ('OK: deploy Success'; rosters read host-side; opal-gateway active; AS metadata serves; /mcp unauth 401); host sha256 of all files vs the deployed artifact: identical 94 of 94, only-host [], only-artifact [] (probes_r8/host_vs_artifact_PHASEB.txt) | CLOSED 20261001T133009Z |
| L4 | verify | read-back: r8.AC2 PASS; .env keys 46==46; MAIL_SENDER_TABLE SET 3 items/67 chars before+after; INTERNAL_READER_ROLE_ARN present; tools 65==65; host==94-file artifact; git-ref e3567ce5f7 on both S3 objects; A1 (3 KNOWN_FIRMS no silver match, OPAL_INTERNAL routed); e1z.AC1.sh unrouted=0 | each line recorded with output | r8.AC2 PASS (SSM Success, /health=200, BD ask next_tools=[blackdiamond_list_fees], ETF ask next_tools=[etfs_get_positioning]); .env KEY set 46 == 46 (0 dropped, 0 added); MAIL_SENDER_TABLE SET items=3 len=67 before and after; INTERNAL_READER_ROLE_ARN present; tools 65 == 65 (0 added, 0 removed); git-ref e3567ce5f788f45195bec065f4d2fc5a68a38cd3 on -latest and -e3567ce5f7 (byte-equal objects); A1 PASS 8 of 8 legs (3 KNOWN_FIRMS no silver match for BD fees and Schwab positions; OPAL_INTERNAL routed blackdiamond_list_fees and schwab_query); e1z.AC1.sh on /c/tmp/mx-dep11: s3 call sites scanned=20 portal-v2 reader files=3 unrouted=0. Records: probes_r8/*_PHASEB*.txt | CLOSED 20261001T133010Z |
| L5 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=e3567ce5f788f45195bec065f4d2fc5a68a38cd3 previous=daa56d81ac (own edit; no foreign manifest commit merged), committed on wk-nfra_mcpindex-6-22 | safe-commit hash | 4ce50b6150 (safe-commit on wk-nfra_mcpindex-6-22, LOCAL): EC2_MANIFEST.json services.opal-gateway deployed_commit e3567ce5f788f45195bec065f4d2fc5a68a38cd3, previous_deployed_commit daa56d81ac7c91795f1a9c47b2c2430cb3879e24; wrapper dep-branch commit 93eacb12e9 not merged | CLOSED 20261001T133010Z |

## Log

- 20261001T123008Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~22 with 5 leg(s)
- 20261001T123036Z LEG L1 closed: 2026-10-01T12:22:37Z read BY REF: s3api head-object opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-lat
- 20261001T133009Z LEG L2 closed: 2026-10-01T12:36Z safe-ec2-deploy.sh opal-gateway from /c/tmp/mx-dep11 (e3567ce5f7), DEPLOY_BASE_REF=daa56d81ac7c91795f1
- 20261001T133009Z LEG L3 closed: SSM ssm:b4d4af51-a13d-4246-b9df-223d93aea423 Success on i-07dccb1615503ac99 ('OK: deploy Success'; rosters read host-sid
- 20261001T133010Z LEG L4 closed: r8.AC2 PASS (SSM Success, /health=200, BD ask next_tools=[blackdiamond_list_fees], ETF ask next_tools=[etfs_get_position
- 20261001T133010Z LEG L5 closed: 4ce50b6150 (safe-commit on wk-nfra_mcpindex-6-22, LOCAL): EC2_MANIFEST.json services.opal-gateway deployed_commit e3567c
- 20261001T133010Z CLOSED -- all 5 legs proven
