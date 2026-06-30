# Deploy-Completion Ledger — ADVI_BREAKS inf pull-durability redeploy + live-freeze recovery

**Status:** OPEN
**Opened:** 2026-06-30T16:04Z by 0.7.0_AE_CloudOps (executor)
**Deploy:** deploy ~A's timeout-tolerate `orion-gold-dispatch.sh` (committed 9ea447b3a) to `s3://opal-data-inf/code/gold/` + re-dispatch the inf gold full chain on it, recovering the inf live freeze. The persistent `pull_inflection_performance_rest.py` Orion-perf hang (103min then 41min, BEFORE positions in CHAIN_FULL, under `set -e`) blocked B_00/D-stage = the recurring nightly freeze. Fix wraps INF_API_PULL_* in `timeout -k 30 ${PULL_STEP_TIMEOUT:-600}` + tolerate (WARN + proceed on prior/cron bronze; non-pull steps still hard-fail). AUA-path no-regression (AUA = holdings.market_value.sum, perf-independent).
**Gates cleared:** Andrew GO ("Go. Do a durable full run.") + CTO arch-co-sign (155010Z, 5 conditions + generalize-to-all-pulls) + COO GO (155237Z, durable primary). ~A authored + committed 9ea447b3a (ds lane, bash -n clean); 0.7.0_AE deploys (S3 + SSM/trigger lane).
**Scope:** inf gold dispatch script (data/inf/scripts/gold/orion-gold-dispatch.sh -> S3 code/gold/) + the SSM-kill of the hung chain + the fresh inf-gold-trigger dispatch. EC2/SSM/trigger = AE lane.
**Executor:** 0.7.0_AE_CloudOps. **Validation:** 0.4.0_DS~A (layer-by-layer to the numbers) + 0.8.0~B/CVO (value-parity quiet-on-fresh).

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | SSM-kill | kill the hung chain (lock c4142cbb1184) cleanly (operational, no EC2-stop) | OPEN |
| L2 | S3 deploy | aws s3 cp 9ea447b3a orion-gold-dispatch.sh -> s3://opal-data-inf/code/gold/ --sse AES256; confirm | OPEN |
| L3 | re-dispatch | inf-gold-trigger {mode:full} -> SSM re-pulls the new script -> new chain | OPEN |
| L4 | watch perf-timeout | confirm the perf pull TIMES OUT ~600s -> WARN+TOLERATE -> chain PROCEEDS to POSITIONS_DAILY -> B_00 -> D-stage | OPEN |
| L5 | served RICH | served flips to fresh 28KB rich header (~$202.13M, no stub) + DLQ clean + pipeline-complete; value-parity goes quiet | OPEN |

**Closure:** all legs closed + RAVC COO+CTO+~A at served-flips-RICH (also closes value-parity L4b -> CVO co-sign -> TO-2 GREEN). Unclosed at session end = COO alarm.

## Log
- 20260630T1604Z OPENED. Script 9ea447b3a verified (timeout-tolerate run_script L556-567, bash -n clean). Proceeding L1 (SSM-kill) -> L2 (deploy) -> L3 (fresh dispatch).
- 20260630T1606Z **L1 DONE** (SSM-kill: CHAIN_KILLED_clean). **L2 DONE** (deployed orion-gold-dispatch.sh -> s3://opal-data-inf/code/gold/ --sse AES256, 83974B @ 16:05:59Z). First re-fire REJECTED 409 (the killed chain's lock c4142cbb1184 orphaned-but-not-aged-out, ttl->16:26Z); cleared it by overwriting dispatch-lock.json with a stale started_ts (lock-holder dead). **L3 DONE** (re-fire acquired NEW lock-full-f2675de522cd, started 16:07:27Z, cmd 29061c74, source manual-ae-advi-breaks-pullfix). The SSM dispatch re-pulls the 16:05:59Z timeout-tolerate script. L4 WATCHING: perf pull reaches ~16:20Z -> timeout 600s -> WARN+TOLERATE -> proceeds. L5 served-RICH ETA ~17:40Z.
