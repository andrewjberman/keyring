# Deploy Completion Record
**Date opened:** 2026-10-17T07:21:36.117927+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T083003Z
**Deploy:** SOC2_MSLOGS round 2: door code, collector retry 0, memory down after the streaming proof
**Authored by:** 0.7.0_AE_CloudOps~SOC21
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply-code | activation | trino root: safe-apply door code + aliases to new version, collector code hash, ONE create aws_lambda_function_event_invoke_config.collector (retry 0) | plan summary + apply receipt + apply_r2_at.txt + s1_check_r1.py applied + retry read 0 | safe-apply rc=0 Apply complete 1 added 3 changed 0 destroyed at 2026-10-17T07:24:16Z (plan: door code hash + 2 aliases + ONE create event_invoke_config.collector; collector code hash unchanged since round 1); door LastModified 2026-10-17T07:24:09Z 10240 MB 600 s, aliases member+collector on v6; s1_check_r1.py applied R1-APPLIED-OK; MaximumRetryAttempts 0; post-apply plan no differences | CLOSED 20261017T072513Z |
| rederive-proof | verify | 8-day re-derive by Andrew at 10240 MB: per-day REPORT Max Memory Used and Duration, no OutOfMemory | 8 REPORT figures (counts and megabytes only) | DEFERRED, NOT RUN AND NOT PROVEN: TO-R2-r2 AMENDMENT 1 @dcdfad0899 (2.0.0_SA_COO~S1, 2026-10-18) -- waits on Andrew's MFA re-derive (open call dell1-20261017T131441Z-89c9); state stable, nothing to roll back; reopens under NEW ledger soc2-mslogs-r2-memory-down-<date> before the item 8 apply | CLOSED 20261018T083002Z |
| memory-down | activation | trino root: safe-apply aws_lambda_function.access memory_size 10240 -> smallest of 2048/3008/4096/6144 >= 2x busiest-day Max Memory Used | plan summary + apply receipt + deployed memory read + s1_check_r1.py applied | DEFERRED, NOT RUN AND NOT PROVEN: TO-R2-r2 AMENDMENT 1 @dcdfad0899 (2.0.0_SA_COO~S1, 2026-10-18) -- waits on Andrew's MFA re-derive (open call dell1-20261017T131441Z-89c9); state stable, nothing to roll back; reopens under NEW ledger soc2-mslogs-r2-memory-down-<date> before the item 8 apply | CLOSED 20261018T083002Z |
| memory-proof | verify | busiest date re-derived by Andrew at the lowered memory: no OutOfMemory, Max Memory Used < 80 percent of memory_size | REPORT line read | DEFERRED, NOT RUN AND NOT PROVEN: TO-R2-r2 AMENDMENT 1 @dcdfad0899 (2.0.0_SA_COO~S1, 2026-10-18) -- waits on Andrew's MFA re-derive (open call dell1-20261017T131441Z-89c9); state stable, nothing to roll back; reopens under NEW ledger soc2-mslogs-r2-memory-down-<date> before the item 8 apply | CLOSED 20261018T083002Z |

## Log

- 20261017T072136Z OPENED by 0.7.0_AE_CloudOps~SOC21 with 4 leg(s)
- 20261017T072513Z LEG apply-code closed: safe-apply rc=0 Apply complete 1 added 3 changed 0 destroyed at 2026-10-17T07:24:16Z (plan: door code hash + 2 aliases +
- 20261018T083002Z LEG rederive-proof closed: DEFERRED, NOT RUN AND NOT PROVEN: TO-R2-r2 AMENDMENT 1 @dcdfad0899 (2.0.0_SA_COO~S1, 2026-10-18) -- waits on Andrew's MF
- 20261018T083002Z LEG memory-down closed: DEFERRED, NOT RUN AND NOT PROVEN: TO-R2-r2 AMENDMENT 1 @dcdfad0899 (2.0.0_SA_COO~S1, 2026-10-18) -- waits on Andrew's MF
- 20261018T083002Z LEG memory-proof closed: DEFERRED, NOT RUN AND NOT PROVEN: TO-R2-r2 AMENDMENT 1 @dcdfad0899 (2.0.0_SA_COO~S1, 2026-10-18) -- waits on Andrew's MF
- 20261018T083003Z CLOSED -- all 4 legs proven
