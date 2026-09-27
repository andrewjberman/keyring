# Deploy Completion Record
**Date opened:** 2026-09-27T13:53:43.985746+00:00
**Status:** OPEN
**Deploy:** window 13: the Analysis chain, fifth attempt, on resident cw (W11 fixes) -- ~Y's ONE upload + ONE Overview (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W13_ANALYSIS_20260927.md); Andrew-direct at ~Y @460e2ae8cb; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; pins (resident cw) re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 49ee40b0 (CTO @99311001d3 101903, CRO @ce115a43f1 101904: window 11's conditions carry; create only after window 12 closes -- W12 closed 14:03:20Z @d187e201b2); pins re-read 14:1xZ equal: generate G/TqLPdL, irpt-status bMMJ/bQ+5, adapter bOefL9nx no plan; resident (SSM) active on /opt/irpt-resident/fe64236bbb-cw, irpt-generation 0/0; ycharts/session/current AWSCURRENT d38f6941.. AWSPREVIOUS 02e53a44..; C: 12 GB free; pre-read epoch 1790518192 K1/email/K1-CRED ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 1 / INF 1, W13 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790518192 at 14:11:33Z, read-back EQUAL; cap cron 49acdd12 at 16:05Z (120 min = 16:11Z). RUNNING WAF re-capture total: 0 completed before W13. | CLOSED 20260927T141239Z |
| K1C | verify | K1-CRED deleted after ~Y's login | ParameterNotFound |  | OPEN |
| K5 | verify | ONE Analysis job | terminal state; status GETs <= 6, re-captures <= 1, saved-portfolio GET <= 1, from the journal; running re-capture total |  | OPEN |
| D1 | verify | K1 delete after every job terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; keys traced to K4/K5; users == baseline; K1 absent |  | OPEN |

## Log

- 20260927T135343Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T141239Z LEG C1 closed: both halves at HEAD naming blob 49ee40b0 (CTO @99311001d3 101903, CRO @ce115a43f1 101904: window 11's conditions carry; 
