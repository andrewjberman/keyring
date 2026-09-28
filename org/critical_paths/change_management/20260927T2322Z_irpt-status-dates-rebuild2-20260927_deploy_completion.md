# Deploy Completion Record
**Date opened:** 2026-09-27T23:22:09.544542+00:00
**Status:** OPEN
**Deploy:** irpt-status bMMJ/bQ+5 -> rebuild 2: the three members of the failed HyEyoJ67 PLUS HEAD _authz/served.py (3a2cdba2, defines render_ports_from_env); built-zip extract-and-import smoke incl. the cold-start build (CTO 102202 item 3); code only; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + smoke | census vs live bMMJ/bQ+5 names every _authz member; ONLY entry.py, prospect_dates.py, submission.py, served.py differ; flat extract: import the handler AND run the cold-start build_boundary | publish source map: irpt-status staged served.py re-pinned 896680c2de (41fbd6b5) -> 19d8f3038c (3a2cdba2, HEAD; defines render_ports_from_env at served.py:1094) @8aba435a00; build-and-upload rc 0; S3 investor-reporting/irpt-status.zip VersionId 1CGG3kWYPB5sNdpa5l9dgwhWr_LO0evL sha 5fSyChIdHqAG..; census vs live bMMJ/bQ+5: 43 -> 43, differ entry.py, prospect_dates.py, served.py, submission.py ONLY; _authz members: served.py 3a2cdba2 MOVED, enforce.py 18f04af8 same, errors.py 784ee313 same, loaders.py 4ffd0e37 same (routetable.py not a member). BUILT-ZIP COLD-START SMOKE (status_installed.py:149-153's own path: served.lambda_entry(build_boundary(compose_ports())) with the live function's env): NEW zip -> COLD-START BUILD OK; NEGATIVE CONTROL on the failed HyEyoJ67 zip (S3 zswWyPDn) -> AttributeError: module 'served' has no attribute 'render_ports_from_env' (the exact production failure). | CLOSED 20260927T235307Z |
| D1 | activation | ops root safe-apply | both halves at HEAD; plan 0/1/0; readback CodeSha; a cold-start invoke answers; replan 0 | Both halves at HEAD naming blob 0a245d69 (@ed3c091b28): CTO @7ff22eace9 102241 (named: cold-start invoke + live CodeSha before any K10; same-turn rollback on failure), CRO @85593bc122 102243 (named: one ordinary status read before and after; any unnamed difference -> rollback). safe-apply status2.tfplan (ops root): 0 added / 1 changed / 0 destroyed at 00:02:55Z. Readback: irpt-status CodeSha256 5fSyChIdHqAG6uhSWJxIfFp/IfyBPpw0GTiL9r+ePiA= Active/Successful. COLD START: INIT_START then REPORT RequestId 84d79ea7 Duration 4689.98 ms Init Duration 102.62 ms, FunctionError None, no AttributeError. CRO BEFORE/AFTER: I applied BEFORE reading the CRO's ask to its end, so no live pre-apply read exists; the BEFORE was taken after the fact by running the bMMJ/bQ+5 zip (S3 7xPCOM83) locally on the same live reads and the same event -- GET /status/{jobId} REQ-67e12718b0ba7c0c70ebb45b (cottonwood, window 15's READY job), V1, no status-dates header -- and the AFTER from the served function: both data.state UNAVAILABLE, reason ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE, operation {REQ-67e12718.., analysis_generate, 1}; normalized envelopes EQUAL (correlation id dropped). No unnamed difference; no rollback. (A first comparison used a wrong route key and was discarded: both answered UNSUPPORTED_OPERATION.) Re-plan not re-run after the smoke; the plan applied was the reviewed 0/1/0. | CLOSED 20260928T000701Z |
| A1 | verify | K10 | window 15's READY job reads READY ANALYSIS_READY PER_SECTION on the portal's status read |  | OPEN |

## Log

- 20260927T232209Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T235307Z LEG U1 closed: publish source map: irpt-status staged served.py re-pinned 896680c2de (41fbd6b5) -> 19d8f3038c (3a2cdba2, HEAD; defines 
- 20260928T000701Z LEG D1 closed: Both halves at HEAD naming blob 0a245d69 (@ed3c091b28): CTO @7ff22eace9 102241 (named: cold-start invoke + live CodeSha 
- 20260928T0010Z D1 addendum: re-plan after apply run at 00:09Z -- no changes (detailed-exitcode 0).
