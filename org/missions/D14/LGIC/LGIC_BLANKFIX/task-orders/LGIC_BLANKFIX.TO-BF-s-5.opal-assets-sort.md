# TO LGIC_BLANKFIX.TO-BF-s-5 -- round 5 BF-s-5: opal-assets' 20 holes, read whole and sorted into classes

<to_id>LGIC_BLANKFIX.TO-BF-s-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none (runs first; the four class cells take its sort)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Two roots read with no hole and were graded by a seat that built none of the check (`bd-pipeline`, 142
names; `investor-reporting/directory`, 18). The run over all 13 roots the root map covers reads 412 names and 38 holes on 9
roots: the table is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_MAPPED_ROOTS_round4.txt` and each root's whole output is under
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round4/`. The CTO's reading is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`), `opal_naming_scope.py`, `opal_naming_rootmap.py`,
`opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`, the `crossfirm` command),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`, the `lines` and `keys` commands). The
registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `event_rules.json`, `legacy_addresses.json`,
`resources.json`, `systems.json`); the map is `infra/logic/registry/root_map.json`. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no
AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed)
and every `lib/tests/test_opal_naming_*.py` script prints `ok=True`; none may fail after your build. A test you write asserts
relations and the rows it needs by name, never a typed total of repository names or registry rows: those move every day.

### THE CELL

`BF-s-5`. `opal-assets` prints 20 of the 38 holes and nobody has read them whole. The CTO sorted the 17 lines it read into four
classes: (S1) skipped by a card that names nothing; (S2) a source-owned bucket on a multi-firm root; (S3) an event-fired rule
with no ruled token; (S4) a first word no vocabulary holds. You read ALL 38 and sort them; you build nothing in `lib/`.

Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/sort_holes.py`: it runs `opal_naming_rootcheck.check_root` over every root of the map
(report-only, output captured), takes every `HOLE` line, and assigns each ONE class by a rule on the line's own text and type
that you write down in the script (a table of class -> the test), with a fifth value `NEW` for a line no rule takes. A `NEW`
line is printed whole and is a finding: name what it is. It prints one line per hole (root, class, the line) and a table of
class by root, and saves both as `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/HOLES_SORTED_round5.txt`. Last line
`HOLES-SORTED ok=True roots=N holes=N carded=N source_bucket=N event_rule=N unknown_word=N new=N`; `ok=True` when the five counts
sum to `holes` and `holes` equals the sum of the roots' own `hole=` counts.

Then, for the registry's lane, write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/HOLES_FOR_RULING_round5.md`: one table per class, one row per
DISTINCT name to rule (type, name, root, where, the bucket where the check read one, and what the line says is missing), with the
count of lines each name closes. It states facts and asks; it proposes no name.

### ACCEPTANCE

<criterion id="BS5-AC1" cell_refs="BF-s-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/sort_holes.py</invocation><expect>HOLES-SORTED ok=True</expect></criterion>
`BS5-AC1` -- every hole of every mapped root is in exactly one class or named as new, and the count is the runs' own.

<expected_criteria>BS5-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-5`.
<owned_cells>BF-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-s-5.opal-assets-sort.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the class-by-root table; every `NEW` line whole and what it is; the ruling file's path and its row count per class; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a hole forced into a class it does not fit so no NEW appears (each class is a written test on the line; NEW is a counted value); a count carried from the saved table instead of a live run (the script runs the roots; holes == the runs' own sum); BLIND: holes on roots the map does not cover.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS5-AC1 base FAIL as expected (file absent).
