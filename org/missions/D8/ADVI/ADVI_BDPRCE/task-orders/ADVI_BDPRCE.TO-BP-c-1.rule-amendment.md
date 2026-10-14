# ADVI_BDPRCE task order -- `BP-c-1` -- R1 AMENDMENT 1 INTO THE MODULE (NO WRITER IMPORTS IT; NOTHING SERVED MOVES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~13</issued_to>
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

### 1a. The amendment, verbatim in substance

1. **Which rows are trades.** Dividend Reinvestment and Income Reinvestment BUYS count as trades: each is a purchase of units at an executed price per unit. Transfer In, Journal, every cash leg, and every row without an executed market price stay OUT (a transfer moves units at a book value, not a market price).
   So the default trade set A becomes `{Buy, Sale, Dividend Reinvestment, Income Reinvestment}`. Keep a SENSITIVITY name for the old two-type set (`TRADE_TYPES_BUY_SALE`), never the default. Every other type is excluded and counted by name; an unseen type is `UNCLASSIFIED` and counted.
2. **The unit for par-quoted bonds.** R1 serves the PER-UNIT price, the unit of today's served price. For an asset whose executed price is quoted per 100 of par, the executed price is divided by 100. The asset dimension's class field is the identifier; the ratio of `price` to `|market_value|/|units|` is a
   CORROBORATING check only: when the two disagree, that row is WITHHELD with its reason, never guessed. This is an exact scale, not an estimate.
   - The dimension is `silver/bd_assets_dim.parquet` in `opal-data-bd` (12,232 rows). Measured columns: `asset_super_class_bd` ('Fixed Income' on 2,562 rows), `asset_class`, `asset_segment` (for example 'Municipal Bonds Long'), `coupon_rate` (5.25 on MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031), `opal_asset_class` ('fixed_income' 3,121), `ticker`, `cusip`.
     There is NO pricing-convention column.
   - Fixed-income FUNDS are priced per unit (ALLSPRING CORE BOND CIT CLASS E2 serves 10.3525 and is super class Fixed Income), so the class alone would wrongly scale them. A par-quoted CANDIDATE is therefore: `asset_super_class_bd == 'Fixed Income'` AND `coupon_rate` is not null (a coupon-bearing bond).
     Prove on the real dimension and partitions how many assets that selects, and whether any fixed-income asset it leaves unscaled has a price/(market_value/units) ratio near 100 (report them, do not scale them).
   - Corroboration: scale when `price / (|market_value|/|units|)` is within 1 percent of 100; ratio within 1 percent of 1 means the two disagree and the row is withheld (`withheld_disagreement`, with the reason `ratio_near_1`); any other ratio is withheld with `ratio_unrecognised`.
   - The module stays free of AWS: `price_for_date` takes the candidate set as a parameter (`par_quoted_assets`, a frozenset of asset names); the PROBE builds the set from the dimension.
3. **Carry-forward** (unchanged, restated): an asset with no qualifying trade on the date is absent; `carry_forward((price, date))` returns the price WITH its observation date. Interpolation stays banned (`resolve_source` refuses `linear_interpolation`).
4. `RULE_ID` stays `"R1"`; add `AMENDMENT = "R1.1"` and print both on `__main__` (`R1.1 module ok`).

### 1b. The test: `data/black_diamond/scripts/silver/tests/test_bd_price_rule.py` (edited; no AWS)

Update the arms the amendment changes (round 2's arm 4 said variant A excludes Dividend Reinvestment: it now INCLUDES it, and the sensitivity set excludes it) and ADD arms. It prints one last line `BD PRICE RULE TEST: OK <n> arms` with n at least 20, and `BD PRICE RULE TEST: FAIL <arm>` (exit 1) on any failing arm.
Required new arms: (a) a Dividend Reinvestment buy beside a Buy prices from both; (b) Income Reinvestment likewise; (c) Transfer In alone leaves the asset absent; (d) Journal and a cash-leg row are excluded and counted; (e) a par-quoted candidate (planted dimension row with Fixed Income and a coupon) with executed price 104.19 and
`market_value/units` 1.0419 reads 1.0419; (f) the same price with `market_value/units` 104.19 (ratio near 1) is WITHHELD with `ratio_near_1`; (g) a fixed-income fund (no coupon) at 10.35 is NOT scaled; (h) two runs over the same frame are byte-equal; (i) the old two-type set still works as a sensitivity.

### 1c. The probe: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json`

Run the amended module over REAL partitions of `opal-data-bd` (`silver/transactions/<date>.parquet`; download to `C:/dev/wk-bdprce-r3-13-data/`), dates 2026-10-09, 2026-09-22, 2026-10-08 and 2026-10-02, reading each date's partition and the next. Include in `assets` (field `kind`: `trade`, `carry`, `absent` or `withheld`):
BLACKROCK INC COM 2026-09-22 (round 2: absent under buys and sells, 1,074.9259 with reinvestment: expect the reinvestment price now), EXXONMOBIL HOLDINGS CORP COM SHS 2026-10-09 (Transfer In only: absent, expect `absent`),
MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031 2026-10-09 (expect 1.0419), the other two par-quoted rows of the round-2 list (find them in `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/BEFORE_AFTER.csv`, flag `scale_100x`), and ALLSPRING CORE BOND CIT CLASS E2 2026-10-02 (expect 10.3525, not scaled).
```json
{"order": "BP-c-1", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api get-object ...", "..."],
 "amendment": "R1.1", "deterministic": true, "reinvestment_in": true, "transfer_in_out": true,
 "par_quoted": {"class_field": "asset_super_class_bd == 'Fixed Income' and coupon_rate not null", "assets_scaled": 0, "withheld_disagreement": 0,
                "unit_scale_rows_unchanged": 0, "candidates_in_dimension": 0, "fixed_income_unscaled_with_ratio_near_100": []},
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
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/ADVI_BDPRCE.TO-BP-c-1.rule-amendment.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-1"><invocation>cd /c/dev/wk-bdprce-r3-13 &amp;&amp; timeout 100 python data/black_diamond/scripts/silver/tests/test_bd_price_rule.py</invocation><expect>^BD PRICE RULE TEST: OK (2[0-9]|[3-9][0-9]) arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-1"><invocation>cd /c/dev/wk-bdprce-r3-13 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py ruleprobe2 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json</invocation><expect>^RULEPROBE2 record ok amendment=R1.1 assets=[0-9]+ par_scaled=[0-9]+ withheld=[0-9]+$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-c-1"><invocation>cd /c/dev/wk-bdprce-r3-13 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-13 --allow data/black_diamond/scripts/silver/bd_price_rule.py --allow data/black_diamond/scripts/silver/tests/test_bd_price_rule.py --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (each clause on planted frames, at least 20 arms); AC2 is the seam probe against the real partitions and dimension; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit the module, its test, `RULE_PROBE2.json` and `RULE_PROBE2.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W13-S<k>` (the dell1 gate requires the D1 coordinate), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the five named assets' R1.1 prices and kinds, the par-quoted candidate and scaled counts, how many of the eight 100x rows now read UNCHANGED, the types seen, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 1 (first half); R1 Amendment 1 (msgs 5323). Module-only; the replay re-run is `BP-c-2` on this module. Disarm map: brings `W6-S2`, `W3-S3`, `W3-S4` and the writers' rows within reach. Class LOCAL: the module sits under `data/black_diamond/scripts/silver/`, a path the silver script does not sync to the runner, and nothing imports it.

<status>complete</status>
<round>3</round>
<workstream>RULEAMEND</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-1</to_id>
<slot>~13</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
