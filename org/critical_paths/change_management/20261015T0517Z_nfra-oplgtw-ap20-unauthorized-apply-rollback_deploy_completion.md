# Deploy Completion Record
**Date opened:** 2026-10-15T05:17:10.079028+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-20: ROLLBACK of an UNAUTHORIZED apply -- gateway-global-etfs-read-policy was applied during Phase A, which forbids any apply, with no ledger and no signed halves. 0.7.0_AE_CloudOps~Z's own error.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the unauthorized state is MEASURED before it is touched: gateway-global-etfs-read-policy live on gateway-global-internal-reader-role, and the role's other three policies read at their pre-act statement counts | get-role-policy on all four, with the document of the unauthorized one captured |  | OPEN |
| L2 | activation | the policy is DESTROYED through safe-apply, targeted, restoring the state the halves will sign from | safe-apply output showing 1 destroyed, 0 added, 0 changed |  | OPEN |
| L3 | verify | the policy is GONE and the role's other three are untouched | get-role-policy returns NoSuchEntity for the destroyed name, and the other three read their pre-act statement counts and resource lists |  | OPEN |

## Log

- 20261015T051710Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
