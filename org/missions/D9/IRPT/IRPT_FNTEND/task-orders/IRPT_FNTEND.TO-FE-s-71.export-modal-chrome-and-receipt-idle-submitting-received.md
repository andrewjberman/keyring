# TO IRPT_FNTEND.TO-FE-s-71 -- the export modal's chrome under current design law, and a genuine idle/submitting/received distinction in the receipt card

<to_id>IRPT_FNTEND.TO-FE-s-71</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~21</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-71` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-65 (its `--delay` flag) | **slot:** ~7 | **rows:** C-S130, S69 | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-71` -- the export modal's chrome under current design law, and a genuine idle/submitting/received distinction in the receipt card.

**The fix for C3 is a ONE-WORD change to an EXISTING pattern, not a new one.** `export/ExportModal.tsx`'s `<Panel variant="chart">` resolves to the BAND (`--bg-band`, `#0A1733`) and today nests inside the light dialog sheet -- a dark container nested in a light one, C3's own definition of the defect. `src/ui/components/panels/Panel.tsx`'s OWN decision-tree comment names `nested` ("Visible nested containers -> SURFACE (#FFFFFF) + hairline. DARK text only") as exactly the case a dark card living inside a lighter container should use. Change `variant="chart"` to `variant="nested"` and flip every light-on-dark class inside that region (`AppliedBranding`/`ReceiptPanel`'s legend, the branding chip labels, the no-approved-assets and narrative-toggle text, the checkbox label) to navy-on-white, per DESIGN.md's inversion rule (C5). This ALSO fixes C8 (the filled-purple 'Opal' branding chip, alongside 'Create export' and 'Close', is three simultaneous primaries): make the selected branding chip the SAME weight-and-rule idiom FE-s-61 already used for period presets this round (navy border, bold label, white fill), demote 'Close' to a plain/bordered button, and correct every 6px radius (`rounded-md`) in the modal to 3px (C11). Also correct every `font-weight: 500` in this region to 400 or 700 (C1) alongside the C8 fix -- one commit, cited to both clauses.

