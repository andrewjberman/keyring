# NFRA_MCPINDEX task order -- `MX-c-19` -- the `firm` field on the 24 firm-scoped table rows whose registry firm value names one known firm, and the discover rule that shows each such row to its own firm only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-19</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-19</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~43</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant changes; the change is which catalog ROW a firm principal is shown, never which data it may read (client data still needs the firm's own data grant, NFRA_OPLGTW v3.1 Ruling 2). No AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the visibility difference control (`f1.AC2`: every silver row x six principals, old tree against new, cross-firm leaks 0) plus eight planted arms are the control; the release order `MX-r-14` carries the never-widen pair that names this visibility change before anything ships.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-19` (round 17; CTO ruling 2 in `ledger/ROUND_ANALYSIS.round12-16.md`)

Work in your own worktree (cut from `box/sitez`; its portal folder is provisioned because the emitter reads it). Every path below is relative to its root.

**Why.** A firm-scoped catalog row with no `firm` field is refused to EVERY firm principal, including the row's own firm, so those rows serve Opal staff only. 24 table rows (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`, key `rows`: entity name -> `49financial` or `inflection`; the issuer authored it from the registry and the check re-derives each value) have a registry firm value that names exactly one known firm. Those 24 get a `firm` field, so the gateway can show each to its OWN firm's principals and to no other firm. Seeing the row never reads the data.

**What to build, in four parts.**

(a) `workflows/atom_decomposition/gen_silver_rows.py`. The FULL row gains an optional `firm` key, placed after `firm_scope_rule` (add it to the key order the full row is built in; a row not in the map has NO `firm` key at all). A new optional argument `--firm-map FILE` (NO default: absent means no map; a file named by the argument that does not exist exits 2, as `--g5r` does) supplies the value by entity name (`entity_of(contract_id)`). Apply it the way `apply_g5r` is applied, before the sanitise/split. The existing sanitiser then makes the CLEAN row's `firm` null (the value is a firm token, and a clean row may carry none) and `split_row` puts the value in the registry entry's `restore` as `firm`. No firm name is typed as a literal in the generator.

(b) `workflows/atom_decomposition/emit_catalog_v02.py`. A silver TABLE row may carry an OPTIONAL `firm` (not in the required set): in `validate_entry` and `_validate_table_fields`, accept `firm` only on a row that carries `contract`, with a value of null or a non-empty string; a `firm` key on a row without `contract` is an error. `silver_catalog_row` writes `firm` when the loaded row carries it (the joined row carries the restored string), after `firm_scope_rule`'s position as far as the field tuples allow (order is not graded). The loader join (`join_fork_registry`) already restores every `restore` field, so the value reaches the emitted catalog by the registry.

(c) `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, function `_silver_answer`. Replace exactly these three lines

```
    if rule == "firm-scoped" and principal_class != catalog_gate.OPAL_INTERNAL:
        return None                            # no firm field on the row to scope by: no firm principal may see it
    firm = catalog_gate.OPAL_INTERNAL
```

with

```
    row_firm = str(row.get("firm") or "")
    scoped = rule == "firm-scoped" and principal_class != catalog_gate.OPAL_INTERNAL
    if scoped and not (row_firm in catalog_gate.KNOWN_FIRMS and principal_class == "firm" and principal_firm == row_firm):
        return None
    firm = row_firm if scoped else catalog_gate.OPAL_INTERNAL
