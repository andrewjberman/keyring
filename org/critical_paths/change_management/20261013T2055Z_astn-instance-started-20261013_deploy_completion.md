# Deploy Completion Record
**Date opened:** 2026-10-13T20:55:26.784598+00:00
**Status:** OPEN
**Deploy:** HVST-bz-8 residual: i-059405dfefcb4b44a started by the provider at 20:48:11Z, stop awaits Andrew's yes
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| STOP | activation | ONE aws ec2 stop-instances for i-059405dfefcb4b44a, only after the issuer's message states Andrew's relayed yes and names step 2 | describe-instances reads stopped |  | OPEN |
| VERIFY | verify | describe-instances State.Name stopped, polled up to 10 minutes | bz8_instance_stop.out |  | OPEN |

## Log

- 20261013T205526Z OPENED by 0.7.0_AE_CloudOps~HV1 with 2 leg(s)
