# Deploy Completion Record
**Date opened:** 2026-10-19T19:43:50.149088+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T201740Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-BACKOFF: promote ONE branch cand/dell2/anlreq-prod-recut-v3 (head a9cc52661e, ONE commit cut from PROD 8cd45f623bdf, 4 files: the Analysis Request upload RESOLVING backoff) DEV->PROD via /prod-deploy chosen-set release; Ticket Center client-facing, row dell2-20261019T192242Z-f75e APPROVED ruled by andrew; rollback = revert of the promote on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-prod-recut-v3 | promoted sha and PROD before/after | origin/PROD 8cd45f623bdf (portal-v2.1.243) -> facddeb687b8 (push receipt 8cd45f62..facddeb6; origin/PROD re-read before push = 8cd45f623bdf); release = 1 non-merge commit a9cc52661e + 1 builder merge, 4 files, 0 trade; tag portal-v2.1.244 peels to facddeb687b8 | CLOSED 20261019T201739Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch | run 39317468736 Deploy to Production completed success 20:15:56Z (Build 20:15:23Z, Deploy to S3 + CloudFront 20:15:44Z = live, Tag 20:15:56Z); the only workflow on facddeb687b8; git diff --stat a9cc52661e origin/PROD empty; branch head ancestor of origin/PROD rc 0 | CLOSED 20261019T201739Z |
| L3 | verify | staff Ticket Center read on PROD | screenshot read or ABSENT with reason | ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal Dev admin read of PROD loaded the Ticket Center frame only (Tickets could not be loaded, no live API), screenshot backoff_prod_ticket_center_stubbed_staff.png; Firm chooser, model list and tickers not read; page load only, no ticket touched | CLOSED 20261019T201739Z |

## Log

- 20261019T194350Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261019T201739Z LEG L1 closed: origin/PROD 8cd45f623bdf (portal-v2.1.243) -> facddeb687b8 (push receipt 8cd45f62..facddeb6; origin/PROD re-read before 
- 20261019T201739Z LEG L2 closed: run 39317468736 Deploy to Production completed success 20:15:56Z (Build 20:15:23Z, Deploy to S3 + CloudFront 20:15:44Z =
- 20261019T201739Z LEG L3 closed: ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal Dev admin read of PROD l
- 20261019T201740Z CLOSED -- all 3 legs proven
