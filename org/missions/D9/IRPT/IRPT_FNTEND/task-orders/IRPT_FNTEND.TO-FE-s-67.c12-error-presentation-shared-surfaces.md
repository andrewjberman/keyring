# TO IRPT_FNTEND.TO-FE-s-67 -- shared C12 error presentation: reuse PanelError and buttonClass, never a new red-text idiom

<to_id>IRPT_FNTEND.TO-FE-s-67</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~17</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-67` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-65 (its --expect/--expect-style/--expect-ground flags -- every criterion below uses them) | **slot:** ~3 | **rows:** W11-S3, W12-S2 (breadcrumb), W12-S3 | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-67` -- shared C12 error presentation: reuse PanelError and buttonClass, never a new red-text idiom.

**Reuse, don't invent.** `src/ui/components/states/PanelStates.tsx` already exports `PanelError` (a danger icon beside bold navy text, an optional hint/cause/retry) and is imported by ZERO files in `InvestorReporting/` today. Wrap EVERY bare `text-red-800` text block your grant touches in it: `index.tsx:105` (`surface="panel"`, it stands on the bare canvas), `GenerateComposer.tsx` (`composer-refusal`, `comparison-refusal`, `snapshot-remainder`; `surface="inset"`, no retry -- these are inline form refusals), `DrillTree.tsx:234` (`holdings-drill-refused`). `StatusPanel.tsx`'s safe-action button is a SECOND filled-primary alongside Export (both compute `rgb(95, 59, 227)` background today): replace it with `buttonClass('secondary', 'canvas', 'sm')` from `src/ui/components/Controls.tsx` (white background, navy border and text). `DrillTree.tsx:181`'s breadcrumb button is plain indigo text with NO at-rest underline (`hover:underline` only) -- add an at-rest underline; whether to also move it off purple to navy is a genuine judgment call this order does NOT make for you (DESIGN.md's underline rule at C8 names five identity places plus the active tab, never a tree-navigation breadcrumb): KEEP the colour, ADD the underline, and record the colour question as a finding for the CVO, citing the exact clause line. Add a `bun test` guard (`__tests__/fe-s-67/panel-error-reuse.test.ts`, reading the four touched files as text like the existing colour-law scanner does) asserting `PanelError` is imported by all of them and `text-red-800` no longer appears in any, outside a comment; print the count. Two existing tests PIN behaviour you must not break: `__tests__/fe-s-21/source-age.test.ts:285-295` (an error-affordance scanner keyed to `text-red-*`/`role="alert"` -- keep something it can still find, or its own row is out of your grant to fix silently) and `__tests__/fe-s-11/colour-law.test.ts` (a whole-tree class scan; keep every button either Panel-descended or self-backgrounded). For the slice-table overflow (W12-S3), the CTO's ruling is EXERCISE, not prescribe: `__tests__/fe-s-32/holdings-driver.mjs` already scrolls the container and captures a second PNG -- use THAT mechanism, do not build a second one.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** `index.tsx`, `tabs/StatusPanel.tsx`, `tabs/analysis/GenerateComposer.tsx`, `tabs/holdings/DrillTree.tsx`, and your own `__tests__/fe-s-67/`. Every other tab and `export/` are read-only to you.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5920-5929 (outside the derived range 5400-5899 that the browser-gated tests use
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

<criterion id="F67-AC1" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F67-AC1` -- the whole portal typechecks.

<criterion id="F67-AC2" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_scope_error.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/default.json --fail investor-reporting/directory/resolve --expect '[data-slot="scope-error"]' --expect-text '[data-slot="scope-error"]::Scope could not be resolved' --expect-style '[data-slot="scope-error"] svg::color=rgb(190, 45, 54)' --expect-style '[data-slot="scope-error"] p::color=rgb(22, 51, 114)'</invocation><expect>ASSERT-CONTENT: 2 of 2 met[\s\S]*ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F67-AC2` -- the scope-failure state (`--fail` has NO leading slash) names a `[data-slot="scope-error"]` block with the failure text, a danger-coloured icon and navy text: `ASSERT-CONTENT: 2 of 2 met`, `ASSERT-STYLE: 2 of 2 met`.

