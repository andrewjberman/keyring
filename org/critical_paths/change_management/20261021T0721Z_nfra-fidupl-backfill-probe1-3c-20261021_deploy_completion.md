# Deploy Completion Record
**Date opened:** 2026-10-21T07:21:49.682912+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T073409Z
**Deploy:** NFRA_FIDUPL FT-s-11 step 3C: ONE bounded run of backfill_main.py (python -u, --max-seconds 480, --max-sessions 4, SSM executionTimeout 660), one sign-in, add-only landing under fidelity/alongside/bronze/
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE run via SSM of backfill_main.py with --max-seconds 480 --max-sessions 4 (no retry) | stdout and stderr verbatim; ft11r; days list and stop | PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM 1441ca48-d06c-42c6-9750-90239de00c39 (07:22:16Z to 07:31:29Z, --max-seconds 480 --max-sessions 4, executionTimeout 660), one sign-in, clean CLOSE (logout), exit=1, no retry. Days: 2026-10-21 empty; 2026-10-20 completed; 2026-10-19 budget (one downloadExport.do ran 452 s, WallBudget). Record backfill-20261021T072217Z.json: run_error TargetClosedError, stop none, per-file-type all zero; 0 data keys landed. ft11r: R1-FT11R-FAIL run_error=TargetClosedError (FT-s-11-AC1 stays FAIL; surprise row NFRA_FIDUPL-D1-S16). The run used the 170a9c69ce8 file; msg 9026 (head 3d8b85fd61d) was sent after the run began and was delivered afterwards. Nothing half-landed. | CLOSED 20261021T073409Z |

## Log

- 20261021T072149Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261021T073409Z LEG L1 closed: PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM 1441ca48-d06c-42c6-9750-90239de00c39 (07:22:16
- 20261021T073409Z CLOSED -- all 1 legs proven
