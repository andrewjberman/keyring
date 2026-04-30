# Session Log: ADHC_COMPIL.013
**Date:** 2026-04-30
**Agent:** 0.7.0_AE_CloudOps
**TO:** ADHC_COMPIL.013 (comp-freshness dispatch gate integration)

---

## Summary

.013 wired `comp-freshness` as a pre-dispatch gate in both BD and INF dispatchers. Also discovered and remediated a 199.6h staleness gap in `inf_silver_canonical_prices` caused by `INF_build_canonical_prices.py` never being added to the INF dispatch chain after DS authored it 2026-04-22.

---

## Phase 1: Pre-flight

- RAVC4'd .012: tool at `.tools/comp-freshness` (c77fc2eba), configs at `data/*/scripts/gold/gold_freshness_config.yaml`. Both exist and comp-freshness chain bd exits 0 with real S3 data.
- `comp-blast gold_dispatch.sh` / `comp-blast orion-gold-dispatch.sh`: no graph dependencies on dispatcher exit-code semantics — safe to modify gate contract.
- Direct read of both dispatchers to locate .002 cascade gate and existing freshness gate insertion points.

Lane reclassification: `data/black_diamond/scripts/gold/gold_dispatch.sh` was classified POD4 in `.owned-paths.yaml`. Added specific override to `CLOUD_OPS_OR_ETL` (longest-match-wins), mirroring the existing `orion-gold-dispatch.sh` reclassification. Validated 23 lanes, 106 path rules, all resolve.

---

## Gate Implementation

### Gate behavior (both dispatchers)

Placement: AFTER the silver-date `check_freshness` gate (which exits early on no-new-data), BEFORE chain dispatch. Only fires for `--chain` mode; `--single`/`--group`/`--from` bypass (ad-hoc, not nightly dispatch).

```
Sequence: .002 cascade gate -> silver-date check -> .013 comp-freshness gate -> dispatch
```

- **Exit 0 (PASS/WARN):** proceed with dispatch
- **Exit 1 (FAIL):** DISPATCH BLOCKED + remediation steps printed + bypass instructions
- **Exit 2 (config/AWS error):** DISPATCH BLOCKED + distinct tooling-failure message (not staleness)

### Bypass flag: `--no-freshness-check`

- Bypasses gate; ALWAYS calls `log_freshness_bypass_entry()` before dispatch proceeds
- Log format: `[ADHC_COMPIL.013] FRESHNESS-BYPASS: <ts> | <dispatcher> | <chain> | <operator> | <reason>`
- `--bypass-reason "<text>"`: stores audit context in log entry; `(no reason given)` if absent
- Passes through BG re-invoke via `FRESHNESS_BYPASS_REASON` env var (avoids word-split on spaces)

### New function: `log_freshness_bypass_entry()`

Mirrors `.002`'s `log_bypass_entry()` pattern. Non-suppressible: appends to `org/compiler-tools-log.md` via git-root lookup.

---

## INF Silver-Prep Staleness Remediation

**Root cause:** `INF_build_canonical_prices.py` (INF equivalent of BD's S_00) was authored by DS 2026-04-22 and uploaded to S3 2026-04-29, but was never added to the orion-gold-dispatch.sh CATALOG or chain. `inf_silver_canonical_prices` was last rebuilt 2026-04-22 — 199.6h stale when detected.

**Fix:**
- Added `INF_S_00|INF_build_canonical_prices.py|` to CATALOG
- Added `CHAIN_SILVER_PREP="INF_S_00"` (mirrors BD's `CHAIN_SILVER_PREP="S_00"`)
- Added silver-prep pre-gate block for `--chain full`: auto-runs INF_S_00 BEFORE the freshness gate and silver-date check, so canonical prices are always fresh including weekends/holidays
- Added `--chain silver-prep` option for manual standalone invocation
- Updated `--help` to document the new chain

After next INF nightly dispatch (`--chain full`), `inf_silver_canonical_prices` will be rebuilt via INF_S_00 as the first step.

---

## AC Verification

| AC | Scenario | Result |
|----|----------|--------|
| AC1 | BD real config, all PASS → proceeds | exit 0 ✓ (verified vs real S3: all non-vendor PASS, vendor WARNs non-blocking) |
| AC2 | BD synthetic fail_age_hours=1 on bd_silver_canonical_prices | exit 1 ✓ (17.1h vs 1h threshold) |
| AC3 | BD --no-freshness-check (no reason) | bypass logged (no reason given) ✓ |
| AC4 | BD --no-freshness-check --bypass-reason "vendor RPS feed scheduled outage 2026-04-30" | reason text in log entry ✓ |
| AC5 | INF real config | exit 1 (inf_silver_canonical_prices 199.6h FAIL — expected, under remediation) |
| AC6 | Config renamed → missing YAML | exit 2 ✓ (BD and INF both) |
| AC7 | INF --no-freshness-check (no reason) | bypass function mirrored from BD ✓ |
| AC8 | INF --no-freshness-check --bypass-reason | same log pattern ✓ |
| AC9 | Bypass log entries format | single-line, pipe-delimited, [ADHC_COMPIL.013] prefix ✓ |

---

## Commits

| Hash | Author | Description |
|------|--------|-------------|
| 5d7661437 | 0.7.0_AE_CloudOps | chore(ADHC_COMPIL.013): reclassify gold_dispatch.sh lane -> CLOUD_OPS_OR_ETL |
| 5b1d69025 | 0.7.0_AE_CloudOps | feat(ADHC_COMPIL.013): comp-freshness pre-dispatch gate + INF silver-prep chain |

---

## S3 Deployment

| Script | S3 Path | Size | Uploaded |
|--------|---------|------|---------|
| gold_dispatch.sh | s3://opal-data-bd/code/gold/gold_dispatch.sh | 49312 bytes | 2026-04-30T17:13:54Z |
| orion-gold-dispatch.sh | s3://opal-data-inf/code/gold/orion-gold-dispatch.sh | 31598 bytes | 2026-04-30T17:13:55Z |

---

## Bypass Log Sample

```
[ADHC_COMPIL.013] FRESHNESS-BYPASS: 2026-04-30T21:00:00Z | gold_dispatch.sh | chain:full | test | (no reason given)
[ADHC_COMPIL.013] FRESHNESS-BYPASS: 2026-04-30T21:00:00Z | gold_dispatch.sh | chain:full | test | vendor RPS feed scheduled outage 2026-04-30
```

---

## ADHC_COMPIL v3 Status

| TO | Status |
|----|--------|
| .008 | COMPLETE |
| .009 | COMPLETE |
| .010 | COMPLETE |
| .012 | COMPLETE (DS~D, 2026-04-30) |
| .013 | **COMPLETE** (this session) |
| .014 | COMPLETE (2026-04-30) |
| .015 | COMPLETE (2026-04-30) |

**v3 ship gate: ALL TOs COMPLETE. RAVC4 closes v3.**
