# Deploy Completion Record
**Date opened:** 2026-09-29T14:08:18.655394+00:00
**Status:** OPEN
**Deploy:** S205: the scheduled 49F holdings producer (irpt-holdings-performance-lambda a1ZUOSw5, holdings_performance.py @23004aaf98, pre-v0.20) redeployed at the v0.21 producer (363dc1fda4) with the schedule input naming source schwab_08335338; date=2026-09-28 re-emitted through the Lambda; gate for the 49F r3 re-switch
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live: ONLY holdings_performance.py + sources.json differ; the BUILT handler dry-run for 2026-09-28 (the schedule's payload + source): 0 OK rows at abs(r) >= 1 | Source map: holdings_performance.py + sources.json re-pinned 23004aaf98 -> 363dc1fda4 (sha256 6f786496 / 34178bc5; the v0.20 f302ab14cd, v0.21 bf1683f172 and COT e79dd684bf producer). build-and-upload rc 0; S3 investor-reporting/irpt-holdings-performance-lambda.zip VersionId ifXqxmjU0kbueSnAiI54fYQu_Hj8oHaK (14:10:09Z) sha gLRGHIyi; census vs live a1ZUOSw5 14 -> 14, ONLY holdings_performance.py + sources.json differ. BUILT handler, extracted zip only on sys.path: resolves 2026-09-28; the schedule payload + source schwab_08335338 dry_run -> rc 0, rows 7548 census OK 6654 / NO-PRIOR-HOLDINGS 885 / NON-POSITIVE-BASE 6 / ALL-HOLDINGS-EXCLUDED 3; compute_day on the built bytes: 0 OK rows at abs(r) >= 1 (live gold today: 14), max OK r +0.0374; the 14 S205 accounts read 0.00% (cash). CONTROL: the schedule's current source-less payload is REFUSED by the new producer (3 declared sources), so the schedule input must carry the source (schedule.tf edit). | CLOSED 20260929T141223Z |
| P1 | verify | fresh plan | holdings-performance root: Lambda code + the schedule input (source) only | Plan 14:2xZ, main tree, terraform v1.14.5 (PATH; the root's locals need && short-circuit -- .tools/terraform.exe v1.9.8 errors at locals.tf:37 on the declaration's string keys), init -reconfigure (local metadata only): 0/2/0 -- aws_scheduler_schedule.irpt_holdings_performance target.input + source = schwab_08335338; module.irpt_holdings_performance.aws_lambda_function.this s3_object_version UoJZFUus -> ifXqxmjU, source_code_hash a1ZUOSw5 -> gLRGHIyi. No IAM change: the role's read grants derive from declared sources carrying , which at HEAD is still schwab_08335338 alone. | CLOSED 20260929T141802Z |
| D1 | activation | apply + re-emit | halves at HEAD; S3 latest == built at apply; safe-apply; readback; ONE invoke with the schedule's exact payload (target day 2026-09-28, upload): rc 0; re-read date=2026-09-28: 0 OK rows at abs(r) >= 1, the 14 S205 accounts ordinary; re-plan 0 |  | OPEN |

## Log

- 20260929T140818Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260929T141223Z LEG U1 closed: Source map: holdings_performance.py + sources.json re-pinned 23004aaf98 -> 363dc1fda4 (sha256 6f786496 / 34178bc5; the v
- 20260929T141802Z LEG P1 closed: Plan 14:2xZ, main tree, terraform v1.14.5 (PATH; the root's locals need && short-circuit -- .tools/terraform.exe v1.9.8 
