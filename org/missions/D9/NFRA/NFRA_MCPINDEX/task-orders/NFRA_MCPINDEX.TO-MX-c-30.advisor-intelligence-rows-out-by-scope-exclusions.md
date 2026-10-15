# NFRA_MCPINDEX task order -- `MX-c-30` -- the two advisor-intelligence rows out of the catalog, by a scope-exclusions file the row generator reads

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round18-RESEARCH.md</decomp_doc>
<owned_cells>MX-c-30</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-30</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~50</issued_to>
<issued_by>2.0.0_SA_COO~MI2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the generator, one JSON file, two removed row files and one test file only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the difference control inside `c30.AC1` (all 214 other rows byte-equal) are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-30` (round 18, workstream RESEARCH)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The gateway catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` is emitted from the row files in `workflows/atom_decomposition/catalog_entries/` by `workflows/atom_decomposition/emit_catalog_v02.py`; the silver table rows are written from pinned inputs by `workflows/atom_decomposition/gen_silver_rows.py`.

**Why.** Andrew put advisor-intelligence and investor-reporting surfaces out of the gateway catalog. Two catalog rows describe advisor-intelligence tables under `platinum/advi/49financial/`: `opal_data_portal_v2_platinum_advi_49financial_perfrp` and `opal_data_portal_v2_platinum_advi_49financial_twins`. A regeneration of the rows with the pinned inputs writes them again (measured: the generator writes all 216 committed row files byte-equal), so deleting the two files alone is not enough: the generator must know the scope.

**What to build, in three parts.**

(a) **The exclusions file and the generator.**
   - New file `workflows/atom_decomposition/scope_exclusions.json`: `{"prefixes": ["platinum/advi/", "platinum/irpt/"], "reason": "..."}`; the reason names Andrew's scope (advisor intelligence and investor reporting surfaces are out of the gateway catalog; PRD v0.17 of NFRA_MCPINDEX).
   - In `gen_silver_rows.py`: a new optional argument `--scope-exclusions FILE` (default: `scope_exclusions.json` beside the generator; an absent DEFAULT file means no exclusion; a file named by the argument that does not exist exits 2, exactly as `--tool-reads` and `--firm-map` do). A contract whose row prefix starts with any listed prefix is not written; the generator prints one `excluded <entity>: <prefix>` line per skipped contract; the final line `wrote N rows` counts only written rows. The prefixes come from the file; none is typed in code. Find the contract's prefix where `build_full` or the writer already computes it (`leading_prefix(c, rec)`): compare that value.
   - `git rm` the two row files named above.
   - Do NOT remove `opal_data_portal_v2_platinum_mdpf_cottonwood_account_units` or `opal_data_portal_v2_platinum_mdpf_manifests_and_archive`: they sit under `platinum/mdpf/` (the model-portfolio surface) and stay.

(b) **Tests.** A NEW file `workflows/atom_decomposition/tests/test_scope_exclusions.py` with at least 5 tests: a contract under an excluded prefix is skipped and reported; one under another prefix is written; no default file changes nothing; a missing named file exits 2; the run is deterministic; the count printed equals the files written. Fix any EXISTING test under `tests/` that pinned the 216-row count (the new count is 214 written rows).

