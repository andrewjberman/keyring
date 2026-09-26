# Deploy Completion Record
**Date opened:** 2026-09-26T04:54:25.104019+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T045911Z
**Deploy:** Row S143: bounded Orion Reporting/Scope probes (control entity 5 household 381, then Account candidates with id 1098) -- the adapter's own body, entity swapped; egress CTO 101098
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | Orion /api/v1/Reporting/Scope | control first (stop on its 404); each status + Orion error or response shape recorded in ORION_ENTITY_PROBE_20260926.json; no credential | 6 Scope calls (adapter body, entity swapped): 5/[381] control 200; 3/[1098] 501; 1/[1098] 501; 2/[1098] 404; 6/[1098] 200 but NOT the account (name check vs accounts_v2); 6/[1098] re-read once. Receipt ORION_ENTITY_PROBE_20260926.json; response bodies not kept; no credential printed | CLOSED 20260926T045911Z |

## Log

- 20260926T045425Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260926T045911Z LEG V1 closed: 6 Scope calls (adapter body, entity swapped): 5/[381] control 200; 3/[1098] 501; 1/[1098] 501; 2/[1098] 404; 6/[1098] 20
- 20260926T045911Z CLOSED -- all 1 legs proven
