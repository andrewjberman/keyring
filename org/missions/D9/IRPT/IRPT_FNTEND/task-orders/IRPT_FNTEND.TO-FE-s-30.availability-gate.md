# TO IRPT_FNTEND.TO-FE-s-30 -- one availability gate, on the report, and Reporting under it

<to_id>IRPT_FNTEND.TO-FE-s-30</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F4, F7; CONTRACTS `StatusEnvelope` consumed) | **Decomp cell:** `FE-s-30` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** FWD-3, FWD-6 | **depends_on:** FE-s-29 (sequencing: the new checker must be in your worktree) | **slot:** ~1 | **rows:** C-S57, S30 (class)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-30` -- **the screens withhold three of the five answer-bearing states, and the PRD already says they must show them.**

Measured by the issuer at portal DEV `c2eb8eb4`: `tabs/reporting/ReportingTab.tsx:175` mounts the body only where `isCompleteState` (`state/status.ts:144`) admits -- READY and STALE. Its own docstring (`:14-19`) routes PARTIAL "and any other non-assertable state" to StatusPanel, and a test asserts it: a designed, tested choice, not an accident. The contract requires `business_date` on FIVE states that carry an answer: READY, PARTIAL, STALE, NEEDS_CORRECTION and UNCERTAIN. The PRD: FWD-3 *"a deliberately incomplete provider mapping yields a PARTIAL or UNSUPPORTED result rather than a full-client claim"*; FWD-5 *"missing attribution stays VISIBLE"*; FWD-6 *"an incomplete result never appears as a complete zero-valued report."* **Qualified and visible -- never hidden, never styled complete.**

`1.0.0_SA_CTO` ruling H, adopted:

1. ONE predicate over ONE object -- **the REPORT's availability** -- decides whether a body renders. Put it in a NEW module, `state/availability.ts`; Reporting uses it here, and the export and Holdings cells consume it after you.
2. The five answer-bearing states render the body, with the state, its reason and the `business_date` shown, and never styled as complete.
3. The four no-answer states (QUEUED, RUNNING, UNAVAILABLE, FAILED) render the status panel.
4. The body reads `business_date`, the field the contract requires on every answer-bearing state.

`isCompleteState` STAYS -- as the predicate for *shown as complete*. It stops being the predicate for *rendered at all*.

⛔ **THE PLANE, CONFIRMED BY 1.0.0_SA_CTO (96408).** The five are PRODUCER states. A body with NO wire state falls back to `EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'` (`contracts/adapt.ts:103`) -- the SAME view state as a producer's UNCERTAIN -- and it must never render as an answer. **Partition on `Availability.producerState` (`contracts/index.ts:127`, added by FE-s-25), never on the view's `EnvelopeState` alone.** F19-AC5 (`UNCERTAIN WITHOUT A WIRE STATE: 2 of 2`, graded as a status panel) stays green.

### ACCEPTANCE

<criterion id="F30-AC1" cell_refs="FE-s-30" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F30-AC1` -- the whole portal typechecks. No environmental precondition.

<criterion id="F30-AC2" cell_refs="FE-s-30" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-30/predicate.test.ts</invocation><expect>ANSWER-BEARING PRODUCER STATES -> BODY: 5 of 5(?![0-9])</expect></criterion>
`F30-AC2` -- the predicate over the producer's nine, printed with the producer enum as its denominator: READY, PARTIAL, STALE, NEEDS_CORRECTION, UNCERTAIN render a body.

<criterion id="F30-AC3" cell_refs="FE-s-30" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-30/predicate.test.ts</invocation><expect>NO-ANSWER PRODUCER STATES -> PANEL: 4 of 4(?![0-9])</expect></criterion>
`F30-AC3` -- QUEUED, RUNNING, UNAVAILABLE and FAILED render the panel.

<criterion id="F30-AC4" cell_refs="FE-s-30" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-30/predicate.test.ts</invocation><expect>NO WIRE STATE -> PANEL, NOT A BODY: 1 of 1(?![0-9])</expect></criterion>
`F30-AC4` -- the plane: an availability whose view state is `UNCERTAIN` and which carries no `producerState` renders the panel. The test prints both planes, so a reader can see which one was partitioned.

<criterion id="F30-AC5" cell_refs="FE-s-30" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-30/predicate.test.ts</invocation><expect>ONE PREDICATE: Reporting reads state/availability</expect></criterion>
`F30-AC5` -- a source read: Reporting's render decision is the predicate's, not a second copy of it.

<criterion id="F30-AC6" cell_refs="FE-s-30" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-30/reporting-in-a-browser.test.ts</invocation><expect>REPORTING UNDER THE GATE, IN A BROWSER: 4 of 4(?![0-9])</expect></criterion>
`F30-AC6` -- **the arm the ruling exists for, driven from a response in a real browser.** Four scenarios, served as v1 envelopes through the dev server: PARTIAL renders the body; producer UNCERTAIN renders the body; UNAVAILABLE renders the panel; a body with no wire state renders the panel. **PRECONDITION: a dev server** -- declared in the test's own output, read through FE-s-27's helper (`__tests__/fe-s-27/_dev-server.ts`); an absent server reports SKIPPED, never FAILED, and this criterion passes only with it present. Write your own scenario maps inside `__tests__/fe-s-30/`, the way `__tests__/fe-s-19/mounted-from-wire.test.ts` writes its own. Run the page under NODE.

<criterion id="F30-AC7" cell_refs="FE-s-30" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-30/reporting-in-a-browser.test.ts</invocation><expect>PARTIAL BODY SHOWS STATE, REASON AND business_date: yes</expect></criterion>
`F30-AC7` -- on the PARTIAL body, the state, its reason and the `business_date` are in the rendered page. The test prints the three values it found. Same precondition as AC6.

<criterion id="F30-AC8" cell_refs="FE-s-30" drives="none"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3 src/pages/InvestorReporting/__tests__/fe-s-5 src/pages/InvestorReporting/__tests__/fe-s-30</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F30-AC8` -- three folders green: fe-s-3 (whose `isCompleteState('PARTIAL') === false` STAYS true), fe-s-5 (re-pointed as the bounds say), and yours. **PRECONDITION: none required** -- your browser test reports SKIPPED without a server. Record which way you ran it.

