# Deploy Completion Record
**Date opened:** 2026-09-27T22:27:43.427210+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T231700Z
**Deploy:** irpt-status bMMJ/bQ+5 -> rebuild: prospect status dates read the CSV + one-sheet XLSX templates (backend c296cdff9c) + HEAD submission.py (PROSPECT_UPLOAD_LANES) + ops/entry.py render_ports line (bd52efb246); ~Y 102050/102067/102087; code only; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload | census vs live bMMJ/bQ+5: ONLY entry.py, prospect_dates.py, submission.py differ; flat import | publish 5cec1a3892 (ops/entry.py sha256 d9643b2f + ops/prospect_dates.py e5bae585 from backend c296cdff9c); source map: staged submission.py re-pinned 896680c2de -> 5cec1a3892 (sha256 9929a829); build-and-upload rc 0; s3 investor-reporting/irpt-status.zip VersionId zswWyPDnQTBhz6RkbO_MemSJ7tenoQc2 sha HyEyoJ67SlAM..; census vs live bMMJ/bQ+5: 43 -> 43, differ entry.py (9da6a1a6 -> d9643b2f), prospect_dates.py (8ffe01a5 -> e5bae585), submission.py (5460fcdc -> 9929a829) ONLY = ~Y's SERVED_DRIFT_CENSUS three. ops suite 180/22s. Dry plan (ops root): 0/1/0 code only (s3_object_version 7xPCOM83 -> zswWyPDn). render_ports line inert on irpt-status: no IRPT_EVIDENCE_BUCKET in its env (served.py:1102-1103 returns None). | CLOSED 20260927T225139Z |
| D1 | activation | status root safe-apply | both halves at HEAD; plan 0/1/0 code only; readback CodeSha; replan 0 | Both halves at HEAD naming blob 6b35dca8 (@a489e56b91): CTO @77f49e8b3d 102187 (named: live CodeSha after safe-apply; K10 decides S25), CRO @c20fe9034a 102189 (no ask). Live before bMMJ/bQ+5. safe-apply status_dates.tfplan (ops root): 0 added / 1 changed / 0 destroyed at 23:00:34Z. Readback: irpt-status CodeSha256 HyEyoJ67SlAMqJIUHO8l+P6bX/4hQgTh2o67viaMiVA= Active/Successful. Re-plan: no changes (detailed-exitcode 0). Rollback: S3 version 7xPCOM83 (bMMJ/bQ+5). | CLOSED 20260927T230108Z |
| A1 | verify | K10 in the next Analysis/page window | window 15's READY job reads READY ANALYSIS_READY PER_SECTION on the portal's status read | FAILED DEPLOY, ROLLED BACK (CTO 102202). HyEyoJ67 (served 23:00:34Z) raised at cold start: ops/entry.py d9643b2f calls _entry.render_ports_from_env(), but the zip's served.py (41fbd6b5, staged by pin 896680c2de) predates it -> AttributeError in build_boundary on EVERY request (~Y 102199; 0 invocations reached it before the rollback per ~Y's 23:10Z CloudWatch read). My packet's 'render_ports inert' read the function body, not whether the symbol existed in the packaged served.py -- no extract-and-import smoke was run on the status zip (it was run for the export zips). ROLLBACK per 6b35dca8's signed rollback: S3 version 7xPCOM83 restored as latest (copy, metadata content-sha256 bMMJ/bQ+5 kept -> new latest version 4iznTTWu), plan 0/1/0 back to bMMJ, safe-apply 23:15:52Z; readback CodeSha256 bMMJ/bQ+5RKoYSCgAIkRwEVcMpK6kxNWt3TFdZX6wyI= Active/Successful. Cold-start proof: direct invoke (V1, a status GET for an unknown job) on the fresh code -- Init Duration present, FunctionError None, a v1 refusal envelope (UNAVAILABLE), no AttributeError in the tail. K10 not run. The rebuild is a NEW packet with HEAD _authz/served.py 3a2cdba2 + a flat extract-and-import smoke of the built zip (CTO 102202 item 3). | CLOSED 20260927T231700Z |

## Log

- 20260927T222743Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T225139Z LEG U1 closed: publish 5cec1a3892 (ops/entry.py sha256 d9643b2f + ops/prospect_dates.py e5bae585 from backend c296cdff9c); source map: 
- 20260927T230108Z LEG D1 closed: Both halves at HEAD naming blob 6b35dca8 (@a489e56b91): CTO @77f49e8b3d 102187 (named: live CodeSha after safe-apply; K1
- 20260927T231700Z LEG A1 closed: FAILED DEPLOY, ROLLED BACK (CTO 102202). HyEyoJ67 (served 23:00:34Z) raised at cold start: ops/entry.py d9643b2f calls _
- 20260927T231700Z CLOSED -- all 3 legs proven
