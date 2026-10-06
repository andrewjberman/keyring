# Deploy Completion Record
**Date opened:** 2026-09-27T17:26:57.238972+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T023812Z
**Deploy:** irpt-export-render ryEMGlRu -> 3EST/hewG: the export admits the reopen rule's callers (backend f92445392d; CTO 101991 (a)); code only 0/1/0; rollback S3 version 9atDu8b.; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | irpt-export-render apply | both halves at HEAD; census 58/58 only retained_export.py; plan 0/1/0 code only; safe-apply; readback CodeSha 3EST/hewG; replan 0 | both halves at HEAD naming blob 12a1afda (CTO @96a286d416 101994: safe-apply only, CodeSha from the live function; arm 2 on the served bytes by direct invoke or a named departure; CRO @700fecf1a6 101995: roll back to 9atDu8b the same turn on any arm failure); census 58/58 only retained_export.py; re-plan 0/1/0 code only (source_code_hash ryEMGlRu -> 3EST/hewG); safe-apply 17:34:21Z 'Resources: 0 added, 1 changed, 0 destroyed'; readback (live get-function-configuration) CodeSha256 3EST/hewGXFU891RW5Y8T18GtIrrGbGE85Ka9e7hzSI= Active/Successful, IRPT_EXPORT_RENDER=on unchanged; replan -detailed-exitcode 0. Rollback root: S3 version 9atDu8b. (ryEMGlRu). | CLOSED 20260927T173744Z |
| A1 | verify | proof arms | next K8 window: a second in-scope principal exports READY; a principal missing one account refused; owner unchanged; grant/receipt name the caller | SUPERSEDED per CTO batch 270 (msg 105439): the change is PRESENT in the running bytes, read by content 2026-10-06 ~02:2xZ: live irpt-export-render CodeSha256 exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg= (r58); f92445392d (reopen rule): retained_export.py 5 of 6 added lines live, 1 later-edited; every line absent live is also absent from HEAD source (later-edited, so the later version is what runs); negative controls: a fabricated line reads absent, and lines the commit removed read absent from the live member. A1 AS WRITTEN WAS NOT EXERCISED: no recorded invoke of it exists in this ledger or elsewhere I could find; the owed proof is row IRPT_BCKEND-S342 @5f9926e04d (not scheduled; starting an export is a write and may need Andrew's per-use word). Recorded for this ledger: ARM 2 only (V0 direct invoke refused at the Enforcer, 09-27), which is not one of A1's listed arms | CLOSED 20261006T023812Z |

## Log

- 20260927T172657Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260927T173744Z LEG D1 closed: both halves at HEAD naming blob 12a1afda (CTO @96a286d416 101994: safe-apply only, CodeSha from the live function; arm 2
- 20260927T1736Z ARM 2 (CTO 101994 cond 2): the direct invoke as V0 (the synthetic 49F advisor with no grant) on 3EST/hewG was refused at the ENTRY's Enforcer (AuthzError EMPTY_GRANT, public NOT_AUTHORIZED, corr-2bf9a61aa2d9; EXPORT_REOPEN_RULE_ARM2_V0_INVOKE_20260927.json) BEFORE the export authorizer -- a 'missing one account' caller cannot be staged by direct invoke without a real advisor identity holding partial grants, which P does not impersonate: a NAMED DEPARTURE for the next K8 packet, which asks the CTO's half again. The CRO's unit proof ON THE DEPLOYED BYTES (the extracted 3EST/hewG zip's own retained_export.py + repository.py): arm 1 second in-scope principal ADMITTED, owner unchanged, grant delegator = the caller; arm 2 missing one account -> ReportDenied; cross-firm caller -> ReportDenied. Arms 1, 3, 4 live in the next K8 window (A1 open until then).
- 20261006T023812Z LEG A1 closed: SUPERSEDED per CTO batch 270 (msg 105439): the change is PRESENT in the running bytes, read by content 2026-10-06 ~02:2x
- 20261006T023812Z CLOSED -- all 2 legs proven
