# Deploy Completion Record
**Date opened:** 2026-10-08T20:27:11.550817+00:00
**Status:** OPEN
**Deploy:** D2 leg A only: group SendCommand Allow on 19 exact ARNs plus result reads. Window CLOSED; no SSM command sent. Halves 298e731471/ac2c6e852d; merge 52ca9d65b1. Rollback detach and delete only cloudops-dell-agent-ssm-send-policy, or apply first parent of merge. Before group list deliverables/d2_legA_20261008/group-before.json. Other identity policies unchanged.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | dell_agent_ssm_send policy and attachment | exact 2/0/0 default plan and applied timestamp |  | OPEN |
| V1 | verify | both Dell users | all named live simulation arms and matched statements; group seven; no-change replan |  | OPEN |

## Log

- 20261008T202711Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
