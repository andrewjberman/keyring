# Deploy Completion Record
**Date opened:** 2026-09-27T21:37:21.557169+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter role: render-grant kms:Decrypt under the S3 Bucket Key (bucket-ARN context, core key only); backend <kms commit>; CTO 102135; policy only 0/1/0; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | performance root safe-apply | both halves at HEAD naming the packet blob; plan 0/1/0 this policy only; safe-apply; live policy readback equal; simulator positive + negative arms; replan 0 |  | OPEN |
| A1 | verify | next K8 window | the render's Performance read as RENDER_DELEGATE succeeds (no AccessDenied); READY %PDF |  | OPEN |

## Log

- 20260927T213721Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
