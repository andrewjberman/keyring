# NFRA_MCPINDEX task order -- `MX-c-14` -- a generator writes the 174 table-grain silver rows (client data with its firm / account / platform fork, Opal's own ETFs, mdpf delta tables, news tables) from the CRO's G2, G4, G5 and G6 data contracts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-14</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-14</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~38</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- a generator, a JSON map and YAML catalog source rows only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run plus planted PASS and FAIL arms are the control (decomposition R14.3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-14` (round 14; PRD v0.12 FWD-22 items 1, 3, 4, 5 and PRD v0.13)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root.

**What exists at the base.** `workflows/atom_decomposition/catalog_entries/` holds 5 silver source rows (`schwab_dim_*`, `blackdiamond_fees`), the portal and need rows, and
the harvest rows. No row describes the client-data tables of `opal-data-assets` (Black Diamond, Orion, Eclipse, SmartX, Schwab, Commonwealth, Tax SMA, Opal's own ETFs, Yahoo), the
`opal-data-etfs` bucket, the `opal-data-mdpf` delta feeds or the news DynamoDB tables.

**What you build.** `workflows/atom_decomposition/gen_silver_rows.py`, `workflows/atom_decomposition/client_tool_map.json`, and then the 174 rows the generator writes into `catalog_entries/`.

**The source.** The CRO's census holds one JSON contract per table. Read each file at its PIN, never the working copy, and save it under your deliverables folder
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`:
- G2 (131 contracts): `git show 339a2804d7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G2_assets_silver.md` -> `G2_pinned.md`
- G4 (7): `git show 7ec87a87e5:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` -> `G4_pinned.md`
- G5 (36): `git show 35f45893a7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md` -> `G5_pinned.md`
- G6 (12): `git show 35f45893a7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G6_news.md` -> `G6_pinned.md`
Each holds fenced ` ```json ` blocks; every block that is a dict carrying `contract_id` is one contract (186 in all).

### The generator's interface (fixed: the checks call it)

```
python workflows/atom_decomposition/gen_silver_rows.py --g2 <file> --g4 <file> --g5 <file> --g6 <file> --out <dir> --deployed-tools <json-list-file | census>
```
- Parse the four files. If the counts are not 131, 7, 36 and 12, exit 2 with a message.
- IN SCOPE: every contract EXCEPT those whose `catalog_entry.present` is true AND whose `catalog_entry.data_catalog_key` starts `silver_datasets.` (174 of 186). Those 12 are the Schwab dim contracts, already rowed by the existing `schwab_dim_*` silver rows; skip them and print their `contract_id`s. A contract that points at the `news` channel text is in scope: the channel keeps its text, the table gets its row.
- Write one file per in-scope contract: `<out>/<entity>.yaml`, where `entity` = the lower-cased `contract_id` with every run of characters outside `a-z0-9` replaced by one `_`, stripped of leading and trailing `_`. Entities must be unique; exit 2 if not.
- If `<out>/<entity>.yaml` already exists and holds no `contract` key, exit 3 (never overwrite a row this generator did not write). Write nothing outside `<out>`.
- `--deployed-tools`: a JSON file holding a list of tool names, or the word `census`, which runs `python workflows/atom_decomposition/tool_census.py` and takes the `tool` names of its JSON `tools`.
- Print `wrote 174 rows to <out>`. Write YAML with `yaml.safe_dump(row, f, sort_keys=False, allow_unicode=True)`, UTF-8, LF.

### The row (exactly these keys; `retired_reason` only on a retired row)

| key | value |
|---|---|
| `bucket`, `prefix`, `table`, `layer`, `format` | the contract's `bucket`, `s3_prefix`, `table`, `layer`, `format`, verbatim |
| `business_meaning` | one sentence you compose: layer, format, table, bucket, prefix and the contract's `grain`, then for a `firm-scoped` row `Client data forked by firm, account last-4 and platform; Opal-internal principals only until a data grant names the firm.` else `Opal-internal data.` (at least 40 characters, never starting `NONE`). Then FROZEN OR EMPTY IS NEVER CURRENT (PRD v0.12 item 4): let `n` be the first number found under the contract's `freshness` keys `trading_days_behind_t1`, `trading_days_behind`, `trading_days_behind_T-1`; when `n` exists and is above 5, append ` NOT CURRENT: <n> trading days behind T-1.` (`<n>` as an integer); when the contract's `size.objects` is 0, append ` EMPTY: no objects.`. Append neither otherwise |
| `example_questions` | the contract's `common_queries` verbatim; if empty, one question `Where is the <table> <layer> table?` |
| `grain` | the contract's `grain`, verbatim |
| `freshness_field` | `FIELD:<k>` where `k` is the first entry of the contract's `partition.keys`; if that list is empty, `NONE -- ` followed by the contract's `freshness.basis` |
| `firm_scope_rule` | `firm-scoped` when the contract's `fork_keys.firm.values` holds any value other than `global` and `opal-internal`; otherwise `opal-internal-only` |
| `never_sum_rules` | a one-item list holding the contract's `size.row_count_rule` when it has one; otherwise the string `NONE -- the contract states no row-count rule for this table` |
| `producer` | the contract's `producer.name`, prefixed `inferred: ` when the word `inferred` is in `producer.claim`; when the name is null, `NOT TRACED -- the contract names no producer (absent)` |
| `tools` | `[read_tool]` when `read_tool` is not null, else `[]` |
| `read_tool` | see "read_tool policy" |
| `gap_owner` | `NFRA_OPLGTW` when `read_tool` is null, else null |
| `contract` | a mapping: `id` = `contract_id`; `size`, `freshness`, `partition`, `producer` = the contract's own objects verbatim |
| `fork_keys` | the contract's `fork_keys` object, verbatim |
| `nl_tags` | the contract's `nl_tags` list, verbatim |
| `retired` | `true` for exactly `opal-data-mdpf/feeds/partner_held_etf_49financial` and `opal-data-mdpf/feeds/non_model_aua` (PRD v0.13 marks them do-not-serve), else `false` |
| `retired_reason` | on those two only: `do-not-serve: ` followed by the contract's `routing` string, verbatim |
| `open_items` | the contract's `open_items` list, verbatim |

Write the keys in this order: `bucket prefix business_meaning example_questions grain freshness_field firm_scope_rule never_sum_rules producer tools read_tool gap_owner table layer format contract fork_keys nl_tags retired` (then `retired_reason` if any) `open_items`.

**read_tool policy (PRD v0.12 item 5; a tool that is not deployed is NEVER named).** Let D be the deployed-tools set. For a contract, its CANDIDATES are, in the order of its `proposed_tools`: take each tool's `name`, cut it at the first space (so `blackdiamond_list_fees (extend)` becomes
`blackdiamond_list_fees`), skip a name that starts `none`, then map it through `client_tool_map.json` (a name that is not a key stays as it is). The `read_tool` is the first candidate in D, else null.

