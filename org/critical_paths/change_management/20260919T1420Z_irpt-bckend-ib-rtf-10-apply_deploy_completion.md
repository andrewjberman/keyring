# Deploy Completion Record
**Date opened:** 2026-09-19T14:20:14.245768+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-10 fourth pass (msg 98264): arm (e) APPLY of the 7 roots packet blob c3a44074d2dabe4292bfc648d855be4b99fe48db signs (COO half @025607941e, CTO half @b6af01c2f4) -- K-OM 6 + K-DIR 4 + K-ENV 6 + K-CODE 1 (irpt-directory-search -> HOpXPDo...); saved planfiles applied through .tools/safe-apply.sh after the packet-s11 pre-checks; 0 to destroy; rollback per packet s7
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/directory (K-OM directory role + K-CODE irpt-directory-search + directory-refresh object version) | pre-apply digest == 0f66bef1 + safe-apply rc=0 Apply complete |  | OPEN |
| L2 | activation | infra/aws/terraform/investor-reporting/ops (K-OM status role + K-ENV irpt-status) | pre-apply digest == a9197cc1 + safe-apply rc=0 |  | OPEN |
| L3 | activation | infra/aws/terraform/investor-reporting/holdings (K-ENV irpt-holdings) | pre-apply digest == 450a1ab8 + safe-apply rc=0 |  | OPEN |
| L4 | activation | infra/aws/terraform/investor-reporting/narrative (K-OM + K-DIR + K-ENV) | pre-apply digest == 5e0e1ed7 + safe-apply rc=0 |  | OPEN |
| L5 | activation | infra/aws/terraform/investor-reporting/export (K-OM + K-DIR + K-ENV) | pre-apply digest == 527c2a50 + safe-apply rc=0 |  | OPEN |
| L6 | activation | infra/aws/terraform/investor-reporting/performance (K-OM + K-DIR + K-ENV) | pre-apply digest == 5059fda3 + safe-apply rc=0 |  | OPEN |
| L7 | activation | infra/aws/terraform/investor-reporting/ycharts (K-OM + K-DIR + K-ENV irpt-ycharts-generate) | pre-apply digest == 063b9919 + safe-apply rc=0 |  | OPEN |
| L8 | verify | the 7 roots post-apply | a fresh plan per root reads No changes (0-diff) 7 of 7 |  | OPEN |

## Log

- 20260919T142014Z OPENED by 0.7.0_AE_CloudOps~V with 8 leg(s)
