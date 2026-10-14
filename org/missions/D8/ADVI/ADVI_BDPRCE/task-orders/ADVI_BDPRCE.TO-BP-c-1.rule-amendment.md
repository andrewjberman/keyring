# ADVI_BDPRCE task order -- `BP-c-1` -- R1 AMENDMENTS 1 TO 3 INTO THE MODULE (NO WRITER IMPORTS IT; NOTHING SERVED MOVES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~20</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an edit of a module imported by no writer; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the probe reads S3 (`get_object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the test prints 15 arms (AC1 requires at least 20) and the probe record does not exist (AC2 FAIL); AC2's grader rejects the wrong amendment id, a kept Transfer In, a missing par-quoted block and a non-deterministic probe (35-arm self-test OK). Blindness: AC2 proves shape, not that the amendment is implemented as ruled; AC1's arms prove each clause on planted frames; the issuer re-runs the module on the held partitions.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-1` (round 3; an edit of the module round 2 built)

Round 2 built R1 as one module, `data/black_diamond/scripts/silver/bd_price_rule.py` (read it and `tests/test_bd_price_rule.py` first; the probe `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.md` shows it run). The CTO ruled AMENDMENT 1
(`org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`; read the whole record). You put the amendment into the module. Nothing imports the module and nothing served changes.

### 1.000 CORRECTION OF 1.00 (issuer, 2026-10-14 ~04:3xZ, after the first report of the third seat) -- READ THIS FIRST; it wins over 1.00 items 1 and the probe paragraph