<criterion id="F67-AC3" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_scope_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --expect '[data-slot="scope-error"]' --expect-text '[data-slot="scope-error"]::Scope could not be resolved'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F67-AC3` -- THE CONTENT CONTROL: the SAME expectations with no `--fail` (scope resolves normally) find nothing.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~17-report):** the fixture `fixtures/smoke/default.json` is defective, unrelated to this
cell -- verified independently: all 12 of its declared entries omit `unprojected_grant`, and
`contracts/envelope.ts:278-279`'s `parseIrEnvelope` unconditionally throws `EnvelopeMismatch('unprojected_grant', ...)` when that field
is absent (comment at `:272-277`: "NON-OPTIONAL on the WIRE on every non-refused response... a response that omits the key entirely is a
genuine backend defect... refused rather than silently carried as null"). So the "control" (no `--fail`) never resolves cleanly against
this fixture regardless of any fix -- it hits a DIFFERENT error path than the one this criterion is trying to rule out. Fix: swap to
`fe-s-18-frozen.json` (already used by this same TO's F67-AC5/AC6; verified independently, all 9 of its entries carry `unprojected_grant`).
The bar is unchanged: the same two `--expect` lines must still find nothing on a genuinely clean, resolved scope. Row
`IRPT_FNTEND-W17-S3` is CORRECT and stays filed as the record of the defect; this amendment is the remedy it called for.

<criterion id="F67-AC4" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_safe_action.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json --expect '[data-slot="safe-actions"] button' --expect-text '[data-slot="safe-actions"] button::Reload' --expect-style '[data-slot="safe-actions"] button::background-color=rgb(255, 255, 255)' --expect-style '[data-slot="safe-actions"] button::color=rgb(22, 51, 114)'</invocation><expect>ASSERT-CONTENT: 2 of 2 met[\s\S]*ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F67-AC4` -- the StatusPanel's safe-action button (an Uncertain Reporting state) is white with navy text, never the second filled-primary Export already holds (C8): `ASSERT-CONTENT: 2 of 2 met`, `ASSERT-STYLE: 2 of 2 met`. NOTE: this is the AFTER-fix target; find or author the fixture that gives a clean READY state with zero safe actions and use it as this criterion's content control before you finish the cell (research left this open).

<criterion id="F67-AC5" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_composer.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --click Analysis --expect '[data-slot="composer-refusal"]' --expect-text '[data-slot="composer-refusal"]::Select a client in the header first' --expect '[data-slot="snapshot-remainder"]' --expect-text '[data-slot="snapshot-remainder"]::Needs correction' --expect-style '[data-slot="composer-refusal"]::color=rgb(22, 51, 114)' --expect-style '[data-slot="snapshot-remainder"]::color=rgb(22, 51, 114)'</invocation><expect>ASSERT-CONTENT: 4 of 4 met[\s\S]*ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F67-AC5` -- the Analysis composer's refusal and remainder text are navy, never Tailwind red-800: `ASSERT-CONTENT: 4 of 4 met`, `ASSERT-STYLE: 2 of 2 met`.

<criterion id="F67-AC6" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_composer_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --expect '[data-slot="composer-refusal"]' --expect '[data-slot="snapshot-remainder"]'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F67-AC6` -- THE CONTENT CONTROL: the same two `--expect` lines with NO `--click Analysis` (stay on Reporting) find neither slot.

<criterion id="F67-AC7" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_holdings.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect '[data-slot="holdings-breadcrumb"]' --expect '[data-slot="slice-table"] thead th:last-child' --expect-style '[data-slot="holdings-breadcrumb"]::text-decoration-line=underline'</invocation><expect>ASSERT-CONTENT: 2 of 2 met[\s\S]*ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F67-AC7` -- the Holdings breadcrumb and slice table render, and the breadcrumb carries an at-rest underline (it is text-coloured navigation, not a purple identity accent): `ASSERT-CONTENT: 2 of 2 met`, `ASSERT-STYLE: 1 of 1 met`.

<criterion id="F67-AC8" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_holdings_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --expect '[data-slot="holdings-breadcrumb"]' --expect '[data-slot="slice-table"] thead th:last-child'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F67-AC8` -- THE CONTENT CONTROL: the same two `--expect` lines with NO `--click Holdings` find neither slot.

<criterion id="F67-AC9" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_overflow_before.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings</invocation><expect>SAVED</expect></criterion>
`F67-AC9` -- BEFORE capture of the slice table at 390: read the PNG and note whether the last column is visibly clipped.

