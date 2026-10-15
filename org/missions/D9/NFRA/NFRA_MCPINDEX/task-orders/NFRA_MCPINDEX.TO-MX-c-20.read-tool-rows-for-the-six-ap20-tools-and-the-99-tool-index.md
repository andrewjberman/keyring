# NFRA_MCPINDEX task order -- `MX-c-20` -- R1: the seven catalog rows the six OG-ap-20 tools read name those tools as `read_tool`, and the tool index covers the 99 tools the gateway serves after that release

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-20</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-20</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~44</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the generator, seven rows, one test and the emitted catalog only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs plus nine planted arms are the control (decomposition R17.3b); the release order `MX-r-14` carries the never-widen pair.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-20` (round 17; the CTO's R1: `read_tool` for tools OPLGTW deployed since v0.5)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). NFRA_OPLGTW's `OG-ap-20` is LIVE (release `06cfb6db64`, `EC2_MANIFEST` `deployed_commit`): the gateway now serves 99 tools, six more than the 93 the catalog's tool index covers. Two defects follow if nothing changes: (1) the tool index has no entry for the six, so the host's partition check reads 93 of 99; (2) the seven table rows those tools read still say `read_tool: null, gap_owner: NFRA_OPLGTW`.

**The six tools and the rows each reads at call time** (read from their modules at `06cfb6db64`: `app/etfs_ownership.py`, `app/etfs_funds.py`, `app/portal_mdpf.py`; the issuer authored the map `workflows/atom_decomposition/tool_reads_ap20.json`, key `tools`, and you do NOT edit it):
- `etfs_get_partner_ownership` reads `opal_data_etfs_gold_daily_partner_ownership`;
- `etfs_get_ownership_rollup` reads `opal_data_etfs_platinum_etf_ownership_dashboard`;
- `etfs_get_monthly_report` reads `opal_data_etfs_platinum_monthly_ownership_report`;
- `etfs_get_fund_nav_history` reads `opal_data_etfs_silver_netassets_daily`;
- `etfs_get_fund_holdings` reads `opal_data_etfs_gold_holding`, `opal_data_etfs_gold_book` and `opal_data_etfs_silver_holdings` (`gold_book` keeps its current `etfs_get_positioning`: that is the first deployed proposed tool and it stays);
- `mdpf_get_category_views` reads `opal_data_portal_v2_platinum_mdpf_category_views`.

**Why a generator change.** `workflows/atom_decomposition/gen_silver_rows.py` picks a row's `read_tool` as the first of the contract's proposed tools that is deployed (`read_tool_for`). Run against the 99-tool list it would also name `etfs_get_fund_holdings` and the other new tools on EIGHT rows those tools never read (for example two pathfinder and two trueshares holdings tables). A `read_tool` on a row its tool does not read is a false claim. So the generator gains a restriction.

**What to build.**

1. In `gen_silver_rows.py`: a new optional argument `--tool-reads FILE` (default `tool_reads_ap20.json` beside the generator; an absent DEFAULT file means no restriction; a file named by the argument that does not exist exits 2, as `--g5r` and `--firm-map` do). The file's `tools` maps a tool name to a list of entity names. A tool that is a key of `tools` is a `read_tool` candidate for a contract ONLY when that contract's entity (`entity_of(contract_id)`) is in the tool's list; the generator then takes the next proposed tool that is deployed (or none). A tool that is not a key is unrestricted, exactly as before. `read_tool_for` is the one place that changes. No firm or product name is typed as a literal.
2. A NEW test file `workflows/atom_decomposition/tests/test_tool_reads.py` with at least 6 tests: a restricted tool is skipped for an unlisted entity and the next deployed proposed tool is taken; it is accepted for a listed entity; an unlisted tool is unrestricted; an absent default file changes nothing; a missing named file exits 2; the result is deterministic.
3. `infra/aws/ec2/opal-gateway/tests/test_blackdiamond.py`, test `test_mx_t13_catalog_gated`: since `MX-c-18` the emitted `blackdiamond_fees` catalog row also carries `nl_tags` (filled, 5 tags) and `nl_tags_basis: inferred`, so the assertion `{k: v for k, v in row.items() if k != "entity"} == src` fails (the row has two more items). Change the comparison to ignore exactly those two keys on the row side (`k not in ("entity", "nl_tags", "nl_tags_basis")`), and add one assertion that `row["nl_tags_basis"] == "inferred"` and `row["nl_tags"]` is non-empty. Change nothing else in that file.

### Steps

0. From the worktree root: `python workflows/atom_decomposition/tests/test_gen_silver_rows.py` passes before you start (a control).
1. Make parts 1 to 3. Run `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` (all pass) and, from `infra/aws/ec2/opal-gateway`, `PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_blackdiamond.py` (all pass).
2. Regenerate the rows with the pinned inputs and the 99-tool list (the `...` is the folder `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`; the registry files are NOT passed, they do not change):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 .../G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/deployed_ap20.json --firm-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`
   It must write 216 rows. `git status` must then show EXACTLY these 7 row files modified under `catalog_entries/`: the seven entities named above for the rows that change (`opal_data_etfs_gold_daily_partner_ownership`, `opal_data_etfs_platinum_etf_ownership_dashboard`, `opal_data_etfs_platinum_monthly_ownership_report`, `opal_data_etfs_silver_netassets_daily`, `opal_data_etfs_gold_holding`, `opal_data_etfs_silver_holdings`, `opal_data_portal_v2_platinum_mdpf_category_views`), each changing only `read_tool` (null to the tool), `tools` (`[]` to `[the tool]`) and `gap_owner` (`NFRA_OPLGTW` to null). Any other changed file is a defect to report, not to commit.
