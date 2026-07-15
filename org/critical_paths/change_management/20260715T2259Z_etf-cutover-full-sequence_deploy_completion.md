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
2. [DONE 23:36Z, 0.7.0, v0.21.0] Notification rules 6-8 LIVE exactly as DS filled them
   (silver-etf-divz/-idvz .html + silver-etf-filepoint .csv -> opal-assets-silver-etf);
   14 configs live-verified, all 11 pre-existing intact (plan-JSON net-set check). Rule 9
   msn: struck, never landed.
3. [DONE 23:36Z, 0.7.0, tag etfs-netassets-v1.2.0] SILVER_ROOT="" LIVE (env read-back exact
   empty string; other 3 vars intact; 0-diff). NOTE: the v1.2.0 tag consumed by this leg;
   the V2-1+msn producer swap re-tags v1.3.0 (CTO 233744Z).
4. [STOP-AND-REPORT 23:42Z, 0.5.0 -- at CTO's gate, NOT a failure] Verify fire executed
   23:37:27Z (pre-fire live env read: SILVER_ROOT="" exact, sha 40KaO/7j held -- one
   variable). GREEN: bronze 4/4 refreshed 23:37:34; legacy LIVE silver 5/5 fresh 23:37:39
   (the flip PROVEN on live keys); event wiring PROVEN behaviorally (4 bronze writes -> 4
   converter invocations timed to them, clean); fact-table content green (6 tables read back;
   conservation 85+23=108 ties). THE GAP (letter of clause c): fact tables carry 23:30:15-16
   stamps -- a single silent invocation pre-fire wrote them from the 22:00 bronze (provenance
   asked of 0.7.0: leg-2 exercise vs container sweep; both lawful); my fire's invocations
   SKIPPED-IF-LANDED (idempotent discipline, bytes identical) -- so post-re-fire fresh fact
   stamps are impossible BY DESIGN on an already-converted date. Disposition at CTO's gate:
   (i) clean-by-mechanism -> leg 5 tonight, or (ii) leg 5 waits on tomorrow's natural 22:00Z
   full-path write. Converter-silence calibration on the record: the 23:30 WRITING run also
   printed zero application lines -- log-silence discriminates nothing for this lambda.
5. [HELD at the leg-4 STOP, 0.5.0] Disable Windows task "ETF NetAssets Daily Probe" (root
   TaskPath; next run 07-16 6:00 PM ET) + ledger CLOSE + evidence to CTO/COO. Fires only on
   CTO's leg-4 disposition (i), or after tomorrow's natural fire under (ii).

## Rollback
Per leg: 0.7.0's swap/TF legs each carry their own plan-gated revert (artifact re-swap /
locals re-flip -- both single-value TF changes). Leg 4 dirty = STOP, report, laptop stays
(next laptop fire 07-16 6:00 PM ET covers continuity -- the fallback IS the rollback).
Leg 5 reversal = Enable-ScheduledTask (one command). A half-landed sequence is NEVER left:
any stop point is recorded here with the completed-legs state.
