# Deploy Completion Record
**Date opened:** 2026-09-22T21:26:40.911386+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260922T213122Z
**Deploy:** AMGT-rk-117 Lenovo dense daily PX_LAST bronze pull
**Authored by:** 0.9.0_WK_AMGT_RESAPP~117
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| w1 | s3-prefix | opal-data-harvest/bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/ | AC4 | AC4: added key bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/20260922T212739Z.json (total pre 1 post 2 added 1, for_992 pre 0 post 1, added_all_under_992 True); content verified: 2459 rows, dates 2016-01-04..2025-12-31, first PX_LAST=7.46 last PX_LAST=9.26; served freshness for 992 moved 20260922T201211Z -> 20260922T212739Z (forward only, MAX rule); 36 of 36 other security partitions byte-equal pre/post | CLOSED 20260922T213101Z |

## Log

- 20260922T212640Z OPENED by 0.9.0_WK_AMGT_RESAPP~117 with 1 leg(s)
- 20260922T213101Z LEG w1 closed: AC4: added key bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/20260922T212739Z.json (total pre 1 
- 20260922T213122Z CLOSED -- all 1 legs proven
