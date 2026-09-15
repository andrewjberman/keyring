# TO IRPT_FNTEND.TO-FE-s-46 -- two slow tests carry their own timeouts, sized to what they measure

<to_id>IRPT_FNTEND.TO-FE-s-46</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-46` (round 8, v0.8 @734eb61ac1) | **outcome_ref:** FWD-1, FWD-11 (evidence) | **depends_on:** none | **slot:** ~1 | **rows:** C-S96 (W3-S33)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-46` -- **three tests pass on their content but can run past bun's 5000 ms default test timeout on a loaded box, and then a later cell's whole-suite census reads red for a reason that cell cannot fix inside its own grant.** This is row W3-S33, graduated by 3.0.0_SA_CVO as C-S96 and assigned to this seat's cut by `1.0.0_SA_CTO`'s round-7 analysis (msg 96865, item 7: "explicit per-test timeouts, sized to the costs you measured"). **The row named two tests. The issuer's round-8 probe found a THIRD** (decomp R8.1).

Measured by the issuer at portal DEV 1f3ce9f0:
- **The three tests.** Each is a `test(...)` call with NO timeout argument.
  - `F40-AC5`: `__tests__/fe-s-40/window.test.ts:253`, `test('every day of the covered years, re-derived from the frontier with is_trading_day', ...)`. It spawns python over four years of days.
  - `F41-AC2`'s control: `__tests__/fe-s-41/one-writer.test.ts:424`, `test('CONTROL -- a seeded second writer is found, directly and through a wrapper; a seeded reader is not', ...)`. It runs the whole-tree census three times.
  - **`F41-AC5`'s control (the third, added by FE-s-45 in round 7):** `__tests__/fe-s-41/one-writer.test.ts:791`, `test('CONTROL -- an UNCOMMITTED in-place edit naming perf-9 moves the checkout read and NOT the committed read', ...)`. It seeds and reverts an in-place edit through git.
- **Their cost.**
  - Loaded:
    - from row W3-S33's own runs: F40-AC5 took 5172 ms and then 5735 ms, and F41-AC2's control took 5875 ms;
    - from the issuer's two round-8 probe suite runs: F41-AC5's control took 5859 ms and 5812 ms.
    - Each printed its passing reading first, then timed out at 5000 ms. In both probe runs it was the suite's ONLY fail (559 pass, 18 skip, 1 fail of 578).
  - Unloaded, the issuer's runs at DEV 1f3ce9f0 (the file totals; bun prints no per-test time on a pass): `fe-s-40/window.test.ts` 2.20 s for 5 tests, and `fe-s-41/one-writer.test.ts` 7.19 s for 11 tests. Three consecutive runs each read 5/0 and 11/0.
- The loaded cost is past the default and the unloaded cost is under it, so a test's pass depends on the box's load, not on its content.

