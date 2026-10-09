# Never-widen half, MDPF_SECCLASS -- Black Diamond's served client files stop carrying the retired class `multi_asset` (FWD-16, cell SC-e-75, row MDPF_SECCLASS-D1-S9)

**Author:** `0.9.0_WK_MDPF_SECCLASS~65` for `2.0.0_SA_COO~M1`, 2026-10-08. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half SIGNED (2.0.0_SA_COO~M1); CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed or written to any bucket. Spec: PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`
FWD-16; trace `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_MULTI_ASSET_TRACE_20261008.md` (@623e08ca6b); order
`MDPF_SECCLASS.TO-SC-e75` as amended (AMENDMENT 1, @fefa9a8057).

## What is wrong

36 files `s3://opal-data-bd/platinum/clients/{rid}/concentration.json` carry 141 holdings of class `multi_asset`, all on the dated entries
2026-10-03, 10-04 and 10-05 (47 each). D_04 copies `concentration` unchanged from the C_06 envelope `gold/entities/clients/{rid}.json`. C_06 classified
those dates while `etf-classifications` still held `multi_asset` rows; the remap (commit `0d9457b639`, 2026-10-07 07:10Z) did not reach them, because C_06's
incremental merge rewrites only the dates in the new partitions and keeps every other dated entry as written.

## The fix (staged, LOCAL, not deployed)

`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`: new module function `reclassify_retained(existing_mix, existing_conc, rebuilt_dates)`
(:273), called in the incremental `_merge_and_write` before the new dates are laid in (:778), plus the per-run census line
`C06-RETAINED-RECLASS entries=<n> holdings=<n>` (:831).
- A RETAINED dated entry (not rebuilt this run) with a holding whose `asset_class` is outside {equity, fixed_income, cash, alternatives, structured,
  commodities, unclassified} has those holdings sent back through `classify_series` (the call new dates use: `classify`, `get_sub_asset_class`,
  `classify_with_identity` for a blank ticker).
- The date's `mix` moves that holding's own `pct` from its old class (if the old class is a mix key) to the new class. A class the table cannot resolve lands
  on `unclassified`, never on a retired class.
- Market values, pcts, dates and every entry already inside the six are untouched. Pinned by
  `data/black_diamond/scripts/gold/tests/test_c06_retained_dates_six_class.py` (6 tests; the control entry is byte-identical).

## The act (by the issuer, after both halves sign)

1. Deploy: copy `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` to `s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py` through the
   DS deploy lane (`.tools/safe-deploy.sh`). One object; no `lib/` file changes.
2. Wait for the next scheduled BD gold fire. It runs C_06 (incremental), which heals the retained entries inside the same pass that writes the new dates,
   and D_04 then rewrites `platinum/clients/{rid}/concentration.json` from the healed envelope.
3. Read back (leg G): the 36 keys, `multi_asset` census = 0; the run log carries `C06-RETAINED-RECLASS entries=<n> holdings=<n>`.

Conditions this worker did NOT verify, stated so the signers read them:
- The next fire's time and mode. If it finds no partition newer than the watermark, C_06 returns at "No new partitions" and heals nothing; a relationship with no
  row in a new partition is not in `new_data` and its envelope is not rewritten. The log line is the check.
- Any other reader of `gold/entities/clients/{rid}.json` or `gold/client_timeseries/{rid}.json` (the dual-written legacy key is rewritten with the same payload).

## Blast radius

**Objects written by the fire:** per relationship in `new_data`, `gold/entities/clients/{rid}.json` and its legacy twin `gold/client_timeseries/{rid}.json`,
`..._views.json` (period views recomputed from the merged mix), and then D_04's `platinum/clients/{rid}/...` files. This is the SAME write set the nightly
fire already makes; the change is in the CONTENT of retained dated entries only.
**Content that moves:** retained dated entries holding a class outside the six. Measured census (read-only, 2026-10-08, the 36 envelopes named by
`SERVED_MULTI_ASSET_SPLIT_20261008T1810Z.json`): 36 keys, **141 holdings** on **105 dated entries**, no other entry changes.

**Local candidate diff** (this worker ran the new `reclassify_retained` locally, on the live-read envelopes, with the live classifier; no write):

| scope | entries | holdings | moves |
|---|---|---|---|
| z08119861 (one hit client) | 3 (10-03, 10-04, 10-05) | 3 | KAGIX `multi_asset` -> `equity` x3 |
| all 36 hit envelopes | 105 | 141 | `multi_asset` -> `equity` 84, `multi_asset` -> `fixed_income` 57 |

z08119861 detail: KAGIX "KENSINGTON DYNAMIC ALLOCATION INST" (pct 0.036687 / 0.036702 / 0.031997) moves to `equity`, `class_source` `etf-classifications`, and the mix
`equity` value moves 0.767911 -> 0.804598 (10-03), 0.768263 -> 0.804965 (10-04), 0.789798 -> 0.821795 (10-05); the mix then sums to 1.0 on all three dates
(0.963313 / 0.963298 / 0.968003 before). The other 1291 dated entries of that envelope are byte-identical after the run; classes outside the six after: 0.

