# Deploy Completion Record
**Date opened:** 2026-09-27T23:02:27.979834+00:00
**Status:** OPEN
**Deploy:** Window 19: K10 (read-only status read of REQ-67e12718) + K7/K8 on the adapter decrypt fix and ~D's S26 poll (DEV 8808eeb6); walker ~D; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the W19 blob; pins re-read equal; pre-read + censuses; put + read-back | Both halves at HEAD naming blob 35c9083d (@f39963673f): CTO @266bf56cb5 102195 (named: if READY, print the served PDF's page count + first-page header), CRO @027eb6137a 102196 (K1-CRED read-back rule adopted). Pins re-read 23:09Z equal: export Ulim/gmf on retries 0; adapter bOefL9nx plan null; adapter decrypt statement StringEquals {aws:s3:arn arn:aws:s3:::opal-data-ycharts, ViaService s3.us-east-1}; irpt-status HyEyoJ67; directory-search o1TXq5PH; render doc v5; portal DEV 8808eeb6, 0 tracked. Pre-read epoch 1790550585 ABSENT. Censuses before: users 51 digest 76cbe66b, SELECTION# 66; W19 chain census; walk_window_census 23:10:12Z: REPORT# 49F 21 / COT 3 / INF 1, 49F rows 148, evidence objects 9, exr_ pointers 1 (W18's), render tokens 0, media 929, arm-3 owner f456df347d7e. K1-CRED then K1 put USER#usr_irptuiwalk_1790550585 at 23:10:20Z, read-back EQUAL. Cap 120 min = 01:10Z. | CLOSED 20260927T231100Z |
| K1C | verify | K1-CRED deleted after the login | walk_principal.py credoff: ParameterNotFound read-back with its timestamp |  | OPEN |
| K10 | verify | status read of REQ-67e12718 | READY ANALYSIS_READY on the portal read; RPT-5288c06d opens |  | OPEN |
| K8 | verify | ONE export, render to PDF | QUEUED exr_ <29 s; page polls; render read no AccessDenied; READY %PDF or a named non-W18 FAILED; grant names caller; owner unchanged; 2 invocations |  | OPEN |
| D1 | verify | K1 delete after every job is terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; writes traced; users == baseline; 0 new media; K1 absent |  | OPEN |

## Log

- 20260927T230227Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260927T231100Z LEG C1 closed: Both halves at HEAD naming blob 35c9083d (@f39963673f): CTO @266bf56cb5 102195 (named: if READY, print the served PDF's 
