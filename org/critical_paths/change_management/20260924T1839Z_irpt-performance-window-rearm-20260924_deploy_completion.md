# Deploy Completion Record
**Date opened:** 2026-09-24T18:39:51.481279+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter: series-window fix dd1811bbaa + ONE re-armed one-use COT plan (Andrew f0bd1c267e)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | artifact build: bd_selected.py row re-pinned to dd1811bbaa, one member differs | census vs deployed 07lSH03z: 61 of 61 names equal, exactly bd_selected.py differs |  | OPEN |
| A1 | activation | module.irpt_performance_adapter + env plan | safe-apply of the saved plan; readback CodeSha256 = built sha; IRPT_PERF_VENDOR_EGRESS_AUTHORIZED = new plan sha |  | OPEN |
| V1 | verify | performance root re-plan | terraform plan -detailed-exitcode rc=0 with the var-file; State Active, LastUpdateStatus Successful |  | OPEN |
| R1 | git | deploy recorder | record-terraform-deploy commit |  | OPEN |
| S1 | verify | served journey | Andrew's signed-in request on acc_d486fc94..: PERFORMANCE_ACCEPTED row + a READY report, or the use's named refusal read from the log |  | OPEN |

## Log

- 20260924T183951Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
