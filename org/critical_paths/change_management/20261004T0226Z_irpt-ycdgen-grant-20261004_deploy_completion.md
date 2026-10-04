# Deploy Completion Record
**Date opened:** 2026-10-04T02:26:48.309239+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN close: the runner role keeps research answers and run records in opal-data-cottonwood (two tables, Put/Get)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | ONE targeted safe-apply of aws_iam_role_policy.runner_resident (+ statement KeepYChartsResearchAnswersAndRunRecords) | the policy read back; simulate: allowed on the two research prefixes, implicitDeny on a sibling table and on another firm |  | OPEN |
| V1 | verify | the IRPT_YCDGEN close run writes its kept answers and run.json from the host | the run record and kept objects read back from the store |  | OPEN |

## Log

- 20261004T022648Z OPENED by 2.0.0_SA_COO~Y with 2 leg(s)
