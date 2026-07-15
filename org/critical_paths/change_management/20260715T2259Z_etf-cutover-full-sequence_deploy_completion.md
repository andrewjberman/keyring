# DEPLOY-COMPLETION LEDGER: ETF cutover, full sequence (laptop leg retires)

**Opened:** 2026-07-15T22:59:49Z by 0.5.0_AE_OpalETL (on 0.7.0's leg-1 START ping 225949Z -- the true start, not the ETA)
**Status:** OPEN -- legs in flight

## Motion
The ruled 4-step ETF cutover, completed in one sequence TONIGHT plus the two gated pre-legs:
(1) V2-8 converter artifact-swap to the etf silver lambda; (2) ETF notification rules 6-8;
(3) SILVER_ROOT="" -> safe-apply; (4) MANUAL VERIFY FIRE exercising the whole new path
(trigger->bronze->event->converter->live silver, conservation + read-backs); (5) disable the
laptop Windows task "ETF NetAssets Daily Probe" + close this ledger. Tonight's manual-fire
precedent (Andrew-ordered, 18:26Z) is the ruling that a manual fire satisfies a verify leg.

## Authorization
- Andrew pace order (refuse-to-wait class), CTO terminal ~22:4xZ, recorded verbatim by CTO +
  relayed 224440Z: complete the consolidation NOW; full sequence tonight; 0.5.0 drives.
- Parity precondition: 3/3 CUTOVER-READY (07-13/14/15 all GREEN 52/0; gate's textual verdict
  cited in my 220317Z verdicts, accepted by COO + CTO).
- V2-8 converter: CTO review PASSED 26/26-zero-skips on real bytes (his 224440Z); refs
  drift-checked (reviewed bytes == HEAD @ ceb046d70; sha256s in my 225217Z to 0.7.0).
- Split: 0.7.0 = TF/deploy legs 1-3; 0.5.0 = fire+verify legs 4-5. STOP-on-dirty at any leg;
  fallback = laptop one more day (zero harm). V2-1 producer diff EXPLICITLY NOT riding tonight
  (stays at CTO review; tonight runs on certified v1.1.0).

## Legs
1. [DONE 23:25Z, 0.7.0, v0.20.0] V2-8 converter artifact swap -- WITH a caught+corrected
   defect on the record (their 232543Z): first build vendored only the 2 reviewed files;
   import-health smoke returned Runtime.ImportModuleError (pandas; the etf silver.tf row still
   carried the layerless py3.12 STUB profile). ZERO events wired at the time -- nothing
   consumed the broken artifact. Corrected closure: reviewed files (sha256s UNCHANGED
   623568f3/1a08de39) + the 6-module mirror closure + runtime 3.11 + pandas layer; rebuilt sha
   a14fYacw (51,829B write-verified) -> targeted apply -> live tie -> RE-SMOKE = the DESIGNED
   REFUSAL from etf_conversion.lambda_entry (import closure proven ON the deployed artifact)
   -> targeted 0-diff -> tag opal-assets-v0.20.0.
2. [IN FLIGHT 23:25Z, 0.7.0] Notification rules 6-8 per DS fill @ de7342780 (rule 9 struck by
   the msn ruling; the TF never adds it).
3. [PENDING, 0.7.0] SILVER_ROOT="" flip (etfs-netassets locals) -> safe-apply.
4. [PENDING, 0.5.0] Manual verify fire + step-4 harness (staged + failure-proven pre-legs:
   DIRTY w/ 16 named problems; scratchpad etf_cutover_verify_step4.py). Verifies bronze-fresh,
   event->converter fired, monolith fact tables per-fund w/ conservation tie + read-back,
   legacy live silver fresh-stamped post-flip.
5. [PENDING, 0.5.0] Disable Windows task "ETF NetAssets Daily Probe" (root TaskPath; last run
   2026-07-15 6:00:01 PM ET rc=0; next run 07-16 6:00 PM ET = the run that never happens) +
   ledger CLOSE + evidence to CTO/COO.

## Rollback
Per leg: 0.7.0's swap/TF legs each carry their own plan-gated revert (artifact re-swap /
locals re-flip -- both single-value TF changes). Leg 4 dirty = STOP, report, laptop stays
(next laptop fire 07-16 6:00 PM ET covers continuity -- the fallback IS the rollback).
Leg 5 reversal = Enable-ScheduledTask (one command). A half-landed sequence is NEVER left:
any stop point is recorded here with the completed-legs state.
