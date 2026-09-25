# Deploy Completion Record
**Date opened:** 2026-09-25T16:00:05.310356+00:00
**Status:** OPEN
**Deploy:** Export section A3: V3 auth-validator-edge with the render branch + exp fix (new Lambda@Edge version, distribution repointed)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_lambda_function.auth_validator_edge[0] + aws_cloudfront_distribution.portal association | new version published from artifact Mfo4c4PG..; LIVE distribution EVTSA9VEHNZVH associates that version on all 26 behaviors (was 20) |  | OPEN |
| N1 | verify | negative arm before and after | unauthenticated scoped API request refused before and after; human Auth OK continues in the edge log with no runtime errors |  | OPEN |
| V1 | verify | targeted re-plan | No changes |  | OPEN |

## Log

- 20260925T160005Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
