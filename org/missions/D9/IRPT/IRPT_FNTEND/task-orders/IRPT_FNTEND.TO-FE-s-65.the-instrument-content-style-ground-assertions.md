# TO IRPT_FNTEND.TO-FE-s-65 -- the instrument: content, style and ground assertions in ui-smoke, with controls that can fail

<to_id>IRPT_FNTEND.TO-FE-s-65</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~15</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

⛔ **COO AMENDMENT (2026-09-22, `2.0.0_SA_COO~F`) -- READ BEFORE F65-AC16. THE DEFECT IS IN THIS ORDER, NOT IN YOUR WORK.** Your first pass measured
17 of 18 criteria PASS and correctly REFUSED F65-AC16 rather than self-grading past it, then correctly left `<status>pending</status>`. Verified: the
`--delay`/`--click` grammar itself is sound (your own diagnostic proved it fires on a second click or a load-time URL); the defect is that clicking
the toolbar `Export` button (`ExportButton.tsx:171-180`) only OPENS the modal -- the POST fires from the modal's own `Create export` button
(`ExportModal.tsx:257-266`). F65-AC16's invocation is missing that second click. Your first-pass evidence (17 PASS criteria, the diagnostic finding)
stands and is drained; this amendment only re-points F65-AC16.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-65` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** none (READY ROOT; every other visual cell of round 11 depends on this) | **slot:** ~1 | **rows:** W11-S1, W12-S1 (the rule's precondition); W13-S2 (the container-ground remedy the CTO named) | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-65` -- the instrument: content, style and ground assertions in ui-smoke, with controls that can fail.

