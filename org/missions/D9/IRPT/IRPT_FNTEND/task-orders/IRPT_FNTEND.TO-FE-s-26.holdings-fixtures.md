# TO IRPT_FNTEND.TO-FE-s-26 -- three fixtures that can actually differ at the view

<to_id>IRPT_FNTEND.TO-FE-s-26</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE; F6) | **Decomp cell:** `FE-s-26` (round 4, v0.4 @1d9839797c) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** none -- READY ROOT | **slot:** ~2 | **rows:** S44, C-S46, W1-S33 (residual)

---

## WORKER FACE

### THE CELL

`FE-s-26` -- **`F18-AC3` has failed for two consecutive rounds and the reason is not the code.**

`FE-s-18` was ordered to capture the Holdings tab on three bases -- observed custody, target blend, and a node whose attribution is unavailable -- and its three captures came out **BYTE-IDENTICAL** (`sha256 8ce52e6ad0b60e29...`). Round 3 fixed the seam that made the bodies unable to mount at all, and the three captures STILL cannot differ, because:

**Measured twice independently -- issuer 84 v1 envelopes across 36 smoke maps with 3 carrying a `status` member; a worker at a narrower scope 62/16/3 -- and the three Holdings maps read `envelopes=9, with_status=0` EACH.**

`status` is the only wire carrier of a state on this plane. Three fixtures with no `status` render three identical panels **BY THE CONTRACT**, however correct the code is.

**Give each of the three maps a `status` that makes its own basis visible at the view.** The three are `fixtures/smoke/fe-s-18-holdings-observed.json`, `...-target.json` and `...-missing-attribution.json`. Each must be a legitimate v1 envelope -- you are supplying a state the wire may genuinely carry, not inventing a field to force a pixel difference.

⛔ **AND PROVE THE SET IS NO LONGER DEFECTIVE USING THE INSTRUMENT THAT ALREADY EXISTS.** `FE-s-22` built the scoped capture-hash rule with a third limb after measuring: *a fixture that does not carry the claimed field is a DEFECTIVE FIXTURE, not an admitted collision* -- now ruling E. Use it. Do not re-derive it, and do not write a second copy of it.

⛔ **THIS CELL TAKES NO CAPTURE AND DOES NOT TOUCH `__tests__/fe-s-18/`.** `FE-s-18` is CARRIED with `F18-AC3` and `F18-AC17` UNTOUCHED (ruling B: *not amended, not re-scoped, not passed with a caveat*) and re-runs itself after you drain. Your job is to make its existing criteria satisfiable, not to satisfy them.

### ACCEPTANCE

