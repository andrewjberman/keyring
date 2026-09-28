# Deploy Completion Record
**Date opened:** 2026-09-28T00:11:31.492070+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T004322Z
**Deploy:** Window 20: K10 only (read-only status read of REQ-67e12718 on irpt-status 5fSyChId), DEV 12aa026a; walker ~D; closes before 02:30Z; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the W20 blob; pins re-read equal; pre-read + censuses; put + read-back | Both halves at HEAD naming blob a46f5919 (@8a2548d284): CTO @519ab8bb5c 102255 (page delta 8808eeb6..12aa026a: 10 Performance-tab files, none on K10's path), CRO @802c8fb54d 102256. Pins re-read 00:18Z equal: irpt-status 5fSyChId, directory-search o1TXq5PH, adapter F0bYtOfB plan null, portal DEV 12aa026a 0 tracked. Pre-read epoch 1790554704 ABSENT. Censuses before: users 51 digest 76cbe66b, SELECTION# 66; W20 chain census; walk_window_census 00:18:55Z (REPORT# 21/3/1, 49F rows 148, evidence objects 14, render tokens 0, media 929, arm-3 owner f456df347d7e). K1-CRED then K1 put USER#usr_irptuiwalk_1790554704 at 00:19:33Z, read-back EQUAL. Close before 02:30Z (cap 60 min = 01:19Z). | CLOSED 20260928T002004Z |
| K1C | verify | K1-CRED off after the login | credoff ParameterNotFound read-back with timestamp | ~D 102262: logged in 00:21:02Z. walk_principal.py --kind=uiwalk credoff 1790554704 (boto3): delete-parameter OK; READ-BACK of the real name ParameterNotFound at 2026-09-28T00:25:29.065779Z. | CLOSED 20260928T002606Z |
| K10 | verify | status read of REQ-67e12718 | READY ANALYSIS_READY PER_SECTION on the portal read; RPT-5288c06d opens | RUN and FAILED on the served 5fSyChId (00:28-00:31Z): REQ-67e12718b0ba7c0c70ebb45b's status read answered HTTP 500 x3 (five other REQs answered 200); the page named it 'Status unavailable' with a Check status action (row S28 @1cc15a4e99). Cause (irpt-status log): AccessDenied on original_holdings/ for irpt-status-role, then TypeError public_line(admitted=) from a pin-skewed errors.py -> 500. irpt-status ROLLED BACK to bMMJ at 00:36:31Z (CTO 102269); K10 re-runs on rebuild 3 after 05:00Z. RPT-5288c06d did not open; the sections rendered (46 values, CERTIFIED partial). | CLOSED 20260928T004322Z |
| D1 | verify | K1 delete at the walk end (<= 60 min, before 02:30Z) | failing consistent read | ~D 102278: walk closed 00:38:28Z. 00:42:08Z walk_principal.py delete 1790554704: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (credoff 00:25:29Z). | CLOSED 20260928T004322Z |
| A1 | verify | route audit + write trace | 0 outside the classes (no export/analysis/upload); writes traced; users == baseline; 0 new media; K1 absent | HAR w20-20260928.har (sha256 32e2da7a79a49fda.., 477 entries): writes = login/refresh + 2 directory/resolve + 1 selections; 0 export, 0 analysis submit, 0 upload; 0 outside the classes. Byte-proof (~D): HEAD 12aa026a, 0 tracked, 0 /__mockcot/. Write trace (00:18:55Z -> 00:42Z): REPORT# 21/3/1 unchanged; 49F rows 148 -> 148; evidence objects 14 -> 14 (0 added); render tokens 0; media 929; arm-3 owner equal; users 51 digest 76cbe66b equal; SELECTION# 66 -> 66; chain census +0. K1 absent. | CLOSED 20260928T004322Z |

## Log

- 20260928T001131Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260928T002004Z LEG C1 closed: Both halves at HEAD naming blob a46f5919 (@8a2548d284): CTO @519ab8bb5c 102255 (page delta 8808eeb6..12aa026a: 10 Perfor
- 20260928T002606Z LEG K1C closed: ~D 102262: logged in 00:21:02Z. walk_principal.py --kind=uiwalk credoff 1790554704 (boto3): delete-parameter OK; READ-BA
- 20260928T004322Z LEG K10 closed: RUN and FAILED on the served 5fSyChId (00:28-00:31Z): REQ-67e12718b0ba7c0c70ebb45b's status read answered HTTP 500 x3 (f
- 20260928T004322Z LEG D1 closed: ~D 102278: walk closed 00:38:28Z. 00:42:08Z walk_principal.py delete 1790554704: K1 consistent GetItem no Item (VERIFIED
- 20260928T004322Z LEG A1 closed: HAR w20-20260928.har (sha256 32e2da7a79a49fda.., 477 entries): writes = login/refresh + 2 directory/resolve + 1 selectio
- 20260928T004322Z CLOSED -- all 5 legs proven
