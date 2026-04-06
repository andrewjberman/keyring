# Gold Rebuild, Silver Transaction Fix, Pipeline Audit -- 0.6.0_AE_PartnerETL

**Date:** 2026-04-02
**Start Time:** 4:30 PM ET (resumed from 4/1 session)
**End Time:** ongoing
**Project:** ADHC_HISTRY / GLDRST

---

## Objective

Continue Phase 1/Phase 2 gold rebuild from 4/1 session (asset mix fix in script 03),
diagnose why portal was stuck on 2026-03-27, and fix the silver transaction pipeline.

---

## Work Completed

### 1. Phase 1 Incremental Rebuild -- COMPLETE

SSM `fddfa10e` on bd-gold-layer-runner (i-01003b035d2988dfb, c6i.16xlarge).
Incremental rebuild from --start-date 2020-01-01 to fix 1900-date portal display.
Instance auto-stopped on completion. positions_cube partitions written through 2026-03-27.

CloudFront invalidated on both portal distributions (E2LPCXXBLDGWXY, EVTSA9VEHNZVH).

### 2. Phase 2 Full Rebuild -- FAILED (SSM timeout)

**First attempt** (SSM `1867da81`): Used wrong entry point (`python3 gold_runner.py`).
Script doesn't exist -- correct entry is `./run_gold_layer.sh full`. Failed immediately.

**Second attempt** (SSM `a3202859`): Correct entry point. Ran through scripts 00, 01, 02, 04
then hit **SyntaxError in script 03** at line 414. Root cause: DS commit 5800ae2a had a
broken docstring -- two `"""` blocks left descriptive text outside the string literal.
The line `Sell gaps (FIFO > RPS) are handled by the positions cube (script 02) and`
was parsed as Python code; `02` triggered "leading zeros in decimal integer literals".

**Fix:** Merged the two docstring blocks into one. Re-uploaded to S3. Syntax-checked locally.

**Third attempt** (SSM `c9e9f007`): Fixed script 03 uploaded. Full rebuild launched.
**Timed out after exactly 2 hours** (SSM executionTimeout: 7200s). The `tee` pipe pattern
(`./run_gold_layer.sh full 2>&1 | tee /tmp/gold_runner.log`) meant SSM killed the process
tree before `run_gold_layer.sh` reached its `shutdown -h now` at the bottom. Instance was
left running idle for 15+ hours.

Script 03 DID complete and wrote holdings_lots (32.8 MiB vs 35.4 MiB -- consistent with
phantom lot closures). But downstream scripts (05+) were killed.

### 3. Portal Stuck on March 27 -- Root Cause Found

Andrew reported portal still showing 2026-03-27 data despite multiple rebuilds.

**Investigation:** All four BD feeds have bronze data through 2026-03-31:
- Transactions: `TXN_DAILY_2026-03-31.xlsx` (43 MB) -- uploaded Apr 1 5:44 PM
- Allocations: `ALLOC_DAILY_2026-03-31.xlsx` (12 MB) -- uploaded Apr 1 5:50 PM
- Realized: `REALIZED_DAILY_2026-03-31.xlsx` (39 KB) -- uploaded Apr 1 5:34 PM
- Unrealized: `UNREALIZED_DAILY_2026-03-31.xlsx` (26 MB) -- uploaded Apr 1 5:28 PM

**But silver/transactions stopped at 2026-03-26.** Allocations, realized, unrealized all
converted to silver through 3/31. Only transactions broke.

**Root cause:** `merge-daily-incremental.py` (the bronze-to-silver converter for transactions)
was updated to import `from lib.config import S3_BUCKET`. The `lib/` package only exists in
the gold layer scripts on the gold runner instance (i-01003b035d2988dfb). The download
instance (i-00c7568bc510f7423) at `/opt/bd-exporter/` has no `lib/` directory.

The download script itself (`download-daily-transaction.ts`) completed fine every day --
xlsx files uploaded to S3 successfully. But `merge-daily-incremental.py` crashed with
`ModuleNotFoundError: No module named 'lib'` on every run since 3/30.

The `python3 -c` inline analysis step in the download TypeScript has a separate bug
(SyntaxError from escaped newlines) but that's non-blocking -- it only affects the
date analysis diagnostic, not the actual download or upload.

### 4. Silver Transaction Fix -- COMPLETE

**Fix:** Replaced `from lib.config import S3_BUCKET` with inline:
```python
S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-bd')
```
Added `import os` to the imports. Uploaded fixed script to `s3://opal-data-bd/scripts/`.

Ran the converter on the download instance (i-00c7568bc510f7423). Result:
- `TXN_DAILY_2026-03-27.xlsx` -> `silver/transactions/2026-03-27.parquet` (42,912 rows)
- `TXN_DAILY_2026-03-30.xlsx` -> `silver/transactions/2026-03-30.parquet` (5,624 rows)
- `TXN_DAILY_2026-03-31.xlsx` -> `silver/transactions/2026-03-31.parquet` (160,394 rows)

Silver transactions now current through 2026-03-31.

### 5. Phase 2 Full Rebuild (retry) -- IN PROGRESS

