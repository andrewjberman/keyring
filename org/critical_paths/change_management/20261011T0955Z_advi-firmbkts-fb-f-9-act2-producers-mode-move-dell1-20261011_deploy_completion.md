# Deploy Completion Record
**Date opened:** 2026-10-11T09:55:46.979659+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-9 phase B (window act 2): ship the 19 dormant gold .py objects and the dispatcher switch to s3://opal-data-bd/code/gold/, moving BD_PLATINUM_MODE to canonical for the scheduled production chain; pair COO half @12b22ef020 + ADDENDUM 1 @1d7f94ebb1, CTO half @03c1c6f001 + ADDENDA 1 @6ac66a8950 and 2 @3d24ccdbd2
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 2 reads: opal-data-bd versioning, the 20 keys' prior VersionIds, the actor's grants at object grain, the producers' role grant at the new home, the schedule, deployed-equal before-read | the entry carries the 20 rows and the read lines |  | OPEN |
| L2 | s3-prefix | s3://opal-data-bd/code/gold/ 19 .py objects: 14 writers (C_05 C_06 C_07 C_08 D_00 D_00b D_00c D_00f D_01 D_02 D_03 D_04 E_01 E_24) + lib/{platinum_dest,platinum_dest_view,gold_utils,helpers,etf_classifier}.py (step 3, HELD for the build-final amendment) | 19 of 19 read back equal to git show HEAD:<path> (sha256 per key) |  | OPEN |
| L3 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh -- the switch (step 4, HELD for the GO amendment), aws s3 cp --sse AES256 then cmp | cmp read-back equal, 0 bytes above 127, MOVE_TS recorded |  | OPEN |
| L4 | activation | the first SCHEDULED production chain after MOVE_TS (--chain, not --single, not QA) | the chain's exit and a run log with no ValueError and no NoSuchKey on a served read |  | OPEN |
| L5 | verify | AC1 deployed-equal 20 of 20, AC2 new-home 11 of 11 since MOVE_TS, AC3 old-home 0 keys of 11 classes since MOVE_TS | the three outputs of r3_act2_reads.py quoted |  | OPEN |
| L6 | git | proof instance written and TO-FB-f-9 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261011T095546Z OPENED by 0.7.0_AE_CloudOps~FB1 with 6 leg(s)
