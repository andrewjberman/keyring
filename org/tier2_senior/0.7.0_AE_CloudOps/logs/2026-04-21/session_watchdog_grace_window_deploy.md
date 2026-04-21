# Session Log: 2026-04-21 — Watchdog Grace-Window Redesign Deploy

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-21
**Tasked by:** 0.6.0_AE_PartnerETL MCP (20260421T193002Z + correction 20260421T193741Z)
**Andrew directive:** 2026-04-21T19:26Z — "there should not be keep-alive, we should have the watchdog working effectively enough that we never need to do that."

---

## Summary

Received watchdog redesign spec from 0.6.0_AE on startup. Found that 0.6.0 had already committed the redesign (11478af7) while I was offline. Executed deployment: S3 upload + QA runner hot-patch. PROD is stopped; watchdog staged in S3 for next-start patch. Coordinated DS for gold_dispatch.sh S3 upload.

---

## Redesign: GOLD_KEEP_ALIVE -> Grace Window

**Supersedes:** commit `425c0fa2` (KEEP_ALIVE marker + 1h TTL)

**New design (11478af7):**
- `/var/lib/watchdog-last-gold` (EBS-persistent) stamped with epoch on every pgrep hit
- When pgrep misses: compare `now - last_sighting` against `GRACE_SECONDS=300`
- Under 5 min: SKIP. Over 5 min: fall through to existing shutdown logic
- No operator-facing marker. No TTL to remember. No watchdog coupling in gold_dispatch.sh

**Why 5 min:** matches the 5-min tick cadence (one extra tick of grace). Covers the 37s post-chain dispatch gap and the 3s inter-phase kill/redispatch scenario. Tight by design per Andrew's push-back on operator overrides.

**Fresh-boot edge case:** no timestamp file on first boot. Falls through to existing uptime-10m threshold on first tick (correct behavior).

---

## Deployment

| Step | Action | Result |
|------|--------|--------|
| S3 upload (watchdog) | `aws s3 cp watchdog-shutdown.sh s3://opal-data-bd/code/runner/watchdog-shutdown.sh` | OK 3.3 KiB |
| QA hot-patch | SSM `b471e92c` to i-0090b823a4a0997e3 | Success — PATCH_OK, GRACE_SECONDS=300 confirmed |
| PROD | i-01003b035d2988dfb stopped at time of deploy | S3 artifact updated; apply on next start |
| gold_dispatch.sh S3 | DS lane per ADHC_DSFLOW | MCP sent 20260421T203808Z to 0.4.0_DS |

---

## PROD Next-Start Patch

When PROD runner is started next, apply via SSM before any gold run:

```bash
aws ssm send-command \
  --instance-ids i-01003b035d2988dfb \
  --document-name AWS-RunShellScript \
  --parameters 'commands=["aws s3 cp s3://opal-data-bd/code/runner/watchdog-shutdown.sh /home/ubuntu/gold-layer/watchdog-shutdown.sh && chmod +x /home/ubuntu/gold-layer/watchdog-shutdown.sh && grep GRACE_SECONDS /home/ubuntu/gold-layer/watchdog-shutdown.sh"]'
```

Confirm `GRACE_SECONDS=300` in output.

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `comp-iam service bd-gold-layer-runner` | N/A — no new boto3 calls in this change | Not required |
| `comp-pipescript deployed gold_dispatch.sh` | N/A — pending DS S3 upload | DS to run after upload |

No IAM changes. No new S3/SSM boto3 calls in this change. IAM check not required.

---

## Related Files

- Redesign commit: `11478af7` (author: 0.6.0_AE_PartnerETL)
- Watchdog (repo): `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh`
- Dispatch (repo): `data/black_diamond/scripts/gold/gold_dispatch.sh`
- Brief (updated): `docs/briefs/watchdog-kill-during-active-gold-run-2026-04-21.md`
- Prior session (KEEP_ALIVE fix): `session_watchdog_rca_and_fix.md` (same folder)

---

## Next Steps

- [0.4.0_DS] Upload gold_dispatch.sh to s3://opal-data-bd/code/gold/ and confirm MATCH
- [0.7.0_AE] Apply PROD hot-patch on next runner start (before any gold run)
- [0.6.0_AE] RAVC COMPLETE pending DS confirmation