Launched with `nohup` to detach from SSM session (avoids 2-hour timeout kill):
```
nohup ./run_gold_layer.sh full > /tmp/gold_runner.log 2>&1 &
```
PID 39671 on bd-gold-layer-runner. Confirmed new data ingested: 1,762 transaction files
(was 1,759), 2,832,113 rows (was 2,791,225). `run_gold_layer.sh` handles
pipeline-complete.json, CloudFront invalidation, and `shutdown -h now` at completion.

---

## Discoveries / Bugs Found

### Bug 1: Script 03 broken docstring (DS commit 5800ae2a)
- Two `"""` blocks left code outside the string literal
- Fixed locally, re-uploaded to S3
- DS should be notified to avoid this pattern

### Bug 2: merge-daily-incremental.py lib import (broke silver transactions 3/30-3/31)
- Someone added `from lib.config import S3_BUCKET` to a script that runs on a different instance
- `lib/` only exists in gold layer scripts directory
- Fixed with inline constant
- Broader lesson: scripts that run on different instances must be self-contained

### Bug 3: SSM timeout kills long-running gold rebuilds
- `executionTimeout: 7200` (2 hours) is not enough for full rebuilds
- The `tee` pipe pattern means SSM kills the entire process tree
- `nohup` pattern works as a workaround but is fragile
- Needs a permanent fix in `run_gold_layer.sh` or the trigger Lambda

### Bug 4: Inline python3 -c SyntaxError in download TypeScript
- `download-daily-transaction.ts` shells out `python3 -c "\nimport pandas..."
- The `\n` escapes aren't interpreted, causing SyntaxError
- Non-blocking (only affects date analysis diagnostic) but should be fixed

### Discovery: bd-gold-layer-runner is c6i.16xlarge
- Memory note previously said c5.4xlarge+ -- corrected to c6i.16xlarge
- 64 vCPUs / 128 GB RAM -- correct sizing for 306k pair expansion with 60 workers

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Inline S3_BUCKET in merge-daily-incremental.py | Script runs on download instance without lib/ package; shared lib makes sense for gold scripts on the same machine, not for cross-instance scripts |
| Use nohup for full rebuild | SSM 2-hour timeout kills tee pipe; nohup detaches process from SSM session |
| Run silver conversion on download instance | That's where the existing Python environment and openpyxl are installed |

---

## Files Modified

| File | Change | Location |
|---|---|---|
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Fixed broken docstring (merged two `"""` blocks) | Local + S3 |
| `merge-daily-incremental.py` | Replaced `from lib.config import S3_BUCKET` with inline `os.environ.get` | S3 only (`s3://opal-data-bd/scripts/`) |

---

## Current State

**Status:** IN PROGRESS
**Active branch:** CLOUD

Full gold rebuild running detached (nohup, PID 39671) on bd-gold-layer-runner (c6i.16xlarge).
Script 02 confirmed processing 1,762 transaction files (including 3/27, 3/30, 3/31).
Silver transactions current through 2026-03-31. Download instance (i-00c7568bc510f7423)
shut down after silver backfill. When rebuild completes, `run_gold_layer.sh` will write
`pipeline-complete.json`, invalidate CloudFront, and self-stop the instance.

Expected results after completion:
- Portal global_end_date advances from 2026-03-27 to 2026-03-31
- holdings_lots MV drops from ~$2.03B to ~$1.58B (script 03 asset mix fix)
- Asset mix categories sum to approximately total AUA

---

## Next Steps

### Immediate (after rebuild completes)
1. **Verify gold rebuild output** -- check holdings_lots total MV ~ $1.58B, confirm
   global_end_date is 2026-03-31, verify instance self-stopped
2. **Validate portal** -- confirm Books tab Firm Overview asset mix no longer overstated

### Autoshutdown reliability fix
3. **Fix run_gold_layer.sh SSM interaction** -- the `tee` pipe pattern is the root problem.
   Options:
   - (a) Change trigger Lambda to use `nohup` + detach pattern instead of inline execution
   - (b) Modify `run_gold_layer.sh` to trap SIGTERM and still run shutdown
   - (c) Add a systemd service or cron watchdog that shuts down if no gold process running
   - (d) Increase SSM timeout to 4+ hours (simplest but masks the problem)
   Recommendation: (a) -- the trigger Lambda should always launch with nohup

### RPS data pipeline from Schwab
4. **Scope the Schwab RPS ingestion pipeline** -- currently RPS data is manually converted
   and uploaded. Need automated daily flow: Schwab SFTP/API -> S3 bronze/rps/ -> silver
   conversion -> gold scripts pick up automatically. This was part of ADHC_HISTRY.005/.006
   design (bronze/rps/ prefix, converter reads bronze/rps/ first).
5. **Determine Schwab delivery mechanism** -- is it SFTP, API, or manual download?
   Andrew needs to clarify the vendor interface.

### GLDRST remainder
6. **Audit remaining GLDRST scope** -- read `org/projects/ADVI_GLDRST.json` and related
   task orders to identify what's left
7. **Integrate all above work items into GLDRST project** -- the silver fix, autoshutdown,
   RPS pipeline, and NNA/market growth rearchitecture (approved but not implemented per
   DS session log) should all be tracked under GLDRST

**Do NOT:**
- Trust portal asset mix numbers until full rebuild confirms holdings_lots MV ~ $1.58B
- Add `lib/` to the download instance -- scripts there must remain self-contained
- Run gold rebuilds via SSM without nohup until the trigger Lambda is fixed
