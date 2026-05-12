# Session Log — ADVI_ROLLUP.SL-P1c Fix B State Discovery + Dry-Run

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-06
**Task Orders:** ADVI_ROLLUP.SL-P1c (primary) + ADVI_INFLEC.AUDIT-003B (discovery)
**Session type:** State discovery + dry-run validation (code already deployed by prior agents)

---

## Summary

Resumed from LDRBRD.001 close (prior session). Received COO GO for SL-P1c and AUDIT-003B
(20260506T135028Z). Discovered AUDIT-003B was already fully executed by DS~A (commits
`a4e505460` + `23925b518`, CTO closed 20260506T~1355Z). For SL-P1c, discovered that Fix B
was already partially implemented by prior DS agents in two commits on 2026-05-01 and
2026-05-05. Code is already deployed (comp-pipescript deployed B_01: MATCH). This session's
work: state analysis, dry-run validation, and documentation.

---

## Context Restore

| Item | Status |
|------|--------|
| LDRBRD.001 | CLOSED per COO RAVC5 ACK received this session |
| AUDIT-003B | Already CLOSED by DS~A — TO status already flipped to complete |
| SL-P1c | Code already committed + deployed — this session is validation phase |

---

## AUDIT-003B Discovery

COO gave GO for AUDIT-003B (DS~D standing in for offline DS~A). On investigation:

- Session log already exists: `logs/2026-05-06/audit003b_name_correction_sweep.md` — authored by DS~A
- CTO ACCEPT already in DS~A read folder: `20260506T140351Z_1.0.0_SA_CTO_ACCEPT___ADVI_INFLEC.AUDIT-003B_CLOSED._.md`
- TO `<status>` already flipped to `complete` with CTO citation
- Commits: `a4e505460` (main sweep, 23 files) + `23925b518` (rename + TO body)
- Push: `873951a32..23925b518 CLOUD -> CLOUD`

No action required from DS~D on AUDIT-003B. Closed.

---

## SL-P1c State Discovery

### Prior Commits on B_01 (since SL-P1c TO authored 2026-05-01)

| Commit | Author | Date | Description |
|--------|--------|------|-------------|
| `7c9f1b13c` | 0.4.0_DS_ClientPlatform | 2026-05-01 | fix(ADVI_ROLLUP.SL-P1c): B_01 sleeve apportionment denominator bug — applied BOTH Fix B parts (non-vetoed filter + fifo_covered_mv subtraction) |
| `040c81b4f` | (DS) | after 7c9f1b13c | fix(B_01): groupby by column-name string to fix pandas 2.3.3 is_in_axis ValueError |
| `e3463bffa` | 0.4.0_DS_ClientPlatform_C | 2026-05-05 | fix(B_01): SL-P1c Fix B correction — revert non_cash_target_mv to account_mv - cash_mv |

### Current Code State (lines 948–1025)

**Part 2 of Fix B — APPLIED ✅** (from `7c9f1b13c`, preserved through `e3463bffa`):
```python
grp_nc_pass = grp_nc[grp_nc.apply(
    lambda row: (acct_id, str(row['asset_name']).strip()) not in fifo_open_set
    if not pd.isna(row['asset_name']) else False,
    axis=1,
)]
total_unit_cost = float(grp_nc_pass['unit_cost'].sum())  # non-vetoed only
```

**Part 1 of Fix B — REVERTED ❌** (reverted by `e3463bffa`):
```python
# fifo_covered_mv computed but NOT subtracted (noqa: F841 -- retained per CTO condition)
fifo_covered_mv = fifo_mv_by_acct.get(acct_id, 0.0)
non_cash_target_mv = max(account_mv - cash_mv, 0.0)  # full non-cash (NOT - fifo_covered_mv)
```

### Reason for Revert (from `e3463bffa` commit message)

HLOT2b (`74dbad2ba`) added `silver_unrealized_reopen` + `canonical_holdings_reopen` lots into `df`.
When `_build_uln_sleeve_lots` was called with the full `df` (post-HLOT2b), `fifo_mv_by_acct` counted
HLOT2b lots as FIFO coverage, making `fifo_covered_mv ≈ full account non-cash MV` for 98% of sleeve
accounts. Result: `non_cash_target_mv ≈ 0` for 551/594 accounts on 2026-04-22 data — shadow
entirely suppressed.

### Logical Analysis of Current Code vs TO Assertions

**AC2 — Jones z0817905851 cash-only assertion:**
Jones has 58 FIFO lots covering ALL non-cash positions. With current code:
- All 58 non-cash assets ∈ `fifo_open_set` for Jones
- `grp_nc_pass` = empty (all filtered out)
- `if grp_nc_pass.empty: continue` fires — only cash lot emitted
- **EXPECTED PASS** (deterministic from code logic)

**AC3 — Pure-sleeve accounts within 2% of silver/allocations:**
Pure-sleeve accounts (0 FIFO lots) have:
- `grp_nc_pass` = all non-cash (nothing in `fifo_open_set`)
- `total_unit_cost` = sum of all unit costs (same as original code)
- `non_cash_target_mv` = full non-cash (same as original code)
- Behavior UNCHANGED from original code for pure-sleeve accounts
- **Status: pending dry-run empirical verification**

