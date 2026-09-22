# Deploy Completion Record
**Date opened:** 2026-09-22T01:37:14.492812+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtj-1: publish C-S153-repaired capture-session.cjs to render host artifact prefix (capture-session.sh unchanged, not republished; host stopped, no on-host verify). Blob c5a18898/sha256 defcb585, changed at bfe67b1eab. Never-widen packet 2450320a, both halves signed (2.0.0_SA_COO~B @5b67db0397, 1.0.0_SA_CTO @088669b331).
**Authored by:** 0.9.0_WK_IRPT_BCKEND~13
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.cjs | S3 readback sha256 == defcb58572276f36036d610d296f53df32f86477ffb3e6b17aab00c6f6c2d95a |  | OPEN |

## Log

- 20260922T013714Z OPENED by 0.9.0_WK_IRPT_BCKEND~13 with 1 leg(s)
