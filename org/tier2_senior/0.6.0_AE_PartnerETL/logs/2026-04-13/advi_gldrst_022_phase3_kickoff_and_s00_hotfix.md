# 0.6.0_AE Log: ADVI_GLDRST.022 Phase 3 Kickoff + S_00 Production Hotfix
**Date:** 2026-04-13
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** No new Terraform deploy this session -- infra-only change via S3 upload
**Related:** ADVI_GLDRST.022, Monday Runbook, advi_gldrst_022_phase1_canonical_prices_daily_eventbridge.md

## Session Summary

Startup orientation revealed a critical production bug in gold_dispatch.sh: `S_00`
(`build_canonical_prices_v2.py`) has been silently failing on every gold run since
bd-v2.22.0 was deployed on 2026-04-10. Hotfix applied and pushed before writing Phase 3 diff
infrastructure. ADVI_OFFICE.W2 remains blocked on DS W1 GO signal.

---

## Phase 3 Startup Checks (Monday Runbook Step 1-2)

### Bucket versioning
```
$ aws s3api get-bucket-versioning --bucket opal-data-bd
{"Status": "Enabled"}
```
**Option A confirmed.** S3 versioning is enabled on opal-data-bd. Post-run snapshot
retrieval is the canonical strategy -- no live SSM interception required.

### Gold logs since Friday deployment
| Log key | S3 LastModified (ET) | Interpretation |
|---|---|---|
| `gold_incremental_2026-04-11_20260411_000742.log` | 2026-04-10 20:07 ET | Friday 22:00 UTC bd-canonical-prices-daily first fire |
| `gold_incremental_2026-04-11_20260411_230540.log` | 2026-04-11 19:05 ET | Saturday 23:05 UTC nightly-fallback |
| `gold_incremental_2026-04-12_20260412_230542.log` | 2026-04-12 19:05 ET | Sunday 22:05 UTC bd-canonical-prices-daily (Sunday) |
| `gold_incremental_2026-04-13_20260413_155925.log` | 2026-04-13 11:59 ET | Monday morning run (manual/pending marker?) |

### canonical_prices.parquet version history
```
$ aws s3api list-object-versions --bucket opal-data-bd \
    --prefix silver/prices/canonical_prices.parquet \
    --query 'Versions[?LastModified>=`2026-04-10`].[LastModified,VersionId,IsLatest]'
2026-04-10T13:55:23.000Z  jsJzwojHEgHJ3jhFsBhb9cHGxV8Kj83D  False  (Phase 1 test)
2026-04-10T22:04:20.000Z  swRfiuMKs4dq4NBGMBi55aFCxl7q_JyY  True   (bd-price-update Job 1)
```

**Critical finding:** No new versions of canonical_prices.parquet after 2026-04-10 22:04 UTC.
Despite 4+ gold runs on the weekend and this morning, v2 has not written canonical_prices.

---

## Root Cause Investigation

Examined the cumulative gold runner log (`gold_incremental_2026-04-13.log`, 17.6 MB).
Log is cumulative (appended across all runs) with frozen internal clock (`2026-01-15`).
Searched for S_00 section in the April 13 run (tail of log):

```
=== Silver prep (pre-gate, 2026-04-13T14:54:07Z) ===
  Rebuilding silver/prices/canonical_prices.parquet before freshness gate.
================================================================
  CHAIN: silver-prep-pre
  Started: 2026-04-13T14:54:07Z
  Scripts: S_00
================================================================
Syncing scripts from s3://opal-data-bd/code/gold/ ...
Synced: 53 scripts

========================================
  S_00  (build_canonical_prices_v2.py)
  2026-04-13T14:54:09Z
  flags: --upload
========================================
usage: build_canonical_prices_v2.py [-h] [--dry-run] [--skip-inject]
build_canonical_prices_v2.py: error: unrecognized arguments: --upload
```

**Root cause:** `gold_dispatch.sh` CATALOG entry was `S_00|build_canonical_prices_v2.py|--upload`.
`build_canonical_prices_v2.py` does not accept `--upload` (its args are `--dry-run` and
`--skip-inject`). Script exits non-zero on every invocation.

**Why it was silent:** The silver-prep call is `run_chain "silver-prep-pre" ... | tee -a "$log_file"`.
Without `set -o pipefail`, the pipe exit code is `tee`'s (always 0), not `run_chain`'s.
`set -e` never fires. Chain continues to the freshness gate and full A/B/C/D run. 25 failures.

**Scope of damage:** v2 has NEVER run in production since Phase 1 deployment on 2026-04-10.
`canonical_prices.parquet` is not being updated by v2. The April 10 22:04 UTC version is from
`bd-price-update Job 1`, NOT from v2. The April 10 13:55 UTC version was from Phase 1 DS testing.

