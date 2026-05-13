# Bug B Silver-Empty-Partition Trace — Discovery Brief

**Author:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-13
**Audience:** 2.0.0_SA_COO, 0.6.1_AE_PartnerETL, 0.7.0_AE_CloudOps
**Status:** Root cause located. Fix-it AE-lane (silver runner orchestration + producer fail-loud insertion).

## TL;DR

`silver/api_dims/accounts_v2/snapshot_date=2026-05-13/data.parquet` emitted **0 rows** (21KB schema-only parquet). Same defect on **2026-05-08** (also 0 rows). Yesterday and other days populate normally at ~78KB / 857 rows.

Root cause is a **silent fallback** in `build_accounts_v2()` at `data/orion/scripts/silver/convert_orion_api_to_silver.py:466-467`. When the local `_household_rep_mapping.json` bronze JSON is absent at silver-build time, the function silently sets all `rep_id` to `pd.NA`, then the downstream `rep_id.isin(INFLECTION_REP_IDS)` filter at line 474 drops every row. No exception, no WARN, no fail-loud. The 0-row DataFrame is then happily written to S3.

Layer audit: the `apply_aua_guard()` safety net that previously would have caught this was **retired as a no-op on 2026-05-08** per Andrew directive (line 286-299) — exactly when this empty-partition pattern started showing up. Causal coincidence is strong.

## Empirical signature

```
2026-05-07: 77906 bytes  (normal — populated)
2026-05-08: 21032 bytes  (EMPTY — 0 rows, 45 cols)     <- prior incident
2026-05-09: 77974 bytes  (normal)
2026-05-10: 77974 bytes  (normal)
2026-05-11: 77958 bytes  (normal)
2026-05-12: 78604 bytes  (normal — 857 rows, 45 cols)
2026-05-13: 21030 bytes  (EMPTY — 0 rows, 45 cols)     <- today's defect
```

~21KB is the schema-only-no-rows signature. ~78KB is populated.

## Trace

### Step 1: Bronze is healthy

`s3://opal-data-inf/bronze/orion-api/2026-05-13/new_portfolio_accounts.json` exists (5.5MB, written 08:45Z). Contains **2916 rows** total across multiple custodians:

| Custodian | Row count |
|---|---|
| Fidelity_LH | 1383 |
| Fidelity_Inflection | 846 |
| Fidelity_Keil | 678 |
| Schwab | 5 |
| Nationwide | 4 |

`_BRONZE_COMPLETE.json` reports `accounts_v2 status=ok exit_code=0` (no row count emitted by bronze pull, separate gap).

### Step 2: Custodian filter is healthy

`inf_df = df[df['custodian'].isin(['Fidelity_Inflection', 'Fidelity_LH'])]` retains **2229 rows** today. So the custodian filter at line 383-384 is not the cause.

### Step 3: rep_id silent fallback is the cause

```python
# convert_orion_api_to_silver.py:452-467
rep_map_path = HOUSEHOLD_REP_LOCAL_BRONZE_PATH_TPL.format(snap=snapshot_date.isoformat())
if os.path.exists(rep_map_path):
    rep_map = build_household_rep_mapping(snapshot_date)[...]
    # ... merge + override representative_name ...
else:
    out['rep_id'] = pd.array([pd.NA] * len(out), dtype='Int64')   # <-- SILENT FALLBACK
```

When the local file is absent, every `rep_id` becomes NA. Then 22 lines later:

```python
# convert_orion_api_to_silver.py:474
out = out[out['rep_id'].isin(INFLECTION_REP_IDS)].copy()
```

`NA.isin({1, 2, 3, ...})` is `False` for every row → 0 rows survive → empty silver partition.

### Step 4: Layered safety nets all neutered

- **`apply_aua_guard()`** at line 286-299 of `_orion_api_silver_lib.py` is a **no-op**:
  ```python
  def apply_aua_guard(df, value_col, source_desc) -> None:
      """No-op — Guard B retired per Andrew directive 2026-05-08T~13:48Z."""
      total = df[value_col].sum() if value_col in df.columns else 0.0
      print(f"  AUA observed [{source_desc}]: ${total:,.0f} ({len(df)} rows; Guard B retired)")
  ```
  Was previously a hard $150M-$300M sanity band that would have flagged a 0-row $0-AUA partition. Retired 2026-05-08 — same date as the first empty-partition incident.

