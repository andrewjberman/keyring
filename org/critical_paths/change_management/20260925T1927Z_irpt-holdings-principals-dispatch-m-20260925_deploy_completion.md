# Deploy Completion Record
**Date opened:** 2026-09-25T19:27:14.559322+00:00
**Status:** OPEN
**Deploy:** R4 rows 2+4b: apply the directory root -- 3 firm holdings principals, the dispatch function, the holdings slot retargeted (DISABLED); CTO half @6c5c27a666, COO half @885ae2f3d6
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | re-plan at apply time | Plan 11 add / 2 change / 0 destroy, same addresses, irpt_directory_refresh absent |  | OPEN |
| AP1 | activation | safe-apply of the saved plan | Apply complete: 11 added, 2 changed, 0 destroyed |  | OPEN |
| V1 | verify | read-back | schedule DISABLED with the new target; each inline policy == plan JSON; function CodeSha256 == artifact sha |  | OPEN |
| N1 | verify | negative arm exercised as the principals | COT principal GetObject on opal-data-bd refused AND 49F principal GetObject on opal-data-cot refused |  | OPEN |

## Log

- 20260925T192714Z OPENED by 2.0.0_SA_COO~M with 4 leg(s)
