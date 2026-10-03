# Deploy Completion Record
**Date opened:** 2026-10-03T16:44:49.163567+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-4: opal-gateway app release 4231bd2ddc -> af2d762970 (audit fields, symmetric shared-value refusal, .env quoting, roster counts, Tax identity host-side) + rosters secret key taxsma_workbook_identity, via safe-ec2-deploy.sh from /c/tmp/og-rel9
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secret-key | verify | Secrets Manager gateway/principals/rosters gains taxsma_workbook_identity (value sha256 == host TAXSMA_WORKBOOK_IDENTITY) | new version id; new key sha256 MATCH host; every pre-existing key value hash unchanged |  | OPEN |
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-af2d762970.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref af2d762970; base guard declared 4231bd2ddc == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl4_verify.sh after: md5 94 of 94 = release bytes, health 200, 50 keys + 50 process value hashes unchanged, 3 own-bearer reads, rl4.AC1 tr.AC1 ht.AC2 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit af2d762970 previous 4231bd2ddc | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb9 at 4231bd2ddc equal to the live artifact, command + identity export recorded | diff -rq 97 of 97 equal (PHASE A) and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261003T164449Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
