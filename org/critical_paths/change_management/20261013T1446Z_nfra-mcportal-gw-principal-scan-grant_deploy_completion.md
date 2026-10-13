# Deploy Completion Record
**Date opened:** 2026-10-13T14:46:12.836192+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-z-4: one dynamodb:Scan grant on gateway-access-state-table for opal-gateway-role (never-widen pair SIGNED: CTO~Z @d9b228d530, COO~MP @b12118d890)
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_iam_role_policy.gw_access_state_principal_scan (safe-apply of the saved targeted plan .build/z4.tfplan) | terraform apply output showing 1 added 0 changed 0 destroyed, plus a 0-diff targeted re-plan |  | OPEN |
| L2 | verify | live IAM read-back of gateway-access-state-principal-scan-policy on opal-gateway-role | z4.AC1.sh RESULT: PASS -- actions=dynamodb:Scan resources=1 problems=0 and 4 of 4 simulation arms |  | OPEN |

## Log

- 20261013T144612Z OPENED by 0.7.0_AE_CloudOps~MQ with 2 leg(s)
