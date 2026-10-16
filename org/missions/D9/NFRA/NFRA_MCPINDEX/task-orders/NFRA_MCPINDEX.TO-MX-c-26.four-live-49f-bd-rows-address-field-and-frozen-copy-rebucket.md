# NFRA_MCPINDEX task order -- `MX-c-26` -- the four live opal-data-bd 49F tables as four NEW catalog rows with an `address`, the eight frozen-copy rows back in opal-data-assets, and the `address` field

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-26</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-26</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~49</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change. The cell reads two S3 prefixes' listings (read-only `aws s3 ls`) to measure freshness. The dedicated `-live` read role is NFRA_OPLGTW's (row Z-S292), not this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- the checks re-measure the listing themselves and compare; no row of any other group changes (c26.AC2 and the validator).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-26` (round 19, enrichment E3; CTO rulings 35025 @ed33f552ae and 35038 @96ea4ac3da)

Work in your own worktree (cut from `box/sitez`). Every path is relative to its root. **First**, run once: `git sparse-checkout add workflows lib .tools` (the only sparse change you may make). Read `workflows/atom_decomposition/validate_catalog_v02.py` and the table-row rules in `emit_catalog_v02.py` (search `SILVER_TABLE_FIELDS`, `SILVER_TABLE_OPTIONAL_FIELDS`, `validate_entry`) before you write anything.

**Why.** The Black Diamond 49F client adapter reads four LIVE tables of the bucket `opal-data-bd`: `silver/unrealized/`, `silver/transactions/`, `silver/allocations/`, `silver/fees/`. It finds each through the catalog: it looks for a row whose `address` is `blackdiamond/49f-live/silver/<t>/` (the CTO's rule (a), msg 35025; the adapter code is NFRA_OPLGTW's). Today no such row exists. The catalog has eight rows, `opal_data_assets_silver_49financial_<t>_silver_legacy`, whose bucket is `opal-data-bd` and prefix `silver/<t>/` but whose CONTENT describes the FROZEN COPY in `opal-data-assets` (`blackdiamond/49financial/silver_legacy/<t>/`, newest partition 2026-08-24, open item "FROZEN copy: do not build a tool on this prefix"). The live tables are current (measured 2026-10-16: `silver/fees/` newest file 2026-10-14, `silver/transactions/` newest 2026-10-16, `silver/unrealized/` and `silver/allocations/` weekly, newest 2026-10-09) and are FLAT FILES, `silver/<t>/<YYYY-MM-DD>.parquet`, with no `date=` directory (`silver/unrealized/` also holds a non-dated `unrealized_gain_loss.parquet`, never a partition). The CTO's ruling (msg 35038): add FOUR NEW rows for the live tables; send the eight legacy rows back to `opal-data-assets` at their real prefix, still out of the finish line on their own open items; rewriting the legacy rows in place is refused.

**What to build.**

1. **Four new entry files** `workflows/atom_decomposition/catalog_entries/opal_data_bd_silver_<t>.yaml` for `<t>` in `unrealized`, `transactions`, `allocations`, `fees`. Start from the matching legacy entry (`opal_data_assets_silver_49financial_<t>_silver_legacy.yaml`) as a template of the field set, then write the LIVE truth:
   - `bucket: null` (the group map in item 3 sets it, as for every table row); `prefix: silver/<t>/`; `table: <t>`; `layer: silver`; `format: parquet`; `retired: false`; `read_tool`: `client_get_holdings` for unrealized, `client_get_transactions` for transactions, `client_get_allocation` for allocations, `client_get_fees` for fees; `gap_owner: null`; `firm_scope_rule: firm-scoped`; `firm: null`.
   - NEW field `address: blackdiamond/49f-live/silver/<t>/` (a string ending in `/`).
   - `business_meaning`: a plain statement that this is the LIVE silver table `<t>` of bucket opal-data-bd, prefix silver/<t>/, 49 Financial accounts only (every account id starts z08), Opal-internal principals only until a data grant names the firm, and that the frozen copy of the same name in opal-data-assets is a different row. `example_questions`, `grain`, `never_sum_rules`: keep the legacy entry's where they describe the table's content (same schema), drop any sentence about the frozen copy. `nl_tags`: 3 to 5 plain lowercase words or phrases a person would ask (do not copy the legacy tags unchanged if they name "silver_legacy").
   - `contract`: `id` = `c-` plus the first 12 hex digits of `sha256("opal-data-bd/silver/<t>/")` (unique, new); `label: silver <t> (live)`; `size`: `objects` and `bytes` measured from `aws s3 ls --recursive --summarize s3://opal-data-bd/silver/<t>/ --human-readable` is NOT needed: use `aws s3 ls --recursive s3://opal-data-bd/silver/<t>/` and count the lines and sum the sizes yourself (bound it: write the listing to a file in your deliverables folder first, then count with python), `newest_part` the newest dated file name, `claim: measured`; DROP the row-count fields the legacy entry has (`rows_all_parts`, `rows_newest_part`, `rows_sampled`, `schema_variants`, `parquet_parts`, `row_count_rule`): you did not measure them; `freshness`: `latest_partition` = the newest `YYYY-MM-DD.parquet` file date under `silver/<t>/` (read it from the listing, ignoring non-dated names), `trading_days_behind_t1` computed with `lib.trading_calendar.trading_days_behind(latest_partition, lib.trading_calendar.expected_last_trading_day(<now UTC>))`, `t1_frontier` the `expected_last_trading_day` date, `basis: trading-day-frontier`, `newest_last_modified_utc` from the listing, `claim: measured`; `partition`: `keys: [file-name date]`, `layout: flat files silver/<t>/<YYYY-MM-DD>.parquet, no date= directory`, `claim: measured`; `producer`: `name` that the bd-49f live runners write opal-data-bd silver/ (the exact trigger is not traced here), `schedule` stated from the listing's observed cadence (daily or weekly) and `claim: inferred`.
   - `fork_keys`: the same three keys as the legacy entry; `firm`: `column_or_key_segment: none -- single-firm table, every account id starts z08`, `values: [49financial]`, `claim: inferred`; `account`: `column: account_id` (the live schemas name it so; keep the legacy `last4_*` keys only if you can measure them, otherwise omit those two keys); `platform`: `null`.
   - `open_items`: exactly these items: `flat files silver/<t>/<date>.parquet, no date= directory`; `grain (snapshot or increment) is UNMEASURED (contract decision 8): no tool sums or spans partitions`; `the FROZEN copy of the same name is opal_data_assets_silver_49financial_<t>_silver_legacy in opal-data-assets: do not read it`; and for `unrealized` also `silver/unrealized/ holds a non-dated unrealized_gain_loss.parquet that is never a partition`.
   - Use only the keys the table-row schema allows (`validate_entry`): the C1 fields, `read_tool`, the table fields, `firm`, and the new `address`.
