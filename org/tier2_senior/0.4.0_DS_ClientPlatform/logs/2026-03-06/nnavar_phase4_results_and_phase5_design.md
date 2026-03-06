# ADVI_NNAVAR: Phase 4 Results + Phase 5 Transfer Out Design — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 22:55
**End Time:** 23:30

## Objective

Analyze Phase 4 volume gap diagnostic results (DT commit `7276c308`), interpret the clean
negative findings, and design Phase 5 targeting the intra-Schwab Transfer Out hypothesis
as the highest-probability remaining explanation for the -$119M volume gap.

---

## Work Completed

### 1. Phase 4 Results — Analysis

DT ran both Phase 4 suites (`diag_nnavar_volume_gap.py`, commit `477784c2`,
DT log `nnavar_volume_gap_phase4_ec2.md`).

**Taxonomy results:**

| Production NNA type | Rows | Gross volume |
|---------------------|------|-------------|
| Cash Deposit | 15,689 | +$369.1M |
| Transfer In | 13,375 | +$330.0M |
| Cash Withdrawal | 30,891 | -$15,529.3M |
| Transfer Out | 7,167 | -$193.2M |
| Candidate extra types | 0 | $0 |

`type_extension_warranted: false` — Wire In, Wire Out, and all other candidate types
are absent or immaterial (<$1M) in the Schwab window.

**Sign audit:** `total_wrong_sign_exposure_dollars: 0.0` — 100% correct signs across
all 4 production flow types.

**What this tells us about the data:**
- Cash Withdrawal gross ($15.5B) vs effective NNA is the phantom-outflow problem
  the AUA/velocity caps address. After vel_w90_t1p00 caps: gap = -$126.3M.
- The 4 production types are the complete universe of NNA-relevant transaction types.
- All values have correct sign conventions.
- The gap is not a code or data entry error.

**Conclusion from Phase 4:** The -$119M gap is a **structural definitional difference**
between how BD and Schwab define NNA. The transaction-level investigation path (types,
signs, caps) is exhausted.

---

### 2. Phase 5 Hypothesis — Transfer Out Intra-Schwab Exclusion

**Schwab Glossary source:** "Clients moving from existing Schwab platforms (Retail or
Advisor Services) to an Advisor are not considered NNA."

DT's hypothesis applies this to outflows: Transfer Out flows from 49F to another Schwab
platform (Schwab Bank, Schwab Retail, legacy TDA accounts) are excluded from Schwab's
NNA calculation but counted as outflows in our gold NNA.

**Direction check:**
- We count Transfer Out as negative NNA
- Schwab doesn't subtract intra-Schwab Transfer Outs from their NNA
- Our NNA = Schwab NNA - (intra-Schwab Transfer Out volume) → negative gap ✓

**Volume check (testable):**
- Transfer Out gross from Phase 4 taxonomy: $193.2M over 13 months
- Gap target: -$119M
- If intra-Schwab Transfer Outs = $119M → 61.5% of Transfer Out volume is intra-Schwab
- Mechanistically plausible: a significant fraction of ACAT transfers would be clients
  consolidating from Schwab retail/TDA to 49F Advisory, and when they leave 49F they
  may return to Schwab platforms

**How to test:** Transfer Out description field. BD records the destination/description
for each transfer. If descriptions include Schwab-platform identifiers (SCHWAB, TDA,
TDAMERITRADE, CHARLES SCHWAB, SCHWAB BANK), those rows are intra-Schwab candidates.

**Note on existing canonical exclusions:** Script 05 already excludes descriptions
containing `TRANSFER FUNDS TO SCHWAB BANK` — but that exclusion applies only to JNL-type
actions. Transfer Out type rows with the same or similar descriptions are NOT currently
excluded. The Phase 5 description audit will reveal whether any Transfer Out rows survive
canonical exclusions and still have Schwab-destination descriptions.

---

### 3. Phase 5 Script — Design and Implementation

**Script:** `data/black_diamond/scripts/diagnostics/diag_nnavar_phase5_transfer_out.py`
**Brief:** `docs/briefs/devops-brief-nnavar-phase5-transfer-out-ec2-run.md`
**Commit:** `d5a50311`

