# Deploy Completion Record
**Date opened:** 2026-10-16T23:10:17.303905+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T235000Z
**Deploy:** IRPT_DASHBD TO-DB-b-315: Cottonwood reporting-publish function irpt-cot-reporting-publish-lambda: ONE new bundle version (publisher 0.4.0, build-only hash vYNB1EBT..), plan 0 add 1 change 0 destroy on the function (code attributes only), ONE safe-apply, the pre-write read with its STOP lines, ONE dry run, a ONE-account canary, the FULL republish of 939 series and 939 manifests at the same keys (1878 served objects overwritten, prior versions kept); SERVED output moves; bound to the signed packet sha256 584a774339a1 (COO half @de90b2bb6f, CTO half @f78b555c93); rollback: prior artifact version 4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA through safe-apply and the prior version of each key; schedule stays DISABLED; nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source-map entry artifact_sha256 for irpt-cot-reporting-publish-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded | source-map commit (artifact_sha256 only: vYNB1EBT.. replaces HDgIzQoX..) and this ledger's records committed with the closing commit | CLOSED 20261016T233626Z |
| L2 | s3-prefix | artifact key investor-reporting/irpt-cot-reporting-publish-lambda.zip: a NEW VERSION (current 4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA is the rollback target) | new VersionId, landed sha256 equals the built zip equals vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE= | build-only sha256 vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE= equals the packet; import smoke rc 0 (13 members); real upload landed NEW VersionId 9bcRGHxD1DRHTBY0_cfD9ZL2mnjBnARe (before 4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA kept as rollback); landed bytes sha256 equal the built zip bd8341d4 | CLOSED 20261016T233626Z |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-publish-iso plan exactly 0 add 1 change 0 destroy on the function by code attributes only | plan counts, naming gate, code hash equals the built zip, schedule DISABLED untouched, post-apply plan No changes | plan 0 add 1 change 0 destroy on module.irpt_reporting_publish_iso.aws_lambda_function.this (last_modified, s3_object_version 4wX9zhqX..->9bcRGHxD.., source_code_hash GagDGBNG..->vYNB1EBT..); naming gate PASS 7 graded; ONE safe-apply 23:18:20Z-23:20:17Z Apply complete 0/1/0; function CodeSha256 vYNB1EBT.. memory 1024 timeout 900 no reserved concurrency one layer no env; schedule DISABLED untouched; post-apply plan No changes; fmt -check flags pinned iam.tf (not edited) | CLOSED 20261016T232309Z |
| L4 | verify | pre-write read inside its STOP lines then ONE dry run {}: uploaded false, published 939, refused inside 10 percent | pre_write counts, 200, within 819 MB and 720 s, object counts unchanged | pre-write read inside its STOP lines (PARTIAL to FULL 102, FULL to PARTIAL 0, series gaining a day 826, changed total_return 657 and external_flow 659, value/income/price return 0, refused 0, published 939); dry run {}: status 200, uploaded false published 939 refused 40, 10816 ms, 304 MB, object counts unchanged | CLOSED 20261016T233626Z |
| L5 | s3-prefix | ONE-account canary then the FULL republish {upload true}: 939 series and 939 manifests rewritten at the same keys (new versions) | canary seven checks true; full: published 939, claim 939, FULL count equals the flips, no value changed on a common day, prior versions kept | canary (one account hash12 01030e0f8a3a): published 1 refused 0, seven checks true; full republish {upload true} 23:25:48Z: status 200, published 939 refused 40, 87054 ms, 309 MB; 939 series and 939 manifests at the same keys, claim 939, FULL 102 equal to the flips, partial 837, every manifest publisher 0.4.0, 0 series changed value on a common day against the original version, prior versions kept on every key, ten sampled series checked | CLOSED 20261016T233627Z |
| L6 | verify | the after-read and the receipt | after, record and words file written, three criteria run | after-read: function vYNB1EBT.. memory 1024 timeout 900 no reserved concurrency; schedule DISABLED; DBC182-1/2/3 PASS; record and words file written; ledger NOT closed (the issuer closes) | CLOSED 20261016T233627Z |

## Log

- 20261016T231017Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261016T232309Z LEG L3 closed: plan 0 add 1 change 0 destroy on module.irpt_reporting_publish_iso.aws_lambda_function.this (last_modified, s3_object_ve
- 20261016T233626Z LEG L1 closed: source-map commit (artifact_sha256 only: vYNB1EBT.. replaces HDgIzQoX..) and this ledger's records committed with the cl
- 20261016T233626Z LEG L2 closed: build-only sha256 vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE= equals the packet; import smoke rc 0 (13 members); real u
- 20261016T233626Z LEG L4 closed: pre-write read inside its STOP lines (PARTIAL to FULL 102, FULL to PARTIAL 0, series gaining a day 826, changed total_re
- 20261016T233627Z LEG L5 closed: canary (one account hash12 01030e0f8a3a): published 1 refused 0, seven checks true; full republish {upload true} 23:25:4
- 20261016T233627Z LEG L6 closed: after-read: function vYNB1EBT.. memory 1024 timeout 900 no reserved concurrency; schedule DISABLED; DBC182-1/2/3 PASS; r
- 20261016T235000Z CLOSED -- all 6 legs proven
