# TO IRPT_FNTEND.TO-FE-s-27 -- an absent precondition is not a failure

<to_id>IRPT_FNTEND.TO-FE-s-27</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-27` (round 4, v0.4 @1d9839797c) | **outcome_ref:** the evidence plane | **depends_on:** none -- READY ROOT | **slot:** ~3 | **rows:** W1-S45, S48

---

## WORKER FACE

### THE CELL

`FE-s-27` -- **the same bytes, the same command, two different verdicts.**

Measured by the issuer at ONE commit on portal DEV `237a9027`:

```
  no dev server on 5181   ->   452 pass / 1 skip / 3 fail
  dev server on 5181      ->   454 pass / 1 skip / 1 fail
```

The delta is exactly `F19-AC4` and `F19-AC5`. `__tests__/fe-s-19/mounted-from-wire.test.ts` hard-codes `PORT = '5181'` and declares a precondition **no runner sees**, so:

- **A DOWN SERVER RENDERS AS A CODE DEFECT.** The failure output reads `driverStatus=1`, `slot=NO DRIVER LINE` -- indistinguishable, to anyone not already expecting it, from the seam being broken again. **The issuer made exactly this mistake once during round 3 and nearly reported a regression on it.**
- **A worker on any other slot's port cannot pass those two tests at all**, because the port is a literal.

The test's own note says a down server can never read as a PASS. That is true, and it is the harmless direction. The dangerous direction is its converse, which the note does not cover.

`1.0.0_SA_CTO` ruling C: **every criterion with an environmental precondition DECLARES it, and an absent precondition renders SKIPPED or BLOCKED, NEVER FAILED.** `3.0.0_SA_CVO`'s generalisation is law: *the criterion asserts the count as a property of the CUT when it is a property of the ENVIRONMENT.*

Make the precondition explicit, make its absence render as SKIPPED or BLOCKED rather than FAILED, and take the port from the environment rather than a literal so the tests are runnable from any slot.

⛔ **DO NOT WEAKEN WHAT THE TESTS ASSERT.** `F19-AC4`'s `BODIES MOUNTED: 2 of 2` and `F19-AC5`'s `UNCERTAIN WITHOUT A WIRE STATE: 2 of 2` are round 3's central evidence and must still be reachable and still fail when the seam is broken. You are changing how an ABSENT PRECONDITION reports, not what a PRESENT one proves.

### ACCEPTANCE

<criterion id="F27-AC1" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F27-AC1` -- the whole portal typechecks. No environmental precondition.

<criterion id="F27-AC2" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>PRECONDITION: dev server</expect></criterion>
`F27-AC2` -- the test DECLARES its precondition in its own output, naming what it needs and on which port, whether or not that precondition is met. **PRECONDITION: none for this criterion -- it passes in both worlds, which is the point.**

<criterion id="F27-AC3" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-27/precondition.test.ts</invocation><expect>ABSENT PRECONDITION: reported SKIPPED, 0 failures</expect></criterion>
`F27-AC3` -- **the arm the ruling exists for.** With no server reachable, the two browser tests report SKIPPED or BLOCKED and contribute **ZERO failures**. The test drives that state deliberately rather than waiting to observe it.

<criterion id="F27-AC4" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-27/precondition.test.ts</invocation><expect>PRESENT PRECONDITION: assertions still enforced</expect></criterion>
`F27-AC4` -- **the other arm, and without it AC3 is indistinguishable from deleting the tests.** With the precondition MET, the assertions still run and still fail on a seeded breakage. A skip that cannot become a real failure is a deleted test wearing a label.

<criterion id="F27-AC5" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-27/precondition.test.ts</invocation><expect>PORT FROM ENVIRONMENT: no literal</expect></criterion>
`F27-AC5` -- the port is read from the environment with a documented default; a source scan of `__tests__/fe-s-19/` for a hard-coded `5181` returns zero, printed with a POSITIVE CONTROL proving the scan fires on a seeded literal.

<criterion id="F27-AC6" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19 src/pages/InvestorReporting/__tests__/fe-s-27</invocation><expect>0 fail</expect></criterion>
`F27-AC6` -- both folders green. **PRECONDITION: NONE REQUIRED** -- after your change this must hold with NO dev server running, because the browser tests skip rather than fail. That is the whole deliverable, stated as a bar.

<criterion id="F27-AC7" cell_refs="FE-s-27"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-27/precondition.test.ts</invocation><expect>SKIPPED IS VISIBLE: named in the output</expect></criterion>
`F27-AC7` -- a skipped precondition is LOUD, not silent: the run names which criteria were skipped and why. A precondition that vanishes quietly converts a missing proof into an apparent pass, which is the opposite failure and the more expensive one.

<criterion id="F27-AC8" cell_refs="FE-s-27" judgment="true"/>
`F27-AC8` -- graded at L9: a reader of a run can tell "this was not exercised" from "this was exercised and held", without knowing the port. RECORD; NO VERDICT.

<expected_criteria>F27-AC1, F27-AC2, F27-AC3, F27-AC4, F27-AC5, F27-AC6, F27-AC7, F27-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **You own `__tests__/fe-s-19/` for THIS PURPOSE ONLY.** Do not change what `F19-AC2` through `F19-AC7` assert; round 3's negative-control evidence is recorded against those exact assertions. You change how an ABSENT precondition reports.
- ⛔ **`scripts/ui-smoke.mjs` IS NOT YOURS.** It is the whole portal's shared instrument and `FE-s-22` changed exactly one line of it last round. If your work needs a change there, that is a surprise row naming the line, not an edit.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** You will need one to prove `F27-AC4`. `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; **kill it before your final report, and say in the result file which criteria were measured with it up and which with it down** -- that distinction is this cell's entire subject.
- ⚠ **`chromium.launch` fails under bun on this box** (network-service crash, rc=124 at 180s) while the identical launch under node returns in seconds; round 3's driver runs under node, spawned by the bun test.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W3-S<k>`. ⛔ **Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) for the last W3 id before minting**; this face names no starting number by design (row S36). Write with `newline='\n'` and READ THE DIFFSTAT of your commit (row S47).
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-19/
portal/src/pages/InvestorReporting/__tests__/fe-s-27/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.4 @1d9839797c, cell `FE-s-27`.
<owned_cells>FE-s-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F27-AC1` .. `F27-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-27.declared-preconditions.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F27-AC1,F27-AC2,F27-AC3,F27-AC4,F27-AC5,F27-AC6,F27-AC7,F27-AC8` BEFORE the `complete` flip. `F27-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `declared-preconditions.result.md` beside it, recording the TWO-WAY measurement at one commit -- with the server and without -- because that pair is the cell's own proof. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the defect: RUN by the issuer TWO WAYS AT ONE COMMIT on portal DEV 237a9027 -- no server 452/1/3, server on 5181 454/1/1, delta exactly F19-AC4 and F19-AC5. Filed by 0.9.0_WK_IRPT_FNTEND~1 as W1-S45 and banked L9-critical by 3.0.0_SA_CVO.
the trap's shape: RUN -- the failure presents as `driverStatus=1` / `slot=NO DRIVER LINE`, which reads as a code defect; the issuer made that mistake once in round 3 and nearly reported a regression.
instrument: RUN -- chromium.launch fails under bun on this box and works under node; round 3's driver already runs under node, spawned by the bun test.
lane: the <paths> block IS the grant; __tests__/fe-s-19/ is granted for the PRECONDITION mechanism only, and scripts/ui-smoke.mjs is excluded because it is the whole portal's shared instrument.
</preflight>

Seating: slot ~3; READY ROOT, seated at issuance on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row S26).
