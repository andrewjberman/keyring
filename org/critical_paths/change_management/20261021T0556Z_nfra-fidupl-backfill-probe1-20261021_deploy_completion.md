# Deploy Completion Record
**Date opened:** 2026-10-21T05:56:06.364210+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T060514Z
**Deploy:** NFRA_FIDUPL FT-s-11: backfill probe 1 live -- ONE run of backfill_main.py (one sign-in) walking the export calendar back, add-only landing under fidelity/alongside/bronze/
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE run of /opt/fidelity-uploader/backfill_main.py --config /opt/fidelity-uploader/config.json via SSM (one sign-in, no retry) | stdout lines verbatim; ft11r R1-FT11R-OK backfill record; fu10m R1-FU10M-OK all | PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM fa3700a4-30fe-414f-a377-f41a083b7663 (06:01:20Z to 06:03:46Z), one sign-in, exit=1, no retry. Result: run_error TimeoutError, walk null, stop none, all six file types days=0 bytes=0 earliest=none; zero data keys landed under fidelity/alongside/bronze/ (non-_runs); completion record _runs/20261021/backfill-20261021T060121Z.json. ft11r: R1-FT11R-FAIL run_error=TimeoutError (FT-s-11-AC1 stays FAIL; surprise row NFRA_FIDUPL-D1-S14). Nothing half-landed: no data was written, no profile or config touched. | CLOSED 20261021T060514Z |

## Log

- 20261021T055606Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261021T060514Z LEG L1 closed: PARTIAL AS WRITTEN, stated plainly: backfill_main.py ran ONCE through SSM fa3700a4-30fe-414f-a377-f41a083b7663 (06:01:20
- 20261021T060514Z CLOSED -- all 1 legs proven
