# Deploy Completion Record
**Date opened:** 2026-10-15T14:47:01.713917+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T150209Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-J7: promote ONE portal commit 6f4e5f671f09 (staff firm chooser) DEV->PROD via /prod-deploy chosen-set release; c8c3 excluded; rollback = revert of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only 6f4e5f671f09 | promoted sha and PROD before/after | origin/PROD c3b21a40e29f -> 33ad65eef369 (push receipt c3b21a40..33ad65ee; fetch re-read origin/PROD before push = c3b21a40e29f); payload 6f4e5f67 + builder merge only, 5 files, c8c3 absent; tag portal-v2.1.224 peels to 33ad65eef369 | CLOSED 20261015T145902Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 38755378258 --json: status completed, conclusion success, headSha 33ad65eef369face7ec7a9aa825ba7fb23f0fa28; the only workflow on that sha | CLOSED 20261015T145902Z |
| L3 | verify | staff read of Ticket Center on PROD | screenshot read or ABSENT with reason | ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal-admin read of PROD reached no live API (Tickets could not be loaded), screenshot j7_prod_ticket_center_stubbed_staff.png; chooser and catalogue not read; nothing minted, no credential asked (order step 6 ABSENT line) | CLOSED 20261015T145903Z |

## Log

- 20261015T144701Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261015T145902Z LEG L1 closed: origin/PROD c3b21a40e29f -> 33ad65eef369 (push receipt c3b21a40..33ad65ee; fetch re-read origin/PROD before push = c3b21
- 20261015T145902Z LEG L2 closed: gh -R Opal-Capital/portal run view 38755378258 --json: status completed, conclusion success, headSha 33ad65eef369face7ec
- 20261015T145903Z LEG L3 closed: ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal-admin read of PROD reach
- 20261015T150209Z CLOSED -- all 3 legs proven
