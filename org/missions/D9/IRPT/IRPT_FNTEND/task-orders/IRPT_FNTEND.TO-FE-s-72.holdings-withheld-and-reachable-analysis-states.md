# TO IRPT_FNTEND.TO-FE-s-72 -- which Analysis and Holdings states the current contract can reach, both widths, withheld included

<to_id>IRPT_FNTEND.TO-FE-s-72</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~22</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-72` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-65 (its --expect/--expect-text/--expect-ground flags) | **slot:** ~8 | **rows:** C-S129 | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-72` -- which Analysis and Holdings states the current contract can reach, both widths, withheld included.

**EVIDENCE ONLY: you write no component or test outside `__tests__/fe-s-72/`.** `listAnalysisRequests` unconditionally rejects with `NoDeclaredRoute` (`api/endpoints/investor-reporting.ts:1012-1013`) -- there is no wire route, and the CTO's ruling is that FNTEND must not invent one; the tab discloses this honestly (`requests-unavailable`). Because of that rejection, `AnalysisTab.tsx`'s `selectedRequest` can NEVER become non-null from a real fixture: it is set from `requests`, which starts empty and is populated only by `listAnalysisRequests` resolving, which structurally never happens. The five states gated on a selected request (`input-review`, `stage-display`, `variant-selector`, `revision-identity`, `native-sections`) are UNREACHABLE FROM THE BROWSER TODAY, not merely unbuilt -- do not claim otherwise, and do not try to fabricate a browser path to them. Prove the COMPONENTS work via the test-only seed props `AnalysisTab.tsx` already documents (`initialRequests`/`initialReport`, its own comment: "the live app never passes this"), and say plainly in your result that this is a DIFFERENT evidence class from a browser disclosure, not a substitute for one. Author `fixtures/withheld.json` from the wire-keyed `fe-s-18-holdings-observed.json` (byte copy of its three bodies, node index 2's `classification.authoritative` flipped false) to distinguish the WITHHELD state from the pre-existing out-of-enum ADVISORY token, which is already wired and not a defect this cell fixes.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** EVIDENCE ONLY: your own `__tests__/fe-s-72/` (including `fixtures/`). No component, no test outside it.

**THE CRITERION RULE (1.0.0_SA_CTO, round-10 analysis, binding on every VISUAL criterion this round).** A capture that reads the
right colour on the wrong page passed round 10 twice: the `CANVAS:` line read `document.body` while the print route's own container was
silver, and it printed the right value over an error page. So each visual state below carries ALL FOUR, and the cut refuses a state missing one:
**(a) WIRE MATCH** -- the fixture's keys equal the operation keys in `contracts/wire/consumed.ts`; the run prints `FIXTURES-MATCH: matched N of N`.
**(b) NAMED CONTENT** -- the specific cards, values or text the state must show, asserted by selector or text (`--expect`, `--expect-text`), never by eye.
**(c) A WRONG-STATE NEGATIVE CONTROL** -- the same content assertions run against the failed or unresolved state; they must print `ASSERT-CONTENT: 0 of N met`.
**(d) GROUND MEASURED ON THE ACTUAL CONTAINER** -- `--expect-ground` on the element that carries the surface, not the page field, with a wrong-ground control
(`--inject-css` a silver `#c4cbdb` onto that container; the same assertion must print `FAIL rgb(196, 203, 219)`).
A PNG is still read by you (a grep cannot see contrast), but it is now a JUDGMENT input, never the pass/fail line.

**THE INSTRUMENT (built by FE-s-65; your worktree already carries it -- if `ui-smoke.mjs` refuses `--expect` as an unknown flag, STOP: your base is wrong, report it).**
Additive flags on `scripts/ui-smoke.mjs` (repeatable; quote each argument with single quotes; a selector is CSS, so `[data-slot="reporting-body"]` is a selector):
- `--expect '<css>'` prints `EXPECT[<css>]: PASS (<n> visible)` or `EXPECT[<css>]: FAIL (0 visible)`.
- `--expect-text '<css>::<text>'` (case-sensitive substring of the FIRST match's `innerText`, which is AFTER CSS `text-transform`) prints `EXPECT-TEXT[<css>::<text>]: PASS|FAIL`.
- `--expect-style '<css>::<property><op><value>'` (`=` or `!=`; computed style of the FIRST match, exact string) prints `EXPECT-STYLE[<css>::<property>]: PASS|FAIL <actual>`.
- `--expect-ground '<css>=<rgb(r, g, b)>'` (the nearest NON-TRANSPARENT background walking up from the first match) prints `EXPECT-GROUND[<css>]: PASS|FAIL <actual>`.
- `--inject-css '<css text>'` adds a `<style>` after load and before the expectations: it builds a wrong-state control and nothing else.
- `--delay '<url-substring>=<ms>'` (repeatable) holds a matching fixture response for `<ms>` before fulfilling it (evaluated alongside `--fail`, same longest-substring match rule): the tool it takes to construct an IN-FLIGHT state (a submit that has not yet resolved) deterministically, without a real backend. Prints `DELAYED: <key> (<ms>ms)` when it fires.
- Summary lines `ASSERT-CONTENT: <met> of <total> met`, `ASSERT-STYLE: ...`, `ASSERT-GROUND: ...`, and an uncoloured `FIXTURES-MATCH: matched <M> of <N>`. `--strict` exits 1 on any failed expectation.
- Old flags still work: `--fail <url-substring>` serves 503 for matching requests (a deterministic failed state on REAL wire keys), `--click`, `--fill`, `--width`.
- The OLD lines are unchanged and are NOT the bar: `CANVAS:` reads `document.body`; `TEXT:` is `body.innerText.slice(0, 160)`.
Colour values: navy `#163372` = `rgb(22, 51, 114)`; primary `#5F3BE3` = `rgb(95, 59, 227)`; white = `rgb(255, 255, 255)`; canvas `#F4F6FA` = `rgb(244, 246, 250)`;
band `#0A1733` = `rgb(10, 23, 51)`; hairline `#C4CBDB` = `rgb(196, 203, 219)`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's FWD-12 ENDPOINT row
   (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v7.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5970-5979 (outside the derived range 5400-5899 that the browser-gated tests use
   for a worktree that names no port, so your server can never be mistaken for another worktree's): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in
   `<WS>/portal`, in the background, with the variable as an INLINE PREFIX on that one command and NEVER exported in the shell that runs your tests. Test the
   port with `curl` first; use that number as `<PORT>`. Sibling workers run at the same time: never 5175.
3. **Run each invocation and READ every PNG** it saves (a grep cannot see contrast). Record per capture: file, viewport, the RAW `FIXTURES-MATCH`,
   `EXPECT*` and `ASSERT-*` lines verbatim, the DESIGN.md clauses you read it against, and what you saw.
4. **A control is a claim.** Before you trust a passing assertion, run its wrong-state arm and confirm it FAILS. If a control passes, the assertion
   cannot tell the states apart: say so and fix the assertion, do not report it as met.
5. **Stop your dev server before the whole-suite criterion and verify the port closed** (`curl` returns `000`). A live server at the port a worktree's
   tests look for makes the browser-gated suites RUN instead of SKIP, which is a different measurement (rows `W8-S1`, `W9-S1`); run the suite in a shell where
   `IRPT_FE_DEV_PORT` is unset. From Git Bash `ps` can miss node: find the listener with PowerShell `Get-NetTCPConnection -LocalPort <n> -State Listen`
   and `Stop-Process` it.
6. **Fixes.** A defect on YOUR write surface (the `<paths>` block) you may fix: keep the BEFORE capture, take an AFTER beside it, one fix per
   finding, cited to its clause. A defect whose fix needs ANY other file is ONE surprise row and you keep going: never widen your grant. If a fix of
   yours breaks a test outside your grant, REVERT it, keep the BEFORE, and file the row. A test inside your grant that pins the OLD behaviour you are
   correcting is updated in the same commit and named in your result.
7. **Result file** (`<slug>.result.md` in your deliverables folder). Its FIRST paragraph says plainly that these captures are FIXTURE-FED (the real
   route with fixtures answered at the network layer; no live route was reached) and why that is the right evidence for THIS card (FWD-12's DONE WHEN is
   about familiarity on the real page and needs no counterpart half) and not for the other seven.
8. **Keep your context small:** read at most the PNGs your criteria need; write long outputs to files and read their tails. A prior worker stalled twice on an oversized context.

### ACCEPTANCE

<criterion id="F72-AC1" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F72-AC1` -- the whole portal typechecks.

<criterion id="F72-AC2" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_unavailable.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --click Analysis --expect '[data-slot="requests-unavailable"]' --expect-text '[data-slot="requests-unavailable"]::UNAVAILABLE: analysis requests are not available (no-declared-route)' --expect '[data-slot="generate-composer"]' --expect-ground '[data-slot="request-list"]=rgb(255, 255, 255)'</invocation><expect>ASSERT-CONTENT: 3 of 3 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F72-AC2` -- the Analysis tab discloses the request-list limitation HONESTLY (the CTO's ruling: no invented route), on a white panel: `ASSERT-CONTENT: 3 of 3 met`, `ASSERT-GROUND: 1 of 1 met`.

<criterion id="F72-AC3" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_unavailable_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --expect '[data-slot="requests-unavailable"]'</invocation><expect>ASSERT-CONTENT: 0 of 1 met</expect></criterion>
`F72-AC3` -- THE CONTENT CONTROL: the same expectation with NO `--click Analysis` (stay on Reporting) finds nothing.

<criterion id="F72-AC4" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_holdings_advisory.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect '[data-slot="slice-advisory"][data-advisory-out-of-enum="true"]' --expect-text '[data-slot="slice-advisory-verbatim"]::ADVISORY' --expect-text '[data-slot="slice-advisory-flag"]::not a contract advisory value -- shown as sent' --expect-ground '[data-slot="slice-table"]=rgb(255, 255, 255)'</invocation><expect>ASSERT-CONTENT: 3 of 3 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F72-AC4` -- the existing Holdings fixture's out-of-enum ADVISORY token (already wired, not this cell's fix) renders and is disclosed honestly: `ASSERT-CONTENT: 3 of 3 met`.

<criterion id="F72-AC5" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_holdings_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --fail investor-reporting/holdings/ --expect '[data-slot="slice-advisory"]' --expect '[data-slot="slice-table"]'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F72-AC5` -- THE CONTENT CONTROL: with the holdings route forced to fail, neither slot renders.

<criterion id="F72-AC6" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_withheld_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-72/fixtures/withheld.json --click Holdings --expect '[data-slot="holdings-qualification"]' --expect '[data-slot="holdings-classification-gap"][data-unknown-nodes="1"][data-nodes="4"]' --expect-text '[data-slot="holdings-classification-gap"]::Classification unknown for 1 of 4 holdings nodes' --expect-text '[data-slot="slice-row"]:nth-of-type(2) [data-slot="slice-supervision"]::withheld' --expect-text '[data-slot="slice-row"]:nth-of-type(2) [data-slot="slice-advisory"]::withheld' --expect-ground '[data-slot="holdings-qualification"]=rgb(255, 255, 255)'</invocation><expect>ASSERT-CONTENT: 5 of 5 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F72-AC6` -- YOUR authored fixture (`fixtures/withheld.json`: a byte copy of `fe-s-18-holdings-observed.json`'s three wire-keyed bodies, with holdings node index 2 flipped to `classification.authoritative: false`, keys unchanged) renders the WITHHELD state -- distinct from the out-of-enum ADVISORY case above -- with the qualification note and both slice cells reading `withheld`: `ASSERT-CONTENT: 5 of 5 met`.

<criterion id="F72-AC7" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_withheld_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-72/fixtures/withheld.json --click Holdings --expect '[data-slot="holdings-qualification"]' --expect '[data-slot="holdings-classification-gap"][data-unknown-nodes="1"][data-nodes="4"]' --expect-text '[data-slot="slice-row"]:nth-of-type(2) [data-slot="slice-supervision"]::withheld'</invocation><expect>ASSERT-CONTENT: 3 of 3 met</expect></criterion>
`F72-AC7` -- the same withheld state, at 390.

<criterion id="F72-AC8" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/f72_withheld_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect '[data-slot="holdings-classification-gap"]' --expect-text '[data-slot="slice-row"]:nth-of-type(2) [data-slot="slice-supervision"]::withheld'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F72-AC8` -- THE CONTENT CONTROL: the SAME two expectations against the UNMODIFIED fixture (node 2 stays authoritative) find neither.

<criterion id="F72-AC9" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-72/reachable-states.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F72-AC9` -- a non-browser guard: using the test-only `initialRequests`/`initialReport` seed props `AnalysisTab.tsx` already documents (the live app never passes them), `renderToStaticMarkup` a seeded, released request and confirm `input-review`, `stage-display`, `variant-selector`, `revision-identity` and `native-sections` all render. This proves the COMPONENTS work; it is NOT evidence that a real user can reach them -- say so in your result, because they cannot (see below).

<criterion id="F72-AC10" cell_refs="FE-s-72" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F72-AC10` -- the whole IRPT_FNTEND suite is green (no dev server of yours running; `IRPT_FE_DEV_PORT` unset).

<criterion id="F72-AC11" cell_refs="FE-s-72" judgment="true" drives="none"/>
`F72-AC11` -- graded at L9 by the CVO against C-S129: which Analysis states are reachable from the BROWSER today (`requests-unavailable`, the composer's refusal and remainder) versus proved only at the component level (`input-review`, `stage-display`, `variant-selector`, `revision-identity`, `native-sections` -- UNREACHABLE from the browser: `listAnalysisRequests` unconditionally rejects with `NoDeclaredRoute`, so `selectedRequest` can never become non-null outside a test-only seed) is stated as TWO DIFFERENT EVIDENCE CLASSES, neither substituting for the other; the Holdings withheld state is distinguished from the pre-existing out-of-enum ADVISORY case; no request-list route was invented. RECORD; NO VERDICT.

<expected_criteria>F72-AC1, F72-AC2, F72-AC3, F72-AC4, F72-AC5, F72-AC6, F72-AC7, F72-AC8, F72-AC9, F72-AC10, F72-AC11</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W22-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- If you find a state's text colour resolves to an `oklch(...)` value with no DESIGN.md clause naming it (fork research flagged this for `requests-unavailable` and similar text), file it as ONE row citing the computed value and the absence of a clause -- the same class of gap as row `W13-S2`.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-72/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-72`.
<owned_cells>FE-s-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F72-AC1`, `F72-AC2`, `F72-AC3`, `F72-AC4`, `F72-AC5`, `F72-AC6`, `F72-AC7`, `F72-AC8`, `F72-AC9`, `F72-AC10`, `F72-AC11`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/IRPT_FNTEND.TO-FE-s-72.holdings-withheld-and-reachable-analysis-states.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F72-AC1,F72-AC2,F72-AC3,F72-AC4,F72-AC5,F72-AC6,F72-AC7,F72-AC8,F72-AC9,F72-AC10,F72-AC11 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-72.holdings-withheld-and-reachable-analysis-states.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `holdings-withheld-and-reachable-analysis-states.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- the instrument (scripts/ui-smoke.mjs: --fail :160, the FIXTURES line :361, the CANVAS line :342, TEXT :343) and the wire keys (contracts/wire/consumed.ts:40-52) read at portal DEV 243089eb; the selectors this order names read in source AND in the rendered DOM by the issuer's research forks; the 4-part criterion rule is the CTO's, round-10 analysis @3020f2a580.
the spec: RUN -- PRD FWD-12's ENDPOINT row and the CTO's round-10 analysis read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 11, wave 2, slot ~8.
