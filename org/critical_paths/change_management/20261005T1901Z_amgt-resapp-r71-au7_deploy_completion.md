# Deploy Completion Record
**Date opened:** 2026-10-05T19:01:00.830768+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 71 AMGT-au-7: ONE code-only redeploy of opal-amgt-scoped-api at a53eaf74c5 carrying au-1/au-3/au-4/au-6. Gold leg removed by AMENDMENT 1 (HARVST is the gold table's one writer). Issuer ruling msg 29756 (2.0.0_SA_COO~Z): the OPEN AMGT_CORPUS amgt-corpus-r36-al5 entry is measured dead and does not block -- window expired 02:34Z, its base aoQ+WrefJ not live, function redeployed since by at-6.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + build at a53eaf74c5 from a clean detached checkout | base GS//XHnVd4+bBIg1VU++r1fp9v495pi6jKFat9KbEYE= and memory 1769 unchanged; CONTENT-DIFF exactly CHANGED lib/research/api/scoped_amgt.py + lib/research/harvest/publication_gold.py, ADDED lib/research/api/served_cache.py, REMOVED none; size under 262144000 B |  | OPEN |
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object |  | OPEN |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply | full-plan show -json: exactly 1 update (the function), 0 destroy/IAM/route/gateway; memory 1769; live CodeSha256 = the new build |  | OPEN |
| L3 | verify | AC1 c34/c36 + AC3 regressions on deployed; AC2 c38 reported only; leadpanel_cold_warm.py --label after | AC1 SERVED YES on c34 and c36; AC3 r70 c30-c33, r69 c29, r67 c23-c26 unchanged; c38 warm min/max per read reported; leadpanel after output captured |  | OPEN |

## Log

- 20261005T190100Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
