# TO IRPT_FNTEND.TO-FE-s-29 -- the checker limbs, at the head of the round

<to_id>IRPT_FNTEND.TO-FE-s-29</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-29` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** the evidence plane | **depends_on:** none -- READY ROOT | **slot:** ~4 | **rows:** S53, S56, W4-S7, S42 (substrate half), C-S67

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-29` -- **four checker limbs, landed before any other round-5 proof is checked.** You are editing the fabric's own grading instruments: every seat's L6 issuance passes through `.tools/to-pipeline-gate.py`, and every proof instance through `.tools/proof-of-spec-check.py`. A limb that refuses an honest input blocks other seats' work; a limb that admits a bad one is worse.

**Limb 1 -- the `<placeholders>` reader, line-anchored in BOTH readers, in ONE change** (`1.0.0_SA_CTO` ruling M(i); rows S53, W4-S7). Both files read the element with `<placeholders>(.*?)</placeholders>` under `re.S`, first match -- the gate at `.tools/to-pipeline-gate.py` (`PLACEHOLDERS_TAG_RE`) and the checker at `.tools/proof-of-spec-check.py` (`PLACEHOLDERS_TAG_RE`, near `:1125`). S53 measured it calling the gate's own function on real task-order bytes: it FALSE-ADMITS (C) an invocation token the real element does not declare, whenever the criteria sit between a prose mention and the element, and (D) an order with NO element whose prose quotes the gate's own help text. A line-anchored reader (`^[ \t]*<placeholders>(.*?)</placeholders>[ \t]*$` with `re.M`) closed both and still admitted the two orders that declare (FE-s-23, FE-s-28). The gate's self-test pins the two readers byte-identical on purpose -- keep that invariant.

**Limb 2 -- a count-bar PASS beside a contradicting count is refused** (ruling M(ii); row S56). The checker decides a mechanical criterion with `re.search(expect, output_evidence, re.S | re.M)` (`:106`) and raises nothing when that search matches. So a `0 fail` bar passes ` 10 fail` (shape a), and passes any evidence that also carries a contradicting count (shape b -- F17-AC8's committed evidence holds its deciding ` 0 fail` AND a BEFORE note's ` 1 fail`; 1.0.0_SA_CTO's live near-miss, and the reason evidence hygiene is now a bound). Refuse a PASS whose evidence carries a nonzero count for the noun a zero-count bar asserts: **REFUSE for new instances, ANNOUNCE for legacy**, in the frame the checker already uses for its legacy instances. ⛔ **Left-anchor counts with `(?<![0-9])`, NEVER `\b`** -- `\b4 passed` false-FAILS `\x1b[1m4 passed` because an ANSI code puts a word character before the count (1.0.0_SA_CTO 96370, tested with the grader's own call).

**Limb 3 -- the seeded-criterion limb, with a MANDATORY declaration** (ruling Q; S42's substrate half; C-S67). This portal has no DOM test environment, so under `renderToStaticMarkup` a body that MOUNTED and a body SEEDED through `initialEnvelope` / `initialHoldingsEnvelope` / `initialReport` are indistinguishable. A seeded criterion and a browser-driven criterion both invoke `bun test <file>` -- **only the invoked TEST FILE's content tells them apart**, which is why this limb lives in the checker. 1.0.0_SA_CTO's condition (@4f6c7abc7b), binding: **every NEW IRPT_FNTEND criterion declares `drives="network"` or `drives="none"` as an attribute of its criterion element; a new instance whose governing order has a criterion declaring NEITHER is REFUSED; legacy instances ANNOUNCE.** For a `drives="network"` criterion the limb refuses a PASS whose invoked test satisfies it by seeding. An explicit `none` is enforcement, not a waiver.

**Limb 4 -- gate (viii) grades a MODIFICATION of an order that already declares the element** (Andrew-direct card 6, ~18:4xZ 2026-09-13, recs approved, record @e2210bf34c). Today gate (viii) grades only orders STAGED AS ADDED (`to-pipeline-gate.py`, the staged-added set near `:925-944`). His ruling: it also grades an order staged as MODIFIED, **only if that order already declares `<placeholders>`**. Nothing is back-filled. Update the gate's own docstring (`:21-24`, PROSPECTIVE ONLY) to state the rule and its authority.

### ACCEPTANCE

<criterion id="F29-AC1" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 180 python .tools/to-pipeline-gate.py --self-test</invocation><expect>RESULT: 0 arm\(s\) failed of</expect></criterion>
`F29-AC1` -- the gate's own self-test, every arm (it read `RESULT: 0 arm(s) failed of 51` at the cut).

<criterion id="F29-AC2" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 180 python .tools/proof-of-spec-check.py --self-test</invocation><expect>RESULT: (\d+) of \1 arm\(s\) behaved</expect></criterion>
`F29-AC2` -- the checker's own self-test, every arm (it read `RESULT: 18 of 18 arm(s) behaved` at the cut). Add arms for limbs 2 and 3.

<criterion id="F29-AC3" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_placeholders_reader.py</invocation><expect>LINE-ANCHORED READER, BOTH READERS: 5 of 5 cases(?![0-9])</expect></criterion>
`F29-AC3` -- limb 1. S53's five cases, from REAL bytes, through BOTH readers: A (FE-s-28 as issued) admitted; E (FE-s-23 as issued) admitted; B (FE-s-27 with no element) refused; C (FE-s-28 plus an invocation `<PORT>` its element does not declare) refused; D (FE-s-27 plus a prose paragraph quoting the gate's own help text, still no element) refused. Build C and D from the real files and the gate's real emitted text, never from strings you chose.

