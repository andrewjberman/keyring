# Deploy Completion Record
**Date opened:** 2026-09-26T21:21:21.424063+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T213225Z
**Deploy:** S147 fix M: irpt-performance-adapter = live ZP7KM9Bc + entry.py @52604d790b (artifact Ll6t4VPa, S3 version 25meino2fa0XGNGJe2TLHHwYNT5M8qej); packet 20c3533c (CTO SIGNOFF_AUTHZ_MEMO_S147_20260926.md, CRO @4eacc1283f); rollback ZP7KM9Bc version y53kUE.NuNij7KiHVIr3Hop53Zf.hlwN
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | before arm on the live code | reopen_authz_arm before on ZP7KM9Bc | reopen_authz_arm.py before on ZP7KM9Bc (MEMO_ARM_BEFORE_20260926.json): V1 past-frontier served PARTIAL end 09-25 RPT-2b65b391.. data d956115014a8; V2 the same ref/data; V0 NOT_AUTHORIZED no data; owner sha f0de54d8.. | CLOSED 20260926T212345Z |
| D1 | activation | irpt-performance-adapter apply | code-only plan with the live INF plan value; safe-apply; readback; replan 0 | artifact Ll6t4VPa1cLWXyvr0IJdB9k5Ph+N2up2L/NYvgU4MAE= (S3 version 25meino2fa0XGNGJe2TLHHwYNT5M8qej; census vs ZP7KM9Bc: only entry.py, sha 7f92ad76..); plan with the live INF plan value (regenerated from the live env, egress digest verified; live CodeSha asserted ZP7KM9Bc) 0/1/0 code only; safe-apply 21:28:13Z; readback CodeSha256 Ll6t4VPa.. Active/Successful; replan -detailed-exitcode 0 | CLOSED 20260926T213224Z |
| A1 | verify | (b) reopen DELTA + (c) the four arms | compare 5 PASS + V1/V2 data identical to before, or same-turn rollback | (b)+(c) MEMO_ARM_BEFORE/AFTER_20260926.json: V1 past-frontier, V2 reopen, V0 refusal and owner digest IDENTICAL before (ZP7KM9Bc) and after (Ll6t4VPa) -> DELTA=0; compare: arms (1) V2 reopens, (2) V0 refused, (3) owner unchanged, (4) past-frontier identical all PASS; the compare's P-REOPEN-01 negative-control line ('before, V2 answered OBJECT_NOT_COVERED') FAILS by construction because this deploy's before is already the fixed code (before V2 served d956115014a8) -- an instrument premise, not a behaviour change; no rollback (reported to the CTO) | CLOSED 20260926T213224Z |
| T1 | verify | (d) three fresh reads re-timed | 3 new windows served, reports valid, timing lines | (d) three fresh windows served on Ll6t4VPa (01-01..09-09 RPT-a3774576.., 01-01..09-08 RPT-858feb75.., 01-01..09-05 RPT-9b0f6bb2.., all PARTIAL, contract-validated): Duration 6942 / 6415 / 6187 ms (was 25843-26861 ms); irpt_performance_timing: 64 authorize calls, 2 full releases, authorize sum 685-721 ms (was 20464), compute 5481-6269, release 332-365; irpt_retained_phases fresh: calculate 4612-5324, evidence_put 163-225, persist 201-212, readback 61-64. Reopens: 11 calls, 1 full, auth 355-387 ms, Duration 1181 ms warm (was 4262-9134 ms) | CLOSED 20260926T213224Z |

## Log

- 20260926T212121Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260926T212345Z LEG B0 closed: reopen_authz_arm.py before on ZP7KM9Bc (MEMO_ARM_BEFORE_20260926.json): V1 past-frontier served PARTIAL end 09-25 RPT-2b
- 20260926T213224Z LEG D1 closed: artifact Ll6t4VPa1cLWXyvr0IJdB9k5Ph+N2up2L/NYvgU4MAE= (S3 version 25meino2fa0XGNGJe2TLHHwYNT5M8qej; census vs ZP7KM9Bc: 
- 20260926T213224Z LEG A1 closed: (b)+(c) MEMO_ARM_BEFORE/AFTER_20260926.json: V1 past-frontier, V2 reopen, V0 refusal and owner digest IDENTICAL before (
- 20260926T213224Z LEG T1 closed: (d) three fresh windows served on Ll6t4VPa (01-01..09-09 RPT-a3774576.., 01-01..09-08 RPT-858feb75.., 01-01..09-05 RPT-9
- 20260926T213225Z CLOSED -- all 4 legs proven
