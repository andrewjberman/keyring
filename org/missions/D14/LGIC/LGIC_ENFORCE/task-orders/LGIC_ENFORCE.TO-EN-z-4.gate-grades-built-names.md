# TO LGIC_ENFORCE.TO-EN-z-4 -- round 20 EN-z-4: row D1-W2-S9: the commit gate grades a name built by name() at a call site, or prints that it did not
<to_id>LGIC_ENFORCE.TO-EN-z-4</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-z-4` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0u) | **outcome_ref:** FWD-5 |
**depends_on:** none (first on slot ~2)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_ENFORCE has 6 of 7 outcomes REALIZED. FWD-5 (PRD `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md`, the FWD-5 card
at line 132; cell E9 at line 402) reads: anyone can run the check over the whole estate -- the stored code AND what is actually
running -- and get a ranked list of every name that breaks the pattern, each with its correct form, totals shown; the totals agree with
the ranking the naming work produced by hand; and a name the check cannot read STOPS the run loudly rather than being filed as breaking
the pattern. The CTO's grade (`org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md`, last section): the stored-code half is MET (86 of 86 roots, 0 holes); round 20 owes the live
plane, the hand-ranking compare, the loud stop, and two gate rows (D1-W2-S9, D1-W2-S12).

**The instruments.** `python lib/opal_naming.py census [--live] [--repo] [--names FILE] [--not-judged FILE] [--report PATH]`
judges names with `grade()`; the live plane is `comp-find --corpus aws` (about 8 s); a RAISE (a name `grade()` cannot read) stops
the run with exit 3, unless the name is CARDED in the `--not-judged` JSON list (`{name, plane, card}`; R-29). `python
lib/opal_naming.py census --all-roots` (about 45 s) is the stored-code check; at the base `133bf5f7a4` it prints `ALL-ROOTS ok=True
roots_total=86 mapped=86 unmapped=0 ... hole=7 ...`. The commit gate is `.tools/naming-gate.py` (`--diff FILE`, `--self-test`),
called by `.tools/safe-commit.sh`; `lib/opal_naming_rootcheck.py place(name, typ, root)` returns a dict whose `kind` is one of RIGHT,
FIX, NOT-ASKED, PATTERN, CARDED, REFUSED, HOLE. The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. The switch
file `org/mcp/naming-place.enforce` is PRESENT and no cell touches it. Python 3.9 syntax, ASCII only, no new dependency. The checks
are `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py` (read-only; read it before you build -- each arm states exactly what it reads).

### THE CELL

`EN-z-4` (row `LGIC_BLANKFIX-D1-W2-S9`, ruled in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round14.md` section
2: "the firm names pass the gate only in module form, where the gate grades 0 strings. That pass is ABSENT, not EXERCISED ... a
gate-coverage defect"). At the base, a new `.tf` whose only name is an `opal_name` module block (system irpt, scope cottonwood,
function reporting-gold, kind role, qualifier scheduler) gives `NAMING-GATE: PASS 0 graded`; so does a Python
`name("irpt", "cottonwood", "reporting-gold", "role", "scheduler")` call. The literals are skipped as permitted builder arguments
(`py_literals` skips builder-call arguments; `tf_literals` marks an `opal_name` module block's literals permitted) and nothing
replaces them.

**Build** in `.tools/naming-gate.py`: for an `opal_name` module block, and for a Python `name(...)` builder call, whose arguments are
all literals, compose the built name with `lib/opal_naming.py name()` and grade it like any other name, printing its usual
`NAMING <verdict> <file>:<line> <name> -> <canonical>` line and counting it in the summary. Where the arguments are not all
literals (or `name()` refuses them), print `NAMING BUILT-NOT-GRADED <file>:<line> <why>` so a pass there is never silent. A hand-typed
literal is graded exactly as today. Add arms for both forms to `--self-test`. The expected built name for the fixture is
`irpt-cot-reporting-gold-scheduler-role`.

### ACCEPTANCE

<criterion id="Z4R20-AC1" cell_refs="EN-z-4"><invocation>python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py s9</invocation><expect>PASS-R20-S9</expect></criterion>
`Z4R20-AC1` -- the module-form and the call-form fixtures each print a graded line for the built name or a BUILT-NOT-GRADED line; the hand-typed control is still graded.

<criterion id="Z4R20-AC2" cell_refs="EN-z-4"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`Z4R20-AC2` -- the gate's own arms, including the new ones, hold.

<expected_criteria>Z4R20-AC1, Z4R20-AC2</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** No AWS write (the live plane is read through `comp-find --corpus aws` only), no `terraform` command,
  no registry edit, no rename of any resource; `org/mcp/naming-place.enforce` and `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py` are never edited.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W<n>-S<k>`, `<n>` your slot, `<k>` one above the highest in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate or the row gate refuses it) in
  `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never weaken a check or an expected value. A fact in this order the repository contradicts is
  also one row; keep working on what it does not block.

<paths>
.tools/naming-gate.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/gate-built-names.r20.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-z-4.gate-grades-built-names.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-4.gate-grades-built-names.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.20, round-20 cell `EN-z-4` (section 0u).
<owned_cells>EN-z-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Z4R20-AC1, Z4R20-AC2. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-z-4.gate-grades-built-names.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Z4R20-AC1,Z4R20-AC2 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-4.gate-grades-built-names.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** both fixtures' gate lines; the self-test line; how many tracked opal_name blocks and name() calls the gate now grades (run it over `git diff` of one real root as a demonstration); the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- the cheapest pass is to print BUILT-NOT-GRADED for every built name and grade none; the order prefers grading, and the drain reads the result for how many are graded. Grading nothing anywhere: the hand-typed control must still be graded. Breaking the live gate for every seat: the self-test and the drain's pytest run before the merge. BLIND: the check runs two fixtures, not every builder shape in the tree.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md` re-grade 2026-10-09 ~15:2xZ (`1.0.0_SA_CTO~DELL1`, msg 2639), round-20 list; decomposition section 0u. Base dry-run at
the cut, by the issuer at base 133bf5f7a4: Z4R20-AC1 base: FAIL as expected (`NAMING-GATE: PASS 0 graded` on the module fixture; the control fixture IS graded at the base: `NAMING RAISE ... zz-probe-scheduler-role-typed`). Z4R20-AC2 base: PASS as expected (NAMING-GATE-SELF-TEST: PASS).
