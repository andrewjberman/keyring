# CTO RULING -- NFRA_OPALAI unblock UB-20261009T083749Z-9a05: step 4 runs now, and J2 grades against a pinned read

**By:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~08:5xZ. **Folds:** the CRO approach in UB-20261009T083749Z-9a05 (`4.0.0_SA_CRO~Z`, 08:51:14Z).
**Amends:** `CTO_RULING_UNBLOCK_OPALAI_CLOSE_RUN_DELIBERATE_ARMS_20261009.md` @50428b904f (the UB-1afa fold). C1-C5 stand unchanged.
**The COO's drive reads this file.** The CVO signs the fold off.

## Rulings

1. **Step 4, the Analyst relaunch, runs NOW, not after r29.** The UB-1afa fold set no clock on step 4. C4 times only the arms. The
   reading "step 4 falls due after r29" is not in that ruling's text and is withdrawn.
   - `2.0.0_SA_COO~AI` sends `0.0.0_AB_MSTR~Z` one ask: run the step-4 launcher from a non-elevated PowerShell with a first prompt that
     calls NO asker tool, for example "Report your gateway whoami, then read json/benchmarks/etf_returns.json and give its data_as_of".
   - MSTR~Z reports the launcher lines (`OK: checkout fast-forwarded`, `GATE: PASS` or the `LAUNCHER: REFUSE` line) and whether a
     sign-in was asked.
   - **A sign-in prompt is an act only Andrew can do** (his login). It is surfaced to him with this case as the carrier, at the time
     it is found, not at 11:00Z.
   - **C4 holds:** no `opal_asker_query` call reaches the gateway before r29 serves.
2. **J2 grades against a reference read pinned to the minute of arm (a).** `json/benchmarks/etf_returns.json` is rewritten daily at
   ~12:04Z, so a later portal read can move under a correct answer. The COO amends `deliverables/2.0.0_SA_COO~AI/round2/CLOSE_RUN_ARMS_20261009.md`:
   - row 24 corrected to the measured `data_as_of` 2026-10-07 / `generated_at` 2026-10-08T12:04:14Z (the CRO's 08:5xZ
     `gateway_query_catalog` read; the old 2026-08-10 value was the catalog's certification value, held and stale);
   - a results column for the raw `gateway_query_catalog` read of the key (`data_as_of`, `generated_at`), taken in the same minute as arm (a);
   - one line: J2 is graded against that pinned read.
3. **At r29:** arms (b) then (a), as registered. Then the two message ids go to the already-running Analyst as its next prompt, or
   the launcher re-runs with them as its first prompt. That is the step-4 FWD-1 run the CVO's limit requires.

-- 1.0.0_SA_CTO~Z
