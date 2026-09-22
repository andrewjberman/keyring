# TO IRPT_FNTEND.TO-FE-s-70 -- CategoryViewTree gains an additive light variant; DrillTree uses it, Model Portfolios' dark default is unchanged

<to_id>IRPT_FNTEND.TO-FE-s-70</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~20</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-70` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-65 (its --expect/--expect-ground flags), FE-s-69 (shares its Model Portfolios fixture; author your own copy if FE-s-69 has not landed) | **slot:** ~6 | **rows:** W12-S2 (container part) | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-70` -- CategoryViewTree gains an additive light variant; DrillTree uses it, Model Portfolios' dark default is unchanged.

**The CTO's condition is RESOLVED, not open.** Model Portfolios' OWN use of `CategoryViewTree` is NOT itself a C3 violation: the dark gradient card sits directly on the light page canvas there, with no white panel wrapping it. The white-panel-nesting violation is `DrillTree.tsx:222-223`'s doing: it wraps the SAME dark card in its own `bg-white` container. So the CTO's branch applies: an ADDITIVE light variant for DrillTree's use is correct, and Model Portfolios' default stays untouched. Add an additive prop to `CategoryViewTree` (e.g. `ground?: 'dark' | 'light'`, default `'dark'`) that, when `'light'`, renders the ready-state card without the dark-gradient `GraphicPanel` wrapper -- swap to a plain white/hairline container and flip the light-on-dark text classes to navy-on-white per C3's inversion rule (C5). `GraphicPanel` (`src/ui/components/graphic/HeroGraphic.tsx`) has exactly ONE other consumer besides `CategoryViewTree` (`CapitalMarketAssumptions/components/PhilosophyPillars.tsx`): your additive prop on `CategoryViewTree` does not touch `HeroGraphic`'s own default, so that consumer is unaffected -- confirm this stays true as you implement. DrillTree needs NO NEW FIXTURE KEY: its `mdpfResultFromSnapshot` function derives the tree entirely from the `holdings/` snapshot already in every Holdings fixture, so the existing `fe-s-18-holdings-observed.json` already reaches the ready state (verified: this is not a guess). Keep the chart legend's own data colours exactly as they are; only the OUTER card's ground and its non-data text move.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** `src/components/CategoryViewTree.tsx` and your own `__tests__/fe-s-70/`. `tabs/holdings/DrillTree.tsx`'s ONE line passing the new prop is the only edit outside `CategoryViewTree.tsx` -- if you need more, it is a row, not a wider grant.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5950-5959 (outside the derived range 5400-5899 that the browser-gated tests use
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

<criterion id="F70-AC1" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F70-AC1` -- the whole portal typechecks.

<criterion id="F70-AC2" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_irpt_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"]' --expect-ground '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div=rgb(255, 255, 255)'</invocation><expect>ASSERT-CONTENT: 1 of 1 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F70-AC2` -- on Holdings, the category-views card renders on a WHITE ground (C3), using the additive light variant: `ASSERT-CONTENT: 1 of 1 met`, `ASSERT-GROUND: 1 of 1 met`. This fixture already reaches the ready state -- `DrillTree.tsx`'s `mdpfResultFromSnapshot` derives it from the `holdings/` snapshot alone, no separate `category-views.json` key is needed for IRPT.

<criterion id="F70-AC3" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_irpt_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"]' --expect-ground '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div=rgb(255, 255, 255)'</invocation><expect>ASSERT-CONTENT: 1 of 1 met[\s\S]*ASSERT-GROUND: 1 of 1 met</expect></criterion>
`F70-AC3` -- the same, at 390.

