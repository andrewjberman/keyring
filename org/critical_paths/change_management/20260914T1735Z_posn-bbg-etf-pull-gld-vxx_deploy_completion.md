# Deploy Completion Record
**Date opened:** 2026-09-14T17:35:10.588395+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX card 4: Bloomberg ETF daily pull captures GLD and VXX (EXTRA_SECURITIES, not FUNDS). Working-tree deploy on site Z: integrations/bloomberg/pipeline/etf_daily_pull.py. Andrew-direct 2026-09-14 ~17:2xZ Call 4 Yes. Rollback: revert the commit (the scheduled task runs the working tree).
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of integrations/bloomberg/pipeline/etf_daily_pull.py (py_compile + commit-gate) | commit hash + push state from ls-remote | commit ac3e03a317 on SITEZ by 1.0.0_SA_CTO~Z: integrations/bloomberg/pipeline/etf_daily_pull.py +10 lines (EXTRA_SECURITIES GLD VXX into qmap only; log line; manifest extra_securities), py_compile OK, LF preserved. Working tree == committed bytes on this device (the scheduled task runs the working tree). Push state: LOCAL, origin/SITEZ 6f09a06dc919bf21ef96b52aff5cd7e9608ccf85 by ls-remote; site-Z pushes held by 0.0.0_AB_MSTR~Z on Andrew's word. | CLOSED 20260914T173953Z |
| L2 | verify | first scheduled fire OPAL_BBGTML_daily_pull 2026-09-15 07:00 ET: bbg/2026-09-14/run_manifest.json run_class=scheduled, extra_securities [GLD, VXX], vendor_observations GLD and VXX present, funds unchanged, objects_failed empty | manifest read with a DIVZ positive control |  | OPEN |

## Log

- 20260914T173510Z OPENED by 1.0.0_SA_CTO~Z with 2 leg(s)
- 20260914T173953Z LEG L1 closed: commit ac3e03a317 on SITEZ by 1.0.0_SA_CTO~Z: integrations/bloomberg/pipeline/etf_daily_pull.py +10 lines (EXTRA_SECURIT
