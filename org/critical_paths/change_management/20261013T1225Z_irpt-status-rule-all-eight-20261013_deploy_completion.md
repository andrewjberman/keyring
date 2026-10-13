# Deploy Completion Record
**Date opened:** 2026-10-13T12:25:04.201173+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R20: status rule (_authz/served.py 564e604838) into eight packagers, ops/status.py e93258c650 into irpt-status only; code only, eight scoped applies; pair COO blob 8eccf7b90a + CTO half @67cadd141d
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0: eight live CodeSha256 + S3 latest version + object hash equal table; patch hash-objects; guard at bases; open-entry denominator | reads and denominator printed |  | OPEN |
| L2 | verify | act-4 sampler SAMPLE_BEFORE (14 records) or ABSENT with reason | records or ABSENT |  | OPEN |
| L3 | s3-prefix | per function: detached worktree at base, guard, release patch, BUILD_ONLY digest equals EXPECTED, then upload and read back | eight digests equal EXPECTED, eight new object versions read back equal |  | OPEN |
| L4 | verify | per function scoped plan: 0 add 1 change 0 destroy, last_modified s3_object_version source_code_hash only | eight plan summary lines |  | OPEN |
| L5 | activation | safe-apply on each saved plan, A1 and A2 per unit | eight Apply complete 0/1/0 and live CodeSha256 equals EXPECTED |  | OPEN |
| L6 | verify | SAMPLE_AFTER and A3 equality or ABSENT | EQUAL 14 of 14 or ABSENT |  | OPEN |
| L7 | verify | A4: first-hour INTERNAL-CALLER-CLASS counts by class and outcome with denominator, sent to CTO and COO | counts |  | OPEN |
| L8 | verify | A1 to A5 file L8_AFTER_R20.txt | eight A1 lines and A2-A5 |  | OPEN |
| L9 | git | eight release diffs applied to trunk map plus artifact_* and last_deployed_*; commit | commit hash |  | OPEN |

## Log

- 20261013T122504Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 9 leg(s)
