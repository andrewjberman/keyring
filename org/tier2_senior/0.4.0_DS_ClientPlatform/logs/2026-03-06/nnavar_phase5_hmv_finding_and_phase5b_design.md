# ADVI_NNAVAR: Phase 5 HMV Finding + Phase 5b Verification Design — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 23:35
**End Time:** 23:55

## Objective

Analyze DT's Phase 5 desc_audit results (commit `cbe221f3`), interpret the
"Holding market value withdrawn" discovery, and design Phase 5b to verify whether
excluding this description closes the -$119M gap.

---

## Work Completed

### 1. Phase 5 Results — Analysis

DT ran `transfer_out_desc_audit` (Phase 5, `cbe221f3`). Schwab keyword gate returned
`exclusion_warranted: false` — only 8 rows / $55K of Schwab-ETF-named transfers, which
are correctly not intra-Schwab platform flows. DT stopped per brief and flagged the
top-volume description.

**The finding:**

```
"Holding market value withdrawn"   4,106 rows   $119.3M   (81.9% of Transfer Out gross)
```

$119.3M matches the -$119M gap target to **$0.3M precision (0.25%)**.

**Total Transfer Out gross (post-exclusion/dedup): $145.7M** (from audit_summary.json).
Of that, $119.3M (81.9%) carries this single description.

**What "Holding market value withdrawn" is:**

This is a BD platform accounting description for the removal of a portfolio holding's
book value from an account. It is NOT a cash transfer to a client. The BD platform
generates this entry when an account's positions are exited — specifically during:

- **Account departures**: Client transfers to another custodian. BD books each position
  as "Holding market value withdrawn" (the exit side). The receiving custodian books
  the corresponding "Holding market value received" (the entry side). No cash changes
  hands — securities move custodian-to-custodian.

- **Internal BD restructuring** (less likely at this volume): Some platform operations
  that mark down a holding's value before a re-entry at a new lot or structure.

**Why Schwab does NOT count this as NNA outflow:**
Schwab's NNA methodology tracks real money movements — client deposits and withdrawals.
A custodian-to-custodian ACAT transfer where 49F assets are moved to another firm is
recorded as an account departure, not as a cash withdrawal. Schwab would note the
departure in their AUA tracking but would NOT subtract it from NNA outflows (NNA tracks
flows of cash/assets from clients into or out of the advisory relationship — a custodian
change is a different classification).

**Why we count it incorrectly:**
The entry has `transaction_type = 'Transfer Out'` and `market_value < 0`. Script 05
includes Transfer Out in OUTFLOW_TYPES and takes abs(market_value). So $119.3M of
BD accounting entries are subtracted from our NNA as real outflows.

**Verification needed before recommending production fix:**
1. Are there paired "Holding market value received" Transfer In entries? If none exist,
   these are one-sided account departure entries (strongest case for exclusion).
2. Does excluding the $119.3M close the gap to ~$0M?

---

### 2. Phase 5b Script — Design and Implementation

**Script:** `data/black_diamond/scripts/diagnostics/diag_nnavar_phase5b_hmv_exclusion.py`
**Brief:** `docs/briefs/devops-brief-nnavar-phase5b-hmv-ec2-run.md`
**Commit:** `6174bd71`

Two suites:

**`hmv_symmetry` (~3-5 min, DT shares results with DS before proceeding):**
- Loads Transfer In and Transfer Out rows (post-exclusion/dedup)
- Checks: how many Transfer In rows carry description "Holding market value received"?
- Computes: net HMV NNA impact (HMV_in_volume - HMV_out_volume)
- Interpretation logic in script:
  - If `hmv_in_rows == 0`: pure account departure entries. No paired inflows in 49F data.
    Strongest possible case for exclusion.
  - If `hmv_in < 10% of hmv_out`: predominantly departures.
  - If `hmv_in ≈ hmv_out`: paired book entries that net to ~$0 (already neutral in NNA).
- Also produces monthly breakdown of HMV outflow volume

**`hmv_exclusion` (~25-40 min):**
Three variants:
- `base_prod`: production caps (vel_w90_t1p00), no exclusion — baseline
- `excl_hmv_prod`: exclude HMV rows, vel_w90_t1p00
- `excl_hmv_best_cap`: exclude HMV rows, vel_w120_t1p00 (best corrected cap)

Key output: `gap_closure_report.json` with verdict field:
- `CONFIRMED` (>90% gap closed): HMV is the explanation. Production fix warranted.
- `PARTIAL` (50-90%): HMV is major contributor, not complete explanation.
- `INSUFFICIENT` (<50%): Something else is at play.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Run `hmv_symmetry` first and wait for DS review | If paired HMV inflows exist in equal volume, the net NNA impact is already ~$0 and no exclusion is needed. The symmetry check gates the exclusion recommendation. |
| Include `excl_hmv_best_cap` variant | Allows seeing the ceiling with both the HMV fix AND the cap correction. If this approaches $0M gap AND r→high, it's the full production fix specification. |
| Gap closure verdict threshold at 90% for CONFIRMED | $0.3M of the $119M is unexplained at DT's precision. 90% threshold accommodates rounding and allows CONFIRMED verdict even with this precision gap. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Phase 5b EC2 execution brief | `docs/briefs/devops-brief-nnavar-phase5b-hmv-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_phase5b_hmv_exclusion.py` | New — Phase 5b HMV verification | Yes — `6174bd71` |
| `docs/briefs/devops-brief-nnavar-phase5b-hmv-ec2-run.md` | New — DT brief | Yes — `6174bd71` |

---

## Blockers

None. DT unblocked to run Phase 5b.

---

## Current State

**Status:** IN PROGRESS — awaiting Phase 5b results
**Active branch:** `CLOUD`

The most likely explanation for the -$119M volume gap has been found: "Holding market
value withdrawn" entries (4,106 rows, $119.3M) in Transfer Out are BD platform
accounting entries for account departures, not real cash outflows. Phase 5b
(`6174bd71`) verifies this by checking for paired inflow entries (hmv_symmetry) and
confirming gap closure upon exclusion (hmv_exclusion).

If Phase 5b returns `CONFIRMED`:
- `"Holding market value withdrawn"` is added to canonical exclusions in script 05
- Production gold rebuild incorporates: HMV exclusion + cap tuning (vel_w120_t1p00) +
  settlement date + JNL/sweep canonical fix (pending CEO) + ACAT (pending CEO)
- Single rebuild closes the gap by ~$119M and improves pearson to vel_w120_t1p00 ceiling

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Run `hmv_symmetry`** — share `symmetry_summary.json`
   + `hmv_monthly_outflow.csv` + stdout with DS

2. **[DS — this agent] Review symmetry result** — confirm interpretation before
   authorizing hmv_exclusion run

3. **[0.4.0_DT_ClientPlatform] Run `hmv_exclusion`** — after DS review of symmetry

4. **[DS — this agent] Analyze gap_closure_report.json** — if CONFIRMED: write
   production fix spec for script 05 canonical exclusion addition

5. **[2.0.0_SA_COO] Production rebuild authorization** — after CONFIRMED verdict:
   single rebuild incorporating all pending improvements

**Files to touch next (DS):**
- `data/black_diamond/scripts/gold/05_build_client_performance.py` — add HMV exclusion
  to canonical description exclusion list (ONLY after CONFIRMED verdict)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-06/` — Phase 5b results log

**Do NOT:**
- Add "Holding market value withdrawn" to script 05 exclusions without CONFIRMED verdict
- Push commits (DT handles all pushes)
