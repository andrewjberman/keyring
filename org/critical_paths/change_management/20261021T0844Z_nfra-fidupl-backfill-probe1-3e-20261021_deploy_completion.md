# Deploy Completion Record
**Date opened:** 2026-10-21T08:44:27.066141+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T090703Z
**Deploy:** NFRA_FIDUPL FT-s-11 step 3E: ONE bounded run of backfill_main.py (python -u, --max-seconds 480, --max-sessions 8, SSM executionTimeout 660), one sign-in, 08:56Z or later and done before 09:30Z; add-only landing under fidelity/alongside/bronze/
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE run via SSM of backfill_main.py with --max-seconds 480 --max-sessions 8 (no retry) | stdout and stderr verbatim; ft11r; days list, earliest_served, days landed and bytes, stop | PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM f26b9129-0448-419c-8838-4515ce3da500 (08:56:14Z to 09:05:19Z, --max-seconds 480 --max-sessions 8, executionTimeout 660) on the 4d6a1aafeda code, one sign-in, clean CLOSE (logout), exit=1, no retry, no cookie or profile touched, done before 09:30Z. Days: 2026-10-21 empty; 2026-10-20 completed; 2026-10-19 budget (five of six files served, transact interrupted_WallBudget, landed_on_stop 4). LANDED: 4 data keys under fidelity/alongside/bronze/ (balance, position, prices, security, content date 20261016, 09:05:17Z), add-only. Record backfill-20261021T085615Z.json: run_error TargetClosedError, stop none. ft11r: R1-FT11R-FAIL run_error=TargetClosedError (FT-s-11-AC1 stays FAIL; surprise row NFRA_FIDUPL-D1-S18). Nothing half-landed: the four landed files are complete objects; no other key written. | CLOSED 20261021T090703Z |

## Log

- 20261021T084427Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261021T090703Z LEG L1 closed: PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM f26b9129-0448-419c-8838-4515ce3da500 (08:56:14
- 20261021T090703Z CLOSED -- all 1 legs proven
