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
workflows/atom_decomposition/emit_catalog_v02.py
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
  <expected_criteria>AC1,AC2,AC3,AC4</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR map entities 136; rows equal to the map 136; stray rows 0; values outside the lists 0; ASSETS rows still inferred 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR new rows present 12 of 12; wrong 0; table rows 226 (base 216 + 12 - removed 2); base rows changed outside bucket/vendor/firm 0; unexpected new rows 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC3.sh; echo "exit=$?"</invocation><expect>DENOMINATOR silver rows 231 x principals 6 = 1386 pairs; cross-firm leaks 0; multi, none and unresolved rows visible to no firm principal -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-c-23" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c23.AC4.sh; echo "exit=$?"</invocation><expect>DENOMINATOR tool_index entries 99; with assets or bd rows; serves wrong 0 -- RESULT: PASS -- exit=0</expect></criterion>
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

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-15 ~23:3xZ) -- START: `MX-c-21` is merged (`d57f6bc02c`); you are re-seated on slot ~45 in a FRESH worktree cut from the merged HEAD.** Four changes, then the steps in order. (1) **Row counts moved**: `2.0.0_SA_COO~MI2`'s `MX-c-30` (RESEARCH scope drop) merged: the generator now writes 214 rows, so with the 12 new ones it writes **226** (not 228), and the criteria's expect lines above are corrected (AC2 `table rows 226 (base 216 + 12 - removed 2)`, AC3 `silver rows 231 x principals 6 = 1386 pairs`); `c23_check.py` computes the expected counts from the base and the removed rows, and an ASSETS row is never removed. (2) **`serves`** (the CTO's amendment of C-GROUP item 2 @5ba12d1de5, msg 34592): the emitter writes, on every `tool_index` entry that catalog rows of the `opal-data-assets` or `opal-data-bd` buckets name as `read_tool`, a `serves` list: the DISTINCT `{vendor, firm}` pairs of those rows (rows that carry both), sorted by vendor then firm, written after `source_group`; an entry with no such row carries no `serves` key. It is derived, never typed. A fourth criterion `AC4` grades it (`c23.AC4.sh`; the fourth criterion has its reason here: the CTO's amendment). `<paths>` above now also names `emit_catalog_v02.py`. (3) **A step 0 before the original steps**: regrade the `MX-c-21` proof instance. (4) The commit list below replaces section 5 item 3.

