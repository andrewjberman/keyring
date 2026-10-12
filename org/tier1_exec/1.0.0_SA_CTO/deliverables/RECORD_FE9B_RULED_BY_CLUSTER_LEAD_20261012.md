# dell1 open call `dell1-20261011T053810Z-fe9b` (MDPF_CANON X2 global fold) -- RULED (A) by the cluster lead; this seat's local record (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~14:0xZ)

**Ruling:** laptop `1.0.0_SA_CTO` msg 108571, relayed by `0.0.0_AB_MSTR~DELL1` msg 4389 (bus 1f4ee70c). The laptop record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL1_FE9B_MDPF_CANON_X2_GLOBAL_FOLD_A_20261012.md`. It is not on origin at this writing, and it reaches CLOUD at the
laptop's next integrate. Substance as relayed:
- MDPF_CANON Global folds every per-model line held at FEWER THAN 2 firms. X2 was granted on "aggregate counts only", so a one-firm line is that firm's book under a Global
  label. The fold restores the grant's basis; (B) would widen it.
- `min_firms = 2`, computed per as-of from the firm scopes' own objects, never a static list.
- Carries fold too. Headline sums and served JSON keys are unchanged.

**This seat's acts:**
- close fe9b on this record (`--ruled-by cluster-lead`);
- the fold is MDPF_CANON's cell for `2.0.0_SA_COO~D1`, under its own never-widen pair (it moves served global lines);
- row D1-W8-S5 disarms on that cell's read-back.
This was the recommendation put to Andrew (option A).

## ADDENDUM 1 (2026-10-12 ~14:1xZ) -- "per as-of": the as-of reading is ACCEPTED, with a build-time guard against the case where the two readings differ

`2.0.0_SA_COO~D1` msg 4396, prep read `deliverables/2.0.0_SA_COO~D1/round6/FE9B_FOLD_PREP.md` @71af9dbc31. At as-of 2026-10-09, 14 of 20 global
`aggregate_aua_timeseries` lines are held by fewer than 2 firms: 8 cottonwood-only, 2 inflection-only, 2 carries and 2 null. 6 stay. The fold is round 6's cell, deployed after
CN-d-1's ledger closes, in its own window, and clear of FIRMBKTS's R2 surfaces.
- **The as-of reading is accepted:** the firm count is evaluated at each served object's as-of and applied to that object's history arrays. On the measured 60 dates it gives
  the same set as the date-by-date reading, with 0 flips.
- **The guard:** the grant's basis is per DATE (a history point reveals that date's book). The two readings differ only when a line's firm count at an earlier date is below 2
  while the as-of count is 2 or more, which is a "flip". So the build COUNTS flips on every run and REFUSES to publish if any is non-zero: fail closed, and the row
  comes back here. With flips at 0, the as-of reading is exactly the date-by-date reading.
- **The 2 null lines** (no model key) are printed with their dollars and folded with the rest. A null is not a model and is never shown as one.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-12 ~14:2xZ) -- the cluster lead's refinement (laptop CTO msg 108578, on the CRO's read): the FOLD LINE itself must hold at least 2 firms

Relayed by `0.0.0_AB_MSTR~DELL1` msg 4406, verbatim in substance:
- The folded "other models" line must itself be held at 2 or more firms. Otherwise it too is SUPPRESSED, per date, in both the primary and the secondary series.
- (A) stands.
- The cell's read-back asserts that EVERY emitted `by_model` line, the fold line included, is held at 2 or more firms.
This supersedes nothing in ADDENDUM 1. It closes the case where the fold of one-firm lines is itself one firm's book. This seat adopts it without amendment.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-12 ~14:2xZ) -- the three implementation decisions (`2.0.0_SA_COO~D1` msgs 4409, 4410, 4412). This seat's fabric; the cluster lead is informed.

**D1, the flip guard over 494 dates: (b), NOT (a).** The five core lines were 49 Financial's book ALONE on 383 dates (2024-11-01 to 2026-05-14). Inflection's first positive value is
2026-05-15.
- (a) would start the guard at that epoch and SHOW those 383 dates of per-model lines under the Global label, which are one firm's book. That is the exact exposure fe9b closes,
  for 78 pct of the history. Refused.
- (c) is dishonest: a measured 0.0 is not a holding.
- **(b): per date, a line held at fewer than 2 firms folds.** Before 2026-05-15 Global therefore carries NO per-model lines, only its headline. The served object states why, in
  band: "per-model detail begins 2026-05-15, the first date Global combined two firms". That is the honest history, and the guard then passes on the honest predicate
  (value > 0).

**D2, the 3 SMA-class lines: YES, leave them untouched.** The 11 model-class lines fold. `opal_div_sma`, `opal_growth_sma` (49financial) and `pfde` (cottonwood) sit outside
`model_aua`, and a `by_model` entry carries one `source_basis`, so no two-firm line can form. Withholding them would break the view-plane identity by $21.1M. And **the SMA tree
already serves by_firm per member by Andrew-direct ruling**, so per-firm SMA is ALREADY authorized display, and leaving these lines reveals nothing that ruling does not. The
outcome is named here: the SMA lines are governed by that Andrew ruling, not by X2's fold.

**D3, the page deltas and the retro-fold:**
1. **Accept the Model Portfolios deltas into the pair:** Total Holdings -185, archetype cards -$43.16M in all, because the two inflection blends no longer roll in. These are the fold's
   correct effect. `/portfolios` is PARTNER-FACING, so Andrew is told the deltas, as information. The page's "durable fix" that would add a JSON key is NOT made, because the
   ruling holds the keys.
2. **Retro-fold: READ before deciding.** The 135 served dated global objects are immutable and keep their one-firm lines.
   - If NO served page or API reads a pre-fold dated object (the page reads only the latest as-of), there is no retro-fold now.
   - If ANY served reader opens a pre-fold dated object, the exposure persists through it, and the retro-fold is REQUIRED, as its own act and pair, publishing folded objects
     at new versions with the readers pointed at them.
   The read is part of this cell's pair.

-- 1.0.0_SA_CTO~DELL1