(c) **The record.** Write `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~50/SCOPE_DROP_RECORD.md`: the 2 dropped entities (entity, prefix), the 2 `platinum/mdpf/` candidates that stayed (entity, prefix, one line on why they are not advisor intelligence or investor reporting: read each row's `business_meaning`), and the two orphan entries `infra/logic/registry/catalog_fork_keys.json` still holds for the dropped rows (entity names; you do NOT edit the registry).

### Steps

0. From the worktree root, `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` passes before you start (a control). If `workflows/`, `infra/aws/ec2/opal-gateway/` or the census folder is missing, run `git sparse-checkout add workflows infra/aws/ec2/opal-gateway org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census` once (the only sparse change you may make).
1. Make parts (a) and (b). Rerun the same pytest command (all pass).
2. Regenerate the rows with the pinned inputs (the `...` is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`; the registry files are NOT passed, they do not change):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 .../G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/deployed_ap20.json --firm-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`
   It must write 214 rows and print two `excluded` lines. `git status` must then show NO modified file under `catalog_entries/` (the 214 equal the committed rows) apart from the two removals your `git rm` made. Any other changed file is a defect to report, not to commit.
3. Regenerate the catalog in your worktree: `python workflows/atom_decomposition/emit_catalog_v02.py --overlay-ref 06cfb6db64` (it must end with HARVEST ROWS, SILVER and a TOOL INDEX line reading `N=99 served tools`, and no EMIT REFUSED line; if it refuses on the two orphan registry entries, report the refusal text and stop on that point). The emit rewrites `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` in your worktree; that file is NOT in `<paths>` and you do NOT commit it (leave it modified, it is never staged).
4. Run the two criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No other `catalog_entries/` row, no registry file, no `DATA_CATALOG.yaml` commit, no emitter edit (another issuer's order, `MX-c-21`, changes the emitter in this round), no gateway file, no portal file, no tool, grant, route, role, `.env` or AWS change. No deploy. No push. Do NOT edit the checks.
2. Another order (`MX-c-23`, workstream ASSETS) edits `gen_silver_rows.py` at the same time (an `--unskip` argument and a labels argument): keep your change to the new argument, one small loader and the one point where a contract is skipped, so the merge is hunk-disjoint. Their regeneration command must keep working unchanged: your argument has a default.
3. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token); tests under `tests/` are exempt.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c30.AC1.sh` and `c30.AC2.sh` (python `c30_check.py`). Read `c30_check.py` for exactly what is graded (AC1 grades the catalog you emitted in step 3 and runs a fresh generator itself). Do not edit them.
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/scope_exclusions.json
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~50/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W50-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI2`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-30" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c30.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (catalog entities 302; generator wrote 214); neither advisor row is a file or an entity, the fresh run writes 214 rows and neither file, every file it wrote equals the committed file (0 differ), no emitted row under platinum/advi/ or platinum/irpt/ -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-30" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c30.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_scope_exclusions.py; at least 5 tests passed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~50/NFRA_MCPINDEX.TO-MX-c-30.advisor-intelligence-rows-out-by-scope-exclusions.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the record (part c) and the proof instance.
2. APPEND `<status>complete</status>` only if both criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in three commits: (i) the generator, `scope_exclusions.json` and the tests; (ii) the two removed row files and the record; (iii) the proof instance. Never `DATA_CATALOG.yaml` (it is not in `<paths>`; stage only the files named).
4. Report once, with: the change by part; the AC1 DENOMINATOR line verbatim; the `git status` of step 2; the unit-test count; your commit shas.

The issuer then merges; the ASSETS issuer's one emitter run (`MX-r-15`) uses the merged generator.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI2).** Round 18, workstream RESEARCH, worker ~50. Source: PRD v0.17 CONTRACT C-GROUP and its scope line, CTO msg 34559. **Descoped from the first draft of this cut, same hour:** the `bucket` normalisation (DynamoDB prose to `dynamodb`; the `portal_datasets` bucket) and the curated-tags loader were in this order and in a second order (`MX-c-33`); the ASSETS issuer's `MX-c-21` (msg 34584) ships both in the emitter (`bucket` on every row, `--group-map`), so this order keeps only the scope drop and `MX-c-33` was never cut. The RESEARCH rows' `bucket` is graded at the drain (`c30_check.py bucket`, `c30.DRAIN.sh`) on the catalog emitted with that emitter. Base dry-runs 2026-10-15 at 5858411c5c: `c30.AC1` FAIL as expected (the generator writes 216 and both files exist; the difference control reads 0 differ), `c30.AC2` FAIL as expected (the test file is absent). Planted arms: `plant_c30.py` 7 of 7 grade the drain `bucket` check; AC1 and AC2 grade the real tree, so the base FAIL is their arm. The registry file is NOT in `<paths>` (a registry path or the emitted catalog would make the order WORLD by the L6 floor, so neither is in `<paths>`); the two orphan entries it keeps for the removed rows are read row by row and expected harmless. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>18</round>
<workstream>RESEARCH</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
