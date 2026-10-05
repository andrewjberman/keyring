# Deploy Completion Record
**Date opened:** 2026-10-05T23:16:06.903109+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 72 AMGT-av-8: THREE legs in order on opal-amgt-scoped-api -- grant (filings/v1 read + dynamodb:BatchGetItem), then code at 7889ef1ae4 carrying av-1..av-7, then the NARROW drafting evidence splice on 2 keys. AMENDMENT 1 removed the pool universe write (row Z-W243-S1). AMENDMENT 2 made the drafting leg a narrow splice, NOT a rebuild. CTO conditions 1-7 @94dea6af08; condition 1 makes grant-before-code load-bearing. The one open entry naming this function, amgt-corpus-r36-al5 (2.0.0_SA_COO~X, on branch wk-oplgtw-15-r16 only), was ruled dead and non-blocking by the issuer at msg 29756 and is re-verified unchanged here: still OPEN, 0 of 4 legs proven, window expired 20.7h ago.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + open_deploys union over every live worktree | CodeSha256 wbIT0PHvxKIgJvgVy+u0XhLuSXFK5dUE/wypJPDcf8o= and MemorySize 1769 unchanged; per-tree denominator printed for every live worktree, 0 unresolved |  | OPEN |
| L1 | activation | GRANT LEG: two edits in infra/aws/terraform/harvest/scoped-amgt-api.tf then ONE safe-apply targeted at aws_iam_role_policy.scoped_amgt_api_grants | plan is exactly ONE in-place update of that policy, anything else a STOP; r72_grant_av8.sh reads 'R72 AV8 GRANT: YES' with C1/C2/C3 allowed beside the three controls; the stale 'NOT BatchGetItem' comment at :343-349 names the batch reader |  | OPEN |
| L2 | verify | CODE LEG build at 7889ef1ae4 from a clean detached checkout, CONTENT-DIFF vs deployed wbIT0PHv | exactly CHANGED lib/research/api/scoped_amgt.py + lib/research/api/monthly_chatter.py + lib/research/print/render_pack.py, ADDED lib/research/peers/numeric_tickers.py, REMOVED none; size under 262144000 B |  | OPEN |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object |  | OPEN |
| L4 | activation | opal-amgt-scoped-api code-only safe-apply | full-plan show -json: exactly 1 update (the function), 0 destroy/route/gateway and no IAM beyond the landed grant; memory 1769; live CodeSha256 = the new build; then leadpanel_cold_warm.py --label after at once |  | OPEN |
| L5 | verify | DRAFTING SPLICE LEG: drafting_evidence_splice.py --keys BA_US_Equity,ASML_NA_Equity --write, pre-act bytes saved first | --dry-run printed 'SPLICE: YES'; BEFORE VersionIds BA .zSrn_broPgdErEesbpfY8lJH5RMBCSb and ASML kQZePsmgbJlF1Tnvf3t2ljwqNnW9wrYX; a NEW VersionId per key read back, diff exactly .evidence_records and .denominators.evidence_records, every other top-level field byte-equal to the pre-act object |  | OPEN |
| L6 | verify | AC1 c39/c41/c43/c44/c45, AC2 c42 after the splice, AC3 r71 c34/c36/c38 + r70 c30-c33, AC4 the grant | each criterion SERVED YES on deployed with exit=0; AC4 'R72 AV8 GRANT: YES'; leadpanel after output captured |  | OPEN |

## Log

- 20261005T231606Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
