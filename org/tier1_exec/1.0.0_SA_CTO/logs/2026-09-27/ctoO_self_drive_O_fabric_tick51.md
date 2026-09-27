# /self-drive ~O fabric -- tick 51 (05:47Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a served release this seat signed went live; its conditions are read against the proofs.

## MX-r-3 LIVE -- every signed condition read off the ledger

`0.9.0_WK_NFRA_MCPINDEX~1` closed the ledger `nfra-mcpindex-r2-gateway-release` with 4 of 4 legs proven (@0ebd5900bb, worker
branch; manifest record @8f7c0dc397). opal-gateway serves `110d93fb73` (base `df724ef284`). Each condition, read from the
L1 and L2 proof text:
- **Condition 1 (the `.env` render):** `ENABLED_INTEGRATIONS` before and after = `ycharts opal_portal globgrph` (unchanged).
- **Condition 2 (the `mcportal` pin):** "INFO: building mcportal @ a3bff71ffa...".
- **Tool list:** 46 before (ssm:6a882d55) and 46 after (ssm:0bb37ad9); the sorted-name diff is EMPTY.
- **Health:** `/health` 200. md5 is 5 of 5 against the release bytes (independent verify ssm:0bb37ad9). NRestarts=0. NOT
  rolled back.

So the served delta is as the two halves bounded it: DELTA = 0 for every caller. The new integrations are shipped and
dormant, and turning them on is Andrew's G-A word. The drain and AC grading stay with `2.0.0_SA_COO~O`.

## Z-S18 closed by its owner

`0.4.0_DS_ClientPlatform~D` (msg 20260927T054621Z):
- 56 files, gate clean 56 of 56.
- 223 safe fixes; 87 noqa rows; 8 local-module F401 imports kept, not removed; 0 py_compile failures.
- **Divergence read (this seat's ruling 2):** all 59 deployed objects equal the PRE-SWEEP bytes, so there was no prior
  drift, and the repo now leads the deploy by lint only.
- 3 refused files (missing `coerce_silver_ids`) are reverted byte-identical to base, and each needs its own functional
  cell. Z-S3, then Z-S6/Z-S11, are started.

## Calls, verdicts

No new call. At Andrew, unchanged: call 1 BLOCKING (the OPLGTW re-seat), call 2 CARRIED (D9 device), and the switchover
sitting. 0 self-drive verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE.

state: ARMED

## Compiler Tools

git show of the worker's ledger close at its pinned commit; the proof column read field by field.
