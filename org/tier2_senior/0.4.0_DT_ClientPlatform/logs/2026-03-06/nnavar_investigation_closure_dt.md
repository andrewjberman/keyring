# ADVI_NNAVAR Investigation Closure — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Status:** COMPLETE — All phases executed and closed.

---

## Summary of DT Execution Across All Phases

| Phase | Script | Suites Run | Key Result |
|-------|--------|-----------|------------|
| Phase 1 | `diag_nnavar_gap_decomposition.py` | baseline, exclusions, dedup, caps, timing, coverage | Velocity cap dominant lever; caps suite identified -$484M without AUA cap |
| Phase 2 | `diag_nnavar_cap_tuning.py` | aua, vel, combo | vel_w120_t1p00 is best clean config (corrected: r=0.448, 13/13) |
| Phase 3 | `diag_nnavar_structural.py` | schema, external_flow, settlement, bi_crossval | Settlement marginal; ef_no_transfers r=0.452 but sign fails; BI unavailable |
| Phase 3b | `diag_nnavar_timing_shift.py` | monthly_lag, day_shift | N=-30 transfer shift: r=0.726. VARIABLE TIMING (std=17.9d). Root cause: BD settlement vs Schwab initiation date |
| Schwab fix | Local recompute `.tmp_recompute.py` | All phases (from S3 CSVs) | SCHWAB_NNA was reversed in all scripts — metrics corrected without re-running EC2 |
| Phase 4 | `diag_nnavar_volume_gap.py` | taxonomy, sign_audit | No missing types; $0 wrong-sign exposure |
| Phase 5 | `diag_nnavar_phase5_transfer_out.py` | transfer_out_desc_audit | "Holding market value withdrawn" = $119.3M — matches gap exactly |
| Phase 5b | `diag_nnavar_phase5b_hmv_exclusion.py` | **CANCELLED** | Gap is correct behavior — no EC2 run needed |

---

## Script Bugs Fixed by DT (all authorized)

| Commit | Script | Bug |
|--------|--------|-----|
| `ba6cf82c` | `diag_nnavar_gap_decomposition.py` | `ACCOUNTS_DIM_KEY` wrong S3 path |
| `d08aef6d` | `diag_nnavar_gap_decomposition.py` | `map_relationships` column collision |
| `1094bb17` | `diag_nnavar_timing_shift.py` | `lag_months` float format code |
| `18e898e4` | `diag_nnavar_timing_shift.py` | SCHWAB_NNA reversed |

---

## The Definitive Finding

### Correlation gap (r=0.329 vs Schwab)

Caused by **BD recording Transfer In/Out at settlement date; Schwab booking TOA at
ACAT initiation date** — approximately 25-30 days earlier. Same money, different
calendar month attribution. Shifting Transfer flows back 30 days: r=0.726.
This exceeds the PRD target of 0.50.

Not an error — BD's settlement-date methodology is correct and defensible.
The lag is variable (std=17.9d) due to ACAT complexity varying by custodian and
transfer size. A fixed 30-day offset rule achieves r=0.726 but is imperfect.

### Volume gap (-$119M)

**"Holding market value withdrawn"** — 4,106 Transfer Out rows — $119.3M.

These are BD's accounting entries for client departures to other advisors who also
custody at Schwab. When a client fires 49F and moves to another Schwab-platform
advisor:
- 49F sees an outflow → BD records "Holding market value withdrawn" → **we correctly
  count this as NNA outflow for 49F**
- Schwab sees nothing — assets never left the platform → **Schwab correctly excludes
  this from their NNA** (Glossary: "Clients moving from existing Schwab platforms to
  an Advisor are not considered NNA" — same rule, opposite direction)

**This is not a bug. Both calculations are correct under their own definitions.**

| System | NNA definition |
|--------|---------------|
| 49F / BD | Flows into and out of 49F's managed AUM |
| Schwab | Flows into and out of the Schwab custodial platform |

The ~$119M gap will persist structurally and is not worth fixing.

---

## What Is Actionable: Production Bundle

The investigation has identified real improvements available for the NNA calculation.
All pending COO authorization and CEO go/no-go:

| Change | Corrected impact | Gate |
|--------|-----------------|------|
| Cap tuning: `vel_w120_t1p00` (window=120d, threshold=1.0×) | r: 0.329 → 0.448, sign_agr: 10/13 → 13/13 | COO rebuild authorization |
| Settlement date adjustment | sign_agr +1, gap -$1M | Same rebuild |
| JNL/sweep canonical fix | Cleaner flow exclusions | CEO go/no-go |
| ACAT params (DAYS=30, BURST=3, MIN=0) | +$45.98M gap reduction | CEO go/no-go |

**Note:** The previous "best" combo config (`aua_t1p50 + vel_w120_t2p00`) was based on
the reversed Schwab vector. The correct best config is `vel_w120_t1p00` alone.

---

## What Is NOT Actionable

- Adding "Holding market value withdrawn" to canonical exclusions — these are real
  outflows from 49F's perspective; excluding would overstate NNA
- Applying a fixed 30-day Transfer date offset in production — reduces r=0.726
  but std=17.9d means it's imprecise; also changes what NNA means for 49F
- Pursuing Phase 5b HMV exclusion verification — cancelled; the finding is resolved
  analytically

---

## Open Non-NNAVAR Item

`diag_acat_param_grid.py` and `diag_acat_correlation_summary.py` still have the
reversed SCHWAB_NNA constants. Out of scope for NNAVAR — requires a separate
ACAT task order.

---

## Files Modified This Session (all pushed to CLOUD)

| Commit | Change |
|--------|--------|
| `59143195` | Phase 1 session log + task order complete |
| `207416d1` | Phase 2 cap tuning session log |
| `1353cc67` | Phase 3 structural diagnostics session log |
| `60d71b56` | Phase 3b timing shift (original, wrong Schwab) |
| `45162cc9` | Schwab vector correction + timing root cause |
| `18e898e4` | Fix SCHWAB_NNA in timing_shift script |
| `7276c308` | Phase 4 volume gap session log |
| `cbe221f3` | Phase 5 desc_audit session log |
| This commit | DT investigation closure log |

---

## Current State

**Status: COMPLETE**
**Active branch:** `CLOUD`

ADVI_NNAVAR is fully closed. Both components of the gap are explained:
- Correlation gap (r=0.329): BD settlement date vs Schwab initiation date. Correctable
  to r=0.726 if desired but not required; production improvement to r=0.448 available
  via cap tuning without methodology change.
- Volume gap (-$119M): Correct behavior — client departures to other Schwab-platform
  advisors. Not a defect.

Production bundle (cap tuning + canonical + ACAT) pending COO/CEO authorization.
Investigation closed.
