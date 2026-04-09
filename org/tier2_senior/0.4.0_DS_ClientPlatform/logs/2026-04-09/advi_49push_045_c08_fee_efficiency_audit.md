# ADVI_49PUSH.045 -- C_08 Fee Efficiency Audit and Fix

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-09
**Project:** ADVI_49PUSH (Wave 11 -- Books tab fee efficiency correctness)
**Status:** COMPLETE. Commit pushed + S3 uploaded. AE notified to include in gold run.

---

## Summary

Full audit of C_08.advisor_fee_efficiency.py per TO instructions. Found and fixed two
confirmed bugs. Confirmed the commission formula is correct (not a bug -- a methodology
note). Findings posted to CTO inbox before any code change was committed.

---

## Commit

| Field | Value |
|-------|-------|
| SHA | `d79ad9e7` |
| Branch | CLOUD |
| Push | origin/CLOUD confirmed |
| S3 upload | `s3://opal-data-bd/code/gold/C_08.advisor_fee_efficiency.py` |
| AE notified | 0.6.0_AE_PartnerETL inbox (include C_08 in gold run before D_04) |

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py` | Efficiency pctile ranking direction fix + two-tier negative NNA ranking |

---

## Investigation Findings

### ISSUE 1 -- Grace McCasland commission discrepancy ($17.9K vs $21.6K)

**Root cause: formula is correct, display is misleading due to mismatched bps denominators.**

The portal displays two fields that come from different denominators, making them
non-reconcilable by simple multiplication:

  Portal "Fee" column = advisor_effective_bps = implied_annual_fee / total_aua * 10000
  Portal "AUA" column = managed_aua = sum(aua_current * split_pct/100)
  Commission formula  = fee_bps_weighted/10000 * managed_aua * period_fraction
                      = (implied_annual_fee / managed_aua) * managed_aua * period_fraction
                      = implied_annual_fee * period_fraction

  fee_bps_weighted (gross rate, split cancels) != advisor_effective_bps (effective rate = fee_bps * split/100)

The natural check "displayed_fee_bps * displayed_AUA * period_fraction" produces:
  advisor_effective_bps/10000 * managed_aua * period_fraction
  = (fee_bps * split/100)/10000 * (aua_current * split/100) * period_fraction
  = commission * (split/100)  [single account, illustrative]

For a multi-account advisor, Andrew's check produces commission / avg_split_fraction.
For Grace with avg split ~83%: $17.9K / 0.83 ≈ $21.6K. Confirms the mismatch mechanism.

**Formula unchanged** -- the commission IS the prorated split-weighted fee estimate.
**DE flag sent** -- FeeEfficiencyPanel tooltip should explain: "Commission is an estimated
  prorated amount = implied annual fee * (period_days / 365.25), using split-weighted AUA.
  It will not equal fee_bps * AUA since fee_bps shown is the advisor's effective rate
  (gross fee * split%), not the gross fee rate used in the commission calculation."

### ISSUE 2 -- Cole Pettis efficiency ranking inverted

**Root cause: rank(ascending=True) gives efficient advisors LOW percentiles -- direction inverted.**

C_08 original code (lines 233-242):
  ranked['_ratio'] = ranked['commission'] / ranked['nna']
  ranked['efficiency_pctile'] = ranked['_ratio'].rank(ascending=True, pct=True) * 100
  # Comment: "Lower ratio = more efficient = higher percentile"

pandas rank(ascending=True, pct=True): lowest value = ~0th pctile, highest = 100th.
So lowest commission/nna (= most efficient) got the LOWEST percentile. Inverted.

The comment described the correct INTENT but ascending=True implements the opposite.

Cole with commission/nna = 0.53% (generates ~$188 NNA per $1 commission = highly efficient)
  Old: ~10th pctile (ascending=True, low ratio = low pctile) -- WRONG
  New: near 90th+ pctile (ascending=False, low ratio = high pctile) -- CORRECT

**Fix: ascending=True -> ascending=False on the Tier 1 rank call.**

### ISSUE 3 -- Negative NNA hardcoded to 0

**Root cause: all nna <= 0 advisors got efficiency_pctile = 0 regardless of magnitude.**

An advisor with nna=-$1K and an advisor with nna=-$5M were indistinguishable -- both at 0th pctile.

**Fix: two-tier ranking system across ALL advisors (0-100 scale):**

  TIER 1 (nna > 0): rank by commission/nna descending (ascending=False)
    Pctile range: [pct_tier2 * 100 .. 100]
    Most efficient (lowest ratio) -> 100th pctile.

  TIER 2 (nna <= 0): rank by |nna| ascending (closer to 0 = less bad = higher tier-2 pctile)
    Pctile range: [0 .. pct_tier2 * 100]
    Least negative (nna=0 or just below 0) -> top of Tier 2, just below Tier 1 floor.

Example with 10 advisors (8 positive NNA, 2 negative):
  pct_tier2 = 2/10 = 0.20
  Tier 2 pctiles: 0 to 20 (nna=-$500K -> 10%, nna=-$100K -> 20%)
  Tier 1 pctiles: 20 to 100 (worst ratio -> 28%, best ratio -> 100%)

All advisors now have differentiated, meaningful percentiles on a 0-100 scale.
Tier 2 advisors always rank below Tier 1, but are distinguished from each other.

---

## Period Completeness Spot-Check

Checked Max window calculation (primary concern from TO):

  `period_days = max(1, (latest_date - window_start).days)`
  where `window_start = detail_all['date'].min()`

  No cap or truncation. The max(1, ...) is just a safety floor for edge cases.
  For a dataset going back 3 years: period_days = ~1095, period_fraction = ~2.998. Correct.

Window completeness: all advisors on latest_date appear in every window (left merge in
_build_window ensures this). If advisor had no trades in a window, nna=0 -> Tier 2.
This is correct behavior -- they have zero NNA for the period, not missing data.

Commission formula at window grain:
  commission = fee_bps_weighted/10000 * current_aua * period_fraction
  AUA is always the CURRENT (latest) snapshot, not period-averaged.
  For long windows (Max), this overstates commission for advisors who grew their book.
  This is documented as "time-prorated estimate" -- intentional methodology, not a bug.
  The TO notes this is "NOT the actual invoiced amount from BD."

Verified: QTD window_start = pd.Timestamp(year, q_month, 1) where q_month = ((month-1)//3)*3+1.
As of 2026-04-09 (Q2): q_month=4, window_start=2026-04-01. period_days=8. Correct.
YTD window_start = pd.Timestamp('2026-01-01'). period_days=99. Correct.

No truncation or cap issues found in any window.

---

## Pending (for AE + downstream)

1. **[AE 0.6.0_AE_PartnerETL]** Include C_08 in gold chain run (before D_04).
   S3 artifact is ready at `s3://opal-data-bd/code/gold/C_08.advisor_fee_efficiency.py`.
   C_08 must run before D_04 (D_04 reads advisor_fee_efficiency.json).

2. **[AE 0.6.0_AE_PartnerETL]** After C_08 + D_04 run: verify platinum/firm/fee_efficiency.json
   has updated efficiency_pctile values. Cole Pettis should be near 90th+ pctile (not 10th).

3. **[DE 0.4.0_DE_ClientPlatform]** Add tooltip to FeeEfficiencyPanel Commission column:
   "Estimated prorated fee earnings (split-weighted AUA x gross fee rate x period fraction).
   Not the actual invoiced amount. Will not equal fee_bps x AUA."
   This explains the Grace discrepancy and prevents future confusion.

4. **[DS post-run]** Re-validate all 5 windows once the gold run completes and new
   advisor_fee_efficiency.json lands in platinum.