<criterion id="F29-AC4" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_placeholders_reader.py</invocation><expect>READERS BYTE-IDENTICAL: yes</expect></criterion>
`F29-AC4` -- the gate's reader and the checker's reader are the same pattern, compared, not assumed.

<criterion id="F29-AC5" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_count_bar_limb.py</invocation><expect>CONTRADICTING COUNT, NEW INSTANCE: REFUSED (\d+) of \1(?![0-9])</expect></criterion>
`F29-AC5` -- limb 2's positive arm. At least shape (a) -- a REAL `bun test` summary whose fail count ends in 0 and is not 0 (produce it by running bun on a scratch suite of ten failing tests under `<WS>/.scratch/`) -- and shape (b) -- F17-AC8's committed evidence, read by `git show`, carried by a NEW instance -- are refused as new instances. Each case prints that the bar's own regex DOES match its evidence, so the refusal is the limb's and not the existing search's (a control refused for the wrong reason proves nothing -- S52).

<criterion id="F29-AC6" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_count_bar_limb.py</invocation><expect>GENUINE ZERO ADMITTED: (\d+) of \1(?![0-9])</expect></criterion>
`F29-AC6` -- limb 2's negative arm, the one that keeps it from being a brick: at least a plain ` 0 fail`, an ANSI-coloured genuine zero, and F18-AC17's pass-2 evidence (` 486 pass |  1 skip |  0 fail`) are admitted.

<criterion id="F29-AC7" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_count_bar_limb.py</invocation><expect>CONTRADICTING COUNT, LEGACY INSTANCE: ANNOUNCED, 0 violations</expect></criterion>
`F29-AC7` -- limb 2 is prospective. F17-AC8's committed instance (a genuine deciding `0 fail` with a BEFORE note carrying `1 fail` in its evidence -- 1.0.0_SA_CTO's live near-miss) ANNOUNCES and raises no violation.

<criterion id="F29-AC8" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_seeded_limb.py</invocation><expect>SEEDED CRITERIA REFUSED: (\d+) of \1(?![0-9])</expect></criterion>
`F29-AC8` -- limb 3's positive arm. The population is every existing criterion whose invocation runs one of the suites that seed `initialEnvelope` / `initialHoldingsEnvelope` / `initialReport` (measured at the cut: 6 test files -- `fe-s-5/{states,fields,controls}`, `fe-s-10/{tabs-mounted,parity}`, `fe-s-26/renders-differently`). Print the denominator and each criterion id, evaluated as if declared `drives="network"`.

<criterion id="F29-AC9" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_seeded_limb.py</invocation><expect>BROWSER CRITERIA ADMITTED: 2 of 2(?![0-9])</expect></criterion>
`F29-AC9` -- limb 3's negative arm: F19-AC4 and F19-AC5 (`__tests__/fe-s-19/mounted-from-wire.test.ts`, which drives a real browser under node) are admitted. A limb that cannot tell AC8's set from this one is not the limb.

<criterion id="F29-AC10" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_seeded_limb.py</invocation><expect>NEW INSTANCE, CRITERION DECLARING NEITHER: REFUSED</expect></criterion>
`F29-AC10` -- the CTO's condition. An instance governed by an order issued under this rule, with one criterion carrying no `drives=`, is refused. The same test prints the legacy side: every round-4 instance (FE-s-25, 26, 27, 28 and FE-s-18) re-checked ANNOUNCES with 0 violations.

<criterion id="F29-AC11" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_gate_viii_modify.py</invocation><expect>MODIFIED DECLARING ORDER, BROKEN DECLARATION: REFUSED</expect></criterion>
`F29-AC11` -- limb 4's positive arm, in a REAL git index: a real declaring order (FE-s-23 or FE-s-28) staged as MODIFIED with its declaration broken is refused.

