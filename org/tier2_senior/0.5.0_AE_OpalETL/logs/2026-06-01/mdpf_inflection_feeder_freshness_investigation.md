# MDPF Inflection Feeder Freshness Investigation — 2026-06-01

**Agent:** 0.5.0_AE_OpalETL (spawned under chimera serial 0.5.0_AE_PartnerETL; Andrew-corrected)
**Dispatched by:** 2.0.0_SA_COO ([DRIVE] 20260601T134837Z) — MDPF P1 redirect
**Question posed:** Is `inflection/2026-05-27.parquet` carrying `as_of_date=2026-05-26` a REAL stale feed (upstream pull failed/skipped → re-pull) or EXPECTED (no source publish that date)?

## Verdict: NEITHER — it is a downstream cross-pipeline SCHEDULING RACE. Source data is fresh and complete.

The upstream Eclipse/INF source produced fresh, complete 5/27 AND 5/28 partitions on schedule. The stale `as_of_date` is a feeder-vs-upstream **ordering** artifact, not a missing/failed source feed and not a no-publish day (5/27, 5/28 are normal business days).

## Mechanism

`data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py` writes the partition **filename** as the run date (`--date`), but stamps the `as_of_date` **column** as `silver_date` — the actual Eclipse vintage resolved by `latest_inf_eclipse_dates()`, which finds the latest `opal-data-inf/gold/eclipse/{date}/` partition that has a `_meta/gold_complete.json` **sentinel** and reads its `eclipse_silver_date`. If today's eclipse gold has not yet landed (sentinel absent) at feeder runtime, it rolls forward to the prior vintage (line 506-518 roll-forward; deliberate "absorb a missed day" resilience per `mdpf-daily-dispatch.sh` lines 195-202).

The MDPF daily chain (`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`) runs the WS-C feeder in **Stage 1** with `--date $RUN_DATE` and **no `--eclipse-date`** (line 206) — so it always auto-resolves. The chain fires ~11:00–11:01 UTC daily. The **upstream Eclipse/INF gold build is on a DECOUPLED schedule** with a drifting completion time. The two are not dependency-linked.

## Evidence (S3 ground-truth, read 2026-06-01)

| Feeder partition | `as_of_date` (column) | Feeder ran (S3 mtime) | Eclipse gold `{date}` sentinel mtime | Outcome |
|---|---|---|---|---|
| 5/25 | 5/25 | 11:00:50 | — | fresh |
| 5/26 | 5/26 | **18:40:29** (manual MemDay drop) | 10:40:49 | fresh (ran after gold) |
| **5/27** | **5/26** (−1d) | 11:01:00 | **11:12:26** | **STALE — ran 11 min before gold** |
| **5/28** | **5/27** (−1d) | 11:00:56 | **11:04:29** | **STALE — ran 4 min before gold** |
| 5/29 | 5/29 | 11:00:53 | 10:55:04 | fresh (gold finished 6 min before feeder) |

- Eclipse gold 5/27 `gold_complete.json` declares `eclipse_silver_date=2026-05-27` (fresh, real). Eclipse gold 5/28 declares `2026-05-28`. Source is NOT missing on either date.
- `non_model_aua/inflection`: 5/26, 5/27, 5/28 all 6861B; `model_aua_positions`: 5/26 == 5/27 (14238B). The identical bytes = the flat 5/26→5/27 step CVO/DS~B flagged.
- The chain reports `complete` (roll-forward is non-fatal), so **no `MDPF/DailyChain.ChainFailed` alarm fires** — the staleness is invisible to ops, only visible in the daily trend. (Self-heals whenever the feeder happens to run after gold, e.g. 5/29.)

## Coordination boundaries

- **`mdpf-daily-dispatch.sh` (EC2 runner orchestration):** AE-owned (mine) — the structural fix lives here.
- **`build_mdpf_wsc_inflection_feeder.py` roll-forward logic:** DS~B-authored (0.4.0_DS_ClientPlatform~B) — re-emit RUN is operational; vintage-resolution CODE change is DS's.
- **`opal-data-mdpf` bucket IAM lock + access-logging:** 0.7.0_AE-owned — any re-emit upload / `code/` script deploy needs 0.7.0_AE coordination.
- A re-emit rewrites consumer-facing platinum (Stage 3 aggregate + Stage 4 timeseries consumed the stale feeder) — historical-data rewrite, warrants COO go (esp. post-MDPF-close + today's Andrew-direct fix 80224d674).

## Recommended remediation (proposed to COO; NOT executed unilaterally)

1. **Immediate cleanup — feeder RE-EMIT (not source re-pull):** re-run the MDPF chain for `--date 2026-05-27` and `2026-05-28` via the EC2 mdpf-daily-runner now that fresh eclipse gold exists — Stages 1→4 propagate the corrected vintage into platinum + the rollup timeseries, removing the flat step. Coordinate the bucket write with 0.7.0_AE; confirm with DS~B that re-emit (vs. accepting the historical flat step) is wanted.
2. **Structural fix (prevent recurrence) — AE, my domain:** gate the chain's Stage-1 WS-C feeder on the eclipse gold sentinel for `RUN_DATE` — poll `s3://opal-data-inf/gold/eclipse/{RUN_DATE}/_meta/gold_complete.json` with a bounded timeout, then run the feeder; on timeout, fall back to the existing roll-forward (preserves current resilience). Robust to eclipse-build drift. Cheaper-but-fragile alternative: shift the chain trigger later (~12:00 UTC) past the observed ~11:12 max end-time. Recommend wait-for-sentinel. I can author this pending COO go.

## Next steps
- [COO] RAVC2 sent with verdict + remediation plan; awaiting go on (1) re-emit and (2) structural-fix TO.
- [0.4.0_DS_ClientPlatform~B] coordination message sent — data-layer confirm + re-emit alignment.
- [0.7.0_AE] flag for bucket-write coordination if re-emit is approved.
