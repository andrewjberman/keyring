# Deploy Completion Record
**Date opened:** 2026-09-16T19:06:40.804730+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-c-2: controlled replay D_r=2026-09-15, one event per master through opal-assets-silver-schwab (4 objects: 2 run manifests + 2 markers)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | 08242234 event replay: schwab/08242234/meta/conversions/{run_id}.json + meta/complete/date=2026-09-15.json | keys + VersionIds, 0 silver VersionId changes |  | OPEN |
| R2 | verify | 08335338 event replay: schwab/08335338/meta/conversions/{run_id}.json + meta/complete/date=2026-09-15.json | keys + VersionIds, 0 silver VersionId changes |  | OPEN |
| R3 | verify | replay-caused advi-49f-gold-dispatch outcomes (G-B conditions 2,5,7) | branch per dispatch, chain log key, date=D before/after VersionIds |  | OPEN |

## Log

- 20260916T190640Z OPENED by 0.9.0_WK_NFRA_OPLGTW~4 with 3 leg(s)
