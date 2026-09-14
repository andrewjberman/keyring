# TO IRPT_FNTEND.TO-FE-s-41 -- one writer per fixture map, and the narrative bound to its own revision

<to_id>IRPT_FNTEND.TO-FE-s-41</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~5</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-41` (round 6, v0.6 @d4d8ae6f9a) | **outcome_ref:** FWD-3, FWD-11 (evidence) | **depends_on:** FE-s-37 (sequencing) | **slot:** ~5 | **rows:** W2-S24, W2-S27

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-41` -- **a fixture map has two writers, and the frozen map's narrative speaks for another revision.** `1.0.0_SA_CTO` RULING W's fixture half (round-5 analysis @942e4ff992 s.3).

Measured by the issuer at portal DEV 741bb54b:
- **W2-S24.** `fixtures/smoke/fe-s-14-global.json` has two writers. `__tests__/fe-s-14/gen-maps.ts` rewrites it whole, with no Holdings (`writeFileSync` at `:94`); `__tests__/fe-s-33/gen-global-holdings.ts` adds FE-s-33's two Holdings envelopes to it (`GLOBAL_PATH` at `:57`). Run alone, the first silently deletes the second's envelopes. Round 5 disarmed that by DETECTION only (row S59: F33-AC6's test fails a stripped map), and the CTO calls detection alone the defect. **RULING W:** the map gets ONE writer, the fixture cell's; every other cell reads it.
- **W2-S27.** The frozen map's narrative names performance revision `perf-9` while the frozen report is `rev-49f-000091` (1 occurrence each in `fixtures/smoke/fe-s-18-frozen.json`). A narrative-on print would pair them. **RULING W:** the narrative is re-bound to its own performance fixture.
- **The Holdings maps inherit from the frozen map.** `__tests__/fe-s-18/gen-fixtures.ts` builds each `fe-s-18-holdings-*.json` from the whole frozen map (row W2-S26), so a change to the frozen map reaches them through that one generator -- run it, never hand-edit its output.

### ACCEPTANCE

<criterion id="F41-AC1" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F41-AC1` -- the whole portal typechecks.

<criterion id="F41-AC2" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts</invocation><expect>WRITERS OF fe-s-14-global.json: 1(?![0-9])</expect></criterion>
`F41-AC2` -- a census of every generator under `__tests__/` that writes the file, its denominator printed, with a positive control proving the census finds a seeded second writer.

<criterion id="F41-AC3" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts</invocation><expect>THE ONE WRITER EMITS HOLDINGS FOR BOTH FIRMS: 2 of 2(?![0-9])</expect></criterion>
`F41-AC3` -- the one writer, run into a scratch path, emits both firms' Holdings envelopes, each a valid v1 envelope.

<criterion id="F41-AC4" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts</invocation><expect>REGENERATED MAP EQUALS THE COMMITTED MAP: yes</expect></criterion>
`F41-AC4` -- the one writer's output, compared byte for byte with the committed `fe-s-14-global.json`.

<criterion id="F41-AC5" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts</invocation><expect>FROZEN NARRATIVE BOUND TO ITS OWN PERFORMANCE REVISION: rev-49f-000091</expect></criterion>
`F41-AC5` -- W2-S27, read from the committed frozen map and from each Holdings map generated from it.

<criterion id="F41-AC6" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-18/paired.test.ts</invocation><expect>PAIRED: 1 report, 3 views</expect></criterion>
`F41-AC6` -- F18-AC2 still holds on the re-bound frozen map.

<criterion id="F41-AC7" cell_refs="FE-s-41" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F41-AC7` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed.

<criterion id="F41-AC8" cell_refs="FE-s-41" judgment="true" drives="none"/>
`F41-AC8` -- graded at L9: no map in this cell's surfaces has a second writer, and the frozen map's narrative speaks for the report it is printed with. RECORD; NO VERDICT.

<expected_criteria>F41-AC1, F41-AC2, F41-AC3, F41-AC4, F41-AC5, F41-AC6, F41-AC7, F41-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **ONE WRITER, CHOSEN AND STATED.** Decide which generator writes `fe-s-14-global.json` and make the other compose into it or stop writing it -- never two writers kept in agreement by a rule someone must remember. Say in the result file which generator it is and why.
- ⛔ **A GENERATED MAP IS REGENERATED, NEVER HAND-EDITED.** The Holdings maps come from `__tests__/fe-s-18/gen-fixtures.ts`: run it after the frozen map's re-binding and commit what it writes. FE-s-26's Holdings statuses and FE-s-33's parented trees must survive byte for byte in the fields they own; prove it in the result file. The `'ADVISORY'` token stays as it is (FE-s-39 flags it; the enum is IRPT_BCKEND's).
- ⛔ **NO CAPTURE.** You change maps and generators; you take no screenshot.
- ⛔ **NOT YOURS:** every non-test source file (`contracts/`, `state/`, `tabs/`, `render/`, `export/`) and every other map under `fixtures/`.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F41-AC7). Any test outside your grant that your change turns red is a BLOCKING row with the list, never an edit.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`. Export `IRPT_FE_DEV_PORT` to a measured-closed port on every `bun test` run; never unset.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W5-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- ⛔ **AMENDMENT 1 (2.0.0_SA_COO~F, 2026-09-14, on row W5-S5; criteria unchanged).** The cut named four maps that inherit from the frozen map, and there are five. `__tests__/fe-s-32/holdings-no-answer.json` was copied by hand from the observed Holdings map and still names perf-9, so `fe-s-32/holdings-in-a-browser.test.ts:256` goes red once the narrative is re-bound. That file is now yours for ONE purpose:
  - it becomes a GENERATED map. `__tests__/fe-s-18/gen-fixtures.ts`, the one Holdings generator, writes it from the observed map with exactly the one difference the test at `:256` asserts. It is never hand-edited, and it carries the re-bound narrative like the other four.
  - `fe-s-32/holdings-in-a-browser.test.ts` is NOT yours: FE-s-39 holds it by its own amendment, for its classification reader only. If `:256`'s assertion itself would have to change, that is a BLOCKING row, never an edit.
  - Your portal worktree still carries 5 modified, unstaged files from the first run (row W5-S6). Never stage them; name each in the result file.
  - FE-s-38 has DRAINED into portal DEV, and DEV is merged into your portal branch. Export `IRPT_FE_DEV_PORT` to a measured-closed port on every `bun test` run, as before.
  - F41-AC7's whole suite must read 0 fail. It stays the census of record.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-no-answer.json
portal/src/pages/InvestorReporting/__tests__/fe-s-14/gen-maps.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-33/gen-global-holdings.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-target.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-missing-attribution.json
portal/src/pages/InvestorReporting/__tests__/fe-s-41/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.6 @d4d8ae6f9a, cell `FE-s-41`.
<owned_cells>FE-s-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F41-AC1` .. `F41-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-41.one-writer-per-map.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F41-AC1,F41-AC2,F41-AC3,F41-AC4,F41-AC5,F41-AC6,F41-AC7,F41-AC8` BEFORE the `complete` flip. `F41-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `one-writer-per-map.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the writers: RUN by the issuer at portal DEV 741bb54b -- gen-maps.ts writeFileSync of fe-s-14-global.json at :94; gen-global-holdings.ts GLOBAL_PATH at :57.
the narrative: RUN -- fe-s-18-frozen.json carries perf-9 once and rev-49f-000091 once.
the inheritance: RUN -- gen-fixtures.ts builds the three Holdings maps from the frozen map (row W2-S26).
lane: the <paths> block IS the grant; no non-test source file.
</preflight>

Seating: slot ~5; wave B -- seated only after FE-s-37 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
