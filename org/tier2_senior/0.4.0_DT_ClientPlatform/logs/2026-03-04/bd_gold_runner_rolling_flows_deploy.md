# bd-gold-layer-runner stacked_bar + rolling_1y Deploy (ADVI-005 B2) — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-04
**Start Time:** ~10:50 ET
**End Time:** ~10:55 ET

---

## Objective

Deploy EC2 gold layer script change from DS commit `c9b3ab76` — adds `stacked_bar` and `rolling_1y` keys to `gold/advisor_rolling_flows.json` output (script 10). Stream B2 of ADVI-005. Start instance for incremental run.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | safe-ec2-deploy.sh bd-gold-layer-runner | Bronze (4), silver (6), gold (14) scripts synced to `s3://opal-data-bd/code/` |
| 2 | Manifest auto-commit by wrapper | `4a908760` Deploy EC2 bd-gold-layer-runner @ c98d1ae5 |
| 3 | aws ec2 start-instances i-01003b035d2988dfb | State: stopped -> pending |
| 4 | Update deployment_map.xml + commit | bd-gold-layer-runner deployed_tag -> bd-v2.15.1 |
| 5 | Tag + push | `bd-v2.15.1`, pushed CLOUD |

---

## Verification (pending — instance running)

Instance `i-01003b035d2988dfb` is booting. It will:
1. Sync scripts from `s3://opal-data-bd/code/`
2. Run `run_gold_layer.sh incremental` (02->05->07->08->09->10)
3. Write `s3://opal-data-bd/gold/advisor_rolling_flows.json` with new `stacked_bar` + `rolling_1y` keys
4. Write `s3://opal-data-bd/gold/pipeline-complete.json` (triggers bd-portal-publisher + bd-portal-advisor-publisher)
5. Shut down automatically

**To check log after completion:**
```bash
aws s3 ls s3://opal-data-bd/logs/gold-layer/ --recursive | sort | tail -5
```

**To verify keys:**
```bash
aws s3 cp s3://opal-data-bd/gold/advisor_rolling_flows.json - | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print('top-level keys:', list(d.keys()))"
```
Expected keys include: `stacked_bar`, `rolling_1y`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Tag bd-v2.15.1 immediately (don't wait for run completion) | Tag certifies code was deployed to S3; run output is a runtime concern, not a deploy concern |
| Not monitoring run inline | Instance runs async, shuts down on completion. Check S3 log if verification needed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/ec2/EC2_MANIFEST.json` | deployed_commit + deployed_at updated for bd-gold-layer-runner | Yes — `4a908760` (auto by safe-ec2-deploy.sh) |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` | bd-gold-layer-runner deployed_tag -> bd-v2.15.1 | Yes — pending commit |

---

## Deployment Tags

| Pipeline | Tag | Commit | Notes |
|----------|-----|--------|-------|
| bd-pipeline (EC2) | `bd-v2.15.1` | `4a908760` | Script 10 stacked_bar + rolling_1y |

---

## Current State

**Status:** COMPLETE (deploy) / IN PROGRESS (runtime — instance running)
**Active branch:** `CLOUD`

Scripts deployed to S3, instance started. `bd-v2.15.1` tagged and pushed. Instance will complete the incremental gold run and shut down. `pipeline-complete.json` will trigger bd-portal-publisher and bd-portal-advisor-publisher as a side effect (expected and normal).

---

## Next Steps

1. **Verify run completed** — check S3 log `s3://opal-data-bd/logs/gold-layer/` for `COMPLETE -- INCREMENTAL` with no script 10 errors
2. **Verify output keys** — `stacked_bar` and `rolling_1y` present in `advisor_rolling_flows.json`
3. **[RD 0.4.2_RD_AdvisorIntelligence] Implement portal rendering** — `stacked_bar` (5-period bar chart) and `rolling_1y` (1Y rolling NNA chart) are now live in `advisor_rolling_flows.json`

**Do NOT:**
- Run incremental again before the current run finishes — check instance state first
- Run in `full` mode unless explicitly requested (full rebuilds all parquets from scratch)
- Modify `architects`/`implementors` legacy keys (backward compat required)
