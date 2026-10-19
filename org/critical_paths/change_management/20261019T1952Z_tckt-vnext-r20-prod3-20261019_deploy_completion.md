# Deploy Completion Record
**Date opened:** 2026-10-19T19:52:43.830793+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R20-PROD3 (GO msg 10941, CTO msg 10936): the TRADE REQUEST JOURNEY ON PROD https://opalinvest.dev: one synthetic internal filer files ONE Trade Request with ONE synthetic .csv through the form's three calls, reads the attachment back through the open route (SHA-256 equal), then the ticket (record saved first), the filer row and the ONE uploaded object are deleted by exact key; surfaces: opal-tickets, opal-users-v2, s3://opal-data-cottonwood trade-form prefix (one object); check 6bc0e03848
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | check blob, start gate (PROD head, promote CI, Y2 backoff live minute, site 200, fire windows, census, filer and ticket ABSENT, prefix count, protected tickets present) | all true and printed | check blob 6bc0e03848 equal to the GO; PROD head facddeb687b8 (v2.1.244; backoff release live 20:15:44Z per Y2 msg 10993; CI run 39317468736 completed success 20:15:56Z, 19 min old; 2a64d211 ancestor); site 200; Lambda CodeSha256 iRxJZYp6 Active; filer row ABSENT; trade-form prefix 0 objects (list-objects-v2, not truncated); protected tickets TCK-20261017-da2a1987 and TCK-20261017-5af976ff present (read only); fire windows: CTO none until 21:00Z (10952), IB2 none (10968), Y2 clear (10993); census 39 trees, 0 other live ledgers; all in deliverables/r20_trade_prod/fire_windows_answer.txt and promote_proof.txt | CLOSED 20261019T203714Z |
| M1 | activation | ONE filer row written attribute_not_exists(PK) PRESENT, ONE token in memory | iat and exp recorded, at most 20 minutes | attempt 1: one filer row written attribute_not_exists(PK) PRESENT 20:37:17Z; one token in memory, life 480 s, exp 20:45:17Z; row DELETED 20:49:11Z by CLI after the script crashed on the S3 denial, ConsistentRead ABSENT | CLOSED 20261019T205135Z |
| F1 | activation | filer submits ONE Trade Request with ONE csv through the upload door, the PUT and the ticket; shots prod_trade_form_filled and prod_trade_filed | three HTTP statuses, ticket id and object key printed, no engine call | attempt 1: filer filed TCK-20261019-2d6d1a25 on https://opalinvest.dev 20:37:23Z; upload door 200, PUT 200, ticket 201; object key portal/cottonwood/state/ticket_attachments/trade-form/8b46f05593e643f0bb229023841d2a4a/tckt-r20-trade-synthetic.csv PRESENT; create logged WE_DL_UNCONFIGURED only; shots prod_trade_form_filled 14797 b and prod_trade_filed 13784 b; no engine call | CLOSED 20261019T205135Z |
| R1 | verify | filer opens the attachment through the open route | SHA-256 read back equals SHA-256 uploaded |  | OPEN |
| D1 | verify | after the last exp: ticket item saved whole, then ticket, filer row and the ONE object deleted by exact printed key | each ABSENT by a 404 only |  | OPEN |
| V1 | verify | r20_tradejourney_check.py with its self-test printed beside the verdict | RUN-OK (tradejourney) |  | OPEN |

## Log

- 20261019T195243Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261019T203714Z LEG S1 closed: check blob 6bc0e03848 equal to the GO; PROD head facddeb687b8 (v2.1.244; backoff release live 20:15:44Z per Y2 msg 10993
- 20261019T205135Z LEG M1 closed: attempt 1: one filer row written attribute_not_exists(PK) PRESENT 20:37:17Z; one token in memory, life 480 s, exp 20:45:
- 20261019T205135Z LEG F1 closed: attempt 1: filer filed TCK-20261019-2d6d1a25 on https://opalinvest.dev 20:37:23Z; upload door 200, PUT 200, ticket 201; 
