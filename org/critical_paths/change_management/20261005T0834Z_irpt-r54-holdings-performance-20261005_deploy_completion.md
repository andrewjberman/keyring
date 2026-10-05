# Deploy Completion Record
**Date opened:** 2026-10-05T08:34:19.405313+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND release r54 (reduced): irpt-holdings-performance-lambda handler.py (IB-pr-320 S297/W123-S1), INF after its 14:00Z fire; CTO half @f342ba6664 + msg 105217, COO half
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | before-read CodeSha256 = 0PuFBxdJSbFH (both functions) | get-function-configuration | before-read ~08:3xZ: irpt-holdings-performance-lambda and irpt-inf-holdings-performance-lambda CodeSha256 0PuFBxdJSbFHNJ9+Z3weyzLvXyZhgZFk2dkGAbIYb/0= = anchor; artifact key version IPBj.bgy462CO8neYf4rAZiaiTja9YVc (versioning Enabled). Baseline OLD code (source schwab_08335338, dry_run): dated 2026-10-01 rc 0; undated planned [2026-10-02] rc 0 | CLOSED 20261005T083932Z |
| B1 | s3-prefix | build-and-upload investor-reporting irpt-holdings-performance-lambda (shared key) | upload verify line + new sha | build-and-upload investor-reporting irpt-holdings-performance-lambda: SHA256 DaDtnTCqCohjzipgmkabSBgixfn3/xM3+gvvnmYAQ0A= (= the census BUILD_ONLY sha); s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings-performance-lambda.zip write VERIFIED size=139553 | CLOSED 20261005T084405Z |
| A1 | activation | targeted safe-apply module.irpt_holdings_performance.aws_lambda_function.this | live CodeSha256 = built sha; INF unchanged | safe-apply targeted 10:08Z under TAGAUTHZ_OVERRIDE (CTO batch 259; audited INTENT id=20261005T100734Z-64084): Apply complete 0/1/0; live irpt-holdings-performance-lambda CodeSha256 DaDtnTCqCohjzipgmkabSBgixfn3/xM3+gvvnmYAQ0A= (= built), LastModified 2026-10-05T10:08:32Z, Successful; INF unchanged 0PuFBxdJ | CLOSED 20261005T101414Z |
| R1 | git | record-terraform-deploy | commit hash | record-terraform-deploy investor-reporting --function irpt-holdings-performance-lambda --code-sha256 DaDtnTCq..: committed d0e344ba38 (ci: record deploy investor-reporting @ a56f22ea) | CLOSED 20261005T101815Z |
| V1 | verify | change invoke dry_run (TARGET_ALREADY_LANDED or rc 0) + happy-path dated dry_run rc 0 | invoke payloads | NEW code invokes (source schwab_08335338, dry_run): undated planned [2026-10-02] rc 0 (landed max 2026-10-01 of 561 per the handler's own lister, so 10-02 is not landed and the non-empty branch is correct, = baseline); dated 2026-10-01 rc 0 (= baseline). No FunctionError. The TARGET_ALREADY_LANDED branch is not reachable live until a target lands (unit-tested W123-S1) | CLOSED 20261005T101414Z |
| A2 | activation | INF targeted apply after the 14:00Z fire is read (W80-S1) | live CodeSha256 |  | OPEN |

## Log

- 20261005T083419Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20261005T083932Z LEG S1 closed: before-read ~08:3xZ: irpt-holdings-performance-lambda and irpt-inf-holdings-performance-lambda CodeSha256 0PuFBxdJSbFHNJ
- 20261005T084405Z LEG B1 closed: build-and-upload investor-reporting irpt-holdings-performance-lambda: SHA256 DaDtnTCqCohjzipgmkabSBgixfn3/xM3+gvvnmYAQ0A
- 20261005T101414Z LEG A1 closed: safe-apply targeted 10:08Z under TAGAUTHZ_OVERRIDE (CTO batch 259; audited INTENT id=20261005T100734Z-64084): Apply comp
- 20261005T101414Z LEG V1 closed: NEW code invokes (source schwab_08335338, dry_run): undated planned [2026-10-02] rc 0 (landed max 2026-10-01 of 561 per 
- 20261005T101815Z LEG R1 closed: record-terraform-deploy investor-reporting --function irpt-holdings-performance-lambda --code-sha256 DaDtnTCq..: committ
