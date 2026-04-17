# Session — 0.4.0_DS_ClientPlatform~B — 2026-04-17 (session I)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Window:** 2026-04-16 23:14 ET to 2026-04-17 00:17 ET (re-startup at 00:16 ET for closeout)
**Scope:** ADVI_ROLLUP.GOLD-DATE-FIX — ship option (d) (B_01 snapshot_date derived from latest `silver/allocations` partition). Two ship cycles across the window: first ship reverted by Andrew, re-ship per COO HIGH PRIORITY TO.

## Context

PROD halted twice on UTC-vs-silver-date drift:
- 2026-04-17 01:23 UTC on QA (auto-skip semantic bug)
- 2026-04-17 04:23 UTC on PROD (post-revert, same date-drift fingerprint)

`snapshot_date` at B_01 main() L2071-2074 and `compute_lots()` L1578-1581 was previously `pd.Timestamp.now().normalize()` when `args.date` and `GOLD_RUN_DATE` were both unset. On the EC2 runner (UTC tz), overnight ET runs pull `snapshot_date = "today UTC"` = "tomorrow or T+2 ET" — 1-2 days ahead of the `silver/allocations` partition. Misalignment cascaded through RPS synthetic-lot generation + sell_corrections.

Prior related commits (context only, not this session):
- `a9f42c3b` — stale-RPS auto-skip (~B, earlier) — masked the bug by silently skipping sell_corrections when `rps_date != snapshot_date`.
- `0e9ece2a` — ~D reverted the auto-skip (semantic fix). Auto-skip fired for legitimately-fresh RPS data and caused ~$800M-$1B MV overcount ($2.493B observed vs $1.695B BD-authoritative).

## Timeline (this session)

| Time (UTC) | Event |
|---|---|
| ~03:14 | `59340b42` — ~B first ship of option (d). |
| ~03:15 | `4317354a` — Andrew reverted. COO sent STOP ("BCD chain firing on QA now"). |
| ~03:40 | COO HIGH PRIORITY dispatch: re-ship option (d) properly, 22:00 UTC deadline for QA GREEN. |
| 04:09 | `ec2c1efc` — ~B re-shipped option (d). Pushed to origin/CLOUD. |
| ~04:10 | `aws s3 cp` to `s3://opal-data-bd/code/gold/B_01.holdings_lots.py`. |
| 04:17 | Startup for closeout — inbox drained, comp-pipescript deployed verified MATCH, MCP COMPLETE dispatched to CTO+COO. |

## Change Summary

File: `data/black_diamond/scripts/gold/B_01.holdings_lots.py` (+40/-5)

Two touchpoints, both following the same precedence order:

```
args.date > GOLD_RUN_DATE env > latest silver/allocations YYYY-MM-DD.parquet > pd.Timestamp.now() fallback
```

1. `main()` L2085-2109 — fully-refactored block, prints derived date for operator visibility. `WARN:` messages on the empty-listing + exception paths so failures are visible in runner stdout (no silent fallback).
2. `compute_lots()` L1578-1595 (`snapshot_date=None` branch) — matches main() logic, minus the print (this function is called internally, operator visibility already covered upstream).

S3 client (`s3`) is module-level in B_01 — no new boto3 client needed, no IAM changes.

## Deploy State

| Step | Result |
|------|--------|
| Commit SHA | `ec2c1efc9ec3773cf4921de9c9c673a517e61699` |
| Author | `0.4.0_DS_ClientPlatform~B <0.4.0_DS_ClientPlatform~B@opal.agent>` |
| Push | `origin/CLOUD` up to date (HEAD == origin/CLOUD verified 04:17 UTC) |
| S3 upload | `s3://opal-data-bd/code/gold/B_01.holdings_lots.py` |
| py_compile | exit 0 |
| `comp-pipescript deployed B_01` | MATCH |
| MCP COMPLETE | 1.0.0_SA_CTO (04:17:40Z), 2.0.0_SA_COO (04:17:47Z) |

## Compiler Tools

| Tool | Result | Pass/Fail |
|---|---|---|
| `comp-pipescript deployed B_01` | 2 MATCH, 0 STALE, 0 MISSING | PASS |
| `comp-pipescript io B_01` | READS: `gold/dimensions/accounts_dimension_latest.parquet` (A_00). WRITES: `gold/timeseries/holdings_lots/{date}.parquet`, `gold/timeseries/holdings_lots_shadow/{date}.parquet`, `gold/holdings_lots_v2_dryrun/{date}.parquet`, `gold/timeseries/holdings_lots/backfill_{date}.parquet`. No COLUMN GAPS. | PASS |

No `comp-validate` run this session — deploy-only change, no artifact produced. AE will run `--single B_01` QA validation on COO/CTO signal.

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/B_01.holdings_lots.py` | `snapshot_date` derived from latest `silver/allocations` partition at main() L2085 + compute_lots() L1578. +40/-5. |

## Current State

- Option (d) shipped, pushed, S3 MATCH. PROD next nightly (04:00 UTC) will pick up `ec2c1efc` on EC2 boot.
- QA validation pending — AE `--single B_01` on qa-runner, coordinated by COO/CTO. Deadline 22:00 UTC (2026-04-17).
- `2026-04-17.parquet` does NOT exist in `gold/timeseries/holdings_lots/` (last night's PROD halted before write — 404 per COO). After fix validates, PROD will write `2026-04-16.parquet` once Schwab CRS lands ~11:00 UTC.

## Next Steps

- [CTO / COO] Coordinate AE `--single B_01` QA run on `bd-gold-qa-runner` (i-0090b823a4a0997e3). Validate: snapshot_date print matches latest silver/allocations key; holdings_lots parquet written; no halt.
- [~B] Standing by. Will close RAVC loop when AE QA evidence lands.
- [Remaining staged TOs] `ADVI_ROLLUP.SL-P1` (sleeve shadow emit Phase 1 of 4), `BDPL_CNPRCS.WP-10b` (gold/silver recon harness), `COMP_LEARNS.005` (adversarial-query scaffolding Phase 4) — all staged, none unblocked by tonight's work.

## Do NOT

- Do NOT re-introduce `pd.Timestamp.now().normalize()` as the primary `snapshot_date` source. It is the fallback only. Overnight UTC drift is the root cause of the twin 04-17 halts.
- Do NOT re-introduce the stale-RPS auto-skip (`a9f42c3b` shape) without first computing `expected_latest_rps_date` from US market calendar + Schwab delivery SLA. The broken spec silently clears sell_corrections on fresh data. See ~D's `0e9ece2a` commit body for the full diagnosis.