<criterion id="F70-AC4" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_irpt_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --inject-css '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div{background:#c4cbdb !important; background-image:none !important}' --expect-ground '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div=rgb(255, 255, 255)'</invocation><expect>ASSERT-GROUND: 0 of 1 met</expect></criterion>
`F70-AC4` -- THE GROUND CONTROL: after painting the card silver, the same ground assertion FAILS.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~20-report, closing row `IRPT_FNTEND-W20-S1`):** the original selector
`section[aria-labelledby="asset-category-views"] > div` matched the section's FIRST div child -- the `Eyebrow` heading wrapper
(`space-y-2`, no explicit background), never the card. `TreeBody` returns a React FRAGMENT (no wrapping DOM node), so its own first
child, `<CategoryOverview>`'s root div (`overflow-hidden rounded-[4px] border border-black`), becomes the section's SECOND direct div
child in the real DOM -- and that div itself carries no background (its OWN child does: `bg-white` in the light branch,
`GraphicPanel`'s dark gradient in the other). So the ground line the worker measured (`FAIL null`... no -- confirmed by the worker's
own mutant-revert: identical PASS under `ground="light"` and `ground="dark"`) was reading some ancestor's page-level background the
whole time, discriminating nothing. Verified independently (`2.0.0_SA_COO~F`, fresh dev server): the corrected selector
`section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div` reads `PASS rgb(255, 255, 255)` against the real fixed
build, and a wrong-ground `--inject-css` paint on that SAME selector reads `FAIL rgb(196, 203, 219)` -- it now genuinely
discriminates. The bar is unchanged (still requires a real white ground on the actual card); only the selector is corrected. Row
`IRPT_FNTEND-W20-S1` is CORRECT and stays filed as the record of the defect; this amendment is the remedy it called for.

<criterion id="F70-AC5" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs portfolios <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_mp_before_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-69/fixtures/mp.json</invocation><expect>SAVED</expect></criterion>
`F70-AC5` -- BEFORE capture: Model Portfolios' own category-views card, current HEAD (uses `__tests__/fe-s-69/fixtures/mp.json`, authored by FE-s-69; if FE-s-69 has not landed yet, author your own copy of it -- one key, `category-views.json`, from `.frontend-dev/fixtures/category-views.fixture.json`'s `global` block).

<criterion id="F70-AC6" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs portfolios <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_mp_after_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-69/fixtures/mp.json --expect 'section[aria-labelledby="asset-category-views"]' --expect-style 'section[aria-labelledby="asset-category-views"] .relative::background-image!=none'</invocation><expect>ASSERT-CONTENT: 1 of 1 met[\s\S]*ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F70-AC6` -- AFTER your fix, Model Portfolios' OWN use is UNCHANGED (`ground` defaults to `'dark'`): the card still shows a real gradient background-image. This is the CTO-mandated before/after PROVING THE SIBLING IS UNBROKEN, not a wrong-state control -- read both PNGs and confirm the dark card looks the same in both.

<criterion id="F70-AC7" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F70-AC7` -- `__tests__/fe-s-7/slices.test.ts` and `drill.test.ts` (the two existing tests that reference `CategoryViewTree`) still pass. READ both files first: if either pins the CURRENT dark-card classes, update it in this commit to expect the additive prop's default (unchanged) behaviour.

<criterion id="F70-AC8" cell_refs="FE-s-70" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F70-AC8` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F70-AC9" cell_refs="FE-s-70" judgment="true" drives="none"/>
`F70-AC9` -- graded at L9 by the CVO: the chart legend's data colours (the percent labels, the donut segments) are UNCHANGED in the light variant (C6/C8 exempt, per the CTO's scope correction); the fix is ADDITIVE (a new prop, default preserves Model Portfolios' current behaviour) rather than a second look-alike component; DrillTree.tsx passes the new prop and nothing else about its render changed. RECORD; NO VERDICT.

<expected_criteria>F70-AC1, F70-AC2, F70-AC3, F70-AC4, F70-AC5, F70-AC6, F70-AC7, F70-AC8, F70-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W20-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- DrillTree.tsx's edit is ONE LINE (the `ground` prop on its `<CategoryViewTree>` call): do not restyle anything else in that file, that is cell B's and FE-s-67's surface.

<paths>
portal/src/components/CategoryViewTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-70/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-70`.
<owned_cells>FE-s-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F70-AC1`, `F70-AC2`, `F70-AC3`, `F70-AC4`, `F70-AC5`, `F70-AC6`, `F70-AC7`, `F70-AC8`, `F70-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/IRPT_FNTEND.TO-FE-s-70.categoryviewtree-light-variant-for-drilltree.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F70-AC1,F70-AC2,F70-AC3,F70-AC4,F70-AC5,F70-AC6,F70-AC7,F70-AC8,F70-AC9 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-70.categoryviewtree-light-variant-for-drilltree.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `categoryviewtree-light-variant-for-drilltree.result.md` beside it.
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

Seating: round 11, wave 3, slot ~6.
