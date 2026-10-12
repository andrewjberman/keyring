# Deploy Completion Record
**Date opened:** 2026-10-12T06:15:17.547213+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-9 phase B (window act 2, the GO @f5da2fc917 AMENDMENT 13): ship the 19 dormant gold .py objects, then gold_dispatch.sh (the switch), to s3://opal-data-bd/code/gold/; MOVE_TS recorded; pair COO half @12b22ef020 + ADDENDA 1 to 3 (ADDENDUM 2 @3c47103dc7, ADDENDUM 3), CTO half @03c1c6f001 + ADDENDA 1 to 4; rollback = the export and the guard removed by re-uploading the recorded prior gold_dispatch.sh version; ROLLS BACK THE SAME HOUR if act 4 cannot land before the next scheduled chain (Mon 23:00Z fallback); a hand run of E_24 exports BD_PLATINUM_MODE=canonical or it writes the legacy home (E_24 now refuses an unset mode, FB-g-7)
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 and 2 reads, fresh: pair bytes and SIGNED, opal-data-bd versioning, the 20 keys' prior VersionIds, ownership-map baseline (legacy VersionId FcsnGhU7Rt280E9rmDacateI5WiK8S28), the schedule and no run in flight, the role grant, the dispatcher diff | the entry carries the 20 rows and the read lines |  | OPEN |
| L2 | s3-prefix | s3://opal-data-bd/code/gold/ 19 .py objects (14 writers + 5 lib) shipped through .tools/safe-deploy.sh and read back (step 3) | 19 of 19 equal git show HEAD:<path>, sha256 per key |  | OPEN |
| L3 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh -- the switch (step 4), aws s3 cp --sse AES256 then cmp, MOVE_TS read after the copy returned | cmp equal, 0 bytes above 127, MOVE_TS printed, ownership-map baseline re-printed |  | OPEN |
| L4 | verify | AC1 deployed-equal 20 of 20 and the legacy-quiet read old-home --since MOVE_TS (it must name exec_summary.json among the classes it covers) | the two outputs quoted |  | OPEN |
| L5 | activation | the first SCHEDULED production chain AFTER act 4 (step 5): exit, run log with no ValueError and no NoSuchKey on a served read (a read after the issuer's act 4, not before) | the chain evidence |  | OPEN |
| L6 | verify | AC2 new-home 11 of 11 since MOVE_TS and AC3 old-home 0 keys of 11 classes since MOVE_TS, read after that chain | the outputs of r3_act2_reads.py quoted |  | OPEN |
| L7 | git | proof instance written and TO-FB-f-9 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T061517Z OPENED by 0.7.0_AE_CloudOps~FB1 with 7 leg(s)