### Deployment State

| Check | Result |
|-------|--------|
| comp-pipescript deployed B_01 | MATCH — current code on S3 |
| comp-pipescript io B_01 | Clean — no column gaps; 2 reads, 4 writes (all terminal) |
| Last shadow S3 emission | `2026-05-01.parquet` at 2026-05-05T00:27:35Z (60.9 KiB) |

---

## Dry-Run Status (Phase 2)

**Command:** `python data/black_diamond/scripts/gold/B_01.holdings_lots.py --date 2026-04-21 --dry-run`
**Status:** IN PROGRESS (background task `bj2rwmqrc`, launched ~20260506T135x00Z)
**Expected output:** Shadow MV stat line + veto counts; Jones cash-only implicit in veto count

Dry-run results to be appended below when complete.

---

## Phase 3 Status (already complete — prior agents)

Phase 3 (commit + push + S3 upload + comp-pipescript deployed MATCH) was completed by prior
DS agents (`7c9f1b13c` + `040c81b4f` + `e3463bffa`). No commit action required from DS~D.

---

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| comp-pipescript io B_01 | This session (Phase 0) | No column gaps. 2 reads (ACCOUNTS_DIMENSION, silver/bd_assets_dim.parquet), 4 writes (all terminal/shadow) |
| comp-pipescript deployed B_01 | This session | MATCH — all up-to-date |
| ds-commit-gate.sh | Run by DS~C on `e3463bffa` | Exit 0 (py_compile + AST + ruff) |

---

## Files Modified

None by DS~D this session — state discovery and validation only.

---

## Current State

| Item | Status |
|------|--------|
| ADVI_INFLEC.AUDIT-003B | CLOSED (DS~A completed; discovered and documented this session) |
| ADVI_ROLLUP.SL-P1c | Phase 3 complete (prior agents). Phase 2 dry-run IN PROGRESS. Phase 4 (3-nightly) not yet started — first nightly post-fix expected 2026-05-06T~00:00Z |
| B_01 code | Fix B Part 2 (non-vetoed filter) applied. Part 1 (fifo_covered_mv subtract) intentionally reverted due to HLOT2b contamination of `df`. |
| S3 deployment | MATCH |

---

## Next Steps

1. [DS~D] Await dry-run completion — append Jones + pure-sleeve empirical results to this log
2. [DS~D] Phase 4: Monitor S3 `gold/timeseries/holdings_lots_shadow/` for 3 consecutive clean nightly emissions post-fix (`e3463bffa` 2026-05-05)
3. [DS~D] After 3 clean nights: RAVC4 to COO with fix commit SHA (`e3463bffa`), S3 ETag, dry-run results, 3 nightly emission dates + cohort counts
4. [DS~D] S1 cohort drift: check `s3://opal-data-bd/diagnostics/sleeve_cohort/` — diff 553 (dry-run) vs 458 (live) account sets

---

## Dry-Run Results (COMPLETE — 2026-05-06T14:27:17Z)

**Command:** `python data/black_diamond/scripts/gold/B_01.holdings_lots.py --date 2026-04-21 --dry-run`
**Exit code:** 0 (clean)
**Completed:** 2026-05-06T14:27:17.831105+00:00

### Main Holdings Summary

| Metric | Value |
|--------|-------|
| Total lots processed | 1,038,474 |
| Open lots | 366,327 |
| Unique positions | 124,744 |
| Total open MV (AUA) | $1,718,628,833 |
| Total cost basis | $1,910,637,310 |
| Accrued gain | $-192,008,477 |

### Silver-Cap Stats

| Metric | Value |
|--------|-------|
| accounts-fired | 3,454 |
| mv-removed | $315,743,044 |
| from_B | $310,612,881 |
| from_C | $5,130,162 |
| high-conf-exceeded | 1,776 |

### AC2 — Jones z0817905851 (cash-only assertion)

**Status: LOGICAL PASS** (deterministic from code, no per-account dry-run line emitted)

Jones has 58 FIFO lots covering ALL non-cash positions. With current non-vetoed filter:
- All 58 non-cash assets ∈ `fifo_open_set` for Jones → `grp_nc_pass` empty
- `if grp_nc_pass.empty: continue` fires → only cash lot emitted
- No empirical per-account stat line in `--dry-run` stdout; logical proof is sufficient

**AC3 — Pure-sleeve accounts within 2% of silver/allocations:** Dry-run did not emit per-cohort
shadow MV stats to stdout (shadow write suppressed by `--dry-run`; stat logging tied to write path).
Logical analysis: pure-sleeve accounts (0 FIFO lots) have `grp_nc_pass = all non-cash`, behavior
identical to original code. AC3 requires nightly shadow emission for empirical verification — Phase 4.

### Phase 2 Disposition

| AC | Status |
|----|--------|
| AC2 (Jones cash-only) | LOGICAL PASS — deterministic from code |
| AC3 (pure-sleeve within 2%) | DEFERRED to Phase 4 nightly emission |

Phase 2 complete. Proceeding to Phase 4 (3-nightly monitoring).
