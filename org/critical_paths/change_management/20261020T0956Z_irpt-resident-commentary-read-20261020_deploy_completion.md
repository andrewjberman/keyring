# Deploy Completion Record
**Date opened:** 2026-10-20T09:56:59.331046+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-IAMGRANT: resident role irpt-ycharts-runner-role gains read (GetObject, GetObjectVersion) of the ANALYSIS_COMMENTARY draft prefixes; one statement on aws_iam_role_policy.runner_resident, pin 430cd08b2a
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: policy Sid list and canonical sha256, simulation get and put implicitDeny | R0 baseline printed |  | OPEN |
| C | verify | scoped plan at the pin: 0 to add 1 to change 0 to destroy, one statement added | plan lines printed |  | OPEN |
| A | activation | safe-apply of the saved plan on aws_iam_role_policy.runner_resident | apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 G2 G3 | G1 G2 G3 printed |  | OPEN |

## Log

- 20261020T095659Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
