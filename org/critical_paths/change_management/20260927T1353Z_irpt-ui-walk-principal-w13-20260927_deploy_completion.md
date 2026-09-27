# Deploy Completion Record
**Date opened:** 2026-09-27T13:53:43.985746+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T143510Z
**Deploy:** window 13: the Analysis chain, fifth attempt, on resident cw (W11 fixes) -- ~Y's ONE upload + ONE Overview (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W13_ANALYSIS_20260927.md); Andrew-direct at ~Y @460e2ae8cb; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; pins (resident cw) re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 49ee40b0 (CTO @99311001d3 101903, CRO @ce115a43f1 101904: window 11's conditions carry; create only after window 12 closes -- W12 closed 14:03:20Z @d187e201b2); pins re-read 14:1xZ equal: generate G/TqLPdL, irpt-status bMMJ/bQ+5, adapter bOefL9nx no plan; resident (SSM) active on /opt/irpt-resident/fe64236bbb-cw, irpt-generation 0/0; ycharts/session/current AWSCURRENT d38f6941.. AWSPREVIOUS 02e53a44..; C: 12 GB free; pre-read epoch 1790518192 K1/email/K1-CRED ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 1 / INF 1, W13 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790518192 at 14:11:33Z, read-back EQUAL; cap cron 49acdd12 at 16:05Z (120 min = 16:11Z). RUNNING WAF re-capture total: 0 completed before W13. | CLOSED 20260927T141239Z |
| K1C | verify | K1-CRED deleted after ~Y's login | ParameterNotFound | ~Y logged in 14:12:36Z (msg 20260927T141318Z); 14:14:xxZ ssm delete-parameter /irpt/ui-walk-principal/1790518192/password; the named get-parameter -> ParameterNotFound. | CLOSED 20260927T141435Z |
| K5 | verify | ONE Analysis job | terminal state; status GETs <= 6, re-captures <= 1, saved-portfolio GET <= 1, from the journal; running re-capture total | ONE job REQ-2119def4de9e8fea43abb6fe (~Y 101911: K4 UP-d5c8571c.. NORMALIZED 14:14:44Z; K5 200 QUEUED 14:14:48Z), TERMINAL ATTENTION VENDOR_READ_BACK_REFUSED at 14:30:33Z; portfolio 2363820 created and KEPT. Resident journal (cw): 14:14:43Z handled=1; 14:15:26Z STEP_WAF_REFRESH step=read_back status=202 source=status polls=3 wall_s=32.0; 14:16:02Z retained_for_retry class=OperationRefused code=CAPTURE_FAILED:UNEXPECTED_CHALLENGE (capture_env WORKED: no LEASE_NOT_HELD; the form sign-in met a challenge); 14:30:33Z (redelivery) STEP_REFUSED step=read_back status=200 portfolio_status=available source=saved_portfolio polls=1 wall_s=3.5 drifted=level_as_of_type absent=- (the saved read WORKS: 7 of 7 fields present, 6 match, ONE value differs). BOUNDS (CTO 101875, from the journal): status GETs 3 + 1 = 4 (<= 6); saved-portfolio GET 1 (<= 1); host re-captures ATTEMPTED 1 (<= 1), stored 0: intent_session_refresh claimed (fence 1, 1790518526), ycharts/session/current AWSCURRENT still d38f6941 (AWSPREVIOUS 02e53a44). No overrun. RUNNING WAF re-capture total across attempts (CRO 101877): 1 attempted, 0 completed (W11 0 + W13 1 attempted). To ~Y: the UNEXPECTED_CHALLENGE on the form sign-in, and the level_as_of_type value mismatch. | CLOSED 20260927T143509Z |
| D1 | verify | K1 delete after every job terminal (<= 120 min) | failing consistent read | the one job is terminal (ATTENTION 14:30:33Z); queues irpt-intake/generation/export 0/0; ~Y makes no further request (101911); 14:33:10Z walk_principal.py --kind=uiwalk delete 1790518192: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (deleted 14:14:3xZ); cap cron 49acdd12 cancelled. | CLOSED 20260927T143509Z |
| A1 | verify | route audit + write trace | 0 outside the classes; keys traced to K4/K5; users == baseline; K1 absent | Routes: ~Y LIVE_CHAIN_1203_20260927_W13.json = 1 POST /auth/login + 1 POST /analysis/inputs + 1 POST /analysis -> 0 outside the classes. Write trace (W13_CHAIN_CENSUS_BEFORE/AFTER): cottonwood irpt-requests 88 -> 98 (+10 = K4 UPLOAD#UP-d5c8571c / NORMALIZATION# / INPUT#portfolio_a61c028d + ARTIFACT#/RETENTION# original_holdings 925e41f7, normalized d31b9ab5, composition 73854e04 + K5 analysis#REQ-2119def4#1); irpt-jobs/cottonwood 4 -> 5 (+REQ-2119def4); objects +1 original_holdings +1 normalized +1 composition; nothing gone. REPORT# 49F 20->20, COT 1->1, INF 1->1; SELECTION# 49->49; users 51->51 digest 76cbe66b.. equal; session secret versions unchanged. Proof of no later use: K1 absent. | CLOSED 20260927T143510Z |

## Log

- 20260927T135343Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T141239Z LEG C1 closed: both halves at HEAD naming blob 49ee40b0 (CTO @99311001d3 101903, CRO @ce115a43f1 101904: window 11's conditions carry; 
- 20260927T141435Z LEG K1C closed: ~Y logged in 14:12:36Z (msg 20260927T141318Z); 14:14:xxZ ssm delete-parameter /irpt/ui-walk-principal/1790518192/passwor
- 20260927T143509Z LEG K5 closed: ONE job REQ-2119def4de9e8fea43abb6fe (~Y 101911: K4 UP-d5c8571c.. NORMALIZED 14:14:44Z; K5 200 QUEUED 14:14:48Z), TERMIN
- 20260927T143509Z LEG D1 closed: the one job is terminal (ATTENTION 14:30:33Z); queues irpt-intake/generation/export 0/0; ~Y makes no further request (10
- 20260927T143510Z LEG A1 closed: Routes: ~Y LIVE_CHAIN_1203_20260927_W13.json = 1 POST /auth/login + 1 POST /analysis/inputs + 1 POST /analysis -> 0 outs
- 20260927T143510Z CLOSED -- all 5 legs proven
