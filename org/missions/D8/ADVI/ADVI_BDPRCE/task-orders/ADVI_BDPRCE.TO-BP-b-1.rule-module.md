# ADVI_BDPRCE task order -- `BP-b-1` -- THE PRICE RULE R1 AS ONE MODULE (NO WRITER IMPORTS IT; NOTHING SERVED MOVES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~5</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a new module imported by no writer; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the probe reads S3 (`get_object`, `list_objects_v2`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the module, its test and the probe record do not exist (AC1, AC2 FAIL); AC2's grader rejects a non-deterministic probe, a single variant, a write verb in `calls` and an empty exclusion census (33-arm self-test OK). Blindness: AC2 proves shape and determinism, not that R1 is implemented as ruled; AC1's arms prove R1's clauses against planted trades; the issuer re-reads the probe's cited partitions.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-1` (round 2; a new, unimported module and its tests)

Black Diamond prices an asset with no public ticker from the previous trading day's trades. Three differing rules are live today. The CTO ruled the one rule, R1. You write R1 as ONE module so every
later writer can import it; in this round nothing imports it and nothing served changes.

### 1a. R1, verbatim from the CTO's ruling (`org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`; read it)

1. **Input rows:** TRADES only (buys and sells). Every non-trade row (cash dividends, reinvestment cash legs, fees, transfers, journals) is EXCLUDED. A dividend's "price" of 1.0 is a cash amount, not a price.
2. **Distinct:** each `transaction_id` counted ONCE.
3. **Value:** the trade's own executed price per unit (the `price` column), not a derived amount over units. A trade with no price is excluded and counted.
4. **Statistic:** the median over the T-1 trading date's distinct trades. A same-date tie between sources is decided by `SOURCE_RANK`, then a stable sort.
5. **No trades on the date:** no new price. The existing carry-forward and its stated source apply, carried WITH its observation date ("last traded <date>"), never presented as that date's own price.
   **Interpolation is banned**: no value that no trade produced.
6. **Date key (DEC-6):** a row belongs to the target date when its `trade_date` equals the target date, whichever daily partition file carries it.

### 1b. What the data holds (measured on `silver/transactions/2026-10-09.parquet`, 6,278 rows, 1,271 distinct ids)

`transaction_type` values (rows / distinct ids): Buy 2,138/430, Sale 1,955/357, Dividend 816/174 (price 1.0), Cash Deposit 346/83, Dividend Reinvestment 310/60, Transfer In 293/81, Transfer Out 145/29,
Cash Withdrawal 145/30, Journal 56/12, Expense 42/11, Capital Gains 18/2, Interest 14/2. Columns include `transaction_id`, `transaction_type`, `price`, `units`, `market_value`, `trade_date`, `asset_name`.
The existing rule is in `data/black_diamond/scripts/silver/bd_price_update.py`: `SOURCE_RANK` :65-71 (scoped_override -2, yahoo_finance -1, transaction_observed 0, linear_interpolation 2, carry_forward 3), `MAX_UNIT_PRICE` :59 (100,000).

### 1c. The module: `data/black_diamond/scripts/silver/bd_price_rule.py` (new; stdlib and pandas only; no AWS call inside it)

Required behavior, as plain functions with docstrings that quote the R1 clause each implements:
- `TRADE_TYPES_A = frozenset({"Buy", "Sale"})` and `TRADE_TYPES_B = TRADE_TYPES_A | {"Dividend Reinvestment"}`. A is R1 as ruled (buys and sells). B is a SENSITIVITY variant for the CTO (reinvestment buys at an executed price);
  it is never the default. Every other type is excluded and counted by name; a type this list has never seen is excluded as `UNCLASSIFIED` and counted.
- `price_for_date(rows, target_date, trade_types=TRADE_TYPES_A)` -> `{asset_name: {"price", "trade_ids", "rows_used", "excluded_by_type", "no_price_excluded", "conflicting_ids"}}`:
  keep rows whose `trade_date` equals `target_date` and whose `transaction_type` is in `trade_types`; drop rows with a missing, non-positive or >= `MAX_UNIT_PRICE` `price`, counting them in `no_price_excluded`;
  count each `transaction_id` once (keep the FIRST by file order; `conflicting_ids` counts ids whose repeats carried more than one distinct price); the price is the median of the distinct trades' `price`.
  An asset with no qualifying trade is ABSENT from the result (never a placeholder).
- `resolve_source(candidates)`: for rows `{source, price}` of one (date, asset), choose the lowest `SOURCE_RANK` (unknown source last), then a stable key (`asset_name`, then `source` label); use `sorted` with a stable sort. The module's `SOURCE_RANK` is the table above WITH `scoped_override`; the key `linear_interpolation` is not accepted as an output source (raise `ValueError`).
- `carry_forward(last_observed)` -> `{"price", "observed_date", "source": "carry_forward"}` where `last_observed` is `(price, date)`; it never returns a price without its date.
- A `RULE_ID = "R1"` constant and a `__main__` that prints one line `R1 module ok` (so an analyst can see it loads).

