# Deploy Completion Record
**Date opened:** 2026-10-11T22:01:29.727470+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-be-1: ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin a03d92221a (box/dell1 first-parent) carrying AMGT_CORPUS's /13 corpus files (dossier.py 13463426d0da METHOD /13, team_sheet.py, template.py, factset_descriptions.json, plus opal_naming.py, analyze.py and two registry files), bd-1's scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c KEPT; pair COO half @926aa022b4 + CTO half (msg 4135); GO msg 4141
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: a03d92221a is a box/dell1 first-parent commit, not a scratch pin and not HEAD; r94_admission_table.py a03d92221a --pin 08d5ea2920 shows exactly the half's six lib members and two registry files at the half's blobs with scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c byte-equal to the live package (a seventh member or a different api blob is a STOP); r94_naming_replay.py --pin 08d5ea2920 YES | the outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK CAPTURE (the kept live package IpaCHo5h.. downloaded and hash-checked) plus the pre-act sweep of every live worktree's open deploys and the change-management ledger | base64 sha equality + kept path + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | PRE-ACT CAPTURES immediately before the apply: aw4_capture.py (95 names' live Thesis payloads, local and uncommitted) and the route baseline (527 requests: the four table scripts' requests plus coverage and compare); the half's own measurement is the prediction | capture counts, bytes per name min/median/max/margin, statuses |  | OPEN |
| L5 | verify | BUILD from the DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; every changed member admitted by blob; any other member is a STOP | build sha + the whole content-diff list + off-list count + each blob |  | OPEN |
| L6 | activation | upload the built file, then ONE untargeted safe-apply on infra/aws/terraform/harvest/ with the plan read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L7 | verify | new CodeSha256 differs from IpaCHo5h and equals the built file's; AC1 (bd-1's serve kept), AC2 (aw4_compare Branch A), AC3 (no-regression, dossier /13) on the live function | get-function-configuration + the live check outputs |  | OPEN |
| L8 | verify | post-apply compare of EVERY route baseline request (0 changed paths expected outside the thesis) and the thesis payloads: changed paths only under model.team_sheet and generation clocks, bytes per name within the name's own team_sheet delta, max under 6291456 | the changed-path list, the bytes per name, the not-moved denominators |  | OPEN |
| L9 | git | the record step: record-terraform-deploy.sh; entry printed before and after | commit hash + the entry's fields after |  | OPEN |
| L10 | verify | AC1, AC2, AC3 as run; the CodeSha256 and apply time reported to the issuer; both scratch branches kept | every criterion's output lines + exit=0 |  | OPEN |

## Log

- 20261011T220129Z OPENED by 0.7.0_AE_CloudOps~RA1 with 10 leg(s)
