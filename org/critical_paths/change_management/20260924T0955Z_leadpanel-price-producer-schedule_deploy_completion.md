# Deploy Completion Record
**Date opened:** 2026-09-24T09:55:26.199712+00:00
**Status:** OPEN
**Deploy:** Lead Panel PRICE producer: add an ISOLATED price leg (rc 80-83, disjoint) to scheduled_daily_pull.cmd so the box-side price_axis_pull.py runs on the existing OPAL_BBGTML_daily_pull 07:00 ET schedule. Producer already works (QA fire 2026-09-24T09:52Z landed as-of 2026-09-23, 64/64 rows, 2/2 pointers); ONLY the trigger was absent. Mandate: org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/BG_BBGTERMINAL_PRICE_PRODUCER.md (B1-B4). Site-Z scheduled tasks run the WORKING TREE, so the .cmd edit IS the deploy.
**Authored by:** 0.0.3_BG_BBGTerminal
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | scheduled_daily_pull.cmd :price_leg inserted between :cons_leg and :prune, own RC_PRICE, exit codes 80-83 disjoint from models 0/1/9/20/30/40/50, ETF 60-63, constituents 70-73 | file on disk + commit hash (LOCAL; this seat commits and does not push) |  | OPEN |
| L2 | verify | control flow re-derived at source across ALL reach paths: price leg reached from cons success, cons failure and :cons_missing; NOT reached from :precond_down (rc 50) nor from a pull failure with DAPI_OK=0; %RC% never touched | path enumeration read back from the SAVED file, not from intent | CONTROL FLOW RE-DERIVED FROM THE SAVED FILE (not from intent): labels+gotos enumerated at scheduled_daily_pull.cmd -- all THREE constituents outcomes reach :price_leg (:288 success, :294 failure, :299 :cons_missing via an EXPLICIT goto, never fall-through); all FOUR price arms reach :prune (:347 :353 :358 :363 :368 -> :370); :precond_down (:107->:115) and a pull failure with DAPI_OK=0 (:147) still bypass every landing leg. %RC% is never assigned after :cons_leg (grep over :279-400 = 0 hits). EXERCISED 6 of 6 arms in an isolated harness (scratchpad/exercise_price_leg.py, stub producer, no Bloomberg/S3/DynamoDB): rc0->RC_PRICE=0, rc3->81, rc1->82, rc62->82, script-missing->80, interpreter-missing->83, and the models-chain %RC% sentinel 7777 survived 6 of 6. NOTE the harness's own first cut was WRONG and is recorded: index(':price_leg') matched the substring inside 'goto :price_leg' and produced a self-looping extract that emitted no stdout; anchored on the line-start label it passes. File integrity: 17702->21406 bytes, CRLF 304->375, bare LF 0, non-ascii byte delta 0. | CLOSED 20260924T101238Z |
| L3 | activation | the 07:00 ET OPAL_BBGTML_daily_pull scheduled fire executes the PRICE leg | the run log's PRICE LEG EXIT CODE line + Get-ScheduledTaskInfo LastRunTime/LastTaskResult |  | OPEN |
| L4 | verify | a PRICE generation dated the trading-day frontier, written BY THE SCHEDULED FIRE and not by the ad-hoc QA fire | _CURRENT pointer read: as_of_date at frontier AND generation_id/run_id distinct from the 09:52Z ad-hoc run R20260924T095217Z |  | OPEN |

## Log

- 20260924T095526Z OPENED by 0.0.3_BG_BBGTerminal with 4 leg(s)
- 20260924T101238Z LEG L2 closed: CONTROL FLOW RE-DERIVED FROM THE SAVED FILE (not from intent): labels+gotos enumerated at scheduled_daily_pull.cmd -- al
