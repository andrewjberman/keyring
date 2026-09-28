# Deploy Completion Record
**Date opened:** 2026-09-28T21:20:40.055664+00:00
**Status:** OPEN
**Deploy:** Holdings firm principals: s3:GetObjectVersion on the READS statements (CTO 635481d716, COO 410f52bdde)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply 3 aws_iam_role_policy.irpt_holdings | Apply complete 0 added 3 changed 0 destroyed |  | OPEN |
| V1 | verify | get-role-policy x3 | each READ statement's Action carries s3:GetObject and s3:GetObjectVersion, resources unchanged; re-plan No changes |  | OPEN |

## Log

- 20260928T212040Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 2 leg(s)
