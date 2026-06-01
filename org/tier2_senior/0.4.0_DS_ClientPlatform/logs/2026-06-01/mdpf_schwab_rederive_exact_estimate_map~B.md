# MDPF 49F Schwab re-derive — EXACT-vs-ESTIMATE MAP (DS~B, 2026-06-01)
PRE-EMIT deliverable per CTO HARD data-honesty gate (164xZ): surface which date-ranges/components are MEASURED vs ESTIMATED vs OLD-BASIS to CTO+Andrew BEFORE the re-derived series is emitted to the trend Andrew reads each morning. GO granted by COO; emit HELD pending this map's confirm.

## The map (49F, per region × component)
| Region | Dates | partner_custody_total | 1a (SmartX model) | 1c (SmartX SMA) | 1b (plug = cust−1a−1c) | CLASSIFICATION |
|---|---|---|---|---|---|---|
| **RE-DERIVE** | 2026-01-16 → 5/17 | **MEASURED/EXACT** — Schwab-restricted from BD `silver/allocations` per-account + stable `silver/fees` custodian crosswalk (empirical: 4/15 = $1,556.2M; 17 unmatched ~$5.9M) | **MEASURED** daily — SmartX daily exports (varies daily, e.g. 1/16 $1,155.0M) | **ESTIMATE** — bandaid weekly-interp, NO production SMA source historically (~$20-25M) | custody+1a EXACT, inherits the ~$25M 1c estimate | **Schwab-canonical; custody+1a MEASURED, 1c ESTIMATE (label)** |
| **LIVE** | 2026-05-18 → | MEASURED | MEASURED | MEASURED (live SmartX SMA) | MEASURED | fully measured |
| **PRE-RE-DERIVE** | 2024-11 → 2026-01-15 | **OLD-BASIS** (bandaid/v0.8; ~$1.37-1.41B, neither BD-full-book $1.83B nor Schwab $1.65B) | varies | ESTIMATE | OLD-BASIS | **NON-CANONICAL — flag boundary at 1/16; do NOT extend the Schwab line** |

Key honesty points:
- The dominant ~$140-180M correction (custody: BD-full-book → Schwab-restricted) is **MEASURED/EXACT** for 1/16-5/17.
- The only ESTIMATE inside the re-derived 1/16-5/17 series is the **~$25M 1c (SMA) bandaid term** → it propagates into 1b (and the FE-folded "other" line). Must carry an estimate marker.
- 1c transitions estimate (≤5/17) → measured (≥5/18 live) — a sub-seam within 1c, small but flag it.
- pre-1/16 is NON-CANONICAL old-basis — a labeled boundary at 1/16, never a smooth Schwab line back through history.

## Provenance-flag design (FE-readable; coordinate render with RD~B)
Per re-emitted partition + rollup meta:
- 1/16-5/17: `basis_tag="schwab_canonical_rederived"`, `cohort_provenance={custody:"measured_schwab", model_1a:"measured_smartx_daily", sma_1c:"estimate_bandaid"}`.
- pre-1/16: `basis_tag="black_diamond_legacy_non_canonical"`, `note="not re-derivable (no silver/allocations pre-2026-01-16); old basis — do NOT present as Schwab-canonical"`.
- Rollup meta: `basis_boundary_date="2026-01-16"` + a provenance legend so RD renders: solid Schwab line ≥1/16 (with a 1c-estimate marker/footnote on the folded "other" line for the ≤5/17 estimated-SMA portion), an annotated break at 1/16, dashed/annotated <1/16 legacy.

## What the re-derive does NOT change
1a (measured) and 1c (bandaid estimate) values stay AS-IS; the re-derive recomputes `partner_custody_total` (Schwab-restricted, exact) and thus `1b = custody − 1a − 1c` for 1/16-5/17. Total_aua and the global headline re-aggregate as a consequence. Inflection unaffected.

## DE serving-AC alignment (the verify target)
AC-S1 (49F non_model continuous across 5/18) — re-derive closes it from 1/16. AC-S2 = target the BASIS seam (v0_8→v0_9), patch bumps fine. AC-S4 = accept by_model 5-models-only pre-cutover (do NOT backfill estimated SMA sleeves into the donut/stack). AC-S5 = sma_aua stays additive-separate at data layer (FE folds).

## STATUS: emit HELD pending CTO+Andrew confirm of this map.
On confirm: build the re-derive (compute_partner_custody_total historical 1/16-5/17 + existing 1a + bandaid 1c → 1b; stamp provenance flags) → re-emit 49F partitions → aggregator + rollup → DE serving-verify + CVO independent verify → RAVC2. Full Rule 13 + ds-commit-gate.
