# Deploy Completion Record
**Date opened:** 2026-10-15T16:55:41.535722+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T174551Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD1 window 2 (addendum 2): one FWD-1 run, a synthetic staff user files one Analysis Request on the local dev build; the user is removed after (F1 ABSENT x2 before close)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | verify | mint fwd1-staff-r41a@opal.invalid row in opal-users-v2 (attribute_not_exists) | the driver's mint line, no secret printed | driver STEP-2 mint rc=0 MINT-OK READBACK-OK at 17:00:10Z (one users row, attribute_not_exists); run_fwd1_r2/run_report.json | CLOSED 20261015T174550Z |
| S | verify | file ONE Analysis Request through the Ticket Center page, firm 49financial | ticket id from run_report.json | ticket TCK-20261015-944c84f8 filed, POST /api/scoped/tickets 201 at 17:00:32Z, guard refused 0; ticket record read open; request analysis#REQ-d47252fe74634d0c5cdd8067#1 owner the synthetic principal commentary_requested true | CLOSED 20261015T174550Z |
| P | verify | poll the chain up to 20 minutes, read attachments n of 4 | run_report.json attachments | 19 polls 17:01:36Z to 17:20:34Z read attachments 0 of 4 on the page (original, form, report, commentary all present=false); ticket record at 17:32Z holds input_id and upload_id and answers, no report_ref, no commentary pdf_ref; read only, nothing clicked | CLOSED 20261015T174550Z |
| R | verify | remove the user; ABSENT by email-index GSI and ConsistentRead | two ABSENT lines | driver STEP-6 remove rc=0 ABSENT GSI and ABSENT CONSISTENT at 17:20:36Z; seat's own reads 17:42:16Z: ConsistentRead get_item absent, email-index count 0 | CLOSED 20261015T174550Z |

## Log

- 20261015T165541Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261015T174550Z LEG M closed: driver STEP-2 mint rc=0 MINT-OK READBACK-OK at 17:00:10Z (one users row, attribute_not_exists); run_fwd1_r2/run_report.j
- 20261015T174550Z LEG S closed: ticket TCK-20261015-944c84f8 filed, POST /api/scoped/tickets 201 at 17:00:32Z, guard refused 0; ticket record read open;
- 20261015T174550Z LEG P closed: 19 polls 17:01:36Z to 17:20:34Z read attachments 0 of 4 on the page (original, form, report, commentary all present=fals
- 20261015T174550Z LEG R closed: driver STEP-6 remove rc=0 ABSENT GSI and ABSENT CONSISTENT at 17:20:36Z; seat's own reads 17:42:16Z: ConsistentRead get_
- 20261015T174551Z CLOSED -- all 4 legs proven
