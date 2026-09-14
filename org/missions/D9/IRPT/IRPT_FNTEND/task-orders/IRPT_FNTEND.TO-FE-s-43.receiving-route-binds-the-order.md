# TO IRPT_FNTEND.TO-FE-s-43 -- the L7->L8 receiving route binds the governing order

<to_id>IRPT_FNTEND.TO-FE-s-43</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-43` (round 7, v0.7 @0ad0ea1fa9) | **outcome_ref:** the evidence plane | **depends_on:** none | **slot:** ~4 | **rows:** C-S90 (W4-S14)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-43` -- **RULING S bound the flip, and the receiving route is still unbound.** This is `1.0.0_SA_CTO` RULING AA (round-6 analysis @4713211d87 s.3), on row W4-S14 as graduated by 3.0.0_SA_CVO (C-S90). The CVO's arm C showed an unbound call still steered by a doctored `to_ref` (record @3d8fda2d73, F37-AC9's qualification).

Measured by the issuer at CLOUD edac45e48c:
- `.tools/receiving-check.py` routes a proof-of-spec instance with `"proof-of-spec-check.py", lambda p: [p]` (`:71`), which passes the instance and nothing else.
  - `run_one` runs the tool and returns `ACCEPT` on rc=0.
  - So the receiving verdict comes from the order the instance's own `decomp_ref.to_ref` names.
  - The tool is a CTO lane's (`1.0.0_SA_CTO~Z`, @adfbe65590, 2026-09-10). RULING AA places its fix in this project's checker lineage (FE-s-29, FE-s-37).
- `.tools/proof-of-spec-check.py` already takes `--governing-order <order>` (FE-s-37, drained @13a3e28b95), and the flip gate passes it (`to-pipeline-gate.py:2543`).
- Census of `receiving-check` across the workspace:
  - the tool itself;
  - `.tools/prd-manifest-gate.py`, which mentions it;
  - `.claude/skills/canonical-flow/SKILL.md`, which documents the call;
  - 3.0.0_SA_CVO's historical deliverables and logs.
  **No `.tools/tests/` battery calls it.**

**THE BINDING:**
- The receiving seat passes the order it is handed, and the route hands that order to the checker as `--governing-order`.
- A proof instance received WITHOUT its order reads **NOT-BOUND**, never `ACCEPT`.
- Every other route (PRD, addendum, task order, surprise rows, register row) keeps its current behaviour.

### ACCEPTANCE

<criterion id="F43-AC1" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 180 python .tools/to-pipeline-gate.py --self-test</invocation><expect>RESULT: 0 arm\(s\) failed of</expect></criterion>
`F43-AC1` -- the gate's own self-test, every arm (0 of 72 failed at the cut).

<criterion id="F43-AC2" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 180 python .tools/proof-of-spec-check.py --self-test</invocation><expect>RESULT: (\d+) of \1 arm\(s\) behaved</expect></criterion>
`F43-AC2` -- the checker's own self-test (42 of 42 at the cut). The checker is not yours, and this proves you did not need it.

<criterion id="F43-AC3" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_receiving_binding.py</invocation><expect>DOCTORED to_ref, BOUND THROUGH THE RECEIVING ROUTE: HAND BACK</expect></criterion>
`F43-AC3` -- **the arm the ruling exists for.** FE-s-29's committed instance, with `decomp_ref.to_ref` doctored to the real `IRPT_FNTEND.TO-FE-s-28.*` order, is handed to `receiving-check.py` together with FE-s-29's own order, and it is handed back.

<criterion id="F43-AC4" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_receiving_binding.py</invocation><expect>THE HAND-BACK NAMES BOTH PATHS: yes</expect></criterion>
`F43-AC4` -- the printed hand-back carries the checker's violation naming the order handed over and the order `to_ref` declared.

<criterion id="F43-AC5" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_receiving_binding.py</invocation><expect>UNBOUND INSTANCE THROUGH THE RECEIVING ROUTE: NOT-BOUND</expect></criterion>
`F43-AC5` -- the SAME doctored instance, received with no order, reads NOT-BOUND. It must not read ACCEPT, and it must not read a verdict the instance steered.

<criterion id="F43-AC6" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_receiving_binding.py</invocation><expect>POSITIVE CONTROL, FE-s-29 AS COMMITTED, BOUND: ACCEPT</expect></criterion>
`F43-AC6` -- the committed instance with its own order reads ACCEPT. Without this arm, AC3 is indistinguishable from refusing everything.

