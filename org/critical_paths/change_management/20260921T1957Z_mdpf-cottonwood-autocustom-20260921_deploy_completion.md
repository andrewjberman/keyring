# Deploy Completion Record
**Date opened:** 2026-09-21T19:57:50.394476+00:00
**Status:** OPEN
**Deploy:** mdpf-gold-lambda Cottonwood auto-custom deploy, Phase A + Phase B, TWO LEGS (Andrew-direct via MSTR @0b46309ec2: ~V does the work, 4.0.0_SA_CRO + 1.0.0_SA_CTO sign off; ~19:45Z @1ab93ec740 'Sign first, then push'). LEG A: minimal pin 74d7efe144 over running 48b8671569, zip sha256 9c6db39ae8ae7c9d21060dfbdc5bb451053fbca9564cd046f3df75090804d0cd 868,952 B, upload to opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip, MDPF_GOLD_COMMIT literal, safe-apply -target=aws_lambda_function.mdpf_gold. LEG B: the CLOUD push's safe-deploy sync of 4 files to opal-data-mdpf/code/scripts/ (EC2 mdpf-daily-runner). NOTHING EXECUTES UNTIL BOTH HALVES ARE AT HEAD naming the packet blob. Rollback: artifact VersionId 9GsracvIPvfBMzF1dttMpew0TkQtt.qg + MDPF_GOLD_COMMIT 48b8671569b72efb4eca64ef41ded4de9c54e84c; LEG B per-key VersionIds in packet s.5. Acceptance = 2026-09-22 13:30Z scheduled fire, never an ad-hoc invoke.
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | new VersionId latest + content-sha256 metadata == 9c6db39a... + re-download sha256 == built; prior version 9GsracvI... kept (packet NEVER_WIDEN_SIGNOFF_PACKET_MDPF_COTTONWOOD_AUTOCUSTOM_20260921.md s.6) |  | OPEN |
| L2 | git | infra/aws/terraform/mdpf-pipeline/gold-lambda.tf MDPF_GOLD_COMMIT -> 74d7efe1449b47587cf0d8ca47e3a0f9824bf297 | CLOUD commit hash; value == the built zip's in-zip source_vintage.commit |  | OPEN |
| L3 | activation | aws_lambda_function.mdpf_gold (safe-apply -target) | targeted plan EXACTLY 1 update (s3_object_version, source_code_hash, env MDPF_GOLD_COMMIT), 0 add, 0 destroy; safe-apply rc=0 'Apply complete' |  | OPEN |
| L4 | verify | mdpf-gold-lambda running plane | CodeSha256 == b64(9c6db39a...), CodeSize 868,952, MDPF_GOLD_COMMIT == pin, re-downloaded in-zip source_vintage == pin; control FALSE->TRUE: mdpf_name_discovery.py member + is_auto_custom in slice; post-apply targeted replan 0-diff |  | OPEN |
| L5 | s3-prefix | opal-data-mdpf/code/scripts/{assets_gold,gold}/ (LEG B, the CLOUD push's sync) | s.5 table re-derived immediately before the push (safe-deploy's own functions, printed); after the push each synced key's blob == HEAD blob |  | OPEN |

## Log

- 20260921T195750Z OPENED by 0.7.0_AE_CloudOps~V with 5 leg(s)
