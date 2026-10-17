# Deploy Completion Record
**Date opened:** 2026-10-17T09:06:35.588126+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R20-RV2 (AMENDMENT 1, GO msg 10445; run pair AMENDMENT 6): read-only RE-SHOT of the completed meeting ticket TCK-20261017-da2a1987 on the fixed DEV build; the CTO's 5174 server (worktree C:/dev/smoke-template-5174) moved from 38d4f9473284 to 539b1ee70ba1 under the CTO's msg 10441; ONE synthetic filer tckt-r20-filer-20261017@opal.invalid (allowedFirmIds [cottonwood]); ONE shot filer_completed; surfaces: opal-users-v2 (one row), 5174 server, ticket service read; pair blobs 7e96f36b11 / b427f42ef2, check af25604aaa
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | blobs and the start gate (fix in origin/DEV, ticket completed+confirmed, no window open, asks to CTO, Y2, IB2, census) | all true and printed |  | OPEN |
| N1 | verify | the sha to be served is NAMED to the CTO and to the issuer BEFORE the server is restarted | messages sent, sha printed |  | OPEN |
| V0 | activation | 5174 server moved to the named sha and restarted on 5174 only, HTTP 200, the CTO told the sha | git rev-parse HEAD equals the named sha, origin printed |  | OPEN |
| M1 | activation | ONE filer row written with attribute_not_exists(PK), PRESENT, ONE token in memory | iat and exp recorded, at most 20 minutes |  | OPEN |
| R0 | verify | the read and ONE shot filer_completed; no write, no click on a control; contrast printed as a number | PNG saved, path and bytes printed, ratio from the PNG |  | OPEN |
| R1 | verify | the row deleted after exp | ConsistentRead ABSENT |  | OPEN |
| V1 | verify | r20_reshot_check.py | RUN-OK (reshot) |  | OPEN |

## Log

- 20261017T090635Z OPENED by 0.7.0_AE_CloudOps~TV2 with 7 leg(s)
