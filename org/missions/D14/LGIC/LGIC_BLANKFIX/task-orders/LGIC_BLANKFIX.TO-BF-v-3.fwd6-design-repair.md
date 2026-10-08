# TO LGIC_BLANKFIX.TO-BF-v-3 -- round 7 BF-v-3: the FWD-6 design repaired -- arm C coherent with step 1, an arm D act that grows the HOLE count, an owner for every HOLE text

<to_id>LGIC_BLANKFIX.TO-BF-v-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-v-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md`) | **outcome_ref:** FWD-6 |
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

`BF-v-3` (item E2). The design `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md` was graded NOT MET as written (`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND6_L9_GRADE_BU6_BU7_20261008.md`, section BU6-AC2; read it
whole). The CTO's three repairs, design only:
1. **Arm C.** The decision rule's step 1 sends a name in an UNMAPPED root to `grade()` alone, so arm C (remove the root's map entry,
   expect `{system}: no map entry for this root` from `place()`) can never print, and neither can the owed table's `no map entry`
   row. State whether step 1 calls `place()` for an unmapped root's HOLE text (refusing only a wrong name), OR re-target arm C to a
   HOLE a mapped root prints (the grade names two: a multi-firm root's missing `fills.system`, or an UNDECIDED key). Make step 1,
   arm C and the owed table agree.
2. **Arm D.** A cron edit on an existing cadence name yields FIX, not HOLE (`decide()` rebuilds on the new word, or returns the
   ruled form), so the count never grows. Replace the act with one that grows the HOLE count; the grade gives one, not run by the
   CVO: a schedule whose name carries no cadence word (`irpt-directory-refresh`, FIX today) given an expression the cadence reader
   cannot decide. Run it on a scratch copy of the root's text in your deliverables folder (never in `infra/`) and record the line
   it prints; if it does not print HOLE, find an act that does and record that instead.
3. **An owner for every HOLE text.** The grade counts 14 distinct HOLE texts printed by `decide()` and its callers in
   `lib/opal_naming_rootcheck.py`, of which the owed table covers 7. Give each an owner, with `1.0.0_SA_CTO` as the default owner
   for a rule defect. Enumerate the texts from the code yourself; the grade's count is a reading, not your denominator.

**Edit** the design in place (git keeps the round-6 text). Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd6_design_round7.py`: it makes every
check `check_fwd6_design.py` makes (leave that file as it is), and it also enumerates the HOLE texts from `lib/opal_naming_rootcheck.py` (every return or print that yields a HOLE verdict or its
`why`), checks each has a row in the owed table naming an owner, and prints
`FWD6-DESIGN ok=True headings=7 paths=N missing=0 hole_texts=N owned=N unowned=0`.

### ACCEPTANCE

<criterion id="BV3-AC1" cell_refs="BF-v-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd6_design_round7.py</invocation><expect>FWD6-DESIGN ok=True .*unowned=0</expect></criterion>
`BV3-AC1` -- the design keeps its seven parts, cites only paths that exist, and every HOLE text in the code has an owner.

<criterion id="BV3-AC2" cell_refs="BF-v-3" judgment="true"/>
`BV3-AC2` (judgment) -- `3.0.0_SA_CVO` reads the repaired design against FWD-6's ACCEPT (PRD lines 67-73) and the three repairs of the round-6 grade: is every exercise arm able to produce its expected value as written, and is every HOLE text owned? You record the artifacts' paths and NO verdict.

<expected_criteria>BV3-AC1,BV3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md</decomp_doc> (round 7), cell `BF-v-3`.
<owned_cells>BF-v-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BV3-AC1, BV3-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-v-3.fwd6-design-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BV3-AC1,BV3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the decision for arm C in one paragraph; arm D's act and the line it printed; the owner table; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a HOLE text left out of the enumeration so the table looks whole (the checker reads the code); arm D asserted to grow the count without running the act (its printed line is recorded); arm C kept contradicting step 1 (the grade's reasoning is the test); BLIND: whether the design can be built in one round -- the CTO's reading.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round6.md @ea45e82c70 (the CTO's enrichment list E1 to E5); decomposition round 7. Base dry-run at the cut: BV3-AC1 base FAIL as expected (file absent; the round-6 checker reads FWD6-DESIGN ok=True headings=7 paths=30 missing=0 and has no owner check).
