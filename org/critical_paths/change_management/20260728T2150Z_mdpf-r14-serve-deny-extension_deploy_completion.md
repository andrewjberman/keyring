# Deploy Completion Record
**Date opened:** 2026-07-28T21:50:05.431444+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260728T215800Z
**Deploy:** R14: extend the principal-scoped serve deny to json/portfolios/{aum-metrics,account-distribution}.json -- LATENT-CAPABILITY FENCE ONLY (CTO 213109Z GO, 214924Z proceed)
**Authored by:** 0.7.0_AE_CloudOps~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of iam.tf | commit hash pushed | commit aa739a36eb (iam.tf + ledger), author 0.7.0_AE_CloudOps~C | CLOSED 20260728T215800Z |
| L2 | activation | targeted apply -target=aws_iam_role_policy.mdpf_runner | safe-apply output + 0-diff re-plan, row 10 held back | safe-apply -target=aws_iam_role_policy.mdpf_runner: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' comp-tagauthz SELF-RAN and PASSED, zero override. Targeted re-plan: No changes. Full plan still shows ONLY row 10's four pending -- tree still FROZEN. | CLOSED 20260728T215800Z |
| L3 | verify | applied truth via get-role-policy | new Sid present in the LIVE policy document | aws iam get-role-policy: 26 statements; Sid R14LatentFenceOnlyNOTAPROTECTIONRunnerIsNotADemonstratedWriterObservedWriterUnidentified20260728 LIVE with both literal keys; both pre-existing P0 Denies unchanged. The warning Sid RENDERS IN FULL on the applied plane -- a get-role-policy reader cannot miss it (a TF comment would have been invisible). | CLOSED 20260728T215800Z |
| L4 | verify | 5-control battery D1/D2 explicitDeny, P1/P2 allowed, C1 unmoved, ISOLATED | per-control verdict; P1 is the one that matters | 6 ISOLATED invocations, one --resource-arns each. PRE-APPLY: D1 allowed, D2 allowed, P1 allowed. POST: P1 platinum/mdpf/aggregate_aua/2026-07-29.json=allowed (THE ONE THAT MATTERS -- chain not broken); D1 aum-metrics=explicitDeny; D2 account-distribution=explicitDeny; P2 assets gold/mdpf_revamp/cottonwood=allowed; C1 json/mdpf/global=explicitDeny UNMOVED; C2 [added by me] account_distribution.json UNDERSCORE twin=allowed, proving the literal-key choice did not over-deny a different older object. | CLOSED 20260728T215800Z |

## Log

- 20260728T215005Z OPENED by 0.7.0_AE_CloudOps~C with 4 leg(s)
- 20260728T215800Z LEG L1 closed: commit aa739a36eb (iam.tf + ledger), author 0.7.0_AE_CloudOps~C
- 20260728T215800Z LEG L2 closed: safe-apply -target=aws_iam_role_policy.mdpf_runner: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' comp-t
- 20260728T215800Z LEG L3 closed: aws iam get-role-policy: 26 statements; Sid R14LatentFenceOnlyNOTAPROTECTIONRunnerIsNotADemonstratedWriterObservedWriter
- 20260728T215800Z LEG L4 closed: 6 ISOLATED invocations, one --resource-arns each. PRE-APPLY: D1 allowed, D2 allowed, P1 allowed. POST: P1 platinum/mdpf/
- 20260728T215800Z CLOSED -- all 4 legs proven
