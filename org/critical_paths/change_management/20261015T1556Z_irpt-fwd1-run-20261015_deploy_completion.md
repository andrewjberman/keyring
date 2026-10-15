# Deploy Completion Record
**Date opened:** 2026-10-15T15:56:49.332569+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261015T161212Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD1: one FWD-1 run, a synthetic staff user files one Analysis Request on the local dev build; the user is removed after (F1 ABSENT x2 before close)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | verify | mint fwd1-staff-r41a@opal.invalid row in opal-users-v2 (attribute_not_exists) | the driver's mint line, no secret printed | driver STEP-2 mint rc=0 MINT-OK READBACK-OK at 16:03:31Z (one users row, attribute_not_exists); run_fwd1/run_report.json | CLOSED 20261015T161211Z |
| S | verify | file ONE Analysis Request through the Ticket Center page, firm 49financial | ticket id from run_report.json |  | OPEN |
| P | verify | poll the chain up to 20 minutes, read attachments n of 4 | run_report.json attachments |  | OPEN |
| R | verify | remove the user; ABSENT by email-index GSI and ConsistentRead | two ABSENT lines | driver STEP-6 remove rc=0 ABSENT GSI and ABSENT CONSISTENT at 16:04:11Z; seat's own reads 16:05:04Z: ConsistentRead get_item absent, email-index count 0 | CLOSED 20261015T161212Z |

## Log

- 20261015T155649Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261015T161211Z LEG M closed: driver STEP-2 mint rc=0 MINT-OK READBACK-OK at 16:03:31Z (one users row, attribute_not_exists); run_fwd1/run_report.json
- 20261015T161212Z LEG R closed: driver STEP-6 remove rc=0 ABSENT GSI and ABSENT CONSISTENT at 16:04:11Z; seat's own reads 16:05:04Z: ConsistentRead get_
- 20261015T161212Z CLOSED -- REFUSED BY GATE before apply, world untouched: Legs S and P NEVER RAN: the driver died at STEP-4 (firm selector not visible in 30000 ms; its route guard refused POST directory/resolve), ticket_id null, polls empty, no retry per the order. Nothing created beyond the one users row, which F1 reads ABSENT by GSI (count 0) and ConsistentRead at 16:05:04Z; positive control: the same two reads returned the row's presence path via the driver's own REA
