# TO LGIC_BLANKFIX.TO-BF-s-9 -- round 5 BF-s-9: the exercise -- every mapped root run live, no hole on any

<to_id>LGIC_BLANKFIX.TO-BF-s-9</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-9` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2, FWD-9 |
**depends_on:** every other order of the round merged; handed by continuation

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

`BF-s-9`. After the eight cells are merged, run every mapped root and save it. You build nothing in `lib/`.

1. Run `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json` from the worktree root; save its whole output as
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_ROOTS_round5.txt`, and each root's own run under `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round5/`.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py`: it re-runs the command, compares the last line with the saved
   one, and checks: `hole=0` and `stopped=0`; `mapped + unmapped == roots_total`; each root's counts sum to its `items`; on each
   root's saved run no `FIX` line carries a brace other than `{scope}` on a line that names a per-firm fill, and no two different
   current names of one type share a `FIX` target. Last line
   `ALL-ROOTS-R5 ok=True mapped=N unmapped=N items=N hole=0 stopped=0 repeat=identical`.
If any root still prints a `HOLE`, do NOT force it: report each whole, by class, and why it remains; `BS9-AC1` then fails as
written and that is a correct outcome of this order.

### ACCEPTANCE

<criterion id="BS9-AC1" cell_refs="BF-s-9"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py</invocation><expect>ALL-ROOTS-R5 ok=True</expect></criterion>
`BS9-AC1` -- the saved run is the live run, every mapped root completed, and none prints a hole.

<criterion id="BS9-AC2" cell_refs="BF-s-9" judgment="true"/>
`BS9-AC2` (judgment) -- `3.0.0_SA_CVO` runs every mapped root LIVE and reads each to the end: no hole on any, and every line can be acted on from the line alone. You record the artifacts' paths and NO verdict.

<expected_criteria>BS9-AC1,BS9-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-9`.
<owned_cells>BF-s-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS9-AC1, BS9-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-s-9.exercise-every-mapped-root.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS9-AC1,BS9-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the saved files' paths; the per-root table; every line of every root that is not `RIGHT`, `FIX` or `PATTERN`, counted by kind and root; every hole whole; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a saved table graded in place of the live run (the check re-runs and compares); zero holes on 13 roots read as the estate (the last line carries unmapped; the judgment criterion is the outcome); BLIND: the roots the map does not cover.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS9-AC1 base FAIL as expected (file absent).
