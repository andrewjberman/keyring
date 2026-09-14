# TO IRPT_FNTEND.TO-FE-s-28 -- an integrity check the checked party may decline to arm is not an enforcement

<to_id>IRPT_FNTEND.TO-FE-s-28</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (no PRD surface -- FABRIC grain, decomp R4.5(ii)) | **Decomp cell:** `FE-s-28` (round 4, v0.4 @1d9839797c) | **outcome_ref:** none -- serves the record | **depends_on:** none -- READY ROOT | **slot:** ~4 | **rows:** S38, S31, S43

---

## WORKER FACE

### THE CELL

`FE-s-28` -- **the invocation-alignment limb exists, works, and is armed by the exact party whose divergence it catches.**

Round 2 (`S31`): an issuer corrected two criteria in a SPAWN PROMPT and never in the task-order FILE. A worker ran and passed invocations the RECORD did not contain, and `proof-of-spec-check` returned `VALID` over the divergence because nothing compared the two.

Round 3 (`FE-s-23`) built the comparison limb. It found **two more real divergences** immediately -- `F18-AC17` recorded `timeout 180` against a criterion saying `120`, and `F12-AC5` recorded an UNBALANCED shell command -- and measured the estate: **294 instances, 874 comparable rows, 318 divergent.** At default-ENFORCE the cell's two constraints were arithmetically unsatisfiable, so it split the axis: detection unconditional, REFUSAL opt-in via a `<placeholders>` declaration in the task order. That was the right call with the numbers it had, and it was disclosed rather than assumed.

`1.0.0_SA_CTO` ruling D closes it: **the declaration becomes MANDATORY at the L6 gate.** An opt-in enforcement is armed by the issuer -- *the exact party whose prompt-only correction the limb exists to catch* -- which is a courtesy, not an enforcement. `NON-APPLICATION: none; an opt-in integrity check has no honest scope.`

**Make `.tools/to-pipeline-gate.py` REFUSE a newly-added task order that does not declare its placeholders.** An issuance then cannot be cut without arming the check on itself.

⛔ **AND THE RETROACTIVITY QUESTION IS THE WHOLE DIFFICULTY, SO MEASURE IT BEFORE YOU CHOOSE.** 0 of 2554 existing task orders carry the element. A gate that refuses every pre-existing order is a gate nobody can commit past; a gate that grandfathers everything forever is the opt-in again under a new name. **The refusal must bind what an issuance ADDS, and the boundary you pick must be stated in the refusal text itself** so a seat that hits it learns the rule rather than guessing at it.

### ACCEPTANCE

<criterion id="F28-AC1" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 120 python .tools/to-pipeline-gate.py --self-test</invocation><expect>RESULT: 0 arm</expect></criterion>
`F28-AC1` -- the gate's own self-test passes with the new limb, whatever the arm count has grown to. ⛔ **THE BAR WAS CORRECTED BY THE ISSUER BEFORE ISSUING, and the reason is worth your attention: this tool does NOT print the same shape as `proof-of-spec-check`.** Measured at this cut it prints `RESULT: 0 arm(s) failed of 42`, not `RESULT: N of N`. So the bar is `RESULT: 0 arm` -- it matches a clean run at ANY arm count and CANNOT match `RESULT: 3 arm(s) failed of 42`. It carries no literal parenthesis because `<expect>` is a REGEX and `arm(s)` would match the text `arms`. **Never assume two tools in `.tools/` report alike.**

<criterion id="F28-AC2" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 180 python .tools/tests/test_mandatory_placeholders.py</invocation><expect>UNDECLARED NEW TO REFUSED: 3 of 3</expect></criterion>
`F28-AC2` -- **the negative control.** Three newly-added task orders with no `<placeholders>` element are each REFUSED, and each refusal NAMES the element and the file.

<criterion id="F28-AC3" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 180 python .tools/tests/test_mandatory_placeholders.py</invocation><expect>DECLARED NEW TO ADMITTED: 3 of 3</expect></criterion>
`F28-AC3` -- the other arm: three newly-added orders that DO declare are admitted. A gate that refuses everything is as useless as one that refuses nothing.

<criterion id="F28-AC4" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 300 python .tools/tests/test_mandatory_placeholders.py</invocation><expect>EXISTING CORPUS STILL COMMITTABLE</expect></criterion>
`F28-AC4` -- **the arm that decides whether this is shippable at all**, measured on REAL bytes rather than fixtures: the boundary you chose does not make the existing corpus uncommittable. The test prints the denominator it checked and the boundary rule in one line.

<criterion id="F28-AC5" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 180 python .tools/tests/test_mandatory_placeholders.py</invocation><expect>REFUSAL TEXT NAMES THE RULE AND ITS BOUNDARY</expect></criterion>
`F28-AC5` -- a seat that hits the refusal can learn the rule from the refusal: its text names the missing element, the boundary (what it binds and what it does not) and how to satisfy it. ⚠ **A fail-closed gate's error text is its author's CLAIM, not a measurement** -- so this criterion asserts what the text SAYS, and `F28-AC2`/`F28-AC3` are what prove it keys on the right thing.

