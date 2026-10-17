# Deploy Completion Record
**Date opened:** 2026-10-17T10:01:47.700119+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T101200Z
**Deploy:** TCKT_VNEXT TO-R20-PROD (AMENDMENT 1, GO msg 10486; run pair AMENDMENT 7): read-only render of the REAL completed meeting ticket TCK-20261017-da2a1987 on the PROD site https://opalinvest.dev as ONE synthetic filer tckt-r20-filer-20261017@opal.invalid (allowedFirmIds [cottonwood]); two shots prod_filer_completed and prod_meeting_form; New Ticket type list recorded (a Trade Request option is a STOP); no ticket write, no routing window; surface: opal-users-v2 (one row), a ticket read; pair blobs 3acf507198 / bda0290f7f, check ba1ef3b0e0
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | blobs and the start gate (origin/PROD carries 2a64d211, ticket completed+confirmed, PROD site 200, no window open, asks to CTO, Y2, IB2, census) | all true and printed | pair blob 3acf507198, CTO half bda0290f7f, check ba1ef3b0e0 equal at worktree and HEAD; git rev-parse origin/PROD = 15bc21b304d4b0a150a9cdd0c1b75251f0b8c2a8, 2a64d211 an ancestor (in); ticket TCK-20261017-da2a1987 completed with meeting.status confirmed (ConsistentRead); GET https://opalinvest.dev/ 200; asks: Y2 (msg 10491: none open, window 5 held to Monday; asks that Andrew's ticket TCK-20261017-5af976ff not be opened, retried or edited: this run touches only the one named ticket), CTO and IB2 no reply (silence read as none per my messages); final census 97 trees read, 0 live open entries naming opal-ticket-api, opal-tickets or opal-users-v2, shared tree none besides this ledger | CLOSED 20261017T100552Z |
| M1 | activation | ONE filer row written with attribute_not_exists(PK), PRESENT, ONE token in memory | iat and exp recorded, at most 20 minutes | ONE row tckt-r20-filer-20261017@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [cottonwood], no scope_all_firms; ONE key read, ONE RS256 token in memory only, iat 2026-10-17T10:05:54Z exp 10:10:54Z (life 300s) | CLOSED 20261017T100630Z |
| R0 | verify | the read on https://opalinvest.dev: two shots, the type list recorded, the contrast printed as a number | two PNGs with path and bytes, no Trade Request option | read on https://opalinvest.dev (page origin printed), as the filer: Completed tab (navigation only), the one named ticket; shots prod_filer_completed 18035 bytes and prod_meeting_form 22044 bytes saved (paths under deliverables/r20_prod/, none described); New Ticket type options recorded: Service Request, Meeting Request, Other, Analysis Request (Trade Request ABSENT); the meeting form opened and NOT submitted; no ticket write, no click on a control; outcome-line contrast from my own PNG: 10.10:1 (WCAG; strongest text pixel rgb(209,212,217) against row background rgb(25,38,67), crop 1294x16 px) | CLOSED 20261017T100631Z |
| R1 | verify | the row deleted after exp | ConsistentRead ABSENT | filer row deleted at 2026-10-17T10:10:59Z, after token exp 10:10:54Z; ConsistentRead ABSENT (R20_PROD_RESULT.json); the ticket still completed/confirmed | CLOSED 20261017T101200Z |
| V1 | verify | r20_prod_check.py | RUN-OK (prod) | r20_prod_check.py (blob ba1ef3b0e0): RUN-OK (prod) the completed confirmed ticket was read on https://opalinvest.dev, two shots saved as PNG, Trade Request absent from the type list, the filer row absent | CLOSED 20261017T101200Z |

## Log

- 20261017T100147Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
- 20261017T100552Z LEG S1 closed: pair blob 3acf507198, CTO half bda0290f7f, check ba1ef3b0e0 equal at worktree and HEAD; git rev-parse origin/PROD = 15bc
- 20261017T100630Z LEG M1 closed: ONE row tckt-r20-filer-20261017@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [co
- 20261017T100631Z LEG R0 closed: read on https://opalinvest.dev (page origin printed), as the filer: Completed tab (navigation only), the one named ticke
- 20261017T101200Z LEG R1 closed: filer row deleted at 2026-10-17T10:10:59Z, after token exp 10:10:54Z; ConsistentRead ABSENT (R20_PROD_RESULT.json); the 
- 20261017T101200Z LEG V1 closed: r20_prod_check.py (blob ba1ef3b0e0): RUN-OK (prod) the completed confirmed ticket was read on https://opalinvest.dev, tw
- 20261017T101200Z CLOSED -- all 5 legs proven
