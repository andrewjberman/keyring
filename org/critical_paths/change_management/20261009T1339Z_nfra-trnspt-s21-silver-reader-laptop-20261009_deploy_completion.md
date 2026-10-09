# Deploy Completion Record
**Date opened:** 2026-10-09T13:39:30.656245+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT s21 silver-only reader apply at pin 32d09cc6ad06beb379ddd344f0f551dcced8077b carrying 365a08577e and dc5032abde (amendment 124e65440e)
**Authored by:** 0.7.0_AE_CloudOps~TRL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| APPLY | activation | Terraform targets aws_iam_role.silver_reader, aws_iam_policy.silver_reader, aws_iam_role_policy_attachment.silver_reader, aws_kms_key.transcripts | safe-apply receipt: exactly 3 creates + 1 in-place key-policy update whose ONLY difference is the added SilverReaderDecryptOnly statement; full key-policy diff printed in this entry; DellAgentUsersGenerateDataKey survives and nothing is removed |  | OPEN |
| AC1 | verify | teams-global-transcripts-silver-reader-role | aws iam get-role --role-name teams-global-transcripts-silver-reader-role --query Role.RoleName returns the role name |  | OPEN |
| PROOF | verify | three reads by the dell2 agent user assuming the silver reader role | statuses only: one Teams silver monday_meeting object 200; one Teams bronze object AccessDenied; one research_meeting silver object AccessDenied |  | OPEN |

## Log

- 20261009T133930Z OPENED by 0.7.0_AE_CloudOps~TRL with 3 leg(s)