---

## Hotfix Applied

**Change:** Remove `--upload` from S_00 CATALOG entry in `gold_dispatch.sh`.

Before: `S_00|build_canonical_prices_v2.py|--upload`
After: `S_00|build_canonical_prices_v2.py|`

`build_canonical_prices_v2.py` uploads to S3 by default (no explicit flag needed --
consistent with convention for standalone silver scripts that were designed to run
with their own argument parser).

**Deployment:**
```
aws s3 cp data/black_diamond/scripts/gold/gold_dispatch.sh \
    s3://opal-data-bd/code/gold/gold_dispatch.sh
# Upload: OK

git add data/black_diamond/scripts/gold/gold_dispatch.sh
git commit --author="0.6.0_AE_PartnerETL <0.6.0_AE_PartnerETL@opal.agent>" \
    -m "fix(gold_dispatch): remove --upload from S_00 CATALOG entry (ADVI_GLDRST.022 hotfix)"
# Commit: 2a6136e4

git push origin CLOUD
# Pushed: b2e4e668..2a6136e4
```

The fix is live on S3 immediately. Next gold run (tonight 22:00 UTC) will pick up the
corrected gold_dispatch.sh and S_00 will run for the first time in production.

---

## Phase 3 Infrastructure Built

### Diff script
Written at `data/analysis/phase3_v2_vs_job1_diff.py`. Supports:
- `--fetch 2026-04-13`: download both S3 versions (Job 1 + v2) to `phase3_diff_snapshots/`
- `--fetch-only 2026-04-13`: download only, no diff
- `2026-04-13`: diff pre-fetched snapshots

Stop-ship signals, expected signals, and S3 version selection logic all per the runbook spec.

### Snapshot directory
`data/analysis/phase3_diff_snapshots/` will hold per-day `_job1.parquet` and `_v2.parquet` files.

---

## Phase 3 Protocol Adjustment

Because S_00 was failing since April 10, the parallel-run window starts tonight:
- **Day 1: 2026-04-13** -- tonight at 22:00 UTC (6 PM ET) is the first CLEAN Phase 3 fire
- **Day 5: 2026-04-17** -- last day of 5-day validation window (pushed back by 3 weekend days)

The original Day 1 was 2026-04-13 and 5-day window ends 2026-04-17. This is unchanged -- the
hotfix means tonight IS Day 1. The only difference is the Sunday/Monday AM runs did NOT update
canonical_prices, so those can't be retroactively diffed.

### Tonight's run (2026-04-13 22:00 UTC):
Expected events:
1. 21:40 UTC: bd-transaction-pipeline-trigger
2. 22:00 UTC: bd-allocation-pipeline-trigger + bd-canonical-prices-daily (double fire)
3. ~22:05 UTC: bd-price-update Job 1 writes canonical_prices (version A)
4. ~22:10-22:15 UTC: gold runner boots, S_00 runs with FIXED gold_dispatch.sh
5. v2 overwrites canonical_prices (version B)
6. Freshness gate passes, A/B/C/D chain runs
7. ~23:30-23:45 UTC: D_04 completes, watchdog shuts down
8. ~22:15 UTC: bd-fees-pipeline-trigger fires (first prod run)

Also first production run of bd-fees tonight at 22:15 UTC. Independent chain, no
collision risk with gold/price.

---

## ADVI_OFFICE.W2 Status

Task order is `staged`. Dependency: DS W1 MCP GO signal.

DS W1 task order (`ADVI_OFFICE.W1`) is still `staged` in the XML. DS's today session
covered "SI fix, GEO AUA, W6-001 through W6-005" -- NOT ADVI_OFFICE W1.

`D_01.partner_analytics.py` shows S3 upload at 10:52 UTC today (from DS W6 work:
"reconcile geo metrics.aua to firm headline AUA") -- NOT the OFC office view changes.
`D_00b.portal_timeseries.py` shows S3 upload from April 10 (pre-OFC).

