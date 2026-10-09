# Deploy Completion Record
**Date opened:** 2026-10-09T00:58:23.872644+00:00
**Status:** OPEN
**Deploy:** TO20 F1 st26 window; openB2 now; closeC2 atX1 or2026-10-09T06:00Z withoutwaiting; noSSMcommand
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B2 | activation | dell2_ssm windowopen | Exact0/1/0;F1shellallowed;otherhostexplicitDeny | Opened2026-10-09T01:00:23Z v4;exact0/1/0;singleARNshell/F1allowed,otherhostexplicitDeny;openreplan0;after.json | CLOSED 20261009T010155Z |
| C2 | activation | dell2_ssm windowclosed atX1 or06:00Z | Plain0/1/0;DenyShellDocuments;defaultreplan0 |  | OPEN |

## Log

- 20261009T005823Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20261009T010155Z LEG B2 closed: Opened2026-10-09T01:00:23Z v4;exact0/1/0;singleARNshell/F1allowed,otherhostexplicitDeny;openreplan0;after.json
