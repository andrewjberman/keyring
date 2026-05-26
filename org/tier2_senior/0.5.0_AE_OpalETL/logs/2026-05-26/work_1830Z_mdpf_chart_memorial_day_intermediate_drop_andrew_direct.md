# work tick — MDPF chart Memorial Day Intermediate-drop fix (Andrew-direct)

**Date:** 2026-05-26
**Tick:** 1830Z (post `/work` session start at ~14:00Z; ad-hoc Andrew-direct work)
**Archetype:** INVESTIGATE + FIX + DEPLOY
**Outcome:** SHIPPED 3-step plan; portal Daily AUA chart restored to clean trend

## Andrew brief

> Today is 5/26/2026. Yesterday, it was Memorial Day, which I do not believe is a
> trading day. We recorded AUA anyway, and demonstrated a collective 70m drop in
> assets which is almost certainly incorrect either way. What I noticed upon
> reviewing the Daily AUA Trend chart in the portal ui was that while most of the
> models were fairly consistent, there was a 60m drop from around 358m to 290m or
> so in the Intermediate model. I need you to look into this, verify what
> happened here, and patch as needed.

## Root cause (single sentence)

The MDPF daily chain hard-failed at the WS-A aggregator's `identity_2_etf_residual`
gate on 2026-05-25 + 2026-05-26 because PFOE net assets dropped from $111.75M
(as_of 5/20) to $79.36M (as_of 5/26) while the Schwab RPS feed for 49F's PFOE
holdings stayed frozen at $100,010,587.95 (`rps_date_used=20260515`, 11d stale)
→ phantom $26.4M over-attribution → no platinum partition written for 5/25 or
5/26 → `build_legacy_compat_emit.py` couldn't emit a 5/25 entry → the SmartX EC2
cron's `append_new_dates_only.py` raced ahead at 14:17Z and contaminated
`aum-timeseries.json` with a 49F-only 5/25 row showing Intermediate $292.91M
(vs the 5/22 combined 49F+Inflection value of $358.40M). The chart rendered
that 49F-only value as a ~$65M Intermediate-model drop.

## Diagnostic chain

1. Located writers to `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json`:
   - SmartX pipeline (Lambda) via `append_new_dates_only.py` + `forward_fill_missing_dates.py` — 49F-only data, runs at 14:15Z daily
   - MDPF chain (EC2 + EventBridge `mdpf-daily-refresh-trigger` cron(0 15 ? * MON-FRI *))
     via `data/mdpf/scripts/backfill/build_legacy_compat_emit.py` — combined
     49F+Inflection methodology, runs at 15:00Z daily

   The two writers race; on a normal trading day MDPF overwrites SmartX's 49F-only
   row with the combined emit. On 5/25 + 5/26 MDPF failed → SmartX's row stayed.

2. Confirmed by reading DynamoDB `TIMESERIES#Intermediate#Daily` SK=2026-05-25
   `{aum: 292,908,640.6, account_count: 1623, source: append_today_smartx,
   last_updated: 2026-05-26T14:17:06.014783}` — the exact contaminating row.

3. Read `s3://opal-data-mdpf/telemetry/mdpf-daily-runner/history/mdpf_daily_20260526_150031.json`
   showing `status: failed`, last completed step WS-A `status: error`,
   `last_output: "Stage 3 WS-A reconciliation HARD FAIL (rc=1)"`. Same failure
   on 5/25 (`mdpf_daily_20260525_150030.json`).

4. Ran the aggregator dry-run locally:
   - `identity_1_aggregate_sum: PASS`
   - `identity_2_etf_residual: ERROR` — `min_public_residual: -26,399,320.29`
   - `identity_3_no_double_count: PASS`
   - `sentinel_1/2/3: all PASS`
   - `overall: ERROR` → platinum write SKIPPED per `drop-rather-than-fabricate`
     (MDPF_ASSETS.019 contract)

5. Identified the failing ETF (PFOE) by reading the WS-D feeders:
   - `mdpf/feeds/etf_net_assets/2026-05-26.parquet`: PFOE `net_assets=$79,356,156`
     (as_of 5/26), vs 5/22 partition's $111,752,976 (as_of 5/20) — a real $32.4M
     NAV drop
   - `mdpf/feeds/partner_held_etf/49financial/2026-05-26.parquet`: PFOE
     `held_value=$100,010,587.95`, `rps_date_used=20260515` — RPS frozen 11d
   - Andrew confirmed RPS data has since been uploaded + converted

## 3-step fix (Andrew-sequenced)

### Step 1 — surgical chart fix (immediate)

Stripped the 2026-05-25 row from `aum-timeseries.json` (aggregate + by_model +
periods + metadata) via `.runtmp/strip_525.py`. S3 versioning preserves the
pre-strip artifact (`2026-05-26T14:17:07Z` version) for forensic rollback.

### Step 2 — structural roll-forward (durable)

