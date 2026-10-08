# TO LGIC_BLANKFIX.TO-BF-u-4 -- round 6 BF-u-4: the key reader's red test -- the real-file case finds its file by what it declares, not by a typed path

<to_id>LGIC_BLANKFIX.TO-BF-u-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-u-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round6.md`) | **outcome_ref:** the pipeline's own gate |
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

`BF-u-4` (item E3; row `LGIC_BLANKFIX-S7`). `python lib/tests/test_opal_naming_keyfill.py` prints `KEYFILL-TEST ok=False cases=86`
on the trunk: the case at line 464 types `investor-reporting/export/backfill_covered_account_ids.py`, and IRPT_BCKEND moved that file
to `investor-reporting/export/tools/` (commit 8d66fb03da). The case is about the reader, not the path.

**Build** in `lib/tests/test_opal_naming_keyfill.py` only: the real-file case finds its file by what it declares -- the source file
under `infra/aws/lambda/investor-reporting/export/` whose text holds the key literal the case asserts on (`firms/`) and whose base
name the case names -- and fails with a clear message if none or more than one file matches. Then look at every OTHER case of this
test that types a repository path: list each in your report and say whether it would break on a move the same way; repair those in
the same manner only where the repair keeps the case's assertion unchanged. No reader code changes.

### ACCEPTANCE

<criterion id="BU4-AC1" cell_refs="BF-u-4"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BU4-AC1` -- the key reader's test passes on the trunk with no typed path to the moved file.

<expected_criteria>BU4-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/tests/test_opal_naming_keyfill.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md</decomp_doc> (round 6), cell `BF-u-4`.
<owned_cells>BF-u-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BU4-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-u-4.red-keyfill-test.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BU4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; each case that types a path, and what you did with it; the diff stat; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- an assertion loosened so the case passes (the face keeps every assertion unchanged); the path simply retyped to the new home (the face asks for a lookup by what the file declares); BLIND: tests in other files that type paths.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round5.md @34ba4c1c90, amended @cbdf36254c (the CTO's enrichment list E1 to E6); decomposition round 6. Base dry-run at the cut: BU4-AC1 base FAIL as expected (ran: KEYFILL-TEST ok=False cases=86).
