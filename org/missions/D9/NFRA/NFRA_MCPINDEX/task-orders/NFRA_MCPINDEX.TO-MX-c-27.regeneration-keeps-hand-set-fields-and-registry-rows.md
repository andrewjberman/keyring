# NFRA_MCPINDEX task order -- `MX-c-27` -- a regeneration by `gen_silver_rows.py` loses no hand-set field and no registry row it does not own

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-27</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-27</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~50</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change; the generator and its checks run in temp folders and read repo files and git objects.
comp-adversary: DECLARED-NOT-APPLICABLE -- the checks regenerate into temp folders against the tracked state and require zero difference; a planted `address` is the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-27` (round 20, R20-1 of the round-19 analysis, BLOCKING before any catalog regeneration)

Work in your own worktree (cut from `box/sitez`; its sparse cone already holds `workflows`, `lib`, `.tools`, `infra/aws/ec2`, `infra/logic` and the project folder; you may add nothing else). Every path is relative to its root. The file you change is `workflows/atom_decomposition/gen_silver_rows.py`.

**Why.** `gen_silver_rows.py` writes one catalog entry per CRO contract into `--out` (default the repo's `workflows/atom_decomposition/catalog_entries/`) and, when given `--registry-file` and `--fork-registry-file`, rewrites `infra/logic/registry/legacy_addresses.json` (its `catalog-*` rows) and `catalog_fork_keys.json`. The issuer MEASURED what a regeneration does to the tracked state today (a dry run into temp folders, the exact inputs of `deliverables/2.0.0_SA_COO~MI2/round18/land_links.sh`, both registry flags pointed at temp COPIES): (a) it rewrites the `prefix` of the eight entries `opal_data_assets_silver_49financial_<t>_silver_legacy` (`<t>` = allocations, assets, fees, prices, realized, transactions_enriched, transactions, unrealized) from the real frozen-copy prefix `blackdiamond/49financial/silver_legacy/<t>/` back to `silver/<t>/`, and the `open_items` of `opal_data_etfs_gold_book` back to the version that still carries a stale line: two hand corrections lost; (b) it replaces the fork registry: 34 of 226 rows lost, and the `restore.bucket` of 8 contracts back to `opal-data-bd` (which makes the catalog emitter REFUSE: "group map bucket would move the row's valid S3 bucket"); (c) a hand-set `address` on a generated entry is dropped. The four `blackdiamond_live_<t>` entries are hand-kept and the generator never writes them: leave that so. A regeneration must be a fixed point on the tracked state.

**What to build** (all in `gen_silver_rows.py`, plus the two new files named below):

1. **`workflows/atom_decomposition/hand_overlay.json`** (NEW, ASCII JSON, indent 1): `{"_about": "<one sentence: hand-set values a regeneration must keep, applied last; maintained by the project issuer>", "entries": {"<entity>": {"<field>": <value>, ...}}, "fork_registry": {"<contract id>": {"restore": {...}, "key_template": "..."}}}`. Fill it by READING the tracked repo files (never type a value): `entries` holds, for each of the eight legacy entities, `{"prefix": <the tracked entry's prefix>}`, and for `opal_data_etfs_gold_book` `{"open_items": <the tracked entry's open_items list>}`; `fork_registry` holds, for the eight legacy contract ids (read each from the tracked entry's `contract.id`), the tracked row of `catalog_fork_keys.json` (`restore` and `key_template`, byte-equal).
2. **The overlay is applied by default.** New option `--hand-overlay FILE`, default `hand_overlay.json` beside the script when it exists. After the generator builds an entry and before it writes it, every field of `entries[<entity>]` is set on it. An overlay entity that is not generated in this run is ignored without error.
3. **Carry-over of keys the generator does not own.** When `<out>/<name>.yaml` already exists and holds a top-level key that the generator did not produce for ANY entry of this run (the owned key set is the union of the keys it produced), that key and its value are kept on the new entry. A hand-set `address` on a generated entry survives; a key the generator owns is still overwritten (except by the overlay).
4. **The fork registry is merged, not replaced.** When `--fork-registry-file` names an existing file: read it; keep every existing row byte-equal and in order; rewrite only the rows of contracts this run generates; then apply `fork_registry` overrides of the overlay to those rows; keep every other top-level key of the file (`_about`, `entities`, `labels`) as it is (a name the run produces for `entities` that the file lacks is appended, existing order first). A file that does not exist is created as today. The legacy-address file keeps its current behaviour (it already keeps every row whose key does not start with `catalog-`).
5. **Tests**: a NEW file `workflows/atom_decomposition/tests/test_regen_preserves.py` with at least 6 tests on small inline fixtures (temp folders): the overlay is applied to a generated entry; an overlay entity that is not generated is ignored; a hand-set `address` on an existing entry file survives a regeneration; a key the generator owns is overwritten; the fork registry keeps rows it does not own byte-equal and in order; its other top-level keys stay; the overlay's fork override wins over the generated row.

### Steps

0. Control (must pass before you start): `cd workflows/atom_decomposition && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_gen_silver_rows.py tests/test_read_links.py tests/test_read_links_repeat.py`.
1. Create `hand_overlay.json` from the tracked files; make the generator changes; write the tests. Run the control line again with `tests/test_regen_preserves.py` added (all pass).
2. Run the three criteria in section 4 (each runs the generator into TEMP folders; `c27.AC1` and `c27.AC2` take under 30 seconds each).

## 2. BOUNDS

1. You change only the files in `<paths>`. NEVER run the generator with `--out` or a registry flag pointing into the repo's `catalog_entries/` or `infra/logic/registry/`; the checks and your own trials use temp folders (copy the two registry files first). No catalog row, no entry file, no registry file, no `DATA_CATALOG.yaml`, no emitter change. No deploy. No push.
2. A value in `hand_overlay.json` is read from a tracked file, never typed from memory.
3. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a new hand-kept token): the overlay file holds data; the code does not name entities.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one. Run `python .tools/naming-gate.py --diff <your diff> --enforce --staged-paths <file>` on each commit before you make it where the commit adds a `.json` or `.py` literal; it must exit 0.
5. The checks are `deliverables/2.0.0_SA_COO~MI/round20/checks/c27.AC1.sh`, `c27.AC2.sh`, `c27.AC3.sh` (python `c27_check.py`). Read them for exactly what is graded. Do not edit them.
6. Another worker (`~51`) edits the catalog emitter and one test file at the same time (no shared file).
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/hand_overlay.json
workflows/atom_decomposition/tests/test_regen_preserves.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~50/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W50-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-27" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/checks/c27.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR regenerated entries 192; differing from the tracked entry 0 (none); planted address on opal_data_assets_silver_49financial_allocations_silver_legacy: kept after a second regeneration True; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-27" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/checks/c27.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR fork registry rows tracked 226; after regeneration 226; lost 0; changed 0; missing or changed after regeneration 0; the CRO alias rows among them 4; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-27" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/checks/c27.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_regen_preserves.py, test_gen_silver_rows.py, test_read_links.py and test_read_links_repeat.py; the new file holds at least 6 tests -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~50/NFRA_MCPINDEX.TO-MX-c-27.regeneration-keeps-hand-set-fields-and-registry-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where counts may differ, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) `gen_silver_rows.py`, `hand_overlay.json` and the test file; (ii) the proof instance.
4. Report once, with: the change by function; the AC1 to AC3 DENOMINATOR and CHECK lines verbatim; the overlay's entity and contract counts; the test count; the two commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 20, worker ~50, an independent chain. Source: CTO round-19 analysis @9b905362bc (R20-1 BLOCKING; the premise "a regeneration drops `address`" is narrowed by the measurement above: the four live entries are hand-kept and untouched; what is lost is the two hand corrections on generated entries and the registry rows). The base dry-run was run in a SPARSE worktree cut like the worker's: `c27.AC1` FAIL (9 differ; the planted address lost), `c27.AC2` FAIL (34 lost, 8 changed; 0 legacy-address rows lost; the CRO's four `*-alias` rows present), `c27.AC3` FAIL (no test file). The lesson of round 19 applies at the drain: the issuer runs a trial emit and the enforcing naming gate before the flip.


**A1 (2.0.0_SA_COO~MI, 2026-10-16 ~19:5xZ), ruling on rows Z-W50-S2 to S5.** Your design works (overlay in the tree: AC1 0 of 192 differ, AC2 0 lost 0 changed); two collisions were the order's. **S2** (the enforcing naming gate refuses the overlay as a new `workflows/` file, 40 firm-token carriers): the overlay is DATA the issuer maintains, not code; the gate grades 0 lines of it at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/hand_overlay.json` (measured by the issuer: `--enforce` exit 0, 0 REFUSE). **S3** (an overlay in the tree by default breaks `tests/test_gen_silver_rows.py::test_every_clean_row_is_carrier_free`, because the overlay puts the tokened legacy prefixes into the generated entries): `--hand-overlay` has NO default; with no option the generator applies nothing and that test is unchanged. **Do:** (1) move your overlay to the path above (same content, read from tracked files as before; `<paths>` now names it and no longer names `workflows/atom_decomposition/hand_overlay.json`); (2) change the option: `--hand-overlay FILE`, no default, no overlay when it is absent; (3) `c27_check.py` (committed on your branch) now passes `--hand-overlay` with that path in every regeneration; (4) your tests that need an overlay write one in a temp folder and pass it; (5) re-run AC1 to AC3 (all three must PASS), update the instance, commit in two commits (generator and tests; the overlay file + instance), report once. **S4** (the `catalog-*` rows of `legacy_addresses.json` are not a fixed point, 36 of 143 dropped): observation, accepted; the generator owns those rows, and the issuer's landing procedure never passes `--registry-file` (it passes only the entries folder). **S5** (`--labels-from` still replaces the labels when named): accepted; an explicit option. The overwrite of the MX-c-30 `session_log.json` you restored byte-equal: noted, thank you. Gate limb that graded this amendment: none (a modification).

<status>issued</status>
<round>20</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
