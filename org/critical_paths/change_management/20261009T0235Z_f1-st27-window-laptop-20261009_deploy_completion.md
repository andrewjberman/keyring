# Deploy Completion Record
**Date opened:** 2026-10-09T02:35:55.284714+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T035614Z
**Deploy:** TO25 F1 st27 window; open B2 now; close C2 at V1 or 2026-10-09T06:00Z without waiting; no SSM command
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B2 | activation | dell2_ssm window open | Targeted exact0/1/0; shell+F1 allowed; otherhost explicitDeny; noSSMcommand | Opened2026-10-09T02:37:46Z v6;targetedexact0/1/0;shellallowed,F1allowed,otherhostexplicitDeny;openreplan0;noSSMcommand | CLOSED 20261009T023837Z |
| C2 | activation | dell2_ssm window closed at V1 or06Z | Plain exact0/1/0; DenyShellDocuments explicitDeny; untargeted replan0; scratch deleted | SUPERSEDED by TO-APPLY-26 standing-access apply at 2026-10-09T03:52:21.7867819Z; live v7 equals repository policy; untargeted default replan0; noSSMcommand; scratch deleted 2026-10-09T03:56:47.7005727Z | CLOSED 20261009T035614Z |

## Log

- 20261009T023555Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20261009T023837Z LEG B2 closed: Opened2026-10-09T02:37:46Z v6;targetedexact0/1/0;shellallowed,F1allowed,otherhostexplicitDeny;openreplan0;noSSMcommand
- 20261009T035614Z LEG C2 closed: SUPERSEDED by TO-APPLY-26 standing-access apply at 2026-10-09T03:52:21.7867819Z; live v7 equals repository policy; untar
- 20261009T035614Z CLOSED -- all 2 legs proven
- 20261009T035647Z POST-CLOSE CLEANUP: retained TO25 Terraform scratch deleted; 718876487 bytes removed; path absent after.