`data/mdpf/scripts/backfill/build_legacy_compat_emit.py` (commit
`322c00779`): added `load_latest_platinum_on_or_before()` + a roll-forward path
that activates when `load_platinum_partition(d)` returns None — searches for
the most recent prior partition within `MAX_ROLLFORWARD_DAYS=7` and emits using
that partition's combined 49F+Inflection values stamped at today's period.
Marks the entry with `roll_forward_source: YYYY-MM-DD` for provenance. Bridges
the 14:15Z → 15:00Z race window when MDPF can't write a fresh partition.

Pre-commit gate clean; pushed to origin/CLOUD; `aws s3 cp` to
`s3://opal-data-mdpf/code/scripts/backfill/build_legacy_compat_emit.py`; local
md5 == S3 ETag MATCH (`1b76e02d91e80d065a839cc1eb0f5583`).

### Step 3 — identity_2 → WARN (root-cause unblock)

`data/mdpf/scripts/gold/mdpf_aggregate_aua.py` (commit `2d0860c60`): downgraded
`id2_status` from `ERROR` to `WARN` on `min_public_residual < -RECON_TOLERANCE`.

Andrew-direct rationale: ETF decomposition / Cohort 0 is audit-only and is NOT
surfaced in the client-facing portal product, so an id2 over-attribution must
NOT hard-block the chain that builds the client-facing per-model Daily AUA
chart. The gate remains visible in the artifact for operational review
(sustained / non-stale-RPS over-attribution still surfaces); it just no longer
triggers `overall=ERROR`.

Pre-commit gate clean; pushed; `aws s3 cp` to
`s3://opal-data-mdpf/code/scripts/gold/mdpf_aggregate_aua.py`; md5 MATCH
(`9370ca7358eea16335a12aedeffc18a8`).

## Validation

Manually re-triggered the chain via `aws lambda invoke
--function-name mdpf-daily-trigger` after Andrew confirmed RPS refreshed.

Run `mdpf_daily_20260526_181245` completed clean:
- STAGE0-BRONZE ok (12s)
- WS-E ok (65s)
- WS-A ok (3s) — `identity_2` passed naturally with fresh RPS data closing the
  over-attribution gap (validating the operational hypothesis, independent of
  the Step 3 code change which provides durable protection going forward)
- LEGACY-EMIT ok (10s)
- ROLLUP ok (23s)
- `last_output: "All 4 stages complete -- platinum/mdpf/aggregate_aua/2026-05-26.json
  + timeseries refreshed"`

Final chart-facing state in `aum-timeseries.json`:

| period | aggregate aum | Intermediate aum |
|---|---|---|
| 2026-05-22 | $1,455,318,627.75 | $358,397,731.23 |
| 2026-05-26 | $1,463,507,194.97 | $359,389,429.34 |

Smooth ~$8M aggregate growth + ~$1M Intermediate growth Mon→Tue. No Memorial
Day phantom drop. CloudFront cache refreshes within 5min (Cache-Control
`max-age=300`).

## Artifacts

- Commits: `322c00779` (build_legacy_compat_emit.py) + `2d0860c60`
  (mdpf_aggregate_aua.py); both pushed to origin/CLOUD
- S3 deployed: both files md5-MATCH between local and
  `s3://opal-data-mdpf/code/scripts/{backfill,gold}/`
- Platinum partition: `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-26.json`
- Chart artifact: `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json`
  (270,394 bytes, ends at 2026-05-26 + Intermediate $359.39M)
- Audit log: `org/git-author-override-audit.log` (two FORCE-BYPASS entries
  for concurrent-agent index contention; commits scoped via `--only` flag to
  single file each)

## Open follow-ons (not blocking)

1. The SmartX EC2 cron daily race with MDPF chain is structurally present; my
   Step-2 roll-forward catches it whenever a missing-platinum date appears in
   the legacy file. Could later eliminate the SmartX append step entirely
   (let MDPF chain be the sole writer of `aum-timeseries.json`) — bigger
   architectural change, not requested.
2. The `partner_held_etf` RPS feed staleness (11d on 5/26) is an operational
   variable; sustained staleness > a week is worth an alarm if it recurs.
3. The SK=2026-05-25 DynamoDB row in `TIMESERIES#*#Daily` PKs is still present
   (49F-only; written by SmartX pull this morning). Could be deleted for
   cleanliness, but `append_new_dates_only.py` only queries SK > latest_date so
   it won't re-leak into `aum-timeseries.json` now that the latest period is
   2026-05-26.

## Archetype + lane discipline

- archetype: INVESTIGATE + FIX + DEPLOY (multi-stage; bordered ad-hoc)
- lane: 0.5.0_AE_OpalETL base (AE infra/data-pipeline scope; gold + backfill
  scripts under `data/mdpf/scripts/` are ANY-lane catch-all path)
- owned-paths: `data/**` → ANY (`permitted_agents: "*"`); commit cleanly under
  AE author
- safe-commit: invoked with `--force` twice due to concurrent-agent index
  contention; `--only` flag scopes both commits to single declared file each;
  FORCE-BYPASS entries logged to `org/git-author-override-audit.log`

work-cycle:NNNN trailer applied on this log via cycle-log discipline.
