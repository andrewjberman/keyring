# TO LGIC_BLANKFIX.TO-BF-u-1 -- round 6 BF-u-1: the 74 unmapped roots sorted -- the entry the registry's lane needs for each, nothing-to-name ones in the registry's shape

<to_id>LGIC_BLANKFIX.TO-BF-u-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-u-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round6.md`) | **outcome_ref:** FWD-7, FWD-2 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first. At the round-5 close it read
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0
hole=0`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round5_second_seat.txt`. One line per name: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`,
`NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`. Each unmapped root is printed `UNMAPPED <root> names=N`. The CTO's reading is
`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots and their
names), `opal_naming_rootmap.py` (`load_map`, `resolve`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and
`all` commands). The registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `name_rulings.json`,
`event_rules.json`, `legacy_addresses.json`, `resources.json`, `systems.json`); only `4.0.0_SA_CRO` writes it. Read the modules
your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code
and output; no new dependency; no AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider`
passes whole at the base (194 passed), and every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base EXCEPT
`test_opal_naming_keyfill.py`, which is red (row `LGIC_BLANKFIX-S7`; cell `BF-u-4` repairs it). None may newly fail after your
build. A test you write asserts relations and the rows it needs by name, never a typed total of repository names, roots or
registry rows: those move every day, and the registry's lane is adding map entries during this round.

### THE CELL

`BF-u-1` (item E1). 74 of 87 Terraform roots are not in the root map, so the check prints no line for any name they declare. The CTO:
"Sort the 74 by whether they declare any stored name (a root with no bucket, key, table or rule is mapped as 'nothing to name' in one
entry), then map those that do, the largest first. Each new entry is one line of the root map." The map is written only by
`4.0.0_SA_CRO`; your cell gives that seat what it needs to write the entries. You build nothing in `lib/`.

**The shape of a nothing-to-name entry is decided:** `infra/logic/registry/root_map.json` `_about` (`row_fields`, the paragraph `A ROOT WITH NOTHING TO NAME`), written by `4.0.0_SA_CRO` @35f40f2c02. Read that paragraph whole before step 3. In short: `names:
'none'`, `why` (exactly `names_from_caller` or `attaches_to_names_declared_elsewhere`) and `evidence`, and none of the other fields.
The registry's owner adds: "names=0 alone never justifies names: 'none'" -- `nfra-agentbus` reads `names=0` and declares IAM roles
named from `local.role_a_name`; the zero is the census not following locals.

1. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/sort_unmapped_roots.py`. It takes the unmapped roots from the check's own `all` command (run it; do not
   keep a second list of roots), and for each root reads its names from `opal_naming_scope` (the same enumeration the `all`
   command counts) and counts them by type. It puts each root in ONE class, by a rule you write down in the script:
   `names-zero` (the scope gives the root no name at all), `no-stored-name` (it has names, none of them a bucket, a stored-file
   key, a table or a rule), `to-map` (anything else). `names-zero` is the census's reading, not a verdict: step 3 decides each.
   `no-stored-name` is named so it is counted and shown, never folded into another class: say in your report what its names are,
   by type.
2. It prints one line per root (class, root, names by type), a table of class counts, and saves both as
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/UNMAPPED_ROOTS_round6.txt`.
3. Write, for the registry's lane, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/MAP_ENTRIES_FOR_RULING_round6.md`: one section per unmapped root, headed
   `### <root>`, the `to-map` and `no-stored-name` roots first, largest first by name count, then the `names-zero` roots.
   - A `to-map` or `no-stored-name` section gives what a map entry needs -- `system` (a `systems.json` key), `scope` (a scope
     `scopes.json` knows), `source` (a `systems.json` key) -- and for EACH field either the value the root's own files decide, with
     the file and line that decide it, or `UNDECIDED` and what was read that does not decide it. Read the existing entries in
     `infra/logic/registry/root_map.json` and their `evidence` sentences for how a value is decided; read the root's `.tf` files and the Lambda
     source folders it deploys. A value is never taken from a folder's name alone. List also the names a default would place
     wrongly (candidate exceptions), each with its evidence.
   - A `names-zero` section reads the root's `.tf` files and gives ONE verdict line, `verdict: none/names_from_caller`,
     `verdict: none/attaches_to_names_declared_elsewhere`, `verdict: DECLARES-NAMES` or `verdict: UNDECIDED`, with the evidence
     the shape asks for (which `.tf` files were read, the line quoted). `DECLARES-NAMES` is a root that declares a named resource
     the census does not count (a name built in `locals`, or through a module the census does not follow): quote the declaring
     line and draft its ordinary entry as above.
   One table at the top gives each root's class and verdict.
4. If any root reads `DECLARES-NAMES`, file ONE surprise row for the class (the scope enumeration misses names declared that way),
   listing the roots and one declaring line each.
5. The script's last line: `UNMAPPED-SORTED ok=True roots_total=N mapped=N unmapped=N names_zero=N no_stored_name=N to_map=N
   sections=N declares_names=N`; `ok=True` when the three classes sum to `unmapped`, `mapped + unmapped == roots_total` as the live
   `all` command prints them, and `sections` (the `### ` headings in the ruling file) equals `unmapped`. `declares_names` counts
   the `verdict: DECLARES-NAMES` lines in the ruling file.

### ACCEPTANCE

<criterion id="BU1-AC1" cell_refs="BF-u-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/sort_unmapped_roots.py</invocation><expect>UNMAPPED-SORTED ok=True</expect></criterion>
`BU1-AC1` -- every unmapped root is in one class, the count is the live run's, and every unmapped root has its section.

<expected_criteria>BU1-AC1</expected_criteria>

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

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md</decomp_doc> (round 6), cell `BF-u-1`.
<owned_cells>BF-u-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BU1-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-u-1.sort-unmapped-roots.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BU1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the class table; the no-stored-name roots and their names by type; every names-zero verdict; the ten largest to-map roots with each field decided or UNDECIDED; the ruling file's path; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a field filled from a folder's spelling so no UNDECIDED appears (each value names the file and line that decide it); a names-zero root entered as none on its zero alone (each verdict quotes a .tf line); a root dropped so the classes sum (the classes are counted against the live unmapped count); a second list of roots that drifts from the check's (the face forbids it); BLIND: names that live only in AWS -- the repository plane.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round5.md @34ba4c1c90, amended @cbdf36254c (the CTO's enrichment list E1 to E6); decomposition round 6. Base dry-run at the cut: BU1-AC1 base FAIL as expected (file absent).
