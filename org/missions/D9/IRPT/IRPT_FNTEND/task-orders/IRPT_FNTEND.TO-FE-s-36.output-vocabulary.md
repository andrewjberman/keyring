# TO IRPT_FNTEND.TO-FE-s-36 -- a bar its tool can never print is refused at the cut

<to_id>IRPT_FNTEND.TO-FE-s-36</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-36` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** the evidence plane | **depends_on:** FE-s-29 (the same file, `.tools/to-pipeline-gate.py`) | **slot:** ~4 | **rows:** S55, C-S58

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-36` -- **five criteria in round 4 were cut against an assumption about a tool's output or a surface's reach, and a worker's refusal caught every one; no gate caught any.** (S55 counts them; `1.0.0_SA_CTO` ruling N adopts this limb.)

The clearest shape is F28-AC6 as issued: its expect bar was `0 fail`, against `.tools/tests/test_proof_of_spec_alignment.py`, which prints only `BATTERY PASS` or `BATTERY FAILED` (`:458-460`). It could never pass, and nothing said so until a worker ran it. The issuer re-cut it to `BATTERY PASS`.

Build **the output-vocabulary limb in the L6 gate**: when a newly added task order is committed, a criterion whose expect bar its named tool can never print is refused. ⛔ **Prospective only** -- it grades orders STAGED AS ADDED, the scope the gate already uses. It never grades an existing order, so it cannot grade this round's.

What the limb can and cannot know is yours to design and to state. It cannot run a test the worker has not written yet, and it must not refuse an honest bar it cannot evaluate. Where it cannot tell, it ANNOUNCES rather than refuses.

### ACCEPTANCE

<criterion id="F36-AC1" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 180 python .tools/to-pipeline-gate.py --self-test</invocation><expect>RESULT: 0 arm\(s\) failed of</expect></criterion>
`F36-AC1` -- the gate's own self-test, every arm, including FE-s-29's.

<criterion id="F36-AC2" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_output_vocabulary.py</invocation><expect>F28-AC6 AS ISSUED: REFUSED</expect></criterion>
`F36-AC2` -- **the real positive control.** F28-AC6's text as issued, read by `git show` from workspace commit `b6062ad2a2`, staged as a newly added order in a REAL git index, is refused -- its tool never prints the bar.

<criterion id="F36-AC3" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_output_vocabulary.py</invocation><expect>F28-AC6 AS RE-CUT: ADMITTED</expect></criterion>
`F36-AC3` -- the same order with F28-AC6 as re-cut at `9ab6043728` (`BATTERY PASS`) is admitted. Without this arm, AC2 is indistinguishable from refusing everything.

<criterion id="F36-AC4" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_output_vocabulary.py</invocation><expect>A RUNNER'S OWN VOCABULARY: ADMITTED</expect></criterion>
`F36-AC4` -- a criterion whose bar comes from the test runner rather than the test file -- a `(?<![0-9])0 fail` bar on `bun test <an existing file>` -- is admitted.

<criterion id="F36-AC5" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_output_vocabulary.py</invocation><expect>TARGET ABSENT AT THE CUT: ANNOUNCED, NOT REFUSED</expect></criterion>
`F36-AC5` -- a criterion invoking a test file that does not exist yet (the ordinary case: the worker writes it) is announced, not refused.

<criterion id="F36-AC6" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_output_vocabulary.py</invocation><expect>REAL ROUND-5 ORDERS: 0 REFUSED</expect></criterion>
`F36-AC6` -- the round-5 orders already on CLOUD, each staged as newly added, are not refused. The test prints its denominator. If one is, that is a row naming the criterion: either the order is wrong or the limb is.

<criterion id="F36-AC7" cell_refs="FE-s-36" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_mandatory_placeholders.py</invocation><expect>EXISTING CORPUS STILL COMMITTABLE</expect></criterion>
`F36-AC7` -- prospective: the existing corpus is still committable.

<criterion id="F36-AC8" cell_refs="FE-s-36" judgment="true" drives="none"/>
`F36-AC8` -- graded at L9: the limb catches the F28-AC6 shape, refuses no bar it cannot evaluate, and says plainly what it cannot know. RECORD; NO VERDICT.

<expected_criteria>F36-AC1, F36-AC2, F36-AC3, F36-AC4, F36-AC5, F36-AC6, F36-AC7, F36-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override. You touch no portal path, and not `.tools/proof-of-spec-check.py`.
- ⛔ **FE-s-29 landed four limbs in this same file before you.** Keep every one of them; its self-test arms stay green (F36-AC1).
- ⛔ **CONTROLS FROM REAL SHAPES.** Build the positive and negative controls from real committed orders, read by `git show` at the commits named, in a real git index -- never from strings you chose.
- ⛔ **CALL THE INSTRUMENT.** Test the limb through the gate's own function or CLI, never by re-deriving its rule.
- **The limb never runs a worker's test.** It reads what exists at the cut. State in the result file exactly what it reads and what it declines to judge.
- **Anchors.** Anything your tests print as a count is anchorable: left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
- **Evidence hygiene.** Each row's `output_evidence` carries the deciding invocation's output only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. **Commit** with `.tools/safe-commit.sh --author "<your serial> <<your serial>@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool or python. A `.py` edit passes `commit-gate.sh`. Verify every commit by `git log`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W4-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<paths>
.tools/to-pipeline-gate.py
.tools/tests/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-36`.
<owned_cells>FE-s-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F36-AC1` .. `F36-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-36.output-vocabulary.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F36-AC1,F36-AC2,F36-AC3,F36-AC4,F36-AC5,F36-AC6,F36-AC7,F36-AC8` BEFORE the `complete` flip. `F36-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `output-vocabulary.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the shape: RUN by the issuer -- F28-AC6 as issued at b6062ad2a2 expected `0 fail`; test_proof_of_spec_alignment.py:458-460 prints only BATTERY PASS / BATTERY FAILED; re-cut to BATTERY PASS at 9ab6043728.
the class: RUN -- S55, five cuts against an assumption in round 4, none caught by a gate.
lane: the <paths> block IS the grant; proof-of-spec-check.py excluded.
</preflight>

Seating: slot ~4; wave B -- seated only after FE-s-29 is drained (the same file), on a fresh worktree cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row S26).