**Known limit of the candidate (a measured shortfall, not a hidden one):** the envelope keeps only the top 10 holdings per date. The old mix never counted
`multi_asset` weight, so a `multi_asset` position outside a date's top 10 is not visible in the envelope and cannot be re-added. Across the 105 changed dates the mix
sum after the candidate is 1.000001 at most and 0.952431 at least; **15 of 105 dates stay below 0.999**. Those 15 mixes stay short by the weight of positions the envelope
does not hold; only a C_06 FULL build (reclassifying from the canonical holdings) closes them. No holding the envelope shows is left outside the six.

**Not touched:** any key outside the 36 hit clients' retained dates; `etf-classifications`; the COT twin (`opal-data-cot`, SC-e-67, 2 hit keys); D_04 (unchanged).

## Rollback per key

The code object `s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py` is versioned (read-only `list-object-versions`, 2026-10-08):

| VersionId | LastModified | size | role |
|---|---|---|---|
| `xypYDUXvKLIIDTKDioI34eU4XQnb.NDY` | 2026-10-07T04:16:19Z | 42619 | CURRENT deployed (IsLatest): **the rollback target** |
| `lsXrurv05cKGG0NHsd9IWcimUOoaOwZH` | 2026-10-07T00:55:11Z | 42619 | prior |
| `WcIi8IMKB.Qsf5TInBFrsGfTaA3sK5Be` | 2026-10-06T23:47:34Z | 43158 | prior |

Code rollback: copy version `xypYDUXvKLIIDTKDioI34eU4XQnb.NDY` back over the key (`s3api get-object --version-id` then deploy it). That restores the old merge; it does NOT
restore envelope content already healed. Data rollback per key: each envelope `gold/entities/clients/{rid}.json` (and `gold/client_timeseries/{rid}.json`) is overwritten
by the fire; the pre-fire version of each is addressable by its S3 VersionId when the bucket is versioned (z08119861 pre-fire version read 2026-10-08:
`pUkdGIUqCg0Y_I8tkmOHelaTlNn5U.ar`, LastModified 2026-10-08T05:24:01Z). The signer who runs the act records the 36 pre-fire VersionIds (a `list-object-versions` sweep
before the fire) in the ledger entry; this worker did not enumerate all 36 and does not claim bucket versioning for the other keys. The healed content is a strict
subset move (141 holdings, class field and its mix share only), so a restore from the pre-fire version is exact.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-08 ~19:1xZ. I re-ran in the worker tree: AC1 6 passed, AC2 HALF-READY, AC3 82 passed. Merged on dell1
@ebcdfb234b.

**Writers of the envelope `gold/entities/clients/{rid}.json` (and its dual-written legacy key), counted: N = 1.** That writer is
C_06's `_merge_and_write`, whose rule I read. With the fix it rewrites a retained entry only when a holding's class is outside the six.

**Both branches:**
- (a) The next scheduled fire finds a new partition. The rewritten envelopes heal: 141 holdings across 105 entries move from
  multi_asset to equity or fixed_income. D_04 republishes the 36 concentration files.
- (b) No new partition, or a relationship with no new row. Nothing is rewritten and the served files stay exactly as they are; the
  fix never widens them.
The log line `C06-RETAINED-RECLASS` tells the two branches apart.

Accepted limit: 15 of the 105 healed dates keep a mix sum below 0.999 (minimum 0.952), because only the top 10 holdings are kept
(row D1-W65-S2). That does not widen anything; the sums were already short.

Rollback per key: the C_06 code VersionId above. The running seat records the 36 envelope VersionIds before the fire. Deploy through
`.tools/safe-deploy.sh` under a change-management ledger, before the next BD gold fire.

## CTO half -- UNSIGNED

(The CTO half is signed in its own file: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECCLASS_SC_E75_BD_MULTI_ASSET_20261008.md`
@0ca2c444c7, conditions 1-3; ADDENDUM 1 @786720019c.)

## COO half -- ADDENDUM 1 (2.0.0_SA_COO~M1, 2026-10-09 ~06:4xZ; matches the CTO's ADDENDUM 1 @786720019c)

**The blast radius widens by ONE relationship, after the fact, KEEP.** On the 2026-10-09 04:00Z fire, C_06 printed
`C06-RETAINED-RECLASS entries=262 holdings=298`. The signed census counted `multi_asset` only: 141 holdings on 105 entries of 36
envelopes. `reclassify_retained` moves ANY retained holding whose class is outside `SERVED_HOLDING_CLASSES`. The envelope diff
(`R13_CHECKS/e75_retained_reclass_diff.py`, 18,176 envelopes against their previous version; `E75_RETAINED_RECLASS_DIFF_20261009.json`)
splits the 298 into:
- the signed 36 envelopes: 141 `multi_asset` holdings, 84 to equity and 57 to fixed_income, exactly as predicted;
- ONE relationship outside the set, `z08296368`: 157 `other` to commodities, PDBC (Invesco Optimum Yield Diversified Commodity Strategy
  No K-1 ETF), on 157 retained dates. Its three keys moved: `gold/entities/clients/z08296368.json`,
  `gold/client_timeseries/z08296368.json` and `platinum/clients/z08296368/concentration.json`.
Commodities is the correct class for PDBC, and a rollback would re-serve the non-six `other`. **KEEP**, per the CTO's addendum.
Rollback targets stay recorded in the ledger: envelope 8YWPRKyK..., client_timeseries XCWaYCxw..., concentration Ns1L1OCm....
**Forward rule (the CTO's):** a later pair over this writer censuses EVERY class outside the six, not one retired class.
