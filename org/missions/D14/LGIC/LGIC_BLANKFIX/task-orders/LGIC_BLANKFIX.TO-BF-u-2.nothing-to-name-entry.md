# TO LGIC_BLANKFIX.TO-BF-u-2 -- round 6 BF-u-2: a root-map entry that says a root has nothing to name -- read, counted as mapped, and stopped where the root does name something

<to_id>LGIC_BLANKFIX.TO-BF-u-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-u-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round6.md`) | **outcome_ref:** FWD-7, FWD-9 |
**depends_on:** BF-u-3 merged on this slot (both write the root check); handed by continuing the slot

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

`BF-u-2` (item E1). The CTO: a root that declares nothing to name "is mapped as 'nothing to name' in one entry". Today
`opal_naming_rootmap.load_map` refuses any entry without a non-empty `system`, `scope` and `source`, so no such entry can exist.

**THE SHAPE** is `infra/logic/registry/root_map.json` `_about` (`row_fields`, the paragraph `A ROOT WITH NOTHING TO NAME`), written by `4.0.0_SA_CRO` @35f40f2c02. Read that paragraph whole. Such an entry carries `names: 'none'`, `why` and `evidence`, and
NO `system`, `scope`, `source`, `fills`, `source_dirs` or `exceptions`; `why` is exactly `names_from_caller` or
`attaches_to_names_declared_elsewhere`. Its reader rule: "a root entered as names: 'none' that the check later finds declaring a
graded name is reported, never skipped." The registry holds no such entry yet ("load_map would refuse one until the reader is
built"); your tests write their own.

**Build**, to that shape:
1. `lib/opal_naming_rootmap.py`: `load_map` accepts the entry, and refuses a malformed one with the root and field named, as it
   does for every other field: `names` with any value but `none`; a `why` outside the two values; an empty or missing `evidence`;
   a `names: 'none'` entry carrying any of the six fields it must not carry. `resolve` and every other reader of a map entry handle
   it without a `KeyError`: find every caller of `load_map` and `resolve` under `lib/` and list them in your report.
2. `lib/opal_naming_rootcheck.py`: the `all` command counts such a root as MAPPED and prints it
   `NOTHING-TO-NAME <root> why=<why> names=N` with its name count from the scope. When the scope gives that root one or more names,
   the root is NOT passed: it prints `STOPPED` with the reason "the map says nothing to name and the root names N" and is counted
   under `stopped`. `ok` keeps its present meaning.
3. The DIFFERENCE CONTROL, on a temporary map the tests write: the same entry on a root with no names reads `NOTHING-TO-NAME`; on a
   root with names it reads `STOPPED`; each malformed form of step 1 is refused. Extend both tests.

### ACCEPTANCE

<criterion id="BU2-AC1" cell_refs="BF-u-2"><invocation>python lib/tests/test_opal_naming_rootmap.py</invocation><expect>ROOTMAP-TEST ok=True</expect></criterion>
`BU2-AC1` -- the loader reads the entry and refuses each malformed form.

<criterion id="BU2-AC2" cell_refs="BF-u-2"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BU2-AC2` -- the difference control: nothing-to-name on an empty root, stopped on a root with names.

<criterion id="BU2-AC3" cell_refs="BF-u-2"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>ALL-ROOTS ok=True</expect></criterion>
`BU2-AC3` -- the estate still runs whole with the entries the registry's lane has landed.

<expected_criteria>BU2-AC1,BU2-AC2,BU2-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootmap.py
lib/tests/test_opal_naming_rootmap.py
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md</decomp_doc> (round 6), cell `BF-u-2`.
<owned_cells>BF-u-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BU2-AC1, BU2-AC2, BU2-AC3. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-u-2.nothing-to-name-entry.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BU2-AC1,BU2-AC2,BU2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; every caller of load_map and resolve and what each does with the entry; the NOTHING-TO-NAME and STOPPED lines of the live run; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- an entry that silences a root which does name things (the root is stopped and counted, and the difference control shows it); a malformed entry read as nothing to name (the loader refuses each form); a caller that crashes on the entry (every caller is listed); BLIND: roots whose names live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round5.md @34ba4c1c90, amended @cbdf36254c (the CTO's enrichment list E1 to E6); decomposition round 6. Base dry-run at the cut: BU2-AC1 base PASS as expected (ran: ROOTMAP-TEST ok=True assertions=30; extended by the cell); BU2-AC2 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=194; extended by the cell); BU2-AC3 base PASS as expected (ran: ALL-ROOTS ok=True roots_total=87 mapped=13 ... hole=0; the control that the estate still runs whole).
