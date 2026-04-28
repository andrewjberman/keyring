# Session Log -- 0.4.0_DS_ClientPlatform~D -- 2026-04-28 (continuation)

**Lane:** ~D
**Project:** ADVI_INFSHIP Phase 1 L4
**TO:** ADVI_INFSHIP.L4
**Continues:** advi_infship_l4_bronze_pull_script_authored.md

---

## Summary

Path C shipped per CTO 2026-04-28 pre-authorization. silver/api_dims/assets/ landed on
S3 sourced from canonical/holdings (8d stale, INFGRD allowlist applied at silver layer
since canonical is pre-INFGRD-chain-rerun). Orion API per-asset pull deferred to
INFSHIP.A2 backlog -- 4x Generate POST timeouts on Asset grouping.

---

## Orion API Pull Attempts (all 4 timed out)

| Version | entityIds | window | POST timeout | Result | Cleanup |
|---------|-----------|--------|--------------|--------|---------|
| v1 | [] (firm) | 3y | 300s | TIMEOUT | DELETE 204 |
| v2 | [3,11,12] | 3y | 900s | TIMEOUT | DELETE 204 |
| v3 | [3,11,12] | 7d | 900s | TIMEOUT | DELETE 204 |
| v4 | [] (firm) | 7d | 900s | TIMEOUT | DELETE 204 |

API itself was reachable throughout (sanity-check `GET /Verbose?top=1` returned 200 in
0.9s). All 4 orphan saved queries cleaned via `DELETE /Verbose/{id}` (204).

**Hypothesis:** Asset-grouping Generate is fundamentally too heavy for the synchronous
Generate POST endpoint, regardless of date window or entity scope. 8 cols + 7d window +
firm scope still timed out after 15 minutes. Server-side cube computation appears to
scale with row count (accounts x assets), not date range. Would need server-side
async support or vendor-side optimization.

---

## Path C — Silver from canonical (CTO pre-auth)

CTO MCP 2026-04-28 ~05:11Z: "PRE-AUTHORIZATION: Path C ships if v4 fails. No further
CTO ACK required... canonical/holdings_2026-04-20.parquet IS the per-(account,asset)
data the silver script needs. 8-day staleness is acceptable for v1 ship; INFSHIP Phase
2 DE B5/B6 (Books L3/L4) gates on this lane and we're not making them wait on an Orion
API timeout debug cycle."

### Refactored `build_assets_dim.py`
- Source: `s3://opal-data-inf/gold/canonical/holdings_{date}.parquet` (auto-discovers latest)
- INFGRD filter at silver: `advisor_key IN {inflection_wealth_management, peter_lee, patrick_scanlan}` (canonical pre-dates INFGRD chain rerun on hold; multi-firm contamination $133.7M total -> $91.8M Inflection-only)
- source_system tag: `'canonical_silver'` (vs `'orion-api'`)
- snapshot_date = canonical parquet date (2026-04-20)
- Schema: account_id, asset_id (synthesized = ticker; NAME::slug fallback), asset_ticker, asset_name, position_mv, rep_id (mapped from advisor_key), snapshot_date, source_system, advisor_firm
- AUA guard $50M-$400M: $91.8M PASS

### Silver counts (post-INFGRD-filter)
| Metric | Value |
|--------|-------|
| Rows | 9,645 |
| Total AUA | $91,847,084.75 |
| Distinct accounts | 781 |
| Distinct assets | 728 |
| Distinct tickers | 728 |
| rep_id breakdown | 3 (firm placeholder) = 8,925 / 11 (Peter) = 706 / 12 (Patrick) = 14 |

### S3 ship
```
s3://opal-data-inf/silver/api_dims/assets/snapshot_date=2026-04-20/data.parquet
113,953 bytes (~111 KB)
```

---

## Next slice (gates on commit + RAVC2)

| Item | State | Owner |
|------|-------|-------|
| RAVC2 to CTO + COO -- Path C silver shipped | Imminent this session | ~D |
| Signal DS~B (L1/L2-2/L3-2 top_holdings publishers) -- silver/api_dims/assets/ available | After RAVC2 | ~D |
| `data/orion/scripts/classification/classify_assets.py` (BD pattern port: gpt-4o-mini + bd-securities DDB lookup for the 728 tickers) | Next session | ~D |
| Refactor `INF_I_D03._classify()` keyword fallback -> use new classifier module | Gates on classifier | ~D |
| Re-run INF_I_D03 -> improved firm_composition.json | Gates on classifier integration | ~D |
| INFSHIP.A2 backlog item: Orion API Asset-grouping Generate vendor ticket | Author next session | ~D |

---

## Compiler Tools

| Tool | Where | Result |
|------|-------|--------|
| `.tools/ds-commit-gate.sh` | Pre-commit on build_assets_dim.py (Path C refactor) | CLEAN |
| `.tools/ds-commit-gate.sh` | Pre-commit on pull_inflection_assets.py (chunking additions) | CLEAN |

`comp-pipescript io` on build_assets_dim.py / INF_I_D03.composition_artifacts.py: not run
yet -- INF gold-script indexing extension is the ADHC_COMPIL.001 deliverable still in
flight. Will run if the INF-aware indexer is available before the classifier integration
session.