Two suites:

**`transfer_out_desc_audit` (~5-10 min):**
- Load Transfer Out rows (post canonical exclusions + dedup)
- Full description taxonomy: every unique description, row count, gross abs volume
- Keyword search: 9 Schwab-platform keywords (SCHWAB, TDA, TDAMERITRADE, etc.)
- Output: `transfer_out_descriptions.csv`, `audit_summary.json`
- Gate: `exclusion_warranted: true` if keyword-matched rows have >$10M volume
- DT shares `audit_summary.json` + descriptions CSV with DS before proceeding

**`transfer_out_exclusion` (~30-45 min, conditional):**
- Variants:
  - `base_prod` — production caps, all Transfer Out included
  - `excl_schwab_kw` — exclude Transfer Out rows with Schwab-platform description keywords
  - `excl_schwab_kw_best_cap` — same + vel_w120_t1p00 (corrected best cap)
  - `excl_all_transfer_out` — extreme bound: Cash Deposit/Withdrawal only
- Interpretation key: if `excl_schwab_kw` closes gap toward $0M, hypothesis confirmed

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Focus Phase 5 on Transfer Out descriptions | Transfer Out is the only flow type where intra-Schwab exclusion produces negative gap in the right direction. Transfer In exclusion would widen gap (Schwab counts fewer inflows → Schwab NNA lower → positive gap). |
| Include `excl_all_transfer_out` as extreme bound | If even total Transfer Out exclusion doesn't close the gap, the hypothesis is fully rejected and the gap is unexplainable with current data. |
| Include `excl_schwab_kw_best_cap` | Allows combining the type fix with the cap correction to see the ceiling with both improvements. |
| Gate `transfer_out_exclusion` on `exclusion_warranted` | If description field contains no Schwab keywords, running the exclusion variant returns the same result as base — wasted runtime. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Phase 5 EC2 execution brief | `docs/briefs/devops-brief-nnavar-phase5-transfer-out-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_phase5_transfer_out.py` | New — Phase 5 transfer_out investigation | Yes — `d5a50311` |
| `docs/briefs/devops-brief-nnavar-phase5-transfer-out-ec2-run.md` | New — DT brief for Phase 5 EC2 run | Yes — `d5a50311` |

---

## Blockers

None. DT unblocked to run Phase 5.

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Phase 4 confirmed the -$119M gap is a structural definitional difference, not a code or
data error. All 4 production transaction types are complete and sign-clean. Phase 5
(`diag_nnavar_phase5_transfer_out.py`, `d5a50311`) is committed and targets the
intra-Schwab Transfer Out exclusion hypothesis. Transfer Out gross = $193.2M; if $119M of
that (62%) is intra-Schwab and excluded from Schwab's NNA, the gap is explained.

**If Phase 5 desc_audit returns `exclusion_warranted: false`** (no Schwab keywords in
Transfer Out descriptions): the gap is unexplainable with current BD transaction data.
Investigation closes; COO decides whether to pursue Schwab-side data acquisition (glossary
definition audit, direct data from Schwab about their NNA exclusion rules).

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Run `transfer_out_desc_audit`** per
   `docs/briefs/devops-brief-nnavar-phase5-transfer-out-ec2-run.md` — share
   `audit_summary.json` + `transfer_out_descriptions.csv` + stdout with DS

2. **[0.4.0_DT_ClientPlatform] Run `transfer_out_exclusion`** if
   `exclusion_warranted: true` — share `summary.csv` with DS/COO

3. **[DS — this agent] Analyze Phase 5 results** — if `excl_schwab_kw` variant closes
   the gap to ~$0M: recommend adding Transfer Out Schwab-destination exclusion to
   production script 05 (similar to existing canonical exclusions pattern).

4. **[Separate task — ACAT]** `diag_acat_param_grid.py` and
   `diag_acat_correlation_summary.py` still have reversed SCHWAB_NNA. Flag to COO.

**Do NOT:**
- Run `transfer_out_exclusion` without reading `audit_summary.json` first
- Extend the canonical exclusion patterns in script 05 without Phase 5 results
- Push commits (DT handles all pushes)