The third seat's first pass built the module logic as ordered and measured that the SOURCE of the unit map was wrong: the lot extract holds 2,909 assets of which only 507 of the 888 served assets, and no per100 asset, so it cannot read the served series' unit (the issuer's error). The module logic (per100 / per_unit / unreadable, as executed, converted_to_per100, `unit_unreadable`) STANDS and is already committed on this branch (ed980d6cd9, 08156c5037). Change ONLY this, as a continuation on the same branch:
1. `served_unit_map(pairs)` stays pure but takes a frame with columns `asset_name`, `served_price`, `per_unit_value` (per_unit_value = |market_value| / |units| of a trade row of that asset, or |market_value| / |quantity| of a lot). Per asset: the MEDIAN of `served_price / per_unit_value` over its pairs (skip a pair with a missing or non-positive value). The bands are COARSE because a pair mixes dates: within 10 percent of 100 -> `per100`; within 10 percent of 1 -> `per_unit`; else, or no pair -> `unreadable` (the median ratio returned beside it). The trade-row ratio test inside `price_for_date` keeps its 1 percent bands.
2. The probe builds the pairs from the SERVED canonical series: the rows of `canonical_prices.parquet` with source `transaction_observed` for 2026-09-16..2026-10-13 (read it as the second replay seat did: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~14/replay_r1_r3.py`) and, for each such (asset, date), the Buy / Sale / reinvestment trade rows of that asset ON that trade_date from the cached partitions under `C:/dev/wk-bdprce-r2-6-data/tx_back/` (READ only; `~14/PARTITIONS2.csv` lists the verified ones). Add the lot pairs (`current_price`, |market_value| / |quantity|) of the extract as a second source. `RULE_PROBE3.json` `served_units` counts the assets of the served set (888 expected) and a new field `units_source` names both sources.
3. The named assets must now read as 1.00 expects: MORGAN STANLEY FIN LLC 0% 05/03/2029 on 2025-05-28 reads 100.0 (per100); MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031 on 2026-10-09 reads 1.0419; the eight round-2 `scale_100x` rows read equal to the served price (8 of 8). If any does not, say which and why in a row; never adjust a number. Rows W20-S1 and W20-S2 are re-read: file new rows for what is still true.
4. Update the test arms for the new input shape (still at least 40 arms); AC1 to AC3 stand as written; the record is overwritten.

### 1.00 AMENDMENT 3 -- THIS ORDER IS REOPENED A SECOND TIME (issuer, 2026-10-14 ~03:5xZ); it REPLACES sections 1c, 4 and the paths below where they differ

You are a THIRD seat of this slot. Your branch inherits both earlier seats' merged work (the module with Amendments 1 and 2, its 36-arm test, `RULE_PROBE2.*`). The CTO ruled AMENDMENT 3 (call 19b2; `org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`, section AMENDMENT 3; read it): **R1 changes a price's VALUE, never an asset's UNIT. Every asset is served in the unit of its own served series.** An asset served per 100 (MORGAN STANLEY FIN LLC 0% 05/03/2029 at 115.995) stays per 100; an asset served per unit stays per unit. The unit of a served series is READ from the served lots; a unit that cannot be read withholds the row with its reason. Build exactly this:
1. `served_unit_map(lots)`, a PURE function (no AWS, no file read) over a frame with the lot extract's price, quantity and market value and asset name columns (read the header of `C:/dev/wk-bdprce-r2-7-data/lot_extract.csv` for the names; its sha256 must read `e7e618d76516c8b7977179aefb3f77ce4fc13c17fbcf1dbeb92001a6e0a2b50b`, else a BLOCKING row and you stop). Per asset: the MEDIAN over its lots of `current_price / (|market_value| / |quantity|)`, skipping a lot with a zero or missing quantity or market value. Within 1 percent of 100 -> `per100`; within 1 percent of 1 -> `per_unit`; anything else, or no usable lot -> `unreadable` (the ratio is returned beside it). Returns `{asset_name: (unit, median_ratio)}`.
2. `price_for_date`, `withheld_for_date` and `exclusion_census` take a REQUIRED keyword `served_units` (asset -> `per100` | `per_unit` | `unreadable`), NO default (no writer imports the module, so the only callers are your test and probe). For a Fixed Income asset (the existing `par_quoted_assets` test): `per_unit` -> Amendment 2 exactly as built (ratio near 100 divided by 100; near 1 left alone). `per100` -> a trade row with ratio near 100 is used AS EXECUTED (counted `par_as_executed`); a trade row with ratio near 1 (a per-unit quote) is MULTIPLIED by 100 into the series' unit (counted `converted_to_per100`); any other ratio is withheld `ratio_unrecognised` with its ratio. `unreadable`, or the asset missing from the map, -> every trade row withheld with reason `unit_unreadable` (new constant `WITHHELD_UNIT_UNREADABLE`). A non-Fixed-Income asset keeps the Amendment 2 behaviour whatever its unit.
3. The carry-forward is unchanged: `carry_forward((price, date))` carries the series-unit price computed at the trade row, so the 1.0-against-per-100 case cannot arise.
4. `AMENDMENT = "R1.3"` (was "R1.2"); `RULE_ID` stays "R1". `__main__` prints `R1.3 module ok`.
Test (`test_bd_price_rule.py`): every existing call now passes `served_units`; arms keep their expectations by passing `per_unit`. ADD arms: a MORGAN-shaped asset (price 100.0, units 250000, market_value 250000) reads 100.0 under `per100` and 1.0 under `per_unit`; a per100 asset with a ratio-near-1 trade (price 1.1599, market_value/units 1.1599) reads 115.99; a per100 ratio-10 row is withheld with its ratio; `unreadable` withholds with `unit_unreadable`; an asset absent from the map withholds with `unit_unreadable`; a per100 carry returns 100.0 with its date; `served_unit_map`: a per100 asset, a per_unit asset, ratio 5 -> `unreadable`, a zero-quantity lot skipped, the median beats one outlier lot; two runs byte-equal. The test prints `BD PRICE RULE TEST: OK <n> arms` with n at least 40.
Probe `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~20/RULE_PROBE3.json` (and `RULE_PROBE3.md`; download partitions to `C:/dev/wk-bdprce-r3-20-data/`): the module run over real partitions of `opal-data-bd` (`silver/transactions/<date>.parquet`) for 2025-05-28 (the date of the MORGAN STANLEY FIN LLC 0% 05/03/2029 par Buy; expect 100.0, not 1.0), 2026-10-09, 2026-09-22 and 2026-10-02, reading each date and the next, with `served_units` built by `served_unit_map` over the extract. Assets (field `kind`: `trade`, `carry`, `absent`, `withheld`): MORGAN STANLEY FIN LLC 0% 05/03/2029; BLACKROCK INC COM 2026-09-22; MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031 2026-10-09 (still 1.0419); the other two rows of the round-2 `scale_100x` list; ALLSPRING CORE BOND CIT CLASS E2 2026-10-02 (still 10.3525). Record shape (the grader is `r3_checks.py ruleprobe3`):
```json
{"order": "BP-c-1", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api get-object ...", "..."], "amendment": "R1.3", "deterministic": true,
 "reinvestment_in": true, "transfer_in_out": true, "extract_sha256": "<64 hex>",
 "served_units": {"assets": 0, "per100": 0, "per_unit": 0, "unreadable": 0},
 "unit_changed_assets": 0,
 "par_quoted": {"class_field": "asset_super_class_bd == 'Fixed Income', then the per-row ratio test and the served unit", "assets_scaled": 0, "withheld_disagreement": 0,
                "unit_scale_rows_unchanged": 0, "per_unit_left": 0, "withheld_ratios": [], "par_as_executed": 0, "converted_to_per100": 0, "unit_unreadable_rows": 0},
 "types_seen": {"<transaction_type>": 0},
 "assets": [{"asset_name": "<name>", "date": "YYYY-MM-DD", "price": 0.0, "kind": "trade", "distinct_trade_ids": ["..."]}]}
```
`unit_changed_assets` is how many of the probe's `trade`/`carry` assets that appear in the extract read a price that is 100x or 1/100 of the extract's served `current_price` (within 1 percent): it must be 0. `unit_scale_rows_unchanged` is still the eight round-2 rows reading equal to the served price (8 of 8).
Proof (replaces section 4): AC1 runs the test (at least 40 arms); AC2 runs `r3_checks.py ruleprobe3` on `RULE_PROBE3.json`; AC3 is the write-surface bound with the same four allows plus this order file. Row ids `ADVI_BDPRCE-D1-W20-S<k>`. The first-seat and second-seat text below stays as history: where it names `~13`, `RULE_PROBE2` or `R1.2`, THIS section wins.

### 1.0 AMENDMENT 2 -- THIS ORDER WAS REOPENED (issuer, 2026-10-14 ~02:2xZ); it REPLACES item 2's identifier below

You are a second seat of this slot. Your branch inherits the first seat's merged work (commits cd073f6a13 and 26132279f9 are in your tree: the module at `data/black_diamond/scripts/silver/bd_price_rule.py`, its test, `RULE_PROBE2.json` and `.md`, rows W13-S1..S7). The CTO ruled AMENDMENT 2
(`org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`, section AMENDMENT 2; read it). Item 2 below ("a par-quoted CANDIDATE is `asset_super_class_bd == 'Fixed Income'` AND `coupon_rate` is not null") is SUPERSEDED: the dimension carries no pricing-convention field and that test reaches only 2 of the 8 rows that read 100x.
The rule now, per ROW:
- The asset class is Fixed Income (`asset_super_class_bd == 'Fixed Income'`; the caller still passes the set of Fixed Income asset names as the parameter, no AWS in the module), AND the row's ratio `price / (|market_value| / |units|)` is within 1 percent of 100: the row is par-quoted and SCALED (executed price divided by 100, exact arithmetic on the row).
- A ratio within 1 percent of 1 is a PER-UNIT quote and is LEFT ALONE (this covers fixed-income FUNDS, which never scale, for example ALLSPRING CORE BOND CIT CLASS E2 at 10.3525). It is NOT withheld (round 3's first seat withheld it as `ratio_near_1`: that changes).
- Any other ratio (or no computable ratio) is WITHHELD with its reason and PRINTED RATIO (`ratio_unrecognised`, ratio value in the row's result and in the probe).
- The dimension `coupon_rate` is a CORROBORATING read only: record, per scaled row, whether the coupon is present; it never decides.
- `AMENDMENT = "R1.2"` (was "R1.1"); `RULE_ID` stays "R1". The 4 dimension names with conflicting rows stay excluded and listed.
Update the test: arm (f) of the first seat (ratio near 1 withheld) now expects the row LEFT ALONE and counted as `per_unit_left`; add arms for: a Fixed Income row with ratio near 100 and a null coupon is scaled (CITIGROUP INC 5.3% 07/22/2032 at 97.021 with market_value/units 0.97021 reads 0.97021); a Fixed Income fund (ratio near 1) is not scaled and not withheld; a ratio of 10 is withheld and its ratio is returned; a non-Fixed-Income asset with ratio near 100 is NOT scaled (it is withheld with its ratio); coupon corroboration is recorded and decides nothing. The test must now print at least 30 arms.
The probe `RULE_PROBE2.json` is re-run and overwritten: it must show all EIGHT round-2 `scale_100x` rows now reading equal to the served price (`unit_scale_rows_unchanged` 8 of 8), `par_quoted.per_unit_left` (a count of Fixed Income rows left alone as per unit) and `par_quoted.withheld_ratios` (a list of the printed ratios of withheld rows, empty if none).

### 1a. The amendment, verbatim in substance

1. **Which rows are trades.** Dividend Reinvestment and Income Reinvestment BUYS count as trades: each is a purchase of units at an executed price per unit. Transfer In, Journal, every cash leg, and every row without an executed market price stay OUT (a transfer moves units at a book value, not a market price).
   So the default trade set A becomes `{Buy, Sale, Dividend Reinvestment, Income Reinvestment}`. Keep a SENSITIVITY name for the old two-type set (`TRADE_TYPES_BUY_SALE`), never the default. Every other type is excluded and counted by name; an unseen type is `UNCLASSIFIED` and counted.
2. **The unit for par-quoted bonds: SUPERSEDED by section 1.0 above (Amendment 2).** R1 serves the PER-UNIT price, the unit of today's served price. The identifier and the ratio test are exactly those of section 1.0. The dimension is `silver/bd_assets_dim.parquet` in `opal-data-bd` (12,232 rows; measured columns `asset_super_class_bd` ('Fixed Income' on 2,562 rows), `asset_class`, `asset_segment`, `coupon_rate`, `opal_asset_class`, `ticker`, `cusip`; there is NO pricing-convention column). The module stays free of AWS: `price_for_date` takes the set of Fixed Income asset names as a parameter (`par_quoted_assets`, a frozenset); the PROBE builds the set from the dimension.
3. **Carry-forward** (unchanged, restated): an asset with no qualifying trade on the date is absent; `carry_forward((price, date))` returns the price WITH its observation date. Interpolation stays banned (`resolve_source` refuses `linear_interpolation`).
4. `RULE_ID` stays `"R1"`; add `AMENDMENT = "R1.2"` and print both on `__main__` (`R1.2 module ok`).

### 1b. The test: `data/black_diamond/scripts/silver/tests/test_bd_price_rule.py` (edited; no AWS)

Update the arms the amendment changes (round 2's arm 4 said variant A excludes Dividend Reinvestment: it now INCLUDES it, and the sensitivity set excludes it) and ADD arms. It prints one last line `BD PRICE RULE TEST: OK <n> arms` with n at least 30, and `BD PRICE RULE TEST: FAIL <arm>` (exit 1) on any failing arm.
Required new arms: (a) a Dividend Reinvestment buy beside a Buy prices from both; (b) Income Reinvestment likewise; (c) Transfer In alone leaves the asset absent; (d) Journal and a cash-leg row are excluded and counted; (e) a Fixed Income asset with executed price 104.19 and
`market_value/units` 1.0419 reads 1.0419; (f) the same price with `market_value/units` 104.19 (ratio near 1) is LEFT ALONE and counted as `per_unit_left` (Amendment 2: not withheld); (g) a fixed-income fund (no coupon) at 10.35 is NOT scaled; (h) two runs over the same frame are byte-equal; (i) the old two-type set still works as a sensitivity.

### 1c. The probe: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json`

Run the amended module over REAL partitions of `opal-data-bd` (`silver/transactions/<date>.parquet`; download to `C:/dev/wk-bdprce-r3-13-data/`), dates 2026-10-09, 2026-09-22, 2026-10-08 and 2026-10-02, reading each date's partition and the next. Include in `assets` (field `kind`: `trade`, `carry`, `absent` or `withheld`):
BLACKROCK INC COM 2026-09-22 (round 2: absent under buys and sells, 1,074.9259 with reinvestment: expect the reinvestment price now), EXXONMOBIL HOLDINGS CORP COM SHS 2026-10-09 (Transfer In only: absent, expect `absent`),
MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031 2026-10-09 (expect 1.0419), the other two par-quoted rows of the round-2 list (find them in `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/BEFORE_AFTER.csv`, flag `scale_100x`), and ALLSPRING CORE BOND CIT CLASS E2 2026-10-02 (expect 10.3525, not scaled).
```json
{"order": "BP-c-1", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api get-object ...", "..."],
 "amendment": "R1.2", "deterministic": true, "reinvestment_in": true, "transfer_in_out": true,
 "par_quoted": {"class_field": "asset_super_class_bd == 'Fixed Income', then the per-row ratio test", "assets_scaled": 0, "withheld_disagreement": 0,
                "unit_scale_rows_unchanged": 0, "per_unit_left": 0, "withheld_ratios": [], "coupon_corroborated_scaled_rows": 0, "scaled_rows": 0, "fixed_income_assets_in_dimension": 0},
 "types_seen": {"<transaction_type>": 0},
 "assets": [{"asset_name": "<name>", "date": "YYYY-MM-DD", "price": 0.0, "kind": "trade", "distinct_trade_ids": ["..."]}]}
```
`unit_scale_rows_unchanged` is how many of the eight round-2 `scale_100x` rows now read equal to the served price within `1e-6 * max(1, |served|)`. `deterministic` is true only when two runs of the whole probe produced byte-equal JSON (state the two md5s in `RULE_PROBE2.md`).
Also write `RULE_PROBE2.md` (one page: the amendment as built, the dimension rule and its counts, what each named asset reads now against round 2, the types seen, anything you could not classify).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run. You edit exactly the two module files outside your deliverables folder; no other product file is edited, and no writer imports the module.
2. No client name, account number or advisor name is printed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-1 probe needs the key listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
data/black_diamond/scripts/silver/bd_price_rule.py
data/black_diamond/scripts/silver/tests/test_bd_price_rule.py
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~20/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~20/ADVI_BDPRCE.TO-BP-c-1.rule-amendment.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-1"><invocation>cd /c/dev/wk-bdprce-r3-20 &amp;&amp; timeout 100 python data/black_diamond/scripts/silver/tests/test_bd_price_rule.py</invocation><expect>^BD PRICE RULE TEST: OK ([4-9][0-9]) arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-1"><invocation>cd /c/dev/wk-bdprce-r3-20 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py ruleprobe3 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~20/RULE_PROBE3.json</invocation><expect>^RULEPROBE3 record ok amendment=R1.3 assets=[0-9]+ per100=[0-9]+ per_unit=[0-9]+ unreadable=[0-9]+ unit_changed=0$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-c-1"><invocation>cd /c/dev/wk-bdprce-r3-20 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-20 --allow data/black_diamond/scripts/silver/bd_price_rule.py --allow data/black_diamond/scripts/silver/tests/test_bd_price_rule.py --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~20/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md --allow org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-c-1.rule-amendment.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (each clause on planted frames, at least 30 arms); AC2 is the seam probe against the real partitions and dimension; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit the module, its test, `RULE_PROBE3.json` and `RULE_PROBE3.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W20-S<k>` (the dell1 gate requires the D1 coordinate), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the five named assets' R1.2 prices and kinds, the par-quoted candidate and scaled counts, how many of the eight 100x rows now read UNCHANGED, the types seen, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 1 (first half); R1 Amendment 1 (msgs 5323). Module-only; the replay re-run is `BP-c-2` on this module. Disarm map: brings `W6-S2`, `W3-S3`, `W3-S4` and the writers' rows within reach. Class LOCAL: the module sits under `data/black_diamond/scripts/silver/`, a path the silver script does not sync to the runner, and nothing imports it.

**REOPENED ~03:5xZ for AMENDMENT 3 (third seat ~20); the note below is the history of the second seat.** **CLOSED (2.0.0_SA_COO~K1, 2026-10-14 ~03:3xZ), second seat, AC1 and AC2 PASS; AC3 note:** the worker's instance reads AC3 FAIL because the checker counts the ISSUER's own face-cleaning commit 544d551f1d (this order file) as an outside change; the worker wrote nothing outside its surface. The issuer re-ran AC3 with this order file allowed: `ROUND 4 SCOPE: OK 8 changed, 0 outside, 0 required missing`. The instance is left as the worker wrote it.

<status>pending</status>
<round>3</round>
<workstream>RULEAMEND</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-1</to_id>
<slot>~20</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