3. Regenerate the catalog in your worktree: `python workflows/atom_decomposition/emit_catalog_v02.py --overlay-ref 06cfb6db64` (it must end with HARVEST ROWS, SILVER and a TOOL INDEX line reading `N=99 served tools; a=11 b=76 c=12; sum 99`, and no EMIT REFUSED line). The six tools enter the index from `workflows/atom_decomposition/tool_index/pending_members.yaml` (class b, owner NFRA_OPLGTW), which the issuer already committed.
4. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit `tool_reads_ap20.json`, `pending_members.yaml`, `members.yaml`, `measured.yaml`, `f1_firm_map.json`, `deployed_ap20.json`, the emitter, the checks, the registry files, any other `catalog_entries/` row or any gateway file other than the one test. No tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token); tests under `tests/` are exempt.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round17/checks/r1.AC1.sh`, `r1.AC2.sh`, `r1.AC3.sh` (python `r1_check.py`). Read `r1_check.py` for exactly what is graded. Do not edit them.
5. Your worktree may be a sparse checkout: if `workflows/` or `infra/aws/ec2/opal-gateway/` is missing, run `git sparse-checkout add workflows infra/aws/ec2/opal-gateway` once (that is the only sparse change you may make).
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/tests/
workflows/atom_decomposition/catalog_entries/
infra/aws/ec2/opal-gateway/tests/test_blackdiamond.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~44/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W44-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-20" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/r1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (rows differing from the base 7); the rows naming one of the six tools are exactly the 7 the modules read; every other row equals its base row -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-20" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/r1.AC2.sh; echo "exit=$?"</invocation><expect>PARTITION a=11 b=76 c=12; sum 99 of N=99; definitions located 99 of 99 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-20" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/r1.AC3.sh; echo "exit=$?"</invocation><expect>only the 7 rows differ from the base catalog; nl_tags 304, inferred 44, firm 24 intact; c10_discover exits 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~44/NFRA_MCPINDEX.TO-MX-c-20.read-tool-rows-for-the-six-ap20-tools-and-the-99-tool-index.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The order's expect fields are prose; the checker matches `expect` as a regex against your recorded output, so encode the literal printed tokens, as the previous workers did, and disclose that in a row.)
2. Do NOT flip the order's status (the order file is outside your paths); the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in three commits: (i) the generator, the tests (`tests/` and `test_blackdiamond.py`); (ii) the 7 rows and the proof instance; (iii) `DATA_CATALOG.yaml` ALONE, started in the BACKGROUND (`... > .scratch/catalog_commit.log 2>&1 &`) and polled with short waits until it prints `committed` or a REFUSE/BLOCKED line (the naming gate takes up to ~10 minutes; give up after 25 and report the log tail). If it REFUSES, report the first 10 REFUSE lines and stop; do not edit the catalog.
4. Report once, with: the change by function; the AC1 DENOMINATOR line, the AC2 PARTITION line and the AC3 result lines verbatim; the unit-test counts; the three commit shas.

The issuer then merges, re-runs the criteria, runs the gateway suite by failing-ID delta and prepares the release.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 17, worker ~44, the CTO's R1 (ROUND_ANALYSIS.round12-16.md item R1: `read_tool` updates for the OPLGTW tools deployed since v0.5, "when live"). Cut when `OG-ap-20` went live (COO~O msg 34427): it also unblocks `MX-r-14`, whose host check `r13.AC2` would read 93 of 99 without this cell. The rival-fund tools (`OG-rv-1`, `OG-rv-2`) are not live; their `read_tool` updates stay held for a later recut and release. Live ref for `MX-r-14`: `06cfb6db64` (no separate deploy-only commit). The released tree's MC Portal per-tool link counts are 33 tools / 112 links before this catalog and 39 tools / 119 links with it (measured on the extract of `06cfb6db64`). Base dry-runs 2026-10-15: `r1.AC1` FAIL (no row names a tool), `r1.AC2` FAIL (index 93, six MISSING), `r1.AC3` FAIL (0 rows differ), as expected. Planted arms: `plant_r1.py` 9 of 9 (the good rows and catalog pass all three; the 15 contract-proposed rows with 8 false readers, six of the seven rows, an unrelated row edit, a catalog with no six members and an unrelated catalog edit each fail the criterion that grades them). `c14.AC2` still PASSES (the builder `glib.py` applies the same restriction). The gateway suite showed one failure this cell causes (`test_mx_t13_catalog_gated`, a consequence of `MX-c-18`); part 3 fixes it. `test_schwab_host_inputs::test_grant_writer_stages_the_contract_only_from_the_standard` also fails and is not ours (its staged copy of `NFRA_OPLGTW_CONTRACT.json` differs from the standard at byte 7913; it fails the same way without the catalog change).

<status>issued</status>
<round>17</round>
<workstream>R1</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
