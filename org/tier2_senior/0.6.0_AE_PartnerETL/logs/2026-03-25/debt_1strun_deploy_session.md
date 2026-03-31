# DEBT_1STRUN -- DE Fixes Deploy Session -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-25
**Task:** Deploy DS/DE code cleanup (centralized config imports) to EC2/S3
**Status:** COMPLETE

---

## Context

DS completed DEBT_1STRUN code cleanup: 14 gold scripts, 6 silver scripts, and 2 shell
scripts refactored to import `S3_BUCKET` from `lib.config` instead of hardcoding
`opal-data-bd`. New shared libraries:
- `gold/lib/config.py` -- `S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-bd')`
- `silver/lib/config.py` -- same pattern
- `silver/lib/ticker_overrides.py` -- OPAL_ETF_OVERRIDES + TICKER_CORRECTIONS dicts

All changes behavior-preserving. Risk: `ModuleNotFoundError` if `lib/` dirs missing on EC2.

---

## Findings on Instance Inspection

### 1. Zombie Process Stacking (42 processes)

Instance `i-01003b035d2988dfb` launched 2026-03-24 19:08 UTC. On inspection found
**42 stacked `run_gold_layer.sh incremental` processes** spanning from boot to present.

Root cause: `/tmp/run-gold-layer-new.sh` (PID 431, the systemd boot spawner) was
repeatedly launching new `run_gold_layer.sh` invocations every ~31 minutes. Earlier
invocations never exited cleanly, so processes accumulated. Only the latest invocation
had an active python child; the rest were sleeping zombies.

This was a one-time issue from the 2026-03-24 boot, not a chronic problem.

### 2. lib/config.py Not on S3

Instance `/tmp/gold_layer_scripts/lib/` only contained `__init__.py` and
`etf_classifier.py`. No `config.py` -- the DE fixes had not been deployed yet.
Scripts running on EC2 were still using old hardcoded values.

### 3. S3 Gold Layer Logs Stale Since Feb 20

`s3://opal-data-bd/logs/gold-layer/` last entry: `run_20260220_150505.log`.
This is a deprecated log location. Current runner writes to `/tmp/gold_runner.log`
and `/var/log/gold-layer-runner.log`. The S3 log upload at end-of-script (line 187
of `run_gold_layer.sh`) only fires on clean completion. Not investigated further --
daily runs have been completing via the current runner path.

---

## Actions Taken

### Step 1: Kill All Processes

- Killed all 42 `run_gold_layer.sh` zombie processes
- Killed parent spawner `/tmp/run-gold-layer-new.sh` (PID 431)
- Killed orphan python children
- Verified instance clean (0 gold-related processes)

### Step 2: Deploy Gold Scripts to S3

```
aws s3 sync data/black_diamond/scripts/gold/ s3://opal-data-bd/code/gold/ \
    --delete --exclude '*.parquet' --exclude 'archive/*' --exclude '__pycache__/*'
```

Uploaded 18 .py scripts + `lib/` directory (config.py, helpers.py, nna_flows.py,
etf_classifier.py, __init__.py). `--delete` cleaned up stale `run_all.sh`.

### Step 3: Deploy Silver Scripts to S3

```
aws s3 sync data/black_diamond/scripts/silver/ s3://opal-data-bd/code/silver/ \
    --delete --exclude '*.parquet' --exclude '__pycache__/*'
```

Uploaded 8 .py scripts + `lib/` directory (config.py, ticker_overrides.py, __init__.py).

### Step 4: Verify S3

Confirmed on S3:
- `code/gold/lib/config.py` -- present (268 bytes)
- `code/gold/lib/helpers.py` -- present (1,279 bytes)
- `code/gold/lib/nna_flows.py` -- present (9,047 bytes)
- `code/silver/lib/config.py` -- present (136 bytes)
- `code/silver/lib/ticker_overrides.py` -- present (8,176 bytes)
- `code/silver/lib/__init__.py` -- present
- 18 gold .py scripts, 8 silver .py scripts

### Step 5: Trigger Fresh Gold Run

Triggered `run_gold_layer.sh incremental` via SSM. Run confirmed:
- Scripts synced from S3 (18 .py files, lib/config.py on disk)
- Pipeline progressed through 00 -> 02 -> 05 -> 05c -> 06b -> 07 -> 08b -> 08 -> 09 -> 10 -> 12
- No `ModuleNotFoundError` -- all `lib.config` imports resolved correctly
- **Pipeline completed successfully at 18:03:37 UTC**
- Sentinel written: `s3://opal-data-bd/gold/pipeline-complete.json`

### Step 6: Kill Redundant Re-run

After completion, the script detected a pending trigger marker from 2026-03-24 23:00 UTC
and re-exec'd. This second run was redundant (8-day lookback already covered that date).
Killed the re-run and cleared `s3://opal-data-bd/gold/trigger-pending.json`.

---

## Verification

| Check | Result |
|-------|--------|
| lib/config.py on S3 (gold) | PASS |
| lib/config.py on S3 (silver) | PASS |
| lib/ticker_overrides.py on S3 | PASS |
| Gold run import resolution | PASS (no ModuleNotFoundError) |
| Pipeline end-to-end completion | PASS (sentinel at 18:03:37 UTC) |
| Instance clean after session | PASS (0 gold processes) |

---

## Open Items

- **Pending trigger stacking:** The `run-gold-layer-new.sh` spawner at
  `s3://opal-data-bd/code/runner/run-gold-layer.sh` does not use a lockfile.
  If the systemd unit restarts it or SSM fires while a run is active, processes
  stack. Yesterday's 42-zombie incident was from this. Needs a PID lockfile or
  systemd `Type=oneshot` guard. One-time issue, not blocking.
- **EC2_MANIFEST.json:** `deployed_commit` is `8d0546634d` (2026-03-18). Should
  be updated to reflect this deploy. Deferring -- no code was deployed via
  `safe-ec2-deploy.sh`, only S3 sync.
