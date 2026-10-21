# Deploy Completion Record
**Date opened:** 2026-10-21T11:15:03.311625+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T112444Z
**Deploy:** NFRA_FIDUPL FT-s-11 step 3F: ONE bounded run of backfill_main.py (python -u, --skip-files transact.txt, --max-seconds 480, --max-sessions 12, SSM executionTimeout 660), one sign-in, 11:20Z or later; add-only landing under fidelity/alongside/bronze/
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE run via SSM of backfill_main.py with --skip-files transact.txt --max-seconds 480 --max-sessions 12 (no retry) | stdout and stderr verbatim; ft11r; days list, earliest_served, days landed and bytes, stop | backfill_main.py ran ONCE through SSM 5ad1ff0a-efad-406f-9697-173a387b91c4 (11:20:39Z to 11:22:36Z, --skip-files transact.txt --max-seconds 480 --max-sessions 12, executionTimeout 660) on the thirtieth-delivery code, one sign-in, clean CLOSE (logout), exit=0, no retry, no cookie or profile touched. Days: 2026-10-21, 2026-10-20, 2026-10-19 completed (five files each served, transact skipped by option); 2026-10-16 and 2026-10-15 empty; 2026-10-14 retention. stop retention, evidence empty listing x3. ft11r: R1-FT11R-OK backfill record: sign_ins=1 stop=retention earliest account:20261019,balance:None,position:None,prices:None,security:None,transact:None. fu10m: R1-FU10M-OK all 23 shipped files match the repo on the box. Landed this run: one data key, account/20261016/account.txt (3794179 bytes); the other served files read skipped_existing. Add-only; nothing half-landed. | CLOSED 20261021T112444Z |

## Log

- 20261021T111503Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261021T112444Z LEG L1 closed: backfill_main.py ran ONCE through SSM 5ad1ff0a-efad-406f-9697-173a387b91c4 (11:20:39Z to 11:22:36Z, --skip-files transac
- 20261021T112444Z CLOSED -- all 1 legs proven
