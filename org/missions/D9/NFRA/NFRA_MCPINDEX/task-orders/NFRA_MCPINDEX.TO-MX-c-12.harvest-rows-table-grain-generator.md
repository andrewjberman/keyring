# NFRA_MCPINDEX task order -- `MX-c-12` -- a generator writes the 78 table-grain harvest rows from the CRO's G1 data contracts, and the catalog source rows become those 78

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-12</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-12</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~37</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- a generator and YAML catalog source rows only; the one AWS act is an optional read-only S3 listing (item 6).
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run plus planted PASS and FAIL arms are the control (decomposition R13.3).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only S3 listing, optional).
</preflight>

## 1. THE CELL -- `MX-c-12` (round 13; PRD v0.11 FWD-22, enrichment items 1, 2, 4, 5)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root.

**What exists at the base.** `workflows/atom_decomposition/catalog_entries/` holds 39 `harvest_*.yaml` source rows, 11 fields each.
Only 26 of the 78 datasets in the `opal-data-harvest` bucket have a row at their own prefix. 50 sit under a source-level row such as
`bloomberg/harvest/`. Two have no row (`amgt/harvest/gold/ai_fill/` and `social/v1/`). The fields `grain`, `freshness_field` and the
never-sum rules read `NONE -- not read` on most of them.

**What you build.** `workflows/atom_decomposition/gen_harvest_rows.py`, and then the 78 rows it writes into `catalog_entries/`.

**The source.** The CRO's census G1 holds one JSON contract per dataset. Read it at its PIN, never the working copy:
`git show 0d7c29b3c5:org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`
(save it to `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~37/G1_pinned.md` and pass that file as `--g1`).
It holds 79 fenced `json` blocks: 78 are dicts carrying `contract_id` (one per dataset) and one is a list (the tool registry, ignore it).

### The generator's interface (fixed: the checks call it)

