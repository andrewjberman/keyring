# Deploy Completion Record
**Date opened:** 2026-10-16T23:10:17.303905+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-315: Cottonwood reporting-publish function irpt-cot-reporting-publish-lambda: ONE new bundle version (publisher 0.4.0, build-only hash vYNB1EBT..), plan 0 add 1 change 0 destroy on the function (code attributes only), ONE safe-apply, the pre-write read with its STOP lines, ONE dry run, a ONE-account canary, the FULL republish of 939 series and 939 manifests at the same keys (1878 served objects overwritten, prior versions kept); SERVED output moves; bound to the signed packet sha256 584a774339a1 (COO half @de90b2bb6f, CTO half @f78b555c93); rollback: prior artifact version 4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA through safe-apply and the prior version of each key; schedule stays DISABLED; nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source-map entry artifact_sha256 for irpt-cot-reporting-publish-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | artifact key investor-reporting/irpt-cot-reporting-publish-lambda.zip: a NEW VERSION (current 4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA is the rollback target) | new VersionId, landed sha256 equals the built zip equals vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE= |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-publish-iso plan exactly 0 add 1 change 0 destroy on the function by code attributes only | plan counts, naming gate, code hash equals the built zip, schedule DISABLED untouched, post-apply plan No changes |  | OPEN |
| L4 | verify | pre-write read inside its STOP lines then ONE dry run {}: uploaded false, published 939, refused inside 10 percent | pre_write counts, 200, within 819 MB and 720 s, object counts unchanged |  | OPEN |
| L5 | s3-prefix | ONE-account canary then the FULL republish {upload true}: 939 series and 939 manifests rewritten at the same keys (new versions) | canary seven checks true; full: published 939, claim 939, FULL count equals the flips, no value changed on a common day, prior versions kept |  | OPEN |
| L6 | verify | the after-read and the receipt | after, record and words file written, three criteria run |  | OPEN |

## Log

- 20261016T231017Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
