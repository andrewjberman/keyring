# Deploy Completion Record
**Date opened:** 2026-10-16T06:31:57.928025+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW TO-OG-ap-26 Phase B: move the etf-classifications dynamodb:GetItem grant from opal-gateway-role to gateway-global-internal-reader-role (1 add, 0 change, 1 destroy, one replacement), safe-apply targeted, both ends read back; .tf sha256-16 867087958bac89b9, ask 69466be19798; halves CTO 4d0a8d3c0d, COO 90b589c58f, CVO f2cf55e41e; GO msg 34769
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | replace the policy then get-role-policy on the internal reader and list-role-policies on the instance role | present on the internal reader (one statement GetItem, table ARN) and absent from opal-gateway-role |  | OPEN |
| S1 | verify | simulate-principal-policy one resource per call with controls, describe-table | internal reader GetItem allowed, Scan not allowed, instance role GetItem not allowed |  | OPEN |
| V1 | verify | targeted re-plan of the one policy | No changes |  | OPEN |

## Log

- 20261016T063157Z OPENED by 0.7.0_AE_CloudOps~ZS with 3 leg(s)
