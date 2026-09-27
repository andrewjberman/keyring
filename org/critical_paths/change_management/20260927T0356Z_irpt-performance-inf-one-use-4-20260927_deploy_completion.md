# Deploy Completion Record
**Date opened:** 2026-09-27T03:56:50.658472+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T041346Z
**Deploy:** INF Orion one-use plan 7f64b166 (acc_5510a.., 01-01..09-22 from served holdings, expires 12:00Z) in window 8: arm-OFF pre-check, arm, ONE read, disarm (packet e2462004 W8-1; Andrew call 2 @6039c2f680)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P0 | verify | arm-OFF pre-check | HAR: account, start, end == the plan; adapter VendorEgressRefused, 0 vendor calls -- recorded BEFORE the arm (CTO c42d47163d, CRO 1dbf46c36b) | arm-OFF pre-check (CTO c42d47163d, CRO 1dbf46c36b), recorded BEFORE the arm: ~D 101785 at 04:03:24Z, Inflection, GET performance/sel_366d48915cb564219ef3623da3827b40edb0c8c8728e82f2d89e65486be734b2?start=2026-01-01&end=2026-09-22&selected_tenant=inflection (sel_366d4891 = the one-account selection of acc_5510a..): account, start, end == plan 7f64b166 (acc_5510a.., 2026-01-01, 2026-09-22), 3 of 3; answer 200 UNAVAILABLE / DEPENDENCY_UNAVAILABLE ~5.5 s; adapter log 04:03:25Z x2 VendorEgressRefused 'matching current server-approved performance use required' (the page fires TWO identical GETs 21 ms apart: the tab's read + IV-e-40's chooser read); INF PERFORMANCE_USE rows = only 01209afb -> 0 vendor calls. P's ruling on the double GET: authorization.py:91-102 claims PERFORMANCE_USE#<sha> by a conditional put (attribute_not_exists) BEFORE the vendor call, so of two concurrent matching reads exactly one wins and makes ONE Orion request; the other is refused 'already spent' with 0 vendor calls -> exactly 1 Orion call holds. | CLOSED 20260927T040628Z |
| A1 | activation | arm | re-plan 0/1/0 exactly 2 env keys; safe-apply; readback plan sha | after P0: re-plan with -var-file INF_ONE_USE_PLAN_4 0/1/0, exactly IRPT_PERFORMANCE_APPROVED_PLAN + IRPT_PERF_VENDOR_EGRESS_AUTHORIZED; safe-apply 04:08:59Z; readback CodeSha256 Ll6t4VPa unchanged Successful, env plan sha 7f64b166f58e.. with the egress digest equal | CLOSED 20260927T040932Z |
| K11 | verify | ONE read | PERFORMANCE_USE#7f64b166 claimed once; the outcome; exactly 1 Orion call across call 2 | ~D 101793: 2 GETs start=2026-01-01 end=2026-09-22 selected_tenant=inflection: 04:11:13Z 200 UNAVAILABLE/DEPENDENCY_UNAVAILABLE 5,001 ms (the tab's read, lost the claim: adapter 04:11:14Z VendorEgressRefused 'performance use already spent or claim unavailable'); 04:11:17Z 200 PARTIAL/PERFORMANCE_PARTIAL RPT-df47a1fc25f8b1895b7ef2b8407d7117, 9,759 ms (IV-e-40's read won: irpt_retained_phases path=fresh calculate 3694 ms). PERFORMANCE_USE#7f64b166.. claimed_at 1790482274 (04:11:14Z) -- ONE claim; INF REPORT# 0 -> 1 (REPORT#RPT-df47a1fc..#f1207846..), traced to the HAR response. Orion calls across Andrew's call 2 in total: exactly 1 (plans 3/4 before: 0). INF's FIRST signed-in retained Performance report (criterion 1 at INF). | CLOSED 20260927T041346Z |
| Z1 | verify | disarm | spent, or the spent 01209afb re-applied the same tick | the plan is SPENT at the claim (04:11:14Z): the gate refuses every further matching read ('already spent'); a same-window reopen serves the retained report via the PERFORMANCE_ACCEPTED pointer with 0 vendor calls. The env keeps the spent 7f64b166 until the COT arm (packet pending) replaces it; nothing re-applied. | CLOSED 20260927T041346Z |

## Log

- 20260927T035650Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260927T040628Z LEG P0 closed: arm-OFF pre-check (CTO c42d47163d, CRO 1dbf46c36b), recorded BEFORE the arm: ~D 101785 at 04:03:24Z, Inflection, GET per
- 20260927T040932Z LEG A1 closed: after P0: re-plan with -var-file INF_ONE_USE_PLAN_4 0/1/0, exactly IRPT_PERFORMANCE_APPROVED_PLAN + IRPT_PERF_VENDOR_EGR
- 20260927T041346Z LEG K11 closed: ~D 101793: 2 GETs start=2026-01-01 end=2026-09-22 selected_tenant=inflection: 04:11:13Z 200 UNAVAILABLE/DEPENDENCY_UNAVA
- 20260927T041346Z LEG Z1 closed: the plan is SPENT at the claim (04:11:14Z): the gate refuses every further matching read ('already spent'); a same-windo
- 20260927T041346Z CLOSED -- all 4 legs proven
