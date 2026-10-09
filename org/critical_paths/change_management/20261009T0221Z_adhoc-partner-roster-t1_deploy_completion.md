# Deploy Completion Record
**Date opened:** 2026-10-09T02:21:29.024483+00:00
**Status:** OPEN
**Deploy:** partner_roster T-1 into its two live readers: leg A bundles.accrual_bridge re-mint, leg B emitter vendored roster on a PINNED build (TO ADHOC.partner-roster-t1-into-live-readers, GO msg 1448, risk SERVED)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | opal-data-assets portal/gold/mdpf/_code/mdpf-accrual-bridge.tar.gz re-mint from HEAD via safe-deploy in-flow mint | new VersionId + TOOL-03/mint output line |  | OPEN |
| A2 | verify | head-object metadata roster-authority-sha256=4c104d9b.. script-sha256=648cf3f5.. unchanged | head-object Metadata read |  | OPEN |
| B0 | verify | CONTROL, NO WRITE: name the commit whose BUILD_ONLY emitter build reproduces live CodeSha256 n/Tu1ns1..; none -> STOP leg B | build sha256 base64 equality | PASS. Commit 9abdfa4c30 (the order's own starting candidate) reproduces the live CodeSha256 n/Tu1ns1eNl1vLBiR29ZttXGVjuzz5DAsjV5gBut/2k= EXACTLY, but ONLY with partner_roster.json at its committed LF bytes. Positive/negative control pair on the same tree and same script: CRLF-as-checked-out -> cxiWUYgfzn+OahvM0gAIMkf4sKPyO9oJew9Js2yKqN0= (no match); LF from the blob -> n/Tu1ns1.. (match). The build-script version is NOT a factor: the pre-BUILD_ONLY script at 9abdfa4c30 and the current script both yield cxiWUYgf.. on the CRLF input. | CLOSED 20261009T023646Z |
| B1 | verify | build = B0 tree with ONLY partner_roster.json replaced by HEAD bytes (LF); roster md5 3d309b26, every other member hash = B0 | per-member hash comparison | PASS. Build input = tree 9abdfa4c30 with ONLY partner_roster.json replaced by git show HEAD:data/mdpf/config/partner_roster.json (27433 bytes, 0 CRs, md5 3d309b267e6987b4f14250ed3d168d1a -- criterion 4's required 3d309b26..). B1 package sha256 GLQf6kv4nzRLGd53ONG4S5F4ikOso/2lkbq03U/+G9A=. Per-member comparison against the B0 zip: 5 members both sides, sets identical, SAME=4 DIFF=1 -- only partner_roster.json moved (b0 af44aaad.. -> b1 4c104d9bb8509b89.., the HEAD authority sha). PIN: 9abdfa4c30 + roster@HEAD; the four undeployed emitter commits (ae106b1124, aaf2be288f, 650df7371e, 85dd7adc26) are NOT in this build. | CLOSED 20261009T023647Z |
| B2 | activation | upload artifact + targeted plan 0/1/0 + safe-apply -target on the emitter module | plan counts + apply output | PASS. Artifact uploaded to s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-daily-emitter.zip version MONq1TwQ2OEsHx9.tHGRiXGXMEvyxyC. with the required stamp content-sha256=GLQf6kv4nzRLGd53ONG4S5F4ikOso/2lkbq03U/+G9A= (read back on head-object, exact). Targeted plan read exactly 0/1/0 -- 'Plan: 0 to add, 1 to change, 0 to destroy', sole resource module.emitter.aws_lambda_function.this updated in-place, sole attribute changes s3_object_version LEBxFtsuAQOsw4xcjeDepTZrRCj9CWAt -> MONq1TwQ.. and source_code_hash n/Tu1ns1.. -> GLQf6kv4.. plus last_modified (known after apply). Applied via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.emitter (Rule 18; never bare terraform apply). Rollback target preserved: artifact version LEBxFtsuAQOsw4xcjeDepTZrRCj9CWAt. | CLOSED 20261009T024425Z |
| B3 | verify | get-function-configuration CodeSha256 = the B1 build | CodeSha256 read | PASS. get-function-configuration opal-assets-daily-emitter CodeSha256 = GLQf6kv4nzRLGd53ONG4S5F4ikOso/2lkbq03U/+G9A=, EQUAL to the B1 build sha. LastModified 2026-10-09T02:43:17Z (was 2026-08-11T01:28:40Z). Runtime python3.11, Timeout 600, Memory 1024 -- all unchanged, confirming code-only movement. Targeted re-plan reads 'No changes. Your infrastructure matches the configuration.' (0-diff verification). | CLOSED 20261009T024425Z |
| B4 | verify | next scheduled opal-assets-daily-emitter-daily run cron(15 17 * * ? *): Cottonwood rows read declared_cadence T-1 | emitter row read after the 17:15Z run |  | OPEN |

## Log

- 20261009T022129Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)
- 20261009T023646Z LEG B0 closed: PASS. Commit 9abdfa4c30 (the order's own starting candidate) reproduces the live CodeSha256 n/Tu1ns1eNl1vLBiR29ZttXGVjuz
- 20261009T023647Z LEG B1 closed: PASS. Build input = tree 9abdfa4c30 with ONLY partner_roster.json replaced by git show HEAD:data/mdpf/config/partner_ros
- 20261009T024425Z LEG B2 closed: PASS. Artifact uploaded to s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-daily-emitter.zip version MON
- 20261009T024425Z LEG B3 closed: PASS. get-function-configuration opal-assets-daily-emitter CodeSha256 = GLQf6kv4nzRLGd53ONG4S5F4ikOso/2lkbq03U/+G9A=, EQ
