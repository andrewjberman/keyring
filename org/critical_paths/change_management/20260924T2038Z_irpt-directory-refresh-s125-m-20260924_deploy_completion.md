# Deploy Completion Record
**Date opened:** 2026-09-24T20:38:50.727856+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T134024Z
**Deploy:** irpt-directory-refresh: every fire asks the runner once (row IRPT_BCKEND-S125; a7e5c59042 on P 82679477a6; Andrew-direct ~20:0xZ)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_directory_refresh aws_lambda_function | census (exactly refresh.py differs; deployed == 82679477a6 blob); build + upload; safe-apply 0/1/0; readback CodeSha256; 0-diff replan; rollback = artifact version OA7DE5C.aLUfImAVZK7JIPhwG.EIcTOJ (d5fqVJ0f) | fix a7e5c59042 on P 82679477a6; publish merge 568cee428e; artifact DXuzx9jpOPKOq+CjWwL36SumE5tRBZA/kfi3y5jKBgk= 43121 bytes S3 version M8O8zFhaS8YGlWPgya0PtiCIXfLSaTmR (source map 34494696c1, lane override IRPT_COMPLETION_SOURCE_MAP audited); census vs deployed d5fqVJ0f (OA7DE5C): 5 of 5 members, exactly refresh.py differs, deployed == 82679477a6 blob, built == a7e5c59042 blob; plan 0/1/0 (source_code_hash + s3_object_version); safe-apply 20:59:5xZ (HALT_ACK: 28 routine, 0 STOP); readback DXuzx9jp Active/Successful 20:59:50Z; replan rc=0 No changes; recorder bcca8b7c1c | CLOSED 20260924T210354Z |
| S1 | verify | one fire of the fixed function | each firm REFRESH_DISPATCHED (or COMPLETED+hand-over) with dispatched_for and fired_on; the served directory past 2026-09-17 at the next read | 09-25 13:30Z fire (schedule moved to 09:30 America/New_York by 2.0.0_SA_COO~P, S126 disarmed @61bce7ee33): each firm REFRESH_DISPATCHED RUNNING fired_on 2026-09-25 dispatched_for 2026-09-25 (49F cid 4237a59f, INF c23247b8, COT 771aae84); served latest.json rewritten 13:30:45-51Z -- 49F as_of 2026-09-24 (was 09-17) 4,620 entries, version dJypVohm; INF as_of 2026-09-25 292 entries, 6wQPRO8j; COT as_of 2026-09-22 258 entries, Hw0c7gyw. The 13:00Z fire before it ran the same fixed code and reached the dispatch at all 3 firms (REFRESH_FAILED HAND_OVER_RUNNER_OFFLINE, the host race S126) | CLOSED 20260925T134023Z |

## Log

- 20260924T203850Z OPENED by 2.0.0_SA_COO~M with 2 leg(s)
- 20260924T210354Z LEG A1 closed: fix a7e5c59042 on P 82679477a6; publish merge 568cee428e; artifact DXuzx9jpOPKOq+CjWwL36SumE5tRBZA/kfi3y5jKBgk= 43121 by
- 20260925T131636Z HELD-SOVEREIGN-GATED gate=external/S1 needs a refresh fire that finds mdpf-daily-runner i-02448edb624a7a7cf SSM-Onl
- 20260925T134023Z HOLD RELEASED -> OPEN
- 20260925T134023Z LEG S1 closed: 09-25 13:30Z fire (schedule moved to 09:30 America/New_York by 2.0.0_SA_COO~P, S126 disarmed @61bce7ee33): each firm REF
- 20260925T134024Z CLOSED -- all 2 legs proven
