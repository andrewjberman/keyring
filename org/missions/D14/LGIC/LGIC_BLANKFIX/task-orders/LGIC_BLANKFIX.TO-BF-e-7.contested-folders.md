# TO LGIC_BLANKFIX.TO-BF-e-7 -- round 2 BF-e-7: folders tied to two roots -- each read once, under the root the short list names

<to_id>LGIC_BLANKFIX.TO-BF-e-7</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~7</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-7` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-2, FWD-7, FWD-9 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** Round 1 built one command: `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline`
prints one line per name of that root, each of kind `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED` or `HOLE`, and exits 1 while any
line is a `HOLE`. Its last run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`: 140 names, 10 right, 101 fix,
6 not asked, 1 pattern, 6 carded, 16 holes. The modules, all under `lib/`: `opal_naming.py` (`grade(name, type) -> (verdict,
canonical)`, `census_repo()`, `census_tf_names()`), `opal_naming_scope.py` (`root_items(root)`), `opal_naming_rootmap.py`
(`load_map`, `resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py` (`word_for`, `cadences`),
`opal_naming_keyfill.py` (`fill_keys`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read the ones your cell touches or
calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new
dependency. The bar for the library's own suite: `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider` fails six
named tests at the base (see `lib/tests/test_opal_naming_fourth_verdict.py` for the list); no test that passes at the base may fail.

### THE CELL

`BF-e-7`. `python lib/opal_naming_scope.py table` reads 1,962 repository names and leaves 119 unassigned; 51 of them are in source
folders that two or more Terraform roots point at (row `LGIC_BLANKFIX-W1-S1`: 12 such folders, among them
`infra/aws/lambda/investor-reporting`, claimed by 12 sibling roots, and `infra/aws/lambda/cot-pipeline`, claimed by `cot-pipeline`
and `opal-assets`). Today a contested folder is assigned to no root. The rule the CTO set: each such folder is read ONCE, under
the root the short list names for it. The short list is the root map, `infra/logic/registry/root_map.json`, which another lane
writes (`4.0.0_SA_CRO`); you build the reader and propose the entries.

**Build** in `lib/opal_naming_scope.py`:
1. An optional map argument: `root_items(root, map_path=None)`, `root_table(map_path=None)` and the three commands take
   `--map PATH`. A root's map entry may carry `"source_dirs": ["<repo-relative folder>", ...]`. A contested folder that exactly
   one root's entry lists is assigned to that root and to no other; one that two entries list raises `ValueError` naming both;
   one that no entry lists stays unassigned exactly as today. With no map the behaviour is unchanged, byte for byte in the
   three commands' output.
2. `python lib/opal_naming_scope.py contested [--map PATH]`: one line per contested folder with the roots that claim it, the
   evidence per root, its item count and the root it is assigned to (or `UNASSIGNED`); last line
   `SCOPE-CONTESTED ok=True folders=N items=N assigned=N unassigned=N`.

**Write the proposal** `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~7/ROOT_MAP_SOURCE_DIRS_PROPOSED.json`: a
copy of the landed map with one NEW thing only: `source_dirs` on the entry of the root you can show owns each contested folder
(add a root entry with `system`, `scope`, `source`, `evidence` only where the repository decides all three; otherwise list the
folder in your report as undecided, with what is missing). The owner of a folder is the root whose `.tf` declares the Lambda
functions built from it; where several sibling roots each declare some functions of one folder, say so and do not pick.

**Extend** `lib/tests/test_opal_naming_scope.py`: on a small map it writes to a temporary folder: the DIFFERENCE CONTROL: one real
contested folder is unassigned with no map and assigned to the listed root with the map, and the table's
`assigned + unassigned` still equals the item total in both runs; a folder listed by two entries raises. Keep the existing
assertions. Last line unchanged in shape: `SCOPE-TEST ok=True assertions=N`.

### ACCEPTANCE

<criterion id="BE7-AC1" cell_refs="BF-e-7"><invocation>python lib/tests/test_opal_naming_scope.py</invocation><expect>SCOPE-TEST ok=True</expect></criterion>
`BE7-AC1` -- a listed folder is read once under its root, and the denominator still sums.

<criterion id="BE7-AC2" cell_refs="BF-e-7"><invocation>python lib/opal_naming_scope.py contested</invocation><expect>SCOPE-CONTESTED ok=True</expect></criterion>
`BE7-AC2` -- every contested folder of the real repository is listed with its claimants and evidence.

<expected_criteria>BE7-AC1,BE7-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W7-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_scope.py
lib/tests/test_opal_naming_scope.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-7`.
<owned_cells>BF-e-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE7-AC1, BE7-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~7/LGIC_BLANKFIX.TO-BF-e-7.contested-folders.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE7-AC1,BE7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole and `SCOPE-TABLE` with and without the proposal; the 12 folders with claimants and the proposed owner or UNDECIDED; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a folder read twice under two roots so its names are double-counted (assigned + unassigned == total in both arms); an owner picked for a folder several roots share functions of (the face says do not pick; listed undecided); behaviour changed for callers that pass no map (stated byte-identical; round 1's assertions kept); BLIND: a Lambda whose source is tied to a root only at deploy time.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE7-AC1 base PASS at the base (the round-1 test; it must still pass after the build, with the new assertions); BE7-AC2 base FAIL as expected (ran at the cut: no such command).
