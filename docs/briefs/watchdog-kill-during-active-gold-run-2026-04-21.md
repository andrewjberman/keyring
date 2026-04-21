# Briefing — Watchdog killed active gold run mid-C_06 on bd-gold-qa-runner

**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**For handoff to:** 0.7.0_AE_CloudOps (per Andrew direct 2026-04-21)
**Status:** Open investigation — I'm continuing Schwab/Phase 6a work; handing watchdog RCA over so it gets dedicated attention.

---

## TL;DR

`bd-gold-qa-runner` (i-0090b823a4a0997e3) was killed mid-C_06 at **2026-04-21T18:25:54Z** during an active `--from C_01 --bg --no-shutdown` run. The gold_dispatch process tree was legitimately running (C_06 python workers active), but the instance shut down anyway. This matches the pattern of yesterday's 2026-04-20T17:36Z mid-D_02 kill — which we thought we'd fixed via the widened watchdog regex in commit `9139086d`.

The regex IS the widened version on this host — verified. So either (a) the regex's `pgrep -f` missed the C_06 process tree for one cycle, or (b) something else triggered `shutdown -h` concurrent with the watchdog's 5-min tick. Hypothesis (b) is more consistent with the journalctl evidence (the watchdog was KILLED by SIGTERM one second after starting, not firing its own shutdown logic).

Either way: the current widened regex is not fully protective. Worth a dedicated investigation.

---

## Evidence

### Timeline (2026-04-21, UTC)

