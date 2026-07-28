# Deploy Completion Record
**Date opened:** 2026-07-28T20:22:09.413875+00:00
**Status:** OPEN
**Deploy:** Stage-6 cottonwood gold grants on mdpf_runner (3 grants: Put+Get on blackdiamond/cottonwood/gold/*, prefix-conditioned ListBucket) -- CTO dispatch 201342Z, AE-base pre-computed 194533Z
**Authored by:** 0.7.0_AE_CloudOps~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of iam.tf | commit hash pushed |  | OPEN |
| L2 | activation | targeted terraform apply -target=aws_iam_role_policy.mdpf_runner | safe-apply output + 0-diff re-plan |  | OPEN |
| L3 | verify | applied truth via aws iam get-role-policy | both Sids present in the LIVE policy document |  | OPEN |
| L4 | verify | 6-control simulate battery T1/T2/T3 allowed + C1/C2/C3 denied, ISOLATED invocations | per-control verdict incl. C3 explicitDeny on json/mdpf serve |  | OPEN |

## Log

- 20260728T202209Z OPENED by 0.7.0_AE_CloudOps~C with 4 leg(s)
