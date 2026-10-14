# ADVI_BDPRCE task order -- `BP-c-7` -- WHERE DID THE PRICES OF THE 1,859 LOTS "PRICED OFF NO CANONICAL ROW" COME FROM? (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~19</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a class partition whose sum differs from `lots_total`, a class with rows but no exemplar, a bad extract hash, named-other-source rows with no named source and a write verb in `calls` (35-arm self-test OK). Blindness: the grader proves arithmetic and shape, not that a lot is in the right class; the issuer re-reads one exemplar per class.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-7` (round 3; read-only)

The full lot census (round 2, `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json`, `CENSUS.md`; read them first) found 1,859 of 5,121 non-cash untickered lots served at a `current_price` that equals NO canonical price row for the asset on the object's `data_as_of` date. 300 of them equal a canonical price more than 5 days away, and 1,559 equal none.
Example: a lot of VANGUARD MORNINGSTAR GROWTH ETF served 83.78 on 2026-10-09 while canonical reads 91.983333 and holds no row equal to 83.78 on any date (row `ADVI_BDPRCE-D1-W4-S2`, ARMED). The served lot object does not say which source priced it. You find where each price came from.

### 1a. What to read

The extract is on local disk and OUTSIDE the checkout: `C:/dev/wk-bdprce-r2-7-data/lot_extract.csv` (198,295 rows; check its sha256 against `extract_sha256` in `CENSUS.json`, expected `e7e618d76516c8b7977179aefb3f77ce4fc13c17fbcf1dbeb92001a6e0a2b50b`; a mismatch is a BLOCKING row and you stop).
The 1,859 lots are those with `price_class == PRICED_OFF_NO_CANONICAL` (never print a client or account name; `account_ref` is a digest).

For each distinct (asset, `current_price`, `data_as_of`) among them (there are fewer than 1,859 distinct triples; classify per lot but search per triple), look for the price in, in this order (the first that matches takes the lot):
1. `EQUALS_OLDER_CANONICAL_VERSION`: a price the canonical table carried for the asset in an OLDER VERSION of `silver/prices/canonical_prices.parquet` (the bucket is versioned; the object has several hundred versions; read versions selectively with a ranged or full `get-object --version-id`, a handful at a time, choosing versions around the asset's relevant dates: start with the version times of the last 14 days; widen only as needed) at any date.
2. `EQUALS_DAILY_FILE_ROW`: a price in a `silver/prices/<date>.parquet` daily file (any date, any version) for the asset.
3. `EQUALS_NAMED_OTHER_SOURCE`: a price you can trace to another source in the estate and NAME: the gold lots builder's own paths (`data/black_diamond/scripts/gold/B_01.holdings_lots.py`: the synthetic injection, the HLOT2 re-open, the ULN sleeve apportionment, an override, the silver-noncash cap, a Schwab RPS price), `silver/historical_prices.parquet`, a scoped override constant, a ticker correction. Name the source (file and line) in `named_sources`.
4. `UNEXPLAINED`: none of the above. Say which of the above you could and could not read.
Print the denominator (`lots_total` must be 1,859 or what the extract says; if it differs, say so).

For the biggest group of lots in each class, give an exemplar: the asset name, the served price, the `data_as_of`, and where you found the price (version id and date, daily file key, or source and line). 

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~19/OFFCANON.json`

```json
{"order": "BP-c-7", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api list-object-versions ...", "..."],
 "lots_total": 0, "distinct_triples": 0, "extract_sha256": "<64 hex>", "versions_read": 0,
 "classes": {"EQUALS_OLDER_CANONICAL_VERSION": 0, "EQUALS_DAILY_FILE_ROW": 0, "EQUALS_NAMED_OTHER_SOURCE": 0, "UNEXPLAINED": 0},
 "named_sources": ["<source and file:line>"],
 "exemplars": {"<class>": "<asset, served price, data_as_of, where found>"},
 "by_asset_kind": {"<kind>": 0}}
```
The four class keys are exactly those (a closed set); their sum MUST equal `lots_total`; every class with rows has an exemplar; `named_sources` is non-empty when `EQUALS_NAMED_OTHER_SOURCE` has rows. Write `OFFCANON_LOTS.csv` (one line per lot: object key hash, asset name, served price, data_as_of, class, evidence reference; no raw object key of a normal client, only the key class and a digest). Commit it only if under 5 MB.
Also write `OFFCANON.md` (one page in plain words: the counts by class, the biggest groups, what each source means for the served price, what a later fix would change (named, not made), what stays unexplained).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r3-19-data/` (outside the checkout).
2. No client name, account number or advisor name is printed or committed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-7 needs the version listing`. A step that cannot finish reports partial counts and `claim: absent` for what was not read; never a class assigned by guess.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~19/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~19/ADVI_BDPRCE.TO-BP-c-7.offcanon-source.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-7"><invocation>cd /c/dev/wk-bdprce-r3-19 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py offcanon --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~19/OFFCANON.json</invocation><expect>^OFFCANON record ok lots=[0-9]+ older_canonical=[0-9]+ daily=[0-9]+ other=[0-9]+ unexplained=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-7"><invocation>cd /c/dev/wk-bdprce-r3-19 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-19 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~19/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, arithmetic and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The issuer re-reads one exemplar per class.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `OFFCANON.json`, `OFFCANON.md` and `OFFCANON_LOTS.csv` (if under the bound) FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W19-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the denominator, the four class counts, the versions read, the named sources with file and line, one exemplar per class, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 5 (second half); closes the census condition of `W4-S2`; brings `W7-S4` and `W4-S8` into view (the identity counts). The fix of a lot's price source is a later cell under FWD-7. Read-only; class LOCAL.

<status>complete</status>
<round>3</round>
<workstream>OFFCANON</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-7</to_id>
<slot>~19</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
