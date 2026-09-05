# Deploy Completion Record
**Date opened:** 2026-09-05T02:39:34.284238+00:00
**Status:** OPEN
**Deploy:** EG-s-7: lambda:InvokeFunction on the three ETFS producers for etfs-reports-reporter-role (targeted: aws_iam_role_policy.reporter only)
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| iam | activation | etfs-reports-reporter-role | get-role-policy shows Sid InvokeProducersForRemediation with the three producer ARNs (applied BY TARGET: -target=aws_iam_role_policy.reporter; aws_instance.reporter's pre-existing user_data drift is NOT touched by this leg) |  | OPEN |

## Log

- 20260905T023934Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~1 with 1 leg(s)
