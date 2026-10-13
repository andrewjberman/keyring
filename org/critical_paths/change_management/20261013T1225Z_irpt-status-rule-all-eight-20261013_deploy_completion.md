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
| L1 | verify | step 0: eight live CodeSha256 + S3 latest version + object hash equal table; patch hash-objects; guard at bases; open-entry denominator | reads and denominator printed | Step 0: pair COO blob 8eccf7b90a verified; 8 of 8 release patch hash-objects equal the table; guard (BUILD_ONLY) 8 mentions at e274a0e60c, 5d8b0390ed, 4067c2dd5b; live CodeSha256 equal table col 2 for 8 of 8; key latest equals col 3 and object hash equals live for 7 of 8. 49f: the table named the wrong key (irpt-49f-reporting-read-lambda.zip); the real key irpt-reporting-read-lambda.zip latest ZHCEj380 hashes to live IhlTVtU9; reported, AMENDMENT 1 + CTO ADDENDUM 1 (blob b90b590cb3) name ZHCEj380 as rollback. Denominator: 44 worktrees, 100 unique open entries, 13 name a function, all 13 CLOSED on trunk. Record units/R0B_step0_reads.py | CLOSED 20261013T131243Z |
| L2 | verify | act-4 sampler SAMPLE_BEFORE (14 records) or ABSENT with reason | records or ABSENT | ABSENT: the act-4 sampler draws viewers from the ownership maps (identities) and this order bounds forbid reading identities; A1 and A2 stand (pair section 5). | CLOSED 20261013T131243Z |
| L3 | s3-prefix | per function: detached worktree at base, guard, release patch, BUILD_ONLY digest equals EXPECTED, then upload and read back | eight digests equal EXPECTED, eight new object versions read back equal | 8 of 8 BUILD_ONLY digests equal EXPECTED before any upload (detached sparse worktrees at the base commits, release patch applied uncommitted, guard checked at base and in the worktree copy); 8 new object versions uploaded and read back byte-equal (sha256 of each downloaded version equals EXPECTED). The script's own head-object verify errors on this CLI (query error); object hash and size verified by hand. Logs in units/. | CLOSED 20261013T131243Z |
| L4 | verify | per function scoped plan: 0 add 1 change 0 destroy, last_modified s3_object_version source_code_hash only | eight plan summary lines | 8 of 8 scoped plans: Plan: 0 to add, 1 to change, 0 to destroy; attributes last_modified, s3_object_version, source_code_hash only (environment not in the diff). Logs units/plan_*.txt | CLOSED 20261013T131244Z |
| L5 | activation | safe-apply on each saved plan, A1 and A2 per unit | eight Apply complete 0/1/0 and live CodeSha256 equals EXPECTED | 8 of 8 safe-apply on the saved plan: Apply complete 0 added 1 changed 0 destroyed (seat-gates ADMITTED, comp-tagauthz PASSED, crossbox-deploy-check no verdict rc=124 in WARN mode); A1 TRUE and A2 TRUE for 8 of 8; no aws lambda update-function-code used. Last apply ended 13:07:25Z. | CLOSED 20261013T131244Z |
| L6 | verify | SAMPLE_AFTER and A3 equality or ABSENT | EQUAL 14 of 14 or ABSENT | A3 ABSENT with reason (see L2); no SAMPLE_AFTER taken. A1 and A2 stand. | CLOSED 20261013T131244Z |
| L7 | verify | A4: first-hour INTERNAL-CALLER-CLASS counts by class and outcome with denominator, sent to CTO and COO | counts |  | OPEN |
| L8 | verify | A1 to A5 file L8_AFTER_R20.txt | eight A1 lines and A2-A5 | L8_AFTER_R20.txt written: 8 A1 lines, A2 8 of 8, A3 ABSENT, A5 28 of 28 envelopes carry CORRECT with words; ar20_checks.py y218-apply prints Y218-APPLY-OK. | CLOSED 20261013T131244Z |
| L9 | git | eight release diffs applied to trunk map plus artifact_* and last_deployed_*; commit | commit hash | Map record commit c7756279dd on scratch branch aq2-r20-map (own worktree), merged to box/dell2 as 8aebb08499 via safe-merge (LOCAL; push not made by this seat). Net diff lambda-source-map.json only: 8 of 235 entries; the eight release diffs applied cleanly (served.py rows, and the status.py row of irpt-status) plus artifact_sha256, last_deployed_commit, last_deployed_at, deploy_ledger, deployed_code_sha256 per function; verified by parsed old-vs-new comparison. | CLOSED 20261013T132020Z |

## Log

- 20261013T122504Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 9 leg(s)
- 20261013T131243Z LEG L1 closed: Step 0: pair COO blob 8eccf7b90a verified; 8 of 8 release patch hash-objects equal the table; guard (BUILD_ONLY) 8 menti
- 20261013T131243Z LEG L2 closed: ABSENT: the act-4 sampler draws viewers from the ownership maps (identities) and this order bounds forbid reading identi
- 20261013T131243Z LEG L3 closed: 8 of 8 BUILD_ONLY digests equal EXPECTED before any upload (detached sparse worktrees at the base commits, release patch
- 20261013T131244Z LEG L4 closed: 8 of 8 scoped plans: Plan: 0 to add, 1 to change, 0 to destroy; attributes last_modified, s3_object_version, source_code
- 20261013T131244Z LEG L5 closed: 8 of 8 safe-apply on the saved plan: Apply complete 0 added 1 changed 0 destroyed (seat-gates ADMITTED, comp-tagauthz PA
- 20261013T131244Z LEG L6 closed: A3 ABSENT with reason (see L2); no SAMPLE_AFTER taken. A1 and A2 stand.
- 20261013T131244Z LEG L8 closed: L8_AFTER_R20.txt written: 8 A1 lines, A2 8 of 8, A3 ABSENT, A5 28 of 28 envelopes carry CORRECT with words; ar20_checks.
- 20261013T132020Z LEG L9 closed: Map record commit c7756279dd on scratch branch aq2-r20-map (own worktree), merged to box/dell2 as 8aebb08499 via safe-me