```

(the file's own text is the truth: read the function first; if the three lines differ from the above, keep the rule, not the text). The rule: a firm-scoped row is shown to a non-internal principal only when the row's `firm` is a known firm AND the principal is a firm principal of that same firm; every other case still returns None; an Opal-internal principal sees every row as before; a row that is not firm-scoped is unchanged. Change nothing else in the gateway.

(d) Tests. A NEW file `infra/aws/ec2/opal-gateway/tests/test_firm_catalog_visibility.py` with at least 6 tests of `_silver_answer` on fixture rows: internal sees a firm-scoped row; the row's own firm sees it; another known firm does not; an unknown firm id does not; an empty firm id does not; a firm-scoped row with NO `firm` field is seen by no firm principal; a row that is not firm-scoped is unchanged. A NEW file `workflows/atom_decomposition/tests/test_firm_field.py` with at least 6 tests (the generator applies the map named by `--firm-map` and the clean row holds null while the registry entry restores the value; an unmapped entity gets no `firm` key; no `--firm-map` argument changes nothing; a missing named map exits 2; the emitter validator accepts null and a string on a table row, refuses a non-string, refuses `firm` on a row without `contract`; the join restores the string). Fix any EXISTING test under `tests/` that pinned the old field set.

### Steps

0. From the worktree root build the deployed-tools file the committed rows were generated under: `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round16/checks/deployed_from_rows.py .scratch/deployed.json` (it prints `deployed tools written: 1`).
1. Make parts (a) to (d). Run `python workflows/atom_decomposition/tests/test_gen_silver_rows.py` and `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` (all pass).
2. Regenerate the rows AND the fork registry with the pinned inputs (the `...` is the folder `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~38/`):
   `python workflows/atom_decomposition/gen_silver_rows.py --g2 .../G2_pinned.md --g4 .../G4_pinned.md --g5 .../G5_pinned.md --g6 .../G6_pinned.md --g3 .../G3_pinned.md --g2f .../G2f_pinned.md --out workflows/atom_decomposition/catalog_entries --deployed-tools .scratch/deployed.json --fork-registry-file infra/logic/registry/catalog_fork_keys.json --firm-map org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/f1_firm_map.json`
   It must write 216 rows. `git status` must then show EXACTLY the 24 mapped row files under `catalog_entries/` modified (each gains `firm: null`, nothing else) and `infra/logic/registry/catalog_fork_keys.json` modified (its `git diff` adds a `firm` value under `restore` of exactly those 24 entries and changes nothing else; `legacy_addresses.json` is NOT passed and must not change). Any other changed file or line is a defect to report, not to commit.
3. Regenerate the catalog in your worktree: `python workflows/atom_decomposition/emit_catalog_v02.py` (it must end with the HARVEST ROWS, SILVER and TOOL INDEX lines and no EMIT REFUSED line). Do NOT commit `DATA_CATALOG.yaml`.
4. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No other `catalog_entries/` row, no `legacy_addresses.json`, no `DATA_CATALOG.yaml` commit, no other gateway file, no portal file, no tool, grant, route, role, `.env` or AWS change. No deploy. No push. Do NOT edit the map file, the checks, the tool index or `catalog_gate.py`.
2. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token); the tests under `tests/` are exempt, but use the gateway's `catalog_gate.KNOWN_FIRMS` values rather than retyping them where you can.
3. `infra/logic/registry/catalog_fork_keys.json` is written by the generator run in step 2, never by hand. A commit that touches it may be refused by a registry gate; if it is, report the refusal text and stop on that file (the issuer rules it).
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `deliverables/2.0.0_SA_COO~MI/round17/checks/f1.AC1.sh`, `f1.AC2.sh`, `f1.AC3.sh` (python `f1_check.py`, `vis_matrix.py`). Read them for exactly what is graded. Do not edit them. The round 14 builder `deliverables/2.0.0_SA_COO~MI/round14/checks/glib.py` already applies the map (`c14.AC2.sh` now expects `firm: null` on the 24; run it as a spot check, it is not a criterion).
6. Another worker (`~42`) edits `emit_catalog_v02.py` in other functions at the same time (the row writers); keep your change to the field tuples, the two validators and `silver_catalog_row`, so the merge is hunk-disjoint.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/gen_silver_rows.py
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/
infra/logic/registry/catalog_fork_keys.json
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_firm_catalog_visibility.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~43/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W43-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-19" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/f1.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR mapped rows 24; rows with a firm field in the new tree 24; 24 of 24 carry their mapped firm and the registry names it -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-19" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/f1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (silver rows x 6 principals = pairs), newly visible 24 (expected 24), cross-firm leaks 0; opal-internal unchanged; the unknown and empty firm see nothing -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-19" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/f1.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_firm_catalog_visibility.py, test_opal_discover.py and test_portal_index.py; new tests collected at least 6 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~43/NFRA_MCPINDEX.TO-MX-c-19.firm-field-on-the-24-prose-firm-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in three commits: (i) the generator, the emitter, the gateway function and the tests; (ii) the 24 rows plus the registry file; (iii) the proof instance. Never `DATA_CATALOG.yaml`.
4. Report once, with:
   - the change by function in each of the four parts;
   - the AC2 DENOMINATOR line verbatim;
   - the `git diff --stat` of step 2, the unit-test counts and your commit shas.

The issuer then merges, regenerates the catalog, runs the gateway suite by failing-ID delta and lands the catalog through the lane that owns the gateway folder.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 17, worker ~43, parallel to `MX-c-18`. Source: `ledger/ROUND_ANALYSIS.round12-16.md` ruling 2 (CTO msg 34404): the cell widens who SEES a catalog row, so it carries its own never-widen pair at `MX-r-14` and is not folded into the tags cell. Scope finding sent to the CTO with this cut: the registry holds 25 prose firm values; 24 name exactly one known firm (23 `49financial`, 1 `inflection`) and are mapped; the 25th (`opal_data_assets_silver_gateway_global_taxsma_workbook`: three firms) stays Opal-internal by design; the other 93 single-clean-value firm-scoped rows also lack the field and are NOT in this cell (widening to them is the CTO's ruling). The registry file is `PLATFORM_LOGIC_DOCS` lane, which refuses this issuer; the worker writes it under this order's `<paths>` (the MX-c-14 A8 precedent), and the CRO `4.0.0_SA_CRO~Z` is told in the issuance record. Live baseline: opal-internal sees all 221 silver rows, every firm principal sees 0 of the firm-scoped. Base dry-runs 2026-10-15: `f1.AC1` FAIL, `f1.AC2` FAIL, `f1.AC3` FAIL (no test file), `c14.AC2` FAIL on exactly the 24 (`missing ['firm']`), as expected. Planted arms: `plant_f1.py` 8 of 8 (a good tree passes ac1 and ac2; five tests only fail ac3; a leak where every firm sees every firm-scoped row fails ac2; a wrong firm on one mapped row fails ac1 and ac2; a firm field on an unmapped row fails ac1 and ac2). Side effect: `c17.AC2` (round 16, closed) counts rows differing from `0f40810fa2` and will read 38, not 14, after this lands; it is not re-run.

<status>issued</status>
<round>17</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-15 ~10:4xZ) -- a RE-SEAT of slot ~43: rows Z-W43-S2/S3 ruled, row Z-S120 fixed, and the final catalog landed.** Your first pass is merged (`73b45f7c7c`): the generator, the emitter, the gateway rule and 24 rows. The issuer re-ran AC1 and AC2 on the merged tree and regenerated the catalog (it differs from the live one by exactly the 44 derived-tag rows of `MX-c-18` and your 24 firm fields, nothing else). Your worktree is a NEW one cut from the merged HEAD. `<paths>` above now also names `tests/test_opal_discover.py` and `DATA_CATALOG.yaml`. Do these steps IN ORDER and nothing else:

1. **Row Z-W43-S2 (ruled).** In `infra/aws/ec2/opal-gateway/tests/test_opal_discover.py`, test `test_gap_need_answers_with_its_owner_and_no_tool`, replace the one line `assert od.discover("cost basis", "firm", "49financial")["matches"] == []     # fail closed: no firm sees a need` with `assert not [m for m in od.discover("cost basis", "firm", "49financial")["matches"] if "need" in m]     # fail closed: no firm sees a NEED (its own mapped catalog row may match)`. Change nothing else in that file.
2. **Row Z-W43-S3 and row Z-S120 (ruled), in `app/integrations/opal_discover/integration.py`.** (a) Update the docstring of `_silver_answer` so it states the current rule (a firm-scoped row is shown to a non-internal principal only when the row's `firm` is a known firm and the principal is a firm principal of that same firm). (b) Add a module function just above `_silver_answer`:
```
def _rule_caveats(row):
    """The caveat lines of a silver row's never_sum_rules (row Z-S120): a list gives its non-blank items; a string gives at most one line and none for the NONE marker; anything else gives none."""
    rules = row.get("never_sum_rules")
    if isinstance(rules, list):
        return [str(r) for r in rules if str(r).strip()]
    if isinstance(rules, str) and rules.strip() and not rules.startswith("NONE"):
        return [rules.strip()]
    return []
```
and in `_silver_answer` replace the one line `"caveats": [str(r) for r in (row.get("never_sum_rules") or []) if str(r).strip()],` with `"caveats": _rule_caveats(row),`. (Before: a string value such as the NONE marker was iterated as a list, one character per caveat.) Change nothing else.
3. **Tests.** Add at least 4 tests to `tests/test_firm_catalog_visibility.py`: `_rule_caveats` on a list (non-blank items kept, blank dropped), on the NONE marker string (empty list), on a non-NONE string (one line), on a missing value (empty); and one `_silver_answer` case showing the NONE marker gives `caveats == []`.
4. **Place the final catalog.** From your worktree root run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/apply_r17_a1.py .` It must print `copied=1 equal=1` (any other output: stop and report). It overwrites `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`; do NOT regenerate it.
5. **Run the criteria** AC1, AC2 and AC3 of section 4 by their literal invocations (AC3 under `timeout 290`), saving the AC3 output (CR stripped) to `.scratch/ac3_a1.out`. As spot checks, not criteria, also run `bash .../round17/checks/t1.AC1.sh`, `t1.AC2.sh`, `t1.AC3.sh` and `.../round14/checks/c14.AC2.sh` and report each result line. All of AC1 to AC3 must PASS.
6. **Regrade the proof instance.** Run `python C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/0c774c5b-0103-40e0-9257-b71087af27bc/scratchpad/regrade_f1_ac3.py . .scratch/ac3_a1.out` (it prints `regraded AC3 FAIL -> PASS; acceptance rows 3`; anything else: stop and report), then `python .tools/proof-of-spec-check.py <your instance path>` and require rc=0.
7. **Commit in three commits through `.tools/safe-commit.sh`**, message files written with the Write tool, each ending with a `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` line and stating push state LOCAL: (i) `integration.py`, `test_opal_discover.py`, `test_firm_catalog_visibility.py`; (ii) the proof instance (and any output files you saved under your deliverables folder); (iii) `DATA_CATALOG.yaml` alone. Commit (iii) takes up to ~10 minutes in the naming gate: start it in the BACKGROUND (`... > .scratch/catalog_commit.log 2>&1 &`) and poll the log with short waits until it prints `committed` or a REFUSE/BLOCKED line (give up after 25 minutes and report the log tail). If it REFUSES, report the first 10 REFUSE lines verbatim and stop; do not edit the catalog.
8. **Report once:** the steps' results, the three commit shas, the AC1 to AC3 result lines, the spot-check lines, and `git diff --stat` of commit (iii) against its parent. Do NOT flip the order's status; the issuer does.

- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it. Row Z-W43-S1 (13 names) and S4 (prose expect against a regex) are ruled correct, no change.
<status>issued</status>
