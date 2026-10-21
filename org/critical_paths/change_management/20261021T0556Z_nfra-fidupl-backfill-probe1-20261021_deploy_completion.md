# Deploy Completion Record
**Date opened:** 2026-10-21T05:56:06.364210+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FT-s-11: backfill probe 1 live -- ONE run of backfill_main.py (one sign-in) walking the export calendar back, add-only landing under fidelity/alongside/bronze/
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ONE run of /opt/fidelity-uploader/backfill_main.py --config /opt/fidelity-uploader/config.json via SSM (one sign-in, no retry) | stdout lines verbatim; ft11r R1-FT11R-OK backfill record; fu10m R1-FU10M-OK all |  | OPEN |

## Log

- 20261021T055606Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
