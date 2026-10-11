# Deploy Completion Record
**Date opened:** 2026-10-11T20:15:44.482566+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bd-2: ONE code leg redeploying opal-amgt-scoped-api at build pin 08d5ea2920 (scratch/r97-bd2-pin, parented on the live build input b3512d18fb, plus scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c only) -- a withheld listing's own sector served by listing key with source and as-of (AMGT-bd-1); pair COO half @741fd2d8fd + CTO half (msg 4094); GO msg 4096
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: 08d5ea2920 is on scratch/r97-bd2-pin and parented on b3512d18fb, the diff is exactly two files; r94_admission_table.py 08d5ea2920 --pin b3512d18fb shows exactly scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c (a third is a STOP); r94_naming_replay.py --pin b3512d18fb YES | the three outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK CAPTURE (the kept live package TmeKvn83.. downloaded and hash-checked) plus the pre-act sweep of every live worktree's open deploys and the change-management ledger | base64 sha equality + kept path + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | PRE-ACT PREDICTION (the four table scripts and r97_sector_serve_census.py in LOCAL mode against the pin's worktree) equals the half (41 sector paths on SAN_FP and CSL_AU, 0 outside) and BASELINES re-read immediately before the apply | prediction counts by route + baseline request count and statuses |  | OPEN |
| L5 | verify | BUILD from the DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; every changed member admitted by blob; any other member is a STOP | build sha + the whole content-diff list + off-list count + each blob |  | OPEN |
| L6 | activation | upload the built file, then ONE untargeted safe-apply on infra/aws/terraform/harvest/ with the plan read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L7 | verify | new CodeSha256 differs from TmeKvn83 and equals the built file's; AC1 sector serve census, AC2 no-regression arm, AC3 currency and casing, on the live function | get-function-configuration + the live check outputs |  | OPEN |
| L8 | verify | post-apply compare of EVERY baseline request: the changed paths equal the half's table path by path (41 sector paths on SAN_FP and CSL_AU), the not-moved set equal (every classification, name, score, rank, peer member) | the changed-path list with before and after, the not-moved denominators |  | OPEN |
| L9 | git | the record step: record-terraform-deploy.sh; entry printed before and after | commit hash + the entry's fields after |  | OPEN |
| L10 | verify | AC1, AC2, AC3 as run; the CodeSha256 and apply time reported to the issuer for 2.0.0_SA_COO~C1; both scratch branches kept | every criterion's output lines + exit=0 |  | OPEN |

## Log

- 20261011T201544Z OPENED by 0.7.0_AE_CloudOps~RA1 with 10 leg(s)
