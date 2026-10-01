# Deploy Completion Record
**Date opened:** 2026-10-01T15:04:20.836733+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD round 1 DB-b-3: write the tie-out proposal into dim_return_method/method_version=1 -- flow_convention STAYS END, tieout_tolerance_proposed 0.037
**Authored by:** 0.4.0_DS_ClientPlatform~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M2 | activation | dim_return_method v1 flow_convention + tieout_tolerance_proposed | the two values read back from the LANDED parquet, plus the schema_hash the type change forces |  | OPEN |

## Log

- 20261001T150420Z OPENED by 0.4.0_DS_ClientPlatform~S with 1 leg(s)
