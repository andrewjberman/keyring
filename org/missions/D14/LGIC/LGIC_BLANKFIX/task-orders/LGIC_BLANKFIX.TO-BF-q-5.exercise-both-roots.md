# TO LGIC_BLANKFIX.TO-BF-q-5 -- round 4 BF-q-5: the exercise -- both roots live, every line acted on from the line alone

<to_id>LGIC_BLANKFIX.TO-BF-q-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-q-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round4.md`) | **outcome_ref:** FWD-1, FWD-2, FWD-3 |
**depends_on:** BF-q-1, BF-q-2, BF-q-3, BF-q-4 merged; handed by continuation

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Round 3's runs are saved: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round3_bd-pipeline.txt` (140 names: 114 fix, 12 not
asked, 9 right, 3 pattern, 2 refused, 0 holes) and `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/SECOND_ROOT_TRACE_round3_investor-reporting-directory.txt`
(17 names: 13 right, 2 fix, 2 holes). The CTO's reading of both is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the source-literal classifier), `opal_naming_scope.py`,
`opal_naming_rootmap.py`, `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`; it reads
`infra/logic/registry/key_rulings.json`). The registry is `infra/logic/registry/`; the root map is `infra/logic/registry/root_map.json`.
Read the modules your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only;
ASCII only in code and output; no new dependency; no AWS call and no network call. The bar for the library:
`python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed); no test may fail after your build.

### THE CELL

`BF-q-5`. After the four cells of this round are merged, run both roots and save them. You build nothing in `lib/`.

1. Run `python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only` and
   `python lib/opal_naming_rootcheck.py infra/aws/terraform/investor-reporting/directory --map infra/logic/registry/root_map.json --report-only` from the worktree
   root. Save each whole output: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/THREAD_TRACE_round4_bd-pipeline.txt` and
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/SECOND_ROOT_TRACE_round4.txt`.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_traces_round4.py`: it re-runs both commands, compares each with its saved file line
   for line, and checks on each live output: `hole=0` and `refused=0`; the counts sum to `items`; `items` equals
   `len(opal_naming_scope.root_items(root, map)[0])`; no `FIX` line contains `{`; every `NOT-ASKED` line contains "rename";
   no two different current names of one type share a `FIX` target. One line per root, then
   `TRACES-R4 ok=True roots=2 items=N hole=0 refused=0 differs=0`; `ok=False` on any failure, each named on its own line above.
If either root still prints a `HOLE` or a `REFUSED` line, do NOT force it: report each whole and why it remains; `BQ5-AC1` then
fails as written and that is a correct outcome of this order.

### ACCEPTANCE

<criterion id="BQ5-AC1" cell_refs="BF-q-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_traces_round4.py</invocation><expect>TRACES-R4 ok=True</expect></criterion>
`BQ5-AC1` -- both saved traces are the live runs, and neither has a hole, a refused line, a shared target or a bare not-asked line.

<criterion id="BQ5-AC2" cell_refs="BF-q-5" judgment="true"/>
`BQ5-AC2` (judgment) -- `3.0.0_SA_CVO`, a seat that built none of the check, runs both roots LIVE, reads each to the end, and can act on 140 of 140 and 17 of 17 lines (or each root's count at that run) from the line alone, without asking anyone. You record the artifacts' paths and NO verdict.

<expected_criteria>BQ5-AC1,BQ5-AC2</expected_criteria>

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

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the two saved traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md</decomp_doc> (round 4), cell `BF-q-5`.
<owned_cells>BF-q-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BQ5-AC1, BQ5-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-q-5.exercise-both-roots.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BQ5-AC1,BQ5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; both traces' paths; the count per kind on each root; every line that is not `RIGHT`, `FIX` or `PATTERN`, whole; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the state you start from, and one rule of your check corrected

The four cells are merged. Measured by the issuer on the trunk at hand time:
- `bd-pipeline`: `items=142 right=9 fix=118 not_asked=12 pattern=3 carded=0 refused=0 hole=0`. It reads 142 names, not 140: two
  Lambda function names the code uses are now read (`opal-assets-bd49f-reporting-pull`, `bd-price-update`).
- `investor-reporting/directory`: `items=18 right=13 fix=5 not_asked=0 pattern=0 carded=0 refused=0 hole=0`. 18 names, not 17.
Re-measure both; they are the issuer's numbers, not yours.

**Step 2's rule "no `FIX` line contains `{`" is corrected.** Two `FIX` lines of the second root now carry `{scope}` on purpose:
their stored file's bucket is chosen per firm at run time, so the registry's correct address marks the firm's place
(`irpt/{scope}/platinum/directory/`), and the line says the place is filled per firm from the variable it names. Your check
admits exactly the brace `{scope}`, and only on a `FIX` line that names that per-firm fill; any other brace on any `FIX` line
fails the check, and so does `{scope}` on a line that does not name the per-firm fill. Print how many lines were admitted this
way (`per_firm=N` on each root's line). Everything else in step 2 stands.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a saved example graded in place of the live run (the check re-runs and diffs); zero holes read as the outcome (the judgment criterion is the outcome; AC1 is its floor); BLIND: names of either root that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round3.md @f0e6411e53 (the CTO's enrichment list); decomposition round 4. Base dry-run at the cut: BQ5-AC1 base FAIL as expected (file absent).
