# Deploy Completion Record
**Date opened:** 2026-09-26T20:36:29.208002+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T204548Z
**Deploy:** S147 second timing line (CTO 101487): irpt-performance-adapter = live 8a6zq+x9 + entry.py + retained.py @b18cb77c7d; timings only, DELTA=0 held by the reopen arm; rollback 8a6zq+x9 (S3 version 3F8gPQNBK1o62ZnJ56EvJ0ZjgZeHawRL)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | irpt-performance-adapter artifact + apply | census vs 8a6zq: exactly entry.py + retained.py; code-only plan with the live INF plan var; safe-apply; readback; replan 0 | source map bd07744930 (entry.py pin b18cb77c7d sha 92f1706f.., retained.py pin b18cb77c7d sha f0d0602e..; + the 8a6zq record); BAU_PARITY_SKIP=1 (same 3 unpackaged dev tools); builder-deleted performance/*.py restored; artifact ZP7KM9BcGz746f610VT4kGB1mfXQ3vfCa5UHJPLYqkU= 416188 bytes S3 version y53kUE.NuNij7KiHVIr3Hop53Zf.hlwN; census vs live 8a6zq: 69=69, exactly entry.py + retained.py differ; plan with the live INF plan value (-var-file regenerated from the live env, egress digest verified) 0/1/0 code only; safe-apply 20:43:23Z; readback CodeSha256 ZP7KM9Bc.. Active/Successful; replan (same var) -detailed-exitcode 0 | CLOSED 20260926T204547Z |
| Z1 | verify | DELTA=0 | reopen_authz_arm after-run on the new code vs REOPEN_ARM_AFTER_20260926.json: V1/V2 same ref + data sha, V0 refused | reopen_authz_arm.py after on ZP7KM9Bc (TIMING2_ARM_AFTER_20260926.json) vs REOPEN_ARM_AFTER_20260926.json on 8a6zq: V1, V2, V0 identical on function_error/ok/state/reason/retained_ref/data_sha256/actual_end; owner digest identical -> DELTA=0 | CLOSED 20260926T204547Z |
| T1 | verify | the two timing lines | one fresh read logs irpt_performance_timing + irpt_retained_phases; the re-ranked card to the CTO | fresh read 01-01..09-17 (RPT-d1662e49.., Duration 25842.94 ms): irpt_performance_timing authorize_calls 64, each 301-365 ms, sum 20463.8 ms, compute 25220.2, select 149.6, release (in list); irpt_retained_phases fresh: prepare 315, calculate 4379 (engine frame 3683), evidence_put 4450, retention_promote 1909, persist 7544, readback 3290, reopen 3323; reopens (Duration 4.3-8.0 s): authorize_calls 11, sum 3458-3546 ms. Re-ranked card to the CTO. | CLOSED 20260926T204548Z |

## Log

- 20260926T203629Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T204547Z LEG D1 closed: source map bd07744930 (entry.py pin b18cb77c7d sha 92f1706f.., retained.py pin b18cb77c7d sha f0d0602e..; + the 8a6zq re
- 20260926T204547Z LEG Z1 closed: reopen_authz_arm.py after on ZP7KM9Bc (TIMING2_ARM_AFTER_20260926.json) vs REOPEN_ARM_AFTER_20260926.json on 8a6zq: V1, 
- 20260926T204548Z LEG T1 closed: fresh read 01-01..09-17 (RPT-d1662e49.., Duration 25842.94 ms): irpt_performance_timing authorize_calls 64, each 301-365
- 20260926T204548Z CLOSED -- all 3 legs proven
