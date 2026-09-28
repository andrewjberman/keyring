# Deploy Completion Record
**Date opened:** 2026-09-28T21:17:45.105450+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter F0bYtOfB -> IB-pr-191: a linked engine day with r_net <= -1 refuses EngineReturnImplausible (DEPENDENCY_UNAVAILABLE), never serves -100% (NEW-01, rows S176/S177); code only; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live F0bYtOfB: ONLY entry.py + f49_engine.py differ; flat_zip_module_census + ~Y zip_module_census + built-zip cold-start smoke PASS |  | OPEN |
| D1 | activation | performance root safe-apply | both halves at HEAD naming the packet blob; LIVE before-read of the NEW-01 account YTD; plan 0/1/0 code only; readback CodeSha; cold start; the same read after; replan 0 |  | OPEN |
| A1 | verify | the Performance page | the NEW-01 account no longer shows -100% on the signed-in page (the next walk window) |  | OPEN |

## Log

- 20260928T211745Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
