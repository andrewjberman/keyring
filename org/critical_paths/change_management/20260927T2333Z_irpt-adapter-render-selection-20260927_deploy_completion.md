# Deploy Completion Record
**Date opened:** 2026-09-27T23:33:15.413435+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter bOefL9nx -> a RENDER_DELEGATE reads only the grant-pinned selection (backend c8ef8b7751; CTO 102216); code only; built-zip smoke; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + smoke | census vs live bOefL9nx: ONLY entry.py differs; flat extract: import entry (module-level Entry build) and the new functions | publish source map: irpt-performance-adapter staged entry.py re-pinned 52604d790b (7f92ad76 = live = backend c8ef8b7751^) -> c8ef8b7751 (42d9c00e); build-and-upload rc 0 (the build's deletion of tracked performance/*.py restored); S3 investor-reporting/irpt-performance-adapter.zip VersionId G4UtfeeRLWcsPcj7xM1AzJGLOY17238s sha F0bYtOfBw3qw..; census vs live bOefL9nx: 69 -> 69, differ entry.py ONLY. Built-zip flat smoke: the handler module runtime imports (lambda_handler callable), entry imports with _resolve_render_selection and _render_grant callable. Suite: performance 210 passed. | CLOSED 20260927T233820Z |
| D1 | activation | performance root safe-apply | both halves at HEAD; plan 0/1/0 code only (null plan tfvars); readback CodeSha; a cold-start invoke answers; replan 0 | Both halves at HEAD naming blob 66fa5652 (@31ebef549f): CTO @30a4f2670f 102233 (named: cold-start invoke + live CodeSha before any K8), CRO @7f91727da1 102234 (named: a directory republish between export and render fails closed). Live before bOefL9nx. safe-apply rsel.tfplan (performance root, null plan tfvars): 0 added / 1 changed / 0 destroyed at 23:47:48Z. Readback: CodeSha256 F0bYtOfBw3qwHtHAALuGcP77bzMB98mTYSBr+eO6rlM= Active/Successful, plan env null. COLD START: INIT_START 23:47:51Z; the probe (V1, cottonwood, an unknown sel_0x64) REPORT RequestId 76c7d870 Duration 3512.70 ms Init Duration 461.61 ms, FunctionError None, a v1 refusal envelope (SelectionRefused 'selection reference unavailable' -> OBJECT_NOT_COVERED, corr-930878607d8b): the human path through resolve_selection unchanged. Re-plan: no changes (detailed-exitcode 0). Rollback: S3 version 8uohgNwE (bOefL9nx). | CLOSED 20260927T234852Z |
| A1 | verify | next K8 window | the render's Performance read as RENDER_DELEGATE answers (no SelectionRefused); READY %PDF |  | OPEN |

## Log

- 20260927T233315Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T233820Z LEG U1 closed: publish source map: irpt-performance-adapter staged entry.py re-pinned 52604d790b (7f92ad76 = live = backend c8ef8b7751^
- 20260927T234852Z LEG D1 closed: Both halves at HEAD naming blob 66fa5652 (@31ebef549f): CTO @30a4f2670f 102233 (named: cold-start invoke + live CodeSha 
