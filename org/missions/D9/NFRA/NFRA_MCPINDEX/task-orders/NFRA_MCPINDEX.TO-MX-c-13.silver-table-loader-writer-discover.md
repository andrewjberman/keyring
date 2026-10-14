# NFRA_MCPINDEX task order -- `MX-c-13` -- the catalog's one writer loads, validates and writes TABLE-grain silver rows (with their firm / account / platform fork), records the mdpf mirror, and discover answers them

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-13</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-13</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~36</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the emitter, its validator, discover and their tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run plus planted PASS and FAIL arms are the control (decomposition R14.3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-13` (round 14; PRD v0.12 item 1 and PRD v0.13; the loader the 174 rows need)

You are the worker that built `MX-c-11`. This cell is the second on your queue: build on your own branch, where the harvest loader, the pending tool index and the v0.5 header
already are. Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root.

The one catalog writer is `workflows/atom_decomposition/emit_catalog_v02.py`. It reads every `catalog_entries/*.yaml` that is not a `need_` or `harvest_` file through
`load_catalog_entries` and `validate_entry`, and writes each as a row of `silver_datasets:` (or `portal_datasets:` for a `portal_` name). You do NOT write any `catalog_entries/` row and you
do NOT write `DATA_CATALOG.yaml`: another cell (`MX-c-14`) writes 174 table-grain silver rows into `catalog_entries/` in parallel, and `2.0.0_SA_COO~MI` regenerates the catalog from
both at the drain. Do not run the emitter's `main`.

**What the user sees at the base.** `validate_entry` accepts a silver row of EXACTLY the 9 C1 fields plus the optional `read_tool`. The new rows are one per table, carry eleven more
fields, and are refused.

### Part 1 -- the table-grain silver row (loader and validator)

A silver source row that carries a `contract` key is a TABLE row. It has EXACTLY the keys `ENTRY_REQUIRED_FIELDS` plus `read_tool`, `bucket`, `prefix`, `table`, `layer`, `format`, `contract`,
`fork_keys`, `nl_tags`, `retired`, `open_items`, `gap_owner`, and `retired_reason` iff `retired` is true. A row without `contract` keeps today's rules exactly (the five existing silver rows
and the portal rows must still load, unchanged). For a table row, `validate_entry` applies the existing rules for `business_meaning`, `example_questions`, `freshness_field`,
`firm_scope_rule` (one of the three), `never_sum_rules`, `producer`, and these changes and additions:
- `grain` is a non-empty string (the contract's measured sentence; the enum does not apply);
- `tools` is a list of strings and MAY be empty (the deployed read tools);
- `read_tool` is present: null or a non-empty string; `gap_owner` is a non-empty string iff `read_tool` is null, else null;
- `layer` is one of `gold silver bronze state served platinum dynamodb`; `bucket`, `prefix`, `table`, `format` are non-empty strings;
- `contract` is a mapping with exactly the keys `id size freshness partition producer`; `id` a non-empty string; the other four are mappings;
- `fork_keys` is a mapping with exactly the keys `firm account platform`, each a mapping or null;
- `nl_tags` and `open_items` are lists of strings (may be empty); `retired` is a bool; `retired_reason` is a non-empty string iff `retired` is true.

### Part 2 -- the writer

Add `silver_catalog_row(name, data)`: it returns the dict that becomes one row under `silver_datasets:`. For a row without `contract` it returns exactly what the loop in `main` builds today:
`{"entity": name}` then each of `ENTRY_REQUIRED_FIELDS + SILVER_READER_FIELDS` that is in `data`. For a table row it returns the same, then the eleven table fields
`bucket prefix table layer format contract fork_keys nl_tags retired open_items gap_owner` (and `retired_reason` when present), every value equal to the source row's. Replace the inline loop in `main` with a call to it.

### Part 3 -- the header

In the emitter's header text (the v0.5 paragraph you wrote in MX-c-11), add one paragraph: `opal-data-mdpf` gold is a measured MIRROR of the served platinum (the CRO's G4 census, OVERLAP 100 percent, measured), so no tool
targets that bucket; cite `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` @7ec87a87e5 and NFRA_MCPINDEX PRD v0.13. The words `opal-data-mdpf`, `mirror`, `platinum` and `overlap` must all appear in the emitter's text.

### Part 4 -- discover answers a table row

In `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, `_silver_answer`:
- for a row that carries `contract`, add to the answer: `bucket`, `prefix`, `fork_keys`, `contract`, `retired` (and `retired_reason` when true); a retired row has `next_tool` null and `servable` false even if it names a `read_tool`;
- the text by which a silver row is matched (its "own text") also includes its `nl_tags`, joined by a space;
- the fail-closed rule stays exactly as it is: a `firm-scoped` row is served only to an opal-internal principal; every firm principal gets no match.
Add exactly three tests to `infra/aws/ec2/opal-gateway/tests/test_opal_discover.py`, each on a fixture row or fixture catalog (not the live catalog), named exactly:
`test_silver_table_row_answer_carries_fork_keys_and_contract`, `test_silver_table_row_nl_tags_reach_the_row`, `test_silver_firm_scoped_table_row_is_fail_closed_for_firms`.
Also write your own tests for Parts 1 and 2 in `workflows/atom_decomposition/tests/test_silver_table_grain.py`.

### Part 5 -- the five tests your MX-c-11 left red (your row Z-W36-S2)

`workflows/atom_decomposition/tests/test_tool_index_and_harvest.py` now fails 5 tests, because they build harvest rows in the old 11-field shape. It is in `<paths>` for this order. Update each of the 5 to build the table-grain row (the six new fields; `contract.id` is written with `:` for `/`), or to the loader's new tool-index behaviour, so that the file passes. Print its result (passed / failed) before and after.

## 2. BOUNDS

1. You change only the files in `<paths>`. No `catalog_entries/` row, no `DATA_CATALOG.yaml`, no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. Grade the gateway suite by failing-ID DELTA (`suite_delta.py`) against the base of this order (your MX-c-11 commit). The known failures (rows Z-S97, Z-S107) are listed, never fixed here.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8).
4. The checks build their own 174 correct rows and their own one-defect rows. You can read the check files under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/` to see the exact interface they call. Do not edit them.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/tests/test_silver_table_grain.py
workflows/atom_decomposition/tests/test_tool_index_and_harvest.py
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~36/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W36-S<k>` (continue your numbering);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c13.AC1.sh; echo "exit=$?"</invocation><expect>ACCEPT: 174 of 174 correct table rows load; existing rows still load 10 of 10; REFUSE: 12 of 12 one-defect rows refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c13.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c13.AC3.sh; echo "exit=$?"</invocation><expect>CHECKS pass 5 of 5 (silver_catalog_row emits a table row's fields and an old row's exactly; the header records the opal-data-mdpf mirror) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~36/NFRA_MCPINDEX.TO-MX-c-13.silver-table-loader-writer-discover.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS.
3. Commit everything together.
4. Report once, with:
   - the validator change by constant and function;
   - `silver_catalog_row` for a table row and an old row (print both);
   - the discover answer for a firm-scoped fixture row, for opal-internal and for a firm principal (print both);
   - the suite delta;
   - your commit sha.

The issuer then merges this with `MX-c-14`, regenerates the catalog and runs the drain checks.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 14, SECOND on worker ~36's queue (chain `MX-c-11 -> MX-c-13`, because both edit the emitter, its validator, discover and their tests).
The issuer hands this order by CONTINUING ~36 after MX-c-11's report, with the order file committed on the worker's branch. Source: PRD v0.12 @95d985d1a5 item 1 and PRD v0.13 @bb9d1ece12.
Battery and planted arms: decomposition R14.3.

<status>issued</status>
<round>14</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
