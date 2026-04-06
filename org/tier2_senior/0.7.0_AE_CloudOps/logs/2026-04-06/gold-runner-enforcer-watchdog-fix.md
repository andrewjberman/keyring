# Gold Runner Enforcer Coverage + Watchdog Hardening

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-06
**Status:** COMPLETE
**Trigger:** CTO escalation -- bd-gold-layer-runner idle 4 days on c6i.16xlarge

---

## Incident Summary

Instance i-01003b035d2988dfb (bd-gold-layer-runner, c6i.16xlarge) ran idle from 2026-04-02 17:52 ET to 2026-04-06 07:41 ET (~84 hours). Estimated wasted cost: ~$228.

- bd-gold-trigger Lambda started the instance on April 2
- Gold process (PID 39671) died at some point
- Neither the watchdog timer nor the enforcer Lambda stopped the instance
- Instance was manually stopped at 07:41 ET on April 6

## Root Cause

**Enforcer gap:** Instance had `AutoShutdown=disabled` tag. The enforcer Lambda (lambda_function.py:116) skips any instance with this tag. Tag was set intentionally because gold runner has self-shutdown mechanisms, but it eliminated the enforcer as a backstop.

**Watchdog failure (probable):** Check 4 in watchdog-shutdown.sh calls `aws s3 cp` to check for trigger-pending.json with no timeout. If the AWS CLI hung (IMDSv2 token expiry, IAM session issue), the oneshot systemd service blocks indefinitely, preventing the timer from firing again. Secondary possibility: the broad `pgrep -f "python3"` matched a stray process.

## Fixes Applied

### Fix 1: Enforcer Coverage

- Removed `AutoShutdown=disabled` tag from i-01003b035d2988dfb
- Enforcer now covers gold runner (MAX_RUNTIME_HOURS=4.0, runs every 15 min)
- Command: `aws ec2 delete-tags --resources i-01003b035d2988dfb --tags Key=AutoShutdown`
- Verified: tag no longer present

### Fix 2: Watchdog Hardening (watchdog-shutdown.sh)

| Change | Before | After |
|--------|--------|-------|
| S3 check | `aws s3 cp ...` (no timeout) | `timeout 10 aws s3 cp ...` |
| Process grep | `pgrep -f "python3"` (too broad) | `pgrep -f "run_gold_layer\|gold_rebuild\|build_gold"` |
| Redundant check | Separate `pgrep -f "run_gold_layer.sh"` | Removed (subsumed by new pattern) |

- Uploaded to s3://opal-data-bd/code/runner/watchdog-shutdown.sh
- EC2 pulls on next boot via setup-instance.sh

## Defense Layers (Post-Fix)

| Layer | Mechanism | Frequency |
|-------|-----------|-----------|
| Primary | run_gold_layer.sh `shutdown -h now` at end of script | On completion |
| Secondary | watchdog-shutdown.timer (hardened) | Every 5 min |
| Backstop | ec2-auto-shutdown-enforcer Lambda (now covers gold runner) | Every 15 min, 4hr limit |

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh` | timeout + narrowed grep |

## AWS Changes

| Resource | Change |
|----------|--------|
| i-01003b035d2988dfb tags | Removed `AutoShutdown=disabled` |
| s3://opal-data-bd/code/runner/watchdog-shutdown.sh | Updated with hardened script |
