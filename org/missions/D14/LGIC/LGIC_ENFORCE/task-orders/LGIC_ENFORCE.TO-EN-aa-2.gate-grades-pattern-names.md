# TO LGIC_ENFORCE.TO-EN-aa-2 -- round 21 EN-aa-2: row D1-W2-S152: the commit gate grades a PATTERN name, never PASS 0 graded
<to_id>LGIC_ENFORCE.TO-EN-aa-2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-aa-2` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0v) | **outcome_ref:** FWD-5 |
**depends_on:** none (slot ~2)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_ENFORCE's seven outcomes are all REALIZED (FWD-5 at round 20). The CTO's round-20 analysis
(`org/missions/D14/LGIC/LGIC_ENFORCE/ledger/ROUND_ANALYSIS.round20.md`) keeps the project open for two gate holes measured on its own mechanism, plus one red test, and names round 21's three
items. When both holes are closed and graded, the round-21 analysis is the close read.

**The instruments.** `lib/opal_lgctfm.py` is the legacy-transform engine (`walk`, `forks`, `plan`, `run`); `walk` reads three
registries: `infra/logic/registry/scopes.json`, `infra/logic/registry/remediations.json` and
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`. A full `walk --subject cottonwood --seed
opal-data-assets/cottonwood/ --out <dir>` takes about 2.5 minutes at the base and reads the live plane through `comp-find`. The commit
gate is `.tools/naming-gate.py` (`--diff FILE`, `--self-test`), called by `.tools/safe-commit.sh`; it asks
`lib/opal_naming_rootcheck.py place(name, typ, root)` for a name in a mapped root (kinds RIGHT, FIX, NOT-ASKED, PATTERN, CARDED,
REFUSED, HOLE). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. The switch file
`org/mcp/naming-place.enforce` is PRESENT and no cell touches it. Python 3.9 syntax, ASCII only, no new dependency. The bar:
`python -m pytest lib/tests -q -p no:cacheprovider` (193 passed, 1 skipped at the base) and `.tools/naming-gate.py --self-test`
(PASS) must not newly fail. The checks are `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py` (read-only; read it before you build -- each arm states what it runs).

**Client-data bound (0.0.0_AB_MSTR msgs 2712, 2739, 2758, 2796).** Search ONLY inside paths you name (lib/, .tools/, infra/,
org/missions/D14/LGIC/), never the whole repo and never in history. Never open, search, copy or git show anything under
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/, any org/**/W73_S*_EVIDENCE.json, or any cottonwood manifest.

### THE CELL

`EN-aa-2` (row `LGIC_ENFORCE-D1-W2-S152`): a planted per-firm stored-file prefix, `investor-reporting/directory` (S3Key;
`place("investor-reporting/directory", "S3Key", "investor-reporting/directory")` is PATTERN), committed on
`qa/lgic-enforce-r20-s12` @a09b284984 as `PROBE_PREFIX = os.environ.get("IRPT_DIRECTORY_PREFIX", "investor-reporting/directory")`
in `infra/aws/lambda/zz-lgic-enforce-r20-s12/probe.py`, read `NAMING-GATE: PASS 0 graded` with no line for the name. The analysis:
"a PATTERN name is graded through `place()` and gets a grade line, and a pass is never '0 graded'". Read the gate first to find
why the literal is skipped (a call's arguments are exempt? the string is not classified as a key?), and say which in your result.

**Build** in `.tools/naming-gate.py`: the planted literal is classified and graded, and a PATTERN name prints a `NAMING <verdict>
<file>:<line> <name> -> <canonical or pattern>` line (it may pass; it may not be silent). Get the diff with `git show --format=
a09b284984`. A non-pattern literal is graded exactly as today. Add a `--self-test` arm for the PATTERN line.

### ACCEPTANCE

<criterion id="AA2R21-AC1" cell_refs="EN-aa-2"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py pattern</invocation><expect>PASS-R21-PATTERN</expect></criterion>
`AA2R21-AC1` -- the planted commit's diff prints a NAMING line for investor-reporting/directory and a summary of at least 1 graded; the hand-typed control is still graded.

<criterion id="AA2R21-AC2" cell_refs="EN-aa-2"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`AA2R21-AC2` -- the gate's own arms, with the new one, hold.

<expected_criteria>AA2R21-AC1, AA2R21-AC2</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** No AWS write, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` and `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py` are never edited.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W<n>-S<k>`, `<n>` your slot, `<k>` one above the highest in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing) in `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never weaken a check or an expected value. A fact in this
  order the repository contradicts is also one row; keep working on what it does not block.

<paths>
.tools/naming-gate.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/gate.r21.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-aa-2.gate-grades-pattern-names.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-aa-2.gate-grades-pattern-names.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.21, round-21 cell `EN-aa-2` (section 0v).
<owned_cells>EN-aa-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AA2R21-AC1, AA2R21-AC2. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-aa-2.gate-grades-pattern-names.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AA2R21-AC1,AA2R21-AC2 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-aa-2.gate-grades-pattern-names.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** why the gate skipped the literal; the planted commit's gate lines; the self-test line; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- the cheapest pass special-cases the one planted string: the drain reads the change for a literal 'investor-reporting/directory' in the gate and refuses it. Grading nothing anywhere: the hand-typed control must still be graded. Breaking every seat's commits: self-test and pytest at the drain. BLIND: one planted shape (an os.environ.get default) is exercised, not every way a pattern name can be written.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/ROUND_ANALYSIS.round20.md` section 3 (`1.0.0_SA_CTO~DELL1`, msg 2861); decomposition section 0v. Base dry-run at the cut, by the issuer at
base 4ca1f1092e: AA2R21-AC1 base: FAIL as expected (planted: NO GRADE LINE | NAMING-GATE: PASS 0 graded; the control literal IS graded at the base). AA2R21-AC2 base: PASS as expected (NAMING-GATE-SELF-TEST: PASS).
