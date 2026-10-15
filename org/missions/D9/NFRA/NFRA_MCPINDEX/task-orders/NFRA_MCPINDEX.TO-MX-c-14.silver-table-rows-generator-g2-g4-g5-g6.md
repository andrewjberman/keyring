# NFRA_MCPINDEX task order -- `MX-c-14` -- a generator writes the 216 table-grain silver rows (client data with its firm / account / platform fork, Opal's own ETFs, mdpf delta tables, news tables) from the CRO's G2, G4, G5 and G6 data contracts

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

**What you build.** `workflows/atom_decomposition/gen_silver_rows.py`, `workflows/atom_decomposition/client_tool_map.json`, and then the 216 rows the generator writes into `catalog_entries/`.

**The source.** The CRO's census holds one JSON contract per table. Read each file at its PIN, never the working copy, and save it under your deliverables folder
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`:
- G2 (131 contracts): `git show 339a2804d7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G2_assets_silver.md` -> `G2_pinned.md`
- G4 (7): `git show 7ec87a87e5:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` -> `G4_pinned.md`
- G5 (36): `git show 35f45893a7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md` -> `G5_pinned.md`
- G3 (42, the portal-v2 served and platinum objects): `git show 339a2804d7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md` -> `G3_pinned.md`
- G6 (12): `git show 35f45893a7:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G6_news.md` -> `G6_pinned.md`
- G2f (8 live-store records, the 49F Black Diamond tables in opal-data-bd): `git show 5e5d312ada:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/parts/G2f_bd_live_prefixes.md` -> `G2f_pinned.md`. Each fenced json block that is a dict carrying `contracted` and `live` is one record (8 in all).
Each holds fenced ` ```json ` blocks; every block that is a dict carrying `contract_id` is one contract (228 in all).

### The generator's interface (fixed: the checks call it)

```
python workflows/atom_decomposition/gen_silver_rows.py --g2 <file> --g4 <file> --g5 <file> --g6 <file> --g3 <file> --g2f <file> --out <dir> --deployed-tools <json-list-file | census>
```
- Parse the four contract files and the G2f file. If the counts are not 131, 7, 36, 12 and 42 contracts and 8 G2f records, exit 2 with a message. A contract is MAPPED when its `s3_prefix` equals a G2f record's `contracted` (8 contracts).
- IN SCOPE: every contract EXCEPT those whose `catalog_entry.present` is true AND whose `catalog_entry.data_catalog_key` starts `silver_datasets.` (216 of 228). Those 12 are the Schwab dim contracts, already rowed by the existing `schwab_dim_*` silver rows; skip them and print their `contract_id`s. A contract that points at the `news` channel text is in scope: the channel keeps its text, the table gets its row.
- Write one file per in-scope contract: `<out>/<entity>.yaml`, where `entity` = the lower-cased `contract_id` with every run of characters outside `a-z0-9` replaced by one `_`, stripped of leading and trailing `_`. Entities must be unique; exit 2 if not.
- If `<out>/<entity>.yaml` already exists and holds no `contract` key, exit 3 (never overwrite a row this generator did not write). Write nothing outside `<out>`.
- `--deployed-tools`: a JSON file holding a list of tool names, or the word `census`, which runs `python workflows/atom_decomposition/tool_census.py` and takes the `tool` names of its JSON `tools`.
- `--registry-file <path>` (optional): add to that `legacy_addresses.json` the `catalog-*` rows described under "The registry files" (replace every row whose key starts `catalog-`; touch no other row), keeping the file's `_about` and its JSON layout (indent 1).
- `--fork-registry-file <path>` (optional): write the fork registry file described there.
- Print `wrote 216 rows to <out>`. Write YAML with `yaml.safe_dump(row, f, sort_keys=False, allow_unicode=True)`, UTF-8, LF.

### The CLEAN row (CTO msg 34160: no firm or product token in a row; the tokens live in a registry file)

The commit-time naming gate reads any whitespace-free string (a value, a list item or a mapping key) as a hand-kept carrier when one of its segments (split at `-` `_` `/` `.` `:` `=` `@`) is a firm token, or the whole string is a firm or product token.
A string with whitespace is prose and is never graded. The token sets come from the registry, not from your code: build `carrier(s)` in a small module `workflows/atom_decomposition/catalog_tokens.py` that reads them the way `.tools/naming-gate.py` class `Naming.__init__` does
(`lib/opal_naming.py` `_registry()["scopes"]` rows whose `class` is `FIRM` or `PRODUCT`, their `_spellings(row)`; a FIRM spelling that is a reserved system key in `_registry()["systems"]` is skipped; a FIRM spelling matching `^[A-Za-z0-9]+$` is a segment token; every FIRM and PRODUCT spelling is a whole-string token).
The generator and its tests type NO firm name, product name or contract id as a literal.