No MCP GO received. W2 remains blocked. Will proceed the moment the GO signal arrives.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Register agent + check inbox | Registered PID 11180. Inbox empty. |
| 2 | Read recent logs (2026-04-10) + task orders | bd-v2.22.0 (EventBridge) + bd-v2.23.0 (fees) confirmed shipped |
| 3 | Monday Runbook: check bucket versioning | `{"Status": "Enabled"}` -- Option A confirmed |
| 4 | Check gold logs since Friday | 4 runs found; canonical_prices stale since 2026-04-10 22:04 UTC |
| 5 | Investigate S_00 in gold logs | 25 failures: `unrecognized arguments: --upload` |
| 6 | Identify root cause | CATALOG entry had `--upload`; v2 argparser rejects it; tee pipe swallows exit |
| 7 | Edit `gold_dispatch.sh` line 87 | Remove `--upload` from S_00 catalog entry |
| 8 | `aws s3 cp gold_dispatch.sh` | Uploaded to `s3://opal-data-bd/code/gold/gold_dispatch.sh` |
| 9 | git commit 2a6136e4 | `fix(gold_dispatch): remove --upload from S_00 CATALOG entry` |
| 10 | git push origin CLOUD | Pushed |
| 11 | Write `phase3_v2_vs_job1_diff.py` | `data/analysis/phase3_v2_vs_job1_diff.py` |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before writing) | comp-blast | `comp-blast bd-gold-trigger` | No edges (known graph gap: EventBridge->Lambda, Lambda->EC2) |
| 1 (diagnostic) | S3 version history | `aws s3api list-object-versions ... silver/prices/canonical_prices.parquet` | Confirmed no new versions since 2026-04-10. Exposed silent S_00 failure. |
| 2 (before commit) | grep CATALOG gold_dispatch.sh | direct file read | Confirmed S_00 entry, argparser usage -- root cause isolated |
| 3 (after commit) | S3 upload verify | `aws s3 cp gold_dispatch.sh s3://...` | OK -- fix live on S3 |

Compiler gap noted: comp-blast/comp-trace do not index EventBridge->Lambda,
Lambda->EC2 SSM, or Lambda->Lambda invoke edges. This is the same gap logged in
bd-v2.22.0 and bd-v2.23.0 session logs.

---

## Current State

| Component | State |
|---|---|
| `gold_dispatch.sh` S_00 CATALOG | FIXED -- `--upload` removed. Fix live in S3 and committed to CLOUD (2a6136e4). |
| `build_canonical_prices_v2.py` | Unchanged -- correct, accepts no `--upload` |
| `canonical_prices.parquet` | Stale at 2026-04-10 22:04 UTC. Will be updated tonight by Job 1 then v2. |
| Phase 3 diff script | Written at `data/analysis/phase3_v2_vs_job1_diff.py` |
| Phase 3 Day 1 snapshot | NOT YET -- tonight after 22:15+ UTC: run `--fetch 2026-04-13` |
| ADVI_OFFICE.W2 | Staged -- blocked on DS W1 GO signal (DS W1 still staged, no MCP received) |
| bd-fees first prod run | Tonight 22:15 UTC -- first unattended run |
| bd-v2.23.0 | No changes this session |

---

## Next Steps

- **[0.6.0_AE_PartnerETL] Tonight ~22:00-23:45 UTC** -- Monitor tonight's gold run:
  1. `aws cloudwatch logs filter-log-events --log-group-name /aws/lambda/bd-gold-trigger` -- confirm Lambda fired
  2. After ~23:45 UTC: `aws s3api list-object-versions --bucket opal-data-bd --prefix silver/prices/canonical_prices.parquet` -- confirm 2 new versions tonight
  3. Run: `python data/analysis/phase3_v2_vs_job1_diff.py --fetch 2026-04-13`
  4. Then: `python data/analysis/phase3_v2_vs_job1_diff.py 2026-04-13` -- record results in diff tracking table

- **[0.6.0_AE_PartnerETL] Tonight ~22:15-22:30 UTC** -- Monitor bd-fees first prod run:
  1. Watch `s3://opal-data-bd/logs/fees-download-2026-04-13.log`
  2. Confirm: bronze upload, silver partitions written, instance auto-shuts down

- **[0.6.0_AE_PartnerETL] Tue-Fri** -- Repeat Phase 3 diff each morning (after 22:00 UTC run from prior night).
  Record results in diff tracking table in the Phase 3 runbook section of ADVI_GLDRST.022 log.

- **[0.6.0_AE_PartnerETL]** On GO signal from DS (ADVI_OFFICE W1 commit + MCP): proceed immediately
  with W2 -- dim file upload, QA run (D_00b, D_01, D_04), PROD run, MCP to DE + COO.

- **[Andrew]** S_00 was failing silently for 25 consecutive runs (since April 10). The fix is live.
  Phase 3 diff starts tonight. v2 will write canonical_prices for the first time in production.

- **[follow-up, not assigned]** `gold_dispatch.sh` line 544: `run_chain ... | tee` without `pipefail`
  swallows run_chain non-zero exits. Should add `set -o pipefail` after `set -e` (line 66) so
  future S_00-class errors are visible and don't silently continue the chain.
