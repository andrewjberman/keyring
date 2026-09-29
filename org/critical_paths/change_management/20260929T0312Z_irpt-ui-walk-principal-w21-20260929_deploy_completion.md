# Deploy Completion Record
**Date opened:** 2026-09-29T03:12:31.011787+00:00
**Status:** OPEN
**Deploy:** WINDOW 21: one principal -- page arms K10/K4/K8 (~D) + Analysis bodies Y1-Y6 and revocation R (~Y live_chain.py @78c8ce05a6); packet blob 84ec7f79 (CTO @edfe5875c6 102559, CRO @8abaf67e11 102560)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming 84ec7f79; st3 D1 closed; pins re-read equal and written here; ~D portal pin 0 tracked; pre-read + censuses; put + read-back | Both halves at HEAD naming blob 84ec7f79 (@fb4c7813d9): CTO @edfe5875c6 102559 (re-signed at amendment 1; original @2c0f7560ba 102541), CRO @8abaf67e11 102560 (conditions 1-3 carried). Precondition: st3 D1 CLOSED @a45157fe5a (root fe64236bbb-st3). Pins re-read 03:14Z equal to W21-1: generate AdE17rT6, irpt-status ZYr+IDMp, adapter qfxZ0DzB (no plan), export-render BORQ2shb IRPT_EXPORT_RENDER=on, directory-search o1TXq5PH; irpt-generation 0/0. ~D's portal pin: named by ~D at login (condition 1). Pre-read epoch 1790651636 ABSENT (K1, email-index 0, K1-CRED). Censuses before: users 51 digest 76cbe66b, SELECTION# 68 (W21_USERS_CENSUS_BEFORE); walk_window_census 03:14:41Z (REPORT# 23/3/1, 49F rows 162, evidence objects 14, 2 exr pointers, render tokens 0, media 956, arm-3 owner f456df347d7e); W21 chain census (cottonwood extraction evidence 2, analysis_reports 1). K1 put USER#usr_irptuiwalk_1790651636 at 03:15:34Z (kind uiwalk), read-back digest c4dff268 EQUAL; K1-CRED put /irpt/ui-walk-principal/1790651636/password (value not printed). | CLOSED 20260929T031624Z |
| K10 | verify | status read of REQ-67e12718 | READY ANALYSIS_READY PER_SECTION on the page; RPT-5288c06d opens |  | OPEN |
| K4 | verify | window 15 Dollars CSV | downloads from the page; rows match the report |  | OPEN |
| K8 | verify | ONE export, render to PDF | QUEUED exr_ <29 s; page polls; 0 AccessDenied; READY %PDF or named FAILED; ONE download; 2 render invocations |  | OPEN |
| Y | verify | Analysis bodies Y1-Y6 | <=7 submissions total, W15-2 bounds per body from the journal; each REQ terminal; case_trace per REQ by ~Y; Y5/Y6 only through the foreign-firm name check |  | OPEN |
| R | verify | revocation arm, last | credoff after R's job RUNNING: ParameterNotFound read-back timestamped; R job named terminal; revoked read refused |  | OPEN |
| D1 | verify | K1 delete after every job terminal (<=120 min) | failing consistent read; login after delete refused |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; writes traced; users == baseline; K1 absent |  | OPEN |

## Log

- 20260929T031231Z OPENED by 2.0.0_SA_COO~P with 8 leg(s)
- 20260929T031624Z LEG C1 closed: Both halves at HEAD naming blob 84ec7f79 (@fb4c7813d9): CTO @edfe5875c6 102559 (re-signed at amendment 1; original @2c0f
