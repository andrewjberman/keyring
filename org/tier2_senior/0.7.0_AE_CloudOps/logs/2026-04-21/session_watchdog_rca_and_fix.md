# Session Log: 2026-04-21 -- Watchdog kill RCA + fix

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-21
**Tasked by:** Andrew direct (brief from 0.6.0_AE_PartnerETL)
**Brief:** `docs/briefs/watchdog-kill-during-active-gold-run-2026-04-21.md`

---

## TL;DR

Brief mischaracterized the incident as a mid-C_06 kill. Full investigation showed the C chain completed successfully at 18:25:17Z; the watchdog fired 37s later after finding zero gold processes. Root cause: `--no-shutdown` only gates gold_dispatch.sh's own shutdown — the watchdog is independent and has no way to know the operator intends to dispatch another chain. Fix: gold_dispatch.sh now stamps `/tmp/GOLD_KEEP_ALIVE` when `--no-shutdown=1`, persisting after chain completion. Watchdog gains a 1h TTL on the marker. Deployed and live on QA runner.

---

## Investigation

### Evidence gathered

| Source | Finding |
|--------|---------|
| `s3://opal-data-bd/gold/logs/from_C_01_20260421_180919.log` | CHAIN COMPLETE at 18:25:17Z. C_06 wall=475s, C_07 wall=13.9s, C_08 wall=63.3s. |
| `/var/log/watchdog-shutdown.log` (via SSM) | 18:20:23Z: SKIP (gold running). 18:25:54Z: SHUTDOWN (no gold process, uptime 42m, no keep-alive). |
| `gold_dispatch.sh` lines 864-867, 927-930 | Both shutdown sites gated by `NO_SHUTDOWN`. H4 ruled out. |
| CloudTrail | No `StopInstances` API call. Stop from inside instance. |
| `infra/aws/ec2/common/setup-autoshutdown-timer.sh` | `autoshutdown.timer` NOT installed on QA runner. Only `watchdog-shutdown.timer` present. |

### Hypothesis dispositions

| Hypothesis | Verdict |
|---|---|
| H1: pgrep regex missed C_06 workers | RULED OUT — chain was complete, no workers remained |
| H2: concurrent external shutdown | RULED OUT — SIGTERM was halt sequence the watchdog itself triggered |
| H3: prior cycle scheduled `+N` shutdown | RULED OUT — script uses `shutdown -h now` exclusively |
| H4: `--no-shutdown` not honored | RULED OUT — both shutdown sites confirmed gated |
| **True cause** | Chain completed at 18:25:17Z. Watchdog fired 37s later. `--no-shutdown` does not suppress the independent watchdog. |

### On Andrew's CPU threshold question

No CPU-based shutdown exists anywhere. Watchdog uses only: pgrep + uptime + file marker + S3 key. The 3.87% cpu_avg on C_06 in PERF logs is gold_prof.py observability output — not read by any shutdown logic.

---

## Changes

### `data/black_diamond/scripts/gold/gold_dispatch.sh`
After the `--bg` parent exits, when `NO_SHUTDOWN=1`: `touch /tmp/GOLD_KEEP_ALIVE`. Marker persists after chain completion. Does not run in the `--bg` parent (which exits before this block).

### `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh`
Check 3 (marker check) now enforces a 1h TTL via `stat -c %Y`. If marker age > 3600s, treated as stale — watchdog proceeds to shutdown decision. Prevents indefinite instance run if operator forgets to clean up.

---

## Deployment

| Step | Action | Result |
|------|--------|--------|
| Commit | `425c0fa2` (author: 0.7.0_AE_CloudOps) | 3 files: watchdog-shutdown.sh, gold_dispatch.sh, RCA doc |
| Push | `git push origin CLOUD` | OK — `64eee063..425c0fa2` |
| S3 upload | `aws s3 cp watchdog-shutdown.sh s3://opal-data-bd/code/runner/watchdog-shutdown.sh` | OK (2.4 KiB) |
| Hot-patch QA | SSM `570b4ca7` to i-0090b823a4a0997e3 | Success — `MAX_KEEP_ALIVE_AGE_SECONDS=3600` confirmed live |

**Pending:** DS to upload `gold_dispatch.sh` to `s3://opal-data-bd/code/gold/gold_dispatch.sh`. AE committed the fix; DS owns the S3 upload per ADHC_DSFLOW.

---

## Operator Workflow (Post-Fix)

```
dispatch --from C_01 --bg --no-shutdown   # stamps /tmp/GOLD_KEEP_ALIVE
  ... chain completes ...
  ... watchdog skips (sees marker) ...
dispatch --from D_00 --bg --no-shutdown   # refreshes marker mtime
  ... done for session:
rm /tmp/GOLD_KEEP_ALIVE                   # explicit release
  ... next watchdog cycle: shuts down cleanly ...
```

Failsafe: if marker is not removed, watchdog TTL (1h) expires it automatically.

---

## Telemetry Gap (Not Blocking)

gold_prof.py PERF lines give cpu_avg/mem_peak per script post-completion. No real-time CPU/mem stream during a run. A CloudWatch Agent config (60s CPU/mem metrics) would give live visibility and eliminate ambiguity for future incidents. Flagged as a separate hardening item — not root cause here.

---

## Related Files

- RCA: `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-04-21/RCA_20260421_watchdog_chain_complete_shutdown.md`
- Brief: `docs/briefs/watchdog-kill-during-active-gold-run-2026-04-21.md`
- Yesterday's RCA: `infra/aws/ec2/bd-gold-layer-runner/RCA_20260420_watchdog_shutdown.md`
- Watchdog (repo): `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh`
- Dispatch: `data/black_diamond/scripts/gold/gold_dispatch.sh`
