# Deploy Completion Record
**Date opened:** 2026-09-27T15:55:19.654011+00:00
**Status:** OPEN
**Deploy:** window 15: the Analysis chain, sixth attempt, on resident lt (release-and-resume + level_as_of_type tolerated) -- ~Y's ONE upload + ONE Overview (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_ANALYSIS_20260927.md); Andrew-direct at ~Y @460e2ae8cb; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; pins (resident lt) re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 51362fca (CTO @04d670fd75 101950: bounds from the journal, an overrun is BLOCKING; the tolerated= value printed, a non-prior_close value is a finding row; CRO @6901753e46 101948: on a non-prior_close value, also name the PDF's level basis); pins re-read 16:0xZ equal: generate G/TqLPdL, irpt-status bMMJ/bQ+5, adapter bOefL9nx no plan; resident (SSM) active on /opt/irpt-resident/fe64236bbb-lt, irpt-generation 0/0; ycharts/session/current AWSCURRENT d38f6941 AWSPREVIOUS 02e53a44; C: 14 GB free; pre-read epoch 1790524948 ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 1 / INF 1, W15 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790524948 at 16:03:44Z, read-back EQUAL; cap cron 43dbb08c at 17:57Z (120 min = 18:03Z). | CLOSED 20260927T160500Z |
| K1C | verify | K1-CRED deleted after ~Y's login | ParameterNotFound | ~Y logged in 16:04:50Z (msg 20260927T160531Z); 16:0xZ ssm delete-parameter /irpt/ui-walk-principal/1790524948/password; the named get-parameter -> ParameterNotFound. | CLOSED 20260927T160620Z |
| K5 | verify | ONE Analysis job | terminal state; status GETs <= 2 per receive x <= 5 receives, 0 read re-captures, saved GET <= 1, the tolerated= line, from the journal | ONE job REQ-67e12718b0ba7c0c70ebb45b (~Y 101954: K4 NORMALIZED 16:06:36Z, K5 QUEUED 16:06:40Z), TERMINAL READY at 16:23:00Z (~Y 101957; watch 16:23:07Z). Resident journal (lt): 16:06:34Z handled=1; 16:07:03Z IRPT_RESIDENT_READ_BACK_RELEASE step=read_back status=200 portfolio_status=calculating source=status polls=2 wall_s=16.8, retained_for_retry class=ReadBackPending code=READ_BACK_PENDING:CALCULATING; (redelivery) READ_BACK_DONE step=read_back status=200 portfolio_status=available source=saved_portfolio polls=1 wall_s=3.6 drifted=- absent=- tolerated=level_as_of_type=custom_date; CERTIFYING -> READY; handled=1. BOUNDS (CTO 101950, from the journal): receives 2 (<= 5); status GETs 2 + 1 (<= 2 per receive); saved GET 1 (<= 1); read re-captures 0 (== 0). No overrun. Running re-capture total: 1 attempted, 0 completed (unchanged). FINDING (CTO 101950 item 2): the stored level_as_of_type is custom_date, not prior_close -- a finding row, not voiding; the CRO's PDF level-basis line rides the amendment-1 audit. Writes: REPORT#RPT-5288c06d6c9799f5251f3a27632ffc1b + the vendor PDF (vendor_documents +1), extraction_evidence +2, platinum analysis_reports +1 -- the FIRST READY Analysis report (FWD-1's Analysis hop, criterion 1). | CLOSED 20260927T162731Z |
| D1 | verify | K1 delete after every job terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; keys traced to K4/K5; users == baseline; K1 absent |  | OPEN |

## Log

- 20260927T155519Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T160500Z LEG C1 closed: both halves at HEAD naming blob 51362fca (CTO @04d670fd75 101950: bounds from the journal, an overrun is BLOCKING; the t
- 20260927T160620Z LEG K1C closed: ~Y logged in 16:04:50Z (msg 20260927T160531Z); 16:0xZ ssm delete-parameter /irpt/ui-walk-principal/1790524948/password; 
- 20260927T162731Z LEG K5 closed: ONE job REQ-67e12718b0ba7c0c70ebb45b (~Y 101954: K4 NORMALIZED 16:06:36Z, K5 QUEUED 16:06:40Z), TERMINAL READY at 16:23:
