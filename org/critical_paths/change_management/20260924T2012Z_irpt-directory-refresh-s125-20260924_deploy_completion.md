# Deploy Completion Record
**Date opened:** 2026-09-24T20:12:05.632256+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T210533Z
**Deploy:** irpt-directory-refresh: the same-frontier no-op re-dispatch fix (row IRPT_BCKEND-S125, 82679477a6)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_directory_refresh aws_lambda_function | census (exactly refresh.py, deployed == pre-fix blob); safe-apply 0/1/0; readback CodeSha256; 0-diff replan; recorder | fix 82679477a6; publish merge + source map bc5135f483; artifact d5fqVJ0fgAFDiL7VAQp3zcVKJXqA2dwGvfaOK1gWffQ= 42479 bytes S3 version OA7DE5C.aLUfImAVZK7JIPhwG.EIcTOJ; census vs deployed q7O3GGjK (09-19): 5 of 5 members, exactly refresh.py differs, deployed refresh.py == 82679477a6~1 blob, built == 82679477a6 blob; plan 0/1/0 (source_code_hash + s3_object_version); safe-apply 20:13:37Z; readback Active/Successful; replan rc=0 No changes; recorder ecd196e609 | CLOSED 20260924T201630Z |
| S1 | verify | next scheduled fire (09-25 09:00 ET) | both firms REFRESH_DISPATCHED with dispatched_for, then a completed build past 09-17 | SUPERSEDED 21:0xZ: 2.0.0_SA_COO~M deployed its S125 fix a7e5c59042 on top of 82679477a6 as irpt-directory-refresh DXuzx9jp at 20:59:50Z (ledger irpt-directory-refresh-s125-m-20260924, M msg 100889; M's multi-day drive: 82679477a6 alone dispatched 6 of 16 fires with 5 false TRIGGER_MISSED, the combined fix 16 of 16, 0 missed). The served artifact this ledger verified (d5fqVJ0f) is replaced; the next-fire proof is M's ledger's S1. Nothing re-executed. | CLOSED 20260924T210533Z |

## Log

- 20260924T201205Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260924T201630Z LEG A1 closed: fix 82679477a6; publish merge + source map bc5135f483; artifact d5fqVJ0fgAFDiL7VAQp3zcVKJXqA2dwGvfaOK1gWffQ= 42479 bytes
- 20260924T210533Z LEG S1 closed: SUPERSEDED 21:0xZ: 2.0.0_SA_COO~M deployed its S125 fix a7e5c59042 on top of 82679477a6 as irpt-directory-refresh DXuzx9
- 20260924T210533Z CLOSED -- all 2 legs proven
