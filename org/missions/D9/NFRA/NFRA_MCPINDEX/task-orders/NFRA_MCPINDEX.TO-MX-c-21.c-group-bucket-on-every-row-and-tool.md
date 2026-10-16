# NFRA_MCPINDEX task order -- `MX-c-21` -- CONTRACT C-GROUP item 1: `bucket` on every catalog row and every tool_index entry, `source_group`, and the emitter's `--group-map`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-21</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-21</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~45</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the emitter, the tool index source and tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs plus the planted arms are the control (decomposition R18.4).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-21` (round 18, workstream ASSETS; PRD v0.17 CONTRACT C-GROUP item 1)

Work in your own worktree (cut from `box/sitez`). Every path below is relative to its root. **First**, run once: `git sparse-checkout add workflows infra/aws/ec2/opal-gateway org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census` (the emitter reads the census from that folder; without it the emitted catalog records a wrong census path). That is the only sparse change you may make. The one catalog writer is `workflows/atom_decomposition/emit_catalog_v02.py`; it writes `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, which you REGENERATE in your worktree to grade the checks and do NOT commit.

**Why.** Andrew wants the gateway view and discovery segmented by the S3 bucket each tool reads. PRD v0.17 CONTRACT C-GROUP item 1: every catalog row and every `tool_index` row carries `bucket` (the S3 bucket name the row reads, or `dynamodb`, or `graph` for the Microsoft tools, or another store's name for a non-S3 tool); `source_group.id` IS that value. Today 10 of 304 rows have no bucket, 10 carry a prose value (`none (DynamoDB us-east-1)`, `dynamodb (not opal-data-portal-v2)`), and `tool_index` has no bucket at all.

**What to build.**

1. **`bucket` on every row** (the three sections `silver_datasets`, `portal_datasets`, `harvest_datasets`), decided in the emitter when it writes a row, after the group map (item 2) is applied:
   - a bucket that is an S3 bucket name (`opal-data-` followed by lowercase letters, digits and hyphens) is kept exactly;
   - a bucket string that names DynamoDB in any wording (`none (DynamoDB us-east-1)`, `dynamodb (not opal-data-portal-v2)`, `dynamodb + s3://opal-data-trade-submissions (not opal-data-portal-v2)` ...) becomes the single word `dynamodb`;
   - a row with no `bucket` takes the group map's value for its entity, else (a `portal_datasets` row) the catalog's top-level `bucket`; a row that still has none is an EMIT REFUSED error naming the entity.
