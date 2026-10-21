# Deploy Completion Record
**Date opened:** 2026-10-21T07:54:34.848052+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T083331Z
**Deploy:** NFRA_FIDUPL FT-s-11 step 3D: ONE bounded run of backfill_main.py (python -u, --max-seconds 480, --max-sessions 6, SSM executionTimeout 660), one sign-in, at 08:22Z or later; add-only landing under fidelity/alongside/bronze/
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE run via SSM of backfill_main.py with --max-seconds 480 --max-sessions 6 (no retry) | stdout and stderr verbatim; ft11r; days list, earliest_served, stop | PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM 52b0a403-ade6-4b44-b3c6-77bc8e87c4d9 (08:22:16Z to 08:31:29Z, --max-seconds 480 --max-sessions 6, executionTimeout 660), one sign-in, clean CLOSE (logout), exit=1, no retry, no cookie or profile touched. Days: 2026-10-21 empty; 2026-10-20 completed (six files ok); 2026-10-19 budget (five of six files served, the sixth never returned). Record backfill-20261021T082217Z.json: run_error TargetClosedError, stop none, earliest_served 20261020 and served_days 1 for all six file types, landed days 0 bytes 0; 0 data keys landed. ft11r: R1-FT11R-FAIL run_error=TargetClosedError (FT-s-11-AC1 stays FAIL; surprise row NFRA_FIDUPL-D1-S17). Nothing half-landed: no data was written. | CLOSED 20261021T083331Z |

## Log

- 20261021T075434Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261021T083331Z LEG L1 closed: PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM 52b0a403-ade6-4b44-b3c6-77bc8e87c4d9 (08:22:16
- 20261021T083331Z CLOSED -- all 1 legs proven
