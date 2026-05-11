# AE 0.7.0 Session Log — INFRUNNERPARITY Boot Dispatcher Bug Fix
**Date:** 2026-05-11
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** P0 message from COO (23:12Z) — fresh-spawn brief after context-drift kill

---

## Background (prior-self honest disclosure)

Prior session (session_infrunnerparity_close.md) claimed "Service installed and enabled OK" for the SSM install of `inf-gold-layer-runner.service`. That claim was correct — the SSM command succeeded and the service was enabled. However, the script that got installed had a latent bug that caused the chain to fail on first real-trigger execution. The prior RAVC did not include an empirical end-to-end test with the actual trigger Lambda; it accepted `systemctl is-enabled` as sufficient evidence.

This session corrects that gap.

---

## Bug Analysis

### Empirical trace from EC2 console (22:38Z, AE 0.6.1 forensic):

```
[22:38:04+00:00] Boot Dispatcher starting
[22:38:20+00:00] Trigger mode marker: mode=full snapshot_date=2026-05-11
[22:38:20+00:00] Chain mode: full
[22:38:20+00:00] Pulling dispatch script from s3://opal-data-inf/code/gold/orion-gold-dispatch.sh...
download: s3://.../orion-gold-dispatch.sh to tmp/orion-gold-dispatch.sh    <- DOWNLOAD SUCCEEDED
[22:38:21+00:00] ERROR: failed to pull orion-gold-dispatch.sh from S3      <- FALSE FAILURE
[22:38:21+00:00] Shutting down (dispatch unavailable)
```

### Root cause: two bugs, one critical

**Bug 1 (CRITICAL) — Line 84, pipefail + tee exit poisoning:**

Original code:
```bash
if ! aws s3 cp "$DISPATCH_S3" "$DISPATCH_LOCAL" 2>&1 | tee -a "$LOG_FILE"; then
```

With `set -o pipefail` active, the pipe exit code is the rightmost non-zero. `aws s3 cp` succeeded (exit 0). `tee -a "$LOG_FILE"` failed (exit 1: Permission denied on /var/log/inf-gold/). Pipe exit = 1. `! 1` = true → error block entered, script shut down. The file WAS downloaded to /tmp/orion-gold-dispatch.sh but the check false-failed.

**Bug 2 (CAUSE of Bug 1) — LOGDIR not writable by ec2-user:**

```
LOGDIR="/var/log/inf-gold"
```

Service runs as `User=ec2-user` (confirmed in inf-gold-layer-runner.service line 8). `/var/log/` is root-owned 755; ec2-user cannot create `/var/log/inf-gold/`. All `tee -a "$LOG_FILE"` calls → Permission denied. Non-critical for log() calls (tee still outputs to stdout/journal; script continues). CRITICAL for line 84 because that call is in an if condition.

### Non-critical related issue:

**EXIT_CODE=$?** after a piped command also captured the pipe exit (max non-zero from tee), not bash's exit code. Fixed to `PIPESTATUS[0]` for accuracy, though non-blocking since EXIT_CODE was only used for logging.

---

## Fix Applied

| Change | File | Description |
|--------|------|-------------|
| LOGDIR /var/log/inf-gold → /tmp/inf-gold | run-gold-layer.sh:28 | /tmp always writable by ec2-user; eliminates tee Permission denied |
| Line 84: if ! cmd | tee → cmd | tee + PIPESTATUS[0] | run-gold-layer.sh:84-91 | Decouples tee exit from aws s3 cp exit check; root-cause fix |
| EXIT_CODE: $? → PIPESTATUS[0] | run-gold-layer.sh:105 | Attribution accuracy for dispatch exit code |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | bash -n syntax check | PASS |
| 2 | safe-commit.sh --author 0.7.0_AE_CloudOps | commit 6a916cccb |
| 3 | git push origin CLOUD | 4d7d0875b..6a916cccb |
| 4 | aws s3 cp run-gold-layer.sh s3://opal-data-inf/code/runner/ | UPLOAD OK |
| 5 | SHA256 verify (repo vs S3) | 783fdf4cf6ace7e5667348098a0db08e5880a1513523b75eb155a1002c3bb980 MATCH |

**Re-install path:** NO MANUAL INSTALL NEEDED. The systemd service has:
```
ExecStartPre=/bin/bash -c "aws s3 cp s3://opal-data-inf/code/runner/run-gold-layer.sh /home/ec2-user/run-gold-layer.sh && chmod +x ..."
```
On next EC2 start (triggered by inf-gold-trigger Lambda), ExecStartPre auto-fetches the fixed script from S3. Script also self-updates from S3 in first run block. Three-layer pull redundancy.

**SSM state:** DescribeInstanceInformation empty (unmanaged). Non-blocking — ExecStartPre works regardless of SSM registration.

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| Syntax check | bash -n run-gold-layer.sh | PASS |
| SHA verify | sha256sum repo + S3 pull-verify | 783fdf4c... MATCH |
| comp-iam | not run (no IAM changes in this fix) | N/A |
| comp-blast | not run (script-level fix only; no infra graph changes) | N/A |

---

## RAVC Trail

| RAVC | Direction | Time (UTC) | Content |
|------|-----------|------------|---------|
| P0 brief received | COO → AE 0.7 | 23:12Z | Boot dispatcher bug; empirical trace; GO scope |
| RAVC1 ACK | AE 0.7 → COO | ~23:18Z | Diagnosis confirmed; PIPESTATUS[0] + LOGDIR fix plan |
| COO GO ACK | COO → AE 0.7 | ~23:19Z | "Diagnosis is sharp; GO on fix" |
| RAVC2 (full evidence) | AE 0.7 → COO | ~23:21Z | Commit 6a916cccb + S3 SHA MATCH + re-install path |

---

## Pending (this session)

- Await RAVC2 ACK from COO
- Await AE 0.6.1 forensic package (requested via MCP)
- Item 1 chain retry: AE 0.6.1 re-invokes inf-gold-trigger Lambda → on boot ExecStartPre fetches fixed script → chain runs clean → platinum artifacts refresh
- If chain exits 0 and DS~A parity_check_group_d.py exits 0: close INFRUNNERPARITY permanently

---

## Empirical Validation Result (23:39Z)

AE 0.6.1 RAVC2 confirmed fix works in PROD:

- Boot trace: NO "ERROR: failed to pull" / "Shutting down" lines
- Chain reached: "CHAIN: chain:full started" → "Synced 127 files to /tmp/orion_gold_scripts"
- /tmp/inf-gold/ logdir: runner log wrote cleanly, uploaded to gold/logs/runner_20260511_233646.log (11.3 KiB)
- AC6 (stop/start via ExecStartPre pull): CONFIRMED — ExecStartPre fetched fixed script from S3 on boot

**Downstream failure at INF_API_SILVER_REPS** (NOT in boot dispatcher scope):
```
Bronze JSON not found at data/orion/manual_api/pulls/2026-05-11_representatives.json
```
EC2 runner missing `INF_PREFER_S3=true` env var (Lambda sets it; EC2 dispatcher doesn't).
Bronze landed in S3 fine (`bronze/orion-api-v2/2026-05-11/representatives.json` 23:36:44Z).
AE 0.6.1 escalated to COO with Option A (add to run-gold-layer.sh) / Option B (add to orion-gold-dispatch.sh).
If Option A routed to AE 0.7: ready to ship same-session.

## Session Status: COMPLETE — boot dispatcher fix empirically validated 23:39Z 2026-05-11
