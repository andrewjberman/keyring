# TO IRPT_FNTEND.TO-FE-s-44 -- the red artifact-coverage battery is diagnosed, not inherited

<to_id>IRPT_FNTEND.TO-FE-s-44</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~6</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-44` (round 7, v0.7 @0ad0ea1fa9) | **outcome_ref:** the evidence plane | **depends_on:** none | **slot:** ~6 | **rows:** C-S90 (W4-S15)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-44` -- **an acceptance battery for the checker has been red since before this round, and its controls cannot fail.** This is `1.0.0_SA_CTO` RULING AB (round-6 analysis @4713211d87 s.3), on row W4-S15 as graduated by 3.0.0_SA_CVO (C-S90).

Measured by the issuer at CLOUD 8f4106a7f2 with `python org/standards/test_artifact_coverage_both_grammars.py`:
- **3/6 PASS, rc=1.**
  - `A-DS-GRAMMAR-STILL-PASSES`, `B-WP1-GRAMMAR-FLIPS` and `E-EXPLICIT-FIELD-PASSES` return rc=1, where rc=0 is owed.
  - `C-UNCOVERED-STILL-FAILS`, `D-INCIDENTAL-EXCLUSION-NOW-FAILS` and `F-DANGLING-CITATION-FAILS` "pass" only because EVERY arm now returns rc=1.
  - So the battery currently discriminates nothing: its anti-disable controls cannot fail while everything is refused.
  - `1.0.0_SA_CTO` measured the same 3/6 at `059526828b`.
- **It is a SCRIPT, not a pytest module.** It calls `sys.exit` at import (`:128`), so `pytest` on it reports "no tests ran". Invoke it as `python <file>`.
- **Where it came from:** it was written by `0.8.0_AE_CloudComp` @ba59c67ada on 2026-08-19. Its synthetic instances come from `base()` (`:39-60`): schema 1.0, `to_id` `FIXTURE.T`, phase `NON-BUILD-OTHER`. Several checker limbs have landed since 08-19: FE-s-29's, FE-s-36's, FE-s-37's binding, and the artifact-resolution and alignment frames.

**THE DIAGNOSIS, THEN THE REMEDY:**
1. Run the checker on each arm's instance, and read which limb's violation refuses A, B and E.
2. Decide which side is wrong. Either the battery's instances are stale against a correct limb, or the limb is wrong for a legitimate instance.
3. Bring the wrong side current. Afterwards A, B and E read rc=0, and C, D and F FAIL **for their NAMED violation** (artifact-coverage, or the dangling citation), not by a blanket refusal.

### ACCEPTANCE

<criterion id="F44-AC1" cell_refs="FE-s-44" drives="none"><invocation>cd <WS> && timeout 600 python org/standards/test_artifact_coverage_both_grammars.py</invocation><expect>ARTIFACT-COVERAGE BATTERY: 6/6 PASS \(denominator 6\)</expect></criterion>
`F44-AC1` -- the battery, whole, green.

<criterion id="F44-AC2" cell_refs="FE-s-44" drives="none"><invocation>cd <WS> && timeout 600 python org/standards/test_artifact_coverage_both_grammars.py</invocation><expect>CONTROLS FAIL FOR THEIR NAMED VIOLATION: 3 of 3(?![0-9])</expect></criterion>
`F44-AC2` -- C, D and F each FAIL the checker, and each FAILS on the violation it is named for. The battery prints, per control, the violation line it matched.

<criterion id="F44-AC3" cell_refs="FE-s-44" drives="none"><invocation>cd <WS> && timeout 600 python org/standards/test_artifact_coverage_both_grammars.py</invocation><expect>WITH THE COVERAGE RULE DISABLED IN A SCRATCH COPY, THE CONTROLS CATCH IT: yes</expect></criterion>
`F44-AC3` -- the mutant. A scratch copy of the checker, with its artifact-coverage rule disabled, makes the controls go red. That proves the battery can fail on the case it exists for. The copy lives under `<WS>/.scratch/` and is removed afterwards.

<criterion id="F44-AC4" cell_refs="FE-s-44" drives="none"><invocation>cd <WS> && timeout 180 python .tools/proof-of-spec-check.py --self-test</invocation><expect>RESULT: (\d+) of \1 arm\(s\) behaved</expect></criterion>
`F44-AC4` -- the checker's own self-test (42 of 42 at the cut). If you changed the checker, add an arm for the limb you corrected.

