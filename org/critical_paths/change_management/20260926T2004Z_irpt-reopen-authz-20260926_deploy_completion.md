# Deploy Completion Record
**Date opened:** 2026-09-26T20:04:22.428614+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T202150Z
**Deploy:** P-REOPEN-01: irpt-performance-adapter = live Zs2OK7C5 + entry.py @260399e940 + f49_engine.py @8d7a8b10fe; packet d01c36c4 (CTO SIGNOFF_REOPEN_AUTHZ_20260926.md, CRO @219f9450da); rollback artifact S3 version AHiiInq1WnKvFVFbQBqfaS0nFM.8N7ZN
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | before arm on the live code | reopen_authz_arm.py before: V1 ok past frontier; V2 OBJECT_NOT_COVERED (negative control); V0 refused; owner digest | reopen_authz_arm.py before on live Zs2OK7C5 (REOPEN_ARM_BEFORE_20260926.json): selection for 49F acc_0030c178..; V1 2026-01-01..2026-09-26 -> served PARTIAL/PERFORMANCE_PARTIAL, actual_end 2026-09-25 (past-frontier window), ref RPT-2b65b391de49902ae9b5fbe390648813, data sha256 d956115014a8..; V2 (second internal viewer) -> ok false UNAVAILABLE OBJECT_NOT_COVERED (the P-REOPEN-01 defect reproduced = negative control); V0 (49F advisor subject, no account) -> ok false NOT_AUTHORIZED, no data; owner row irpt-requests tenant 49financial owner_sha256 f0de54d8df291b26.. principal sha12 a2bdcb8898f7. Instrument fix before the after phase: compare keyed success on data present + no function error (a success envelope carries no ok key); arm meanings unchanged. | CLOSED 20260926T200634Z |
| D1 | activation | irpt-performance-adapter artifact + apply | census vs Zs2OK7C5: exactly entry.py + f49_engine.py; safe-apply; readback; import census; 0-diff replan | source map d25a491d9e (irpt-p-publish-20260923; entry.py pin 260399e940 sha 524d9bbf.., f49_engine.py pin 8d7a8b10fe sha d285eaf4..); build BAU_PARITY_SKIP=1 (the same 3 unpackaged dev tools build_candidate/build_dependencies/cot_probe as the D1 export build; the builder's deleted performance/*.py restored by git checkout); artifact 8a6zq+x9zpTqlI/n9I1SoSkZPkwvNtZ+N/NAOUcxDhk= 415216 bytes S3 version 3F8gPQNBK1o62ZnJ56EvJ0ZjgZeHawRL; census vs Zs2OK7C5: 69=69 members, exactly entry.py (524d9bbf..) + f49_engine.py (d285eaf4..) differ (CTO condition met). FIRST plan also showed destroy of performance_approved_inf_session[0] + removal of IRPT_PERFORMANCE_APPROVED_PLAN (the per-apply var not passed): NOT applied; re-planned with the live function's exact plan value (-var-file, egress digest verified equal) -> 0/1/0 code only; safe-apply 20:17:50Z; readback CodeSha256 8a6zq.. Active/Successful 1536 MB; invoke {} -> 200 CONTRACT_VERSION before and after; replan (same var) -detailed-exitcode 0 No changes | CLOSED 20260926T202150Z |
| A1 | verify | after arm + compare | reopen_authz_arm.py after + compare: 5 PASS or same-turn rollback to Zs2OK7C5 | reopen_authz_arm.py after + compare (REOPEN_ARM_AFTER_20260926.json): V1 past-frontier 01-01..09-26 served PARTIAL end 09-25 RPT-2b65b391.. data d956115014a8 (identical to before); V2 served, the SAME ref and data sha (before: OBJECT_NOT_COVERED); V0 ok false NOT_AUTHORIZED no data; owner row sha f0de54d8.. unchanged (principal sha12 a2bdcb8898f7 = V1); compare: 5 PASS, rc 0 -- no rollback | CLOSED 20260926T202150Z |
| T1 | verify | ruling A phase split | one irpt_engine_phases line from the fresh read, sent to the S147 card | fresh read V1 01-01..09-19 (RPT-b82626e9.., PARTIAL end 09-18), Lambda Duration 26729.57 ms: irpt_engine_phases {list_ms 99.2, map_ms 225.9, frame_ms 3685.4, link_ms 4.5, objects 181, bytes 51423897, get_ms_p50 92.8, p95 176.4, sum 18739.5, parse_ms_sum 36260.0, partitions 180, listed 559}: the engine read is ~4.0 s of 26.7 s; ~22.7 s is outside f49_engine.calculate. Sent to the S147 card. | CLOSED 20260926T202150Z |

## Log

- 20260926T200422Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260926T200634Z LEG B0 closed: reopen_authz_arm.py before on live Zs2OK7C5 (REOPEN_ARM_BEFORE_20260926.json): selection for 49F acc_0030c178..; V1 2026
- 20260926T202150Z LEG D1 closed: source map d25a491d9e (irpt-p-publish-20260923; entry.py pin 260399e940 sha 524d9bbf.., f49_engine.py pin 8d7a8b10fe sha
- 20260926T202150Z LEG A1 closed: reopen_authz_arm.py after + compare (REOPEN_ARM_AFTER_20260926.json): V1 past-frontier 01-01..09-26 served PARTIAL end 0
- 20260926T202150Z LEG T1 closed: fresh read V1 01-01..09-19 (RPT-b82626e9.., PARTIAL end 09-18), Lambda Duration 26729.57 ms: irpt_engine_phases {list_ms
- 20260926T202150Z CLOSED -- all 4 legs proven
