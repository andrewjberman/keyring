# Deploy Completion Record
**Date opened:** 2026-10-11T17:32:18.919506+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-aa-5: ONE code leg redeploying opal-amgt-scoped-api at build pin b3512d18fb (scratch/r95-aa5-pin = the live pin 15b7af1601 plus scoped_amgt.py ec7c8fde988b and monthly_chatter.py 5243b870cac5 only) -- the withheld classification of a disagreeing table row (AMGT-aa-2) and CSL/JD initialism casing (AMGT-aa-4); pair COO half @b38de315e7 + CTO half (msg 4042); GO msg 4043
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: b3512d18fb is on scratch/r95-aa5-pin, 15b7af1601 an ancestor, the diff is exactly two files; r94_admission_table.py b3512d18fb --pin 15b7af1601 shows exactly two members differing at the half's blobs (a third is a STOP); r94_naming_replay.py YES | the three outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK CAPTURE (the kept live package VNcX9ntm.. downloaded and hash-checked) plus the pre-act sweep of every live worktree's open deploys and the change-management ledger | base64 sha equality + kept path + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | PRE-ACT PREDICTION (the three table scripts and r95_series_by_ticker_table.py in LOCAL mode against the pin's worktree) equals the half (39 name and classification paths, 0 outside) and BASELINES re-read immediately before the apply (all requests the table names) | prediction counts by route + baseline request count and statuses |  | OPEN |
| L5 | verify | BUILD from the DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; every changed member admitted by blob; any other member is a STOP | build sha + the whole content-diff list + off-list count + each blob |  | OPEN |
| L6 | activation | upload the built file, then ONE untargeted safe-apply on infra/aws/terraform/harvest/ with the plan read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L7 | verify | new CodeSha256 differs from VNcX9ntm and equals the built file's; 0-diff re-plan; AC1 classification census + casing, AC2 no-regression arm, AC3 minor-unit census, on the live function | get-function-configuration + the live check outputs |  | OPEN |
| L8 | verify | post-apply compare of EVERY baseline request: the changed paths equal the half's table path by path (39 name and classification paths on SAN_FP and CSL_AU), the not-moved set equal (every other classification, score, rank, peer member) | the changed-path list with before and after, the not-moved denominators |  | OPEN |
| L9 | git | the record step: record-terraform-deploy.sh; entry printed before and after | commit hash + the entry's fields after |  | OPEN |
| L10 | verify | AC1, AC2, AC3 as run; the CodeSha256 and apply time reported to the issuer for 2.0.0_SA_COO~C1 | every criterion's output lines + exit=0 |  | OPEN |

## Log

- 20261011T173218Z OPENED by 0.7.0_AE_CloudOps~RA1 with 10 leg(s)
