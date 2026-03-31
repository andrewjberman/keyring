# ADVI_MVPLVL.010 — Gold Deploy Session Log

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-03-26
**Task Order:** ADVI_MVPLVL.010.ae-gold-rerun-06b-06.md
**Status:** PAUSED — S3 deploy complete, gold run not yet executed

---

## Completed

### Requirement 1: Verify DS commits on CLOUD
All 4 DS commits confirmed on CLOUD:
- `9bca5ff6` — mix_timeseries alias + script 06 ghost exclusion
- `38faa34f` — lib/exclusions.py + dedup scripts 05+06
- `df5e8004` — script 05b ghost exclusion
- `ae3403f5` — scripts 06b+12 ghost exclusion + shared insurance AP gate

### Requirement 2: S3 deploy
Synced gold scripts to `s3://opal-data-bd/code/gold/` via:
```
aws s3 sync data/black_diamond/scripts/gold/ s3://opal-data-bd/code/gold/ \
  --delete --exclude '*.parquet' --exclude 'archive/*' --exclude '*__pycache__*'
```

6 files uploaded:
- `lib/exclusions.py` (new)
- `05_build_client_performance.py`
- `05b_build_account_performance.py`
- `06_build_client_tax_liability.py`
- `06b_build_client_mix_timeseries.py`
- `12_build_composition_artifacts.py`

Verified `lib/exclusions.py` on S3: 7,396 bytes, uploaded 2026-03-26 12:36:05.

---

## Not Started

### Requirement 3: Full gold layer run
An SSM command was dispatched (`f8853376-abcf-4cba-a902-78a3101e5e7e`) but cancelled
before completion per user instruction. The EC2 runner (`i-01003b035d2988dfb`) may
have partially executed — check `/var/log/gold-full-run.log` or S3 logs before
re-running.

**IMPORTANT:** Must use `full` mode, not `incremental`. Script 05b only runs in full
mode and is the primary fix for the $7.4M Books-vs-Advisors AUA gap.

To resume:
```bash
aws ssm send-command --instance-ids "i-01003b035d2988dfb" \
  --document-name "AWS-RunShellScript" \
  --parameters 'commands=["cd /home/ubuntu/gold-layer/scripts && aws s3 sync s3://opal-data-bd/code/gold/ . && chmod +x *.sh *.py 2>/dev/null; ./run_gold_layer.sh full 2>&1 | tee /var/log/gold-full-run.log && aws s3 cp /var/log/gold-full-run.log s3://opal-data-bd/logs/gold-layer/gold_full_mvplvl010_$(date +%Y%m%d_%H%M%S).log"]' \
  --timeout-seconds 7200 \
  --comment "ADVI_MVPLVL-010 full gold rerun"
```

### Requirement 4: Post-run verification
Blocked on Req 3. After full run completes, verify:
- 4a: `aws s3 ls s3://opal-data-bd/gold/advisors/ --recursive | grep mix_timeseries.json` — expect 20 files
- 4b: Check log for ghost exclusion messages from scripts 05b, 06, 06b, 12
- 4c: `aws s3 ls s3://opal-data-bd/gold/account_performance.parquet` — timestamp should reflect new run