2. **The eight legacy entries** `opal_data_assets_silver_49financial_<t>_silver_legacy.yaml` for `<t>` in `allocations, assets, fees, prices, realized, transactions_enriched, transactions, unrealized`: change ONLY the `prefix:` line to `blackdiamond/49financial/silver_legacy/<t>/`. `read_tool` stays null, `gap_owner` stays NFRA_OPLGTW, the FROZEN open item and every other field stay byte-equal. (The ninth, `single_file`, is already in opal-data-assets and is not touched.)
3. **Two group maps.** (a) In `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json` change `bucket` from `opal-data-bd` to `opal-data-assets` for exactly the eight legacy entities (nothing else in that file changes; its `_about` text stays). (b) Create `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/live_bd_group_map.json` with the same shape as (a) (`_about`, `rows`, `unresolved: []`), `rows` holding the four new entities `opal_data_bd_silver_<t>` each as `{"bucket": "opal-data-bd", "firm": "49financial", "vendor": "blackdiamond"}`; the `_about` text says it is round 19 / MX-c-26 and cites msgs 35025 and 35038. Keep ASCII.
4. **The `address` field.** In `emit_catalog_v02.py` add `address` to the optional table-row fields (beside `firm`) and validate it (when present: a non-empty string ending in `/`; only on a TABLE row); carry it to the emitted table row wherever `firm` is carried (the row builder at the emitter, and `gen_silver_rows.py` if it builds table rows from entries). In `validate_catalog_v02.py` accept it and refuse a duplicate `address` across entries. A row without `address` is byte-equal to today. Do not touch any other field rule.
5. **Tests**: a NEW file `workflows/atom_decomposition/tests/test_address_field.py` with at least 5 tests: an entry with a valid `address` validates; an empty or non-string `address` is refused; `address` on a non-table entry is refused; two entries with the same `address` are refused by the validator; the emitted/built row carries the `address` and a row without one does not gain the key.

