# TO LGIC_BLANKFIX.TO-BF-r-5 -- round 3 BF-r-5: the exercise again -- the root run live, 140 of 140 lines acted on from the line alone

<to_id>LGIC_BLANKFIX.TO-BF-r-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-r-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round3.md`) | **outcome_ref:** FWD-1, FWD-3 |
**depends_on:** BF-r-1 and BF-r-2 merged, and the registry acts their holes name landed; handed by AMENDMENT 1

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline` prints one line per name of
that root: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it
exits 1 while any line is a `HOLE`. Round 2's run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`: 140 names,
9 right, 113 fix, 9 not asked, 1 pattern, 6 carded, 2 refused, 0 holes. A seat that built none of it read that run and could act on
122 of the 140 lines from the line alone; its grade, with the 18 lines it could not act on, is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md` -- read it first. The modules are under `lib/`:
`opal_naming.py` (`grade`), `opal_naming_scope.py` (`root_items`, `root_table`, `contested`), `opal_naming_rootmap.py` (`load_map`,
`resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py` (`policy_roles`, `system_for`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read
the ones your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency. The bar for the library: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at
the base (194 passed); no test may fail after your build.

### THE CELL

`BF-r-5`. After `BF-r-1` and `BF-r-2` are merged and the registry's lane has landed what their holes name, run the thread and
save it. You build nothing in `lib/`.

1. Run `python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only` from the worktree root. Save the whole output to
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/THREAD_TRACE_round3_bd-pipeline.txt`.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_trace_round3.py`: it runs the same command
   again, compares its output with the saved file line for line, and checks on the live output: `hole=0`; the seven counts sum to
   `items`; no `FIX` line contains `{`; every `NOT-ASKED` line contains "rename"; no two different current names of one type share
   a `FIX` target. Last line `TRACE-R3 ok=True items=N hole=0 differs=0`; `ok=False` on any failure, each named on its own line
   above.
If `hole` is not 0, do NOT force it: report every `HOLE` line whole and why it remains; `BR5-AC1` then fails as written and that
is a correct outcome of this order.

### ACCEPTANCE

<criterion id="BR5-AC1" cell_refs="BF-r-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_trace_round3.py</invocation><expect>TRACE-R3 ok=True</expect></criterion>
`BR5-AC1` -- the saved trace is the live run, and the live run has no hole, no shared target and no bare not-asked line.

<criterion id="BR5-AC2" cell_refs="BF-r-5" judgment="true"/>
`BR5-AC2` (judgment) -- `3.0.0_SA_CVO`, a seat that built none of the check, runs the root LIVE, reads it to the end, and can act on 140 of 140 lines from the line alone, telling a wrong name apart from one not asked for a system. You record the artifact's path and NO verdict.

<expected_criteria>BR5-AC1,BR5-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- The judgment criterion gets its artifact path and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md</decomp_doc> (round 3), cell `BF-r-5`.
<owned_cells>BF-r-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BR5-AC1, BR5-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-r-5.exercise-again.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BR5-AC1,BR5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the trace's path; the count per kind; every line that is not `RIGHT`, `FIX` or `PATTERN`, whole; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a saved example graded in place of the live run (the check re-runs and diffs; FWD-1 says a saved example fails); zero holes read as the outcome (the judgment criterion BR5-AC2 is the outcome; AC1 is its floor); BLIND: names of the root that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @ef7133ec9a (the CTO's enrichment list); decomposition round 3. Base dry-run at the cut: BR5-AC1 base FAIL as expected (file absent).
