# NFRA_MCPINDEX task order -- `MX-c-11` -- the catalog's one writer accepts table-grain harvest rows, lists the harvest tools only once served, never lets a row name an unserved tool, carries v0.5 with Andrew's verbatim, and discover answers a retired row and a row's tags

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-11</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-11</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~36</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the emitter, its validator, the tool-index source, discover and their tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run plus planted PASS and FAIL arms are the control (decomposition R13.3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-11` (round 13; PRD v0.11 FWD-22, enrichment items 3 and 6, and the loader the 78 rows need)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root. The one catalog writer is
`workflows/atom_decomposition/emit_catalog_v02.py`. It reads `catalog_entries/harvest_*.yaml` (`load_harvest_entries`, `validate_harvest`) and
`tool_index/members.yaml` (`load_tool_index`), and writes `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`. You do NOT write that file
and you do NOT write any `catalog_entries/` row: another cell (`MX-c-12`) writes 78 table-grain rows into `catalog_entries/` in parallel, and
`2.0.0_SA_COO~MI` regenerates the catalog from both at the drain. Do not run the emitter's `main`.

**What the user sees at the base.** The loader accepts only 11-field harvest rows at 39 exact prefixes. The new rows are one per dataset
(78), carry six more fields, and sit at table prefixes such as `bloomberg/harvest/silver/article/`. The loader refuses all of them.

### Part 1 -- the table-grain row (item: the loader)

A harvest source row has EXACTLY the keys `HARVEST_FIELDS` plus `table`, `layer`, `format`, `contract`, `nl_tags`, `retired`, and `retired_reason`
iff `retired` is true. (`prefix` or `prefix_key`, as today.) Change `validate_harvest` and its constants so that:
- the prefix check is: ends in `/`, does not start with `/`, is not the whole gold root (`HARVEST_NEVER_ROWED` stays), and its FIRST path segment is one of the 24 served top-level
  prefixes: `amgt barrons bloomberg crosswalk derived drafting filings ft identity issuer-site lib management packs peers posture publication-links publications raw scores sec seeking-alpha social universe wsj`.
  The exact-prefix tuple `HARVEST_SERVE_NOW` and the gold-table tuples no longer gate a row (the file-name-is-the-slug rule stays);
- `layer` is one of `gold silver bronze state`; `table` and `format` are non-empty strings; `nl_tags` is a list of strings (may be empty); `retired` is a bool; `retired_reason` is a non-empty string iff `retired` is true;
- `grain` is a non-empty string (a table row carries G1's measured sentence, so the `ENTRY_GRAIN_VALUES` enum no longer applies to a harvest row);
- `contract` is a mapping with exactly the keys `id size keys freshness partition producer`; `id` a non-empty string; each of `size`, `keys`, `freshness`, `partition`, `producer` a mapping whose `claim` is one of `measured inferred absent` (a value carries its claim);
- the existing rules stay: bucket, `firm_scope_rule: opal-internal-only`, `read_tool` / `gap_owner` (a null `read_tool` needs a `gap_owner`; a named one needs a null `gap_owner`).
The writer of the `harvest_datasets:` list (search `harvest_datasets` in the emitter) emits the six new fields on every row, after the fields it emits today.

### Part 2 -- a harvest row names only a served tool, and the tool index lists the harvest tools only once served (item 3)

- Add `harvest_read_tool_errors(rows, served)`: `rows` is the dict `load_harvest_entries` returns, `served` a set of tool names. It returns a list of error strings, one for each row whose `read_tool` is not null and not in `served`, naming the row. Call it in `main` after the tool index is built, with `served` = the census's tool names, and REFUSE the emit (the same way the tool-index errors refuse) on a non-empty result.
- Add `tool_index/pending_members.yaml`: a mapping `pending:` holding two entries in the shape of a `members.yaml` entry: `harvest_list` and `harvest_read`, `member: b`, `owner: AMGT_HARVST`. In `load_tool_index`, an entry of `pending:` is used ONLY when the census serves that tool; when it does not, skip it and print `tool_index: pending <tool> -- not served yet` (never an error). All current behaviour stays: a served tool with no entry in `members.yaml` or `pending:` is an error; a `members.yaml` entry for an unserved tool is an error; a tool in both files is a duplicate error. `load_tool_index(row_ids, census=None, row_keys=None)` keeps its signature (the check injects a census).

### Part 3 -- the version (item 6)

The emitter's header text (the triple-quoted string that today holds `version: 0.4`) becomes `version: 0.5` with `supersedes: v0.4 (...)`, and a new paragraph (comment lines) quoting
Andrew's word EXACTLY and citing its record. Quote exactly this sentence, as one string (a line break between `# ` comment lines is fine):

> We need to colonize that bucket. We need to figure out all the gold and silver tables that are in that bucket and where we want to create tools because the asset managers need to be able to do direct research right to the bucket.

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md`. Say in one line that v0.5 widens the harvest rows from 39 source-level prefixes to one row per dataset (78), read-only, Opal-internal. Widen nothing else.

### Part 4 -- discover answers what the rows now carry (reason for a fourth criterion: the PRD asks that plain words reach the table and that a retired table is never a tool target)

In `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`:
- `_harvest_answer` adds `retired` (a bool, false when the row lacks it) to every answer. When true it also adds `retired_reason`, sets `next_tool` null and `servable` false even if the row names a `read_tool`, and the `gap` reason starts `retired: ` followed by the row's reason (the gap owner is the row's `gap_owner` or `unowned`);
- the text by which a harvest row is matched (its "own text") also includes its `nl_tags` (joined by a space), so that a plain-word tag reaches the row.
Add exactly three tests to `infra/aws/ec2/opal-gateway/tests/test_opal_discover.py`, each on a fixture row or fixture catalog (not the live catalog), named exactly:
`test_harvest_retired_flag_in_answer`, `test_harvest_retired_row_is_not_a_tool_target`, `test_harvest_nl_tags_reach_the_row`.
Two existing tests there assume the old rows and must change so they hold for 39 rows now AND for 78 rows with named readers later:
- `test_every_harvest_row_is_reachable_by_its_own_example_question`: change `len(rows) == 39` to `len(rows) >= 39`;
- `test_harvest_rows_answer_as_themselves_with_their_gap`: replace the three assertions that `read_tool is None`, `next_tool is None` and `servable is False` with their consistency: `(row["read_tool"] is None) == (m["next_tool"] is None)`, `m["servable"] == (m["next_tool"] is not None)`, and the gap owner assertion only when `row["read_tool"] is None`.

Also write your own tests for Parts 1 to 3 in `workflows/atom_decomposition/tests/test_harvest_table_grain.py`.

## 2. BOUNDS

1. You change only the files in `<paths>`. No `catalog_entries/` row, no `DATA_CATALOG.yaml`, no `members.yaml` edit (the harvest tools go in `pending_members.yaml`), no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. Grade the gateway suite by failing-ID DELTA (`suite_delta.py`). The known failures (rows Z-S97, Z-S107) are listed, never fixed here.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8).
4. The checks build their own 78 correct rows and their own one-defect rows. You can read the check files under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/` to see the exact interface they call. Do not edit them.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/tool_index/pending_members.yaml
workflows/atom_decomposition/tests/test_harvest_table_grain.py
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~36/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W36-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3,AC4</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c11.AC1.sh; echo "exit=$?"</invocation><expect>ACCEPT: 78 of 78 correct table-grain rows load; REFUSE: 11 of 11 one-defect rows refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c11.AC2.sh; echo "exit=$?"</invocation><expect>ARMS pass 6 of 6 (pending members apply only when served; a row names only a served tool; the old refusals stay) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c11.AC3.sh; echo "exit=$?"</invocation><expect>CHECKS pass 6 of 6 (version 0.5, supersedes v0.4, Andrew's verbatim exact, the record path cited) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-c-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round13/checks/c11.AC4.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~36/NFRA_MCPINDEX.TO-MX-c-11.table-grain-loader-pending-tools-version.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all four criteria PASS.
3. Commit everything together.
4. Report once, with:
   - the validator change by constant and function;
   - the `pending_members.yaml` entries and the four arms' readings;
   - the discover answer for a retired fixture row (print it);
   - the suite delta;
   - your commit sha.

The issuer then merges this with `MX-c-12`, regenerates the catalog and runs the drain checks.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 13, chain head, worker ~36, parallel to `MX-c-12` (no shared file). Source: PRD v0.11 @7878037d98
(1.0.0_SA_CTO~Z msg 34078) items 3 and 6, plus the loader the 78 rows need. The fourth criterion is Part 4 (the PRD asks that plain words reach
the table and that a retired table is never a tool target). The catalog is NOT regenerated by this cell: the drain does it (R13.4).
Battery and planted arms: decomposition R13.3.

<status>issued</status>
<round>13</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