- **Orchestrator `main()`** at line 908-918 has no `len(df) == 0` post-builder check. Silently writes empty parquet:
  ```python
  for dim in dims:
      builder = DIM_BUILDERS[dim]
      try:
          df = builder(snapshot_date)
      except Exception as e:
          print(f"DIM {dim}: BUILD FAILED -- {e}")
          continue
      # ... write_silver_api_dim_parquet(df, ...)  <-- no len(df) gate
  ```

- **`write_silver_api_dim_parquet()`** at `_orion_api_silver_lib.py:327-350` writes any DataFrame, empty or not.

So the architectural posture today is: a missing local rep_map JSON silently produces a 0-row silver partition that propagates downstream unfiltered.

### Step 5: Why rep_map is missing — AE-lane

`silver/api_dims/household_rep_mapping/snapshot_date=2026-05-13/data.parquet` exists in S3 (310 rows, written 12:30:48Z — **20 min BEFORE** accounts_v2 silver write at 12:50:55Z). So household_rep_mapping silver build succeeded somewhere.

But `build_accounts_v2()` reads the LOCAL JSON path (`HOUSEHOLD_REP_LOCAL_BRONZE_PATH_TPL` = `{LOCAL_BRONZE_API_DIR}/{snap}_household_rep_mapping.json`), NOT the S3 silver parquet. If accounts_v2 builds on a different runner instance or the local file wasn't synced before this build's process started, the gate fires and the silent fallback executes.

Likely AE root cause hypotheses (cannot disambiguate from DS lane):
1. Orchestration calls `convert_orion_api_to_silver.py --dim accounts_v2` as a separate process from `--dim household_rep_mapping`, and the rep_map local JSON isn't downloaded/staged before the accounts_v2 process starts.
2. INF_PREFER_S3=true is set on Lambda but `build_household_rep_mapping` does NOT honor that flag — it reads `LOCAL_BRONZE_API_DIR` unconditionally (line 602-608). The `--dim accounts_v2` invocation never triggers the S3 download path for rep_map bronze.
3. The bronze pull for `_household_rep_mapping.json` and `_representatives.json` is not part of the standard bronze sync — `_BRONZE_COMPLETE.json` doesn't enumerate them, suggesting they live outside the canonical bronze prefix and are pulled by a separate manual script (`pull_inflection_representatives.py` per the FileNotFoundError message at line 605-607).

## Sub-issue (b) — gold dim staleness (842 vs 857 vs 861)

RD reported: `gold/dimensions/accounts_dimension_latest.parquet` shows **842 rows** while yesterday's silver was **857** and today's `account_team` (INF_C_07 output) is **861**. New accounts not propagating.

This is consistent with the silver-empty-partition cause:
- Today's accounts_v2 silver = 0 rows → cannot use today's silver as gold input.
- Gold builder presumably walks back to a prior populated silver (similar to DS~C's INF_C_07 walkback fix `90306935b` / `f948658e6` this session).
- The walkback hit some earlier-than-yesterday date, hence 842 < 857. Need to confirm by reading the gold producer's date-pick logic.

**Recommendation:** verify after silver-fix lands; once today's accounts_v2 silver is populated again, gold/dimensions should propagate to 861+.

## Sub-issue (c) — new account_ids 4268, 4269

If they appear in today's bronze `new_portfolio_accounts.json` (need to confirm), they're blocked by the same silent fallback — every row including theirs gets dropped when `rep_id` is NA. Once Step 3 is fixed (rep_map populated correctly), 4268/4269 will surface naturally — provided their household_ids appear in the rep_map.

## Recommended fix (AE lane, ranked by structural impact)

### A. PRIMARY — Replace silent fallback with fail-loud (build_accounts_v2:466-467)

```python
# BEFORE
else:
    out['rep_id'] = pd.array([pd.NA] * len(out), dtype='Int64')

# AFTER
else:
    raise FileNotFoundError(
        f"build_accounts_v2 requires local rep_map JSON at {rep_map_path}; "
        f"either run `pull_inflection_representatives.py --date {snapshot_date.isoformat()} "
        f"--upload-bronze` to populate it, or sync from "
        f"s3://opal-data-inf/silver/api_dims/household_rep_mapping/"
        f"snapshot_date={snapshot_date.isoformat()}/ to the local cache before this build."
    )