**This cell builds the instrument the CTO's criterion rule needs, and every other visual cell of this round depends on it.** Round 10's `ui-smoke.mjs` cannot meet rules (b) or (d): its `TEXT:` line is `document.body.innerText.slice(0, 160)` and its `CANVAS:` line is `getComputedStyle(document.body)`, the page field, never a route's own container. You add the flags in THE INSTRUMENT above to `scripts/ui-smoke.mjs`, ADDITIVELY, in the script's own existing style (`args.includes(...)`, the `reduce` pattern for repeatable flags, the header comment listing every flag): with none of the new flags the output is byte-for-byte what it was (F65-AC2 proves it). Insert the expectation pass after the click steps and the observation wait and before the existing `state` evaluation (`:331`); print the `EXPECT*` lines and the three `ASSERT-*` summaries next to the `TEXT` line, and print the plain `FIXTURES-MATCH` line beside the existing `FIXTURES:` line (`:361`), built with a template literal so it carries no colour codes. "Visible" means the element has a non-empty bounding box and computed `display` not `none` and `visibility` not `hidden`. Ground = the first ancestor-or-self whose computed `background-color` has non-zero alpha. Every `--expect*` argument is a CSS selector: the first `::` in an `--expect-text` or `--expect-style` argument separates selector from the rest, and a selector containing `::` is not supported (say so in the header). `--strict` sets `process.exitCode = 1` after the browser closes when any expectation failed or `FIXTURES-MATCH` reads M below N. Portal `scripts/` is shared tooling other seats use: touch nothing but `scripts/ui-smoke.mjs`, and only additively. The dead-fixture file and `regression.sh` live in your own `__tests__/fe-s-65/`.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** `portal/scripts/ui-smoke.mjs` (additive flags only) and your own `__tests__/fe-s-65/` (`regression.sh`, `fixtures/dead.json`). Everything else is read-only to you, including every component and every existing fixture.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5900-5909 (outside the derived range 5400-5899 that the browser-gated tests use
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

<criterion id="F65-AC1" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F65-AC1` -- the whole portal typechecks.

<criterion id="F65-AC2" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && timeout 300 bash src/pages/InvestorReporting/__tests__/fe-s-65/regression.sh <PORT></invocation><expect>REGRESSION: 4 of 4 default lines identical</expect></criterion>
`F65-AC2` -- DEFAULT BEHAVIOUR IS UNCHANGED: your `regression.sh` runs the BASELINE `scripts/ui-smoke.mjs` (`git show 243089eb:scripts/ui-smoke.mjs`, copied beside the script, deleted after) and the new one on the same route and fixture with none of the new flags, and prints `REGRESSION: <k> of 4 default lines identical` for the `LOC`, `CANVAS`, `TEXT` and `REFAREAS` lines.

<criterion id="F65-AC3" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac3.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect '[data-slot="tabs"]'</invocation><expect>EXPECT\[\[data-slot="tabs"\]\]: PASS \([1-9][0-9]* visible\)</expect></criterion>
`F65-AC3` -- `--expect` PASS arm: the tabs container is on the real route, so the run prints `EXPECT[[data-slot="tabs"]]: PASS (<n> visible)` with n above zero.

<criterion id="F65-AC4" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac4.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect '[data-slot="no-such-slot-zzz"]'</invocation><expect>EXPECT\[\[data-slot="no-such-slot-zzz"\]\]: FAIL \(0 visible\)</expect></criterion>
`F65-AC4` -- `--expect` FAIL arm: a selector that matches nothing prints `FAIL (0 visible)`. This is the arm that proves the instrument can say no.

<criterion id="F65-AC5" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac5.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect-text 'body::Investor Reporting'</invocation><expect>EXPECT-TEXT\[body::Investor Reporting\]: PASS</expect></criterion>
`F65-AC5` -- `--expect-text` PASS arm: `Investor Reporting` is in the sidebar's `innerText` at 1440 wide.

<criterion id="F65-AC6" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac6.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect-text 'body::ZZZ NOT ON THIS PAGE ZZZ'</invocation><expect>EXPECT-TEXT\[body::ZZZ NOT ON THIS PAGE ZZZ\]: FAIL</expect></criterion>
`F65-AC6` -- `--expect-text` FAIL arm: a string that is not on the page prints `FAIL`.

<criterion id="F65-AC7" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac7.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect-style 'body::background-color=rgb(244, 246, 250)'</invocation><expect>EXPECT-STYLE\[body::background-color\]: PASS rgb\(244, 246, 250\)</expect></criterion>
`F65-AC7` -- `--expect-style` PASS arm with `=`: the body's computed `background-color` is the canvas, and the line prints the ACTUAL value beside PASS.

<criterion id="F65-AC8" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac8.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect-style 'body::background-color!=rgb(244, 246, 250)'</invocation><expect>EXPECT-STYLE\[body::background-color\]: FAIL rgb\(244, 246, 250\)</expect></criterion>
`F65-AC8` -- `--expect-style` FAIL arm with `!=`: asserting the body is NOT the canvas fails and prints the actual value, so the `!=` operator is exercised in its failing direction.

<criterion id="F65-AC9" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac9.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect-ground 'body=rgb(244, 246, 250)'</invocation><expect>EXPECT-GROUND\[body\]: PASS rgb\(244, 246, 250\)</expect></criterion>
`F65-AC9` -- `--expect-ground` PASS arm: the nearest non-transparent background at or above `body` is the canvas.

<criterion id="F65-AC10" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac10.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --inject-css 'body{background-color:#c4cbdb !important}' --expect-ground 'body=rgb(244, 246, 250)'</invocation><expect>EXPECT-GROUND\[body\]: FAIL rgb\(196, 203, 219\)</expect></criterion>
`F65-AC10` -- THE WRONG-GROUND CONTROL: after `--inject-css` paints the body silver, the same ground assertion prints `FAIL rgb(196, 203, 219)`. This is the control the CTO's rule (d) requires of every later cell.

<criterion id="F65-AC11" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac11.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect '[data-slot="tabs"]' --expect '[data-slot="no-such-slot-zzz"]' --expect-text 'body::Investor Reporting' --expect-text 'body::ZZZ NOT ON THIS PAGE ZZZ'</invocation><expect>ASSERT-CONTENT: 2 of 4 met</expect></criterion>
`F65-AC11` -- the SUMMARY line counts honestly: two passing and two failing content expectations print `ASSERT-CONTENT: 2 of 4 met`.

<criterion id="F65-AC12" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac12.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export</invocation><expect>FIXTURES-MATCH: matched (\d+) of \1(?![0-9])</expect></criterion>
`F65-AC12` -- WIRE MATCH, live arm: the wire-keyed fixture with the Export click prints `FIXTURES-MATCH: matched N of N` (the same number twice), an uncoloured plain line.

<criterion id="F65-AC13" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac13.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-65/fixtures/dead.json</invocation><expect>FIXTURES-MATCH: matched 0 of 1(?![0-9])</expect></criterion>
`F65-AC13` -- WIRE MATCH, dead arm: `__tests__/fe-s-65/fixtures/dead.json` (you author it: ONE key, `/api/scoped/investor-reporting/no-such-operation`) prints `matched 0 of 1`, so the line detects a fixture that answers nothing.

<criterion id="F65-AC14" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac14.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --strict --expect '[data-slot="no-such-slot-zzz"]'; echo EXIT=$?</invocation><expect>EXIT=1(?![0-9])</expect></criterion>
`F65-AC14` -- `--strict` exits 1 when an expectation fails.

<criterion id="F65-AC15" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac15.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --strict --expect '[data-slot="tabs"]'; echo EXIT=$?</invocation><expect>EXIT=0(?![0-9])</expect></criterion>
`F65-AC15` -- `--strict` exits 0 when every expectation is met.

<criterion id="F65-AC16" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac16.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --click 'Create export' --delay 'api/scoped/investor-reporting/export=4000' --console DELAYED</invocation><expect>DELAYED: .*\(4000ms\)</expect></criterion>
`F65-AC16` -- AMENDED: `--delay` PASS arm, with the SECOND click that actually submits (opening the modal alone never fires the POST): a fixture
key matching the argument's substring is held for the given milliseconds before it resolves, and the run prints `DELAYED: <key> (<ms>ms)`. FE-s-71
depends on this to build a genuine in-flight submit state.

<criterion id="F65-AC17" cell_refs="FE-s-65" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F65-AC17` -- the whole IRPT_FNTEND suite is green (your dev server STOPPED and its port verified closed; `IRPT_FE_DEV_PORT` unset in that shell).

<criterion id="F65-AC18" cell_refs="FE-s-65" judgment="true" drives="none"/>
`F65-AC18` -- graded at L9 by the CVO: the flag block you added to `scripts/ui-smoke.mjs` (header comment and code) matches the grammar in THE INSTRUMENT above exactly; every failing arm above was produced by the instrument and not by a hand-written line; the OLD flags and the OLD output lines are untouched (F65-AC2). RECORD; NO VERDICT.

<expected_criteria>F65-AC1, F65-AC2, F65-AC3, F65-AC4, F65-AC5, F65-AC6, F65-AC7, F65-AC8, F65-AC9, F65-AC10, F65-AC11, F65-AC12, F65-AC13, F65-AC14, F65-AC15, F65-AC16, F65-AC17, F65-AC18</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W15-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- Cells FE-s-67..72 are cut against this grammar and cannot start until this cell is drained. If you find the grammar unimplementable as written, REFUSE the affected criterion with the measurement: do not invent a different grammar, the other orders quote this one.

<paths>
portal/scripts/ui-smoke.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-65/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-65`.
<owned_cells>FE-s-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F65-AC1`, `F65-AC2`, `F65-AC3`, `F65-AC4`, `F65-AC5`, `F65-AC6`, `F65-AC7`, `F65-AC8`, `F65-AC9`, `F65-AC10`, `F65-AC11`, `F65-AC12`, `F65-AC13`, `F65-AC14`, `F65-AC15`, `F65-AC16`, `F65-AC17`, `F65-AC18`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F65-AC1,F65-AC2,F65-AC3,F65-AC4,F65-AC5,F65-AC6,F65-AC7,F65-AC8,F65-AC9,F65-AC10,F65-AC11,F65-AC12,F65-AC13,F65-AC14,F65-AC15,F65-AC16,F65-AC17,F65-AC18 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `the-instrument-content-style-ground-assertions.result.md` beside it.
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

Seating: round 11, wave 1, slot ~1.