<criterion id="F67-AC10" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && timeout 120 node src/pages/InvestorReporting/__tests__/fe-s-32/holdings-driver.mjs <PORT> <scenario-map.json, one entry wrapping fixtures/smoke/fe-s-18-holdings-observed.json> <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_overflow/</invocation><expect>DRIVER OK</expect></criterion>
`F67-AC10` -- OVERFLOW EXERCISED, NOT PRESCRIBED: the EXISTING driver (`__tests__/fe-s-32/holdings-driver.mjs`, already built for exactly this) scrolls the slice table's container and captures the reached state; read BOTH PNGs and confirm the last column is reachable by scroll, not permanently clipped. If this driver's CLI shape differs from this invocation, adapt the call and say so in your result -- do not invent a second mechanism when the CTO named this one to reuse.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~17-report):** the literal invocation above was wrong on TWO counts, both confirmed
independently by reading `holdings-driver.mjs:37-39` and its header comment: (1) its real CLI is POSITIONAL --
`argv[2]`=port, `argv[3]`=a scenario-map JSON path (shape `{"<scenario>": {"<route-key>": <envelope>, ...}, ...}`, NOT a flat
ui-smoke.mjs-style fixture file), `argv[4]`=capture directory -- never `--port`/`--width`/`--fixtures`/`--out` flags; (2) its only
`console.log` call sites (`:198-228`) print `CAPTURE`/`RESULT`/`  served(...)`/`PAGE CRASHES:`/`DRIVER OK` -- the driver's own source
cannot emit `SAVED` or `scrollLeft` under ANY invocation shape, so that `<expect>` could never match regardless of correctness. The
invocation above is corrected to the real positional shape (worker `~21`'s own already-proven adaptation: wrap the flat fixture as one
scenario, e.g. `{"fe-s-18-holdings-observed": <the same map>}`, written to a scratch path in your deliverables folder); `<expect>` is
corrected to `DRIVER OK`, the driver's own rc=0 success sentinel -- the same evidentiary weight `F67-AC9`'s `<expect>SAVED</expect>`
already carries for the OTHER instrument. The bar is unchanged: you still read BOTH PNGs yourself and confirm the last column is
scroll-reachable, not permanently clipped -- that qualitative judgment was never something a regex could grade, on the original
invocation or this one. Row `IRPT_FNTEND-W17-S2` is CORRECT and stays filed; this amendment is the remedy it called for.

<criterion id="F67-AC11" cell_refs="FE-s-67" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F67-AC11` -- the whole IRPT_FNTEND suite is green, including the unmodified pinning tests `fe-s-21/source-age.test.ts` and `fe-s-11/colour-law.test.ts` (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F67-AC12" cell_refs="FE-s-67" judgment="true" drives="none"/>
`F67-AC12` -- graded at L9 by the CVO: every fix reuses an EXISTING pattern (`PanelError` from `src/ui/components/states/PanelStates.tsx`, unused anywhere in InvestorReporting today, for every red-only text block; `buttonClass('secondary','canvas','sm')` from `src/ui/components/Controls.tsx` for the safe-action button) rather than inventing a new one, cited to its clause; the breadcrumb's colour choice (kept purple-and-underlined vs navy-and-underlined) is recorded as the CTO's call, not self-graded; the two rows this cell could not fully close (the StatusPanel content-control fixture; the DrillTree `:234` revision-mismatch text, not confirmed reachable from any fixture) are named as open, not silently dropped. RECORD; NO VERDICT.

<expected_criteria>F67-AC1, F67-AC2, F67-AC3, F67-AC4, F67-AC5, F67-AC6, F67-AC7, F67-AC8, F67-AC9, F67-AC10, F67-AC11, F67-AC12</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W17-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- The DrillTree revision-mismatch text (:234) is not confirmed reachable from any existing fixture; if you cannot reach it, wrap it anyway from source and file a row naming which fixture you tried.

<paths>
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-67/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-67`.
<owned_cells>FE-s-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F67-AC1`, `F67-AC2`, `F67-AC3`, `F67-AC4`, `F67-AC5`, `F67-AC6`, `F67-AC7`, `F67-AC8`, `F67-AC9`, `F67-AC10`, `F67-AC11`, `F67-AC12`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F67-AC1,F67-AC2,F67-AC3,F67-AC4,F67-AC5,F67-AC6,F67-AC7,F67-AC8,F67-AC9,F67-AC10,F67-AC11,F67-AC12 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `c12-error-presentation-shared-surfaces.result.md` beside it.
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

Seating: round 11, wave 2, slot ~3.