**THE REMEDY:** every test in those two files whose measured cost can reach the default carries an explicit per-test timeout (bun's third `test()` argument), sized from its measured loaded cost. The content of every test is unchanged.

### ACCEPTANCE

<criterion id="F46-AC1" cell_refs="FE-s-46" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F46-AC1` -- the whole portal typechecks.

<criterion id="F46-AC2" cell_refs="FE-s-46" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-46/timeouts.test.ts</invocation><expect>EVERY TEST IN THE TWO FILES MEASURED: (\d+) of \1(?![0-9])</expect></criterion>
`F46-AC2` -- the census, by subtraction over the two files.
- The test enumerates every `test(` call in the COMMITTED blobs (`git cat-file blob HEAD:<path>`) of `fe-s-40/window.test.ts` and `fe-s-41/one-writer.test.ts`, and prints the denominator.
- It prints each test's measured cost from a run of that file, taken with a reporter that records per-test time (for example `bun test --reporter=junit --reporter-outfile=<WS>/.scratch/<file>.xml`).
- The line reads `n of n` only when every enumerated test has a cost.

<criterion id="F46-AC3" cell_refs="FE-s-46" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-46/timeouts.test.ts</invocation><expect>EXPLICIT TIMEOUT ON EVERY TEST THAT CAN REACH THE DEFAULT: (\d+) of \1(?![0-9])</expect></criterion>
`F46-AC3` -- W3-S33, read from the COMMITTED blobs.
- "Can reach the default" means a measured cost of at least 2500 ms (half of 5000) on ANY recorded run, OR the test is one of the three named above. All three named tests are in the set whatever your own runs read.
- Each such test's third argument is at least 3 times its highest recorded cost, and at most 60000 ms, so a real hang still fails within a minute. For the three named tests the floor is 3 x 5875 ms = 17625 ms (the highest cost recorded for any of them), whatever your own runs read.
- The test prints each such test's name, its highest recorded cost and its timeout.

<criterion id="F46-AC4" cell_refs="FE-s-46" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-46/timeouts.test.ts</invocation><expect>A SEEDED 1 MS TIMEOUT FAILS THE SAME TEST: yes</expect></criterion>
`F46-AC4` -- the control, which shows bun honours the argument.
- A scratch copy under `<WS>/.scratch/` of F41-AC2's control test, with its timeout set to 1 ms, is run and FAILS on the timeout.
- The same copy with the committed timeout passes.
- An argument bun ignored would read the same both ways; this arm is the one that can say no.

<criterion id="F46-AC5" cell_refs="FE-s-46" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-46/timeouts.test.ts</invocation><expect>THE TWO FILES UNDER LOAD: 3 of 3 RUNS 0 FAIL(?![0-9])</expect></criterion>
`F46-AC5` -- exercised under load.
- The two files are run 3 times, each time concurrently with a load you generate: for example, 2 more copies of the same two files running at once.
- The test prints each run's per-test cost for the two named tests, and the load it generated.
- The BEFORE arm is recorded, not graded: the same load on the DEV 1f3ce9f0 blobs, with its fail count. A load timeout is probabilistic, so its absence on one run proves nothing.

<criterion id="F46-AC6" cell_refs="FE-s-46" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F46-AC6` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed.

<criterion id="F46-AC7" cell_refs="FE-s-46" judgment="true" drives="none"/>
`F46-AC7` -- graded at L9: a loaded box can no longer turn a later cell's census red through these two files, and every timeout is sized from a measured cost. RECORD; NO VERDICT.

<expected_criteria>F46-AC1, F46-AC2, F46-AC3, F46-AC4, F46-AC5, F46-AC6, F46-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`fe-s-40/window.test.ts` AND `fe-s-41/one-writer.test.ts` ARE YOURS FOR TIMEOUT ARGUMENTS ONLY.**
  - Add or change the third argument of a `test(...)` call, and nothing else.
  - No assertion, no printed line, no helper and no constant changes.
  - Paste the diff of each file into the result file, and show that it touches only `test(` lines.
- ⛔ **SIZE FROM A MEASUREMENT, NEVER A ROUND GUESS.** Every timeout cites the recorded cost it is 3 times, in the result file.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F46-AC6). A red test outside your grant is a BLOCKING row with the list, never an edit.
- ⛔ **NOT YOURS:** every other file under `fe-s-40/` and `fe-s-41/`; `state/tradingCalendar.ts`; `lib/trading_calendar.py`; the fixture maps; `package.json` and `bunfig.toml` (a global timeout would hide every other slow test, which is the opposite of this remedy).
- **RULING AC.** F46-AC2 and F46-AC3 read the committed blobs. Your load runs read the working tree, and that is deliberate: they exercise what runs.
- **Servers.** No dev server is needed. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run to a port you have measured closed (5261 is this slot's). A closed loopback port refuses in about 0.3 to 2 s here, so any probe timeout must exceed 2 s. Sibling slots use 5263 and 5265; never touch them.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`, starting at W1-S71. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-40/window.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-46/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.8 @734eb61ac1, cell `FE-s-46`.
<owned_cells>FE-s-46</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F46-AC1` .. `F46-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-46.per-test-timeouts-sized-to-cost.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F46-AC1,F46-AC2,F46-AC3,F46-AC4,F46-AC5,F46-AC6,F46-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-46.per-test-timeouts-sized-to-cost.md` BEFORE the `complete` flip. `F46-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `per-test-timeouts-sized-to-cost.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-7 analysis, msg 96865, no addendum).
the three tests: RUN by the issuer at portal DEV 1f3ce9f0 -- window.test.ts:253, one-writer.test.ts:424 and one-writer.test.ts:791, each a test() call with no timeout argument.
their cost: RUN -- unloaded file totals 2.20 s (5 tests) and 7.19 s (11 tests), 3 of 3 runs 5/0 and 11/0; loaded single-test readings 5172, 5735 and 5875 ms (row W3-S33's evidence) and 5859 and 5812 ms (F41-AC5's control, the issuer's two probe suite runs, each the suite's only fail).
the reach: RUN -- round 8's reach census by whole-suite probe (decomp R8.1): FE-s-47's and FE-s-48's changes each turn 0 tests red, and neither touches these files, so the cells are disjoint by file.
lane: the <paths> block IS the grant; timeout arguments only in the two named files; package.json and bunfig.toml excluded.
</preflight>

Seating: slot ~1; one wave -- round 8 has no dependency edge, seated on a fresh worktree pair cut from HEAD with the `<status>` flip committed BEFORE the pair is cut (row S26).