<criterion id="F26-AC1" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F26-AC1` -- the whole portal typechecks. No environmental precondition.

<criterion id="F26-AC2" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26/fixtures-carry-status.test.ts</invocation><expect>HOLDINGS MAPS CARRYING status: 3 of 3</expect></criterion>
`F26-AC2` -- all three Holdings maps now carry a `status` member on the holdings envelope, printed per map with its state. The denominator is the three maps, named.

<criterion id="F26-AC3" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26/fixtures-carry-status.test.ts</invocation><expect>STATES DISTINCT ACROSS THE THREE: 3 of 3</expect></criterion>
`F26-AC3` -- the three states differ from one another. Three fixtures carrying the SAME state would satisfy AC2 and reproduce the original defect exactly.

<criterion id="F26-AC4" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26/fixtures-carry-status.test.ts</invocation><expect>ENVELOPES STILL VALID: 27 of 27</expect></criterion>
`F26-AC4` -- every envelope in the three maps still validates against the v1 contract. Nine per map; a fixture that stopped being a legal envelope would trade one defect for a worse one.

<criterion id="F26-AC5" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26/not-defective.test.ts</invocation><expect>DEFECTIVE FIXTURES: 0 of 3</expect></criterion>
`F26-AC5` -- run through `FE-s-22`'s existing scoped rule, the set is NO LONGER DEFECTIVE: each fixture now carries the field its capture claims to render. Import that rule; do not reimplement it.

<criterion id="F26-AC6" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26/not-defective.test.ts</invocation><expect>RULE IS IMPORTED, NOT COPIED: 1 module</expect></criterion>
`F26-AC6` -- the test imports `FE-s-22`'s module rather than carrying its own copy, printed with the resolved module path. Two copies of an evidence rule drift, and the drift is invisible.

<criterion id="F26-AC7" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26/renders-differently.test.ts</invocation><expect>PANELS DISTINCT: 3 of 3</expect></criterion>
`F26-AC7` -- **the arm that makes the rest mean anything.** The three fixtures, driven through the adapter to the view, produce THREE DIFFERENT rendered outputs. A fixture difference the view does not surface leaves `F18-AC3` exactly where it was. **PRECONDITION: none -- this is a pure render assertion, not a browser capture.**

<criterion id="F26-AC8" cell_refs="FE-s-26"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26 src/pages/InvestorReporting/__tests__/fe-s-22</invocation><expect>0 fail</expect></criterion>
`F26-AC8` -- your own folder and the rule's own folder are both green, proving you did not change the rule's behaviour by using it. **PRECONDITION: none; both are pure bun tests.** ⛔ This order carries NO whole-suite bar (ruling C).

<criterion id="F26-AC9" cell_refs="FE-s-26" judgment="true"/>
`F26-AC9` -- graded at L9: each fixture's state is one the wire may genuinely carry for that basis, and none was chosen merely to force a difference. RECORD; NO VERDICT.

<expected_criteria>F26-AC1, F26-AC2, F26-AC3, F26-AC4, F26-AC5, F26-AC6, F26-AC7, F26-AC8, F26-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. ⛔ **`__tests__/fe-s-18/` IS NOT IN YOUR GRANT AND YOU TAKE NO CAPTURE.** A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **Under `fixtures/smoke/` you own THE THREE HOLDINGS MAPS ONLY.** Other maps in that directory belong to terminal cells and to `FE-s-18`'s carried criteria; changing one would move another cell's evidence under it.
- **A legitimate envelope, not a forced difference.** The state you give each map must be one the contract permits for that basis. If no legitimate state distinguishes two of the three, that is a `BLOCKING` row naming which two and why -- a real and useful finding, not a failure.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W2-S<k>`. ⛔ **Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) for the last W2 id before minting** -- the gate allocates across both and this face names no starting number by design (row S36). Write with `newline='\n'` and READ THE DIFFSTAT of your commit (row S47).
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-target.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-missing-attribution.json
portal/src/pages/InvestorReporting/__tests__/fe-s-26/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.4 @1d9839797c, cell `FE-s-26`.
<owned_cells>FE-s-26</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F26-AC1` .. `F26-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-26.holdings-fixtures.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F26-AC1,F26-AC2,F26-AC3,F26-AC4,F26-AC5,F26-AC6,F26-AC7,F26-AC8,F26-AC9` BEFORE the `complete` flip. `F26-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `holdings-fixtures.result.md` beside it, naming the state given to each map and why it is legitimate for that basis. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the gap: RUN by the issuer, twice and independently of the worker who first found it -- 84 v1 envelopes across 36 smoke maps carry `status` in 3 cases; fe-s-18-holdings-{observed,target,missing-attribution}.json read envelopes=9 with_status=0 EACH.
the instrument: RUN -- FE-s-22's scoped rule is live at HEAD and its third limb (defective fixture vs admitted collision) is ruling E. This cell uses it and writes no second copy.
ruling: RUN -- ruling B carries FE-s-18 untouched for a SECOND round, which is why this cell makes its criteria satisfiable rather than satisfying them.
lane: the <paths> block IS the grant and names THREE fixture files individually rather than the directory, because the directory holds other cells' evidence.
</preflight>

Seating: slot ~2; READY ROOT, seated at issuance on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row S26).
