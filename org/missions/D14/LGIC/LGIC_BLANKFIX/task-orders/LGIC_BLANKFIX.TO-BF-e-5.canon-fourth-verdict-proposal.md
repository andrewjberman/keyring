# TO LGIC_BLANKFIX.TO-BF-e-5 -- round 2 BF-e-5: the canon section and the worked case carry the fourth verdict -- a patch proposed to the registry's lane

<to_id>LGIC_BLANKFIX.TO-BF-e-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~5</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-3 |
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

`BF-e-5`. Round 1 added the verdict `NO-SYSTEM-ASKED`. Two documents outside this project's write surface do not carry it (rows
`LGIC_BLANKFIX-W2-S2`, `W2-S3`): `infra/logic/render_naming_section.py` (about line 324) renders the `ALIAS` and `OUT-OF-PATTERN`
sentences from `org/standards/NAMING_SCHEMA.json` and not the new one, so the generated NAMING section of
`infra/logic/02_DOCTRINE.md` will not state it; and `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` records the
worked case `pandas-pyarrow-layer|LAMBDA_LAYER` with its old answer. Both files belong to another lane (`4.0.0_SA_CRO`). You
PROPOSE the change and prove it on copies; you edit neither file.

**Build**, all in your deliverables folder `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/`:
1. `canon_fourth_verdict.patch`: a unified diff (`git diff` format, repo-relative paths) that makes the renderer emit the fourth
   verdict's sentence from the schema, and restates the one worked case in `GRADING_RULE.md`. Smallest change that does it.
2. `check_canon_patch.py`: copies the two files and whatever the renderer needs into a temporary folder, applies the patch there
   with `git apply`, runs the patched renderer the way its own `__main__` or documented entry does, and checks: the rendered
   section contains `NO-SYSTEM-ASKED` and its schema sentence; the DIFFERENCE CONTROL: the UNPATCHED renderer's output does not
   contain it; `git apply --check` of the patch against the repository's HEAD files succeeds. Last line
   `CANON-PATCH ok=True applies=True rendered_has_verdict=True unpatched_has_verdict=False`.
3. `PROPOSAL_CANON_FOURTH_VERDICT.md`: one page for the owning lane: what the patch changes, the check's last line, and what
   regenerating `02_DOCTRINE.md` will move (run the unpatched and patched renderer on copies and give the diff's line count).

### ACCEPTANCE

<criterion id="BE5-AC1" cell_refs="BF-e-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_canon_patch.py</invocation><expect>CANON-PATCH ok=True</expect></criterion>
`BE5-AC1` -- the patch applies to HEAD and is what makes the sentence appear (the unpatched arm does not show it).

<criterion id="BE5-AC2" cell_refs="BF-e-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_grading_rule.py</invocation><expect>GRADING-RULE ok=True</expect></criterion>
`BE5-AC2` (AMENDMENT 1) -- the worked-case file itself carries the fourth verdict's case and the ratified cadence rules, and the library's suite, which loads its cases from that file, still passes whole.

<expected_criteria>BE5-AC1,BE5-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-5`.
<owned_cells>BF-e-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE5-AC1, BE5-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/LGIC_BLANKFIX.TO-BF-e-5.canon-fourth-verdict-proposal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE5-AC1,BE5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the patch's diff stat; the proposal's path; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- REOPENED on a ruling: you now WRITE the worked-case file

The order was complete and merged (`BE5-AC1` stands; do not redo it). `1.0.0_SA_CTO` ruled (msg 106331) that the writer of
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` for this project is this cell's worker, because the registry's lane
is refused on that file. The file is now in your grant. The renderer half of your patch is already landed by its own lane
(`infra/logic/render_naming_section.py`, commit eb29bf7f37); do not touch it.

**Build:**
1. In `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`, the worked case `pandas-pyarrow-layer|LAMBDA_LAYER` restated as
   `NO-SYSTEM-ASKED`, canonical `pandas-pyarrow-layer`. The exact one-line hunk is the file
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/GRADING_RULE_WORKED_CASE_PANDAS_PYARROW_LAYER_20261007.patch`: apply it with
   `git apply` (check first with `git apply --check`); if it no longer applies, make the same one-line change by hand and say so.
2. In the same file, the cadence restatement that follows from
   `org/missions/D14/LGIC/LGIC_BLANKFIX/prd/E1_CADENCE_RULES_RATIFIED.md` and `org/standards/NAMING_SCHEMA.json` block `cadence`
   (read its current version): where the file states the cadence rule (R7) or lists cadence words, it must say what the schema
   now says -- `daily` is at most once a calendar day on five or more days of the week and a weekday restriction is never named;
   a fixed interval shorter than a day takes `{N}min` or `{N}h` within the schema's ranges; an event rule takes
   `{function}-on-{event}`, decided per rule, the function never empty. Restate; do not invent a rule the two sources do not
   carry, and change no worked case's expected answer except the one in step 1. If a worked case in the file now contradicts
   the ratified rules, list it in your report and leave it.
3. `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_grading_rule.py`: asserts on the real file that the
   `pandas-pyarrow-layer` case reads `NO-SYSTEM-ASKED`; that the cadence text carries the daily definition's "five or more days",
   one `{N}min` and one `{N}h` example the schema's `interval_form.token_regex` accepts (read the regex from the schema and test
   your examples against it), and the `on-{event}` form; then runs
   `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider --color=no` and requires 0 failed. Last line
   `GRADING-RULE ok=True worked_case=True cadence=True suite_failed=0 suite_passed=N`.

`lib/tests/test_opal_naming.py` restates some worked cases at load time over what this file records, and it is NOT in your grant.
If your edit makes the suite fail, that is a refusal to report with the failing ids, not a test to edit.

Extend your existing proof-of-spec instance with the `BE5-AC2` row and re-validate it. Your rows continue at
`LGIC_BLANKFIX-W5-S2`.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a patch that no longer applies by the time its owner reads it (applies=True is checked against HEAD; the owner re-runs the check); a rendered sentence typed into the renderer instead of read from the schema (the proposal states where the sentence comes from); an edit to another lane's file by the back door (no such file is in the grant); BLIND: other documents that restate the three verdicts in prose -- only the renderer and the one worked case are read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE5-AC1 base FAIL as expected (file absent).
