# Deploy Completion Record
**Date opened:** 2026-09-22T06:05:19.634396+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtl-1: publish C-S170/C-S171-repaired, taxonomy-closed capture-session.cjs to render host artifact prefix (capture-session.sh unchanged, not republished; host stopped, no on-host verify). Blob 82abe684/sha256 b6f75a20, changed at cb6429dc9e. Never-widen packet 3676e2a2, both halves signed (2.0.0_SA_COO~B, 1.0.0_SA_CTO).
**Authored by:** 0.9.0_WK_IRPT_BCKEND~13
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.cjs | S3 readback sha256 == b6f75a20150c170687ef2c1974b0a219a4ba56fc11a457b03b1fa688c68f353c |  | OPEN |

## Log

- 20260922T060519Z OPENED by 0.9.0_WK_IRPT_BCKEND~13 with 1 leg(s)