<criterion id="F28-AC6" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 300 python .tools/tests/test_proof_of_spec_alignment.py</invocation><expect>BATTERY PASS</expect></criterion>
`F28-AC6` -- `FE-s-23`'s own alignment battery still passes; you are arming its limb, not changing what it compares. If that file is named differently, run the battery that exists and say which in the result file.

<criterion id="F28-AC7" cell_refs="FE-s-28"><invocation>cd <WS> && timeout 120 python .tools/to-pipeline-gate.py --self-test</invocation><expect>placeholders</expect></criterion>
`F28-AC7` -- the limb is DISCOVERABLE from the tool itself, so a seat can find what it keys on without reading the source.

<criterion id="F28-AC8" cell_refs="FE-s-28" judgment="true"/>
`F28-AC8` -- graded at L9: the boundary between what the gate binds and what it grandfathers is defensible and stated, rather than chosen to make the tests pass. RECORD; NO VERDICT.

<expected_criteria>F28-AC1, F28-AC2, F28-AC3, F28-AC4, F28-AC5, F28-AC6, F28-AC7, F28-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. ⛔ **THIS IS THE ONLY ROUND-4 CELL WRITING THE WORKSPACE REPO AND IT TOUCHES NO PORTAL PATH.** You need no portal worktree and must not create one.
- ⛔ **NEVER EDIT AN EXISTING TASK ORDER OR PROOF INSTANCE TO MAKE YOUR GATE PASS.** The corpus is what you are testing against. If a real order trips your boundary, that is a FINDING -- a row naming the file and the rule -- never a reason to edit it or to widen the boundary until it stops.
- ⛔ **YOUR OWN ORDER IS PART OF THE CORPUS.** This face declares its placeholders below, so your gate will be graded against it. If that creates a circularity you cannot resolve, name it in a row rather than special-casing your own file.
- **Workspace paths bind MECHANICALLY.** A refused write is a `BLOCKING` row naming the path and the refusal text -- never an override, and never `GIT_COMMIT_AUTHOR_OVERRIDE`.
- **`.py` edits pass `.tools/commit-gate.sh`** (py_compile + ds-precommit + ruff py39) -- universal law, not this order's invention.
- **One repo: the workspace.** Never stage `portal`. Never push, merge, rebase, `checkout --` or `clean`.
- ⚠ **Do not key any criterion on rc alone.** Measured on a sibling tool this project: `proof-of-spec-check.py --help` prints `READ-ERROR (rc=2)` and, through a pipe, reports rc=0 because a pipeline's status is its LAST command's (rows S36, W3-S15).
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W4-S<k>`. ⛔ **Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) for the last W4 id before minting** -- the W4 coordinate's highest id lives in `v1`, and a starting number named in a face was refused by the gate once for exactly this reason (row S36). This face names none. Write with `newline='\n'` and READ THE DIFFSTAT of your commit (row S47).
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<placeholders>WS</placeholders>

<paths>
.tools/to-pipeline-gate.py
.tools/tests/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.4 @1d9839797c, cell `FE-s-28`.
<owned_cells>FE-s-28</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F28-AC1` .. `F28-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F28-AC1,F28-AC2,F28-AC3,F28-AC4,F28-AC5,F28-AC6,F28-AC7,F28-AC8` BEFORE the `complete` flip. ⚠ Your instance is graded by a tool whose sibling gate you are changing -- say so in the result file, and state which arm is the stronger oracle (`F28-AC4`'s real-corpus run, not the self-test). `F28-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `mandatory-placeholders.result.md` beside it, stating the boundary and why it is the right one. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource; the subject is a repo-local gate.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; this cell has no PRD surface and is declared at the FABRIC grain in R4.5(ii), as FE-s-23 was in round 3.
the gap: RUN -- FE-s-23 measured 294 instances / 874 comparable rows / 318 divergent, and 0 of 2554 task orders carry the <placeholders> element. Those two numbers together are why the opt-in existed and why the boundary is the hard part.
the ruling: RUN -- 1.0.0_SA_CTO ruling D, NON-APPLICATION: none. The CTO's own note: fourth instance in a day of "a named enforcement surface is a claim until someone runs it".
instrument caution: RUN -- a sibling tool's --help returns rc=2 while reporting rc=0 through a pipe; no criterion in this order keys on rc alone.
lane: .tools/ is workspace-mechanical; a refusal is a BLOCKING row. This order DECLARES its own placeholders so the cell's gate is graded against its own face.
</preflight>

Seating: slot ~4; READY ROOT, seated at issuance on a WORKSPACE-ONLY worktree (no portal pair), with the `<status>` flip committed BEFORE the worktree is cut (row S26).