```
python workflows/atom_decomposition/gen_harvest_rows.py --g1 <file> --out <dir> --deployed-tools <json-list-file | census> [--existing <dir>]
```
- Parse every ` ```json ` block of `--g1`. The contracts are the dict blocks with `contract_id`. If there are not exactly 78, exit 2 with a message.
- Write exactly 78 files `<out>/harvest_<slug>.yaml`, one per contract. The slug of a contract's `s3_prefix` is
  `emit_catalog_v02.harvest_slug(prefix)` (import it from `workflows/atom_decomposition/emit_catalog_v02.py`).
- `--deployed-tools`: a JSON file holding a list of tool names, or the word `census`, which runs
  `python workflows/atom_decomposition/tool_census.py` and takes the `tool` names of its JSON `tools`.
- `--existing <dir>` (default `workflows/atom_decomposition/catalog_entries`): the harvest rows to preserve text from. Read-only.
- When `--out` is the same directory as `--existing`, also delete every `harvest_*.yaml` in it that is not one of the 78, and print the names.
- Print `wrote 78 rows to <out>`; write nothing outside `<out>`.
- Write YAML with `yaml.safe_dump(row, f, sort_keys=False)`, UTF-8, LF.

### The row (exactly these keys, in this order)

| key | value |
|---|---|
| `prefix` | the contract's `s3_prefix`. EXCEPTION: for the six hyphenated gold tables (`research-backlog`, `research-continuation`, `research-dossier`, `research-fund-form`, `research-model-typecast`, `research-sector-template`, under `amgt/harvest/gold/`) write `prefix_key: harvest-gold-<table>` INSTEAD of `prefix` (they are legacy read addresses; the loader resolves the key through `legacy_addresses.json`; a typed literal is refused). Exactly one of the two keys, never both |
| `bucket` | the contract's `bucket` |
| `business_meaning` | if a `--existing` row has the same resolved prefix, its `business_meaning` VERBATIM. Otherwise one sentence you compose from the contract: layer, format, table, prefix and the contract's `grain` (at least 40 characters, never starting `NONE`) |
| `example_questions` | the `--existing` row's list (same resolved prefix) in its order, then every G1 `common_queries` entry not already in it. If both are empty: one question `Where is the <table> <layer> table of the harvest bucket?` |
| `grain` | the contract's `grain` string, verbatim |
| `freshness_field` | `FIELD:<column>` only when the contract's `freshness.derived_from` names a column that is in its `columns` list; otherwise `NONE -- ` followed by `freshness.derived_from` verbatim |
| `firm_scope_rule` | `opal-internal-only` |
| `never_sum_rules` | a list: the contract's `never_sum_rules`, then every `--existing` rule (same resolved prefix) not already in it. If both are empty: the string `NONE -- G1 states no never-sum rule for this table` |
| `producer` | the contract's `producer.name` when it is not null, prefixed `inferred: ` when `producer.claim` is `inferred`; when the name is null, the string `NOT TRACED -- G1 read no producer for this table (absent)`. A producer text never reads as measured when G1 says inferred or absent |
| `read_tool` | see "read_tool policy" |
| `gap_owner` | `NFRA_OPLGTW` when `read_tool` is null, else null |
| `table`, `layer`, `format` | the contract's own, verbatim |
| `contract` | a mapping: `id` = `contract_id`; `size`, `freshness`, `partition`, `producer` = the contract's own objects verbatim; `keys` = the contract's `securities` object verbatim |
| `nl_tags` | the contract's `nl_tags` list, verbatim (may be empty) |
| `retired` | `true` for `publication-links/v1/` and `publications/v1/`, else `false` (see item 6 for research-dossier) |
| `retired_reason` | present ONLY when `retired` is true: one sentence naming what supersedes it and G1 section 2 item 4 |

**read_tool policy (PRD v0.11 item 3; a tool that is not deployed is NEVER named).** Let D be the deployed-tools set. Walk the
contract's `proposed_tools` in order: the first whose `name` is in D is the `read_tool`. If none, `harvest_read` when it is in D. If neither,
null. Examples: D = [] gives null on all 78; D = [harvest_list, harvest_read] gives `harvest_read` on all 78; D adds `harvest_get_research` and a
contract proposing it gives `harvest_get_research`.

### The steps

1. Write the generator and `workflows/atom_decomposition/tests/test_gen_harvest_rows.py` (your own tests: slug uniqueness over the 78, the count refusal, the read_tool policy under three sets, the six legacy keys).
2. Run it with `--out workflows/atom_decomposition/catalog_entries --deployed-tools census`. That writes the 78 rows and deletes the 13 stale source-level files.
3. Read the diff summary: files added, removed, kept. Print it.
4. Run the three criteria below.
5. **Item 6, optional and bounded.** Measure whether gold `research_dossier` (underscore) supersedes `research-dossier` (hyphen): list the object keys of both prefixes in
   `s3://opal-data-harvest/amgt/harvest/gold/` (read-only `list-objects-v2`, via `bash .tools/aws s3api ...`; no object body). Write
   `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~37/research_dossier_supersession.json` with: the two key counts, the security_key
   sets' difference both ways, and the newest `LastModified` of each. Set the hyphen row's `retired: true` ONLY IF the hyphen table holds no security_key the underscore
   table lacks AND the underscore table's newest write is not older than the hyphen's; then the `retired_reason` names that evidence file's path. Otherwise leave it `false`. If you cannot run the
   listing within your bounds, leave it `false` and file one surprise row. Both outcomes are valid.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `emit_catalog_v02.py`, `validate_catalog_v02.py`, `DATA_CATALOG.yaml`, the tool index or the gateway: `2.0.0_SA_COO~MI` regenerates the catalog at the drain, and the loader changes are another cell's.
   At your commit the loader still refuses your rows (it expects 11 fields). That is expected and is not yours to fix. Do not run the emitter.
2. No AWS write, no deploy, no push. The one AWS act is item 5's listing.
3. The shape of a row is exactly the table above. Do not add a field, rename one or reorder them.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8).
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_harvest_rows.py
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/test_gen_harvest_rows.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~37/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W37-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c12.AC1.sh; echo "exit=$?"</invocation><expect>ROWS files=78; G1 contracts=78; prefix set equal=yes (missing 0, extra 0); contract.id match 78 of 78; other errors 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c12.AC2.sh; echo "exit=$?"</invocation><expect>ROWS graded 78 of 78; failing fields: none; RETIRED set holds publication-links/v1/ and publications/v1/ (and research-dossier only with its evidence file) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c12.AC3.sh; echo "exit=$?"</invocation><expect>ARMS pass 5 of 5; rows graded right 390 of 390 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~37/NFRA_MCPINDEX.TO-MX-c-12.harvest-rows-table-grain-generator.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS.
3. Commit everything together.
4. Report once, with:
   - the generator's `--help` line and the diff summary (files added, removed, kept);
   - the number of rows by `layer`;
   - the retired set and, for research-dossier, the supersession measurement or why it was not run;
   - your commit sha.

The issuer then regenerates the catalog from the merged rows and the loader cell's code.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 13, chain head, worker ~37, parallel to `MX-c-11` (no shared file). Source: PRD v0.11
@7878037d98 (1.0.0_SA_CTO~Z msg 34078), items 1, 2, 4 and 5; G1 @0d7c29b3c5. The base for the preserved text is @8c74d1d902 (the 39 round-12
rows), read by the check through `git show`. Battery and planted arms: decomposition R13.3.

<status>issued</status>
<round>13</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
