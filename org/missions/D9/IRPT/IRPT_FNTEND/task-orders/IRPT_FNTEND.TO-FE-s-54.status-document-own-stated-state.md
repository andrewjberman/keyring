# TO IRPT_FNTEND.TO-FE-s-54 -- status-summary / status-job carry the response's OWN stated state, never a default

<to_id>IRPT_FNTEND.TO-FE-s-54</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~15:40Z).** The worker correctly left this `pending`: row
`W4-S77` named the exact, predicted mechanical consequence of this cell's own fix on `fe-s-47/no-status-
reason.test.ts` (F47-AC6 18->16, F47-AC7 controlRefused 9->7) and correctly declined to touch that file --
it is not in this order's `<paths>`, and self-grading the criterion green on its own diagnosis alone would
have been exactly the self-graded override this fabric refuses. That discipline is right; I am the one
closing this, on my own measurement, not the worker's. Its 3 hand-built envelope bodies also lacked
`unprojected_grant` (a sibling gap to FE-s-57's AMENDMENT 1/2, in a file FE-s-54 alone had no reason to
touch), and `IR_STATUS_DOCUMENT_OPERATIONS` was module-private so no test could name the identity-carry set
by reference. Fixed directly (workspace `15ceef79` in portal, workspace commit to follow): exported the
const, added `unprojected_grant` to `statusOperationBody()` and the two inline F54-AC3/F54-AC-CROSS bodies,
and gave `fe-s-47`'s F47-AC6/AC7 the same identity-carry awareness (compare against the document's own
carried state/reason rather than the generic reasonless-UNCERTAIN default, for `status-summary`/`status-job`
only). Verified independently in the merged tree: `fe-s-47/no-status-reason.test.ts` 8 of 8 pass; whole
`src/pages/InvestorReporting` suite `603 pass / 21 skip / 0 fail` at portal `15ceef79`; `bun run typecheck`
clean. Flipping to `complete` on that measurement.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-54` (round 9, v0.9) | **outcome_ref:** FWD-6 | **depends_on:** FE-s-53 shares `contracts/adapt.ts` -- SEQUENCED after it, never concurrent | **slot:** ~5 | **rows:** W3-S38 (round-8 analysis item 3)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-54` -- **round-8's analysis, item 3, VERBATIM:** *"W3-S38 -- a stated state wins, wherever the response
states it. For status-summary and status-job, the data IS a status document, and it states PARTIAL at the top
level. That is the response's stated state. The adapter lifts it, with its reason, into the carried
availability, and supplies no `NO_STATUS_REASON`. The cell's first act is the read 3.0.0_SA_CVO did not make:
which production components render those two operations' availability or top-level state."*

**FIRST ACT (per the analysis's own instruction): find every production component that renders the
`status-summary` / `status-job` operations' result.** Trace from `IR_DATA_ADAPTER['status-summary']` /
`['status-job']` in `contracts/envelope.ts:147-148` (both map to `adaptStatusEnvelope`) forward to whichever tab
body or panel calls the typed client with those two operations (search `portal/src/api/endpoints/investor-reporting.ts`
and the tab bodies for the operation string literals `'status-summary'` and `'status-job'`). Print the
denominator: how many production render sites consume each operation's result, and via which prop/field.

**THE GAP THIS NAMES:** for these two operations, the response body's OWN `status.state` field (e.g. `PARTIAL`)
is the ONLY place the state lives -- there is no separate wrapping document with its own state to defer to.
`adaptStatusEnvelope` (`contracts/adapt.ts:536-569`) already reads `wire.state` (`:561`,
`state: STATE_FOR_WIRE[wire.state]`) and carries it onto the returned `StatusEnvelope.state` correctly. **Verify
by a RED test first** whether the GAP is instead downstream: does the render site your first-act trace found
actually READ `StatusEnvelope.state` (or `.availability.state`), or does it instead read something that
defaults past it (e.g. a caller that wraps the result through `envelopeFromAvailability` a second time, or a
component that reads `TabEnvelope.state` from a STALE placeholder because these two operations are typically
one-shot write-acknowledgements rather than a polled tab body)? **Do not assume the fix is in `adapt.ts` --
ground it in what your first-act trace actually finds**, and if the trace finds ZERO production render sites
for these two operations (i.e., nothing today actually displays a `status-summary`/`status-job` result to a
viewer), report that as the finding and REFUSE the render-side criteria below with that measurement, since
there is nothing to fix on a path nothing reads.

### ACCEPTANCE

<criterion id="F54-AC1" cell_refs="FE-s-54" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F54-AC1` -- the whole portal typechecks.