| Time | Event |
|------|-------|
| 17:26:26Z | I started i-0090b823a4a0997e3 from stopped state |
| 17:47:02Z | Dispatched `--from B_00 --bg --no-shutdown` via SSM `51ce2df1` |
| 17:50:14Z | B_00 wrote canonical/holdings/2026-04-17.parquet |
| 18:01:06Z | B_01 wrote canonical/lots_unrealized/2026-04-17.parquet |
| 18:05:48Z | **B chain COMPLETE** (5 scripts, 18m46s wall). Returned to idle. |
| ~18:05:48Z → 18:09:22Z | **IDLE WINDOW #1** (~3.5 min, no gold process) |
| 18:09:22Z | Dispatched `--from C_01 --bg --no-shutdown` via SSM `1b3e2e3f` |
| 18:11:12Z | C_01 wrote canonical/nna/2026-04-17.parquet (DS's dfaeddc2 merge) |
| 18:11:13Z | C_01 wrote canonical/nna_atomic/2026-04-17.parquet |
| 18:16:30Z | C_06 started (python3 gold_prof.py running C_06.client_mix_timeseries.py with 28 ProcessPoolExecutor workers) |
| 18:23:XXZ | Verified via SSM: PID 19618 bash wrapper + python PIDs 28378/28379/28729/28730 all active, C_06 running |
| 18:25:53Z | Watchdog 5-min timer tick started |
| **18:25:54Z** | **Watchdog killed (SIGTERM). Instance begins shutdown.** |
| 18:27:22Z | EC2 instance state = `stopped` |

### Journal evidence

```
Apr 21 18:25:53 ip-172-31-12-190 systemd[1]: Starting BD Gold QA Runner - Watchdog Shutdown Check...
Apr 21 18:25:54 ip-172-31-12-190 systemd[1]: watchdog-shutdown.service: Main process exited, code=killed, status=15/TERM
Apr 21 18:25:54 ip-172-31-12-190 systemd[1]: watchdog-shutdown.service: Failed with result 'signal'.
```

**Watchdog script ran for ~1 second and was killed by SIGTERM (status 15/TERM).** It did not exit on its own logic. That strongly suggests a concurrent `shutdown -h now` sent SIGTERM to all services, including the just-started watchdog check.

### CloudTrail

- `aws cloudtrail lookup-events ResourceName=i-0090b823a4a0997e3` since 18:20Z returned only my later `StartInstances` at 18:34Z. **No `StopInstances` API event** — so the stop was initiated from inside the instance (`shutdown -h`), not via API.
- Yesterday's 17:36Z kill had the same signature: watchdog-shutdown.service killed 1s after starting.

### Current watchdog script (as live on i-0090b823a4a0997e3)

Location: `/home/ubuntu/gold-layer/watchdog-shutdown.sh`

```bash
# Regex — CORRECT widened version
pgrep -f "run_gold_layer|gold_rebuild|build_gold|gold_dispatch|gold_prof|gold_layer_scripts/"

# Logic: 4 escape hatches (gold proc, min uptime, KEEP_ALIVE marker, pending S3 trigger)
# If all 4 fail: shutdown -h now
```

Timer: every 5 min (`watchdog-shutdown.timer`, active).
Min uptime threshold: 10 min.

### Gold processes at 18:23Z snapshot

```
root  19618  1      bash /tmp/gold_dispatch.sh --from C_01 --no-shutdown
root  28378  19618  python3 /tmp/gold_layer_scripts/gold_prof.py /tmp/gold_layer_scripts/C_06.client_mix_timeseries.py --upload --process-workers 28 --write-workers 28
root  28379  28378  /usr/bin/python3 /tmp/gold_layer_scripts/C_06.client_mix_timeseries.py --upload --process-workers 28 --write-workers 28
root  28729  28379  /usr/bin/python3 /tmp/gold_layer_scripts/C_06.client_mix_timeseries.py --upload --process-workers 28 --write-workers 28
... (more worker PIDs)
```

All four of `gold_dispatch`, `gold_prof`, `gold_layer_scripts/`, and `C_06.client_mix_timeseries.py` (which matches `gold_layer_scripts/`) should hit the `pgrep -f` regex.

---

## Hypotheses

### (H1) Watchdog regex `pgrep -f` missed C_06 workers for one cycle
**Less likely.** The regex's `gold_layer_scripts/` pattern matches the cmdline path `/tmp/gold_layer_scripts/C_06.client_mix_timeseries.py`. However — `pgrep -f` uses the commandline the kernel sees, not the full resolved path. Possible edge case if the ProcessPool worker exec replaced argv[0] or obscured the path momentarily. Unlikely to have a gap long enough for the watchdog to reach `shutdown -h`.

### (H2) A concurrent `shutdown -h` killed the watchdog
**Most likely given journal evidence (watchdog killed at t+1s by SIGTERM).** If shutdown was triggered by some other process in the same second as the watchdog timer fired, shutdown's SIGTERM sweep would kill the watchdog before it could complete its checks. Candidates for the shutdown source:
- `gold_dispatch.sh`'s auto-shutdown path (line 924-925 in the script on S3). My dispatch passed `--no-shutdown`, which sets `NO_SHUTDOWN=1` — needs verification that the flag is honored on every shutdown path, including any partial-completion scenarios.
- A separate monitoring/ops process doing its own idle reap.
- A systemd timer that isn't `watchdog-shutdown.timer` (e.g. `instance-auto-stop.timer` or similar).

### (H3) Watchdog's prior 5-min cycle (18:20:23Z) fired the shutdown
**Also possible.** If the 18:20:23Z cycle decided to shut down but `shutdown -h` scheduled the action for `+N` minutes (not `now`), the actual shutdown would fire later — possibly coinciding with 18:25:54Z. But the script uses `shutdown -h now`, not `+N`, so this would require the delay to be accumulated elsewhere.

### (H4) My `--no-shutdown` flag wasn't honored in some code path
**Merits a direct read of `gold_dispatch.sh`.** From earlier skim: line 924-925 auto-shutdown, line 654 sets `NO_SHUTDOWN=1` on `--no-shutdown`, but need to verify EVERY `shutdown -h` site is gated by `NO_SHUTDOWN`. Looking at the script quickly earlier I saw at least two shutdown call sites (line 865-866 freshness-gate path, line 929 end-of-chain path). Do both check `NO_SHUTDOWN`?

---

## What to investigate

1. **Confirm H2 vs H3 vs H4.** Pull the actual shutdown trigger from `/var/log/wtmp` or `last -x` to identify the process that issued `shutdown -h` and when. If it was gold_dispatch.sh, confirm `--no-shutdown` gating on all shutdown sites in the script.

2. **Verify regex coverage during active C_06.** Simulate: while a `--from C_01 --bg --no-shutdown` run is active in C_06, run `pgrep -f "run_gold_layer|gold_rebuild|build_gold|gold_dispatch|gold_prof|gold_layer_scripts/"` in a loop every 5s for 30m. If any gap appears, H1 is back on the table.

3. **Check for a second watchdog.** `systemctl list-timers --all` + `crontab -l` for root/ec2-user/ubuntu. Any other timer or cron that issues `shutdown -h`?

4. **Contrast with bd-gold-layer-runner (PROD).** PROD ran `--chain full` clean last night (23:00Z EventBridge → 04:20Z failure was B_00 NameError, unrelated). PROD did NOT exhibit this kill pattern. What's different between QA (`i-0090b823a4a0997e3`) and PROD (`i-01003b035d2988dfb`)?
   - Different AMI version?
   - Different watchdog binary?
   - Different systemd units?
   - Different shutdown hooks?

5. **Capture a reproducer.** Next time QA runs, enable `set -x` on `watchdog-shutdown.sh` and pipe to `/var/log/watchdog-shutdown-trace.log` so we can see exactly which branch fires and which pids it sees.

---

## Constraints for the investigator

- **Do not modify production watchdog scripts.** Changes stay in the investigator's scratch on the QA host until root cause is confirmed.
- **EBS root on the instance is persistent** but `/tmp` is `tmpfs` and wipes on stop/start. Any logging must go to `/var/log/` or S3 to survive.
- **Phase 6a RAVC4 is in flight on this instance right now** (I dispatched `--from D_00 --bg --no-shutdown` at 18:38Z to complete the DS dfaeddc2 validation). Please coordinate before any runaway-kill experiments — ping me first, don't hard-stop the instance.
- DS is watching for D-cascade artifacts (expected by ~18:55-19:05Z). After that closes, the runner is free for your investigation.

## Related files

- Watchdog script (live): `/home/ubuntu/gold-layer/watchdog-shutdown.sh` on i-0090b823a4a0997e3
- In-repo copy: `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh`
- Gold dispatch (investigate --no-shutdown gating): `data/black_diamond/scripts/gold/gold_dispatch.sh` (local) and `s3://opal-data-bd/code/gold/gold_dispatch.sh` (deployed)
- Yesterday's RCA for the widened-regex fix: `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-20/RCA_20260420_watchdog_shutdown.md`
- This session's overnight log (shows yesterday's 17:36Z kill): `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/overnight_recovery_schwab_sync_role_aua_backfill.md`

## What I've ruled out

- **AMI / regex regression:** the live script is the widened version. Regex wasn't reverted.
- **Andrew or agent API stop:** no `StopInstances` API event in CloudTrail since I started it at 17:26Z. Stop originated inside the instance.
- **Missing permissions:** SSM doc dispatches worked; aws s3 cp worked from the instance; shutdown runs as root via sudo. No IAM issue.
