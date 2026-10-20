# Deploy Completion Record
**Date opened:** 2026-10-20T01:06:44.494127+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-cw-6: Cottonwood retained-key release -- runner bundle (directory_runner.py f2d2329d39a1) FIRST, then irpt-directory-refresh zip (refresh.py 304eb35580ee) and the directory root apply
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | runner bundle s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz via safe-deploy (Branch B: VersionId 7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB, ETag 643410f6) | version before and after, every member equal to HEAD |  | OPEN |
| L2 | s3-prefix | irpt-directory-refresh zip built digest 3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g= uploaded and head-object verified (Branch B: S3 version zvhYGi4jAIJtLIQOXw4.EYKkuA_pIU8w, CodeSha256 I7T8wRYm) | digest, head-object |  | OPEN |
| L3 | tf-lambda | directory root plan 0/1/0 on module.irpt_directory_refresh.aws_lambda_function.this, ONE safe-apply, clean re-plan | plan counts, replan, CodeSha256, env key names |  | OPEN |
| L4 | verify | record, criteria output and proof committed with explicit paths | commit ids |  | OPEN |

## Log

- 20261020T010644Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