**Build the FULL row first, then split it.** The full row has these keys, in this order:
`bucket prefix business_meaning example_questions grain freshness_field firm_scope_rule never_sum_rules producer tools read_tool gap_owner table layer format contract fork_keys nl_tags retired` (then `retired_reason` if any) `open_items`.

| key | FULL value |
|---|---|
| `layer`, `format`, `grain` | the contract's own, verbatim |
| `bucket` | the contract's `bucket`; for a MAPPED contract the bucket of the record's `live` address (`s3://<bucket>/<key>`: the part before the first `/` after `s3://`) |
| `prefix` | for a MAPPED contract, the key part of the record's `live` address (`silver/<table>/`); otherwise the LEADING LITERAL of the contract's `s3_prefix`: when it holds a `{`, the text before the first `{` cut back to the last `/` (`daily/{partner}/{date}.json` becomes `daily/`); otherwise the prefix unchanged. `null` when the prefix starts `none` or (for a contract that is NOT mapped) has a path segment `silver_legacy` |
| `table` | the contract's `table`, verbatim |
| `business_meaning` | one sentence you compose: layer, format, table, bucket, the contract's `s3_prefix` and its `grain`, then for a `firm-scoped` row `Client data forked by firm, account last-4 and platform; Opal-internal principals only until a data grant names the firm.` else `Opal-internal data.` (at least 40 characters, never starting `NONE`). Then FROZEN OR EMPTY IS NEVER CURRENT (PRD v0.12 item 4): let `n` be, for a MAPPED contract, the record's `trading_days_behind_t1`, otherwise the first number found under the contract's `freshness` keys `trading_days_behind_t1`, `trading_days_behind`, `trading_days_behind_T-1`; when `n` exists and is above 5, append ` NOT CURRENT: <n> trading days behind T-1.` (`<n>` as an integer); when the contract's `size.objects` is 0, append ` EMPTY: no objects.`. Append neither otherwise |
| `example_questions` | the contract's `common_queries` verbatim; if empty, one question `Where is the <table> <layer> table?` |
| `freshness_field` | `FIELD:<k>` where `k` is the first entry of the contract's `partition.keys`; if that list is empty, `NONE -- ` followed by the contract's `freshness.basis` |
| `firm_scope_rule` | `firm-scoped` when the contract's `fork_keys.firm.values` holds any value other than `global` and `opal-internal`; otherwise `opal-internal-only` |
| `never_sum_rules` | a one-item list holding the contract's `size.row_count_rule` when it has one; otherwise the string `NONE -- the contract states no row-count rule for this table` |
| `producer` | the contract's `producer.name`, prefixed `inferred: ` when the word `inferred` is in `producer.claim`; when the name is null, `NOT TRACED -- the contract names no producer (absent)` |
| `tools`, `read_tool`, `gap_owner` | `read_tool` per the policy below; `tools` is `[read_tool]` or `[]`; `gap_owner` is `NFRA_OPLGTW` when `read_tool` is null, else null |
| `contract` | a mapping: `id` = `c-` followed by the first 12 hex characters of the SHA-1 of the UTF-8 `contract_id`; `label` = the contract's `layer`, a space, then its `table` with any parenthetical `(...)` removed and any whitespace-separated word that is a carrier dropped; `size`, `freshness`, `partition`, `producer` = the contract's own objects verbatim |
| `fork_keys` | the contract's `fork_keys` object, verbatim |
| `nl_tags`, `open_items` | the contract's lists, verbatim |
| `retired` | `true` for the contracts the rules select, else `false`, by these rules and NEVER by a typed contract id (5 contracts in all, after rule (3)): (1) DO-NOT-SERVE: the contract has a `routing` string that contains `do NOT build a tool` or `must not be served` (2 contracts); (2) NOT-SERVED: its `table` starts `model_aua_positions` (2 contracts, PRD v0.14); and ALSO (3) every contract that is NOT mapped and whose `s3_prefix` has a path segment `silver_legacy` (1 contract: a frozen single-file copy). The 8 MAPPED contracts are NOT retired (Andrew-direct ~18:3xZ, CTO msg 34185, PRD v0.15: 49F Black Diamond is read from opal-data-bd). So `true` for 5 contracts |
| `retired_reason` | on the retired rows only. Rule (1): `do-not-serve: ` followed by the contract's `routing` string, verbatim. Rules (2) and (3), exactly: `not_served: ANDREW_DIRECT_20261014_150xZ_CLIENT_DATA_ONLY_OPAL_DATA_ASSETS_VENDOR_SILVER.md @9a314c1e98 -- client data only from the opal-data-assets vendor silver folders`; for rule (3) append, after the last word, ` (a frozen silver_legacy copy)` |

