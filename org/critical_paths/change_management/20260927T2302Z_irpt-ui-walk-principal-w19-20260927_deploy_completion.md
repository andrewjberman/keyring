# Deploy Completion Record
**Date opened:** 2026-09-27T23:02:27.979834+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T235104Z
**Deploy:** Window 19: K10 (read-only status read of REQ-67e12718) + K7/K8 on the adapter decrypt fix and ~D's S26 poll (DEV 8808eeb6); walker ~D; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the W19 blob; pins re-read equal; pre-read + censuses; put + read-back | Both halves at HEAD naming blob 35c9083d (@f39963673f): CTO @266bf56cb5 102195 (named: if READY, print the served PDF's page count + first-page header), CRO @027eb6137a 102196 (K1-CRED read-back rule adopted). Pins re-read 23:09Z equal: export Ulim/gmf on retries 0; adapter bOefL9nx plan null; adapter decrypt statement StringEquals {aws:s3:arn arn:aws:s3:::opal-data-ycharts, ViaService s3.us-east-1}; irpt-status HyEyoJ67; directory-search o1TXq5PH; render doc v5; portal DEV 8808eeb6, 0 tracked. Pre-read epoch 1790550585 ABSENT. Censuses before: users 51 digest 76cbe66b, SELECTION# 66; W19 chain census; walk_window_census 23:10:12Z: REPORT# 49F 21 / COT 3 / INF 1, 49F rows 148, evidence objects 9, exr_ pointers 1 (W18's), render tokens 0, media 929, arm-3 owner f456df347d7e. K1-CRED then K1 put USER#usr_irptuiwalk_1790550585 at 23:10:20Z, read-back EQUAL. Cap 120 min = 01:10Z. | CLOSED 20260927T231100Z |
| K1C | verify | K1-CRED deleted after the login | walk_principal.py credoff: ParameterNotFound read-back with its timestamp | ~D 102211: logged in 23:18:33Z (password read by name). walk_principal.py --kind=uiwalk credoff 1790550585 (boto3, no MSYS path): delete-parameter OK /irpt/ui-walk-principal/1790550585/password; READ-BACK of the real name: ParameterNotFound at 2026-09-27T23:20:08.997963Z (CRO 102121 rule, row S172 remedy). | CLOSED 20260927T232030Z |
| K10 | verify | status read of REQ-67e12718 | READY ANALYSIS_READY on the portal read; RPT-5288c06d opens | NOT RUN, held by CTO 102202 then 102227: irpt-status HyEyoJ67 failed at cold start (rolled back 23:15:52Z); K10 moves to the post-freeze window on the status rebuild 2 (ledger irpt-status-dates-rebuild2-20260927). ~D ran no Analysis history or status view (HAR: 0 status reads). | CLOSED 20260927T235103Z |
| K8 | verify | ONE export, render to PDF | QUEUED exr_ <29 s; page polls; render read no AccessDenied; READY %PDF or a named non-W18 FAILED; grant names caller; owner unchanged; 2 invocations | RUN; a named FAILED one hop past W18. K7 23:20:36Z 8.05% PARTIAL RPT-b5e0a16e. K8: ONE POST /export 23:20:55Z -> QUEUED exr_9f785460503746a6b486950e in 3,460 ms (HAR); the page (8808eeb6, S26 live) issued ONE receipt GET 23:20:58Z -> UNAVAILABLE/NOT_READY and stopped polling (row S27; CTO 102223/102227: R11 contract + a RUNNING receipt answer, after the freeze). Pointer BUILDING -> SUBMITTED EXP-52790d0545476c0d65e00de900f36931. Render SSM cecda10c: token carried then deleted, 14 requests all opalinvest.dev, 0 vendor; the adapter read now DECRYPTS the grant (no AccessDenied: the f7aa7b3c fix holds live) and was refused at selection: corr-6a0911404047 SelectionRefused 'current entitled viewer required' (selection.py:49-50 refuses every RENDER_DELEGATE) -> no PDF. Fixed and SERVED 23:47:48Z (F0bYtOfB, packet 66fa5652). Invocations for the ONE POST: exactly 2 (2fa32b0b HTTP 2,633 ms + f42999ca marked event 38,367 ms), plus the page's one receipt GET 56103e3d. Owner arm-3 sha12 f456df347d7e unchanged. No export-code arm failed: no rollback owed. | CLOSED 20260927T235103Z |
| D1 | verify | K1 delete after every job is terminal (<= 120 min) | failing consistent read | ~D 102232: walk closed 23:39:50Z. The export is terminal at the render (SSM cecda10c Failed). 23:49:43Z walk_principal.py delete 1790550585: login after delete refused; K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (credoff 23:20:08Z). Cap cron 59399710 superseded. | CLOSED 20260927T235103Z |
| A1 | verify | route audit + write trace | 0 outside the classes; writes traced; users == baseline; 0 new media; K1 absent | HAR w19-20260927.har (sha256 9259170dcf103eb2.., 466 entries): writes = POST auth/login 1, auth/refresh 5, directory/resolve 2, selections 3, export 1; 1 receipt GET; the guard blocked 302 analytics POSTs; 0 outside the classes; no download. Byte-proof (~D): HEAD 8808eeb6, 0 tracked, 0 /__mockcot/. Write trace (walk_window_census 23:10:12Z -> 23:49Z): REPORT# 21/3/1 -> 21/3/1; 49F rows 148 -> 148; evidence objects 9 -> 14, added = exactly the export's five (EXP pending, exr pending, narrative_packet, render_grant, bundle); render tokens 0 -> 0; media 929 -> 929; arm-3 owner equal. users 51 -> 51 digest 76cbe66b; SELECTION# 66 -> 66; chain census +0. K1 absent. | CLOSED 20260927T235103Z |

## Log

- 20260927T230227Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260927T231100Z LEG C1 closed: Both halves at HEAD naming blob 35c9083d (@f39963673f): CTO @266bf56cb5 102195 (named: if READY, print the served PDF's 
- 20260927T232030Z LEG K1C closed: ~D 102211: logged in 23:18:33Z (password read by name). walk_principal.py --kind=uiwalk credoff 1790550585 (boto3, no MS
- 20260927T235103Z LEG K10 closed: NOT RUN, held by CTO 102202 then 102227: irpt-status HyEyoJ67 failed at cold start (rolled back 23:15:52Z); K10 moves to
- 20260927T235103Z LEG K8 closed: RUN; a named FAILED one hop past W18. K7 23:20:36Z 8.05% PARTIAL RPT-b5e0a16e. K8: ONE POST /export 23:20:55Z -> QUEUED 
- 20260927T235103Z LEG D1 closed: ~D 102232: walk closed 23:39:50Z. The export is terminal at the render (SSM cecda10c Failed). 23:49:43Z walk_principal.p
- 20260927T235103Z LEG A1 closed: HAR w19-20260927.har (sha256 9259170dcf103eb2.., 466 entries): writes = POST auth/login 1, auth/refresh 5, directory/res
- 20260927T235104Z CLOSED -- all 6 legs proven
