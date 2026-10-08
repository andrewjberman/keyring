# TO LGIC_BLANKFIX.TO-BF-u-5 -- round 6 BF-u-5: the repeat check compares the mapped roots' lines only -- an unmapped root's growth no longer reads as a difference

<to_id>LGIC_BLANKFIX.TO-BF-u-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-u-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round6.md`) | **outcome_ref:** FWD-9 |
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

`BF-u-5` (item E4; row `LGIC_BLANKFIX-S8`). `python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py` reads `repeat=DIFFERS` on the trunk:
it compares the whole live output with `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_ROOTS_round5.txt`, and one line differs --
`UNMAPPED infra/aws/terraform/nfra-ctlpln-identity names=10` against `names=11`, a name another project added to a root the map does
not cover. The mapped totals are identical.

**Build** in that script (your slot's own deliverable from round 5):
1. The repeat compares, root by root, the section of each MAPPED root in the saved file with the same root's section in the live
   run: its `ROOTCHECK` line, its `COMPLETED`/`STOPPED` line and its name lines. `UNMAPPED` lines are not compared.
2. A root mapped in the live run and absent from the saved file is listed `ADDED <root>` and not compared; a saved mapped root
   absent from the live run is a difference. The registry's lane is adding map entries during this round, so both can happen.
3. The `ALL-ROOTS` last lines are compared field by field over the fields BOTH lines carry; a field only one line carries is
   listed and is not a difference (cell `BF-u-3` adds one, `stale_hints`). A root printed `NOTHING-TO-NAME` (cell `BF-u-2`) is
   mapped: compare its line when both runs carry it.
4. `repeat=identical` when no compared section or field differs; else `repeat=DIFFERS` and each difference printed whole. The last
   line keeps its present form and every other check the script makes now.

### ACCEPTANCE

<criterion id="BU5-AC1" cell_refs="BF-u-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py</invocation><expect>ALL-ROOTS-R5 ok=True</expect></criterion>
`BU5-AC1` -- the repeat holds over the mapped roots while the unmapped ones grow.

<expected_criteria>BU5-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md</decomp_doc> (round 6), cell `BF-u-5`.
<owned_cells>BF-u-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BU5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-u-5.repeat-mapped-lines.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BU5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; every ADDED root and every field only one line carries; what the compare was and is; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a compare loosened until nothing differs (mapped sections and shared fields are still compared, and a missing saved root is a difference); the saved file rewritten to match the live run (it is not in your grant to change; the script reads it); BLIND: a change inside a mapped root made by a registry edit -- it is a real difference and must print.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round5.md @34ba4c1c90, amended @cbdf36254c (the CTO's enrichment list E1 to E6); decomposition round 6. Base dry-run at the cut: BU5-AC1 base FAIL as expected (ran: ALL-ROOTS-R5 ok=False mapped=13 unmapped=74 items=412 hole=0 stopped=0 repeat=DIFFERS).
