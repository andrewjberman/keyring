# NFRA_MCPINDEX task order -- `MX-c-31` -- the row generator's `--read-links`: 27 RESEARCH rows get the one tool that reads them, each link live only when its tool is deployed; the 6 whose tool is live today are linked now

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round18-RESEARCH.md</decomp_doc>
<owned_cells>MX-c-31</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-31</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~56</issued_to>
<issued_by>2.0.0_SA_COO~MI2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the generator, one test file and six regenerated row files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (all three criteria FAIL at the base) and the difference control inside `c31.AC1` and `c31.AC2` (no other row's read_tool moves; 13 links agree with another seat's independent classification) are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-31` (round 18, workstream RESEARCH; PRD v0.17: a live `read_tool` on every in-scope row)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The silver table rows in `workflows/atom_decomposition/catalog_entries/` are written by `workflows/atom_decomposition/gen_silver_rows.py` from pinned inputs. A row's `read_tool` is the first tool its contract PROPOSES that is in the deployed-tools list the generator is given (`read_tool_for`). For 27 rows the contract proposes no tool that reads them, so the row says `read_tool: null, gap_owner: NFRA_OPLGTW` although the gateway has, or has just built, the tool that reads it. Six of the 27 are read by tools the gateway serves TODAY.

**What to build.**

(a) **`--read-links FILE` in `gen_silver_rows.py`.**
   - New optional argument. There is NO default: absent means no links. A file named by the argument that does not exist exits 2, exactly as `--tool-reads`, `--firm-map` and `--scope-exclusions` do. The file the issuer has already committed is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/read_links.json` (`{"_about": "...", "links": {"<entity>": "<tool>", ...}}`, 27 links); you do NOT edit it. (It lives under `org/` because the commit-time naming gate refuses tool names such as `etfs_get_peer_group` in a file under `workflows/`.)
   - **The rule (AMENDED 2026-10-16 by the issuer: a link WINS over a contract proposal).** If the contract's entity (`entity_of(contract_id)`) is in `links` AND the linked tool is in the deployed-tools list, the row's `read_tool` is that tool, its `tools` is `[tool]` and its `gap_owner` is null, whatever `read_tool_for` found (the three fields `build_full` derives from `read_tool`; make `build_full` derive them from the linked value so the three stay consistent). Reason: the contract of `opal_data_etfs_gold_canonical_shape` proposes `etfs_who_holds`, which resolves identifiers through `security_universe` (OG-rv-1 `test_ogrv1_ac03`); the tool that reads canonical_shape is `etfs_get_rival_fund_holdings` (`test_ogrv1_ac02`), so a proposal-first rule linked the wrong tool once both are deployed. A link whose tool is not deployed does nothing (the row keeps what `read_tool_for` found), and an entity not in `links` is untouched.
   - Print one line at the end: `read-links applied: N of M` (N rows linked by this file, M links in the file).
   - Keep your change to the new argument, one small loader and the one place `read_tool` is decided, so it merges hunk-disjoint with other edits of this generator. No tool or entity name is typed as a literal in code.

(b) **Tests.** A NEW file `workflows/atom_decomposition/tests/test_read_links.py` with at least 6 tests: a link whose tool is deployed sets `read_tool`, `tools` and `gap_owner` together; a link whose tool is NOT deployed changes nothing; a row whose contract proposes a deployed tool takes the linked tool instead when the link's tool is deployed, and keeps the proposed tool when the link's tool is not deployed (AMENDED); an entity not in the links is untouched; no argument changes nothing; a missing named file exits 2; the printed `read-links applied` count equals the rows linked.

**INHERITED STATE (re-seat, 2026-10-16).** Your branch `wk-NFRA_MCPINDEX-56` (worktree `C:/tmp/mi2-wk56`) already holds two commits from the first seat: `b6912db1dd` (generator `--read-links`, tests) and `fdf950da08` (the six live-now rows). They implement the OLD rule (a row that has a `read_tool` keeps it). The rule above is AMENDED: change `read_tool_with_links` (and its tests) so a deployed link WINS; do not redo the rest. With the amended rule the six rows and `c31.AC1` are unchanged.

### Steps