<criterion id="F30-AC9" cell_refs="FE-s-30" judgment="true" drives="none"/>
`F30-AC9` -- graded at L9: a reader of the PARTIAL Reporting body can tell it is a qualified answer, not a complete one, and nothing on it is styled as complete. RECORD; NO VERDICT.

<expected_criteria>F30-AC1, F30-AC2, F30-AC3, F30-AC4, F30-AC5, F30-AC6, F30-AC7, F30-AC8, F30-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`state/status.ts` IS NOT YOURS** -- it is FE-s-34's this round, which relabels its age text. Your predicate lives in the NEW `state/availability.ts`. Read `status.ts`; never edit it. `isCompleteState` is unchanged.
- ⛔ **ONE TEST OF ANOTHER CELL IS YOURS, FOR ONE PURPOSE: `__tests__/fe-s-5/states.test.ts`.** It asserts, by its own docstring, the behaviour ruling H overturns: PARTIAL routes to StatusPanel. Change ONLY the claims ruling H changes -- a PARTIAL (and each other answer-bearing) report now renders the body, qualified -- cite ruling H beside each changed assertion, and leave every other assertion as written. Anything else that file needs is a row.
- ⛔ **DO NOT STYLE A QUALIFIED ANSWER AS COMPLETE.** `isCompleteState` still decides "shown complete". A PARTIAL body carries its qualification visibly and never the complete path's presentation.
- ⛔ **`scripts/ui-smoke.mjs` IS NOT YOURS.** Drive the browser the way fe-s-19 does, under node, from your own test.
- **The precondition is declared, never silent.** A browser criterion names its dev-server precondition in its own output and reports SKIPPED when it is absent (ruling C).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port>`, export it as `IRPT_FE_DEV_PORT` (the variable `__tests__/fe-s-27/_dev-server.ts` reads; its default is 5181), and **kill it before your final report**. Say in the result file which criteria were measured with it up and which with it down.
- ⚠ **`chromium.launch` fails under bun on this box**; the identical launch under node returns in seconds.
- **Anchors and evidence.** Counts your tests print are anchorable (`(?<![0-9])`, `(?![0-9])`); each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/state/availability.ts
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/__tests__/fe-s-5/states.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-30/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-30`.
<owned_cells>FE-s-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F30-AC1` .. `F30-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-30.availability-gate.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F30-AC1,F30-AC2,F30-AC3,F30-AC4,F30-AC5,F30-AC6,F30-AC7,F30-AC8,F30-AC9` BEFORE the `complete` flip. `F30-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `availability-gate.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the gate: RUN by the issuer at portal DEV c2eb8eb4 -- ReportingTab.tsx:175 via isCompleteState (status.ts:144, READY and STALE); docstring :14-19 routes PARTIAL to StatusPanel; HoldingsTab.tsx:90 READY-only; PrintEntry checks no report state.
the plane: RUN -- EXPLICIT_UNKNOWN_STATE='UNCERTAIN' at adapt.ts:103; Availability.producerState at contracts/index.ts:127; confirmed by 1.0.0_SA_CTO 96408.
overturned tests: RUN, by census of 19 files then read -- fe-s-5/states.test.ts asserts PARTIAL -> StatusPanel (granted); fe-s-3/status.test.ts isCompleteState('PARTIAL')===false stays; fe-s-19 F19-AC5 stays green by the plane rule.
lane: the <paths> block IS the grant; state/status.ts excluded (FE-s-34's).
</preflight>

Seating: slot ~1; wave B -- seated only after FE-s-29 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
