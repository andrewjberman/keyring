# Deploy Completion Record
**Date opened:** 2026-10-12T13:40:56.795772+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-11 act 4 dell1 leg (GO @8cd6a18a3b): the eight IRPT consumers deploy the flipped loaders.py (re-pin e274a0e60c to flip commit 69679b90e3), BEFORE and AFTER authorization sample, first hour; pair COO 0a4d82ac06 + ADDENDA 1-2, CTO 507d3b3ce1 + ADDENDA 1-5; rollback by prior artifact object versions (no published versions exist) and act 2's gold_dispatch.sh prior VersionId
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair bytes and SIGNED; pre-flip reads r4_oai 3 of 3, r4_flipcommit 4 of 4, r4_repin 3 of 3 (detached worktree at e274a0e60c); authority at the 8 function ARNs; the eight current CodeSha256 values; CloudFront TTL read and named; producers' next chain start | each last line printed in the entry |  | OPEN |
| L2 | verify | BEFORE sample: SAMPLE_BEFORE.json, a granted and a refused viewer per side-effect-free function, status and body sha256 only; 5xx at baseline is a STOP | record count and status denominator |  | OPEN |
| L3 | s3-prefix | build-and-upload.sh investor-reporting for the eight functions (ycharts from branch scratch/r4-act4-ycharts-pin c4ca0c9a99 in a throwaway worktree); ACT4_EXPECT.json written; each hash printed beside the rehearsal | the eight artifact sha256 beside the rehearsal values |  | OPEN |
| L4 | activation | eight scoped plans, each changing the function's code hash only (s3_object_version, source_code_hash, last_modified); plan check script prints the attribute diff | each plan summary line and the attribute check |  | OPEN |
| L5 | activation | eight safe-apply on the saved plans, begun not before 13:45Z the same minute as the laptop leg; first and last unit apply times printed | the first and last apply times, each read-back CodeSha256 equals its artifact |  | OPEN |
| L6 | verify | AFTER sample SAMPLE_AFTER.json, r4_sample_eq.py all EQUAL, irpt-ycharts-generate same answers; irpt-performance-adapter invoked once and its evidence artifact KEY named not under a served class | the sample last line and the key |  | OPEN |
| L7 | verify | first hour: router behaviors origin responses (CloudFront metrics) over the first hour after the last unit, denominator printed; 403 or 404 is Branch B | the metric read and denominator |  | OPEN |
| L8 | verify | AC1 r4_act4.py --arms irpt 8 of 8; AC3 act-3 compare DEST-VS-MANIFEST EQUAL; platinum_dest_view.py shipped at close so FB-f-9 AC1 reads 20 of 20 | the three outputs quoted |  | OPEN |
| L9 | git | source-map artifact_* record committed (the M3 commit), proof instance written, TO-FB-f-11 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T134056Z OPENED by 0.7.0_AE_CloudOps~FB1 with 9 leg(s)