### 1d. The test: `data/black_diamond/scripts/silver/tests/test_bd_price_rule.py` (stdlib `unittest` or plain asserts; no AWS)

Planted in-memory frames. It prints one last line `BD PRICE RULE TEST: OK <n> arms` (exit 0), at least these arms; any failing arm prints `BD PRICE RULE TEST: FAIL <arm>` and exits 1:
(1) a repeated `transaction_id` is counted once (rows_used > distinct, price equals the distinct median); (2) a Dividend row with price 1.0 beside two trades does not move the median; (3) the executed `price` column is
used, not `market_value / units` (plant a row where they differ); (4) variant A excludes Dividend Reinvestment and variant B includes it, same frame, different price; (5) a tie between `transaction_observed` and
`scoped_override` resolves to `scoped_override` (rank -2), and two equal-rank candidates resolve identically on two runs and under a shuffled input order; (6) an asset with no qualifying trade is absent, and
`carry_forward` returns its observation date; (7) a row whose `trade_date` differs from the target date is excluded even when it sits in the frame; (8) `resolve_source` refuses `linear_interpolation`;
(9) two runs over the same frame are byte-equal (compare the JSON dump); (10) a trade with a missing price is excluded and counted.

### 1e. The probe: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json`

Run the module over REAL partitions from `opal-data-bd` (`silver/transactions/<date>.parquet`; download to `C:/dev/wk-bdprce-r2-5-data/`): the dates 2026-10-09 and 2026-09-22 (and a third of your choice).
Include in `assets` at least: `EXXONMOBIL HOLDINGS CORP COM SHS` on 2026-10-09 (the round-1 thread asset: expect 168.94) and `BLACKROCK INC COM` on 2026-09-22 (the T1 median read 1.0 because cash rows dominated; R1 must read a trade price).
```json
{"order": "BP-b-1", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api get-object ...", "..."],
 "deterministic": true,
 "variants": {"A_trades_only": {"assets_priced": 0, "assets_absent": 0}, "B_plus_reinvestment": {"assets_priced": 0, "assets_absent": 0}},
 "excluded_by_type": {"Dividend": 0, "Cash Deposit": 0},
 "assets": [{"asset_name": "<name>", "date": "YYYY-MM-DD", "price": 0.0, "distinct_trade_ids": ["..."], "price_variant_b": 0.0}],
 "types_seen": {"<transaction_type>": 0}}
```
`deterministic` is true only when two runs of the whole probe produced byte-equal JSON (state the two md5s in `RULE_PROBE.md`). Also write `RULE_PROBE.md` (one page: R1 as built, what each variant does to the two named assets,
the types seen across the three dates with their counts, and any type you could not classify).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run. You create exactly two repo files outside your deliverables folder (`bd_price_rule.py` and its test); no other product file is edited, and no existing writer imports the module.
2. No client name, account number or advisor name is printed anywhere. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-1 probe needs the key listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
data/black_diamond/scripts/silver/bd_price_rule.py
data/black_diamond/scripts/silver/tests/test_bd_price_rule.py
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/ADVI_BDPRCE.TO-BP-b-1.rule-module.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-1"><invocation>cd /c/dev/wk-bdprce-r2-5 &amp;&amp; timeout 100 python data/black_diamond/scripts/silver/tests/test_bd_price_rule.py</invocation><expect>^BD PRICE RULE TEST: OK [0-9]+ arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-1"><invocation>cd /c/dev/wk-bdprce-r2-5 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py ruleprobe --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json</invocation><expect>^RULEPROBE record ok assets=[0-9]+ deterministic=true excluded_types=[0-9]+$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-b-1"><invocation>cd /c/dev/wk-bdprce-r2-5 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-5 --allow data/black_diamond/scripts/silver/bd_price_rule.py --allow data/black_diamond/scripts/silver/tests/test_bd_price_rule.py --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (R1's clauses against planted trades, with the determinism arm); AC2 is the seam probe against the real partitions; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit the module, its test, `RULE_PROBE.json` and `RULE_PROBE.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W5-S<k>` (the dell1 gate requires the D1 coordinate), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. If the channel file does not exist in your worktree, create it by filing your first row.
Report once: the two named assets' R1 prices (variant A and B), the types seen, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 1 (first half); PRD C5, C6, C7, C8 read this module later. Variant B exists so the CTO can rule on reinvestment rows with numbers; it is never the default. The module sits under
`data/black_diamond/scripts/silver/`, a path the silver script does not sync to the runner (`deploy-to-ec2.sh:16-20`), and nothing imports it: LOCAL. Disarm map: `W2-S2`, `W2-S4`, `W1-S3`, `W3-S3`, `W3-S4` are brought within reach.

<status>pending</status>
<round>2</round>
<workstream>RULE</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-1</to_id>
<slot>~5</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
