# NFRA_MCPINDEX task order -- `MX-c-17` -- the silver-row generator applies the G5r enrichment to the 14 rival-fund rows, and regenerates them

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-17</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-17</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~41</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the generator, its rows and its tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs plus the planted PASS and FAIL arms are the control (decomposition R16.3a).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-17` (round 16; PRD v0.16, FWD-22 enrichment G5r)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root. The generator is `workflows/atom_decomposition/gen_silver_rows.py` (it wrote the 216 committed rows of `workflows/atom_decomposition/catalog_entries/` and the two registry files). The enrichment DATA is a file the issuer already wrote and you do NOT edit: `workflows/atom_decomposition/g5r_enrichment.json` (`rows` maps a row's entity name, e.g. `opal_data_etfs_gold_canonical_shape`, to `meaning_add`, `never_sum` and `nl_tags_add`).

**What to build.** The generator applies the enrichment, so a regeneration keeps it. For each in-scope contract whose entity name (the row's file stem, the generator's `entity_of(contract_id)`) is a key of `rows`, the FULL row (before it is sanitised and split into the clean row and the registry entry) changes in three fields:
- `business_meaning` becomes the old text, one space, then `meaning_add`;
- `never_sum_rules` becomes a list: the old value if it is a list (otherwise an empty list), then `never_sum` as a last item;
- `nl_tags` becomes the old list followed by `nl_tags_add`.
The sanitiser and the registry split then run as before, on the changed full row. A contract whose entity is not a key is untouched. The file is read from `workflows/atom_decomposition/g5r_enrichment.json` next to the generator, with a new optional argument `--g5r FILE` to name another; an absent default file means no enrichment (not an error). Add your own tests to `workflows/atom_decomposition/tests/test_gen_silver_rows.py` (an enriched entity gets the three changes; an unlisted entity does not; a missing file changes nothing).

### Steps

0. From the worktree root build the deployed-tools file the committed rows were generated under (so nothing drifts with today's census): `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round16/checks/deployed_from_rows.py .scratch/deployed.json` (it prints `deployed tools written: 1`).
1. Change the generator and its tests. Run `python workflows/atom_decomposition/tests/test_gen_silver_rows.py` (all pass).
2. Regenerate the rows with the pinned inputs and write them in place; the two registry files are NOT passed (they do not change):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools .scratch/deployed.json`
   (the `...` is the same folder as the `--g2` file). It must write 216 rows. `git status` must then show EXACTLY the 14 rival-fund row files modified (the 13 `opal_data_etfs_gold_*` rows named in the enrichment file and `opal_data_etfs_platinum_rivalfunds_page.yaml`) and no registry file; any other changed file is a defect to report, not to commit.
3. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. The two registry files are NOT yours: the enrichment text carries no firm or product token, so no registry value moves; if `git status` shows a registry file changed, that is a defect to report, never to commit. Do NOT edit `g5r_enrichment.json`, `emit_catalog_v02.py`, `DATA_CATALOG.yaml`, the checks, the tool index or any gateway file. No tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. No contract id, firm name or product name is typed as a whole-string literal in `gen_silver_rows.py` (the naming gate refuses a NEW hand-kept firm or product token in code; the tests under `tests/` are exempt).
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC2.sh`, `c14.AC3.sh` and `deliverables/2.0.0_SA_COO~MI/round16/checks/c17.AC2.sh` (python `c17_check.py`); the round 14 builder `glib.py` already applies the enrichment. Read them for exactly what is graded. Do not edit them.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/tests/test_gen_silver_rows.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~41/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W41-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-17" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC2.sh; echo "exit=$?"</invocation><expect>ROWS graded 216 of 216; failing fields: none -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-17" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round16/checks/c17.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (table rows 226; enriched 14; rows differing from the base 14) and CHECKS pass 15 of 15 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-17" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c14.AC3.sh; echo "exit=$?"</invocation><expect>ARMS pass 5 of 5; rows graded right 1080 of 1080 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~41/NFRA_MCPINDEX.TO-MX-c-17.g5r-rival-fund-row-enrichment.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit everything together through `.tools/safe-commit.sh`, the generator and its test first, then the 14 rows in a second commit.
4. Report once, with:
   - the generator change by function;
   - one enriched row's `business_meaning` tail, `never_sum_rules` and `nl_tags` (no more than 12 lines);
   - the AC2 DENOMINATOR line and your commit shas.

The issuer then merges and regenerates the catalog at the drain.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 16, worker ~41, parallel to `MX-c-16` (no shared file). Source: PRD v0.16 and `G5r_rivalfunds_spec.md` @e1b9937129. The issuer verified on 2026-10-15 that regenerating the 216 rows with the pinned inputs and the derived deployed-tools file reproduces every committed row byte for byte, so the only rows that move are the 14. Base dry-runs: `c14.AC2` FAIL (the builder expects the additions), `c17.AC2` FAIL (0 of 15), as expected; `c14.AC3` PASSES at the base as expected (a control: the read_tool and tools arms must not drift when the enrichment lands). Planted arms: `plant_c17.py` 4 of 4, `plant_c14.sh` 24 of 24.

<status>issued</status>
<round>16</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-15 ~01:2xZ), on rows Z-W41-S1 and Z-W41-S2.** (S1) The order's AC2 expect text said `table rows 216`; the check counts every table row in the folder, 226 (the 216 the generator writes and 10 older rows it does not), so the denominator in the order was the issuer's error. The check, not the text, is right: on the merged tree `c17.AC2` reads `DENOMINATOR table rows 226; enriched 14; rows whose bytes differ from 0f40810fa2: 14`, `CHECKS pass 15 of 15`, `RESULT: PASS`. AC2 is graded PASS by the issuer. (S2) An explicit `--g5r` path that does not exist exits 2 and an absent default file means no enrichment: ruled correct, no change. Merged at d0e04b517d. Gate limb that graded this ruling: none (LIMB 6 does not fire on a modification).
<status>complete</status>

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-15 ~02:0xZ), a one-step re-seat.** Your proof instance records AC2 as FAIL on the order's own wrong denominator text (the issuer's ruling above grades AC2 PASS); the round-close check refuses a FAIL row, and the lane gate refuses the issuer your deliverables folder. Your ONLY act: (1) from your worktree run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/regrade_instance.py <your worktree root>` (it prints `regraded AC2 FAIL -> PASS; acceptance rows 3`; any other output: stop and report); (2) run `python .tools/proof-of-spec-check.py <that instance path>` and require rc=0; (3) commit exactly that one instance file with `safe-commit.sh`, first line `proof(NFRA_MCPINDEX.TO-MX-c-17 A1, 0.9.0_WK_NFRA_MCPINDEX~41): AC2 regraded PASS on the issuer's ruling`, body one line citing the ruling, push state LOCAL, Co-Authored-By Haiku line; (4) report the commit and the checker's rc. Edit nothing else. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification).
<status>issued</status>
<status>complete</status>
