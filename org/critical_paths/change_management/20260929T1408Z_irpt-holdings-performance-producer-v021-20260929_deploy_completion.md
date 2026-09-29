# Deploy Completion Record
**Date opened:** 2026-09-29T14:08:18.655394+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T144814Z
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
| D1 | activation | apply + re-emit | halves at HEAD; S3 latest == built at apply; safe-apply; readback; ONE invoke with the schedule's exact payload (target day 2026-09-28, upload): rc 0; re-read date=2026-09-28: 0 OK rows at abs(r) >= 1, the 14 S205 accounts ordinary; re-plan 0 | Halves at HEAD naming blob 35c58b3f43: CTO 102832 (@50b3681e4e; conditions: the r3 census re-runs on the rewritten 09-28 gold and the r3 packet cites it; the INF switch names a SCHEDULED INF producer -> TO-IB-er-501 issued @4461f4494c), CRO 102838 (@39ab6ba7d2; conditions: S3 latest + read-backs, E3-AC4 through 2026-09-28 PASS, Wednesday's 11:30Z fire read from its partition -- carried to the r3 ledger). S3 latest ifXqxmjU read 14:40Z. safe-apply 14:40:05Z (terraform v1.14.5 via SAFE_APPLY_TERRAFORM; halt gate 39 routine, 0 STOP; HALT_ACK=1): 0/2/0. Readback: CodeSha256 gLRGHIyi.. 14:42:51Z Successful; schedule irpt-holdings-performance-daily input carries source schwab_08335338, cron(30 7 ? * MON-FRI *) ENABLED. ONE invoke with the schedule's exact input at 14:44:50Z: 200, {date 2026-09-28, rc 0, ok true}; rows 7548 LANDED, census OK 6654 / NO-PRIOR-HOLDINGS 885 / NON-POSITIVE-BASE 6 / ALL-HOLDINGS-EXCLUDED 3; Duration 6.5 s, Init 2.9 s. AFTER: date=2026-09-28/data.parquet version q6nwcljY (14:45:04Z): 0 OK rows at abs(r) >= 1 (was 17 incl. the 14 S205 accounts), S205 accounts max abs(r) 0.0188, leveraged present. E3-AC4 through 2026-09-28: days 558, absent 0, OK rows abs(r)>=1 0, days without leveraged 0, manifests 558 of 558 -> PASS. Re-plan: No changes. | CLOSED 20260929T144814Z |

## Log

- 20260929T140818Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260929T141223Z LEG U1 closed: Source map: holdings_performance.py + sources.json re-pinned 23004aaf98 -> 363dc1fda4 (sha256 6f786496 / 34178bc5; the v
- 20260929T141802Z LEG P1 closed: Plan 14:2xZ, main tree, terraform v1.14.5 (PATH; the root's locals need && short-circuit -- .tools/terraform.exe v1.9.8 
- 20260929T144814Z LEG D1 closed: Halves at HEAD naming blob 35c58b3f43: CTO 102832 (@50b3681e4e; conditions: the r3 census re-runs on the rewritten 09-28
- 20260929T144814Z CLOSED -- all 3 legs proven
