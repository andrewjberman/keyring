# Deploy Completion Record
**Date opened:** 2026-09-30T03:13:56.979492+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T035739Z
**Deploy:** WINDOW 25: one principal, ~Y's S218 step-2 one-body read (W15 CSV, cottonwood Overview); cap 1 / 60 min; credoff before K4; Andrew's word d821060b8b; packet blob pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the packet blob; pins re-read (generate inrij6hL, resident st5 8d1f5431, status, directory-search); queue 0/0 + DLQ; users + walk_window_census before; put + read-back | Halves at HEAD naming packet blob f3273476 (@90aebc3952): CTO 103129 (SIGNOFF_UI_WALK_W25_20260930.md @641044e981, seven conditions), CRO 103131 (NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W25_20260930.md @870ac1736e, five conditions); both blob hashes printed in the files. Pins re-read 03:28Z: irpt-ycharts-generate inrij6hL, irpt-status ZYr+IDMp, irpt-directory-search s0riHZ9h; resident root /opt/irpt-resident/fe64236bbb-st5 active, resident_worker 8d1f5431, pid 307882 (SSM read-only); irpt-generation 0/0; irpt-generation-dlq 1/0. Censuses before: users 51 digest 76cbe66b (UI_WALK_W25_USERS_CENSUS_BEFORE_20260930.json, SELECTION# 146); walk_window_census UI_WALK_W25_CENSUS_BEFORE_20260930.json (49financial 109, cottonwood 7, inflection 1 report rows; 49F rows 737; evidence 19; media 956). walk_principal.py --kind=uiwalk preread 1790739020: K1 ABSENT, email-index 0, K1-CRED ABSENT; create: K1-CRED put /irpt/ui-walk-principal/1790739020/password (value not printed); K1 put USER#usr_irptuiwalk_1790739020 at 2026-09-30T03:30:34.834787Z, read-back digest 2b0a0a4b EQUAL. Window closes 04:30:34Z at the latest. | CLOSED 20260930T033144Z |
| D1 | verify | credoff + K1 delete | credoff ParameterNotFound before K4; K1 consistent read no item; <= 60 min | credoff 1790739020: K1-CRED delete OK, READ-BACK ParameterNotFound at 2026-09-30T03:35:44.624Z, after ~Y's login line 03:34:40Z and before the claim at 03:36:03Z (journal), so no credential existed at K4. K1 delete at 2026-09-30T03:45:34.935Z: consistent GetItem -> no Item (VERIFIED), K1-CRED get-parameter ParameterNotFound; inside the 04:30:34Z cap (15 min after create). DEVIATION, recorded: K1 was deleted on ~Y's 'fired and graded' (103141) before ~Y's hold (03:49Z) and before the job was terminal; packet W25-3 says after terminal. The job is not terminal: state SUBMITTING, message retained; the terminal is unobtainable while the resident is stopped (~Y 103150). The refused-login arm of delete was skipped (credoff had already removed the credential). | CLOSED 20260930T035739Z |
| A1 | verify | write trace | walk_window_census diff traced; users == baseline; DLQ unchanged; ~Y's route record | walk_window_census before 03:28:40Z vs after 03:47:23Z (UI_WALK_W25_CENSUS_BEFORE/AFTER_20260930.json, diff printed): report rows 49financial 109 -> 109, cottonwood 7 -> 7, inflection 1 -> 1; 49F rows 737 -> 737; evidence objects 19 -> 19, evidence_added none; render tokens 0 -> 0; media 956 -> 956; arm-3 owner f456df347d7e equal. users census 51 digest 76cbe66b before and after (SELECTION# 146 -> 146). DLQ irpt-generation-dlq 1/0 before and after (03:53Z), no growth; irpt-generation 1 visible / 0 in flight after (the retained message). ~Y's route record: S225 @040313abdc (one EVICTION verdict=EVICTED on the first vendor call job REQ-86f1ce70, then CAPTURE_FAILED:AUTH_FAILED). No report was produced. The resident was STOPPED by this seat at 03:50:34Z (CTO ruling 103148: leave stopped; stop ratified); row IRPT_BCKEND-S226 ARMED, disarm_owner 2.0.0_SA_COO~P; restart only under a new ledger after the auth cause is fixed and the retained message is handled on purpose. | CLOSED 20260930T035739Z |

## Log

- 20260930T031356Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260930T033144Z LEG C1 closed: Halves at HEAD naming packet blob f3273476 (@90aebc3952): CTO 103129 (SIGNOFF_UI_WALK_W25_20260930.md @641044e981, seven
- 20260930T035739Z LEG D1 closed: credoff 1790739020: K1-CRED delete OK, READ-BACK ParameterNotFound at 2026-09-30T03:35:44.624Z, after ~Y's login line 03
- 20260930T035739Z LEG A1 closed: walk_window_census before 03:28:40Z vs after 03:47:23Z (UI_WALK_W25_CENSUS_BEFORE/AFTER_20260930.json, diff printed): re
- 20260930T035739Z CLOSED -- all 3 legs proven
