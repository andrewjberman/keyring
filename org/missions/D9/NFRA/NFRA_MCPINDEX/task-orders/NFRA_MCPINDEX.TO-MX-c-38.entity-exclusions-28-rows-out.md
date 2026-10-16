# NFRA_MCPINDEX task order -- `MX-c-38` -- 28 catalog rows the CTO ruled out of the finish line leave the row files, and the row generator reads an entity-exclusions file so a regeneration does not bring them back

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round18-RESEARCH.md</decomp_doc>
<owned_cells>MX-c-38</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-38</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~57</issued_to>
<issued_by>2.0.0_SA_COO~MI2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the generator, one test file and 28 removed row files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the difference control inside `c38.AC1` (every written row equals its committed row outside the three link fields) are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-38` (round 18, workstream RESEARCH-EXCL; PRD v0.17: C-GROUP, finish line 2026-10-16 ~22:00Z)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The silver table rows in `workflows/atom_decomposition/catalog_entries/` are written by `workflows/atom_decomposition/gen_silver_rows.py` from pinned inputs. The CTO (ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md`) ruled 28 rows out of the finish line: no tool reads them and each is not a served research surface. The issuer's data file `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/entity_exclusions.json` is `{"_about": "...", "entities": {"<entity>": "<reason class>", ...}}` (28 entries; you do NOT edit it). A regeneration with the pinned inputs writes all 28 again, so deleting their files alone is not enough: the generator must know.

**What to build.**

(a) **`entity_exclusions` in `gen_silver_rows.py`.**
   - New optional argument `--entity-exclusions FILE`. DEFAULT: the file above, resolved from the repo root (the generator already knows its own location: `HERE`); an absent DEFAULT file means no exclusion; a file named by the argument that does not exist exits 2, and so does one that does not parse or holds no `entities` object of non-empty strings; exactly as `--scope-exclusions` and `--read-links` do.
   - A contract whose entity (`entity_of(contract_id)`) is a key of `entities` is not written; the generator prints one line `excluded <entity>: <reason>` for it (`<reason>` is the value); the final `wrote N rows` counts only written rows. No entity or reason is typed in code.
   - `git rm` the 28 row files named by the keys of `entities`. Remove no other row.
   - Keep your change to the new argument, one small loader and the one place `--scope-exclusions` already skips a contract, so it merges hunk-disjoint with `MX-c-31` (`--read-links`, another worker edits this file now). Your command line must keep working unchanged (the argument has a default).

(b) **Tests.** A NEW file `workflows/atom_decomposition/tests/test_entity_exclusions.py` with at least 5 tests: a contract whose entity is listed is skipped and reported; one that is not listed is written; an absent default file changes nothing; a missing named file exits 2; the count printed equals the rows written. Fix any EXISTING test that pinned the 214-row count (the new count is 186).

### Steps

0. From the worktree root, `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` passes before you start (a control). If `workflows/` is missing, run `git sparse-checkout add workflows` once; the generator also reads `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38`, `.../2.0.0_SA_COO~MI`, `.../2.0.0_SA_COO~MI2` and the registry files: add whichever is missing with `git sparse-checkout add <folder>` (the only sparse change you may make).
1. Make parts (a) and (b). Rerun the same pytest command (all pass).
2. Regenerate the rows with the pinned inputs (the `...` is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`; the registry files are NOT passed, they do not change):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 .../G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/deployed_r18.json --firm-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`
   It must write 186 rows and print 28 `excluded` lines for the entities (plus the two prefix lines). `git status` must then show NO modified file under `catalog_entries/` other than the 28 removals your `git rm` made. Any other changed file is a defect to report, not to commit.
3. Run the two criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `entity_exclusions.json`, `deployed_r18.json`, the checks, `scope_exclusions.json`, any other `catalog_entries/` row, the emitter, a registry file, any gateway file or the catalog; do NOT commit `DATA_CATALOG.yaml`. No tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. `MX-c-31` (worker ~56) adds `--read-links` and `read_tool_with_links` in the same file; rebase nothing, keep your hunks small.
3. No tool, firm or entity name is typed as a whole-string literal in code; tests under `tests/` are exempt.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c38.AC1.sh` and `c38.AC2.sh` (python `c38_check.py`). Read `c38_check.py` for exactly what is graded. Do not edit them. (`c30.AC1` pins the old 214 and is superseded by `c38.AC1`; do not run or fix it.)
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~57/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W57-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI2`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-38" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c38.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (entities 28; fresh generator rows 186); none of the 28 is a row file, the fresh run writes exactly 186 rows and none of the 28, 28 `excluded` lines carry the file's reasons, every fresh row is a committed row and equals it outside read_tool/tools/gap_owner -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-38" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c38.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_entity_exclusions.py; at least 5 tests passed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~57/NFRA_MCPINDEX.TO-MX-c-38.entity-exclusions-28-rows-out.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the generator and tests first, then the 28 removals, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order only if both criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in three commits: (i) the generator and the tests; (ii) the 28 removed row files; (iii) the proof instance (and the status flip). Never `DATA_CATALOG.yaml`.
4. Report once, with: the change by part; the `git status` of step 2; the AC1 DENOMINATOR line verbatim; the unit-test count; your commit shas.

The issuer then merges after `MX-c-31`; the ASSETS issuer's one emitter run uses the merged tree.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI2).** Round 18, workstream RESEARCH-EXCL (the gate keys one issuance per (workstream, round); RESEARCH and RESEARCH-LINKS are taken), worker ~57. Source: CTO ruling @32a4dd88dd on `research_no_tool_dispositions.md` @e8cd68632d: of the 32 section-(b) rows, 29 ratified and 3 amended. Two of the 32 (`..._platinum_advi_49financial_perfrp` and `_twins`) were already removed by `MX-c-30` (prefix `platinum/advi/`); `opal_data_portal_v2_served_cma_assumptions` moves to (a) (current 2026 edition, read by the CapitalMarketAssumptions page) and `opal_data_mdpf_gold_ai_classified_securities` leaves (b) (no tool reads the DynamoDB etf-classifications table it points at; the table goes to (a)), so neither is excluded; `opal_data_portal_v2_served_benchmark_returns` is excluded with reason class `held_at_andrew` and reopens on his word. 32 - 2 - 2 = 28. The three rows OPLGTW (`2.0.0_SA_COO~O`, msg 34657) says it cannot serve by the line (harvest_articles table empty, market_updates and semantic_news_trending_daily not current) are NOT in this cut: the CTO has not ruled them; a ratified batch is appended to `entity_exclusions.json` by a later amendment. Base dry-runs 2026-10-16 at 5aeafbda15: `c38.AC1` FAIL as expected (28 are committed rows; the generator writes 214; 0 of 28 `excluded` lines), `c38.AC2` FAIL as expected (test file absent). AC1's two difference arms (every fresh row is a committed row; equal outside the three link fields) PASS at the base and are the control that no other row moves; they exclude the three link fields because `MX-c-31` (read-links) merges around the same time. The reason values are classes (no tool or firm token), so the file passes the naming gate under `org/`. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>18</round>
<workstream>RESEARCH-EXCL</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