<criterion id="F44-AC5" cell_refs="FE-s-44" drives="none"><invocation>cd <WS> && timeout 900 python .tools/tests/test_governing_binding.py</invocation><expect>EVERY .tools BATTERY THAT CALLS EITHER TOOL: (\d+) of \1 green(?![0-9])</expect></criterion>
`F44-AC5` -- **the whole-suite census of record**. This is FE-s-37's census battery over every `.tools/tests/` file that calls the checker or the gate, run once with your change applied.

<criterion id="F44-AC6" cell_refs="FE-s-44" drives="none"><invocation>cd <WS> && timeout 180 python .tools/to-pipeline-gate.py --self-test</invocation><expect>RESULT: 0 arm\(s\) failed of</expect></criterion>
`F44-AC6` -- the flip gate's self-test (0 of 72 failed at the cut). The gate runs the checker on every flip.

<criterion id="F44-AC7" cell_refs="FE-s-44" judgment="true" drives="none"/>
`F44-AC7` -- graded at L9: the diagnosis names the limb that refused A, B and E, which side was wrong and why, and the battery discriminates again. RECORD; NO VERDICT.

<expected_criteria>F44-AC1, F44-AC2, F44-AC3, F44-AC4, F44-AC5, F44-AC6, F44-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override. You touch no portal path.
- ⛔ **DIAGNOSE FIRST, AND WRITE THE DIAGNOSIS BEFORE THE FIX.** For each of A, B and E, your result file carries the checker's violation lines at the cut and the limb they come from, cited `file:line @ <commit>`.
- ⛔ **`.tools/proof-of-spec-check.py` IS YOURS ONLY IF THE CHECKER IS THE WRONG SIDE,** and then only for the limb that refuses a legitimate instance. If the battery is the wrong side, you change the battery alone and leave the checker byte-identical; say which, and prove it.
- ⛔ **KEEP EVERY LIMB THAT IS RIGHT.** FE-s-29's, FE-s-36's and FE-s-37's limbs, and the binding, stay as they are. Loosening a limb to turn the battery green is the disabled-rule failure the battery exists to catch.
- ⛔ **CONTROLS FROM REAL SHAPES.** A fixture the battery builds is shaped like a real committed instance, and the result file names the committed instance it was compared with. RULING AC: files are read as committed blobs.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F44-AC5). A battery your change turns red that is outside your grant is a BLOCKING row with the list, never an edit.
- ⛔ **NOT YOURS:** `.tools/receiving-check.py` and `.tools/tests/test_receiving_binding.py` (FE-s-43's); `.tools/to-pipeline-gate.py`; every existing file in `.tools/tests/`.
- **Anchors.** Counts your tests print are anchorable: left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
- **Evidence hygiene.** Each row's `output_evidence` carries the deciding invocation's output only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Commit** with `.tools/safe-commit.sh --author "<your serial> <<your serial>@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool or python. A `.py` edit passes `commit-gate.sh`. Verify every commit by `git log`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W6-S<k>`. The W6 coordinate holds no row yet, so your first is `IRPT_FNTEND-W6-S1`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<paths>
org/standards/test_artifact_coverage_both_grammars.py
.tools/proof-of-spec-check.py
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.7 @0ad0ea1fa9, cell `FE-s-44`.
<owned_cells>FE-s-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F44-AC1` .. `F44-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~6/IRPT_FNTEND.TO-FE-s-44.artifact-coverage-battery-current.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F44-AC1,F44-AC2,F44-AC3,F44-AC4,F44-AC5,F44-AC6,F44-AC7` BEFORE the `complete` flip -- with the checker as your change leaves it. `F44-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `artifact-coverage-battery-current.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-6 analysis s.1, no addendum).
the battery: RUN by the issuer at CLOUD 8f4106a7f2 -- python org/standards/test_artifact_coverage_both_grammars.py reads 3/6 PASS rc=1; A, B and E rc=1 where 0 is owed; C, D and F pass only as blanket refusals.
the invocation: RUN -- under pytest the file collects zero (sys.exit at :128); python <file> is its form.
the authorship: RUN -- written by 0.8.0_AE_CloudComp @ba59c67ada (2026-08-19); base() at :39-60 builds the synthetic instances.
instruments at the cut: RUN -- to-pipeline-gate --self-test 0 of 72 failed; proof-of-spec-check --self-test 42 of 42 (CLOUD edac45e48c).
lane: the <paths> block IS the grant; the checker only if it is the wrong side; receiving-check, the gate and the existing .tools/tests excluded.
</preflight>

Seating: slot ~6; one wave -- round 7 has no dependency edge, seated on a fresh worktree cut from HEAD with the `<status>` flip committed BEFORE the worktree is cut (row S26).
