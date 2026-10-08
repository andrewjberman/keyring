# TO LGIC_BLANKFIX.TO-BF-v-6 -- round 7 BF-v-6: the repeat check compares names and verdicts, not line numbers -- a moved line no longer reads as a difference

<to_id>LGIC_BLANKFIX.TO-BF-v-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-v-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first. At the round-6 close it read
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0
hole=0 ... stale_hints=0`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round6.txt`. One line per name: `KIND type current -> detail  [where]`, kinds
`RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`. Each unmapped root is printed `UNMAPPED <root> names=N`. The
CTO's reading of round 6 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, on the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND6_L9_GRADE_BU6_BU7_20261008.md` -- read the analysis first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots and their
names, `root_items`), `opal_naming_rootmap.py` (`load_map`, `resolve`), `opal_naming_cadence.py`, `opal_naming_keyfill.py`,
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and `all`
commands). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS
call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed), and
every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move every
day, and the registry's lane may add map entries during this round.

### THE CELL

`BF-v-6` (item E5; row `LGIC_BLANKFIX-S8`, OPEN). `python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py` reads `ok=False` on the trunk:
`FAIL: investor-reporting/ycharts: the saved run differs from the live run` after commit 51f4545acd shifted ycharts line numbers;
the per-root compare matches name lines whole, `[file:line]` included. The CTO: "Compare by name and verdict, not line number."

**Build** in that script (your slot's own deliverable):
1. A name line's identity for the compare is (kind, type, current, file) and its answer is the text after `->`; the line number in
   `[file:line]` is not compared. Within one root, a name that appears several times is compared as a multiset.
2. A name in the live run and absent from the saved one is listed `ADDED-NAME` and is not a difference (other cells of this round
   add names: `BF-v-4` counts names that were invisible, and map entries may land). A saved name absent from the live run is a
   difference; the same name with a different kind or answer is a difference, printed whole both ways. A line kind the saved run
   does not carry at all (`UNCOUNTED`, from `BF-v-4`) is listed and not compared.
3. Every other check and the last line's form stay as they are.

### ACCEPTANCE

<criterion id="BV6-AC1" cell_refs="BF-v-6"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py</invocation><expect>ALL-ROOTS-R5 ok=True</expect></criterion>
`BV6-AC1` -- the repeat holds when lines move, names are added, or a new line kind appears, and still fails when a saved name's answer changes.

<expected_criteria>BV6-AC1</expected_criteria>

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

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md</decomp_doc> (round 7), cell `BF-v-6`.
<owned_cells>BF-v-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BV6-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-v-6.repeat-by-name.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BV6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; every ADDED-NAME and every unlisted kind; a negative control showing a changed answer still fails; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a compare loosened until nothing differs (a removed saved name and a changed answer are still differences, and the report shows a negative control); the saved files rewritten to match the live run (they are not in your grant; the script reads them); BLIND: a name renamed in place reads as one removal and one addition -- a difference, by design.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round6.md @ea45e82c70 (the CTO's enrichment list E1 to E5); decomposition round 7. Base dry-run at the cut: BV6-AC1 base FAIL as expected (ran: FAIL: investor-reporting/ycharts: the saved run differs from the live run; ALL-ROOTS-R5 ok=False ... repeat=identical).
