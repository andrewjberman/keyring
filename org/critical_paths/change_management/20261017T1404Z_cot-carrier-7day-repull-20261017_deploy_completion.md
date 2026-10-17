# Deploy Completion Record
**Date opened:** 2026-10-17T14:04:40.209994+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T141847Z
**Deploy:** Cottonwood 7-day carrier re-pull for dell2 (07-22,07-27,07-29,08-03,08-19,09-24,09-25); holdings via guard, allocations on count; CTO half @8c36f9f375
**Authored by:** 4.0.0_SA_CRO~DDD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V0 | verify | prior VersionIds recorded | vers7.json committed | prior VersionIds of 10 keys x 7 days recorded before any write: org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/COT_CARRIER_7DAY_PRIOR_VERSIONS_20261017.json (0 absent); landed holdings nzf 0.636/0.651/0.6522/0.6506/0.6368/0.6571/0.6589 | CLOSED 20261017T140531Z |
| B1 | verify | holdings per day via guard | per-day LANDED/REJECT with nzf | holdings x7 via guard 14:05-14:10Z: ALL 7 REJECTED (BD historical pulls less valued than landed): 07-22 51.3<63.6, 07-27 51.3<65.1, 07-29 51.5<65.2, 08-03 51.5<65.1, 08-19 55.3<63.7, 09-24 60.2<65.7, 09-25 60.2<65.9 (nzf %); nothing landed | CLOSED 20261017T141846Z |
| B2 | verify | allocations per day on printed count | per-day new vs landed counts | allocations: no-write local fetch (cot_bronze_ingest template/query/download, no land) printed new vs landed accounts: 07-22 894>878 LAND, 07-27 897=897 REFUSE, 07-29 896=896 REFUSE, 08-03 901>888 LAND, 08-19 921>814 LAND, 09-24 949>941 LAND, 09-25 948>940 LAND; SSM land 14:12-14:14Z; landed_now equals dry on all 5 | CLOSED 20261017T141847Z |
| S1 | activation | scoped silver + mirror/convert per landed day | totals read back | scoped silver allocations x5 (60d48b04, 14:15Z; no holdings, no account_attributes, no finalize): 894/901/921/949/948 rows; mirror {firm:cot} written 51 failed 0; converter force run 20261017T141638Z-96f88542 converted 5; MDPF fact_allocations accounts 894/901/921/949/948 | CLOSED 20261017T141847Z |
| P1 | verify | no-write after-print before next fire | Global + cot model_aua equal | no-write build_composed after-print (before the next fire): Cottonwood partner_custody_total, model_aua, non_model_aua EQUAL to before on all 7 dates (0 fields moved); Global unchanged by rule (takes cot model/SMA legs only; both equal) | CLOSED 20261017T141847Z |

## Log

- 20261017T140440Z OPENED by 4.0.0_SA_CRO~DDD with 5 leg(s)
- 20261017T140531Z LEG V0 closed: prior VersionIds of 10 keys x 7 days recorded before any write: org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/COT_CARRIER
- 20261017T141846Z LEG B1 closed: holdings x7 via guard 14:05-14:10Z: ALL 7 REJECTED (BD historical pulls less valued than landed): 07-22 51.3<63.6, 07-27
- 20261017T141847Z LEG B2 closed: allocations: no-write local fetch (cot_bronze_ingest template/query/download, no land) printed new vs landed accounts: 0
- 20261017T141847Z LEG S1 closed: scoped silver allocations x5 (60d48b04, 14:15Z; no holdings, no account_attributes, no finalize): 894/901/921/949/948 ro
- 20261017T141847Z LEG P1 closed: no-write build_composed after-print (before the next fire): Cottonwood partner_custody_total, model_aua, non_model_aua E
- 20261017T141847Z CLOSED -- all 5 legs proven
