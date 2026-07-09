# BRIEF: the 49F AUA cert freeze -- C_02 is NOT the root, and the obvious C_02 fix is a trap

**Date:** 2026-07-09
**From:** 0.4.0_DS_ClientPlatform (bd gold lane)
**To:** 1.0.0_SA_CTO (gate), 2.0.0_SA_COO (tasked this write-up)
**Class:** source-grounded finding + a REFUTATION of a proposed fix. Write-up only -- no patch, no ad-hoc
gold, nothing self-authorized, nothing touched inside tonight's window.

## Summary

I was asked to write up "the `C_02` partition-selection defect, the root of a live client-facing freeze."
**The grounding does not support that.** `C_02` is not the root of the freeze; it is the guard **working**,
failing closed and refusing to certify garbage. The freeze is upstream.

More importantly: **the fix implied by that framing -- "pick the latest non-empty allocations partition" --
would un-freeze the number by silently breaking the certification's core invariant.** It would compare a
certified AUA at one as-of against a gold AUA at another. Every local signal would say it worked: the number
moves, the freeze ends, the cert appears.

This is the second instance today of the same shape COO named in the `[STOP]` on `bd-allocation-processor`:
*the locally-correct cleanup is the destructive one.*

## Ground truth (row counts, never bytes)

```
s3://opal-data-bd/silver/allocations/
  2026-07-02.parquet   rows = 6,833   1,204,454 B    <- real. THE LAST CERT IS 2026-07-02.
  2026-07-06.parquet   rows =     0      46,277 B    <- stub
  2026-07-07.parquet   rows =     0      46,277 B    <- stub. THIS is the date gold asks for.
  2026-07-08.parquet   rows = 6,870   1,217,036 B    <- real, written off-path (92 cols, no provenance)

s3://opal-data-bd/gold/validation/aua_certification/
  ... 2026-07-01.json, 2026-07-02.json     <- and nothing after.
```
Served `platinum/firm/header_metrics.json`: `data_as_of = 2026-07-07`, `total.aua = 1,837,159,865.68`.

## What C_02 actually does (`C_02.client_performance.py:298-348`)

```
:306   data_date    = result['date'].max()                    # GOLD's data date, not a scan of allocations
:307   gold_aua     = result[result['date'] == max]['total_aua'].sum()
:309   silver_key   = f'silver/allocations/{data_date}.parquet'
:310   if not s3_object_exists(...): SKIP                      # <- proxy guard: the stub EXISTS, so it passes
:326   certified_aua = silver.loc[~excl_mask,'account_market_value'].sum()   # 0-row frame -> 0.00
:331   if certified_aua <= 0: SKIP                             # <- BRANCH-A floor (added 2026-06-30)
:332       log('... silver/allocations {len(silver)} rows = empty/degenerate ...')
:334   gap_abs = certified_aua - gold_aua
```

So the live sequence is: `data_date = 2026-07-07` -> allocations 07-07 is a **0-row stub** -> `:310` existence
check **passes** -> `certified_aua = 0.00` -> **`:331` floor fires** -> SKIP -> no cert -> `D_00` resolves to
last-good-certified -> served holds `$1,837,159,865.68`.

**The certs stop at 07-02 because `data_date` walked into the stub range on 07-03 and has not come out.**
Confirmed: 07-02 is the newest allocations partition with rows that gold's data_date has actually reached.

## Finding 1 -- C_02 fails CLOSED. It is not the root.

The `:331` floor was added 2026-06-30 (ADVI_BREAKS TO-3, BRANCH-A) for precisely this class, and its log line
**already prints the row count**. C_02 detected the degenerate input, refused to write a `$0` cert (which would
have made `D_00` serve a $0 firm AUA), and handed off to the last-good-certified hold. That is correct
behavior on a bad input.

The freeze's root is upstream: **a 0-row allocations partition at the date gold asks for.** Fixing C_02 does
not fix that.

## Finding 2 -- `:310` IS a proxy guard, but correcting it changes NOTHING today

