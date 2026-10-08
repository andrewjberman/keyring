# Deploy Completion Record
**Date opened:** 2026-09-04T13:55:35.605722+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T140208Z
**Deploy:** scheduled_daily_pull.cmd:129 -- a MODELS pull failure skipped the ETF + constituents landing legs, converting one leg's fault into two legs' PERMANENT data loss (the exact harm the file's own :252 comment names). Work order 1.0.0_SA_CTO per :185. Fix routes a failed pull to :etf_leg ONLY when DAPI was VERIFIED UP, preserving the original skip for the genuine Bloomberg-unreachable case -- including the INSTRUMENT-ERROR path at :100 which reaches :pull with NO DAPI verdict. SITE-Z SCHEDULED TASKS RUN THE WORKING TREE: this edit is live at the instant it touches disk
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the .cmd edit committed under 1.0.0_SA_CTO~Z | commit hash | Committed 0f4fd97d17 under 1.0.0_SA_CTO~Z via safe-commit -F. 18 insertions, 0 deletions -- 0 deletions is correct: the original 'goto :prune' SURVIVES as the else-branch rather than being replaced. CRLF detected and preserved; a pre-edit copy was taken to the scratchpad safe harbour first. | CLOSED 20260904T140207Z |
| L2 | verify | control-flow EXERCISED, not read: all four precondition paths simulated (pass / recheck-pass / instrument-error / precond-down) x pull-fail, asserting the landing legs run ONLY where DAPI was verified up | simulation output with the pre-fix behaviour as the control | EXERCISED, not read. A harness carrying the EXACT branch text EXTRACTED FROM THE LIVE EDITED FILE (not retyped) was run across all four cells: DAPI_OK=1/RC=0 -> REACHED-PUBLISH-PATH; DAPI_OK=1/RC=1 -> LANDING-LEGS-RAN; DAPI_OK=0/RC=0 -> REACHED-PUBLISH-PATH; DAPI_OK=0/RC=1 -> LANDING-LEGS-SKIPPED. PRE-FIX CONTROL via the identical harness built from the pre-edit backup: REACHED / SKIPPED / REACHED / SKIPPED. EXACTLY ONE CELL CHANGED (DAPI_OK=1 with a failed pull: SKIPPED -> RAN); the other three are behaviourally identical, so the success path is untouched in both DAPI states and the original skip is preserved exactly where its reasoning applies. Had the pre-fix control also read RAN, the fix would be a no-op and the test vacuous. The fragile construct -- a single-line 'if ... goto' inside a parenthesised block -- is the one the exercise actually proves. | CLOSED 20260904T140207Z |

## Log

- 20260904T135535Z OPENED by 1.0.0_SA_CTO~Z with 2 leg(s)
- 20260904T140207Z LEG L1 closed: Committed 0f4fd97d17 under 1.0.0_SA_CTO~Z via safe-commit -F. 18 insertions, 0 deletions -- 0 deletions is correct: the 
- 20260904T140207Z LEG L2 closed: EXERCISED, not read. A harness carrying the EXACT branch text EXTRACTED FROM THE LIVE EDITED FILE (not retyped) was run 
- 20260904T140208Z CLOSED -- all 2 legs proven