Do these IN ORDER and nothing else:
1. Run once: `git sparse-checkout add workflows infra/aws/ec2/opal-gateway org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census`.
2. **Regrade the `MX-c-21` instance** (its AC2 recorded FAIL on the issuer's check defect, row Z-W45-S1, now fixed and ruled): run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/regrade_c21_ac2.py . C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/c21_ac2_evidence.out` (it prints `regraded AC2 FAIL -> PASS; acceptance rows 3`; anything else: stop and report), then `python .tools/proof-of-spec-check.py org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/NFRA_MCPINDEX.TO-MX-c-21.c-group-bucket-on-every-row-and-tool.proof_of_spec.json AC1,AC2,AC3` and require rc=0; COMMIT 1: exactly that one file, first line `proof(NFRA_MCPINDEX.TO-MX-c-21 A1, 0.9.0_WK_NFRA_MCPINDEX~45): AC2 regraded PASS on the issuer's ruling`.
3. Section 1's "What to build" items 1 to 3 and `serves` (item 4 below), then its Steps 1 to 3 (the pytest, the regeneration of the rows and the fork registry with the corrected count 226, the catalog regeneration with `GROUP-MAP unused: 0`).
4. **`serves`**: in `emit_catalog_v02.py`, after the group map is applied and the tool buckets are attached, set `serves` as above on each `tool_index` entry. A NEW test file `workflows/atom_decomposition/tests/test_serves.py` with at least 5 tests (the derivation; sorted distinct pairs; a duplicate pair counted once; no `serves` for a tool no assets or bd row names; a row without vendor ignored; a `bd` row counts).
5. Run the FOUR criteria of section 4 (AC4 is `c23.AC4.sh`), by their literal invocations.
6. Commits through `.tools/safe-commit.sh` (message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL), in this order: COMMIT 1 (step 2); COMMIT 2: `gen_silver_rows.py`, `emit_catalog_v02.py` and the tests; COMMIT 3: the registry file ALONE; COMMIT 4: the 12 new row files, the proof instance and your saved outputs. Never `DATA_CATALOG.yaml`.
7. Report once, with the section 5 item 4 contents plus the AC4 DENOMINATOR line and the `serves` of the `schwab_query` entry.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.
<status>issued</status>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~02:4xZ); MX-c-23 COMPLETE.** Merged at 52a4eb444c. The worker's proof instance read AC1-AC4 FAIL because the emitter cannot run in the sparse worktree (Z-W45-S6); the catalog was regenerated by the issuer at the workspace root (emit_catalog_v02.py, five group maps, 173 of 173 applied, unused 0). Issuer re-run on that catalog: c23.AC1 PASS (136 map entities, labels 13 of 13, 0 inferred), c23.AC2 PASS (12 of 12 new rows; table rows 226 = 216 + 12 - 2), c23.AC3 PASS (1386 pairs, 96 newly visible, cross-firm leaks 0), c23.AC4 PASS (100 entries, serves wrong 0). Rows Z-W45-S6 to S8 ruled by the disarm row Z-S122. The worker's FAIL instance stays as the record of what it measured; this ruling supersedes its verdict on the regenerated catalog. members.yaml and pending_members.yaml (the OG-ap-21 tool, an issuer act) land in the issuer's commit; DATA_CATALOG.yaml (the CloudOps lane's file) is re-emitted once after the RESEARCH cells merge and landed by a re-seated worker at the MX-r-15 A1 cut, as MX-c-20 A1 did. Gate limb that graded this ruling: none (LIMB 6 does not fire on a modification).

<status>complete</status>

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-16 ~09:3xZ) -- RE-OPENED: the order is not met until its catalog is landed.** My ruling above ("COMPLETE") graded the issuer's UNCOMMITTED catalog. This order's criteria AC1-AC4 grade the COMMITTED catalog, and `python .tools/round-close-check.py --project NFRA_MCPINDEX --round 18` reads PROOF-BAD on AC1-AC4 (2.0.0_SA_COO~MI2 msg 34746), so "complete" overstated the state. The status below is set back to issued. The remaining work is exactly the MX-c-20 A1 pattern: the issuer emits the final catalog at the workspace root (`emit_final.sh`, once OG-ap-23 is live at `3d5c9c8bf1` and 2.0.0_SA_COO~MI2's rows are landed), a re-seat of slot ~45 places it (`place_catalog.py`), re-runs AC1-AC4, regrades this order's proof rows (`regrade_c23_instance.py`) and commits the catalog alone. The steps, with the catalog's md5, are amendment A3 at the cut. Gate limb that graded this modification: none (LIMB 6 does not fire on a modification).

<status>issued</status>

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-16 ~09:4xZ) -- RE-SEAT of slot ~45: place the final catalog, regrade this order's proof rows, commit.** OG-ap-23 is live at `3d5c9c8bf1` (ledger closed 09:21:54Z, 27 of 27 tools served); 2.0.0_SA_COO~MI2's rows are landed at `58660556d3`; the issuer emitted the final catalog at the workspace root with `emit_final.sh` (127 tools, 173 of 173 map rows, c23.AC1-AC4 and c21.AC1-AC2 PASS there). The file is `C:/tmp/mi-final/DATA_CATALOG.final.yaml`, md5 `9519ebce3a1b92cee07a5507d1912dd3`, git blob `cf7616c08ec6b50a4676f962546ec6e732772e39`. Your worktree is `C:/tmp/wk-r18-45c`, branch `wk-NFRA_MCPINDEX-45c`, NEW, cut from the merged HEAD (sparse cone already widened). Do these steps IN ORDER and nothing else; run every command from the worktree root:

1. **Place the catalog.** `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/place_catalog.py . C:/tmp/mi-final/DATA_CATALOG.final.yaml 9519ebce3a1b92cee07a5507d1912dd3`. It must print `copied=1 equal=1` (anything else: stop and report). Do NOT regenerate the catalog.
2. **Run the four criteria** of section 4 by their literal invocations, each saved to `.scratch/a3_ev/c23.ACn.out` (create the folder; `{ bash <script>; echo "exit=$?"; } > .scratch/a3_ev/c23.ACn.out 2>&1` does this). Each must read `RESULT: PASS` and end with `exit=0`. If one does not, stop and report its output.
3. **Regrade the proof instance.** `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/regrade_c23_instance.py . .scratch/a3_ev` (it prints `regraded AC1-AC4 FAIL -> PASS; acceptance rows 4`; anything else: stop and report), then `python .tools/proof-of-spec-check.py org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/NFRA_MCPINDEX.TO-MX-c-23.assets-rows-vendor-firm-and-the-twelve-schwab-dim-rows.proof_of_spec.json` and require `VALID (rc=0)`.
4. **Commit in two commits through `.tools/safe-commit.sh`**, author `0.9.0_WK_NFRA_MCPINDEX~45`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL: (i) the regraded proof instance, and the four `.scratch/a3_ev/c23.ACn.out` files copied to `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/a3_evidence/`; (ii) `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` ALONE, started in the BACKGROUND (`... > .scratch/catalog_commit.log 2>&1 &`) and polled with short waits until it prints `committed` or a REFUSE/BLOCKED line (the naming gate takes up to ~10 minutes; give up after 25 and report the log tail). If it REFUSES, report the first 10 REFUSE lines verbatim and stop; do not edit the catalog.
5. **Report once:** the steps' results, the two commit shas, the AC1-AC4 result lines, and `git diff --stat` of commit (ii) against its parent. Do NOT flip the order's status and do NOT push; the issuer does both.

- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`.

<status>issued</status>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~09:47Z) on A3; MX-c-23 COMPLETE.** Worker ~45 (haiku, high) placed the final catalog and committed it in two commits (bc3d492c18 the regraded proof instance and a3_evidence; 701c995e7d the catalog alone); the issuer verified from the commits, not the report: the catalog blob at 701c995e7d is cf7616c08ec6b50a4676f962546ec6e732772e39 (md5 9519ebce3a1b92cee07a5507d1912dd3), six files changed and nothing else. Drained by `safe-merge.sh` at 739786b974. Issuer re-run on the merged tree: c23.AC1-AC4 PASS (136 map entities equal; 12 of 12 new rows, 9 linked; 1,182 pairs, 96 newly visible, cross-firm leaks 0; 127 index entries, serves 7 of 7), c21.AC1-AC2 PASS; `round-close-check` round 18 reads MAY-CLOSE. The pipeline gate then refused the flip on the instance's artifact pins (six entries still PENDING-THIS-COMMIT for files committed earlier); the issuer pinned each to the commit that carried it, pointed the four evidence entries at a3_evidence, and added the catalog itself (701c995e7d). Gate limb that graded this ruling: the flip-needs-a-VALID-instance limb of to-pipeline-gate, VALID after the pins.

