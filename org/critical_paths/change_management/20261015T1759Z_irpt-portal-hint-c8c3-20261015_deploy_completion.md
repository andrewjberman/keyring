# Deploy Completion Record
**Date opened:** 2026-10-15T17:59:39.709181+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T181429Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-HINT: promote TWO portal commits a6b83f692084 (filing hint, call 469b) and 406345bce1 (c8c3, commentary_requested always sent) DEV->PROD via /prod-deploy chosen-set release; keep-equal-pair excluded; rollback = revert of the promote merge on PROD (both), or c8c3 alone on ~Y2's word
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only a6b83f692084 and 406345bce1 | promoted sha and PROD before/after | origin/PROD 33ad65eef369 -> 45a3e18f197c (push receipt 33ad65ee..45a3e18f; origin/PROD re-read before push = 33ad65eef369); non-merge payload a6b83f69 + 406345bc only, 6 files, keep-equal-pair f78ea50e absent; tag portal-v2.1.225 peels to 45a3e18f197c | CLOSED 20261015T181428Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 38783306136 --json: status completed, conclusion success, headSha 45a3e18f197c485eb6534f4e29d49fd5e9636c98; the only workflow on that sha | CLOSED 20261015T181428Z |
| L3 | verify | staff read of Ticket Center on PROD | screenshot read or ABSENT with reason | ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal-admin read of PROD reached no live API (Tickets could not be loaded), screenshot hint_prod_ticket_center_stubbed_staff.png; chooser and catalogue not read; nothing minted, no credential asked (order step 6 ABSENT line) | CLOSED 20261015T181428Z |

## Log

- 20261015T175939Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261015T181428Z LEG L1 closed: origin/PROD 33ad65eef369 -> 45a3e18f197c (push receipt 33ad65ee..45a3e18f; origin/PROD re-read before push = 33ad65eef36
- 20261015T181428Z LEG L2 closed: gh -R Opal-Capital/portal run view 38783306136 --json: status completed, conclusion success, headSha 45a3e18f197c485eb65
- 20261015T181428Z LEG L3 closed: ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal-admin read of PROD reach
- 20261015T181429Z CLOSED -- all 3 legs proven
