# Deploy Completion Record
**Date opened:** 2026-09-27T05:09:25.184602+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T052351Z
**Deploy:** irpt-performance-adapter code-only: COT actual_start = the account's first series point (backend 05778597eb); plan stays null; DELTA=0 on every reachable surface (49F arms, reopens; COT/INF fresh refused without a plan)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | before arms on Ll6t4VPa | reopen_authz_arm.py before (V1/V2/V0 + past-frontier) recorded before the build | reopen_authz_arm.py before on live Ll6t4VPa (WINDOW_FIX_ARM_BEFORE_20260927.json): V1 2026-01-01..09-26 PARTIAL end 09-25 RPT-2b65b391.. data d956115014a8; V2 the same ref and data; V0 UNAVAILABLE NOT_AUTHORIZED, no data; 49F owner sha f0de54d8.. | CLOSED 20260927T051120Z |
| D1 | activation | irpt-performance-adapter apply | zip census vs Ll6t4VPa = bd_selected.py only; plan with the null var-file 0/1/0 code only; safe-apply; readback CodeSha + env still no plan; replan 0 | publish tree: cherry-pick of backend 05778597eb = f360e6c80e; lambda-source-map bd_selected.py pin b905df2c60 -> f360e6c80e33.. sha256 18526628.. (the first build with the old pin produced a byte-identical Ll6t4VPa zip: the build stages files from their PINS, not the checkout -- caught by the census, never applied); BAU_PARITY_SKIP=1 as f9c91a554d (build_candidate.py/build_dependencies.py/cot_probe.py are tooling, absent from the live zip); artifact bOefL9nxk9EdN8l0sf636+eGWX43OH06WuZ19O7E6lw= (S3 version 8uohgNwEsCt4KPOXk1sJ6.4SG8NTTmWf); census vs Ll6t4VPa: 69/69 entries, only bd_selected.py changed; plan with null-plan.tfvars.json 0/1/0 code only (s3_object_version + source_code_hash); safe-apply 05:22:03Z; readback CodeSha256 bOefL9nx.. Active/Successful, IRPT_PERFORMANCE_APPROVED_PLAN and IRPT_PERF_VENDOR_EGRESS_AUTHORIZED absent; replan -detailed-exitcode 0. The build deleted tracked performance/*.py in the publish tree twice (parked trap); restored by git checkout each time. | CLOSED 20260927T052351Z |
| A1 | verify | DELTA=0 + the change | reopen_authz_arm after + compare all PASS with V1/V2 data identical; replay of RPT-b683f188's recorded provider bytes through the DEPLOYED zip's bd_selected gives actual 2026-07-21; or same-turn rollback to Ll6t4VPa | WINDOW_FIX_ARM_BEFORE/AFTER_20260927.json: V1 past-frontier PARTIAL RPT-2b65b391.. data d956115014a8 and V2 reopen the same, V0 NOT_AUTHORIZED no data, owner f0de54d8.. -- IDENTICAL before (Ll6t4VPa) and after (bOefL9nx) -> DELTA=0; compare arms (1)-(4) PASS; its negative-control line FAILS by construction (before already runs the fixed reopen code, as at irpt-authz-memo). After-phase fresh 49F window 01-01..09-19 PARTIAL RPT-b82626e9.. contract-valid. COT/INF fresh: refused without a plan (none armed). The change: replay of RPT-b683f188's recorded provider bytes (ART-36a64d88) through the extracted DEPLOYED zip: actual 2026-07-21..09-22 (series 45, 07-21..09-22); through the Ll6t4VPa zip: actual 2026-01-02..09-22 (~D's face). No rollback. | CLOSED 20260927T052351Z |

## Log

- 20260927T050925Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T051120Z LEG B0 closed: reopen_authz_arm.py before on live Ll6t4VPa (WINDOW_FIX_ARM_BEFORE_20260927.json): V1 2026-01-01..09-26 PARTIAL end 09-2
- 20260927T052351Z LEG D1 closed: publish tree: cherry-pick of backend 05778597eb = f360e6c80e; lambda-source-map bd_selected.py pin b905df2c60 -> f360e6c
- 20260927T052351Z LEG A1 closed: WINDOW_FIX_ARM_BEFORE/AFTER_20260927.json: V1 past-frontier PARTIAL RPT-2b65b391.. data d956115014a8 and V2 reopen the s
- 20260927T052351Z CLOSED -- all 3 legs proven