0. From the worktree root, `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` passes before you start (a control). If `workflows/` is missing, run `git sparse-checkout add workflows` once (the only sparse change you may make, plus -- AMENDED -- `git sparse-checkout add org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~109 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~110`, which `c31.AC2` reads for the 13-link agreement; without them that arm reads `0 of 0`).
1. Make parts (a) and (b). Rerun the same pytest command (all pass).
2. Regenerate the rows with the pinned inputs and the list of the 99 tools the gateway serves today (the `...` is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`; the registry files are NOT passed, they do not change):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 .../G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/deployed_r18.json --firm-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`
   It must write 214 rows and print `read-links applied: 6 of 27`. `git status` must then show EXACTLY these six row files modified under `catalog_entries/`, each changing only `read_tool` (null to the tool), `tools` (`[]` to `[the tool]`) and `gap_owner` (`NFRA_OPLGTW` to null): `opal_data_portal_v2_platinum_etfs_positioning_data`, `opal_data_portal_v2_platinum_mdpf_account_distribution`, `opal_data_portal_v2_platinum_mdpf_aggregate_aua_timeseries`, `opal_data_portal_v2_platinum_mdpf_aum_metrics`, `opal_data_portal_v2_served_model_portfolio_benchmarks`, `opal_data_portal_v2_served_sentiment_singletons`. Any other changed file or line is a defect to report, not to commit.
3. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `read_links.json` (in the issuer's deliverables folder), `deployed_r18.json`, `deployed_future.json`, the checks, any other `catalog_entries/` row, the emitter, a registry file, any gateway file or the catalog; do NOT commit `DATA_CATALOG.yaml`. No tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. Other seats edit `gen_silver_rows.py` in this round (an `--unskip` argument, a labels argument, `--scope-exclusions`): they are merged already or touch other functions; rebase nothing, keep your hunks small.
3. No tool or firm name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept token); tests under `tests/` are exempt.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c31.AC1.sh`, `c31.AC2.sh`, `c31.AC3.sh` (python `c31_check.py`). Read `c31_check.py` for exactly what is graded. Do not edit them.
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~56/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W56-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI2`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-31" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c31.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (table rows 304; rows differing from the base 6); exactly the 6 live-now rows differ, each carrying its tool, tools == [tool] and gap_owner null, differing only in those three fields -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-31" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c31.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (links 27; both generator runs rc 0); all 27 links take effect with the future list, no other row's read_tool changes, with today's 99 tools the committed rows are already right, the 13 COVERED/BUILT links agree with OPLGTW's classification -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-31" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/c31.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_read_links.py; at least 6 tests passed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~56/NFRA_MCPINDEX.TO-MX-c-31.read-links-for-27-research-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the generator, tests and rows first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in three commits: (i) the generator and the tests; (ii) the six regenerated row files; (iii) the proof instance (and the status flip). Never `DATA_CATALOG.yaml`.
4. Report once, with: the change by part; the `git status` of step 2; the AC1 and AC2 DENOMINATOR lines verbatim; the unit-test count; your commit shas.

The issuer then merges; at the batch code release the issuer regenerates with the extended deployed list (the 21 later links take effect) and re-lands the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI2).** Round 18, workstream RESEARCH-LINKS (a scope of the RESEARCH workstream: the pipeline gate keys one issuance per (workstream, round) and the first issuance holds RESEARCH, the way `MX-c-20` carried workstream R1 in round 17), worker ~56. This is the held `MX-c-31`/`MX-c-32` of decomposition R18-RES.2, MERGED INTO ONE CELL and cut now: NFRA_OPLGTW's classification files (OG-gp-1 worker ~109, OG-gf-1 worker ~110) show that of the 47 etfs and portal-v2/mdpf rows OPLGTW targets, 6 are read by tools live TODAY (COVERED), 7 by tools built and merged but not yet released (BUILT), and 34 are DEFERRED with no tool planned; the 14 rival-fund rows are the tools of OG-rv-1/rv-2, also unreleased. The generator's own proposal path already gives 13 of the 27 links once the tools are in the deployed list (measured with a trial run: it links none of the 6 live ones), so an explicit entity-to-tool file is needed for the rest; where the two agree the file changes nothing. A link takes effect only when its tool is in the deployed-tools list, so the 21 later links stay inert until the issuer regenerates with the list that includes the released tools: no hold on the cell is needed. Mapping sources: the two classification files (13 rows) and the OG-rv-1/rv-2 tool definitions (14 rival rows: peer_group_map to `etfs_get_peer_group`, canonical_shape to `etfs_get_rival_fund_holdings`, security_universe to `etfs_who_holds`, security_market/corporate_actions/security_names to `etfs_get_security_reference`, input_census/holdings_coverage to `etfs_get_coverage`, trade_schedule to `etfs_get_fund_trades`, flow_reconciliation to `etfs_get_fund_flows`, buying_trend/holding_contribution to `etfs_compare_peers`, research_hypotheses to `etfs_get_research_notes`, the platinum page to `etfs_get_rival_page_status`). Base dry-runs 2026-10-16 at 6321876e2e: `c31.AC1` FAIL as expected (0 of the 6 rows differ), `c31.AC2` FAIL as expected (the generator refuses `--read-links`, rc 2), `c31.AC3` FAIL as expected (test file absent). The PASS arms grade the real tree (a fresh generator run), so no planted arm; the independent oracle is the 13-link agreement with OPLGTW's classification. NOT in this cell: the 34 DEFERRED rows and the 9 DynamoDB/news rows (no tool planned; a CTO ruling on the finish line is asked separately). Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>18</round>
<workstream>RESEARCH-LINKS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