<criterion id="F43-AC7" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 600 python .tools/tests/test_receiving_binding.py</invocation><expect>EVERY OTHER ROUTE UNCHANGED: (\d+) of \1(?![0-9])</expect></criterion>
`F43-AC7` -- each non-proof route classifies a committed example of its own artifact type and builds the same argv as at the cut. The denominator and each route are printed.

<criterion id="F43-AC8" cell_refs="FE-s-43" drives="none"><invocation>cd <WS> && timeout 900 python .tools/tests/test_governing_binding.py</invocation><expect>EVERY .tools BATTERY THAT CALLS EITHER TOOL: (\d+) of \1 green(?![0-9])</expect></criterion>
`F43-AC8` -- **the whole-suite census of record**. This is FE-s-37's census battery, run once with your change applied.

<criterion id="F43-AC9" cell_refs="FE-s-43" judgment="true" drives="none"/>
`F43-AC9` -- graded at L9: the L7->L8 receiving route binds the order it is handed, and no receiving verdict is ACCEPT on an unbound instance. RECORD; NO VERDICT.

<expected_criteria>F43-AC1, F43-AC2, F43-AC3, F43-AC4, F43-AC5, F43-AC6, F43-AC7, F43-AC8, F43-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override. You touch no portal path.
- ⛔ **CONTROLS FROM REAL SHAPES.** The doctored arm is FE-s-29's committed instance and FE-s-28's committed order, read by `git show`. RULING AC: every file your battery inspects is read as the committed blob, never a string you typed.
- ⛔ **CALL THE INSTRUMENT.** Test the binding through `receiving-check.py`'s own CLI and its `run_one`. Never re-derive its dispatch table.
- ⛔ **NOT YOURS:**
  - `.tools/proof-of-spec-check.py`: it already takes `--governing-order`; FE-s-44 may change it this round.
  - `.tools/to-pipeline-gate.py`.
  - Every existing file in `.tools/tests/`.
  - `.claude/skills/canonical-flow/SKILL.md`: it documents the receiving call. Put the exact change it needs in the result file and in ONE row, for that skill's owner.
  - 3.0.0_SA_CVO's intake and audit scripts: that seat binds its own.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F43-AC8). A battery your change turns red that is outside your grant is a BLOCKING row with the list, never an edit.
- **Anchors.** Counts your tests print are anchorable: left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
- **Evidence hygiene.** Each row's `output_evidence` carries the deciding invocation's output only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Commit** with `.tools/safe-commit.sh --author "<your serial> <<your serial>@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool or python. A `.py` edit passes `commit-gate.sh`. Verify every commit by `git log`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W4-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<paths>
.tools/receiving-check.py
.tools/tests/test_receiving_binding.py
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.7 @0ad0ea1fa9, cell `FE-s-43`.
<owned_cells>FE-s-43</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F43-AC1` .. `F43-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-43.receiving-route-binds-the-order.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F43-AC1,F43-AC2,F43-AC3,F43-AC4,F43-AC5,F43-AC6,F43-AC7,F43-AC8,F43-AC9` BEFORE the `complete` flip. `F43-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `receiving-route-binds-the-order.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-6 analysis s.1, no addendum).
the receiving route: RUN by the issuer at CLOUD edac45e48c -- receiving-check.py:71 builds [instance] only; run_one returns ACCEPT on rc=0.
the checker's binding: RUN -- proof-of-spec-check.py takes --governing-order since FE-s-37 (13a3e28b95); to-pipeline-gate.py:2543 passes it on the flip.
the consumers: RUN -- receiving-check named in .tools/receiving-check.py, .tools/prd-manifest-gate.py, .claude/skills/canonical-flow/SKILL.md and historical CVO records; no .tools/tests battery calls it.
instruments at the cut: RUN -- to-pipeline-gate --self-test 0 of 72 failed; proof-of-spec-check --self-test 42 of 42 (CLOUD edac45e48c).
lane: the <paths> block IS the grant; no portal path; the checker, the gate and the canonical-flow skill excluded.
</preflight>

Seating: slot ~4; one wave -- round 7 has no dependency edge, seated on a fresh worktree cut from HEAD with the `<status>` flip committed BEFORE the worktree is cut (row S26).
