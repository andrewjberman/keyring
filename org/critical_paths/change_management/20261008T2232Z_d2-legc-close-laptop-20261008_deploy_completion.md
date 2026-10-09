# Deploy Completion Record
**Date opened:** 2026-10-08T22:32:43.081637+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T064817Z
**Deploy:** TO18 legC close dell2 F1 shell window X1 reached22:27Z
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | aws_iam_policy.dell2_ssm | Plain no-var plan exact0/1/0 and safeapply closes window | SUPERSEDED by TO-APPLY-26 commit 8d42d8967a; current TO26 proof VALID; original closure 55112a7de6; fresh 20261009T0647Z IAM measurement confirms AWS-RunShellScript and resident host allowed. | CLOSED 20261009T064817Z |
| V1 | verify | dell2 AWS-RunShellScript F1 | explicitDeny DenyShellDocuments live; defaultreplan0; deadline retired onclose | SUPERSEDED by TO-APPLY-26 standing shell posture at 8d42d8967a; fresh d2-live-iam-measurement.json: ShellScript allowed, resident host allowed, PowerShell explicitDeny; no SSM command sent. | CLOSED 20261009T064817Z |

## Log

- 20261008T223243Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20261009T064817Z LEG C1 closed: SUPERSEDED by TO-APPLY-26 commit 8d42d8967a; current TO26 proof VALID; original closure 55112a7de6; fresh 20261009T0647Z
- 20261009T064817Z LEG V1 closed: SUPERSEDED by TO-APPLY-26 standing shell posture at 8d42d8967a; fresh d2-live-iam-measurement.json: ShellScript allowed,
- 20261009T064817Z CLOSED -- all 2 legs proven
