# Deploy Completion Record
**Date opened:** 2026-09-22T04:05:19.521474+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtk-1: publish C-S158/C-S159-repaired capture-session.cjs to render host artifact prefix (capture-session.sh unchanged, not republished; host stopped, no on-host verify). Blob ded60502/sha256 f03666ef, changed at 0d0c8cdc4d. Never-widen packet 5d30a76a, both halves signed (2.0.0_SA_COO~B @cf4da2c5b3, 1.0.0_SA_CTO).
**Authored by:** 0.9.0_WK_IRPT_BCKEND~13
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.cjs | S3 readback sha256 == f03666ef827e7c6a169214c83b2a4fe593d7f1cbf181f728f1febb0235eacd0d |  | OPEN |

## Log

- 20260922T040519Z OPENED by 0.9.0_WK_IRPT_BCKEND~13 with 1 leg(s)
