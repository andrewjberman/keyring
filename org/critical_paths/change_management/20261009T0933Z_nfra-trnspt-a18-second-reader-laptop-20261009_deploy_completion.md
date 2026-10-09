# Deploy Completion Record
**Date opened:** 2026-10-09T09:33:18.594111+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / Opal_Terminal real GetObject ADMITTED plus dell2 irpt-ycharts-runner-role real GetObject REFUSED, status-only (held since 2026-10-09T10:02:46.804410+00:00)
**Deploy:** NFRA_TRNSPT a18 second named reader apply from integrated pin f7a4fb5d04efb908b96ab3b8d86277c9b9f982ad carrying f8c4859407, 04313a7e39, dc5032abde
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| APPLY | activation | Terraform targets aws_iam_role.second_reader, aws_iam_policy.second_reader, aws_iam_role_policy_attachment.second_reader, aws_kms_key.transcripts | safe-apply receipt and exact 3 create plus 1 update result | safe-apply SUCCESS 2026-10-09T09:55Z: 3 added, 1 changed, 0 destroyed; pin f7a4fb5d04; plan gate commit 5d27fc36a7; tag override audit id 20261009T095303Z-3890779 after direct comp-tagauthz rc=0 and tombstone rc=0 | CLOSED 20261009T100241Z |
| VERIFY | verify | Named reader role, key-policy one-principal delta, admitted/refused S3 proof | role readback, full key-policy diff, ADMITTED and REFUSED statuses only |  | OPEN |

## Log

- 20261009T093318Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20261009T100241Z LEG APPLY closed: safe-apply SUCCESS 2026-10-09T09:55Z: 3 added, 1 changed, 0 destroyed; pin f7a4fb5d04; plan gate commit 5d27fc36a7; tag 
- 20261009T100246Z HELD-SOVEREIGN-GATED gate=external/Opal_Terminal real GetObject ADMITTED plus dell2 irpt-ycharts-runner-role real G
