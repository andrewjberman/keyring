# TO IRPT_FNTEND.TO-FE-s-37 -- the governing order is the order being flipped

<to_id>IRPT_FNTEND.TO-FE-s-37</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-37` (round 6, v0.6 @d4d8ae6f9a) | **outcome_ref:** the evidence plane | **depends_on:** none -- READY ROOT | **slot:** ~4 | **rows:** S61, C-S84

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-37` -- **the checker can be steered by the party it grades, and this cell binds it.** `1.0.0_SA_CTO` RULING S (round-5 analysis @942e4ff992 s.2), adopted as the head of round 6. F29-AC15's third clause -- *"none of the four can be satisfied by the party it grades"* -- was graded NOT MET by 3.0.0_SA_CVO (row S61).

Measured by the issuer at CLOUD 6462e98cc6:
- `check_complete_flip` (`.tools/to-pipeline-gate.py:2469`) finds the proof instance beside the flipped order and runs `subprocess.run(["python", chk, inst], ...)` -- the instance and nothing else. It passes neither the flipped order nor a criterion list.
- `.tools/proof-of-spec-check.py` resolves its governing order from the instance's `decomp_ref.to_ref` when present (`:614-641`, "An explicit decomp_ref.to_ref wins when present"; `_governing_rel` at `:1300`). Limbs 2 (count-bar) and 3 (drives) decide ENFORCE vs ANNOUNCE from that order's add commit.
- The CVO measured it on FE-s-29's own instance: with `to_ref` doctored to point at `IRPT_FNTEND.TO-FE-s-28.*` (a real round-4 order), both limbs moved to ANNOUNCE/LEGACY and **no violation named the mismatch**.

**THE BINDING:** `check_complete_flip` hands the checker the flipped order's path, and the checker takes THAT as the governing order. An instance whose `decomp_ref.to_ref` (or `to_id`) names a DIFFERENT order is REFUSED, before any limb runs, by a violation that names BOTH paths. `to_ref` stays as a cross-check, never as the source. When the checker is run from its CLI without a flipped order, its behaviour is yours to state and prove -- and it must not be looser than today's (an unbound run says so in its output).

### ACCEPTANCE

<criterion id="F37-AC1" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 180 python .tools/to-pipeline-gate.py --self-test</invocation><expect>RESULT: 0 arm\(s\) failed of</expect></criterion>
`F37-AC1` -- the gate's own self-test, every arm (0 of 70 failed at the cut).

<criterion id="F37-AC2" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 180 python .tools/proof-of-spec-check.py --self-test</invocation><expect>RESULT: (\d+) of \1 arm\(s\) behaved</expect></criterion>
`F37-AC2` -- the checker's own self-test, every arm (32 of 32 at the cut). Add arms for the binding.

<criterion id="F37-AC3" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_governing_binding.py</invocation><expect>DOCTORED to_ref THROUGH THE FLIP PATH: REFUSED</expect></criterion>
`F37-AC3` -- **the arm the ruling exists for.** FE-s-29's committed instance with `decomp_ref.to_ref` doctored to the real `IRPT_FNTEND.TO-FE-s-28.*` order, its order's `<status>` flip staged in a REAL git index, is refused by the gate's own flip path (`check_complete_flip`), not only by the checker's CLI.

<criterion id="F37-AC4" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_governing_binding.py</invocation><expect>THE REFUSAL NAMES BOTH PATHS: yes</expect></criterion>
`F37-AC4` -- the violation text names the flipped order's path and the path `to_ref` declared. The test prints the violation.

<criterion id="F37-AC5" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_governing_binding.py</invocation><expect>POSITIVE CONTROL, FE-s-29 AS COMMITTED: VALID</expect></criterion>
`F37-AC5` -- the same flip path with FE-s-29's instance exactly as committed stays VALID. Without this arm AC3 is indistinguishable from refusing everything.

<criterion id="F37-AC6" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_governing_binding.py</invocation><expect>LIMB 1 FRAME ON THE DOCTORED ARM: \S</expect></criterion>
`F37-AC6` -- limb 1's frame (the placeholders reader) is read and printed on the doctored arm, which the CVO did not read.