### Steps

0. The sparse command above. Then `cd workflows/atom_decomposition && python -m pytest -q -p no:cacheprovider tests/test_c_group.py tests/test_silver_table_grain.py` passes before you start (a control). The AWS CLI is `.tools/aws` (use `.tools/aws s3 ls ...`).
1. Make the changes and the tests. Run the same pytest line with `tests/test_address_field.py` added (all pass). Run `python validate_catalog_v02.py` (no FAIL line).
2. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No `DATA_CATALOG.yaml`, no `catalog_fork_keys.json` (a clean table row with no registry entry is returned unchanged by the join; do NOT add one), no gateway file, no adapter, no grant, role, route, `.env` or AWS change; AWS is read-only listings only. No deploy. No push.
2. The numbers in the new entries are a POINT-IN-TIME read (as every measured claim in the catalog is). `c26.AC1` re-lists the prefixes and compares: run the criteria in the same session you measure, and write down in your report the UTC time of your listing. The issuer re-measures at the release.
3. A value you did not measure is not written as measured: omit it, or mark it `inferred` with its basis.
4. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token); the entry files are data and carry the values.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
6. The checks are `deliverables/2.0.0_SA_COO~MI/round19/checks/c26.AC1.sh`, `c26.AC2.sh`, `c26.AC3.sh` (python `c26_check.py`). Read them for exactly what is graded. Do not edit them.
7. Other workers (`~47`, `~48`) edit the gateway tree and one other entry file at the same time (no shared file).
8. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/catalog_entries/opal_data_bd_silver_unrealized.yaml
workflows/atom_decomposition/catalog_entries/opal_data_bd_silver_transactions.yaml
workflows/atom_decomposition/catalog_entries/opal_data_bd_silver_allocations.yaml
workflows/atom_decomposition/catalog_entries/opal_data_bd_silver_fees.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_allocations_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_assets_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_fees_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_prices_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_realized_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_transactions_enriched_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_transactions_silver_legacy.yaml
workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_49financial_unrealized_silver_legacy.yaml
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/tests/test_address_field.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/live_bd_group_map.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~49/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W49-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-26" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c26.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR live rows present 4 of 4; live group map entries 4; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-26" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c26.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR legacy entries 8; frozen prefixes non-empty 8; group-map legacy rows 9, not in opal-data-assets 0; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-26" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c26.AC3.sh; echo "exit=$?"</invocation><expect>DENOMINATOR entries carrying address 4; pytest rc=0; at least 5 new tests; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~49/NFRA_MCPINDEX.TO-MX-c-26.four-live-49f-bd-rows-address-field-and-frozen-copy-rebucket.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where the count may differ, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in three commits: (i) the emitter, validator, generator and test file; (ii) the entry files and the two group maps; (iii) the proof instance.
4. Report once, with: the four new rows' freshness lines (`latest_partition`, `trading_days_behind_t1`, the UTC time of your listing); the AC1 to AC3 DENOMINATOR and CHECK lines verbatim; the listing counts (objects, bytes) per table; the test count; the three commit shas; and any field you could not measure and how you marked it.

The issuer then merges, re-measures at the release, and re-emits the catalog once with the live group map as a sixth `--group-map`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 19, worker ~49, an independent chain. Source: CTO msgs 35025 (@ed33f552ae, rule (a): an `address` field on the rows), 35038 (@96ea4ac3da, the REC ratified: four NEW live rows, eight legacy rows re-bucketed, rewrite in place refused), and the issuer's measurement of 2026-10-16 ~13:4xZ (the legacy entries describe the frozen copy; the live bd tables are current and flat). Base dry-runs: `c26.AC1` FAIL (0 of 4 live rows), `c26.AC2` FAIL (8 of 9 legacy rows not in opal-data-assets), `c26.AC3` FAIL (no `address` field, no test file). The four client tools named in `read_tool` exist in the tool index; whether they SERVE these rows is NFRA_OPLGTW's `OG-en-11` (address match, flat-file partitions) and the dedicated `-live` role (Z-S292). Newly visible rows at the release: the four new rows are firm 49financial, so they widen catalog visibility for the 49financial principal by four rows; the never-widen pair at `MX-r-16` names them. LOCAL: catalog source and emitter only.

<status>issued</status>
<round>19</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
