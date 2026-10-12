# Deploy Completion Record
**Date opened:** 2026-10-12T02:43:02.284627+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bg-1: the THIRD redeploy -- ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin 6e8dcaf414 (box/dell1 first-parent) carrying AMGT_CORPUS's /15 corpus files (dossier.py 7b67bf62afdd METHOD /15, team_sheet.py ef4da7cdc85a), bd-1's scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c KEPT, AMGT-bg-2's scoped_amgt.py NOT in this build; pair COO half @c9fe8212d6 + CTO half (msg 4225); GO msg 4229
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: 6e8dcaf414 is a box/dell1 first-parent commit, not box/dell1 HEAD, bg-2's scoped_amgt.py NOT carried; r94_admission_table.py 6e8dcaf414 --pin b3d4856531 shows exactly TWO lib members at the half's blobs with scoped_amgt.py and monthly_chatter.py byte-equal to the live package (a third member or a different api blob is a STOP); r94_naming_replay.py --pin b3d4856531 YES | the outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK CAPTURE (the kept live package oEDHTRPq.. downloaded and hash-checked) plus the pre-act sweep of every live worktree's open deploys and the change-management ledger | base64 sha equality + kept path + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | PRE-ACT CAPTURES immediately before the apply: the route baseline (timed, with request ids) and aw4_capture.py (95 names' live Thesis payloads, local and uncommitted), in sequence, no other reader | capture counts, bytes per name min/median/max/margin, statuses, durations |  | OPEN |
| L5 | verify | BUILD from the DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; every changed member admitted by blob; any other member is a STOP | build sha + the whole content-diff list + off-list count + each blob |  | OPEN |
| L6 | activation | upload the built file, then ONE untargeted safe-apply on infra/aws/terraform/harvest/ with the plan read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L7 | verify | new CodeSha256 differs from oEDHTRPq and equals the built file's; AC1 (bd-1's serve kept), AC2 (ay4_compare Branch A), AC3 (no-regression, dossier /15) on the live function | get-function-configuration + the live check outputs |  | OPEN |
| L8 | verify | post-apply thesis capture and route replay, single reader: thesis changed paths only under model.team_sheet and clocks, bytes per name within the name's own team_sheet delta, max under 6291456; every replay request over 20 s re-invoked 3x (200, identical bytes) and recorded | the changed-path list, the bytes per name, the slow-request record |  | OPEN |
| L9 | git | the record step: record-terraform-deploy.sh; entry printed before and after | commit hash + the entry's fields after |  | OPEN |
| L10 | verify | AC1, AC2, AC3 as run; the CodeSha256 and apply time reported to the issuer; the pin worktree left for the issuer | every criterion's output lines + exit=0 |  | OPEN |

## Log

- 20261012T024302Z OPENED by 0.7.0_AE_CloudOps~RA1 with 10 leg(s)
