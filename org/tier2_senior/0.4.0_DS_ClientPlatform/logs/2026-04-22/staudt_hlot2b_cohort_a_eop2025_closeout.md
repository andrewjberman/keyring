# STAUDT Closeout: HLOT2b + COHORT-A + EOP2025
**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-22
**Session scope:** ADVI_STAUDT ~B lane — three TOs closed

---

## HLOT2b (ADVI_STAUDT.HLOT2b) — P1 Bug Fix

**Status at session start:** TO complete (commit `74dbad2b`, TO flipped `cab84b77`).
**This session:** Confirmed closure per prior MCP/RAVC3 chain.

Key evidence (from SSM 87227091, `--chain full`, 2026-04-21):
```
[HLOT2 reopen] ticker->cusip enriched 79,704 of 85,156 rows via bd_assets_dim; 5,452 skipped
[HLOT2 reopen] 22,148 synth lots / 3,269 accts / MV=$220,793,554
tier1_unrl=21,426, tier2_canon=722; silent_close=7,631, overlap_topup=14,517
```

CTO RAVC3 (20260422T202650Z): Patch A 73% PASS; HLOT2b CLOSED on --from B_01 chain.
HLOT2 parent held for nightly 23:00Z.

---

## COHORT-A (CP-DS1 PIVOT 5, D_04 cohort_a_summary) — P2

**Status:** Already complete per CP-DS1 PIVOT 2/5 (D_04 commit `3cf43c26`, chain evidence from AE SSM 87227091).
cohort_a_summary.json on S3 as of 2026-04-22T17:25:07Z:
- account_count: 442, total_aua: $57,640,936.85, client_count: 328, snapshot_date: 2026-04-20
- comp-validate: 6 PASS, 0 ERROR, 2 WARN (benign scalar-path type-mismatch, same as CP-WP5)
- COO RAVC4 (20260422T200908Z): CP-WP5 complete, cohort_a_summary evidence validated

---

## EOP2025 (ADVI_STAUDT.EOP2025) — P3 Diagnostic

**Status:** COMPLETE. Commit `70788788`, pushed CLOUD.

### Investigation summary

Original briefing delta: $1,446M (timeseries_chart) vs $1,478M (canonical_nna raw) = $32M.

Post-AUAGAP.002 (chain 2026-04-22 16:27-17:25Z UTC), both surfaces refreshed:
- timeseries_chart Dec 2025: $1,448,134,643 (S3 timestamp 17:01Z)
- canonical_nna/2025-12-31 raw: $1,473,035,605 (S3 timestamp 16:44Z)
- Current gap: $24,900,962

### Root cause: 164 null-relationship_id accounts

```
canonical_nna raw (account grain):    $1,473,035,605   5,905 accounts
  164 accounts have relationship_id = NaN:
    156 bd source                     $22,149,370
      7 schwab_imputed                 $2,751,592
      1 bd_diff_flagged                       $0
  Subtotal null-rel-id:               $24,900,962

D_00b groupby(['date','relationship_id']) silently drops NaN keys
  -> 2,757 relationships survive      $1,448,134,643  <- timeseries_chart
```

D_00b exact replication confirmed: snap date = 2025-12-31, groupby drop = 146 null-rel accounts, NMNC+NMEC = $1,448,134,643 = exact match to timeseries_chart.json.

### Hypothesis disposition

| Hypothesis | Result |
|---|---|
| H1: cohort-scope (null-rel-id exclusion) | CONFIRMED |
| H2: date-boundary (snap to wrong date) | RULED OUT — snap correctly to 2025-12-31 |
| H3: aggregation flag filter | RULED OUT — no such filter in code |
| H4: source-of-truth difference | PARTIAL — C_01 reads gains directly (no dim join); D_00b does groupby which drops nulls |
| H5: staleness | WAS a factor for old $32M gap; NOW RESOLVED post AUAGAP.002 |

### BD silver comparison
`silver/allocations/2025-12-31.parquet`: NOT FOUND. Earliest available: 2026-01-16. No anchor.

### Canonical recommendation
`canonical_nna.aua_current` ($1,473M) is the correct EOP 2025 firm AUA.
`timeseries_chart` ($1,448M) understated by $24.9M — mechanical exclusion, not policy.

### Proposed fix
Option A: D_00b `_load_perf()` line 1279:
```python
# Before
agg = ap.groupby(['date', 'relationship_id']).agg(...)
# After
agg = ap.groupby(['date', 'relationship_id'], dropna=False).agg(...)
```
One-line fix, zero risk. Raises timeseries NMNC+NMEC at 2025-12-31 to $1,473M.
Separate upstream TO recommended to assign relationship_ids to 164 orphan accounts.

### Deliverable
`data/black_diamond/diagnostics/STAUDT/EOP2025/cohort_delta_trace.md` — all ACs met.

---

## MCP Status

COO MCP queued with HLOT2b close + EOP2025 brief + fix recommendation.