**`workflows/atom_decomposition/client_tool_map.json`** is a JSON object, vendor tool name -> `client_*` tool (OPLGTW PRD v3.1 ruling 1: client data is one tool set with vendor adapters). Write exactly these 29 pairs:
```
schwab_resolve_account, blackdiamond_resolve_account, commonwealth_resolve_account            -> client_resolve_account
blackdiamond_get_holdings, schwab_get_positions, orion_get_holdings                           -> client_get_holdings
blackdiamond_list_transactions, schwab_list_transactions, orion_list_transactions, commonwealth_list_transactions -> client_get_transactions
blackdiamond_get_model_assignment, blackdiamond_get_model_targets, orion_get_allocation, smartx_allocation_by_account, smartx_model_assignments, smartx_model_detail -> client_get_allocation
blackdiamond_get_unrealized_lots, blackdiamond_list_realized, schwab_get_realized_lots, schwab_get_tax_lot_detail, schwab_get_unrealized_lots -> client_get_lots
orion_get_household_performance, orion_get_account_performance, commonwealth_get_performance  -> client_get_performance
blackdiamond_get_account_fee_roles, blackdiamond_list_fees                                    -> client_get_fees
blackdiamond_get_account_profile, smartx_account_lookup                                       -> client_get_profile
blackdiamond_list_insurance                                                                   -> client_get_insurance
```
A G2 tool not listed here (balances, find_holders, flows, documents, delivery, the Eclipse tools, prices, workbook rows, platform lists) is NOT mapped: its tables are catalogued with `read_tool` null (OPLGTW: "a table no question reaches is catalogued but gets no adapter this round").

### The steps

1. Write the generator, the map and `workflows/atom_decomposition/tests/test_gen_silver_rows.py` (your own tests: entity uniqueness over the 174, the count refusal, the exit-3 refusal, the read_tool policy under three sets, the two retired rows, `firm-scoped` for a client table and `opal-internal-only` for an ETF table).
2. Run it with `--out workflows/atom_decomposition/catalog_entries --deployed-tools census`. That writes the 174 rows.
3. Print the diff summary (files added) and the counts by `layer` and by `firm_scope_rule`.
4. Run the three criteria below.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `emit_catalog_v02.py`, `validate_catalog_v02.py`, `DATA_CATALOG.yaml`, the tool index, an existing `catalog_entries/` row or the gateway: `2.0.0_SA_COO~MI` regenerates the catalog at the drain, and the loader is another cell's.
   At your commit the loader still refuses your rows (it expects the old shape). That is expected and is not yours to fix. Do not run the emitter.
2. No AWS call, no deploy, no push.
3. The shape of a row is exactly the table above. Do not add, rename or reorder a field. A string the contract holds is copied, never paraphrased.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8).
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/client_tool_map.json
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/test_gen_silver_rows.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W38-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC1.sh; echo "exit=$?"</invocation><expect>ROWS files=174; in-scope contracts=174; entity names unique=yes; missing 0, extra 0, contract.id wrong 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC2.sh; echo "exit=$?"</invocation><expect>ROWS graded 174 of 174; failing fields: none -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC3.sh; echo "exit=$?"</invocation><expect>ARMS pass 5 of 5; rows graded right 870 of 870 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/NFRA_MCPINDEX.TO-MX-c-14.silver-table-rows-generator-g2-g4-g5-g6.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS.
3. Commit everything together.
4. Report once, with:
   - the generator's `--help` line and the diff summary;
   - the number of rows by `layer` and by `firm_scope_rule`;
   - the 12 skipped contract ids;
   - your commit sha.

The issuer then regenerates the catalog from the merged rows and the loader cell's code.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 14, chain head, worker ~38, parallel to the chain `MX-c-11 -> MX-c-13` (no shared file). Source: PRD v0.12 @95d985d1a5
(1.0.0_SA_CTO~Z msg 34100) items 1, 3, 4 (the not-yet-catalogued tables) and 5, and PRD v0.13 @bb9d1ece12 (msg 34117). G3 and the `news` / `ft.04` / `mdpf` channel
corrections are not in this order: they edit CVO-certified channel specs (decomposition R14.6). Battery and planted arms: decomposition R14.3.

<status>issued</status>
<round>14</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