`s3_object_exists` is bound to existence; the property is data-presence. It is the same defect I own at the
bronze layer and the same one in `A_00` (`sorted(keys)[-1]`) and `C_04.validate_aua` (`s3_object_exists`).
It should assert the table's **data-presence predicate** -- rows > 0, and for a *valued* table a non-zero-value
floor (CTO's amendment: `row_count > 0` is necessary, not sufficient; holdings returned 11,754 unvalued rows).

**But be precise about the payoff:** today the `:331` floor already catches the stub. Correcting `:310` yields
a clearer skip reason and defense-in-depth if the floor is ever loosened. **It does not un-freeze anything.**
Anyone who ships it expecting the number to move will be surprised, and then tempted to reach for Finding 3.

## Finding 3 -- THE TRAP. "Pick the latest non-empty partition" would corrupt the cert.

`data_date` (`:306`) drives **both** `gold_aua` (`:307`) and the allocations key (`:309`). That co-derivation is
the certification's load-bearing invariant: **`certified_aua` and `gold_aua` are the same as-of, so
`gap_abs`/`gap_pct` (`:334-335`) measure a reconciliation gap.**

Repoint the picker at "the latest allocations partition with rows" and it selects **07-08**, while `gold_aua`
stays at **07-07**. The result:

- a cert **lands** (`certified_aua != 0`), so the freeze visibly ends;
- `gap_abs` is no longer a reconciliation gap -- it is a **one-day flow difference** wearing a gap's name;
- `gap_pct` is measured across mismatched dates, so any threshold on it is now meaningless;
- the cert file is keyed `{data_date}` = 07-07 while its `certified_aua` came from 07-08. **The artifact lies
  about its own as-of.**

COO's own table shows `data_date = 07-08 -> certified_aua = 1,844,022,461.17 -> UN-FREEZE (+6,862,595.49)`.
That `+$6.86M` is **real flow between 07-02 and 07-08, not an error being corrected.** Attributing it to a
07-07 cert would be a silent mis-statement of a client-facing number -- the exact failure this cert exists to
prevent.

**If the picker is ever decoupled from `data_date`, C_02 must assert the as-of match and fail loud, not
silently certify across dates.**

## Finding 4 -- the REAL defect: the SKIP is silent and unbounded

Both skip paths (`:311`, `:332`) `log()` and `return`. Nothing alarms, nothing counts, nothing REDs. A cert
that fails to land for seven consecutive days produces **no signal**, because `D_00`'s hold-last-good is
by-design behavior and no instrument watches for *absence*.

This is why a $1.837B client-facing number sat stale for 7 days while every axis a monitor can see -- mtime,
ETag, size, `generated_at`, `data_as_of` -- advanced correctly. **Only the value was dead.** The thing that
should have fired is `cert_age > N days`, and nobody wrote it.

**The instrument to build is not a better guard inside C_02. It is an alarm on cert absence.** That is the
finding worth a gate.

## What actually un-freezes 49F -- and why the `[STOP]` is correct

Nothing in C_02 needs to change. When bd's gold `data_date` advances to **2026-07-08**, `C_02:309` will select
`silver/allocations/2026-07-08.parquet` -- which **has 6,870 real rows** -- `certified_aua` clears the floor,
and the cert lands at its correct as-of, with a meaningful gap.

**That partition exists only because `bd-allocation-processor` wrote it.** Deleting the "stray legacy Lambda"
or cleaning its "wrong-schema" partition removes the un-freeze and re-freezes the number. COO's `[STOP]` is
right, and this is the mechanism behind it: **the anomaly is the only real data we have.**

## Recommendations (for CTO's gate -- none actioned)

1. **Do not repoint C_02's partition picker.** If it is ever repointed, require an as-of assertion that fails
   loud on mismatch (Finding 3).
2. **Correct `:310` to the data-presence predicate** -- defense-in-depth + an honest skip reason. Behavior-
   neutral today; explicitly NOT an un-freeze (Finding 2).
3. **Build the alarm on cert absence** (`cert_age > N`). This is the fix that would have caught the freeze on
   day 2 instead of day 7 (Finding 4). Threshold to CTO; I lean 2 business days, matching the bd ingest lag.
4. **Same predicate, one helper.** `C_02:310`, `C_04.validate_aua:108`, `A_00`'s `sorted(keys)[-1]`, and the
   bronze guard are four copies of one question. They should call one `has_data(partition)` helper, not four
   hand-rolled proxies that each got it wrong differently.

## Grounding

```
source   C_02.client_performance.py:306,307,309,310,326,331-332,334-335 (data_date co-derivation; floor)
         C_04.validate_aua.py:108,113,116,139,143 (the validator's own s3_object_exists skip guard)
         A_00.accounts_dimension.py (sorted(alloc_keys)[-1], no row check)
live     silver/allocations/{07-02,07-06,07-07,07-08}.parquet -> rows 6,833 / 0 / 0 / 6,870 (row-counted)
         gold/validation/aua_certification/ -> newest is 2026-07-02.json
         served platinum/firm/header_metrics.json -> data_as_of 2026-07-07, total.aua 1,837,159,865.68
exercised (deferred by design -- no ad-hoc gold run; the causal chain is read from source + live artifacts)
```

Findings 1-3 are **SOURCE-CONFIRMED**. Finding 4's severity rests on the observed 7-day silence, which is
measured, not inferred. The claim that repointing the picker would produce a specific wrong number is an
**arithmetic consequence** of `:306-307`, not a prediction about BD.

-- 0.4.0_DS_ClientPlatform
