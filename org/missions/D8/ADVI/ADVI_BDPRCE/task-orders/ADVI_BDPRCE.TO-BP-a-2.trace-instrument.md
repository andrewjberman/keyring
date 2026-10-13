# ADVI_BDPRCE task order -- `BP-a-2` -- THE TRACE INSTRUMENT: A SERVED PRICE TO ITS RULE, ITS TRADE IDS AND ITS RECOMPUTE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP.md</decomp_doc>
<owned_cells>BP-a-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~2</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a new read-only script; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the script reads S3 (`get_object`, `list_objects_v2`, `list_object_versions` through boto3). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the script and the sample do not exist (AC1 and AC2 FAIL); AC2's grader rejects a transaction_observed row with no trade ids and a non-boolean match (14-arm self-test OK). Blindness: AC2 proves the sample's shape, not that its recompute is right; AC1's self-test arms prove the recompute logic against planted trades; the issuer re-reads the sample's cited objects.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-a-2` (round 1; a new read-only instrument, no served file touched)

An analyst must be able to ask "where did this served price come from?" and get the rule and the trades without reading code. You build the instrument that answers it for one (asset, date)
of the 49 Financial served T-1 price. It lives in your deliverables folder, not in `data/black_diamond/scripts/`. It must reproduce what the pipeline does TODAY, bugs included: another cell
measures where today's rule is wrong. It changes no file anywhere but its own outputs.

### 1a. What the pricing pipeline does today (read these lines; the instrument reproduces them)

- `data/black_diamond/scripts/silver/bd_price_update.py`: `SOURCE_RANK` :65-71 (scoped_override -2, yahoo_finance -1, transaction_observed 0, linear_interpolation 2, carry_forward 3);
  `MAX_UNIT_PRICE` :59; `load_transactions_for_date` :263-271 (reads `silver/transactions/<YYYY-MM-DD>.parquet`, no de-duplication on `transaction_id`);
  `extract_t1_prices` :327-344 (valid rows: `asset_name` not null, `units` not null and abs > 1e-8, `market_value` not null and != 0; `calc_price = |market_value| / |units|`;
  keep 0 < calc_price < MAX_UNIT_PRICE; the price is the MEDIAN per `asset_name` over all rows given); `_SCOPED_PRICE_OVERRIDES` :86 on; `upsert_canonical` :587-602.
- The bucket is `opal-data-bd`. Price objects: `silver/prices/<YYYY-MM-DD>.parquet` (columns date, asset_name, ticker, price, source) and `silver/prices/canonical_prices.parquet`.
- `data/black_diamond/scripts/gold/B_01.holdings_lots.py:319-361` (`load_latest_prices`): reads every `silver/prices/*.parquet`, concatenates, sorts by date descending and keeps the FIRST row per
  `asset_name`. A same-date tie between the daily file and the canonical file is therefore settled by sort order, not by `SOURCE_RANK`.

### 1b. The instrument: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py` (stdlib, pandas, pyarrow, boto3 only)

```
python trace_price.py --asset "<asset_name>" --date YYYY-MM-DD [--bucket opal-data-bd] [--out <file.json>]
python trace_price.py --date latest --first-transaction-observed [--out <file.json>]
python trace_price.py --self-test
```

For the (asset, date) it:
1. Reads the served price: the row(s) for the asset on that date in `silver/prices/<date>.parquet` AND in `canonical_prices.parquet`; reports both with their `source`, the object and its VersionId, and which
   one B_01 would keep (state the tie as a tie when both rows carry the same date; do not pick by rank silently).
2. Names the rule by the served row's `source` (one sentence each, citing file:line): scoped_override (the constant list), yahoo_finance (the close in `silver/historical_prices.parquet`),
   transaction_observed (the median above), linear_interpolation, carry_forward.
3. For `transaction_observed`: loads `silver/transactions/<date>.parquet` (the day's partition), applies the rule's filters to the asset's rows, and lists the `transaction_id` of every row used
   (`trade_ids`, in file order, repeats kept), the `rows_used`, the `distinct_trade_ids` and `median_distinct` (the median over distinct ids, informational: it is NOT the rule today).
   `recomputed_price` is the median over ALL rows used, exactly as the rule does today. `match` is `abs(recomputed - served) <= 1e-6 * max(1, abs(served))`.
4. For any other source: `trade_ids` is `[]`, `recomputed_price` is `null`, `match` is `false`, and `rule` says which input the price comes from and where it was read.
5. `--date latest` resolves to the newest `silver/prices/<date>.parquet` in the bucket; `--first-transaction-observed` takes the first row (file order) with `source == transaction_observed`
   that has at least one valid trade in that day's `silver/transactions/<date>.parquet`, and records how many earlier transaction_observed rows it skipped for having none
   (`skipped_without_trades`: a served transaction_observed price with no trade in its day's partition is itself a finding, so report the count, never hide it).

JSON output keys (all required): `asset_name`, `date`, `served_price`, `price_source`, `rule`, `trade_ids` (list), `recomputed_price`, `match` (boolean), plus `rows_used`, `distinct_trade_ids`,
`median_distinct`, `served_from` (object key and VersionId) and `claim` (`measured`).

`--self-test` runs offline against planted in-memory frames and prints one last line `TRACE SELFTEST: OK <n> arms` (exit 0), at least these four arms: (1) three planted trades whose median is known:
`recomputed_price` equals it and `trade_ids` lists the three ids; (2) a planted repeated row (the same `transaction_id` twice): `rows_used` is one more than `distinct_trade_ids`;
(3) a planted served price that differs from the median: `match` is `false`; (4) a `yahoo_finance` row: `trade_ids` is `[]` and `rule` names the close. Any arm failing prints `TRACE SELFTEST: FAIL <arm>` and exits 1.

### 1c. The sample record: `.../deliverables/0.9.0_WK_ADVI_BDPRCE~2/TRACE_SAMPLE.json`

Run `python trace_price.py --date latest --first-transaction-observed --out TRACE_SAMPLE.json` against the real bucket and keep the output. It is the seam probe against the real neighbour.
Also write `TRACE_README.md` (half a page: how to run it, what it does not do: it does not fix a rule, it does not read lots).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited; the script writes only the `--out` file. Downloaded files go to `C:/dev/wk-bdprce-r1-2-data/` (outside the checkout).
2. No client name, account number or advisor name is printed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-a-2 instrument needs the key listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/ADVI_BDPRCE.TO-BP-a-2.trace-instrument.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-a-2"><invocation>cd /c/dev/wk-bdprce-r1-2 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py --self-test</invocation><expect>^TRACE SELFTEST: OK [0-9]+ arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-a-2"><invocation>cd /c/dev/wk-bdprce-r1-2 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round1/checks/r1_checks.py trace --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/TRACE_SAMPLE.json</invocation><expect>^TRACE record ok source=transaction_observed trades=[1-9][0-9]* match=(true|false)$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-a-2"><invocation>cd /c/dev/wk-bdprce-r1-2 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r1-2 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (four planted arms); AC2 is the seam probe against the real served objects (a transaction_observed row traced to at least one trade id); AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `trace_price.py`, `TRACE_SAMPLE.json` and `TRACE_README.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-W2-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the sample's asset (name), date, served price, source, trade count, recompute and match; AC1, AC2, AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD cell C9 (instrument half), FWD-1 and FWD-3 (the instrument is generalised to every price source at the enrichment round). The nearest prior art is `E_06.trace_asset_pricing.py`, which
compares against Yahoo and does not list trades; this order does not extend it. Class LOCAL: a new script under `deliverables/`, reads only.

<status>complete</status>
<round>1</round>
<workstream>TRACE</workstream>
<to_id>ADVI_BDPRCE.TO-BP-a-2</to_id>
<slot>~2</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
