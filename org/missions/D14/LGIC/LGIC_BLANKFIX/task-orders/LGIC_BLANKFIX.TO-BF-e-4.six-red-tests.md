# TO LGIC_BLANKFIX.TO-BF-e-4 -- round 2 BF-e-4: the six tests that are red at the base -- each fixed, or named with its reason

<to_id>LGIC_BLANKFIX.TO-BF-e-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** C-CHECK |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** Round 1 built one command: `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline`
prints one line per name of that root, each of kind `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED` or `HOLE`, and exits 1 while any
line is a `HOLE`. Its last run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`: 140 names, 10 right, 101 fix,
6 not asked, 1 pattern, 6 carded, 16 holes. The modules, all under `lib/`: `opal_naming.py` (`grade(name, type) -> (verdict,
canonical)`, `census_repo()`, `census_tf_names()`), `opal_naming_scope.py` (`root_items(root)`), `opal_naming_rootmap.py`
(`load_map`, `resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py` (`word_for`, `cadences`),
`opal_naming_keyfill.py` (`fill_keys`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read the ones your cell touches or
calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new
dependency. The bar for the library's own suite: `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider` fails six
named tests at the base (see `lib/tests/test_opal_naming_fourth_verdict.py` for the list); no test that passes at the base may fail.

### THE CELL

`BF-e-4`. `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider --color=no` fails six tests before this project
wrote anything (row `LGIC_BLANKFIX-S1`): `test_grade_agrees_with_every_worked_case` for the cases `inf-silver-chain|LAMBDA`,
`opal-portal-data-proxy-api|API_GW`, `Inflection-SilverChain-DimConversionFailure|CW_ALARM`, `wsb-49f-model-aua-pull-daily|SCHEDULE`,
`inf/otp-relay/token|SECRET`; and `test_lambda_plane_consumers_is_import_aware_not_a_bare_substring` (asserts 7, reads 8).

For EACH of the six, find the cause by reading: the test, where its expected answer comes from (the worked cases are loaded from
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`; read how the test file loads them), the registry rows that touch
the name (`infra/logic/registry/resources.json`, `systems.json`) with `git log` on those files, and the grader. Then one of:
- **the recorded answer is stale** (the registry or a ruling moved after the case was recorded, and the grader is right): restate
  the case in `lib/tests/test_opal_naming.py` the way the file already restates others at load time, with a one-line comment
  naming the commit or ruling that moved it;
- **the grader is wrong**: fix `lib/opal_naming.py`, minimally;
- **neither can be shown from the repository**: leave the test failing and name it in your report with what is missing.
Do not delete a test, do not weaken an assertion to a tautology, and do not edit `GRADING_RULE.md` or any registry file.

**Build** `lib/tests/test_opal_naming_base_six.py`, a plain script: it runs the suite, and prints one line per one of the six ids
with `PASS` or `FAIL`, then `BASE-SIX ok=True fixed=N still_failing=N other_failing=0 passed=N total=N`; `ok=True` when
`fixed + still_failing == 6`, no test outside the six fails, and `total` is not less than 93.

### ACCEPTANCE

<criterion id="BE4-AC1" cell_refs="BF-e-4"><invocation>python lib/tests/test_opal_naming_base_six.py</invocation><expect>BASE-SIX ok=True</expect></criterion>
`BE4-AC1` -- the six are accounted for one by one, and nothing that passed at the base fails.

<expected_criteria>BE4-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming.py
lib/tests/test_opal_naming_base_six.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-4`.
<owned_cells>BF-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE4-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-e-4.six-red-tests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; for each of the six: the cause, which of the three outcomes, and the commit or ruling cited; any grader line changed; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a red test turned green by weakening it (the face forbids it; the report gives the cause per test and the CTO reads the diff); a grader edit that fixes one case and moves others (other_failing=0 over the whole suite, total printed); a stale answer 'fixed' in the grader instead of restated (the face orders the read of the registry history first); BLIND: worked cases outside this test file.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE4-AC1 base FAIL as expected (file absent).
