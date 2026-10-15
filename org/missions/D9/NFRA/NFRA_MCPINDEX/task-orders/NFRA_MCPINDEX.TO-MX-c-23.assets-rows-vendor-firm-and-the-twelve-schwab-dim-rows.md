# NFRA_MCPINDEX task order -- `MX-c-23` -- ASSETS: `bucket`, `vendor`, `firm` on all 136 opal-data-assets and opal-data-bd rows, the twelve Schwab `dim_*` rows, the curated tags, and the registry `labels`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-23</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-23</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~45</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change: a catalog row and its labels are text; the visibility of a labelled row is a gate decision the release's never-widen pair covers (CTO msg 34562), and data access stays behind the firm's data grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the visibility difference control (c23.AC3: BASE tree against NEW tree, every silver row x six principals, cross-firm leaks 0) and the planted arms (decomposition R18.4) are the control; the release order MX-r-15 carries the never-widen pair naming the rows.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-23` (round 18, workstream ASSETS; PRD v0.17 CONTRACT C-GROUP item 2)

**Start only when `MX-c-21` is complete and drained.** The issuer continues you with an amendment (A1) that names the merged emitter; until it arrives, do nothing. (You hold this slot's queue after MX-c-21; your worktree is the one A1 names.)

Work in your own worktree (cut from `box/sitez` after MX-c-21 merged). Every path is relative to its root. **First**, run once: `git sparse-checkout add workflows infra/aws/ec2/opal-gateway org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census` (the only sparse change you may make).

**Why.** PRD v0.17 CONTRACT C-GROUP item 2: every opal-data-assets and opal-data-bd row carries `vendor` and `firm`, beside `bucket`; and NFRA_OPLGTW (msg 34560) found that the four Schwab `dim_*` tables of each of the three masters have no catalog rows, so its client adapters are refused (`no_catalog_row`). The issuer authored the data: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json` (136 entities with `bucket`, `vendor`, `firm`, derived by rule; 7 also carry curated `nl_tags`), and `round18/unskip_schwab_dim.json` (the 12 contract ids). You do NOT edit them. `MX-c-21` made the emitter apply a map (`--group-map`).

**What to build.**

1. **`gen_silver_rows.py` generates the 12 rows**: a new optional argument `--unskip FILE` (JSON; reads its `contract_ids` list; default none; a named file that does not exist exits 2 like `--g5r`). `is_skipped(c)` stays as it is, except that a contract whose `contract_id` is in that list is NOT skipped. Add `--unskip org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/unskip_schwab_dim.json` to the regeneration line (step 2).
2. **Registry `labels`**: a new optional argument `--labels-from FILE` (default none; named file missing exits 2): reads a group map like `assets_group_map.json` and writes the sorted set of every `vendor` and `firm` value in it as a top-level `labels` list of `catalog_fork_keys.json` (beside `_about`, `rows`, `entities`), preserved on every later write. The naming gate admits a catalog literal only as a whole string held at HEAD in that file, so the labels must be COMMITTED before the catalog (step 4).
3. **Tests**: add tests to `workflows/atom_decomposition/tests/test_gen_silver_rows.py` or a new `tests/test_assets_rows.py` (at least 6): `--unskip` generates exactly the listed ids and none other, an absent default changes nothing, a missing named file exits 2, `--labels-from` writes the sorted set and keeps it on a second write, the 12 entity names, the new rows carry `read_tool` null and `gap_owner` NFRA_OPLGTW when the deployed list has no `client_*` tool.

### Steps

0. The sparse command. The deployed-tools list is the committed `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/deployed_ap20.json` (99 names); step 2 passes it as `--deployed-tools`.
1. Make the generator change and the tests. Run `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` (all pass).
2. Regenerate the rows AND the fork registry (the `...` is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`; do not pass the legacy registry file):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 .../G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/deployed_ap20.json --firm-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json --fork-registry-file infra/logic/registry/catalog_fork_keys.json --unskip org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/unskip_schwab_dim.json --labels-from org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json`
   It must write 228 rows. `git status` must then show EXACTLY these changes: 12 NEW files under `catalog_entries/` (`opal_data_assets_silver_schwab_<master>_dim_<table>.yaml`) and `infra/logic/registry/catalog_fork_keys.json` modified; its `git diff` adds the 12 new `rows` entries, 12 names to `entities`, and the `labels` list, and changes nothing else; no existing row file is modified (a modified existing row file is a defect to report, not to commit).
3. Regenerate the catalog in your worktree: `python workflows/atom_decomposition/emit_catalog_v02.py --group-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/assets_group_map.json` (it must end with the HARVEST ROWS, SILVER and TOOL INDEX lines, `GROUP-MAP unused: 0`, and no EMIT REFUSED line). Do NOT commit `DATA_CATALOG.yaml` (a later amendment lands it).
4. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the two data files, `emit_catalog_v02.py`, `validate_catalog_v02.py`, `tool_index/`, an existing `catalog_entries/` row, the legacy registry, the checks, or any gateway file; no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. No firm, vendor or product name is typed as a whole-string literal in `gen_silver_rows.py` (the labels come from the map file; tests under `tests/` are exempt).
3. The registry file is written by the generator run in step 2, never by hand. A commit that touches it may be refused by a registry or naming gate; if it is, report the refusal text and stop on that file (the issuer rules it).
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC1.sh`, `c23.AC2.sh`, `c23.AC3.sh` (python `c23_check.py`, which calls the round 17 `vis_matrix.py`). Read `c23_check.py` for exactly what is graded. Do not edit them.
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/tests/
workflows/atom_decomposition/catalog_entries/
infra/logic/registry/catalog_fork_keys.json
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W45-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR map entities 136; rows equal to the map 136; stray rows 0; values outside the lists 0; ASSETS rows still inferred 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR new rows present 12 of 12; wrong 0; table rows 228; base rows changed outside bucket/vendor/firm 0; unexpected new rows 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC3.sh; echo "exit=$?"</invocation><expect>DENOMINATOR silver rows 233 x principals 6 = 1398 pairs; cross-firm leaks 0; multi, none and unresolved rows visible to no firm principal -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/NFRA_MCPINDEX.TO-MX-c-23.assets-rows-vendor-firm-and-the-twelve-schwab-dim-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance (encode the literal printed tokens for the prose `expect`, disclose it in a row, and pin every artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file predates the instance).
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in THREE commits in this order: (i) `gen_silver_rows.py` and the tests; (ii) the registry file ALONE (so the labels are held at HEAD); (iii) the 12 new row files, the proof instance and the outputs you saved. Never `DATA_CATALOG.yaml` (a later amendment lands the final catalog, emitted by the issuer against the shipped cut).
4. Report once, with: the change by function; the AC1 and AC3 DENOMINATOR lines verbatim, with the per-firm lines of AC3; the `git status` and the registry `git diff --stat` of step 2; the test counts; the three commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 18, workstream ASSETS, worker ~45, queued behind `MX-c-21`. Source: PRD v0.17 C-GROUP item 2, CTO msgs 34562 and 34579, NFRA_OPLGTW msg 34560. Measured at the cut: the map covers 124 existing rows (the 111 + 8 generated, the 5 older) plus the 12 new; `vendor` counts schwab 61, blackdiamond 31, smartx 13, commonwealth 12, market 9, orion 5, eclipse 4, gateway 1; `firm` counts 49financial 85, cottonwood 26, inflection 9, multi 7, none 9; 0 unresolved. The widening the labels cause (about 96 rows newly visible to their own firm) is graded in `c23.AC3` and covered by the release's pair. The expect line of AC3 says 233 rows (221 + 12) x 6 = 1398 pairs. Base dry-runs 2026-10-15: `c23.AC1` FAIL, `c23.AC2` FAIL, `c23.AC3` FAIL, as expected. Planted arms: `plant_r18.py` 11 of 11 on c23.

<status>issued</status>
<round>18</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
