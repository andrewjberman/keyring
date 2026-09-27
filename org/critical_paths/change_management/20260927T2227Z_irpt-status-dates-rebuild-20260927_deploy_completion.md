# Deploy Completion Record
**Date opened:** 2026-09-27T22:27:43.427210+00:00
**Status:** OPEN
**Deploy:** irpt-status bMMJ/bQ+5 -> rebuild: prospect status dates read the CSV + one-sheet XLSX templates (backend c296cdff9c) + HEAD submission.py (PROSPECT_UPLOAD_LANES) + ops/entry.py render_ports line (bd52efb246); ~Y 102050/102067/102087; code only; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload | census vs live bMMJ/bQ+5: ONLY entry.py, prospect_dates.py, submission.py differ; flat import | publish 5cec1a3892 (ops/entry.py sha256 d9643b2f + ops/prospect_dates.py e5bae585 from backend c296cdff9c); source map: staged submission.py re-pinned 896680c2de -> 5cec1a3892 (sha256 9929a829); build-and-upload rc 0; s3 investor-reporting/irpt-status.zip VersionId zswWyPDnQTBhz6RkbO_MemSJ7tenoQc2 sha HyEyoJ67SlAM..; census vs live bMMJ/bQ+5: 43 -> 43, differ entry.py (9da6a1a6 -> d9643b2f), prospect_dates.py (8ffe01a5 -> e5bae585), submission.py (5460fcdc -> 9929a829) ONLY = ~Y's SERVED_DRIFT_CENSUS three. ops suite 180/22s. Dry plan (ops root): 0/1/0 code only (s3_object_version 7xPCOM83 -> zswWyPDn). render_ports line inert on irpt-status: no IRPT_EVIDENCE_BUCKET in its env (served.py:1102-1103 returns None). | CLOSED 20260927T225139Z |
| D1 | activation | status root safe-apply | both halves at HEAD; plan 0/1/0 code only; readback CodeSha; replan 0 |  | OPEN |
| A1 | verify | K10 in the next Analysis/page window | window 15's READY job reads READY ANALYSIS_READY PER_SECTION on the portal's status read |  | OPEN |

## Log

- 20260927T222743Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T225139Z LEG U1 closed: publish 5cec1a3892 (ops/entry.py sha256 d9643b2f + ops/prospect_dates.py e5bae585 from backend c296cdff9c); source map: 