**Row `S69` (idle vs in-flight):** `export/ReceiptPanel.tsx:42-44` synthesizes `state: 'LOADING'` for ANY null receipt, so IDLE and SUBMITTING render byte-identical markup today. `ExportButton.tsx` ALREADY tracks `flow.submitting` and passes it to the modal (it already shows "Creating export..." on the button) -- the missing piece is threading that same boolean into `ReceiptPanel`/`StatusPanel` so the CARD changes too. The smallest correct surface (per the CTO's ruling) is a local three-value flow state in `export/` (idle / submitting / receipt), rendered as a `data-flow-state` attribute so it can be asserted directly -- no shared enum change anywhere else. Build `__tests__/fe-s-71/fixtures/export-flow.json` for the submit route: `contract_version`, `operation: "submit-export"`, `firm_id`, `data` (the receipt body, `job_state: "READY"`), and `unprojected_grant` at the ENVELOPE'S TOP LEVEL (sibling of `data`, not inside it) -- the parser throws `EnvelopeMismatch` without it, the same requirement W13-S1 found for the print fixture.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** `export/` (the whole folder) and your own `__tests__/fe-s-71/`, PLUS the ONE literal-string assertion at `__tests__/fe-s-16/mounted-states.test.ts:146` (widened by this order, because your own fix changes the string it pins). Every other tab, `render/`, and every shared component are read-only to you.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5960-5969 (outside the derived range 5400-5899 that the browser-gated tests use
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

<criterion id="F71-AC1" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F71-AC1` -- the whole portal typechecks.

<criterion id="F71-AC2" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_idle_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect '[data-slot="receipt-panel"][data-flow-state="idle"]' --expect '[data-slot="submit-export"]:not([disabled])' --expect-text '[data-slot="submit-export"]::Create export' --expect-style '[data-slot="submit-export"]::border-radius=3px' --expect-style '[data-slot="submit-export"]::font-weight!=500' --expect-ground '[role="dialog"]=rgb(244, 246, 250)'</invocation><expect>ASSERT-CONTENT: 3 of 3 met[\s\S]*ASSERT-STYLE: 2 of 2 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F71-AC2` -- IDLE (no receipt, nothing submitted): the receipt panel carries a NEW `data-flow-state="idle"` attribute (never the synthesized `Loading` state), Create export is enabled, radius 3px (C11), weight not 500 (C1), and the dialog body sits on the canvas colour, never the band -- `ASSERT-CONTENT: 3 of 3 met`, `ASSERT-STYLE: 2 of 2 met`, `ASSERT-GROUND: 1 of 1 met`.

<criterion id="F71-AC3" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_idle_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect '[data-slot="receipt-panel"][data-flow-state="idle"]' --expect-ground '[role="dialog"]=rgb(244, 246, 250)'</invocation><expect>ASSERT-CONTENT: 1 of 1 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F71-AC3` -- the same IDLE state, at 390.

<criterion id="F71-AC4" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_idle_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --expect '[data-slot="submit-export"]' --expect-ground '[role="dialog"]=rgb(244, 246, 250)'</invocation><expect>ASSERT-CONTENT: 0 of 1 met</expect></criterion>
`F71-AC4` -- THE CONTENT CONTROL: the same button expectation with NO `--click Export` (modal never opened) finds nothing.

<criterion id="F71-AC5" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_ground_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --inject-css '[role="dialog"]{background-color:#c4cbdb !important}' --expect-ground '[role="dialog"]=rgb(244, 246, 250)'</invocation><expect>ASSERT-GROUND: 0 of 1 met</expect></criterion>
`F71-AC5` -- THE GROUND CONTROL: after painting the dialog silver, the same ground assertion FAILS.

<criterion id="F71-AC6" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_submitting_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-71/fixtures/export-flow.json --click Export --click 'Create export' --delay 'api/scoped/investor-reporting/export=4000' --clickwait 1200 --expect '[data-slot="receipt-panel"][data-flow-state="submitting"]' --expect '[data-slot="submit-export"][disabled]' --expect-text '[data-slot="submit-export"]::Creating export...'</invocation><expect>ASSERT-CONTENT: 3 of 3 met</expect></criterion>
`F71-AC6` -- SUBMITTING (in flight): your authored `fixtures/export-flow.json` (a copy of `export-ready.json`'s three keys plus a fourth, `/api/scoped/investor-reporting/export`, whose body needs `unprojected_grant` at the ENVELOPE'S TOP LEVEL, sibling of `data`, or the parser throws `EnvelopeMismatch` -- the same requirement W13-S1 found for the print fixture) held for 4000ms by `--delay` renders a distinct `data-flow-state="submitting"`, never the same markup as IDLE: `ASSERT-CONTENT: 3 of 3 met`.

<criterion id="F71-AC7" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_submitting_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect '[data-slot="receipt-panel"][data-flow-state="submitting"]' --expect '[data-slot="submit-export"][disabled]'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F71-AC7` -- THE CONTENT CONTROL: the same two expectations against the IDLE fixture (nothing submitted) find neither -- IDLE and SUBMITTING are provably distinct states, closing row `S69`.

<criterion id="F71-AC8" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_received_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-71/fixtures/export-flow.json --click Export --click 'Create export' --clickwait 3000 --expect '[data-slot="receipt-panel"][data-flow-state="receipt"][data-job-state="ready"]' --expect '[data-slot="download-link"]' --expect-text '[data-slot="download-link"]::Download'</invocation><expect>ASSERT-CONTENT: 3 of 3 met</expect></criterion>
`F71-AC8` -- RECEIVED: the same fixture with no artificial delay resolves to a `ready` receipt with a download link, and `data-flow-state` reads `"receipt"` -- the third of the three distinct flow states.

<criterion id="F71-AC9" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_received_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect '[data-slot="download-link"]'</invocation><expect>ASSERT-CONTENT: 0 of 1 met</expect></criterion>
`F71-AC9` -- THE CONTENT CONTROL: the IDLE fixture (never submitted) has no download link.

<criterion id="F71-AC10" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_chrome_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect-ground '[data-slot="branding-options"]=rgb(255, 255, 255)' --expect-style '[data-slot="branding-options"] button[aria-pressed="true"]::border-radius=3px' --expect-style '[data-slot="submit-export"]::border-radius=3px' --expect-style '[data-slot="export-modal"] [data-slot="close"]::background-color!=rgb(95, 59, 227)'</invocation><expect>ASSERT-STYLE: 3 of 3 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F71-AC10` -- AFTER the fix: the branding section (`AppliedBranding`/`ReceiptPanel`'s container, currently `<Panel variant="chart">` which resolves to the BAND, `#0A1733`, nested inside the light dialog -- exactly the C3 shape this project keeps finding) is now `<Panel variant="nested">` (the SAME component, an EXISTING variant that already resolves to `--bg-surface` white with dark-text-only, per `Panel.tsx`'s own decision tree comment -- this is reuse, not invention). The selected branding chip is a navy-bordered, bold-label control (C8's "weight and rule" idiom, the FE-s-61 precedent), never a second filled-purple chip. Close is a plain/bordered button, never a second filled-primary beside Create export (C8). Every button in the modal is `rounded-[3px]` (C11), never `rounded-md`.

<criterion id="F71-AC11" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_chrome_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect-ground '[data-slot="branding-options"]=rgb(255, 255, 255)'</invocation><expect>ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F71-AC11` -- the same white-panel ground, at 390.

<criterion id="F71-AC12" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_chrome_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --inject-css '[data-slot="branding-options"]{background-color:#0a1733 !important}' --expect-ground '[data-slot="branding-options"]=rgb(255, 255, 255)'</invocation><expect>ASSERT-GROUND: 0 of 1 met</expect></criterion>
`F71-AC12` -- THE GROUND CONTROL: after re-painting the branding section as the band colour, the same assertion FAILS.

<criterion id="F71-AC13" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_preview_scroll.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect '[data-slot="preview-scroll"]'</invocation><expect>ASSERT-CONTENT: 1 of 1 met</expect></criterion>
`F71-AC13` -- the preview container exists at 390. Read the PNG: confirm by reading `preview-scroll`'s `scrollWidth` vs `clientWidth` in your own probe (they differ, per research: 1056 vs 264) that this is a genuine horizontal-scroll affordance, not permanent clipping -- do not assert clipping from the still alone.

<criterion id="F71-AC14" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-71/receipt-flow-state.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F71-AC14` -- a non-browser guard, `renderToStaticMarkup(createElement(ReceiptPanel, ...))` exactly as `__tests__/fe-s-9/receipt.test.ts` already does: (a) no receipt, not submitting -> markup carries `data-flow-state="idle"` and NEVER the string `Loading`; (b) no receipt, submitting=true -> `data-flow-state="submitting"`, still no `Loading`; (c) a ready receipt -> `data-flow-state="receipt"`, unchanged download behaviour.

<criterion id="F71-AC15" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9 src/pages/InvestorReporting/__tests__/fe-s-15 src/pages/InvestorReporting/__tests__/fe-s-16 src/pages/InvestorReporting/__tests__/fe-s-31</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F71-AC15` -- the pinning suites (`fe-s-9`, `fe-s-15`, `fe-s-16`, `fe-s-31`) stay green. `fe-s-16/mounted-states.test.ts:146` currently asserts the literal source string `<Panel variant="chart">` -- update THAT ONE assertion, in this commit, to `<Panel variant="nested">` (the test's own comment says its intent is "the two round-1 components are mounted INSIDE the ... Panel", never the specific variant; changing the variant is the correct fix, not a break to route around).

<criterion id="F71-AC16" cell_refs="FE-s-71" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F71-AC16` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F71-AC17" cell_refs="FE-s-71" judgment="true" drives="none"/>
`F71-AC17` -- graded at L9 by the CVO: `<Panel variant="nested">` is confirmed an EXISTING variant (not a new one) whose decision tree already names white-surface-dark-text as its rule; every `text-white`/`border-white/N` class inside the changed region is flipped to a navy equivalent per DESIGN.md's inversion rule (C5), captured before and after; `S69`'s three states (idle, submitting, receipt) are read as genuinely distinct markup, not merely distinct prose; the preview's horizontal scroll is confirmed reachable, not merely captured. RECORD; NO VERDICT.

<expected_criteria>F71-AC1, F71-AC2, F71-AC3, F71-AC4, F71-AC5, F71-AC6, F71-AC7, F71-AC8, F71-AC9, F71-AC10, F71-AC11, F71-AC12, F71-AC13, F71-AC14, F71-AC15, F71-AC16, F71-AC17</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W21-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- The `fe-s-42/every-site.test.ts:132` class-string literal MAY or may not belong to a file in your grant: read it yourself before touching anything it pins; if it is unrelated, ignore it.

<paths>
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-71/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-71`.
<owned_cells>FE-s-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F71-AC1`, `F71-AC2`, `F71-AC3`, `F71-AC4`, `F71-AC5`, `F71-AC6`, `F71-AC7`, `F71-AC8`, `F71-AC9`, `F71-AC10`, `F71-AC11`, `F71-AC12`, `F71-AC13`, `F71-AC14`, `F71-AC15`, `F71-AC16`, `F71-AC17`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/IRPT_FNTEND.TO-FE-s-71.export-modal-chrome-and-receipt-idle-submitting-received.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F71-AC1,F71-AC2,F71-AC3,F71-AC4,F71-AC5,F71-AC6,F71-AC7,F71-AC8,F71-AC9,F71-AC10,F71-AC11,F71-AC12,F71-AC13,F71-AC14,F71-AC15,F71-AC16,F71-AC17 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-71.export-modal-chrome-and-receipt-idle-submitting-received.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `export-modal-chrome-and-receipt-idle-submitting-received.result.md` beside it.
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

Seating: round 11, wave 2, slot ~7.
