# TO LGIC_BLANKFIX.TO-BF-e-1 -- round 2 BF-e-1: one cadence reader -- the new words, and no finished name that the schedule contradicts

<to_id>LGIC_BLANKFIX.TO-BF-e-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-1, FWD-4 |
**depends_on:** the ratified cadence vocabulary record (4.0.0_SA_CRO proposes, 1.0.0_SA_CTO ratifies); handed by AMENDMENT 1

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

`BF-e-1`. Two defects of the round-1 run. (a) Eight schedules and event rules of the root print `HOLE` because the cadence
vocabulary has no word for their period: weekday-only crons, a Monday-to-Saturday cron, `rate(15 minutes)`, and a rule with an
event pattern and no schedule. (b) Two rules that fire Monday to Friday (`bd-49f-fees-runner-daily`, `bd-49f-fees-session-daily`)
print a finished `FIX` ending `-daily`, because `grade()` takes the cadence word from the current NAME and never reads the
schedule. The fix path and the cadence reader must be ONE reader.

**THE WORDS.** The new cadence words, and the rule for a rule with no schedule, are a vocabulary decision made outside this order.
They are written into this order as AMENDMENT 1 before it is handed to you, with the path of the ratified record. If this order
reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_cadence.py`:
1. `word_for(expression)` returns the ratified word for each period AMENDMENT 1 names, by the same exact-period rule as today.
2. `carried_word(name, type) -> word or None`: the cadence word the current name already carries (use the grader's own reading:
   `opal_naming._cadence_slot`).
3. `verdict_for(row) -> dict` for one `cadences(root)` row: `{"word": the word the SCHEDULE gives or None, "carried": the word the
   name carries or None, "agrees": True/False/None}`; `agrees` is `None` when either is missing.
4. `python lib/opal_naming_cadence.py root ROOT` keeps its last line and adds `contradicted=N` (rows whose carried word differs
   from the schedule's word). Add `python lib/opal_naming_cadence.py contradicted ROOT`: one line per contradicted row, last line
   `CADENCE-CONTRADICTED ok=True root=... rows=N contradicted=N`.

**Extend** `lib/tests/test_opal_naming_cadence.py`: each new word from its expression; the DIFFERENCE CONTROL: a name carrying
`daily` on `cron(30 22 ? * MON-FRI *)` reads `agrees=False`, and the same name on `cron(30 22 * * ? *)` reads `agrees=True`. Keep
the existing cases; change an existing `None` case only where AMENDMENT 1 gives that period a word. Last line unchanged in shape:
`CADENCE-TEST ok=True cases=N`.

You do not edit `lib/opal_naming_rootcheck.py`: cell `BF-e-8` wires `verdict_for` into the run. If AMENDMENT 1 names a schema file
in your grant, the vocabulary edit there is yours and is exactly the rows the record names.

### ACCEPTANCE

<criterion id="BE1-AC1" cell_refs="BF-e-1"><invocation>python lib/tests/test_opal_naming_cadence.py</invocation><expect>CADENCE-TEST ok=True</expect></criterion>
`BE1-AC1` -- the new words come from their expressions, and a carried word the schedule contradicts is seen (the difference control).

<criterion id="BE1-AC2" cell_refs="BF-e-1"><invocation>python lib/opal_naming_cadence.py contradicted infra/aws/terraform/bd-pipeline</invocation><expect>CADENCE-CONTRADICTED ok=True</expect></criterion>
`BE1-AC2` -- the root's contradicted rows are listed on the real `.tf` files.

<expected_criteria>BE1-AC1,BE1-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-1`.
<owned_cells>BF-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE1-AC1, BE1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-e-1.cadence-one-reader.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE1-AC1,BE1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines and the `CADENCE-ROOT` and `CADENCE-ESTATE` lines whole; every row of the root still undecided, with its basis; every contradicted row; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a word invented by the worker when the record is silent on a period (the face forbids it: such a row stays undecided and is listed); a weekday schedule still printed as daily because the name says so (AC1's difference control, AC2's list); BLIND: a schedule whose live expression differs from its .tf text.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE1-AC1 base PASS at the base (the round-1 test; it must still pass after the build, with the new cases); BE1-AC2 base FAIL as expected (no such command, rc 2).
