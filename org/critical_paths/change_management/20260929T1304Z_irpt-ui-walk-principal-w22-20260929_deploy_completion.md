# Deploy Completion Record
**Date opened:** 2026-09-29T13:04:35.031651+00:00
**Status:** OPEN
**Deploy:** WINDOW 22: one principal -- the first Analysis on resident st4, ~Y bodies Y1-Y5 (live_chain.py @78c8ce05a6), cap 5; packet blob 1f3bf0914f (CTO @3b209c072c 102804; CRO pending)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming 1f3bf0914f; st4 D1 closed; pins re-read equal (generate wnt7hjAB, root fe64236bbb-st4, status, directory-search) and written here; queue 0/0 + DLQ count; users + walk_window_census before; put + read-back | Both halves at HEAD naming blob 1f3bf0914f (@6550c62cdf): CTO @3b209c072c (102804; conditions: Y3 reads the NEEDS_CORRECTION row itself if the bound fires; DLQ growth = BLOCKING row), CRO @af1940e31d (102805; conditions: pins re-read at create; credoff/K1 read-backs; Y4/Y5 through the foreign-firm name check, per body the resolve line + terminal state by name). Precondition: st4 D1 CLOSED @4af16f7879. Pins re-read 13:09:53Z EQUAL to W22-1 and to the CRO's 13:01:44Z read: generate wnt7hjAB, irpt-status ZYr+IDMp, irpt-directory-search o1TXq5PH; irpt-generation 0/0; DLQ irpt-generation-dlq 1/0 (pre-existing); resident SSM read: ExecStart root fe64236bbb-st4, MainPID 280258, NRestarts 0, resident_worker 5288ff5a. Censuses before: users 51 digest 76cbe66b, SELECTION# 115 (W22_USERS_CENSUS_BEFORE); walk_window_census 13:10:03Z REPORT# 49F 39 / cottonwood 6 / inflection 1, 49F rows 280, evidence 19, exr pointers 3, render tokens 0, media 956, arm-3 owner f456df347d7e (UI_WALK_W22_CENSUS_BEFORE). Pre-read epoch 1790687432 ABSENT; K1 put USER#usr_irptuiwalk_1790687432 at 13:10:37Z (kind uiwalk), read-back digest 86812647 EQUAL; K1-CRED put /irpt/ui-walk-principal/1790687432/password (value not printed). Ledger files committed inside ~M's bb145ff1fe (shared-index sweep). | CLOSED 20260929T131117Z |
| Y | verify | Analysis bodies Y1-Y5 | <=5 submissions, W15-2 bounds per body; each REQ terminal; case_trace per REQ by ~Y; IRPT_RESIDENT_RESOLVE lines; Y3 reads the NEEDS_CORRECTION row itself if the bound fires (CTO) |  | OPEN |
| D1 | verify | credoff + K1 delete after every job terminal (<=120 min) | ParameterNotFound read-back; failing consistent read; login after delete refused |  | OPEN |
| A1 | verify | route record + write trace | ~Y per-body route record; walk_window_census diff traced; users == baseline; DLQ count unchanged (growth = BLOCKING row, CTO) |  | OPEN |

## Log

- 20260929T130435Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260929T131117Z LEG C1 closed: Both halves at HEAD naming blob 1f3bf0914f (@6550c62cdf): CTO @3b209c072c (102804; conditions: Y3 reads the NEEDS_CORREC