<criterion id="F29-AC12" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_gate_viii_modify.py</invocation><expect>MODIFIED ORDER WITHOUT THE ELEMENT: NOT GRADED</expect></criterion>
`F29-AC12` -- limb 4's boundary: a real order that does not declare `<placeholders>`, staged as MODIFIED, is not graded. Nothing is back-filled.

<criterion id="F29-AC13" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_mandatory_placeholders.py</invocation><expect>EXISTING CORPUS STILL COMMITTABLE</expect></criterion>
`F29-AC13` -- FE-s-28's battery still green, on the corpus it counts.

<criterion id="F29-AC14" cell_refs="FE-s-29" drives="none"><invocation>cd <WS> && timeout 300 python .tools/tests/test_proof_of_spec_alignment.py</invocation><expect>BATTERY PASS</expect></criterion>
`F29-AC14` -- FE-s-23's alignment battery still green. It prints `BATTERY PASS` only on the branch where no arm failed.

<criterion id="F29-AC15" cell_refs="FE-s-29" judgment="true" drives="none"/>
`F29-AC15` -- graded at L9: each limb refuses what its ruling names and admits what it must, and none of the four can be satisfied by the party it grades. RECORD; NO VERDICT.

<expected_criteria>F29-AC1, F29-AC2, F29-AC3, F29-AC4, F29-AC5, F29-AC6, F29-AC7, F29-AC8, F29-AC9, F29-AC10, F29-AC11, F29-AC12, F29-AC13, F29-AC14, F29-AC15</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override. You touch no portal path.
- ⛔ **CONTROLS FROM REAL SHAPES.** Every positive control is built from real task orders, real proof instances and the tools' real emitted text -- never from a string you chose so that it passes. Round 4 had two positive controls pass for the wrong reason (S52: one fired on a bucket name in a comment; one read a commit after the thing it tested was retired). A detector that cannot go non-zero on the real positive case is a constant.
- ⛔ **CALL THE INSTRUMENT, never re-derive its rule.** Test each limb by calling the gate's and the checker's own functions or CLIs.
- **The legacy boundary is derived from repository state, never from a clock or a list**, and an issuer cannot enter the legacy side by omitting the declaration (that is the CTO's condition on limb 3). State the boundary you chose in the result file, with its NON-APPLICATION.
- **Keep the two readers byte-identical.** If you find the line-anchored pattern rejects a form a real declaring order uses, that is a BLOCKING row with the measurement -- not a looser pattern.
- **Anchors.** Every count your tests print is one a bar can anchor: left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
- **Evidence hygiene.** Each row's `output_evidence` carries the deciding invocation's output only; earlier runs go in `status_reason`.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. **Commit** with `.tools/safe-commit.sh --author "<your serial> <<your serial>@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool or python. A `.py` edit passes `commit-gate.sh` (py_compile, ds-precommit, ruff py39). Verify every commit by `git log`, never by exit code.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W4-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) for the last W4 id before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<paths>
.tools/to-pipeline-gate.py
.tools/proof-of-spec-check.py
.tools/tests/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-29`.
<owned_cells>FE-s-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F29-AC1` .. `F29-AC15`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F29-AC1,F29-AC2,F29-AC3,F29-AC4,F29-AC5,F29-AC6,F29-AC7,F29-AC8,F29-AC9,F29-AC10,F29-AC11,F29-AC12,F29-AC13,F29-AC14,F29-AC15` BEFORE the `complete` flip -- with the checker your own change produced. `F29-AC15` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `checker-limbs.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the readers: RUN by the issuer through the gate's own function on real bytes (S53) -- shipped reader false-admits cases C and D; line-anchored reader closes both, admits FE-s-23 and FE-s-28.
the grader: RUN -- proof-of-spec-check.py:104-116, re.search(expect, output_evidence, S|M); 0 false PASS across 648 instances estate-wide (1.0.0_SA_CTO 96370), 0 across this project's 72 recorded 0-fail rows (S56).
the seeded population: RUN -- 6 test files seed initialEnvelope/initialHoldingsEnvelope/initialReport (20 occurrences); the negatives F19-AC4/AC5 drive a real browser.
instruments at the cut: RUN -- to-pipeline-gate --self-test 0 of 51 failed; proof-of-spec-check --self-test 18 of 18; alignment battery BATTERY PASS; placeholders battery green.
lane: the <paths> block IS the grant; no portal path.
</preflight>

Seating: slot ~4; READY ROOT, seated on a fresh worktree cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row S26).
