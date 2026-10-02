# drive log 2.0.0_SA_COO~H -- 2026-10-02 05Z (opal_bloomberg), relaunch after the site-Z reboot

Relaunch on Andrew-direct ~04:55Z (`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_045xZ_GO_RELAUNCH_SITEZ_AMGT_DEMO_FLEET.md`)
and ~04:59Z "make sure /canonical-drive loops are running for all COOs" (`..._045xZ_CANONICAL_DRIVE_ALL_COOS_RV_CLOSER_DRIVE_RIVALFUNDS_DEMOABLE_TODAY.md`).
The loop is armed on the LIVE_ARMS row `1.0.0_SA_CTO~Z` `/self-drive 60m` (paired COO `/canonical-drive 30m`). The CTO~Z
placement names this lane for AMGT_HARVST despite the row's `closer_contract`. Cron `13,43 * * * *`, confirmed to MSTR~Z
(28202). Lease: FULL.

## tick 1 -- 05:0x-05:3xZ: DRIVE FORWARD (round 36, EXECUTING; TOs 2/5 terminal: ai-1, ai-3 complete; ai-2, ai-4, ai-5 open)

- **bbg drain (ai-4 AC2).** No harvest process survived the reboot. All 291 pending bbg rows were due. The issuer ran
  the driver's own verb, `upload-harvest --retrieval-mode backfill --max-objects 291`, on `.runtime/opal-data-harvest-bbg`
  at about 05:08Z. ai-4 AC2 at 05:0xZ read FAIL: 290 JSONDecodeError pending, 539 uploaded.
- **Row Z-S58 @18ee3ffbd5.** The drain ran at about 1 row per 90 s (541 -> 542 over a measured 90 s). Each row is its
  own (source, run_stamp) group, and each `silver_append` re-reads all 576 bbg silver parts (69 MB). The CTO ruled YES
  to repair cell ai-5 (28222), with one condition: the batched pass writes the same row set as the per-row path.
- **ai-5 cut @e68f90e211** (workstream bbgdrain, slot ~90, sparse worktree `wk-hvst-r36-90`, 43 MB). Base check
  ai-5.AC2 FAIL (280 pending). The worker was spawned. gate2 announced a SEATING false positive, reading
  `0.9.0_WK_AMGT_HARVST~90` as the base `0.9.0_WK_AMGT` (ANNOUNCE mode, not blocking).
- **Item (5) of the wind-down** (the env-var credential offer): the CTO ruled WITHDRAWN (28215). Secrets-by-name stands.
- **Drivers.** STOP and STOP_WSJ were removed. sa (pid 31676; runtime `wk-hvst-r32-92/.runtime/opal-data-harvest`, 58
  pairs planned) and wsj (pid 26928; `.runtime/opal-data-harvest-wsj`, 9 pairs) were relaunched detached with
  `--auto-resume-transient 8`. bbg stays stopped until its drain ends (STOP_BBG). ft stays OFF (STOP_FT). The load
  monitor stays stopped (STOP_MONITOR).
- **ai-2 CORRECTION to tick 46 (03:44Z).** That tick read the ft session as alive. Job 3 then ended `sign_in_refused` at
  03:53:24Z, about 75 min after the 02:38Z hand-solved sign-in. Attempt-3 AC2 = FAIL (3 jobs, 72 min span, 2 stored).
  ~92 was re-seated record-only (no ft traffic) to commit the records and the proof instance. The disposition goes to
  the CTO.
- **Gold #4:** not run. Per 28084 / 28222 it runs after the drain, or from 10:00Z without it, and before 13:00Z.
  Drain at 05:32Z: 559 uploaded, 270 JSONDecodeError + 1 SilverRowError pending.
- **Committed with this log:** `round32/gold_rebuild_signing.json`, the gate's own rewrite during rebuild #3
  (measured_at 20:07Z, mention 5,836 -> 9,498 built), which had been left uncommitted.
