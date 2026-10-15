# Deploy Completion Record
**Date opened:** 2026-10-15T18:19:34.566637+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T182953Z
**Deploy:** IRPT_ANLREQ TO-REVERT-C8C3: revert merge 45a3e18f (c8c3, commentary_requested always sent) alone on PROD with git revert -m 1; the filing hint 469b (merge 9176227f) stays; CTO ruling msgs 8530 8534
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of the single revert commit of 45a3e18f | promoted sha and PROD before/after | origin/PROD 45a3e18f197c -> e0b43076d9da (push receipt 45a3e18f..e0b43076; origin/PROD re-read before push = 45a3e18f197c); one revert commit (git revert -m 1 45a3e18f), 3 files, hint files untouched, filingHints present; tag portal-v2.1.226 peels to e0b43076d9da | CLOSED 20261015T182952Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 38785590551 --json: status completed, conclusion success, headSha e0b43076d9daf56f8eb4937137180e3cf4246e7f; the only workflow on that sha | CLOSED 20261015T182952Z |
| L3 | verify | staff read of Ticket Center on PROD | screenshot read or ABSENT with reason | ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal-admin read of PROD reached no live API (Tickets could not be loaded), screenshot revert_prod_ticket_center_stubbed_staff.png; chooser and catalogue not read; nothing minted, no credential asked (order step 6 ABSENT line) | CLOSED 20261015T182953Z |

## Log

- 20261015T181934Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261015T182952Z LEG L1 closed: origin/PROD 45a3e18f197c -> e0b43076d9da (push receipt 45a3e18f..e0b43076; origin/PROD re-read before push = 45a3e18f197
- 20261015T182952Z LEG L2 closed: gh -R Opal-Capital/portal run view 38785590551 --json: status completed, conclusion success, headSha e0b43076d9daf56f8eb
- 20261015T182953Z LEG L3 closed: ABSENT: no sanctioned staff-class login or real bearer for this seat; ui-smoke stubbed internal-admin read of PROD reach
- 20261015T182953Z CLOSED -- all 3 legs proven
