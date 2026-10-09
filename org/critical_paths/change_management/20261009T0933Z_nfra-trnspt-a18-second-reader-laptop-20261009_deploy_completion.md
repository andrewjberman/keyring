# Deploy Completion Record
**Date opened:** 2026-10-09T09:33:18.594111+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT a18 second named reader apply from integrated pin f7a4fb5d04efb908b96ab3b8d86277c9b9f982ad carrying f8c4859407, 04313a7e39, dc5032abde
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| APPLY | activation | Terraform targets aws_iam_role.second_reader, aws_iam_policy.second_reader, aws_iam_role_policy_attachment.second_reader, aws_kms_key.transcripts | safe-apply receipt and exact 3 create plus 1 update result |  | OPEN |
| VERIFY | verify | Named reader role, key-policy one-principal delta, admitted/refused S3 proof | role readback, full key-policy diff, ADMITTED and REFUSED statuses only |  | OPEN |

## Log

- 20261009T093318Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)

## Pre-apply plan gate — 2026-10-09T09:44Z

- Apply pin: `f7a4fb5d04efb908b96ab3b8d86277c9b9f982ad`; required ancestors `04313a7e39` and `dc5032abde` both present.
- Targeted plan: `3 to add, 1 to change, 0 to destroy`.
- Changed addresses only: `aws_iam_role.second_reader`, `aws_iam_policy.second_reader`, `aws_iam_role_policy_attachment.second_reader`, `aws_kms_key.transcripts`.
- No Lambda resource change.
- Semantic key-policy comparison: only `NamedReadersUseTheKey` changes; exactly one role principal is added; no principal is removed; `DellAgentUsersGenerateDataKey` is byte-equivalent before/expected-after.

Full key-policy diff:

```diff
--- kms-key-policy.before.json
+++ kms-key-policy.expected-after.json
@@ -35,7 +35,8 @@
       "Effect": "Allow",
       "Principal": {
         "AWS": [
-          "arn:aws:iam::313476888478:user/Andrew_Berman"
+          "arn:aws:iam::313476888478:user/Andrew_Berman",
+          "arn:aws:iam::313476888478:role/teams-global-transcripts-second-reader-role"
         ]
       },
       "Resource": "*",
```

Evidence: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/nfra_trnspt_a18_20261009/`.
