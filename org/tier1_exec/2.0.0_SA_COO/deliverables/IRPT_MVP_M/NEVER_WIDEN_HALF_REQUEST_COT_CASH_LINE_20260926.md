# Never-widen half requested -- COT: Black Diamond's cash line is `cash`, not the ticker CASH's equity

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`, 2026-09-26 ~22:5xZ. Asked by CTO msg 101547: "the COT
cash line ... is a served error. Bring its own half: class it `cash` by its Black Diamond row rather than the ticker,
with the per-firm delta."

**Recommendation:** sign. Deploy the COT gold part after Monday's cash read-back (ledger cot-cash-admission-m-20260925
R1), so that read-back stays clean. The Holdings part rides the R4 enable publication.

## The error

- The ticker `CASH` is **Pathward Financial Inc** in bd-securities (equity; the one 49F node is CUSIP 59100U108, 200.7655
  units). Black Diamond also uses ticker `CASH` with asset name `CASH` for its OWN cash line; fact_holdings marks those
  rows `Cash Equivalent = true`.
- Every COT classifier resolves by ticker first, so BD's cash line is served as Pathward's class, equity:
  - C_06 `classify_holding`, D_03 `classify_series`, and D_04 at both classify sites;
  - Holdings `classify_security`.
  - The name-based cash fallbacks in D_03/D_04 never run, because the ticker already answered.

## The fix (code 8a52e2c352 + f28c0d89f2, branch `irpt-m-cot-cash-line`, NOT merged)

- `is_bd_cash_line(ticker, asset_name)`: ticker `CASH` AND asset name exactly `CASH` gives `cash`, checked BEFORE the
  classifier, in COT C_06, D_03 and D_04 (both sites).
- Holdings `classify_security(..., description=)`: the same rule on the row's own asset name (`display.description`),
  NEVER the label. A 49F Pathward node's label is its symbol `CASH`, and it stays equity. Basis `NAME_PATTERN`, inside
  the contract enum.
- The branch is held off CLOUD on purpose: a CLOUD commit to a COT gold script deploys on the next push (S141).
- Tests: COT test_other_admission 4 passed; investor_reporting 282 passed (including Pathward staying equity);
  commit-gate clean.

## Served delta, per firm (read from the producers' rules on the served inputs)

| Firm | Reader | Moves | Measure |
|---|---|---|---|
| COT | C_06 client mix (2026-09-22 canonical) | equity -> cash | 853 rows in 853 accounts, 71 nonzero in 29 relationships, net $59,253,165.31 (largest z09305653 +$63,196,106.53; some rows are negative cash) |
| COT | D_03 composition, D_04 portal summary | equity -> cash, the same rows | the same rows as C_06 |
| COT | Holdings (served 2026-09-22 revision) | SECURITY equity -> cash | 884 nodes, $62,076,247.51 |
| BD | C_06 / D_03 / D_04 | none | BD's one CASH row is PATHWARD FINANCIAL INC COM: equity, unchanged |
| 49F | Holdings | none | the Pathward node has no description, so the rule does not fire |
| INF | Holdings | none | no CASH-symbol nodes |

## Readers of the moved value

- `cash` is already an admitted class:
  - C_06 MIX (deployed as its own act, cot-cash-admission-m-20260925);
  - D_03 labels (`'cash': 'Cash'`);
  - D_04 mix loop;
  - the Holdings enum and contract;
  - the AI Cottonwood views, which render cash on PROD (36a37afc).
- No reader crashes or drops it.
- **Named, not fixed here:** a07 `dim_asset_classification` (49F runners owner) ports the same ticker-first classify,
  so the COT mix summary d08 keeps BD's cash line as equity until a07 takes the same rule. That is its owner's act,
  routed by the CTO.

## Order and rollback

1. After ledger cot-cash-admission-m-20260925 R1 reads back on Monday: merge the branch, then safe-deploy C_06, D_03
   and D_04 under their own ledger. The COT mix moves at the next scheduled run; read back z09305653's cash slice.
2. The Holdings change rides the R4 enable publication (the pinned diff lists it as its own class).

Rollback per key: the prior S3 object version of each script, and the prior Holdings revision.

## Addendum 1 (~23:0xZ): the re-cut after the CRO's refusal (@9946616779)

- **Refused, correctly:** C_06's guard sat in `classify_holding`, which has 0 callers. The served mix classifies through
  `classify_series` (C_06:471, reached through the call at :217), so C_06 would have stayed equity while D_03/D_04 moved.
- **Re-cut @9e3f568d42** (branch `irpt-m-cot-cash-line`, still NOT merged): the guard sits in `classify_series` before
  the classifier call, and has left `classify_holding`. The test calls `classify_series`: CASH/CASH gives cash,
  CASH/Pathward gives equity.
- **Real run on the branch:** `classify_series` over COT canonical 2026-09-22 classes all 853 CASH/CASH rows cash,
  $59,253,165.31.
- **Census of every classifier call in C_06, D_03 and D_04 (CTO 101583):** 5 calls. The 4 on served paths are guarded
  (C_06:217 by :213; D_03:133 by :131, reached from :686; D_04:1346 by :1344; D_04:2916 by :2914). The 1 unguarded call,
  C_06:186 `classify_holding`, has 0 callers.

## Addendum 2 (~23:3xZ): the negative-cash census (CRO msg 101595)

Script `cot_cash_line_negative_census.py`, output `COT_CASH_LINE_NEGATIVE_CENSUS_20260926.json` (beside this file), on
the served input `gold/canonical/holdings/2026-09-22.parquet` with the ghost exclusion (4 accounts).

- **The 29 relationships:** 71 nonzero cash-line rows (45 positive, 26 negative, the negatives -$6,802,732.49).
  - 17 of 29 net negative on the cash line itself.
  - 13 of 29 net negative in the whole cash class after the move; other cash rows offset the other 4.
- **C_06 renders no negative.** C_06:462 drops `market_value <= 0` before it classifies, before and after the fix.
  - Correction to the table above: C_06 moves the 45 positive rows, **+$66,055,897.80 in 15 relationships**. The
    $59,253,165.31 is the signed net, which only D_03 sees.
- **D_04 renders no negative.**
  - The firm mix takes C_06's values (D_04 :565-583).
  - Both lot-based classify sites (account summaries :1297, advisor positions :2852) skip for COT, because
    `gold/timeseries/holdings_lots/` holds 0 partitions.
- **D_03 renders no negative slice, but 13 relationship compositions go over 100%.** D_03 keeps negative rows. When a
  relationship's cash class nets to 0 or less, `_build_composition` drops the class (:407), while `total_mv` still
  carries the negative, so the rendered slices sum to 100.5%-128.0%. The largest is z09305707: before, 100.0%; after,
  128.0%. Before the fix, all 29 sum to 100.0%, because the debit netted inside equity.
- **AI Cottonwood views render no negative.** `normalizeMixTo4Class` (composition.ts :119-125) re-percents over the
  kept classes. For those 13 relationships, cash disappears and equity reads high.
- **Other negative rows in the partition:** 3, all personal liabilities (INVESTOR MANUAL ASSET - MORTGAGE -$544,000,
  CAR -$21,521, CREDIT CARD -$9,000).
- **d08 beside C_06:** printed at the Monday read-back, as asked.

**Ask (one decision):** D_03 cannot deploy as cut. REC (a): D_03's composition takes C_06's own rule, positive rows
only (`market_value > 0`, C_06:462), so the two agree. The rule would also drop the 3 personal-liability rows from D_03,
and that delta is measured before the deploy. (b): deploy C_06 and D_04 only, and hold D_03 on today's code. The
relationship composition then keeps the cash line as equity while C_06 shows cash.

## Addendum 3 (~23:5xZ): ruling (a) built, and every moved D_03 scope measured (CTO 101616, CRO 101619)

**Code:** `irpt-m-cot-cash-line` @0deac23f1e, still NOT merged.
- `positive_rows()` in D_03 keeps `market_value > 0` before the ghost exclusion and the classification, as C_06:462
  does.
- New test `test_d03_composition_never_exceeds_100_with_a_negative_cash_line`. test_other_admission.py has 5 tests and
  all 5 pass. The commit message says 6; that count is wrong.

**Measurement:** `d03_positive_rows_diff.py` produced `D03_POSITIVE_ROWS_DIFF_20260926.json` (beside this file).
- It runs D_03's own steps for BOTH versions (CLOUD code, then the branch) on `gold/canonical/holdings/2026-09-22.parquet`:
  canonical holdings, the open filter, ghost exclusion, classification, the architect join (client_dimension fallback,
  as D_03 does) and the canonical-AUA normalization.
- It then calls each version's `_build_composition` for every scope.
- **Scopes:** 1 firm, 222 relationships, and 0 advisor compositions (every architect resolves to Unassigned, for both
  versions).

**Results:**
- **Over 100.0% (tolerance 0.05pp):** 0 of 223 before, and **0 of 223 after**. This is the pre-deploy form of condition
  (2); the post-deploy read repeats it.
- **Totals do not move for any scope.** D_03 scales each composition to the account_performance AUA (:382-386), so
  dropping the negative rows changes the mix, not the total.
- **Mix moves:** the firm plus **27 relationships** move by $1 or more, or by 0.005pp or more. Another 22 move by under
  $1 (a rounding change in the AUA scale factor); they are listed by id in the JSON.
  - All 17 cash-line net-negative relationships are among the moves; z09305667 (-$1.07) is in the under-$1 set.
  - Largest: z09305653, cash 0.4% -> 82.5% (the $63.2M BD cash line); z09305727, 0% -> 17.6%.
  - The firm's cash share goes from 3.50% to 15.33%.
  - The JSON's `material_moves` has every row: before and after cash, equity and other, the largest class move, and the
    largest pp move.
- **The 3 personal-liability rows (condition 1), all in relationship z09305672:**
  - rows: Mortgage -$544,000 (z0927135161), Car -$21,521 (z0927135171), Credit Card -$9,000 (z0927137001);
  - total unchanged at $8,838,093.55;
  - before: equity 79.65%, fixed_income 15.40%, alternatives 4.61%, cash 0.34%;
  - after: 80.51%, 14.45%, 4.33%, 0.71%.
- **Found, not fixed here:** the classifier puts those three liabilities in `equity`, and they are dropped only because
  they are negative. Under Andrew-direct 02:3xZ ("the only context for other is personal assets ... their credit card
  line"), they are `other`. Owner: ~M, under the R5 `other` admission, as its own measured half.
  - **Correction (00:0xZ 09-27):** no new half is needed. All three (`NAME::INVESTOR MANUAL ASSET - MORTGAGE`, `- CAR`,
    `- CREDIT CARD`) are already among COT-new Part 2's 26 `other` keys, signed @ab4a2e41bb. Part 2 makes them
    `other`; the positive-rows rule still keeps them out of C_06 and D_03, because they are negative.
- **C_06 (condition 3):** its delta is +$66,055,897.80 over the positive rows (addendum 2), replacing the $59.25M net.

## Addendum 4 (00:1xZ 09-27): the served baseline for the post-deploy check

Script `cot_served_composition_check.py`, output `COT_SERVED_COMPOSITION_BASELINE_20260927.json` (beside this file).
It reads every SERVED D_03 composition in s3://opal-data-cot: the firm file plus 225 relationship files.

- **9 served relationship compositions sum above 100% today** (100.24%-112.29%): z09304677, z09305548, z09305614,
  z09305639, z09305643, z09305647, z09305707, z09305719 and z09305724.
- **Why:** the files were generated 2026-09-23 11:35Z by the D_03 that S3 served then (version mHFLoYZcd1, 2026-07-07).
  That version put unknowns in `other` (z09304677 serves BRK.B as `other`) and drops a class whose value is 0 or less.
- **The deployed D_03 has not run on a schedule yet:** S3 version lv.RgLOiJs, 2026-09-26 02:39Z.
- **Correction to addendum 3's "0 of 223 before":** that count is the CLOUD code on the 09-22 input. The served bytes
  differ; they are the 9 above.
- The "after" bar is unchanged: **0 over 100%** at the first scheduled run that carries this act.
- **Also in the served set:** 3 relationship files are stale, with data_as_of 2026-08-25, 2026-08-28 and 2026-09-18 (2
  files each counted with the firm set; see the JSON). D_03 no longer writes them. Parked, not in this act.
- **Monday:** re-run this script after the run. Before the merge it reads the act-1 and cash-admission bytes; after
  the cash-line deploy, the bar is 0.
