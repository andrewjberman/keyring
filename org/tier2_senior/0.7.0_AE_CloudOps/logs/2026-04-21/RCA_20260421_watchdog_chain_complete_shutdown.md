# RCA — Watchdog fired 37s after chain completion, killed instance

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-21
**Instance:** bd-gold-qa-runner (i-0090b823a4a0997e3)
**Handed off from:** 0.6.0_AE_PartnerETL brief (`docs/briefs/watchdog-kill-during-active-gold-run-2026-04-21.md`)

---

## Verdict

**Not a mid-run kill.** The C chain completed successfully at 18:25:17Z. The watchdog fired 37 seconds later at 18:25:54Z after finding zero gold processes. All prior hypotheses (H1-H4 from the brief) are ruled out.

---

## Root Cause

`--no-shutdown` only gates `gold_dispatch.sh`'s own shutdown calls. The watchdog is a completely independent systemd timer. When the chain completes, gold processes exit; the watchdog fires next cycle, finds nothing, and shuts down. There is no mechanism that tells the watchdog "the operator intends to dispatch another chain."

---

## Timeline (UTC)

| Time | Event |
|------|-------|
| 18:09:22Z | Dispatched `--from C_01 --bg --no-shutdown` via SSM |
| 18:16:30Z | C_06 started (28 ProcessPool workers) |
| 18:20:23Z | Watchdog cycle: SKIP — gold process running |
| 18:24:00Z | C_06 complete (wall=475.0s, cpu_avg=3.87%) |
| 18:24:14Z | C_07 complete (wall=13.9s) |
| 18:25:17Z | C_08 complete (wall=63.3s). **CHAIN COMPLETE.** All gold processes exit. |
| 18:25:53Z | Watchdog timer fires (5-min after 18:20:23Z cycle) |
| 18:25:54Z | pgrep: zero gold processes. Watchdog logs SHUTDOWN, calls `shutdown -h now`. |
| 18:25:54Z | systemd halt SIGTERM sweep kills the just-started watchdog service process. |
| 18:27:22Z | Instance state = stopped |

---

## Evidence

**Chain log** (`s3://opal-data-bd/gold/logs/from_C_01_20260421_180919.log`):
```
[PERF] C_06.client_mix_timeseries  wall=475.0s  cpu_avg=3.87%  mem_peak=181775MB
[PERF] C_07.advisor_attribution    wall=13.9s   cpu_avg=3.43%  mem_peak=3619MB
[PERF] C_08.advisor_fee_efficiency wall=63.3s   cpu_avg=18.33% mem_peak=5526MB
CHAIN from:C_01 COMPLETE
Finished: 2026-04-21T18:25:17Z
```

**Watchdog log** (`/var/log/watchdog-shutdown.log` via SSM):
```
[2026-04-21T18:20:23+00:00] WATCHDOG: SKIP: gold process is running
[2026-04-21T18:25:54+00:00] WATCHDOG: SHUTDOWN: no gold process, uptime 42m, no keep-alive marker
[2026-04-21T18:25:54+00:00] WATCHDOG: Initiating shutdown...
```

**Journal** (t+1s kill pattern):
```
Apr 21 18:25:53 systemd[1]: Starting BD Gold QA Runner - Watchdog Shutdown Check...
Apr 21 18:25:54 systemd[1]: watchdog-shutdown.service: Main process exited, code=killed, status=15/TERM
```
The SIGTERM was from the halt sequence the watchdog itself triggered — not an external kill.

---

## Hypothesis Dispositions

| Hypothesis | Disposition | Basis |
|---|---|---|
| H1: pgrep regex missed C_06 workers | RULED OUT | Chain was complete — no workers to miss |
| H2: concurrent external shutdown | RULED OUT | SIGTERM was watchdog's own halt sequence, not external |
| H3: prior cycle issued `shutdown +N` | RULED OUT | Script uses `shutdown -h now` exclusively; no delay scheduling |
| H4: `--no-shutdown` not honored | RULED OUT | Both shutdown sites in gold_dispatch.sh gated by `NO_SHUTDOWN` (lines 864-867, 927-930); verified by direct read |

---

## On Andrew's CPU Threshold Question

