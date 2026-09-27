# Deploy Completion Record
**Date opened:** 2026-09-27T15:27:30.073336+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T154505Z
**Deploy:** ONE corrected COT use (IRPT_BCKEND-S157): plan 63cf95e9 (acc_81d92b2b.., 01-01..09-21, a stated end departure), direct IAM invoke as V1; arm 1/1/0, ONE read (= 2 BD requests), reopen, disarm to null 0/1/1; packet NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_S157_20260927.md; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P0 | verify | plan-off pre-check | 01-01..09-21 refused VendorEgressRefused, no report, 0 vendor calls -- recorded BEFORE the arm | plan-off pre-check 15:23:49Z (COT_S157_PRECHECK_PLAN3_20260927.json, cot_direct_read.py precheck ... 2026-09-21, V1 direct invoke): UNAVAILABLE/DEPENDENCY_UNAVAILABLE, no report; adapter log 15:23:4xZ path=refused:VendorEgressRefused 'matching current server-approved performance use required'; cottonwood PERFORMANCE_USE# rows 2 -> 2 (106eaa0e, 22f0a988) -> 0 vendor calls; the 01-01..09-21 window has no retained report (unlike 09-22, which reopens RPT-b683f188, 12:29:54Z). | CLOSED 20260927T152730Z |
| A1 | activation | arm | both halves at HEAD; re-plan exactly 1/1/0 (COT session read added, the two env keys); safe-apply; readback plan sha 63cf95e9 | both halves at HEAD naming blob 9c807347 (CTO @2d311d070f 101937: disarm to null the same tick whatever the outcome; name V1's report and claim in the release test-data item; CRO @6ae7ed831d 101939); re-plan with cot_plan3.tfvars.json read exactly 1/1/0 (add performance_approved_session[0] on the ONE COT session secret; change the env: the two keys); safe-apply 15:40:27Z 'Resources: 1 added, 1 changed, 0 destroyed'; readback CodeSha256 bOefL9nx unchanged Successful, env plan cottonwood 2026-01-01..2026-09-21, egress digest 63cf95e9defc == recomputed plan sha. | CLOSED 20260927T154504Z |
| K1 | verify | ONE COT read + reopen | PERFORMANCE_USE#63cf95e9 claimed once; BD requests = 2 (provider evidence); actual_start = first series point (expected 07-21); reopen = same report | ONE use SPENT, NO report (a named refusal; no retry per the terms). READ 15:40:57Z (COT_S157_READ_20260927.json, V1 direct invoke, 01-01..09-21): UNAVAILABLE/UNEXPECTED. Adapter 15:41:03Z: path=refused:BDRequestFailed 'provider request failed: HTTPError' (corr-dbfad6652d1f). PERFORMANCE_USE#63cf95e9.. claimed (cottonwood claims 2 -> 3). REOPEN 15:41:04Z (COT_S157_REOPEN_20260927.json): DEPENDENCY_UNAVAILABLE, adapter VendorEgressRefused 'performance use already spent or claim unavailable' (correct: spent, and no retained pointer since no report). BD requests under the claim: AT MOST 2 by construction (CottonwoodTransport consumes before I/O; the first request loads the COT session cookie and GETs the ClientView token, then POSTs performancePeriod) -- 1 token GET plus 0 or 1 performance POST; no provider evidence was retained on failure, so the exact count is not measured. Likely cause, NOT proven: the COT BD session (secret blackdiamond/cot/session AWSCURRENT created 2026-09-16) worked at 04:31Z (K12, RPT-b683f188) and was refused by 15:41Z -- an expired session answering a redirect or a 401 (urllib HTTPError under _NoRedirect). Cottonwood REPORT# 1 -> 1. S157 is NOT resolved: criterion 3 still has no real-data report from the fixed code. | CLOSED 20260927T154505Z |
| Z1 | verify | disarm to null | re-plan 0/1/1; safe-apply; env keys absent; no session grant | disarm to null the same tick (CTO 101937): re-plan with null-plan.tfvars.json read 0/1/1 (destroy performance_approved_session[0]; change the env); safe-apply 15:43:11Z 'Resources: 0 added, 1 changed, 1 destroyed'; readback CodeSha256 bOefL9nx Successful, IRPT_PERFORMANCE_APPROVED_PLAN and IRPT_PERF_VENDOR_EGRESS_AUTHORIZED absent; role inline policies with 'session' = 0. | CLOSED 20260927T154505Z |

## Log

- 20260927T152730Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260927T152730Z LEG P0 closed: plan-off pre-check 15:23:49Z (COT_S157_PRECHECK_PLAN3_20260927.json, cot_direct_read.py precheck ... 2026-09-21, V1 dire
- 20260927T154504Z LEG A1 closed: both halves at HEAD naming blob 9c807347 (CTO @2d311d070f 101937: disarm to null the same tick whatever the outcome; nam
- 20260927T154505Z LEG K1 closed: ONE use SPENT, NO report (a named refusal; no retry per the terms). READ 15:40:57Z (COT_S157_READ_20260927.json, V1 dire
- 20260927T154505Z LEG Z1 closed: disarm to null the same tick (CTO 101937): re-plan with null-plan.tfvars.json read 0/1/1 (destroy performance_approved_s
- 20260927T154505Z CLOSED -- all 4 legs proven
