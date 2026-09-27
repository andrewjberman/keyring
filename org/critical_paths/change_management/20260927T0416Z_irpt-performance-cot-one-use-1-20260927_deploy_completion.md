# Deploy Completion Record
**Date opened:** 2026-09-27T04:16:28.378707+00:00
**Status:** OPEN
**Deploy:** COT one-use plan 22f0a988 (acc_81d92b2b.., 01-01..09-22 from served holdings, expires 18:00Z) in window 8 as K12: arm-OFF pre-check, arm (1/1/1), ONE use (= 2 BD requests), disarm; packet 27434c70 (halves pending); Andrew call 3 @6039c2f680
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P0 | verify | arm-OFF pre-check | HAR account/start/end == plan; adapter VendorEgressRefused, 0 vendor calls; recorded BEFORE the arm | arm-OFF pre-check (CTO c42d47163d, CRO 1dbf46c36b), recorded BEFORE the arm: ~D 101805 at 04:22Z, Cottonwood, ****0441 / BROKERAGE (a one-account client), GET performance/sel_66e6034cd164fb0f141b662babd962a65b17e37670281b4800c85a85ebd565e6?start=2026-01-01&end=2026-09-22&selected_tenant=cottonwood x2 (the tab + IV-e-40's chooser read); sel_66e6034c = the selection cot_one_use_plan.py read the end from; account, start, end == plan 22f0a988 (acc_81d92b2b.., 2026-01-01, 2026-09-22), 3 of 3; answer 200 UNAVAILABLE / DEPENDENCY_UNAVAILABLE 4,151 ms and 5,373 ms; adapter log 04:21:30-04:23:30Z: 2 invocations (db905e32, 805250a8), both path=refused:VendorEgressRefused 'matching current server-approved performance use required' (live plan = spent INF 7f64b166); irpt-requests cottonwood PERFORMANCE_USE# rows = only 106eaa0e (claimed 1790257673, 09-24, a prior plan), none for 22f0a988 -> 0 vendor calls; cottonwood REPORT# = 0. Card facts from ~D: WHO 'Sole Ownership' (a registration phrase), HOW MUCH -$40,348.28 (a negative client total; parked for ~D's read, not this ledger's). | CLOSED 20260927T042641Z |
| A1 | activation | arm | re-plan exactly 1/1/1 (COT session read added, env, INF session read destroyed); safe-apply; readback plan sha | after P0 @cd5c7bf068: re-plan with -var-file cot_plan1.tfvars.json read exactly 1/1/1 (add performance_approved_session[0] = irpt-performance-approved-session-policy; change the adapter env; destroy performance_approved_inf_session[0]); safe-apply 04:29:10Z 'Resources: 1 added, 1 changed, 1 destroyed'; readback: CodeSha256 Ll6t4VPa unchanged, Successful; env plan firm cottonwood acc_81d92b2b.. 2026-01-01..2026-09-22 exp 1790532000; egress digest 22f0a98881b6db96.. == recomputed plan sha; the session grant is ONE statement secretsmanager:GetSecretValue on blackdiamond/cot/session-jnzOyC; the role's inline policies no longer list an INF session read. | CLOSED 20260927T043019Z |
| K12 | verify | ONE COT read | PERFORMANCE_USE#22f0a988 claimed once; outcome; BD requests = 2 under one claim |  | OPEN |
| Z1 | verify | disarm | spent, or the spent INF plan 7f64b166 re-applied the same tick |  | OPEN |

## Log

- 20260927T041628Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260927T042641Z LEG P0 closed: arm-OFF pre-check (CTO c42d47163d, CRO 1dbf46c36b), recorded BEFORE the arm: ~D 101805 at 04:22Z, Cottonwood, ****0441 /
- 20260927T043019Z LEG A1 closed: after P0 @cd5c7bf068: re-plan with -var-file cot_plan1.tfvars.json read exactly 1/1/1 (add performance_approved_session[