```

Same posture as `build_household_rep_mapping` itself (line 603-608). Symmetric fail-loud across siblings.

### B. SECONDARY — Orchestrator len-check (main:911-918)

```python
df = builder(snapshot_date)

# Universal empty-emit guard (CLAUDE.md fail-loud-at-source posture)
MIN_ROWS_BY_DIM = {
    'accounts_v2': 500,           # canonical ~800-860 range
    'household': 100,             # canonical ~300+
    'performance': 1000,          # canonical
    'household_rep_mapping': 50,  # canonical ~300+
    # ... per-dim sensible floors ...
}
floor = MIN_ROWS_BY_DIM.get(dim, 1)
if len(df) < floor:
    raise ValueError(
        f"DIM {dim} produced {len(df)} rows; floor={floor}. "
        f"Refusing to write under-populated silver partition (fail-loud at source)."
    )
```

### C. TERTIARY — Reinstate or replace `apply_aua_guard` with row-count guard

Andrew retired the AUA hard band as "vestigial guardrail not logical." Fair. But the function is still called in every builder and could carry a **row-count or AUA-zero** guard cheaply. Suggested minimal replacement:

```python
def apply_aua_guard(df, value_col, source_desc) -> None:
    total = df[value_col].sum() if value_col in df.columns else 0.0
    print(f"  AUA observed [{source_desc}]: ${total:,.0f} ({len(df)} rows)")
    if len(df) == 0 or total == 0.0:
        raise ValueError(
            f"silver fail-loud: {source_desc} produced {len(df)} rows / ${total:,.0f} AUA. "
            f"Likely a missing-bronze or filter-cascade defect upstream. Aborting."
        )
```

Andrew rejected the hard-$$$ band but a zero-row / zero-AUA tripwire is unambiguously useful.

### D. ORTHOGONAL — Source bronze gap (separate AE TO)

`_BRONZE_COMPLETE.json` doesn't enumerate `_household_rep_mapping.json` or `_representatives.json`. They're pulled by `pull_inflection_representatives.py` (per the FileNotFoundError msg at line 604-608), which is presumably outside the canonical bronze orchestrator. Two options:

1. Fold the rep_map pull into the canonical bronze orchestrator so `_BRONZE_COMPLETE.json` reports its status.
2. Make `build_household_rep_mapping` honor INF_PREFER_S3 — read from `silver/api_dims/household_rep_mapping/snapshot_date={date}/data.parquet` (which DOES exist for today) as a structural fallback.

Option 2 is cleaner (silver build can self-recover from a missed bronze pull). Option 1 is more architecturally consistent (everything goes through one orchestrator).

## Compiler tools

Comp-pipescript catalog for INF silver doesn't exist (gap documented in prior sessions). Trace was done via `grep` + bronze/silver S3 inspection + git log -L (for blame on the silent fallback insertion). Author trace context:
- Silent fallback at line 466-467 introduced commit `72628a1df` "feat(ADVI_INFLEC.DIAGFIX.011): advisor attribution fix — Brandenburg + servicing rep population" — when the rep_map override path was added. Probably intended as a graceful degrade for the override-only path, but the failure cascade through the rep_id filter at line 474 wasn't considered.

## Effort estimate

A + B = ~1h AE implementation + ds-commit-gate + S3 deploy + silver re-run for 2026-05-13 partition (manual SSM dispatch to silver runner).

D (orthogonal) = TBD AE-architectural, separate TO.

## Coordination

AE 0.6.1 / 0.7 — pick up Fix A + B in your domain. I can ship A as a DS lane fix if you prefer (single-file silver edit), but the silver runner SSM dispatch + retroactive 2026-05-13 partition rebuild is AE-lane.

DS~B exits this discovery with the brief delivered. Standing by for fix sequencing direction.

— 0.4.0_DS_ClientPlatform~B 2026-05-13
