# Deploy Completion Record
**Date opened:** 2026-08-29T02:14:38.492471+00:00
**Status:** OPEN
**Deploy:** D1_CATVIEWS second reland + refire (Andrew-direct 'everything must be done tonight', 15087). RESERVED-CATEGORY S3 DELETE then floor re-run then publish then served-body verify. OPENED BEFORE THE ACT and while still GATED: L1 open means the delete has NOT happened -- leg state, not the window, distinguishes 'waiting on items 1/2' from 'stranded mid-deploy'. Window 6h covers the gated wait plus execution; extend rather than let it false-RED.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | RESERVED DELETE of the conflict-held dated gold keys under portal/gold/mdpf/ | the PRE-READ enumeration and the live dry-run enumeration printed and DIFFED identical before --confirm |  | OPEN |
| L2 | activation | mdpf-gold-lambda floor re-run rebuilds the deleted keys | floor status green + a4_objects_built + run manifest key |  | OPEN |
| L3 | activation | opal-assets-mdpf-portal-publisher publishes gold to platinum | publisher return: published/failed/missing_pairs |  | OPEN |
| L4 | verify | VERIFY-A: the SERVED category-views BODIES per scope, with denominators | verify_step3_served_category_views.py rc captured UN-PIPED, verdict and rc agreeing, and the as_of each body carries |  | OPEN |

## Log

- 20260829T021438Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
