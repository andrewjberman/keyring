# NEVER-WIDEN HALF REQUEST -- MDPF_SECCLASS FWD-7 backfill first scheduled write (SC-k-1)

**Requesting seat:** `0.9.0_WK_MDPF_SECCLASS~1` (worker of `2.0.0_SA_COO~M`), task order `MDPF_SECCLASS.TO-SC-k1`.
**For:** the CTO+COO never-widen sign-off on the FIRST real scheduled write of `etf-classifications` rows under FWD-7
(PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`, C-WRITER, C-SERVED). This build itself performs
NO such write (LOCAL build + record bound); the numbers below are measured from the dry-run census,
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BACKFILL_CENSUS_20260929.json` (generated 2026-09-29,
real S3/DynamoDB reads), plus one live, refused, no-op conditional put against GLD proving the rule the write obeys.

## The act

For each firm with a live, ticker-keyed held-securities source (`bd`, `49financial`, `inflection`; `cottonwood` has
none live at this build -- see census), run `etf_classification_scheduled.plan_rows()` then `write()` against
DynamoDB `etf-classifications`: a conditional put per candidate ticker, `ConditionExpression=attribute_not_exists(ticker)`,
`classified_by = "scheduled"`. No existing row is ever read for its OWN sake and no existing row is ever an input to a
write -- an existing ticker is skipped before classification is even attempted (`plan_rows`, existing_tickers test).

Measured scope of this act (R1_BACKFILL_CENSUS_20260929.json, amendment 1 applied -- a held ticker the SEED SOURCE
already carries, e.g. any ticker `seed-etf-classifications.py` would write on its next run, is `seed_pending`: the
seed path's, never planned here, even though the live table lacks it today):

| firm | held tickers | already present | seed_pending (the seed path's) | would-write (candidate rows) | unresolved (no fold, listed by name) |
|---|---|---|---|---|---|
| bd | 2,234 | 262 | 16 | 1,749 | 207 |
| 49financial | 2,302 | 258 | 12 | 1,431 | 601 |
| inflection | 285 | 71 | 1 | 137 | 76 |
| cottonwood | 0 (no ticker-keyed holdings source live) | 0 | 0 | 0 | 0 |

1,943 DISTINCT new tickers across all firms (some tickers held by more than one firm; the table itself grows from its
current 344 rows to 2,287). By resolved class: equity 1,767, fixed_income 174, alternatives 2. Every one of these rows
is resolved directly from its own bd-securities `(asset_class, sub_asset_class)` value against the canonical table's
own vocabulary (`TableVocabulary`, read from the live table) -- no fold, no outside model. 884 candidate names
(207+601+76) stay unresolved and are listed by name in the census, never guessed into a class. 29 further names
(16+12+1) are `seed_pending`: PHYS is the named example in amendment 1, but it is not among them today (PHYS's own
bd-securities value, `alternatives`/`Gold`, is a fold and PHYS is not yet in the seed source -- see surprise row
`MDPF_SECCLASS-W1-S1`); the 29 found here are real seed-source tickers (e.g. `MDY`, `WALMART INC COM`) whose live row
has not caught up with a prior seed-source edit -- this write does not touch them either.

## Blast radius

- **The rows.** Exactly the 1,943 tickers listed in `R1_BACKFILL_CENSUS_20260929.json`'s per-firm `rows[]`. Zero
  existing rows are touched: `overwrites: 0` on every firm, and the live overwrite-refused control (below) proves the
  write path itself cannot touch one even if a candidate happened to collide.
- **`find_by_asset_class` / `find_by_sub_asset_class` callers** (the one client,
  `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py:116-158`), whose result sets grow with every
  new row: a repo-wide census of actual METHOD INVOCATIONS (`\.find_by_(asset_class|sub_asset_class)\(`), excluding the
  module's own usage docstring, reads **ZERO functional call sites today**, across all three existing copies of the
  client (`_shared/etf_classifications_dynamodb.py`, `yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py`,
  `yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py`) -- only each copy's
  own docstring illustrates the two methods. So this write's blast radius on find_by_* READERS is measured at zero call
  sites today, smaller than the decomposition's ~10k-row full-backfill estimate (this round's 1,943 rows is itself
  smaller than that estimate). The table's row count still grows 344 -> 2,287, and any FUTURE caller of either method
  inherits the larger result set from that point on.
- **IAM (DESIRED, NOT APPLIED).** PutItem on `etf-classifications` for E_18's principal
  (`infra/aws/terraform/bd-pipeline/iam.tf`, DS BD lane); removal of that same principal's PutItem grant on
  `bd-securities` (the stub write `E_18.detect_new_securities.py` no longer performs -- see the code change at
  `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`).
- **Readers.** Positioning's two surfaces and every FWD-2 consumer of `etf-classifications` see the 1,943 tickers as
  ordinary new rows; today, with no row, they already render each as unclassified by name (FWD-2's own bar) -- so no
  reader's CURRENT output for an EXISTING ticker changes; only tickers that were unclassified gain a class.
- **Not in scope of this act.** GLD, PHYS and VXX are never write candidates (GLD/VXX already have rows; PHYS's only
  input, bd-securities' `alternatives/Gold`, is a fold against the canonical vocabulary and stays unresolved --
  see surprise row `MDPF_SECCLASS-W1-S1`, which also notes PHYS currently has no live row at all, pending a different
  workstream, IB-mr-251).

## Rollback per key

Delete exactly the rows with `classified_by = "scheduled"` AND `updated_by` in
`{"mdpf-secclass-scheduled", "bd-e18-scheduled"}` that this write added -- the key list is the per-firm `rows[].ticker`
entries in `R1_BACKFILL_CENSUS_20260929.json` (the candidate set this half names), one `DeleteItem` per ticker, never a
table-wide delete or scan-and-filter. No pre-existing row is touched by the write (proved live, below), so no existing
row ever needs restoring as part of this rollback.

## The schedule

The BD gold-layer run that already calls `E_18.detect_new_securities.py` (`run_gold_layer.sh`, after script 12) is
FWD-7's first scheduled caller in this cell's scope -- the trigger is that schedule, never upstream success alone
(CLAUDE.md NEVER-moratorium on inferred triggers). No new Terraform resource is required for E_18 itself; it already
runs on that schedule and this act only changes what it writes and where. If 49financial/inflection/cottonwood need
their own scheduled caller in a later round, any new name is builder output, not hand-typed (C-NAMES, run 2026-09-29):
`lib/opal_naming.py name('mdpf', None, 'secclass', 'lambda')` -> `mdpf-secclass-lambda`;
`name('mdpf', None, 'secclass', 'role')` -> `mdpf-secclass-role`;
`name('mdpf', None, 'secclass', 'daily')` -> `mdpf-secclass-daily`.

## Live control proving the rule this write obeys

A real, no-op conditional put was run against the live `etf-classifications` GLD row, using GLD's OWN bd-securities
value (`alternatives`/`Gold` -- the exact fold this rule exists to refuse), via `etf_classification_scheduled.write()`
with `ConditionExpression=attribute_not_exists(ticker)`:

- result: `[("GLD", "refused")]` -- `ConditionalCheckFailedException`, as required.
- GLD's row read back byte-identical before and after (`R1_BACKFILL_CENSUS_20260929.json` ->
  `overwrite_refused_control: true`, `overwrite_refused_control_detail.gld_unchanged: true`).

No other table write of any kind was performed in this build.
