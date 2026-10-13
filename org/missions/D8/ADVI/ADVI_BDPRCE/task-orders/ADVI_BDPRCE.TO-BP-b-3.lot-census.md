# ADVI_BDPRCE task order -- `BP-b-3` -- THE W4-S2 CENSUS: EVERY 49F CLIENT OBJECT'S LOTS, PRICED FROM A CANONICAL ROW OR NAMED AS NOT (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~7</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`head-object`, or boto3 `get_object`/`list_objects_v2`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a class partition whose sum differs from `lots_total`, `objects_read` over `objects_total`, a bad extract hash and a write verb in `calls` (33-arm self-test OK). Blindness: the grader proves arithmetic and shape, not that a lot is in the right class; the issuer re-reads sampled lots from their objects.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-3` (round 2; read-only)

A sample of 586 untickered lots (from 26 client objects) found 61 whose served `current_price` matches no canonical price row on the object's as-of date. The round-1 analysis orders the full census:
every client object of 49 Financial's served home, every lot, read once. It also names the holdings the pipeline serves without a ticker although a ticker exists in another source (a mapping gap).

### 1a. What to read

- The served home `opal-data-49financial`, prefix `advi/49financial/platinum/entities/clients/`, one `detail.json` per client object (about 3,509: list the keys and print the count; the catch-all `0/` and the `acct_z...` and `z0...`
  keyed objects are all in scope). Each object has `data_as_of` and `tax.open_lots`: a list of lots with `account_id`, `asset_name`, `ticker`, `quantity`, `current_price`, `market_value`, `acquisition_date`.
- The prices: `opal-data-bd`, `silver/prices/canonical_prices.parquet` (columns date, asset_name, ticker, price, source), read ONCE into memory.
- Other ticker sources for the mapping gap: `opal-data-bd` `config/ticker_lookup.json`, `silver/historical_prices.parquet` (ticker column), and the canonical table's own `ticker` column.
- Read objects in parallel (a thread pool of about 16) with retries; a throttled or missing object is recorded, never skipped silently.

### 1b. Classes (every lot lands in exactly one)

An **untickered lot** has a served `ticker` that is null, empty or `UNKNOWN`. For each untickered lot:
- `PRICED_FROM_CANONICAL`: the canonical table holds a row for that `asset_name` on the object's `data_as_of` date whose `price` equals the lot's `current_price` within `1e-6 * max(1, |price|)`.
- `PRICED_OFF_NO_CANONICAL`: no such row. For each, record the nearest canonical price for the asset on any date within 5 days and whether the lot price equals ANY canonical price of the asset (say which date).
- `NOT_UNTICKERED`: a lot with a served ticker (counted so the denominator is every lot).
Also compute `listed_untickered`: the distinct assets served with a null ticker whose name maps to a ticker in `ticker_lookup.json`, or whose canonical rows carry a non-null ticker, or whose name has a ticker in
`historical_prices.parquet`; give the count of assets and of lots, and the list of asset names (names only).
`by_entity_class`: objects by key class `catch_all` (client_key `0`), `acct_z`, `z0`, `other`.

### 1c. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json`, plus the extract

```json
{"order": "BP-b-3", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api list-objects-v2 ...", "..."],
 "objects_total": 0, "objects_read": 0, "objects_failed": [], "lots_total": 0,
 "classes": {"PRICED_FROM_CANONICAL": 0, "PRICED_OFF_NO_CANONICAL": 0, "NOT_UNTICKERED": 0},
 "by_entity_class": {"catch_all": 0, "acct_z": 0, "z0": 0, "other": 0},
 "listed_untickered": {"count": 0, "lots": 0, "assets": ["<name>"]},
 "off_canonical_detail": {"equals_some_canonical_price": 0, "equals_none": 0, "median_abs_gap_to_nearest": 0.0},
 "market_value_identity": {"lots_checked": 0, "lots_off_quantity_times_price": 0},
 "data_as_of_distribution": {"<YYYY-MM-DD>": 0},
 "extract_file": "C:/dev/wk-bdprce-r2-7-data/lot_extract.csv", "extract_sha256": "<64 hex>", "extract_rows": 0}
```
`extract_file` is a CSV OUTSIDE the checkout with one line per lot: object_key, entity_class, data_as_of, asset_name, ticker_served, current_price, quantity, market_value, price_class, account_ref
(`account_ref` = first 12 hex of sha256 of the account id; never the raw id). The next cell reads it by that absolute path and checks the sha256. Commit a 200-row sample as `lot_extract_sample.csv`.
Also write `CENSUS.md` (one page: the counts, the shapes of the off-canonical lots, the mapping-gap names, how many lots break `market_value = quantity * current_price`, what you could not read).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited. Downloaded objects go to `C:/dev/wk-bdprce-r2-7-data/` (outside the checkout).
2. No client name, account number or advisor name is printed or committed anywhere (the object's `client_name` field is never read into any output). An asset's name is not one. Do not print raw lists of client keys; count them.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-3 census needs the object listing`. A step that cannot finish reports partial counts and `claim: absent` for what was not read; `objects_read` then reads below `objects_total`.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/ADVI_BDPRCE.TO-BP-b-3.lot-census.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-3"><invocation>cd /c/dev/wk-bdprce-r2-7 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py census --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json</invocation><expect>^CENSUS record ok objects=[0-9]+ lots=[0-9]+ off_canonical=[0-9]+ listed_untickered=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-3"><invocation>cd /c/dev/wk-bdprce-r2-7 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-7 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, arithmetic and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The issuer re-reads sampled lots from their objects.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `CENSUS.json`, `CENSUS.md` and the sample FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W7-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: objects read of total, lots total, the three class counts, the listed-but-untickered asset and lot counts,
the market-value identity count, the extract's sha256 and path, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 2; closes the census condition of W4-S2 and W4-S9; its extract is the input of `BP-b-7` (dollar effect) and `BP-b-8` (candidates). The count of lots off quantity x price also bears on W4-S8 and FWD-8.

<status>pending</status>
<round>2</round>
<workstream>CENSUS</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-3</to_id>
<slot>~7</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
