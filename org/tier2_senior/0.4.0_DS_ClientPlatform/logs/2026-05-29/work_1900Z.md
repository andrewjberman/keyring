# /work tick — MDPF_SCOPED F4/F1-C2/F5

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE
**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-29

---

## Work done this tick

### Commits landed (941e4dce6..a1a344e6d CLOUD)

| Commit | Finding | Description |
|--------|---------|-------------|
| a27c02971 | F4 | load_1a_daily period-end-coherent selection + partial-suppress + regression sentinel |
| a1a344e6d | F1-CHANGE-2 | Inflection history backfill script (client_performance spine) |
| e88c54e23 | F5 | Registry v4 S4-canonical display_names + consolidation re-resolve |
| 30c19b26c | F1-CHANGE-1 | Daily feeder repoint (spine custody) — prior tick, accepted |

### S3 deploys

- 391 `non_model_aua/inflection/{date}.parquet` feeder files uploaded (2024-11-01 → 2026-05-17) via new backfill script
- `build_aggregate_aua_timeseries.py --upload` ran (401 dates, all 4 per-firm timeseries + combined)

### Verification results

| Finding | Result | Notes |
|---------|--------|-------|
| F5 | PASS | S4 canonical: Ultra-Long Term / Long Term / Intermediate Term / Short Term / Ultra-Short Term |
| F1 latest tie | PASS | $206.01M (spine 5/29 value; $205.53M was 5/28 — correct) |
| F1 full history | NOT YET | Consolidation reads per-date platinum JSONs; pre-5/18 JSONs have only 49financial; Inflection feeders feed the WS-A aggregator not the consolidation directly |
| F4 | NOT YET | Per-date S3 partitions carry old .029 LTC values; load_1a_daily fix prevents recurrence but the stale JSONs haven't been re-emitted |

### Scope finding surfaced to COO

Per-date `platinum/mdpf/aggregate_aua/{date}.json` re-emit needed to land F1-history + F4 correction. Two options:
1. Run `build_mdpf_process_backfill.py --upload` (F4 fix + includes Inflection post-5/18) + a pre-5/18 Inflection patch (new) 
2. Scope F1 historical to "post-5/18 only" (defer pre-5/18 Inflection fill)

Awaiting COO decision.

## Compiler Tools

comp-pipescript io: MDPF scripts not in comp-graph (BD-gold only); attempted per Rule 14, fallback to direct reads. comp-pipescript deployed: MDPF bucket not covered by BD-gold checker. Both gaps flagged to COO (2nd occurrence today; low-pri follow-on).

## Current State

Code for F1-CHANGE-1 (ACCEPTED), F4, F1-CHANGE-2, F5 all committed and pushed. F5 fully verified. F1/F4 S3 re-emit pending COO scope decision. Awaiting COO on per-date re-emit authorization.

## Next Steps

- [COO] Authorize F4 per-date re-emit (build_mdpf_process_backfill.py --upload) + scope decision on pre-5/18 Inflection historical fill
- [DS~B] On GO: run process-backfill re-emit → Inflection patch (if scoped) → reconsolidation → verify (12/26 jump gone + Inflection history) → RAVC2 F1+F4
- [DS~B/AE] F1 daily-feeder S3 deploy: `aws s3 cp data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py s3://opal-data-mdpf/code/...` per Rule 13 (pending COO nod for coherent deploy after CHANGE-2 completes)