2. **`--group-map FILE`** (repeatable; absent means none; a named file that does not exist exits 2 like `--g5r`): a JSON file `{"rows": {"<entity>": {"bucket"?: "...", "vendor"?: "...", "firm"?: "...", "nl_tags"?: ["...", ...]}}}`. For each entity of the map that is a row of the emitted catalog: set the given keys on the row (`bucket`, `vendor`, `firm` after the row's existing keys); `nl_tags` REPLACES the row's tags and removes the row's `nl_tags_basis` key. Validation, refusing the emit with the entity named: `vendor` one of `schwab blackdiamond orion eclipse smartx commonwealth gateway market`; `firm` one of `49financial cottonwood inflection multi none unresolved`; `bucket` as in item 1; `nl_tags` a list of 3 to 6 distinct strings of 2 to 5 lowercase ASCII words; a map `firm` that conflicts with a `firm` the row already carries is refused. A map entity that is not a row is NOT an error: print `GROUP-MAP unused: <n>` (the entities are listed after the count, first 20). Two maps naming the same entity: refused. Print one line `GROUP-MAP rows applied: <n> of <m> entities`.
3. **`tool_index`**: every entry gains `bucket` and `source_group: {id, name, kind}`, written after the entry's other keys:
   - the bucket of a member-`a` tool is the bucket of its `index` row; of any other tool that catalog rows name as `read_tool`, the most frequent bucket among those rows (ties: alphabetical);
   - a tool no row names declares `bucket:` in `workflows/atom_decomposition/tool_index/members.yaml` (a new optional field on a member), with `bucket_source: <path>:<line>` (path relative to `infra/aws/ec2/opal-gateway`, the line in the tool's own code where it names the bucket or the store: for an S3 bucket the line must contain the bucket name within 6 lines; for `graph` the line of the Microsoft Graph call). You declare it for EVERY tool the rows do not name: read the tool's definition (the tool index's `definition` field gives its file and line). Classify by what the tool's code reads, never by its name: Microsoft Graph tools (mail, calendar, SharePoint, Teams, OneDrive) `graph`; the harvest tools `opal-data-harvest`; the YCharts tools `ycharts`; the Kuzu graph tools `kuzu`; a tool that reads only gateway state `gateway`. A tool reading several buckets takes its primary one;
   - `source_group.id` = the bucket; `kind` = `bucket` for an `opal-data-` bucket, `graph` for `graph`, else `store`; `name` = the bucket name for kind `bucket`, `Microsoft 365` for `graph`, else the bucket word title-cased.
   - the emitter refuses a tool with no derivable and no declared bucket, naming the tool.
4. **Tests**: a NEW file `workflows/atom_decomposition/tests/test_c_group.py` with at least 10 tests (the DynamoDB normalisation, a kept S3 bucket, a missing bucket refused, the map applied, each validation refused, the curated tags replacing the inferred ones and dropping the basis, a conflicting firm refused, an unused map entity counted not refused, the tool bucket from rows, the declared bucket, the source_group shape). Fix any EXISTING test that pinned the old field set.

### Steps

0. The sparse command above. Then `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` passes before you start (a control).
1. Make the changes. Run the same pytest command again (all pass).
2. Regenerate the catalog in your worktree WITH the issuer's map: `python workflows/atom_decomposition/emit_catalog_v02.py --group-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json` (it must end with the HARVEST ROWS, SILVER and TOOL INDEX lines, the two GROUP-MAP lines, and no EMIT REFUSED line; `GROUP-MAP unused` is 12 at this vintage, the twelve Schwab rows a later cell adds). Do NOT commit `DATA_CATALOG.yaml`.
3. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `assets_group_map.json`, any other file under `deliverables/2.0.0_SA_COO~MI/`, the checks, a `catalog_entries/` row, a registry file, `gen_silver_rows.py`, `gen_harvest_rows.py`, or any gateway file; no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. No firm, vendor or product name is typed as a whole-string literal in code outside the validator's allowed-value tuples (tests under `tests/` are exempt); the tuples hold the C-GROUP lists exactly.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round18/checks/c21.AC1.sh`, `c21.AC2.sh`, `c21.AC3.sh` (python `c21_check.py`). Read `c21_check.py` for exactly what is graded. Do not edit them.
5. Another worker (`~46`) edits `portal_index/integration.py` at the same time (no shared file). Later `MX-c-23` edits `gen_silver_rows.py`; you do not.
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/tool_index/members.yaml
workflows/atom_decomposition/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W45-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-21" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c21.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR rows 304 (base 304); with a valid bucket 304; rows differing outside bucket/vendor/firm/nl_tags: 0; rows whose valid S3 bucket moved: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-21" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c21.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR tool_index entries 99; malformed 0; kind wrong 0; bucket differs from its rows 0; declared S3 buckets unproved 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-21" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c21.AC3.sh; echo "exit=$?"</invocation><expect>tests in test_c_group.py at least 10; pytest rc=0 on the atom_decomposition folder -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/NFRA_MCPINDEX.TO-MX-c-21.c-group-bucket-on-every-row-and-tool.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The order's expect fields are prose; the checker matches `expect` as a regex against your recorded output, so encode the literal printed tokens, as the previous workers did, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status (the order file is outside your paths); the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) the emitter, validator, `members.yaml` and the tests; (ii) the proof instance. Never `DATA_CATALOG.yaml`.
4. Report once, with: the change by function; the AC1 DENOMINATOR line, the AC2 DENOMINATOR line and the kinds line verbatim; the tools you declared in `members.yaml` grouped by bucket (counts); the unit-test counts; the two commit shas.

The issuer then merges, re-runs the criteria and starts `MX-c-23` on the merged emitter.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 18, workstream ASSETS, worker ~45, chain head (then `MX-c-23` on the same slot). Source: PRD v0.17 C-GROUP items 1 and 3; COO~MP msgs 34510 and 34525 (the field shape and the graph kind); CTO msg 34579 (Z-C-S61 curated tags, applied here through the map's `nl_tags`). Measured at the cut: of the 99 tools, 39 are named by catalog rows as `read_tool` (31 single-bucket, 8 touching an older portal row that the map and the portal rule now bucket), 60 name no row and must be declared. Base dry-runs 2026-10-15: `c21.AC1` FAIL, `c21.AC2` FAIL, as expected (`c21.AC3` runs the folder's tests in the worker's tree). Planted arms: `plant_r18.py` 9 of 9 on c21 (a good catalog passes both; a row without bucket, a `none (DynamoDB ...)` string, a moved S3 bucket, a tool bucket different from its rows, a wrong source_group id and a wrong kind each fail the criterion that grades them, and the base catalog fails AC1). The round 17 lesson on sparse worktrees is the first sentence of section 1.

<status>issued</status>
<round>18</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~02:4xZ); MX-c-21 COMPLETE.** Merged at d57f6bc02c. Graded on the merged tree with the catalog regenerated by the issuer (emit_catalog_v02.py with the five group maps, 173 of 173 applied, 100 served tools): c21.AC1 PASS (314 rows, all with a valid bucket), c21.AC2 PASS (100 of 100 tool_index entries), c21.AC3 PASS (282 passed). The issuer amended its own check c21_check.py in two places, both stale after later merges: AC1 now allows added rows only when they are MX-c-23's Schwab dim rows (graded by c23.AC2), and AC2's tool-count floor is `>= 99` (OG-ap-21 made it 100). The suite count in tests/test_c_group.py moved 60 to 61 for the one new declared bucket (harvest_get_published_analysis). Gate limb that graded this amendment: none (LIMB 6 does not fire on a modification).

<status>complete</status>
