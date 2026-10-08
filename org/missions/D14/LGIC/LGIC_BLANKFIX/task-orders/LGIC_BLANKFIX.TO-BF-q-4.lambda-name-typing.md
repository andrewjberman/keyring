# TO LGIC_BLANKFIX.TO-BF-q-4 -- round 4 BF-q-4: a name the code uses as a function name is typed as one wherever the reader meets it

<to_id>LGIC_BLANKFIX.TO-BF-q-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-q-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round4.md`) | **outcome_ref:** FWD-1, FWD-2 |
**depends_on:** none

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

`BF-q-4`. Round 3 typed a source literal `LAMBDA` when it is held under a function-name context AND the last-token rule had
already given it some type (a retype only: 2 of 1,966 repository names). Row `LGIC_BLANKFIX-W1-S10`: literals held under a
function-name context that the last-token rule gives NO type are still dropped; about 40 across the repository, one in
`infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py` line 54 (`opal-assets-bd49f-reporting-pull`).
`1.0.0_SA_CTO`: a name the code uses as a function name is typed as one wherever the reader meets it.

**Build** in `lib/opal_naming.py` (the source-literal classifier and what feeds it its context; nothing else):
1. A literal held under a function-name context (as round 3 defined it; read the code and
   `lib/tests/test_opal_naming_function_literal.py`) is typed `LAMBDA` whether or not the last-token rule types it, when it is
   shaped like a resource name (the classifier's own kebab-name test). An ARN, a URL, a file path, an empty string, a name with
   a space, or a literal with a variable part is not typed.
2. Keep the module-level switch; add a second one for this wider rule (default on) so a test can compare the three states.
3. Extend `lib/tests/test_opal_naming_function_literal.py`: on small texts, a function-name literal with no kind token is typed
   `LAMBDA`; the DIFFERENCE CONTROL: the SAME literal under a name that says neither function nor lambda is not typed; an ARN
   and a path under a function-name context are not typed. On the real repository: every item the wider rule ADDS, printed with
   its `where`; each must be type `LAMBDA`; none may be an item that existed before with another type. Last line
   `FNLITERAL-TEST ok=True fees_runner=LAMBDA runner=LAMBDA retyped=2 added=N other_changes=0 items=N`.
4. Grade every added name with `opal_naming.grade(name, "LAMBDA")` and count the ones that RAISE: a name the check now reads and
   cannot place stops a whole-estate run. Print them, and report the count; do not card them and do not edit the registry.
Run `python -m pytest lib/tests -q -p no:cacheprovider`: no test may fail. `bd-pipeline` will read 141 names where it read 140:
report its last line (`python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only`).

### ACCEPTANCE

<criterion id="BQ4-AC1" cell_refs="BF-q-4"><invocation>python lib/tests/test_opal_naming_function_literal.py</invocation><expect>added=</expect></criterion>
`BQ4-AC1` -- every added name is a Lambda held under a function name, and the same literal elsewhere is not typed.

<criterion id="BQ4-AC2" cell_refs="BF-q-4"><invocation>python lib/opal_naming_rootcheck.py lines infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json</invocation><expect>ROOTCHECK-LINES ok=True</expect></criterion>
`BQ4-AC2` -- the thread's own line checks still pass with the added names.

<expected_criteria>BQ4-AC1,BQ4-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Edit only the source-literal classifier and what feeds it its context. `grade()`, `_slots`, `_cadence_slot` and the Terraform reader are not yours.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming_function_literal.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the two saved traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md</decomp_doc> (round 4), cell `BF-q-4`.
<owned_cells>BF-q-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BQ4-AC1, BQ4-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-q-4.lambda-name-typing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BQ4-AC1,BQ4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; every added item with its where; the added names that raise, whole; the bd-pipeline run's last line; the suite's last line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- an ARN, a path or a template typed as a function (the face lists what is not typed; three control cases); names added that the grader cannot place, stopping the whole-estate run (counted and printed; not carded); an existing item's type changed (other_changes=0); BLIND: function names held under a name that says neither function nor lambda.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round3.md @f0e6411e53 (the CTO's enrichment list); decomposition round 4. Base dry-run at the cut: BQ4-AC1 base FAIL as expected (ran: the last line carries no added field); BQ4-AC2 base PASS as expected (ran: ROOTCHECK-LINES ok=True; a control).
