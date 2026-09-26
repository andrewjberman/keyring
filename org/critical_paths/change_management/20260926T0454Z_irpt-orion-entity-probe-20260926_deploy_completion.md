# Deploy Completion Record
**Date opened:** 2026-09-26T04:54:25.104019+00:00
**Status:** OPEN
**Deploy:** Row S143: bounded Orion Reporting/Scope probes (control entity 5 household 381, then Account candidates with id 1098) -- the adapter's own body, entity swapped; egress CTO 101098
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | Orion /api/v1/Reporting/Scope | control first (stop on its 404); each status + Orion error or response shape recorded in ORION_ENTITY_PROBE_20260926.json; no credential |  | OPEN |

## Log

- 20260926T045425Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
