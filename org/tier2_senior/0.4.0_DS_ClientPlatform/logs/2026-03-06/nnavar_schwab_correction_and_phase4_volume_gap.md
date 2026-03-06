# ADVI_NNAVAR: Schwab Vector Correction Review + Phase 4 Volume Gap Design — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 21:30
**End Time:** 22:55

## Objective

Review DT's Schwab vector correction findings (commit `45162cc9`), accept or reject the
corrected metrics, fix SCHWAB_NNA in 3 remaining diagnostic scripts, design and commit
Phase 4 `diag_nnavar_volume_gap.py` targeting the -$119M total volume gap.

---

## Work Completed

### 1. DT Schwab Vector Correction — Review and Acceptance

DT found that all diagnostic scripts (Phases 1-3) used a reversed SCHWAB_NNA dict.
PDF text extraction pulled bar chart values right-to-left (newest → oldest), causing
each month's value to be stored 12 positions from its actual key. Total sum was
approximately correct ($353M script vs $354.6M actual — rounding difference only), so
`total_gap` metrics were approximately valid. All shape-based metrics (pearson_r,
sign_agreement) were computed against a mirror-image ground truth.

**Corrected SCHWAB_NNA** (sourced from PDF page 3, 49 Financial May 2025 dashboard):

| Month | Correct | Was (reversed) |
|-------|---------|----------------|
| 2024-05 | $10.4M | $21.0M |
| 2024-06 | $46.3M | $9.0M |
| 2024-07 | $28.2M | $29.0M |
| 2024-08 | $9.5M | $22.0M |
| 2024-09 | $7.4M | $44.0M |
| 2024-10 | $46.3M | $64.0M |
| 2024-11 | $17.9M | $18.0M |
| 2024-12 | $64.3M | $46.0M |
| 2025-01 | $44.0M | $7.0M |
| 2025-02 | $21.8M | $9.0M |
| 2025-03 | $29.0M | $28.0M |
| 2025-04 | $8.9M | $46.0M |
| 2025-05 | $20.6M | $10.0M |

