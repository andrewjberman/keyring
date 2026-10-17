# Deploy Completion Record
**Date opened:** 2026-10-17T08:24:32.010200+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T084048Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-SET: promote ONE branch cand/dell2/anlreq-prod-recut-v2 (head 24034edcbb, 20 cherry-picked commits cut from PROD fa21a303d8, 36 files, Trade Request form excluded) DEV->PROD via /prod-deploy chosen-set release; client-facing pages included under Andrew word 9063a44a4c, row dell2-20261017T081434Z-4df0 APPROVED; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-prod-recut-v2 | promoted sha and PROD before/after | origin/PROD fa21a303d872 (portal-v2.1.232) -> 4cf06588736b (push receipt fa21a303..4cf06588; origin/PROD re-read before push = fa21a303d872); release = 20 non-merge commits of cand/dell2/anlreq-prod-recut-v2 (head 24034edcbb) + 1 builder merge, 36 files, Trade Request form c05e3dda and 7f6c698d absent; tag portal-v2.1.233 peels to 4cf06588736b | CLOSED 20261017T084047Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch | gh -R Opal-Capital/portal run view 39017972082 --json: status completed, conclusion success, headSha 4cf06588736bd1e1279b3ba249f922173e0b9ae8; the only workflow on that sha; git diff --stat 24034edcbb origin/PROD prints nothing; branch head ancestor of origin/PROD rc 0 | CLOSED 20261017T084047Z |
| L3 | verify | staff Ticket Center read on PROD | screenshot read or ABSENT with reason | ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal Dev admin read of PROD loaded the Ticket Center frame only (board: Tickets could not be loaded, no live API), screenshot set_prod_ticket_center_stubbed_staff.png; Firm chooser and catalogue not read; page load only, no click, no ticket opened, filed, retried or edited (TCK-20261017-5af976ff untouched); nothing minted, no credential asked | CLOSED 20261017T084048Z |

## Log

- 20261017T082432Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261017T084047Z LEG L1 closed: origin/PROD fa21a303d872 (portal-v2.1.232) -> 4cf06588736b (push receipt fa21a303..4cf06588; origin/PROD re-read before 
- 20261017T084047Z LEG L2 closed: gh -R Opal-Capital/portal run view 39017972082 --json: status completed, conclusion success, headSha 4cf06588736bd1e1279
- 20261017T084048Z LEG L3 closed: ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal Dev admin read of PROD l
- 20261017T084048Z CLOSED -- all 3 legs proven