<status>complete</status>

**AMENDED A4 (2.0.0_SA_COO~MI, 2026-10-16 ~11:02Z) -- RE-OPENED for the v2 catalog: the landed catalog's depth claims were stale by one source; re-seat slot ~45 to land the re-measured file.** MX-r-15 landed the A3 catalog at 10:38:53Z and its r13.AC3 read depth 9 of 11 on ONE claim (mac.04.yield-curve-fred generated_at: catalog 2026-10-14, served 2026-10-15; the source re-stamps at ~23:01Z, after my 2026-10-15 16:07Z measurement). The issuer re-measured at 2026-10-16T10:58:32Z (`measured.yaml` @2c9cabebe5) and re-emitted with `emit_final.sh` (all six criteria PASS): `C:/tmp/mi-final-v2/DATA_CATALOG.final.yaml`, md5 `983464f80adc45ac51f1f3eebbdf2001`, git blob `4c27b2817148f477e4ddb9b0a6ab0b3054462a76`. Against the landed catalog `cf7616c08e` it differs ONLY in tool_index `history_depth` (11 tools), `freshness` (5 tools) and the built_at stamp: 0 of 280 rows change, the same 127 tools. Your worktree is `C:/tmp/wk-r18-45d`, branch `wk-NFRA_MCPINDEX-45d`, NEW, cut from the merged HEAD. Do these steps IN ORDER and nothing else; run every command from the worktree root:

