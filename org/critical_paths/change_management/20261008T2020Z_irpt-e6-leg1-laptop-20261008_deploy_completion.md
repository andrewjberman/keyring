# Deploy Completion Record
**Date opened:** 2026-10-08T20:20:14.237135+00:00
**Status:** OPEN
**Deploy:** IRPT E6 leg 1: add only ReadPartnerProfileRowForOnBehalfAdvisor GetItem on opal-partner-49financial/cottonwood/inflection to irpt-ycharts-generate-role. CTO half 10dae3bf03; COO TO and GO 107162/107212; leg0 passed. Rollback: remove this statement and targeted safe-apply pre-grant policy saved in deliverables/irpt_e6_20261008/leg1-policy-before.json. No code deploy or other policy change.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_iam_role_policy.generate | exact 0/1/0 saved plan applied; timestamp |  | OPEN |
| V1 | verify | irpt-ycharts-generate-role | live policy exact delta and targeted no-change replan |  | OPEN |

## Log

- 20261008T202014Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
