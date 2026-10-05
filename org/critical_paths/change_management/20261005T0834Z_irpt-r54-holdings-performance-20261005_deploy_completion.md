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
| B1 | s3-prefix | build-and-upload investor-reporting irpt-holdings-performance-lambda (shared key) | upload verify line + new sha |  | OPEN |
| A1 | activation | targeted safe-apply module.irpt_holdings_performance.aws_lambda_function.this | live CodeSha256 = built sha; INF unchanged |  | OPEN |
| R1 | git | record-terraform-deploy | commit hash |  | OPEN |
| V1 | verify | change invoke dry_run (TARGET_ALREADY_LANDED or rc 0) + happy-path dated dry_run rc 0 | invoke payloads |  | OPEN |
| A2 | activation | INF targeted apply after the 14:00Z fire is read (W80-S1) | live CodeSha256 |  | OPEN |

## Log

- 20261005T083419Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20261005T083932Z LEG S1 closed: before-read ~08:3xZ: irpt-holdings-performance-lambda and irpt-inf-holdings-performance-lambda CodeSha256 0PuFBxdJSbFHNJ