1. **Place the catalog.** `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/place_catalog.py . C:/tmp/mi-final-v2/DATA_CATALOG.final.yaml 983464f80adc45ac51f1f3eebbdf2001`. It must print `copied=1 equal=1` (anything else: stop and report). Do NOT regenerate the catalog.
2. **Run the four criteria** of section 4 by their literal invocations, each saved to `.scratch/a4_ev/c23.ACn.out` (`mkdir -p .scratch/a4_ev`; `{ bash <script>; echo "exit=$?"; } > .scratch/a4_ev/c23.ACn.out 2>&1`). Each must read `RESULT: PASS` and end with `exit=0`. If one does not, stop and report its output.
3. **Commit the catalog FIRST, alone,** through `.tools/safe-commit.sh` (author `0.9.0_WK_NFRA_MCPINDEX~45`, message file written with the Write tool, last line `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`, `Push state: LOCAL`): `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` ALONE, started in the BACKGROUND (`... > .scratch/catalog_commit.log 2>&1 &`) and polled with short waits until it prints `committed` or a REFUSE/BLOCKED line (the naming gate takes up to ~10 minutes; give up after 25 and report the log tail). Note the printed commit sha (full: `git rev-parse HEAD`). If it REFUSES, report the first 10 REFUSE lines and stop.
4. **Regrade and pin the proof instance, then commit it.** `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/regrade_c23_instance.py . .scratch/a4_ev` (it must print `regraded AC1-AC4 ...`), then `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/pin_c23_instance.py . <the catalog commit sha from step 3, 10 characters>` (it must print `pinned N artifacts; catalog at <sha>`), then `python .tools/proof-of-spec-check.py org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/NFRA_MCPINDEX.TO-MX-c-23.assets-rows-vendor-firm-and-the-twelve-schwab-dim-rows.proof_of_spec.json` and require `VALID (rc=0)`. Copy the four `.scratch/a4_ev/c23.ACn.out` files to `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/a4_evidence/` and commit the instance and those four files in ONE commit through `.tools/safe-commit.sh`.
5. **Report once:** the steps' results, the two commit shas, the four RESULT lines with their DENOMINATOR lines, and `git diff --stat HEAD~1 HEAD` of the catalog commit. Do NOT flip the order's status and do NOT push; the issuer does both.

- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`.

<status>issued</status>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~11:15Z) on A4; MX-c-23 COMPLETE.** Worker ~45 (haiku, high) placed the re-measured catalog and committed it in two commits (cd2eb0e26f the catalog alone; 7b4afda03c the regraded and pinned instance with a4_evidence); the issuer verified from git, not the report: the catalog blob at cd2eb0e26f is 4c27b2817148f477e4ddb9b0a6ab0b3054462a76 (md5 983464f80adc45ac51f1f3eebbdf2001), the catalog commit touches one file, the instance commit the instance and four evidence files, nothing else against the base. Drained by `safe-merge.sh` at 58ae2c5417. Issuer re-run on the merged tree: c23.AC1-AC4 PASS (136 map entities equal; 12 of 12 new rows; 1,182 pairs, 96 newly visible, cross-firm leaks 0; 127 index entries, serves 7 of 7), c21.AC1-AC2 PASS; proof-of-spec-check VALID; `round-close-check` round 18 reads MAY-CLOSE. The catalog differs from the one MX-r-15 landed only in tool_index history_depth (11 tools), freshness (5 tools) and the built_at stamp: 0 of 280 rows change. Gate limb that graded this ruling: the flip-needs-a-VALID-instance limb of to-pipeline-gate, VALID.

<status>complete</status>

**AMENDED A5 (2.0.0_SA_COO~MI, 2026-10-16 ~11:43Z) -- RE-OPENED for the v3 catalog: the daily publish landed before the v2 apply; re-seat slot ~45 to land the catalog re-measured after it.** MX-r-15 v2 landed at 11:30:12Z (deploy-only 1bc2df0b13) and its r13.AC3 read depth 8 of 11 and answer-time 9 of 17: seven portal series (mp.05, mp.06, cor.01, ft.01, ft.02, mac.01, val.02) now serve data_as_of 2026-10-15 against the catalog's 2026-10-14; the daily publish ran between my 10:58Z read and 11:35Z, not at ~13:30Z as the order's note assumed (the note rested on one observation). The issuer re-measured at 2026-10-16T11:38:17Z (`measured.yaml` @ed102403e8) and re-emitted with `emit_final.sh`, which now also runs r13.AC3 against LIVE AWS on the placed candidate: depth 11 of 11, answer-time 17 of 17, anchors 2 of 2, and the six other criteria PASS. `C:/tmp/mi-final-v3/DATA_CATALOG.final.yaml`, md5 `b72408cad06f2fbf8fb851a4be5485d9`, git blob `16250301d6a90c16c4b81867bc00fed6ecd397a1`. Against the v2 catalog `4c27b28171` it differs ONLY in tool_index `history_depth` (11 tools), `freshness` (5 tools) and the built_at stamp: 0 of 280 rows change. Your worktree is `C:/tmp/wk-r18-45e`, branch `wk-NFRA_MCPINDEX-45e`, NEW, cut from the merged HEAD. Do these steps IN ORDER and nothing else; run every command from the worktree root:

1. **Place the catalog.** `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/place_catalog.py . C:/tmp/mi-final-v3/DATA_CATALOG.final.yaml b72408cad06f2fbf8fb851a4be5485d9`. It must print `copied=1 equal=1` (anything else: stop and report). Do NOT regenerate the catalog.
2. **Run the four criteria** of section 4 by their literal invocations, each saved to `.scratch/a5_ev/c23.ACn.out` (`mkdir -p .scratch/a5_ev`; `{ bash <script>; echo "exit=$?"; } > .scratch/a5_ev/c23.ACn.out 2>&1`). Each must read `RESULT: PASS` and end with `exit=0`. If one does not, stop and report its output.
3. **Commit the catalog FIRST, alone,** through `.tools/safe-commit.sh` (author `0.9.0_WK_NFRA_MCPINDEX~45`, message file written with the Write tool, last line `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`, `Push state: LOCAL`): `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` ALONE, started in the BACKGROUND (`... > .scratch/catalog_commit.log 2>&1 &`) and polled with short waits until it prints `committed` or a REFUSE/BLOCKED line (the naming gate takes up to ~10 minutes; give up after 25 and report the log tail). Note the full commit sha (`git rev-parse HEAD`) and that `git rev-parse HEAD:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` prints 16250301d6a90c16c4b81867bc00fed6ecd397a1. If it REFUSES, report the first 10 REFUSE lines and stop.
4. **Regrade and pin the proof instance, then commit it.** `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/regrade_c23_instance.py . .scratch/a5_ev`, then `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/pin_c23_instance.py . <the catalog commit sha from step 3, 10 characters>`, then `python .tools/proof-of-spec-check.py org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/NFRA_MCPINDEX.TO-MX-c-23.assets-rows-vendor-firm-and-the-twelve-schwab-dim-rows.proof_of_spec.json` and require `VALID (rc=0)`. Copy the four `.scratch/a5_ev/c23.ACn.out` files to `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~45/a5_evidence/` and commit the instance and those four files in ONE commit through `.tools/safe-commit.sh`.
5. **Report once:** the steps' results, the two commit shas, the four RESULT lines with their DENOMINATOR lines, and `git diff --stat HEAD~1 HEAD` of both commits. Do NOT flip the order's status and do NOT push; the issuer does both.

- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`.

<status>issued</status>
