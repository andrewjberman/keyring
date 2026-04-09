# Session Summary — 0.4.0_DS_ClientPlatform — 2026-04-06

**Start Time:** 7:30 AM ET
**End Time:** ~12:10 PM ET
**Projects:** ADVI_GLDOPS, ADVI_GLDRST, ADVI_ANONYM

---

## Task Orders Completed (7)

| TO | Project | Commit(s) | Summary |
|---|---|---|---|
| GLDOPS.002 | ADVI_GLDOPS | `af47c84e` | Pending marker re-enabled in EC2 runner + watchdog Check 4 |
| GLDOPS.003 | ADVI_GLDOPS | `8a6fef07`, `e419d83b`, `6c2b23e9`, `81ce9182`, `2c45ae29` | Silver override disabled, publisher GRO alignment, surgical garbage filter, churn decomposition |
| GLDRST.004 | ADVI_GLDRST | `426ac7ab`, `48513b64`, `c93552d1` | S3 key migration: lib/s3_layout.py + Phase A dual-write + Phase B read migration |
| GLDRST.005 | ADVI_GLDRST | `c2b42625` | --run-date flag + GOLD_RUN_DATE env var |
| GLDRST.006 | ADVI_GLDRST | `1f1cf3c9` | Post-run manifest (pipeline-manifest.json) |
| ANONYM.012 | ADVI_ANONYM | `4a1e289c` | Lambda PII handlers (clients-tab + client-detail) |
| ADHC_HISTRY | ADHC_HISTRY | (status only) | Confirmed project closed, corrected stale open items in CTO message |

---

## GLDOPS.003: GRO Investigation Arc

This was the main analytical thread of the session. Portal GRO showed ~1% for 2025 when actual 49F portfolio returns were 10-12%. Investigation uncovered four layered issues:

### Layer 1: Silver AUA Override (fixed, `8a6fef07`)
`SILVER_OVERRIDE_ENABLED` in script 05 was scaling gold AUA to BD allocations daily, clipping legitimate market appreciation. Disabled. RPS injection (ADHC_HISTRY P2) makes it unnecessary.

### Layer 2: Publisher Formula (fixed, `e419d83b`)
Publisher was recomputing `market = delta(AUA) - delta(NNA)` instead of reading pre-computed `market_growth` column from script 05. Fixed to read decomposition columns with graceful fallback.

### Layer 3: Blunt Outflow Caps (replaced, `6c2b23e9`)
AUA-based + velocity caps were eliminating $673M in legitimate outflows, inflating NNA and depressing GRO. Replaced with surgical garbage filter: exclude events > 10x account silver AUA OR > $50M absolute. Filter caught 282 garbage events ($7.5B total) while letting legitimate withdrawals through.

**After Layers 1-3:** GRO = +0.3%. Still not 10-12%.

### Layer 4: Relationship Churn (fixed, `81ce9182`)
`diff().fillna(0)` in the decomposition created a systematic negative bias: new clients' initial AUA attributed to nothing (zeroed), departing clients' AUA loss attributed to negative market growth. Added `churn` as 4th component in the decomposition identity:

```
delta(total_aua) = delta(nna) + market_growth + synthetic_correction + churn
```

Publisher updated to include churn. `total` in growth_decomposition JSON uses actual AUA delta (authoritative), not component sum (`2c45ae29`).

**After Layer 4:** Awaiting gold rerun verification. Expected GRO ~10-12%.

### Pricing Coverage Diagnostic
Ran as a side investigation. Found 99.4% pricing coverage. $153M (9.3%) has stale/never-updated prices (cash, structured notes, private funds). Not the primary cause but contributes marginally.

---

## GLDRST.004/.005/.006: S3 Key Migration

### .004: S3 Key Migration (3 commits)
- `lib/s3_layout.py`: ~45 S3 keys across 7 categories (dimensions, timeseries, views, artifacts, entities, validation, meta)
- Phase A: all 18 production scripts dual-write to new + old keys (19 files, +269/-75)
- Phase B: all read paths switched to new layout constants (15 files, +76/-48)
- 06b has try-new/fallback-legacy for self-referencing reads

### .005: TX Snapshot Date Anchor
- `--run-date` flag in run_gold_layer.sh, exported as `GOLD_RUN_DATE`
- Script 03 reads env var for snapshot_date with fallback to now()
- WS1 spec (publisher geo date anchor) documented for DT

### .006: Post-Run Manifest
- `gold/meta/pipeline-manifest.json` written after each run
- Per-script name, status (ok/skip), duration_s
- pipeline-complete.json still written for backward compat

---

## ANONYM.012: Lambda PII Handlers

Added `handle_clients_tab` and `handle_client_detail` to opal-partners-data Lambda. Both routed under `/shared/advisor-intelligence` with `_pseudonymize_s3_response` wrapper. Follows `handle_advisor_book` pattern exactly. Unblocks .013 (DT authorizer) and .014 (DE endpoint migration).

---

## Awaiting Results

1. **GRO verification** — AE running gold rerun with churn decomposition fix. Expected market_growth ~$93-112M (10-12% of $931M). NNA should be unchanged (~$305M).

2. **GLDRST .009** — AE migration gold rerun with new S3 layout. Needs to verify new keys populated correctly.

---

## Deployments This Session

| Tag | Pipeline | What |
|---|---|---|
| `bd-v2.20.1` | bd-pipeline | Publisher GRO decomposition (e419d83b) |
| `bd-v2.21.1` | bd-pipeline | Churn decomposition (81ce9182) |
| `bd-v2.21.2` | bd-pipeline | Total uses actual AUA delta (2c45ae29) |
| pending | partners-api | ANONYM.012 PII handlers (4a1e289c) |

---

## Current State

**All DS task orders complete.** No pending or staged TOs remaining.

Waiting on:
- AE gold rerun to verify GRO (churn fix)
- DT push + deploy for ANONYM.012
- DT .013 (authorizer passthrough) -> DE .014 (endpoint migration)
- AE .009 (GLDRST migration rerun) -> .010 (old key cleanup)

---

## Do NOT

- Re-enable silver AUA override -- deprecated post-RPS
- Re-enable AUA-based or velocity outflow caps -- replaced by surgical garbage filter
- Trust GRO numbers until gold rerun with churn fix (`81ce9182`) completes
- Deploy ANONYM.014 (DE endpoints) before .012 (DS handlers) + .013 (DT authorizer) are deployed -- that's what broke it last time
