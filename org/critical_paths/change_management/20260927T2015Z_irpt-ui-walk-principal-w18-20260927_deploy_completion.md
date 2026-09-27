# Deploy Completion Record
**Date opened:** 2026-09-27T20:15:32.346973+00:00
**Status:** OPEN
**Deploy:** Window 18: ~D round-8 read-only walk (DEV 3b98939b) + K7/K8 on the async export Ulim/gmf + ~Y's 4 identity reads on the resident session; walker ~D; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the W18 blob; CRO walker DISARMED reported; pins re-read equal; pre-read + censuses; put + read-back | Both halves at HEAD naming blob b74de7e4 (@ec6aae3838): CTO @7ffe09ff0b 102078 (part C: journal re-capture and session_refresh counts, non-zero BLOCKING), CRO @8d09b3994c 102079 (citation fix recorded here: part C's authority is CTO 102028 (1) on Andrew's 09-26 word 'egress is permitted for API calls', not MSTR 101850 via CTO 101854). Part C runner re-signed on blob 3373f308 (@8b62d16176, the unit-name fix): CTO @5b85a6ddfe 102095, CRO 102096. CRO ui-walker DISARMED 20:46:39Z (102091). Pins re-read 20:50Z equal: export Ulim/gmf IRPT_EXPORT_RENDER=on TIMEOUT 120 retries 0; render doc v5; adapter bOefL9nx plan null bucket opal-data-ycharts; irpt-status bMMJ/bQ+5; directory-search o1TXq5PH; resident root fe64236bbb-lt, queue 0/0; portal DEV 3b98939b, 0 tracked changes. Pre-read epoch 1790542273 ABSENT. Censuses before (20:51Z): users 51 digest 76cbe66b, SELECTION# 66; W18 chain census; walk_window_census: REPORT# 49F 21 / COT 3 / INF 1, 49F rows 148, evidence objects 4, exr_ pointers 0, render tokens 0, tracked media 929, arm-3 owner sha12 f456df347d7e. K1-CRED then K1 put USER#usr_irptuiwalk_1790542273 at 20:51:51Z, read-back EQUAL. Cap: 120 min = 22:51Z. | CLOSED 20260927T205215Z |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound | ~D 102099: logged in 20:52:58Z, password read by name only. 20:54:19Z: ssm delete-parameter /irpt/ui-walk-principal/1790542273/password -> ParameterNotFound (ALREADY absent); get-parameter -> ParameterNotFound. The parameter was removed between ~D's read and 20:54:19Z by an actor not yet named: CloudTrail DeleteParameter since 20:50Z returned 0 events at 20:5xZ (delivery lag); the deleter is read at the A1 audit. | CLOSED 20260927T205523Z |
| K8 | verify | ONE export on the async path | POST QUEUED exr_ under 29 s (HAR); pointer BUILDING -> SUBMITTED with binding; receipt READY %PDF or named FAILED; grant/receipt name the caller; owner unchanged; exactly 2 invocations for the POST |  | OPEN |
| Y1 | verify | 4 identity reads | ONE SSM run of comparison_identity_read_20260927.sh: 4 statuses or a recorded stop; lease holder empty after; queue 0/0 before/after; evidence file sha256 | ONE SSM AWS-RunShellScript a18ad551-cb4d-4dbf-9e68-23741a067851 (20:52:47Z) of runner blob 3373f308 (file sha256 dea4cd99..) on i-0167fd745ad906a66: Success rc 0, running root /opt/irpt-resident/fe64236bbb-lt; reads sent 4 of 4, stopped None, statuses [200,200,200,200], all application/json, login_destination false. Each identity returned exactly 1 row with its security_id, detailed_security_type model_portfolio; names 'Opal Long-Term ' and 'Opal Ultra Long-Term ' carry a TRAILING SPACE (P:1728413, P:1728420), 'Opal Short-Term' and 'Opal Intermediate-Term' exact -- ~Y's grader decides. Queue 0/0 before and after. _opal PROVIDER_OPERATION# lease after: holder '' expires_at 0 (released), operation_version 246, session_fence 13. CTO item: resident journal since 20:52:47Z: capture-pattern lines (unit) 0, session_refresh (unit) 0, capture-pattern lines (all units) 0 -- grep counts with no positive control of the log wording (stated). Evidence file org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/COMPARISON_IDENTITY_READS_W18_20260927.json sha256 424eb3bf70d9975250cc8351de025930f72715b76b8586cad936515e86250194 (retrieved_at 20:52:56Z). Vendor writes 0; no S3, queue or job row written. | CLOSED 20260927T205704Z |
| D1 | verify | K1 delete after every job is terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; writes traced; users == baseline; 0 new media; K1 absent |  | OPEN |

## Log

- 20260927T201532Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260927T205215Z LEG C1 closed: Both halves at HEAD naming blob b74de7e4 (@ec6aae3838): CTO @7ffe09ff0b 102078 (part C: journal re-capture and session_r
- 20260927T205523Z LEG K1C closed: ~D 102099: logged in 20:52:58Z, password read by name only. 20:54:19Z: ssm delete-parameter /irpt/ui-walk-principal/1790
- 20260927T205704Z LEG Y1 closed: ONE SSM AWS-RunShellScript a18ad551-cb4d-4dbf-9e68-23741a067851 (20:52:47Z) of runner blob 3373f308 (file sha256 dea4cd9