**Corrected metrics (accepted from DT's local recompute, verified plausible):**

| Phase | Best variant | pearson_r (was) | pearson_r (corrected) | sign_agr |
|-------|-------------|-----------------|----------------------|----------|
| Baseline | prod caps | 0.175 | **0.329** | 10/13 |
| Phase 2 best | vel_w120_t1p00 | 0.111 (dismissed) | **0.448** | 13/13 |
| Phase 2 prev "best" | comb_aua1p5_w120t2p00 | 0.271 | 0.141 | 10/13 |
| Phase 3 no-transfers | ef_no_transfers | 0.386 | 0.452 | 7/13 |
| Phase 3b timing | N=-30 (day shift) | N/A | **0.726** | 12/13 |

**Key reversal impact:**
- vel_w120_t1p00 (previously dismissed at 0.111) is now the best single cap config at 0.448
- All "combo" variants that were the Phase 2 leaders are now worse than velocity-only
- PRD target (r≥0.50) is achievable with timing adjustment (r=0.726 at N=-30), but that path
  is closed per Andrew's methodology decision (use settlement date as-is)
- Best deployable cap config remains vel_w120_t1p00 (r=0.448, 13/13) — not vel_w120_t2p00

**Methodology decision (Andrew/Yang):** Use BD settlement date. BD-specific and defensible.
Timing gap vs Schwab is explainable by methodology, not data quality.

**Investigation ceiling (revised):**
- Deployable (cap tuning only): r=0.448
- PRD target (r≥0.50): reachable only with timing shift, which is closed
- PRD target reassessment needed

### 2. SCHWAB_NNA Fixes — 3 Remaining Scripts

Fixed reversed constants in:
- `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py`
- `data/black_diamond/scripts/diagnostics/diag_nnavar_cap_tuning.py`
- `data/black_diamond/scripts/diagnostics/diag_nnavar_structural.py`

diag_nnavar_timing_shift.py was already fixed by DT at `18e898e4`. All 4 scripts are now
consistent with the corrected PDF source.

**Note:** `diag_acat_param_grid.py` and `diag_acat_correlation_summary.py` also contain the
old reversed SCHWAB_NNA. These are ACAT diagnostic scripts, not NNAVAR. Not touched in this
session — flag to COO for a separate ACAT fix task if those scripts will be re-run.

### 3. Phase 4 Volume Gap Script — Design and Implementation

**Script:** `data/black_diamond/scripts/diagnostics/diag_nnavar_volume_gap.py`
**Brief:** `docs/briefs/devops-brief-nnavar-volume-gap-ec2-run.md`
**Commit:** `477784c2`

**Hypothesis:** The -$119M total gap is a volume classification problem, not a timing problem.
The original silver NNA logic (`BD_TRANSACTIONS_DATA_SUMMARY.md`) listed `Wire In`, `Transfer`
(broad), and `Wire Out` as NNA types. Production script 05 only uses `Cash Deposit`, `Transfer In`,
`Cash Withdrawal`, `Transfer Out`. If `Wire In` / `Wire Out` were dropped when the silver
architecture was restructured and they carry material volume, this directly explains the gap.

Three suites:

**`taxonomy` (~5-10 min, gates everything else):**
- Full audit of every transaction_type in silver/transactions/ for the 13-month window
- Per type: row count, gross positive/negative market_value, net, classification
  (prod_inflow / prod_outflow / candidate_inflow / candidate_outflow / excluded)
- Outputs: `txn_type_taxonomy.csv`, `taxonomy_summary.json`
- Key flag: `type_extension_warranted` — true if any candidate type has >$1M gross volume
- Also prints complete type landscape to stdout (share with DS/COO)

**`sign_audit` (~2-5 min):**
- Checks sign-convention consistency on production NNA types
- Quantifies: how many Cash Deposit / Transfer In rows have negative market_value,
  and how many Cash Withdrawal / Transfer Out rows have positive market_value
- Script 05 uses abs() so wrong-sign rows count toward the wrong direction
- `total_wrong_sign_exposure_dollars` quantifies dollar exposure
- Can run in parallel with type_extension

**`type_extension` (~30-60 min, conditional on taxonomy):**
- Builds variants for each material candidate type found in taxonomy
- Base: production (Cash Deposit + Transfer In / Cash Withdrawal + Transfer Out)
- Incremental: `plus_wire_in`, `plus_wire_out`, `plus_all_candidates`
- Isolation: `cash_only` (Cash Deposit/Withdrawal only — confirms Transfer contribution)
- Production caps throughout (vel_w90_t1p00 as base for production comparability)
- Outputs: `summary.csv` with pearson_r, sign_agr, total_gap per variant

**Key design decisions:**
- `taxonomy` runs first and always; gates `type_extension` automatically
- If `type_extension_warranted=false` (no Wire In / Wire Out in data): investigation
  closes the type-extension hypothesis and COO must decide whether to pursue BI data pull
- Production caps (vel_w90_t1p00) used in type_extension to make gap directly comparable
  to production; vel_w120_t1p00 (best corrected config) reserved for a production rebuild
- Safety rail: DIAG_PREFIX constant; all writes to diagnostics/nnavar_volume_gap/ only

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix SCHWAB_NNA in all 3 scripts now (not when re-run) | Scripts are committed artifacts. Incorrect constants in committed code are a correctness risk. Fix before DT uses them again. |
| Use vel_w90_t1p00 (production) as base for type_extension | Goal is to measure gap vs production. Using best corrected config would make the base gap smaller and mask the true production gap being investigated. |
| Include `cash_only` variant | Confirms dollar contribution of Transfer rows. If cash_only gap >> production gap, Transfer types are adding inflows we shouldn't count. If cash_only gap << production gap, Transfer types are net beneficial. |
| Include `sign_audit` as separate suite | Sign errors are cheap to detect and could explain part of the gap without requiring type additions. |
| Do NOT fix diag_acat_* scripts in this commit | Out of scope for NNAVAR work. Separate flag to COO. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Phase 4 EC2 execution brief | `docs/briefs/devops-brief-nnavar-volume-gap-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py` | Fix SCHWAB_NNA (reversed → correct) | Yes — `477784c2` |
| `data/black_diamond/scripts/diagnostics/diag_nnavar_cap_tuning.py` | Fix SCHWAB_NNA | Yes — `477784c2` |
| `data/black_diamond/scripts/diagnostics/diag_nnavar_structural.py` | Fix SCHWAB_NNA | Yes — `477784c2` |
| `data/black_diamond/scripts/diagnostics/diag_nnavar_volume_gap.py` | New — Phase 4 volume gap diagnostic (3 suites) | Yes — `477784c2` |
| `docs/briefs/devops-brief-nnavar-volume-gap-ec2-run.md` | New — DT brief for Phase 4 EC2 run | Yes — `477784c2` |

---

## Blockers

None. DT unblocked to run Phase 4.

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

SCHWAB_NNA corrected in all 4 NNAVAR diagnostic scripts (`477784c2`). Phase 4
`diag_nnavar_volume_gap.py` committed and ready for DT to run. The investigation now targets
the -$119M total volume gap independent of timing. Primary hypothesis: Wire In / Wire Out
transaction types present in original silver NNA logic were dropped from production script 05.
Taxonomy suite gates the investigation — if no material Wire In/Out volume exists, the
type-extension hypothesis is closed and COO decides next steps (BI data pull or close).

Revised cap recommendation (corrected Schwab vector): vel_w120_t1p00 is now the best
deployable cap config (r=0.448, 13/13), not the previously recommended aua_t1p50+vel_w120_t2p00.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Run `taxonomy` suite** per
   `docs/briefs/devops-brief-nnavar-volume-gap-ec2-run.md` — share `txn_type_taxonomy.csv`
   and `taxonomy_summary.json` with DS before proceeding

2. **[0.4.0_DT_ClientPlatform] Run `sign_audit` suite** — can run in parallel with taxonomy
   or immediately after; share `sign_mismatches.csv` with DS

3. **[0.4.0_DT_ClientPlatform] Run `type_extension` suite** if `type_extension_warranted=true`
   — share `summary.csv` with DS/COO

4. **[DS — this agent] Analyze Phase 4 results** — if Wire In / Wire Out have material volume
   and closing the gap, recommend adding them to production INFLOW/OUTFLOW_TYPES in script 05

5. **[2.0.0_SA_COO] Revise cap recommendation** — best single deployable config is now
   vel_w120_t1p00 (r=0.448, 13/13), NOT aua_t1p50+vel_w120_t2p00 (r=0.141 corrected).
   COO memo `docs/briefs/coo-memo-nnavar-investigation-complete.md` needs a correction note.

**Files to touch next (DS):**
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-06/` — Phase 4 results analysis
  log (after DT returns taxonomy + type_extension results)

**Do NOT:**
- Deploy any NNA type changes to production script 05 before Phase 4 results analyzed
- Fix diag_acat_param_grid.py SCHWAB_NNA without a separate ACAT-scoped task
- Push any commits (DT handles all pushes)
- Use aua_t1p50+vel_w120_t2p00 as the cap recommendation — it scores 0.141 corrected,
  not 0.271 as previously documented
