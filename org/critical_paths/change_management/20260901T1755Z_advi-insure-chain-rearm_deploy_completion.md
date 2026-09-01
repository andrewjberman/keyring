# Deploy Completion Record
**Date opened:** 2026-09-01T17:55:09.594931+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260901T175842Z
**Deploy:** ADVI_INSURE INSR1DS-AC2: RE-ARM the insurance_nav_current stage in _stage_list on 2.0.0_SA_COO's lift 92374, after the scoped IAM grant landed
**Authored by:** 0.4.0_DS_ClientPlatform~R
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | git | CLOUD commit uncommenting the ONE stage entry | commit hash + AST parse + the stage argv DERIVED back out of the committed file | CLOSED. Commit 2adf5583d0 under 0.4.0_DS_ClientPlatform~R. commit-gate clean for 1 of 1 file(s) -- a REAL check (.py). AST parse OK. THE STAGE'S ARGV DERIVED BACK OUT OF THE COMMITTED FILE rather than trusted: [sys.executable,'bd49f_insurance_nav_current.py','--date',date] + u, with u = ['--upload'] if upload else ['--dry-run'] -- the EXACT matrix exercised at 8d5cd96653 (--upload rc=0 emit(dry_run=False); --dry-run rc=0 emit(dry_run=True); native rc=0; --write rc=0; --upload --dry-run rc=0 failing closed; --bogus rc=2 negative control). SCOPE per 92374 s.1: the one entry, nothing else functional. THE COMMENT BLOCK ABOVE IT WAS REWRITTEN AND THAT IS INHERENT TO THE ACT, NOT SCOPE CREEP -- it was headed 'DISARMED', and leaving it would have made the file say DISARMED about a live stage, the exact stale-carrier defect this project annotated its own prior ledger for two hours earlier. | CLOSED 20260901T175841Z |
| R2 | s3-prefix | opal-data-49financial _code/chain_49f_entrypoint.py | comp-pipescript deployed MATCH row + content identity vs the pin + the sha MOVED from the disarmed value | CLOSED. safe-deploy TOOL-03: 'VERIFY OK comp-pipescript deployed ...' + 'gate PASS -- all 1 file(s) deployed and verified'. CONTENT IDENTITY: deployed LF-normalised sha256 d2f991893d3f4175 == the git blob at pin 2adf5583d0. CHANGE-DETECTION CONTROL, captured BEFORE the deploy in the same invocation: the prior served sha was 8defda7bdc7b28b8 (the DISARMED object), so the value MOVED. A bare identity check against an unchanged baseline reads MATCH on a stale object; proving the bytes moved is what distinguishes a real deploy from a no-op that looks clean. | CLOSED 20260901T175841Z |
| R3 | verify | the stage is ACTIVE in the SERVED bytes, 0 -> 1 | 1 active reference in the object pulled back from S3, c02_twr_daily positive control >0, and a bogus-token negative control = 0 | CLOSED, measured on the object PULLED BACK FROM S3, not on the repo copy. ACTIVE (uncommented) lines naming the stage in the SERVED bytes = 1, up from 0 while disarmed -- the 0 -> 1 this leg required. POSITIVE CONTROL: c02_twr_daily = 2 active lines, so the parser sees live code and a zero would have meant something. NEGATIVE CONTROL: a fabricated token = 0, so the matcher discriminates rather than counting any line. The served stage line reads ('insurance_nav_current', [sys.executable, 'bd49f_insurance_nav_current.py', ...]. ⚠ THIS IS NOT AC2's ACCEPTANCE AND DOES NOT CLOSE IT: 91655 s.6 pins that to a PRODUCTION CHAIN RUN NO SEAT HAND-TRIGGERED with the no-hand-invoke control over gold/advi/_logs/. Re-arming makes the acceptance POSSIBLE; it does not supply it. First eligible fire is the 12:45Z cron advi-49f-gold-floor on EventBridge SCHEDULER. And the IAM allow is SIMULATED, never EXERCISED -- only that first real read exercises it. | CLOSED 20260901T175841Z |

## Log

- 20260901T175509Z OPENED by 0.4.0_DS_ClientPlatform~R with 3 leg(s)
- 20260901T175841Z LEG R1 closed: CLOSED. Commit 2adf5583d0 under 0.4.0_DS_ClientPlatform~R. commit-gate clean for 1 of 1 file(s) -- a REAL check (.py). A
- 20260901T175841Z LEG R2 closed: CLOSED. safe-deploy TOOL-03: 'VERIFY OK comp-pipescript deployed ...' + 'gate PASS -- all 1 file(s) deployed and verifie
- 20260901T175841Z LEG R3 closed: CLOSED, measured on the object PULLED BACK FROM S3, not on the repo copy. ACTIVE (uncommented) lines naming the stage in
- 20260901T175842Z CLOSED -- all 3 legs proven
