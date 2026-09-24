# Deploy Completion Record
**Date opened:** 2026-09-24T06:35:28.351345+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T064456Z
**Deploy:** irpt-performance-adapter rebuild: X10 ACTIVE registry row (M 7262571e4c) + hops 4b/3 (7a8d2a4ca3); CTO batch 27 item 2
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_performance_adapter.aws_lambda_function.this | safe-apply of saved plan 0/1/0, readback CodeSha256 07lSH03z | safe-apply (tools terraform 1.9.8, backend performance root) of the saved plan 0/1/0 (hash + version only): source_code_hash NFbaNR0r -> 07lSH03z, s3_object_version jfx18fFv -> xG9..VR5J; Apply complete 0/1/0 rc=0 at 06:36:46Z, log 84a2b41f5bc447ad; readback CodeSha256 07lSH03z53irjBk3AkX2upzUuWzVd4QOuPA4JmisLss= LastModified 06:36:41Z Active Successful | CLOSED 20260924T063805Z |
| V1 | verify | performance root re-plan + readback | 0-diff re-plan; handler runtime.lambda_handler / 1536 MB / two layers unchanged | re-plan -detailed-exitcode rc=0 No changes at 06:37Z; readback Handler runtime.lambda_handler, MemorySize 1536, Layers irpt-common:5 + irpt-performance-native-layer:1 -- the root in the backend worktree reads 0 against the live function (the CLOUD root's entry.lambda_handler / 512 MB / one layer is the trunk's stale copy, superseded when this branch drains) | CLOSED 20260924T063805Z |
| R1 | git | deploy recorder | record-terraform-deploy commit | record-terraform-deploy.sh investor-reporting --function irpt-performance-adapter: commit 3e46ea7ee6 on irpt-p-publish-20260923 (map aa0c453006) | CLOSED 20260924T063806Z |
| S1 | verify | served refusal codes | relationship -> SELECTION_UNSUPPORTED; single account not UNEXPECTED (next trace / HAR) | 4.0.0_SA_CRO 100381 (06:40:20Z), an independent instrument on the DEPLOYED bytes (zip sha256 == 07lSH03z, 61 members, registry ACTIVE + enforcement_ref 0a101a6668): ARM A single account acc_d486fc.. -> retention gate PASSES, stops at OneUseTransportFactory VendorEgressRefused -> DEPENDENCY_UNAVAILABLE (hop 4 CLOSED; hop 6 the plan is the first gate); ARM B two accounts -> SelectionUnsupported before any read -> SELECTION_UNSUPPORTED (hop 3 CLOSED); CONTROL RetentionRefused -> DEPENDENCY_UNAVAILABLE at the new boundary vs UNEXPECTED at the old (MRO walk load-bearing). No user traffic since 05:28Z; the HTTP-path envelope reads the same codes on Andrew's next HAR | CLOSED 20260924T064456Z |

## Log

- 20260924T063528Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260924T063805Z LEG A1 closed: safe-apply (tools terraform 1.9.8, backend performance root) of the saved plan 0/1/0 (hash + version only): source_code_
- 20260924T063805Z LEG V1 closed: re-plan -detailed-exitcode rc=0 No changes at 06:37Z; readback Handler runtime.lambda_handler, MemorySize 1536, Layers i
- 20260924T063806Z LEG R1 closed: record-terraform-deploy.sh investor-reporting --function irpt-performance-adapter: commit 3e46ea7ee6 on irpt-p-publish-2
- 20260924T063857Z HELD-SOVEREIGN-GATED gate=external/S1 served reading: 4.0.0_SA_CRO's next Performance trace or Andrew's next HAR sh
- 20260924T064456Z HOLD RELEASED -> OPEN
- 20260924T064456Z LEG S1 closed: 4.0.0_SA_CRO 100381 (06:40:20Z), an independent instrument on the DEPLOYED bytes (zip sha256 == 07lSH03z, 61 members, re
- 20260924T064456Z CLOSED -- all 4 legs proven
