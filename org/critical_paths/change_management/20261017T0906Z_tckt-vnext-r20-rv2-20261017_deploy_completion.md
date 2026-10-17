# Deploy Completion Record
**Date opened:** 2026-10-17T09:06:35.588126+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T091537Z
**Deploy:** TCKT_VNEXT TO-R20-RV2 (AMENDMENT 1, GO msg 10445; run pair AMENDMENT 6): read-only RE-SHOT of the completed meeting ticket TCK-20261017-da2a1987 on the fixed DEV build; the CTO's 5174 server (worktree C:/dev/smoke-template-5174) moved from 38d4f9473284 to 539b1ee70ba1 under the CTO's msg 10441; ONE synthetic filer tckt-r20-filer-20261017@opal.invalid (allowedFirmIds [cottonwood]); ONE shot filer_completed; surfaces: opal-users-v2 (one row), 5174 server, ticket service read; pair blobs 7e96f36b11 / b427f42ef2, check af25604aaa
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | blobs and the start gate (fix in origin/DEV, ticket completed+confirmed, no window open, asks to CTO, Y2, IB2, census) | all true and printed | pair blob 7e96f36b11, CTO half b427f42ef2, check af25604aaa equal at worktree, HEAD and GO commit f2e986792e; origin/DEV tip = 539b1ee70ba1 (fix in), 8ecad4a5fb its ancestor; ticket TCK-20261017-da2a1987 completed with meeting.status confirmed (ConsistentRead); asks: CTO (msg 10454: nothing open), Y2 (msg 10453: none open, window 5 held until Monday), IB2 (no reply; silence read as none per my message; held TO-DB-b-328 step 8 not started); final census 95 trees read, 0 live open entries naming opal-ticket-api, opal-tickets or opal-users-v2, shared tree none besides this ledger | CLOSED 20261017T091000Z |
| N1 | verify | the sha to be served is NAMED to the CTO and to the issuer BEFORE the server is restarted | messages sent, sha printed | sha 539b1ee70ba1b2a9b0c562a9169d9fcca1b7c18e named to 2.0.0_SA_COO~V2 (09:06:49Z) and 1.0.0_SA_CTO~DELL2 (09:06:55Z) before any restart; the CTO then moved the server himself (msg 10454, 09:07:44Z) and told me not to restart or check out | CLOSED 20261017T091000Z |
| V0 | activation | 5174 server moved to the named sha and restarted on 5174 only, HTTP 200, the CTO told the sha | git rev-parse HEAD equals the named sha, origin printed | the CTO moved C:/dev/smoke-template-5174 to 539b1ee70ba1b2a9b0c562a9169d9fcca1b7c18e and restarted Vite (node pid started 09:07:28Z) on 5174 --strictPort; I did NOT stop, restart or check out anything; read by me: git rev-parse HEAD = 539b1ee70ba1b2a9b0c562a9169d9fcca1b7c18e, 0 dirty rows, 8ecad4a5fb an ancestor, GET http://localhost:5174/ 200 | CLOSED 20261017T091000Z |
| M1 | activation | ONE filer row written with attribute_not_exists(PK), PRESENT, ONE token in memory | iat and exp recorded, at most 20 minutes | ONE row tckt-r20-filer-20261017@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [cottonwood], no scope_all_firms; ONE key read, ONE RS256 token in memory only, iat 2026-10-17T09:10:02Z exp 09:15:02Z (life 300s) | CLOSED 20261017T091043Z |
| R0 | verify | the read and ONE shot filer_completed; no write, no click on a control; contrast printed as a number | PNG saved, path and bytes printed, ratio from the PNG | board read as the filer on http://localhost:5174 (page origin printed) at the CTO's server, DEV 539b1ee70ba1b2a9b0c562a9169d9fcca1b7c18e; Completed tab opened (navigation only); ONE shot filer_completed saved: org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_reshot/filer_completed__tckt-r20-filer-20261017__TCK-20261017-da2a1987__localhost-5174__dev-539b1ee70ba1.png (18035 bytes), clipped to the ticket's two rows; no ticket write, no click on a control; outcome-line contrast from the saved PNG: 10.10:1 (WCAG; strongest text pixel rgb(209,212,217) against the row background rgb(25,38,67); crop 1294x16 px) | CLOSED 20261017T091043Z |
| R1 | verify | the row deleted after exp | ConsistentRead ABSENT | filer row deleted at 2026-10-17T09:15:07Z, after token exp 09:15:02Z; ConsistentRead ABSENT (R20_RESHOT_RESULT.json); the ticket still completed/confirmed; the CTO's 5174 server untouched by me (HEAD 539b1ee70ba1, 200) | CLOSED 20261017T091536Z |
| V1 | verify | r20_reshot_check.py | RUN-OK (reshot) | r20_reshot_check.py (blob af25604aaa): RUN-OK (reshot) the completed confirmed ticket was read on http://localhost:5174 at DEV 539b1ee70ba1, one shot saved as PNG, the filer row absent | CLOSED 20261017T091536Z |

## Log

- 20261017T090635Z OPENED by 0.7.0_AE_CloudOps~TV2 with 7 leg(s)
- 20261017T091000Z LEG S1 closed: pair blob 7e96f36b11, CTO half b427f42ef2, check af25604aaa equal at worktree, HEAD and GO commit f2e986792e; origin/DEV
- 20261017T091000Z LEG N1 closed: sha 539b1ee70ba1b2a9b0c562a9169d9fcca1b7c18e named to 2.0.0_SA_COO~V2 (09:06:49Z) and 1.0.0_SA_CTO~DELL2 (09:06:55Z) bef
- 20261017T091000Z LEG V0 closed: the CTO moved C:/dev/smoke-template-5174 to 539b1ee70ba1b2a9b0c562a9169d9fcca1b7c18e and restarted Vite (node pid starte
- 20261017T091043Z LEG M1 closed: ONE row tckt-r20-filer-20261017@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [co
- 20261017T091043Z LEG R0 closed: board read as the filer on http://localhost:5174 (page origin printed) at the CTO's server, DEV 539b1ee70ba1b2a9b0c562a9
- 20261017T091536Z LEG R1 closed: filer row deleted at 2026-10-17T09:15:07Z, after token exp 09:15:02Z; ConsistentRead ABSENT (R20_RESHOT_RESULT.json); th
- 20261017T091536Z LEG V1 closed: r20_reshot_check.py (blob af25604aaa): RUN-OK (reshot) the completed confirmed ticket was read on http://localhost:5174 
- 20261017T091537Z CLOSED -- all 7 legs proven