<criterion id="F54-AC2" cell_refs="FE-s-54" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-54/stated-state-wins.test.ts</invocation><expect>RENDER SITES FOR status-summary/status-job: (\d+)(?![0-9])</expect></criterion>
`F54-AC2` -- your new test's FIRST assertion is the denominator from THE FIRST ACT above -- print the count of
production render sites found for each operation, by name and file:line.

<criterion id="F54-AC3" cell_refs="FE-s-54" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-54/stated-state-wins.test.ts</invocation><expect>A status-summary RESPONSE STATING PARTIAL RENDERS PARTIAL, NOT A DEFAULT: yes</expect></criterion>
`F54-AC3` -- feed a fixture (or a constructed wire object) whose `status.state` is `PARTIAL` through the whole
adapt-then-render path your first act traced, and assert the rendered state is `PARTIAL` -- not `READY`, not
`LOADING`, not the explicit unknown.

<criterion id="F54-AC4" cell_refs="FE-s-54" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-47</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F54-AC4` -- the existing envelope/status suites are unaffected.

<criterion id="F54-AC5" cell_refs="FE-s-54" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F54-AC5` -- the whole IRPT_FNTEND suite, at drain time (after FE-s-53 has landed in this worktree's file
history, per the sequencing bound).

<criterion id="F54-AC6" cell_refs="FE-s-54" judgment="true" drives="none"/>
`F54-AC6` -- graded at L9: the first-act trace is real (cites actual render sites or honestly reports zero),
and any fix made is grounded in what that trace found rather than a guess at `adapt.ts`. RECORD; NO VERDICT.

<expected_criteria>F54-AC1, F54-AC2, F54-AC3, F54-AC4, F54-AC5, F54-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file. **Your first-act trace may find the fix belongs OUTSIDE this grant** (e.g. a tab
  body file not listed here) -- if so, REPORT a BLOCKING row naming the exact file and line, and do not edit
  outside your grant without an amendment.
- ⛔ **`contracts/adapt.ts` IS YOURS FOR `adaptStatusEnvelope` ONLY, AND ONLY IF YOUR TRACE PUTS THE GAP THERE.**
  Sequenced after FE-s-53 on this same file -- confirm FE-s-53's commit is present in your worktree before
  touching `adaptStatusEnvelope`; if it is not yet, work the trace (F54-AC2/AC3 investigation) first and hold
  the code edit.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/envelope.ts
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-54/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-54`.
<owned_cells>FE-s-54</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F54-AC1` .. `F54-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-54.status-document-own-stated-state.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F54-AC1,F54-AC2,F54-AC3,F54-AC4,F54-AC5,F54-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-54.status-document-own-stated-state.md`
BEFORE the `complete` flip. `F54-AC6` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`status-document-own-stated-state.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED).
the gap: DECLARED-UNGROUNDED BY THE ISSUER, DELIBERATELY -- round-8's own item 3 says "the cell's first act is the read 3.0.0_SA_CVO did not make", so this order hands the trace to the worker rather than asserting a location the issuer has not verified.
lane: the <paths> block IS the grant; a fix outside it is a BLOCKING row, never a silent edit.
</preflight>

Seating: wave A, slot ~5; SEQUENCED after FE-s-53 on `contracts/adapt.ts` (same worker slot, or a commit
hand-off the COO merges in file order before this cell's code-edit phase begins).