<criterion id="F37-AC7" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_governing_binding.py</invocation><expect>LIMBS 2 AND 3 READ THE FLIPPED ORDER'S BOUNDARY: (\d+) of \1(?![0-9])</expect></criterion>
`F37-AC7` -- with the governing order bound, limbs 2 and 3 read ENFORCE/NEW for an order added after their rulings even when `to_ref` names a legacy order; the test prints each limb's frame for the bound and the doctored run.

<criterion id="F37-AC8" cell_refs="FE-s-37" drives="none"><invocation>cd <WS> && timeout 900 python .tools/tests/test_governing_binding.py</invocation><expect>EVERY .tools BATTERY THAT CALLS EITHER TOOL: (\d+) of \1 green(?![0-9])</expect></criterion>
`F37-AC8` -- **the whole-suite census of record** (R6.2 `census`): every file under `.tools/tests/` that calls `proof-of-spec-check.py` or `to-pipeline-gate.py` is run once with your change applied, the denominator and each file printed. Measured at the cut: 3 of 63 files reference `to_ref` (count-bar, alignment, seeded).

<criterion id="F37-AC9" cell_refs="FE-s-37" judgment="true" drives="none"/>
`F37-AC9` -- graded at L9, where F29-AC15's clause 3 is re-graded on this instance: no limb of the checker can be steered by the party it grades. RECORD; NO VERDICT.

<expected_criteria>F37-AC1, F37-AC2, F37-AC3, F37-AC4, F37-AC5, F37-AC6, F37-AC7, F37-AC8, F37-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override. You touch no portal path.
- ⛔ **CONTROLS FROM REAL SHAPES.** The doctored arm is FE-s-29's committed instance and FE-s-28's committed order, read by `git show`, in a real git index staging a real flip -- never strings you chose. A detector that cannot go non-zero on the real positive case is a constant.
- ⛔ **CALL THE INSTRUMENT.** Test the binding through `check_complete_flip` and the gate's CLI, and through the checker's CLI; never re-derive their rules.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F37-AC8). A battery your change turns red that is outside your grant is a BLOCKING row with the list, never an edit. Keep FE-s-29's and FE-s-36's limbs as they are.
- **Every other order's instance still validates.** The binding must not refuse an instance whose `to_ref` names its own order; say in the result file how you proved that over the committed IRPT_FNTEND instances (denominator printed).
- **Anchors.** Counts your tests print are anchorable: left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
- **Evidence hygiene.** Each row's `output_evidence` carries the deciding invocation's output only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. **Commit** with `.tools/safe-commit.sh --author "<your serial> <<your serial>@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool or python. A `.py` edit passes `commit-gate.sh`. Verify every commit by `git log`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W4-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<paths>
.tools/to-pipeline-gate.py
.tools/proof-of-spec-check.py
.tools/tests/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.6 @d4d8ae6f9a, cell `FE-s-37`.
<owned_cells>FE-s-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F37-AC1` .. `F37-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-37.governing-order-binding.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F37-AC1,F37-AC2,F37-AC3,F37-AC4,F37-AC5,F37-AC6,F37-AC7,F37-AC8,F37-AC9` BEFORE the `complete` flip -- with the checker your own change produced. `F37-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `governing-order-binding.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the flip path: RUN by the issuer at CLOUD 6462e98cc6 -- check_complete_flip at to-pipeline-gate.py:2469 runs subprocess.run(["python", chk, inst]) with the instance only.
the governing order: RUN -- proof-of-spec-check.py:614-641 lets decomp_ref.to_ref win; _governing_rel at :1300; the CVO's doctored-to_ref measurement on FE-s-29's instance (row S61).
the batteries: RUN -- 3 of 63 .tools/tests files reference to_ref (count-bar, alignment, seeded); gate self-test 0 of 70, checker self-test 32 of 32 at the cut.
lane: the <paths> block IS the grant; no portal path.
</preflight>

Seating: slot ~4; READY ROOT, seated on a fresh worktree cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row S26).
