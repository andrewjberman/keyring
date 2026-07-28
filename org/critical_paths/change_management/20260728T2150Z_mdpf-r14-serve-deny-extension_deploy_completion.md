# Deploy Completion Record
**Date opened:** 2026-07-28T21:50:05.431444+00:00
**Status:** OPEN
**Deploy:** R14: extend the principal-scoped serve deny to json/portfolios/{aum-metrics,account-distribution}.json -- LATENT-CAPABILITY FENCE ONLY (CTO 213109Z GO, 214924Z proceed)
**Authored by:** 0.7.0_AE_CloudOps~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of iam.tf | commit hash pushed |  | OPEN |
| L2 | activation | targeted apply -target=aws_iam_role_policy.mdpf_runner | safe-apply output + 0-diff re-plan, row 10 held back |  | OPEN |
| L3 | verify | applied truth via get-role-policy | new Sid present in the LIVE policy document |  | OPEN |
| L4 | verify | 5-control battery D1/D2 explicitDeny, P1/P2 allowed, C1 unmoved, ISOLATED | per-control verdict; P1 is the one that matters |  | OPEN |

## Log

- 20260728T215005Z OPENED by 0.7.0_AE_CloudOps~C with 4 leg(s)
