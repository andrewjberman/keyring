# Deploy Completion Record
**Date opened:** 2026-09-24T20:12:05.632256+00:00
**Status:** OPEN
**Deploy:** irpt-directory-refresh: the same-frontier no-op re-dispatch fix (row IRPT_BCKEND-S125, 82679477a6)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_directory_refresh aws_lambda_function | census (exactly refresh.py, deployed == pre-fix blob); safe-apply 0/1/0; readback CodeSha256; 0-diff replan; recorder | fix 82679477a6; publish merge + source map bc5135f483; artifact d5fqVJ0fgAFDiL7VAQp3zcVKJXqA2dwGvfaOK1gWffQ= 42479 bytes S3 version OA7DE5C.aLUfImAVZK7JIPhwG.EIcTOJ; census vs deployed q7O3GGjK (09-19): 5 of 5 members, exactly refresh.py differs, deployed refresh.py == 82679477a6~1 blob, built == 82679477a6 blob; plan 0/1/0 (source_code_hash + s3_object_version); safe-apply 20:13:37Z; readback Active/Successful; replan rc=0 No changes; recorder ecd196e609 | CLOSED 20260924T201630Z |
| S1 | verify | next scheduled fire (09-25 09:00 ET) | both firms REFRESH_DISPATCHED with dispatched_for, then a completed build past 09-17 |  | OPEN |

## Log

- 20260924T201205Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260924T201630Z LEG A1 closed: fix 82679477a6; publish merge + source map bc5135f483; artifact d5fqVJ0fgAFDiL7VAQp3zcVKJXqA2dwGvfaOK1gWffQ= 42479 bytes
