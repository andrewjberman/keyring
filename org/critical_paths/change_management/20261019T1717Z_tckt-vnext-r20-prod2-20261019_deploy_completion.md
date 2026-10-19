# Deploy Completion Record
**Date opened:** 2026-10-19T17:17:12.087810+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R20-PROD2 (AMENDMENT 1, GO msg 10800; run pair AMENDMENTS 8 and 9): the FWD-11 JOURNEY ON PROD https://opalinvest.dev: synthetic filer tckt-r20-pfiler-20261019 FILES one Meeting Request, synthetic coordinator tckt-r20-pcoord-20261019 CONFIRMS it inside ONE routing window on opal-ticket-api ROUTING_MATRIX meeting_request.primary (coordinator alone, then jeanette alone); filer reads the confirmed line (contrast printed); then the ONE synthetic opal-tickets item (record saved first) and BOTH opal-users-v2 rows are deleted by key; surfaces: ticket service, opal-tickets, opal-users-v2, Lambda ROUTING_MATRIX; pair blobs 0b2978bfea / e7a33cf976, check v2 9ff30a5d38
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | blobs, start gate (PROD carries 2a64d211 and the TO-DB-b-336 release, site 200, routing jeanette alone, census, asks to CTO, Y2 and IB2, fire-window answer printed) | all true and printed |  | OPEN |
| M1 | activation | TWO rows (filer, coordinator) written with attribute_not_exists(PK), PRESENT, ONE token each in memory | iat and exp recorded, each at most 20 minutes |  | OPEN |
| W1 | activation | routing window opened: scratch copy, plan ONE attribute change, safe-apply, read back | meeting_request.primary equals the coordinator alone |  | OPEN |
| F1 | activation | the filer FILES one Meeting Request on https://opalinvest.dev; shot prod_filer_waiting | ticket open, routing.primary the coordinator alone, WE_DL_UNCONFIGURED, ticket id printed |  | OPEN |
| C1 | activation | coordinator shot prod_coordinator_controls BEFORE the click, then CONFIRMS one proposed time | meeting.status confirmed, meeting.by the coordinator, ticket open |  | OPEN |
| W2 | activation | routing window closed: committed tree re-applied under safe-apply | meeting_request.primary equals jeanette alone |  | OPEN |
| X1 | verify | filer reloads and shot prod_filer_confirmed; type list recorded; contrast printed as a number from my own PNG | PNG saved, ratio at least 4.5 |  | OPEN |
| D1 | verify | after the last exp: ticket item saved whole, then deleted by its printed key; both rows deleted by key | ticket and both rows ConsistentRead ABSENT |  | OPEN |
| V1 | verify | r20_prodjourney_check_v2.py with its self-test printed beside the verdict | RUN-OK (prodjourney) |  | OPEN |

## Log

- 20261019T171712Z OPENED by 0.7.0_AE_CloudOps~TV2 with 9 leg(s)