**Then split it into the CLEAN row and a registry entry.** `sanitize(x)`: a mapping drops every key that is a carrier and sanitises its values; a list drops every item that is a carrier string and sanitises the rest; a string that is a carrier becomes `null`; a string with whitespace has the QUOTE CHARACTERS removed around any quoted span (`"..."` or `'...'`) that is a carrier, because the gate's YAML reader reads each quoted span of a line as a literal (`QUOTED = ("|')([^"'\s]+)\1`; keep the span's text, drop its two quotes); anything else is unchanged.
The CLEAN row is the full row with every top-level field replaced by `sanitize(value)`, EXCEPT `prefix`, which is its leading literal when that literal is not a carrier, else `null`. For every top-level field whose clean value differs from the full value, the registry entry's `restore` holds the FULL value under that field name
(for `prefix`, the leading literal). The registry entry is `{"key_template": <the contract's full s3_prefix; for a MAPPED contract the record's `key_shape`>, "restore": {...}}`, keyed by the hashed `contract.id`. The clean row is what you write to `<out>/<entity>.yaml`.
A clean row therefore holds no carrier in any string, key or value, which `c14.AC2` scans for.

**read_tool policy (PRD v0.12 item 5; a tool that is not deployed is NEVER named).** Let D be the deployed-tools set. For a contract, its CANDIDATES are, in the order of its `proposed_tools`: take each tool's `name`, cut it at the first space (so `blackdiamond_list_fees (extend)` becomes
`blackdiamond_list_fees`), skip a name that starts `none`, then map it through `client_tool_map.json` (a name that is not a key stays as it is). The `read_tool` is the first candidate in D, else null.

**`workflows/atom_decomposition/client_tool_map.json`** is a JSON object, vendor tool name -> `client_*` tool (OPLGTW PRD v3.1 ruling 1: client data is one tool set with vendor adapters). Write exactly these 28 pairs:
```
schwab_resolve_account, blackdiamond_resolve_account, commonwealth_resolve_account            -> client_resolve_account
blackdiamond_get_holdings, schwab_get_positions, orion_get_holdings                           -> client_get_holdings
blackdiamond_list_transactions, schwab_list_transactions, orion_list_transactions, commonwealth_list_transactions -> client_get_transactions
blackdiamond_get_model_assignment, blackdiamond_get_model_targets, orion_get_allocation, smartx_allocation_by_account, smartx_model_assignments, smartx_model_detail -> client_get_allocation
blackdiamond_get_unrealized_lots, blackdiamond_list_realized, schwab_get_realized_lots, schwab_get_tax_lot_detail, schwab_get_unrealized_lots -> client_get_lots
orion_get_household_performance, orion_get_account_performance, commonwealth_get_performance  -> client_get_performance
blackdiamond_get_account_fee_roles, blackdiamond_list_fees                                    -> client_get_fees
smartx_account_lookup                                                                         -> client_get_profile
blackdiamond_list_insurance                                                                   -> client_get_insurance
```
(`blackdiamond_get_account_profile` is deliberately NOT mapped: the commit-time naming gate reads that exact string in a JSON key as a resource name and refuses it. Its table stays `read_tool: null`; this is reported to the CTO.) A G2 tool not listed here (balances, find_holders, flows, documents, delivery, the Eclipse tools, prices, workbook rows, platform lists) is NOT mapped: its tables are catalogued with `read_tool` null (OPLGTW: "a table no question reaches is catalogued but gets no adapter this round").

### The registry files (CTO msgs 34143 and 34160: rule 30's own remedy, no gate edit)

**legacy_addresses.json.** The commit-time naming gate grades a prefix literal CONFORMANT when it equals a `legacy_addresses.json` row of the COMMITTING PROJECT (`reader` = `NFRA_MCPINDEX`, no `params`) that is COMMITTED AT HEAD. So the registry rows land in a commit BEFORE the rows that name them.
For every in-scope contract whose clean row has a non-null `prefix` and whose `bucket` starts `opal-data-` but is neither `opal-data-news-v2` nor `opal-data-news-av`, add one row per DISTINCT (`bucket`, `prefix`) pair (the registry is unique on that pair; when the pair is already a row of another project, add nothing and list it in your report). Fields:
- `key`: `catalog-` + the entity with every `_` replaced by `-`, taken from the first contract that names the pair;
- `bucket`: the bucket; `template`: the clean row's `prefix`; `shape`: `prefix` when it ends in `/`, else `object`; `params`: `[]`; `reader`: `NFRA_MCPINDEX`;
- `evidence`: `measured by 4.0.0_SA_CRO~Z in the census <file name of G2|G4|G5|G6, e.g. G2_assets_silver.md> @<its pin>: <size.objects> objects (the contract's size.objects, a count; no object content read)`;
- `note`: `Catalog source-row address; the owner of the data renames it (R19).`
(Your first commit already wrote 130 such rows for the full prefixes. Replace them: keep only the rows the rule above yields; a row whose prefix now carries a token or a template is removed.)

**catalog_fork_keys.json** (new, in `infra/logic/registry/`; registry files may carry firm tokens): `{"_about": "<one sentence: the full values of the catalog silver table rows, keyed by the hashed contract id; the loader joins them (MX-c-15)>", "rows": {"<hashed id>": <the registry entry above>, ...}}` with one entry per in-scope contract (216).
The generator writes it with `--fork-registry-file <path>` (replace the whole `rows` object; keep `_about`). Validate with `opal_naming.validate(None, None)` (it must return no refusals).

### The steps

0. Write the generator first (step 1 below), then run it ONCE with `--registry-file infra/logic/registry/legacy_addresses.json` and `--out` a scratch folder; confirm `python -c "import sys; sys.path.insert(0,'lib'); import opal_naming; print(len(opal_naming.validate(None,None)[0]))"` prints 0 (the registry validates); COMMIT THE REGISTRY FILE AND THE GENERATOR FIRST, in their own commit through `safe-commit.sh` (stage a `.json` under this project's home with it, e.g. your deliverables folder's `step0.json`, so the committing project is derived). That commit is what makes the next one pass.
1. Write the generator, the map and `workflows/atom_decomposition/tests/test_gen_silver_rows.py` (your own tests: entity uniqueness over the 216, the count refusal, the exit-3 refusal, the read_tool policy under three sets, the four retired rows, `firm-scoped` for a client table and `opal-internal-only` for an ETF table).
2. Run it with `--out workflows/atom_decomposition/catalog_entries --deployed-tools census`. That writes the 216 rows.
   **Commit what the naming gate accepts, hold the rest (CTO msg 34143).** Stage all 216 rows plus a `.json` under this project's home, write the staged diff to a file, and run `NAMING_GATE_ENFORCE=1 python .tools/naming-gate.py --diff <that file> --enforce --post-from-index`; every `NAMING REFUSE <path>:<line> ...` line names a row file that cannot land. Unstage those files (`git restore --staged <file>`), commit the rest through `safe-commit.sh` (the commit must pass), and leave the refused files in the working tree UNCOMMITTED. Print: rows committed, rows held, and the REFUSE count by kind: (a) `contract.id`, (b) a firm token in `fork_keys` or another field, (c) an out-of-pattern or templated `prefix`, (d) a news bucket id, (e) other. Write the same numbers to `residual_refusals.json` in your deliverables folder.
3. Print the diff summary (files added) and the counts by `layer` and by `firm_scope_rule`.
4. Run the three criteria below. While rows are held, AC1 to AC3 cannot all PASS: that is expected. Report each criterion's output, and do NOT flip `<status>`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `emit_catalog_v02.py`, `validate_catalog_v02.py`, `DATA_CATALOG.yaml`, the tool index, an existing `catalog_entries/` row or the gateway: `2.0.0_SA_COO~MI` regenerates the catalog at the drain, and the loader is another cell's.
   At your commit the loader still refuses your rows (it expects the old shape). That is expected and is not yours to fix. Do not run the emitter.
2. No AWS call, no deploy, no push.
3. No contract id, firm name or product name is typed as a literal in `gen_silver_rows.py` (the naming gate refuses a NEW hand-kept firm or product token in code; the tests under `tests/` are exempt). The tool map is JSON data and carries vendor tool names, which the gate accepts except the one named above. The shape of a row is exactly the table above. Do not add, rename or reorder a field. A string the contract holds is copied, never paraphrased.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8).
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/logic/registry/legacy_addresses.json
infra/logic/registry/catalog_fork_keys.json
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
workflows/atom_decomposition/catalog_tokens.py
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
  <criterion id="AC1" cell_refs="MX-c-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC1.sh; echo "exit=$?"</invocation><expect>ROWS files=216; in-scope contracts=216; entity names unique=yes; missing 0, extra 0, contract.id wrong 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC2.sh; echo "exit=$?"</invocation><expect>ROWS graded 216 of 216; failing fields: none -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC3.sh; echo "exit=$?"</invocation><expect>ARMS pass 5 of 5; rows graded right 1080 of 1080 -- RESULT: PASS -- exit=0</expect></criterion>
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

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-14 ~15:3xZ).** Two rulings arrived while you were building. (1) Andrew-direct ~15:0xZ (CTO msg 34135, PRD v0.14 @26a247b289): client data comes ONLY from the `opal-data-assets` vendor silver folders, so the two `model_aua_positions` MDPF feeds are `not_served` (retired, with the record cited), and no row names `opal-data-bd`. The 49F Black Diamond rows keep the contract's `opal-data-assets` location and state their lag through the NOT CURRENT mark. (2) The commit-time naming gate refuses a slash-bearing `contract.id` as an S3 key, so `contract.id` is written with `:` for `/` (the first worker's rows showed it). (4) The gate refused 3 strings in your first code files: the `blackdiamond_get_account_profile` key of the map (dropped), and the contract ids typed in the generator (replaced by the two rules in the `retired` row). (3) CTO ruling msg 34143: the gate's legacy-address branch makes a prefix literal CONFORMANT when a committed `legacy_addresses.json` row of this project names it, so the generator also writes those registry rows (130), they land in their OWN commit first, and the rows the gate still refuses (firm tokens in `fork_keys` and ids, `{param}` and `none` prefixes, news buckets) are HELD, not forced: commit what passes and report the residual by kind. The checks were amended to the same rules. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A13 (2.0.0_SA_COO~MI, 2026-10-15 ~07:3xZ), a one-step re-seat of the A10 kind, for the MX-r-13 RE-CUT.** MX-r-13 PHASE B rolled back on r13.AC2 (CloudOps~MI msg 34382); the catalog is re-emitted with `--overlay-ref d020bee315` so its definition lines match the shipped source (4 lines change). It is finished in the issuer's tree and the lane gate refuses the issuer the gateway folder. Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_catalog_r19.py <your worktree root>` (it prints `cmp ... equal=True` and `copied=1 equal=1`; anything else: stop and file a surprise row); (2) commit exactly `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` with `safe-commit.sh` on your branch, in the BACKGROUND with a wait loop exactly as in A9; message first line `feat(NFRA_MCPINDEX MX-r-13 re-cut, 0.9.0_WK_NFRA_MCPINDEX~38): the runtime catalog with definition lines taken from the shipped source`, body: emit_catalog_v02.py --overlay-ref d020bee315 output, no hand edit; push state LOCAL; the Co-Authored-By Haiku line; (3) it must land with rc=0 and no summary REFUSE or lane VIOLATION; if it refuses, report those lines and stop. Do not run tests, regenerate anything or edit any file. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A12 (2.0.0_SA_COO~MI, 2026-10-15 ~05:4xZ), a one-step re-seat of the A10 kind.** The history-depth measurements were re-read today (387564df3c) and the catalog re-emitted; it is finished in the issuer's tree and the lane gate refuses the issuer the gateway folder. Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_catalog_r18.py <your worktree root>` (it prints `cmp ... equal=True` and `copied=1 equal=1`; anything else: stop and file a surprise row); (2) commit exactly `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` with `safe-commit.sh` on your branch, in the BACKGROUND with a wait loop exactly as in A9; message first line `feat(NFRA_MCPINDEX MX-r-13 PHASE A, 0.9.0_WK_NFRA_MCPINDEX~38): the runtime catalog with the history-depth claims re-read on 2026-10-15`, body: emit_catalog_v02.py output after the issuer's measured.yaml commit 387564df3c, no hand edit; push state LOCAL; the Co-Authored-By Haiku line; (3) it must land with rc=0 and no summary REFUSE or lane VIOLATION; if it refuses, report those lines and stop. Do not run tests, regenerate anything or edit any file. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A11 (2.0.0_SA_COO~MI, 2026-10-15 ~05:2xZ), a one-step re-seat of the A10 kind, for the MX-r-13 release.** The catalog regenerated against the live gateway (ee23dd004c, 93 tools) and one test fix are finished in the issuer's tree and the lane gate refuses the issuer the gateway folder; `<paths>` already grants both to you. Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_r17.py <your worktree root>` (it prints two `cmp ... equal=True` lines and `copied=2 equal=2`; any other output means stop and file a surprise row); (2) commit exactly `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` and `infra/aws/ec2/opal-gateway/tests/test_opal_discover.py` with `safe-commit.sh` on your branch, in the BACKGROUND with a wait loop exactly as in A9; message first line `feat(NFRA_MCPINDEX MX-r-13 PHASE A, 0.9.0_WK_NFRA_MCPINDEX~38): the runtime catalog regenerated against the live gateway ee23dd004c, and the harvest-gap test follows a retired row that names a tool`, body: emit_catalog_v02.py output at the issuer's rows commit c299791b57, no hand edit; the 78 harvest rows and 19 table rows now name the live tools; the gateway suite failing-ID set differs from the baseline only by two failures that also fail on the unchanged catalog; push state LOCAL; the Co-Authored-By Haiku line; (3) the commit must land with rc=0 and no summary REFUSE (a `CATALOG-EXEMPT` line may or may not appear: it prints only when the diff adds a graded literal); if it refuses, report the REFUSE lines and stop. Do not run tests, regenerate anything or edit any file. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A10 (2.0.0_SA_COO~MI, 2026-10-15 ~01:4xZ), a one-step re-seat of the A9 kind.** The round 16 catalog (MX-c-16 and MX-c-17 merged, the tool-index fix in) is finished in the issuer's tree and the lane gate refuses the issuer the gateway folder; `<paths>` already grants it to you. Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_catalog_r16.py <your worktree root>` (it prints `cmp ... equal=True` and `copied=1 equal=1`; any other output means stop and file a surprise row); (2) commit exactly `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` with `safe-commit.sh` on your branch, in the BACKGROUND with a wait loop exactly as in A9 (the naming gate takes about ten minutes); message first line `feat(NFRA_MCPINDEX round 16 drain, 0.9.0_WK_NFRA_MCPINDEX~38): the regenerated runtime catalog with the aum-metrics row denied, the legacy mdpf row dropped, the news text corrected and the 14 rival-fund rows enriched`, body: emit_catalog_v02.py output at generator commit 824f26fa68 plus the merged MX-c-16 change 7406f93e89, no hand edit; the gateway suite failing-ID set equals the baseline of 48; push state LOCAL; the Co-Authored-By Haiku line; (3) the log must hold `CATALOG-EXEMPT admitted=<n> refused=0` and `DONE rc=0`; if it refuses, report the REFUSE lines and stop. Do not run tests, regenerate anything or edit any file. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A9 (2.0.0_SA_COO~MI, 2026-10-14 ~23:4xZ), a one-step re-seat; it overrides rule 1 of section 2 for these four files only.** The regenerated runtime catalog and the discover ranking fix are finished in the issuer's shared tree and are refused to the issuer by the lane gate (lane CLOUD_OPS_OR_ETL); `<paths>` now grants them to you. Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_gateway_files.py <your worktree root>` (it copies four finished files into your worktree and prints one `cmp ...` line per file and then `copied=4 equal=4`; any other output means stop and file a surprise row); (2) commit exactly those four files with `safe-commit.sh` on your branch, in the BACKGROUND with a wait loop, because the naming gate takes about ten minutes on the catalog: write the message file with the Write tool, start `( bash .tools/safe-commit.sh --author ... -F <msgfile> -- <the four paths> > <logfile> 2>&1; echo DONE rc=$? >> <logfile> ) &`, then loop `until grep -q '^DONE' <logfile>; do sleep 10; done` in calls of at most 9 minutes each until it prints DONE; (3) the line `CATALOG-EXEMPT admitted=<n> refused=0` must appear in the log and the commit must land; if it refuses, report the log's REFUSE lines and stop. Do not run tests, regenerate anything, or edit any file. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A8 (2.0.0_SA_COO~MI, 2026-10-14 ~23:1xZ), a one-step re-seat.** The emitted gateway catalog is graded by the naming gate, which admits a catalog literal only as a whole string held at HEAD in `infra/logic/registry/catalog_fork_keys.json`. That file must gain a top-level `entities` list: the sorted entity names of the 216 rows (`gen_silver_rows.py` `write_fork_registry` already writes it, at HEAD on trunk since `824f26fa68`). Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_entities.py <your worktree root>` (it adds `entities` to that file in your worktree and prints `entities=216 rows=216 rows_unchanged=True`; any other output means stop and file a surprise row); (2) run `c14.AC1.sh` and `c15.AC1.sh` (both must still print `RESULT: PASS`); (3) commit that ONE file with `safe-commit.sh` on your branch; (4) report the commit and the script's line. Do not regenerate rows, do not edit any other file. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A7 (2.0.0_SA_COO~MI, 2026-10-14 ~19:5xZ), on your report (rows Z-W38-S9, S10, S11).** (S9) the retired_reason wording is the one in the `retired_reason` row (rule (3) appends ` (a frozen silver_legacy copy)` after `folders`): the check was aligned to it. (S10) the retired set is the 5 contracts the rules select: the words `exactly four` were stale. (S11) a quoted token inside a prose `fork_keys` value is read as a literal by the gate: `sanitize` removes the quote characters around a carrier span (see "Then split it"), and `c14.AC2` now scans for quoted carrier spans. Everything else of A4 to A6 stands (the live 49F rows, G3, the landing order). Re-run the generator and criteria; your 165 committed rows are regenerated where they change. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A6 (2.0.0_SA_COO~MI, 2026-10-14 ~19:2xZ), on CTO msg 34192 (the Friday order).** G3's 42 portal contracts join the generator: the gateway's G3 portal tools read each S3 key from its catalog row, and `json/...`, `platinum/mdpf/{scope}/...` keys are token-bearing or templated, so they travel as clean rows with the full key in the fork registry `key_template` (the same mechanism). 216 rows now. LAND IN THIS ORDER, one commit per tranche, each through the naming gate: (1) the two registry files and the generator (as before); (2) TRANCHE 1, the rows of G5, G6 and G3 (131 minus the G2 and G4 ones; i.e. every row whose contract came from G5, G6 or G3); (3) TRANCHE 2, the Schwab rows of G2; (4) TRANCHE 3, every other row. Print the row count of each tranche. The corrections to the certified channel text (ft.04, json/mdpf, the portal_lookup channel) are NOT in this order. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A5 (2.0.0_SA_COO~MI, 2026-10-14 ~19:0xZ), on Andrew-direct ~18:3xZ via CTO msg 34185 (PRD v0.15 @6d6702425a).** The 8 49F Black Diamond tables read `opal-data-bd`: a MAPPED contract's row names the live bucket and prefix from CRO~Z's G2f, states the live lag (NOT CURRENT when above 5), and is NOT retired; `--g2f <file>` is a new generator argument. The ninth silver_legacy copy stays `not_served`. `bucket` can now be null in a clean row (the live bucket name carries a token). Re-run the generator and the criteria. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

**AMENDED A4 (2.0.0_SA_COO~MI, 2026-10-14 ~18:0xZ), on your report and CTO ruling msg 34160 (no gate edit).** Your 70 committed rows and the registry commit stand as history; this amendment changes the row. (1) `contract.id` is a hash and `contract.label` is added; (2) the clean row holds no firm or product token anywhere: the tokens move to the new registry file `catalog_fork_keys.json`, keyed by the hashed id, and the loader (MX-c-15) joins them back; (3) a prefix with `{params}` registers and writes its leading literal, a `none` prefix and a `silver_legacy` prefix are null; (4) nine `silver_legacy` contracts are retired `not_served`; (5) the generator reads the token sets from the registry (`catalog_tokens.py`) and types none. Regenerate all 216 rows; the rows already committed are rewritten (their ids change). Re-run the criteria. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification; `<placeholders>NONE`).

<status>issued</status>
<round>14</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<status>issued</status>
<status>issued</status>
<status>complete</status>
<status>issued</status>
<status>complete</status>
<status>issued</status>
<status>issued</status>
<status>complete</status>
<status>issued</status>
<status>complete</status>
