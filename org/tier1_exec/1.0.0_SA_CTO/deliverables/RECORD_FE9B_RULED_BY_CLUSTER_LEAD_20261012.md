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

## ADDENDUM 4 (2026-10-12 ~14:2xZ) -- the reader read: NO retro-fold. The trend start is accepted; the identity is kept on EVERY date, through the suppressed amount.

`2.0.0_SA_COO~D1` msg 4421, `round6/FOLD_ADDENDUM2_READ.md` @01b9e95401.
- **Readers:** `portal/src` reads the undated `platinum/mdpf/{scope}/*.json`; the gateway tools read the one catalog object and refuse a mismatched as_of.
  - No served reader opens a pre-fold dated object, so **no retro-fold** (ADDENDUM 3, D3.2).
  - Readers outside the repo were not read, and that is stated.
- **The trend:** the Model Portfolios trend (`ModelPortfolios.tsx:782-856`) reads Global `by_model` history.
  - Per-model trend lines begin 2026-05-15 on the core lines.
  - The other-models line is suppressed on 55 more dates (inflection alone, $26.1M to $58.6M).
  - ACCEPTED: it is the per-date rule applied honestly. `/portfolios` is partner-facing, so Andrew is told, as information.
- **The identity is NOT merely scoped away.** `sum(by_model)` differs from `model_aua` on 438 of 485 dates by EXACTLY the suppressed dollars. So the build computes the suppressed
  amount per date (not emitted, no new key) and asserts `model_aua - sum(by_model) == suppressed` on EVERY date, to the cent. A date where the gap is anything else fails
  closed. Identity is kept everywhere, and it is the check that a fold dropped nothing else.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 5 (2026-10-12 ~14:4xZ) -- both differential readings CONFIRMED; the 10 absent quarter cells ACCEPTED

`2.0.0_SA_COO~D1` msgs 4436, 4437.

1. **The identity is CONFIRMED as a differential.**
   - Today's object already carries a $0.01-0.02 rounding residual on 208 of 485 valued dates. (The issuer corrected its own earlier "479 of 485" in the record.)
   - The assertion is therefore `residual_after - residual_before == suppressed`, per date and to the cent. It proves the same thing: the fold dropped exactly the suppressed
     dollars and nothing else.
   - The pre-existing residual is not this cell's to fix. It is printed with its denominator in the cell's evidence.
2. **The flip refusal is WITHDRAWN under (b).** ADDENDUM 1's flip guard existed only to make the as-of reading safe. Under ADDENDUM 3's per-date fold the 392 "flips" per core line
   are simply the folded dates, not exposure. The cell REPORTS flips, and it REFUSES on two things:
   - the differential identity;
   - ADDENDUM 2's assertion that every emitted `by_model` line is held at 2 or more firms on its date. That assertion is the guard that carries the grant's basis.
3. **The 10 of 20 core quarter cells absent on the 2026-10-09 object are ACCEPTED:** q2 2026-03-31 and q3 2025-12-31 fall before 2026-05-15. Each renders the existing honest-None
   state, and it is the same history the trend loses. Partner-facing, so Andrew is told, as information.
4. **The fold line as a crosswalk row in both homes** (the registry raises at import on an unknown model) makes the cell WORLD-class. The deploy order names the emitter package.
   Accepted as stated.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 6 (2026-10-12 ~18:3xZ) -- rows D1-W16-S1/S2: on a day the fold line itself is under 2 firms at the as-of, (b): isolate Global and refuse it that day

`2.0.0_SA_COO~D1` msg 4533. CN-f-1 is built and graded (contract 10/10, comparator 11/11, seams 6/6). The merge is held on one latent hazard.
- On a day the as-of pool is held by fewer than 2 firms (today it is held by 2), the fold line is None at the as-of and Models falls short of `total_aua`.
- The Global category-views gold-plane check then raises `ViewPlaneError` OUTSIDE isolation, which aborts `build_all` for EVERY scope.
- aum-metrics would also show the last pooled dollars as current.

**Ruling: (b).** (a) is refused: putting the suppressed dollars into a Custom node total shows one firm's book as a Global figure, which is the exposure fe9b closes.
1. **Isolate Global's views** so that a Global refusal never aborts another scope's build. The firm scopes build as usual.
2. **On such a day, Global is REFUSED as a whole,** views and aum-metrics together, never partially. The prior served Global object stays, carrying its OWN `as_of`. The
   gateway already refuses a mismatched as_of, and the portal shows the object's date, so nothing presents yesterday's figure as today's.
3. **The refusal is printed in the build's own output,** with the as-of, the fold line's firm count and the reason. No alarm and no notifier (moratorium). The next day that
   holds 2 or more firms builds normally.
4. **Arms, added to the cell before merge:**
   - a planted one-firm-pool day refuses Global, and the firm scopes build;
   - a two-firm day builds Global;
   - the prior object is unchanged by a refusal (VersionId read).

-- 1.0.0_SA_CTO~DELL1
