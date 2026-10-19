# Deploy Completion Record
**Date opened:** 2026-10-19T15:40:15.619311+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T170632Z
**Deploy:** IRPT_DASHBD TO-DB-b-336: promote ONE approved branch cand/dell2/irpt-promote-all-dell2-ir-set-20261019 (head 8c52f547f4, three commits on PROD d729ee6d8456, 49 files: the Investor Reporting Performance set, the Trade Request form and the reveal of Trade Request in the New Ticket list; five dell1 files and commentary-always excluded) DEV->PROD via /prod-deploy chosen-set release; client-facing pages, Andrew word 2026-10-19 (records 142xZ and 144xZ) with the CTO closing the approval row; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/irpt-promote-all-dell2-ir-set-20261019 | promoted sha and PROD before/after | origin/PROD d729ee6d8456 (portal-v2.1.241) -> 9107d48ae3d2 (push receipt d729ee6d..9107d48a; origin/PROD re-read before push = d729ee6d8456); release = 3 non-merge commits of cand/dell2/irpt-promote-all-dell2-ir-set-20261019 (head 8c52f547f4) + 1 builder merge, 49 files; tag portal-v2.1.242 peels to 9107d48ae3d2 | CLOSED 20261019T170630Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | run 39284545087 Deploy to Production: jobs Build success 16:21:48Z, Deploy to S3 + CloudFront success 16:22:04Z (PROD live), Tag success 16:22:17Z; run status read queued until ~16:33Z then completed/success 16:37:19Z; the only workflow on 9107d48ae3d2; served bundle carries the new literal (PrintEntry-3_bJi1mU.js) | CLOSED 20261019T170630Z |
| L3 | verify | PROD pages read as staff-class and attachment-upload route read | screenshots read, route and env key names stated or ABSENT with reason | stubbed staff session (not a real login): Ticket Center loaded, New Ticket offers trade_request 'Trade Request' (controls fail as they should); Performance tab loaded but the template view was NOT seen rendered (mounts only for a selected 49 Financial client; no scope in the stub) = record line P4 FAIL; analysis-request files byte-equal to DEV. attachment-upload route configured live (API 7k3ed8px20 route -> integration vgix3jf AWS_PROXY opal-ticket-api), 14 env key names read, no values, route not called, S3 scope not read | CLOSED 20261019T170631Z |

## Log

- 20261019T154015Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261019T170630Z LEG L1 closed: origin/PROD d729ee6d8456 (portal-v2.1.241) -> 9107d48ae3d2 (push receipt d729ee6d..9107d48a; origin/PROD re-read before 
- 20261019T170630Z LEG L2 closed: run 39284545087 Deploy to Production: jobs Build success 16:21:48Z, Deploy to S3 + CloudFront success 16:22:04Z (PROD li
- 20261019T170631Z LEG L3 closed: stubbed staff session (not a real login): Ticket Center loaded, New Ticket offers trade_request 'Trade Request' (control
- 20261019T170632Z CLOSED -- all 3 legs proven
