# Deploy Completion Record
**Date opened:** 2026-10-05T03:25:15.842184+00:00
**Status:** OPEN
**Deploy:** W100-S2: withdraw the 49F perfrp account leaf from opal-data-portal-v2 (Andrew card 1 @c9c8e0c191; CTO half @4a63c9b600; COO half @48fa2860ab)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | delete-object platinum/advi/49financial/perfrp_performance_account.json under ETag stop 9873b72ef5da73fc0399d2905d4f7821 | delete marker VersionId | pre-head ETag 9873b72ef5da73fc0399d2905d4f7821 + version E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim matched; delete-object -> DeleteMarker True, marker VersionId vQdm_KxXCknlz3LooZIS.ViTHQiTiZVn (2026-10-05 ~03:2xZ) | CLOSED 20261005T032932Z |
| V1 | verify | head-object 404 with the delete marker current | list-object-versions IsLatest marker | head-object 404; list-object-versions: marker vQdm_KxXCknlz3LooZIS.ViTHQiTiZVn IsLatest True, version E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim IsLatest False (rollback intact) | CLOSED 20261005T032932Z |
| V2 | verify | one 49F PROD login on /advisor-intelligence shows the designed shell | walker screenshot path |  | OPEN |

## Log

- 20261005T032515Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20261005T032932Z LEG D1 closed: pre-head ETag 9873b72ef5da73fc0399d2905d4f7821 + version E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim matched; delete-object -> Dele
- 20261005T032932Z LEG V1 closed: head-object 404; list-object-versions: marker vQdm_KxXCknlz3LooZIS.ViTHQiTiZVn IsLatest True, version E78kI4KB4KsZhdwsAF
