# Deploy Completion Record
**Date opened:** 2026-09-24T20:25:29.521624+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T202830Z
**Deploy:** irpt-performance-adapter: 49F/INF refused by name (UNSUPPORTED_OPERATION) before any I/O (7f6b5589f6); armed COT plan 99052771 preserved
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_performance_adapter code only | census exactly entry.py+retained.py; plan 0/1/0 code only with the var-file; safe-apply; readback CodeSha + egress sha unchanged 99052771; replan 0; use row still absent; recorder | census vs deployed NuIaCuqn: 61/61, exactly entry.py + retained.py differ (7f6b5589f6); plan 0/1/0 source_code_hash + s3_object_version only, with the plan var-file (env unchanged); safe-apply 20:26:37Z; readback l3NswChjnfWeIG9wEh/zYsdWxiU9dotJAaxsGINm8HE= Active/Successful, IRPT_PERF_VENDOR_EGRESS_AUTHORIZED 99052771.. unchanged; replan rc=0; PERFORMANCE_USE#99052771 absent (unspent); recorder c9af24bdda | CLOSED 20260924T202830Z |

## Log

- 20260924T202529Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260924T202830Z LEG A1 closed: census vs deployed NuIaCuqn: 61/61, exactly entry.py + retained.py differ (7f6b5589f6); plan 0/1/0 source_code_hash + s3
- 20260924T202830Z CLOSED -- all 1 legs proven
