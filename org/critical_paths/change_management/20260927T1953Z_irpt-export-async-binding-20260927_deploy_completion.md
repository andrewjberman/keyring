# Deploy Completion Record
**Date opened:** 2026-09-27T19:53:29.679331+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T201103Z
**Deploy:** irpt-export-render 8nkjGpT0 -> binding + client refusal copy (backend 118612b599; CRO 102039, CTO 102041/102044 (a)); code only; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload | census vs live 8nkjGpT0: only submit_async.py and prose.py differ; flat import | publish e861ec930c (cherry-pick of backend 118612b599; submit_async.py and prose.py bytes EQ); source map prose.py re-pinned to e861ec930c; build-and-upload rc 0; S3 version JgYVUcWEIR28pGPVe4taHLl18KbskD87, sha Ulim/gmfvzfu..; census vs live 8nkjGpT0: 59 -> 59, differ prose.py + submit_async.py only; flat import OK (REFUSAL_TEXT client copy, submit_async.binding present). Not served until D1. | CLOSED 20260927T195906Z |
| D1 | activation | export root safe-apply | both halves at HEAD naming the delta packet blob; plan 0/1/0 code only; safe-apply; readback CodeSha + MaximumRetryAttempts 0 unchanged; replan 0 | Both halves at HEAD naming delta packet blob 5f45ed04 (@6a4c10d9d9): CTO @cd5899cdfc 102068 (named item: unbound-pointer census re-read before apply + live CodeSha after), CRO @26cfc35706 102069 (no ask). Live before: 8nkjGpT0. PRE-APPLY unbound-pointer census 20:07:33Z: exr_ objects 0, pending.json 0 across firm segments 49financial, cottonwood, inflection. safe-apply bind.tfplan: Apply complete, 0 added, 1 changed, 0 destroyed. AWS readback after: CodeSha256 Ulim/gmfvzfuBvPiHFLUaAlRTwFfCsC2vjoQzHosmSQ= Active/Successful; event-invoke-config MaximumRetryAttempts 0, MaximumEventAgeInSeconds 60 (unchanged). Re-plan: no changes (detailed-exitcode 0). Rollback remains S3 version kN5tj1K0 (8nkjGpT0). | CLOSED 20260927T201102Z |

## Log

- 20260927T195329Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260927T195906Z LEG U1 closed: publish e861ec930c (cherry-pick of backend 118612b599; submit_async.py and prose.py bytes EQ); source map prose.py re-pi
- 20260927T201102Z LEG D1 closed: Both halves at HEAD naming delta packet blob 5f45ed04 (@6a4c10d9d9): CTO @cd5899cdfc 102068 (named item: unbound-pointer
- 20260927T201103Z CLOSED -- all 2 legs proven
