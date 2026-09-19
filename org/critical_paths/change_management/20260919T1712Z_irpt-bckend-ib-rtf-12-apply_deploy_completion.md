# Deploy Completion Record
**Date opened:** 2026-09-19T17:12:02.797721+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-12 third pass (msg 98296): arm (e) APPLY of the 6 roots packet blob 9d273fb8517a00288ec13d8dd0814a47af8782fa signs (COO half @71d5098fd9, CTO half @f62dd3e5bb) -- K-CODE x 6 (the raw_keys.json/firm_registry.json members), saved planfiles through .tools/safe-apply.sh after the packet-s9 pre-checks; 0 to destroy; rollback per packet s5
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/directory (K-CODE irpt-directory-search -> PUjH3OjD...) | pre-apply digest == d26db7c0 + safe-apply rc=0 of the SAVED planfile |  | OPEN |
| L2 | activation | infra/aws/terraform/investor-reporting/ops (K-CODE irpt-status -> O3TyGqfq...) | pre-apply digest == 82b6c8ef + safe-apply rc=0 of the SAVED planfile |  | OPEN |
| L3 | activation | infra/aws/terraform/investor-reporting/holdings (K-CODE irpt-holdings -> uS+WBeNx...) | pre-apply digest == 9635d3b9 + safe-apply rc=0 of the SAVED planfile |  | OPEN |
| L4 | activation | infra/aws/terraform/investor-reporting/narrative (K-CODE irpt-narrative -> o4newc7E...) | pre-apply digest == a292e378 + safe-apply rc=0 of the SAVED planfile |  | OPEN |
| L5 | activation | infra/aws/terraform/investor-reporting/export (K-CODE irpt-export-render -> 9IMayS94...) | pre-apply digest == 328dab19 + safe-apply rc=0 of the SAVED planfile |  | OPEN |
| L6 | activation | infra/aws/terraform/investor-reporting/performance (K-CODE irpt-performance-adapter -> IHosoGqG...) | pre-apply digest == 3ab3ce3d + safe-apply rc=0 of the SAVED planfile |  | OPEN |
| L7 | verify | the 7 roots post-apply (ycharts not applied, S102) | a fresh plan per root reads No changes (0-diff) 7 of 7 |  | OPEN |

## Log

- 20260919T171202Z OPENED by 0.7.0_AE_CloudOps~V with 7 leg(s)
