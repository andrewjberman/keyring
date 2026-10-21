# Deploy Completion Record
**Date opened:** 2026-10-21T10:27:10.429021+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T103013Z
**Deploy:** NFRA_FIDUPL FT-s-13 step 3B: ONE manual rule-shaped start of fidelity-alongside-uploader-document (InstanceId only), read to terminal; one sign-in; no second start
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE aws ssm start-automation-execution of the document with InstanceId=i-028e830f7226cc685, read get-automation-execution to terminal and the wrapper run record | execution id, terminal status, step names, FailureMessage if Failed, run record outcome and counts | ONE manual rule-shaped start (aws ssm start-automation-execution, document fidelity-alongside-uploader-document, parameter InstanceId only) at 10:27:27Z, execution bf5bc3dd-fce8-4fe4-a973-c20e0d57e331, terminal Success about 10:28:50Z, no FailureMessage; steps startInstance Success, waitForOnline Success, runWrapper Success. Wrapper run record _runs/20261020/run-20261021T102840Z.json: outcome ALL_LANDED, landed_count 6, failed_count 0, source automated, business_date_in_content 20261020; 6 data keys written 10:28Z. Instance left running; one sign-in; no second start. | CLOSED 20261021T103013Z |

## Log

- 20261021T102710Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261021T103013Z LEG L1 closed: ONE manual rule-shaped start (aws ssm start-automation-execution, document fidelity-alongside-uploader-document, paramet
- 20261021T103013Z CLOSED -- all 1 legs proven