There is NO CPU-usage-based shutdown threshold in the watchdog or any other script. The watchdog checks only: (1) pgrep process name match, (2) uptime >10min, (3) `/tmp/GOLD_KEEP_ALIVE` file, (4) S3 trigger-pending key. The `cpu_avg` values logged by `gold_prof.py` are observability only — no shutdown logic reads them. C_06's 3.87% cpu_avg with 28 workers is low because the 475s wall time is dominated by S3 I/O; compute bursts are higher.

---

## Fix (Implemented)

### gold_dispatch.sh — write GOLD_KEEP_ALIVE when `--no-shutdown=1`

After the `--bg` parent exits (so only in the actual execution child), write `/tmp/GOLD_KEEP_ALIVE` before the chain starts. Leave it in place after completion. This tells the watchdog "operator is in session, don't shut down." The marker persists until the operator removes it (`rm /tmp/GOLD_KEEP_ALIVE`) or the watchdog TTL expires.

```bash
if [ "$NO_SHUTDOWN" = "1" ]; then
    touch /tmp/GOLD_KEEP_ALIVE
fi
```

File: `data/black_diamond/scripts/gold/gold_dispatch.sh` (after line ~800, post `--bg` block)

### watchdog-shutdown.sh — add 1h TTL to marker check

Prevents indefinite cost accumulation if the operator forgets to clean up the marker. If the marker is older than 3600s, treat as stale and proceed to the shutdown decision.

```bash
MAX_KEEP_ALIVE_AGE_SECONDS=3600
if [ -f "$MARKER" ]; then
    MARKER_AGE=$(( NOW_EPOCH - $(stat -c %Y "$MARKER") ))
    if [ "$MARKER_AGE" -lt "$MAX_KEEP_ALIVE_AGE_SECONDS" ]; then
        log "SKIP: $MARKER exists (age ${MARKER_AGE}s) -- instance held alive"
        exit 0
    else
        log "WARN: $MARKER is stale (age ${MARKER_AGE}s > ${MAX_KEEP_ALIVE_AGE_SECONDS}s TTL) -- treating as absent"
    fi
fi
```

File: `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh`

---

## Operator Workflow (Post-Fix)

```
dispatch --from C_01 --bg --no-shutdown   # writes /tmp/GOLD_KEEP_ALIVE
  ... chain runs ...
  ... chain completes ...
  ... watchdog fires, sees marker, SKIPS shutdown ...
dispatch --from D_00 --bg --no-shutdown   # refreshes /tmp/GOLD_KEEP_ALIVE touch time
  ... next chain runs ...
  ... when fully done:
rm /tmp/GOLD_KEEP_ALIVE                   # explicit operator release
  ... watchdog next cycle: no marker, no processes, shuts down ...
```

If operator forgets to remove: watchdog TTL (1h) acts as safety net.

---

## Telemetry Gap (Noted, Not Blocking)

`gold_prof.py` PERF logs provide per-script cpu_avg/mem_peak after each script completes. There is no real-time instance-level CPU/memory stream during a run. The gap is: an operator watching SSM has no live visibility into whether the instance is actually working between PERF log lines. This is a separate hardening item — not the root cause of this incident, but worth a dedicated telemetry TO (CloudWatch Agent + basic CPU/mem metrics at 60s resolution would cost pennies and eliminate this class of ambiguity).

---

## Deploy Path

Both modified files require upload to S3 before they take effect on the instance:
- `gold_dispatch.sh` → `s3://opal-data-bd/code/gold/gold_dispatch.sh` (DS owns this per ADHC_DSFLOW)
- `watchdog-shutdown.sh` → `s3://opal-data-bd/code/runner/watchdog-shutdown.sh` (0.7.0_AE owns this)

The QA runner's watchdog reads the live on-disk copy at `/home/ubuntu/gold-layer/watchdog-shutdown.sh`. After S3 upload: run `aws s3 cp s3://opal-data-bd/code/runner/watchdog-shutdown.sh /home/ubuntu/gold-layer/watchdog-shutdown.sh` via SSM on i-0090b823a4a0997e3 to take effect without a restart.

For PROD (i-01003b035d2988dfb): same watchdog script is used — same fix applies, but coordinate with EventBridge schedule before deploying.
