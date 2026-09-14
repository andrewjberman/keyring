# TO IRPT_FNTEND.TO-FE-s-33 -- fixtures that can show what their captures claim

<to_id>IRPT_FNTEND.TO-FE-s-33</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-33` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** FWD-3, FWD-5, FWD-11 (evidence) | **depends_on:** FE-s-29 (sequencing) | **slot:** ~2 | **rows:** W1-S51, W1-S52, W1-S53

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-33` -- **three fixtures emptied round 4's captures, each for a reason measured at portal DEV `c2eb8eb4`.**

- **W1-S51.** `fixtures/smoke/fe-s-18-frozen.json` carries **9 envelopes and a `status` on 0 of them**. The frozen report serves the Reporting screen, the export preview and the print route; with no `status`, its screen view falls back to the explicit unknown and shows a StatusPanel ("Uncertain") where the report should be. Give the envelopes each view reads a legitimate state and reason. ⚠ **Which state is a graded judgment** -- choose one the contract permits for a frozen, whole report, say why in the result file, and the CVO grades it.
- **W1-S52.** `__tests__/fe-s-18/gen-fixtures.ts:143` emits `parent_node_id: null` for every Holdings node, so the READY tree has no root to hang from and its donut and table render empty. Emit a tree with a real parent chain.
- **W1-S53.** `fixtures/smoke/fe-s-14-global.json` carries **2 keys and no holdings key**, so the Global view's Holdings tab reads Failed and no second firm is visible. Add Holdings envelopes for both firms the map already names.

⛔ **THE HAZARD THIS CELL CAN CREATE.** The three Holdings maps (`fe-s-18-holdings-{observed,target,missing-attribution}.json`) carry `status` members that **FE-s-26 hand-authored and the generator does not emit**. Regenerating them from a fixed generator would silently strip FE-s-26's repair. Either teach the generator to emit exactly those states or edit the maps' trees in place -- but FE-s-26's statuses survive, byte for byte, and its three tests stay green.

This cell does NOT re-take a capture.

### ACCEPTANCE

<criterion id="F33-AC1" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F33-AC1` -- the whole portal typechecks.

<criterion id="F33-AC2" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts</invocation><expect>FROZEN MAP, ENVELOPES A VIEW READS CARRYING status: (\d+) of \1(?![0-9])</expect></criterion>
`F33-AC2` -- W1-S51. The test prints the denominator: the frozen map's envelopes that any of the three paired views reads, and each one's state.

<criterion id="F33-AC3" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-18/paired.test.ts</invocation><expect>PAIRED: 1 report, 3 views</expect></criterion>
`F33-AC3` -- F18-AC2 still holds: the screen, preview and print maps carry one identical report body.

<criterion id="F33-AC4" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts</invocation><expect>HOLDINGS NODES WITHOUT A PARENT CHAIN TO A ROOT: 0(?![0-9])</expect></criterion>
`F33-AC4` -- W1-S52, read from the three Holdings maps as committed, with the node denominator printed.

<criterion id="F33-AC5" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts</invocation><expect>FE-s-26 STATUSES PRESERVED: 3 of 3(?![0-9])</expect></criterion>
`F33-AC5` -- the hazard. Each Holdings map's `status` equals the one FE-s-26 committed (read from history at portal commit `0c456933`, FE-s-26's drain; its fixture commit is `ed90ce2d` -- the workspace gitlink does not pin either), compared field by field.

<criterion id="F33-AC6" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts</invocation><expect>GLOBAL MAP CARRIES HOLDINGS FOR BOTH FIRMS: 2 of 2(?![0-9])</expect></criterion>
`F33-AC6` -- W1-S53. Each firm's Holdings envelope is a valid v1 envelope, checked with the same validator the other maps pass.

<criterion id="F33-AC7" cell_refs="FE-s-33" drives="none"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-18 src/pages/InvestorReporting/__tests__/fe-s-22 src/pages/InvestorReporting/__tests__/fe-s-26 src/pages/InvestorReporting/__tests__/fe-s-33</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F33-AC7` -- every folder that reads these maps stays green: FE-s-18's paired and manifest tests, FE-s-22's capture rule, FE-s-26's three, and yours. **PRECONDITION: none required.**

<criterion id="F33-AC8" cell_refs="FE-s-33" judgment="true" drives="none"/>
`F33-AC8` -- graded at L9: each state you chose is one the contract permits for that map's basis, and the frozen report's state is legitimate for a whole report. RECORD; NO VERDICT.

<expected_criteria>F33-AC1, F33-AC2, F33-AC3, F33-AC4, F33-AC5, F33-AC6, F33-AC7, F33-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **Under `fixtures/smoke/` you own the FIVE maps named in `<paths>` ONLY.** Every other map belongs to a terminal cell's evidence.
- ⛔ **NO CAPTURE.** You change maps; you take no screenshot and write nothing under any deliverables folder but your own. FE-s-18's captures stand as committed; the Holdings cell re-captures after you.
- ⛔ **A legitimate envelope, not a forced one.** Every state and reason you add is one the contract permits for that envelope; a state chosen to make a capture look right is not.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W2-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-target.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-missing-attribution.json
portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-33/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-33`.
<owned_cells>FE-s-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F33-AC1` .. `F33-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-33.fixture-reach.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F33-AC1,F33-AC2,F33-AC3,F33-AC4,F33-AC5,F33-AC6,F33-AC7,F33-AC8` BEFORE the `complete` flip. `F33-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `fixture-reach.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the gaps: RUN by the issuer at portal DEV c2eb8eb4 -- fe-s-18-frozen.json 9 envelopes, 0 with status; fe-s-14-global.json 2 keys, 0 holdings; gen-fixtures.ts:143 parent_node_id: null.
the hazard: RUN -- FE-s-26 hand-authored the Holdings maps' statuses (portal ed90ce2d); the generator does not emit them.
lane: the <paths> block IS the grant; five named maps, the generator, and a new test folder.
</preflight>

Seating: slot ~2; wave B -- seated only after FE-s-29 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
