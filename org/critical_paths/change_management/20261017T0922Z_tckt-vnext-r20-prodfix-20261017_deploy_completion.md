# Deploy Completion Record
**Date opened:** 2026-10-17T09:22:24.841234+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T093850Z
**Deploy:** TCKT_VNEXT TO-R20-PROMOTE-FIX: promote ONE portal commit 2a64d2115f (cand/dell2/tckt-outcome-line-contrast-prodfix, two files: MeetingRequestParts.tsx and meeting-outcome-contrast.test.tsx) DEV->PROD via /prod-deploy chosen-set release; Ticket Center meeting outcome line contrast fix, read client-facing by the CTO under Andrew record 9063a44a4c, row dell2-20261017T090236Z-70b4 APPROVED; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only commit 2a64d2115f | promoted sha and PROD before/after | origin/PROD 4cf06588736b (portal-v2.1.233) -> 15bc21b304d4 (push receipt 4cf06588..15bc21b3; origin/PROD re-read before push = 4cf06588736b); non-merge payload 2a64d211 only, 2 files, parent = the PROD tip, 0 Trade Request strings; tag portal-v2.1.234 peels to 15bc21b304d4 | CLOSED 20261017T093850Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 39021252990 --json: status completed, conclusion success, headSha 15bc21b304d4b0a150a9cdd0c1b75251f0b8c2a8; the only workflow on that sha | CLOSED 20261017T093850Z |
| L3 | verify | Ticket Center outcome line contrast read on PROD as a number | screenshot, method line and number or ABSENT with reason | outcome line contrast 10.10:1 from this seat's own saved PNGs (strongest text pixel rgb(209,212,217) over rgb(25,38,67); line located by differencing a shot with the line hidden; controls 1.25:1 for the defect ink, 21.00:1 black on white). FIXTURE, NOT THE REAL TICKET: ui-smoke stubbed internal Dev admin session, served PROD bundle rendering a synthetic completed meeting ticket; TCK-20261017-da2a1987 not read. New Ticket type list: Service Request, Meeting Request, Analysis Request, Other present; Trade Request absent (probe controls fail as they should). | CLOSED 20261017T093850Z |

## Log

- 20261017T092224Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261017T093850Z LEG L1 closed: origin/PROD 4cf06588736b (portal-v2.1.233) -> 15bc21b304d4 (push receipt 4cf06588..15bc21b3; origin/PROD re-read before 
- 20261017T093850Z LEG L2 closed: gh -R Opal-Capital/portal run view 39021252990 --json: status completed, conclusion success, headSha 15bc21b304d4b0a150a
- 20261017T093850Z LEG L3 closed: outcome line contrast 10.10:1 from this seat's own saved PNGs (strongest text pixel rgb(209,212,217) over rgb(25,38,67);
- 20261017T093850Z CLOSED -- all 3 legs proven
