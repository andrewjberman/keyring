# TO IRPT_FNTEND.TO-FE-s-82 -- breadcrumb weight 700 + a genuinely MOUNTED revision-mismatch guard test

<to_id>IRPT_FNTEND.TO-FE-s-82</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~32</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-82` (round 13, v0.13) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-80 | **slot:** ~3 | **rows:** C-S164, W17-S1 | **base:** workspace = the round-13 issuance commit on CLOUD (your worktree branches from it), portal DEV `2d7b2f21` (round 12's close) plus FE-s-80's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-82` -- two residuals the CTO's round-12/round-13 rulings left open on `DrillTree.tsx`'s breadcrumb, both completing rulings from earlier
rounds:

**Fix 1, breadcrumb weight (C-S164).** `DrillTree.tsx:188`'s current (non-link) breadcrumb segment carries `font-semibold` -- Tailwind's
`font-semibold` utility is WEIGHT 600. DESIGN.md's C1 clause allows only 400 and 700; the CTO's ruling is explicit that the current crumb takes
700, the others take 400 (this is the round-11 "current crumb by WEIGHT" judgment call FINALLY pinned to a number). Change `font-semibold` to
`font-bold` (Tailwind's 700 utility) at `DrillTree.tsx:188`. Measure the ACTUAL computed `font-weight` (not the class name) against both the
current and a link segment.

**Fix 2, a genuinely MOUNTED integration test (W17-S1).** `__tests__/fe-s-76/revision-mismatch-guard.test.ts` (round 12) constructs `PanelError`
DIRECTLY (`createElement(PanelError, {{...}})`, `:95`/`:129`) -- it proves `PanelError`'s own rendering is correct, but never proves `DrillTree`
ITSELF decides to render `PanelError` when a real revision mismatch occurs. The CTO's round-11 ruling asked for "component level"; this predicate-only
test does not meet it. UPGRADE the existing test file (do not replace it -- keep whatever of its content still tests something real) to ALSO mount
the actual `DrillTree` component (not `PanelError` directly) with a `HoldingsSnapshot`/`HoldingsNode` pair whose provenance revision disagrees (the
exact mismatch shape `DrillTree.tsx:~234`'s `data-slot="holdings-drill-refused"` branch checks for), and assert that `PanelError`'s named content
appears in `DrillTree`'s OWN rendered output -- proving the conditional branch inside `DrillTree` itself gets taken, not just that `PanelError`
renders when constructed by hand. Browser coverage stays "not reachable by construction" (unchanged ruling) -- this is a component-level, no-DOM
test, same instrument class as the existing file.

**Your surface.** `tabs/holdings/DrillTree.tsx` (the breadcrumb weight class ONLY -- no other change), `__tests__/fe-s-76/` (the existing test file,
upgraded in place), and your own `__tests__/fe-s-82/`.

**THE CRITERION RULE (round 12's five parts, unchanged, binding on every VISUAL criterion this round).**
**(a) WIRE MATCH** -- the fixture's keys equal the operation keys in `contracts/wire/consumed.ts`; the run prints `FIXTURES-MATCH: matched N of N`.
**(b) NAMED CONTENT** -- the specific cards, values or text the state must show, asserted by selector or text (`--expect`, `--expect-text`), never by eye.
**(c) A WRONG-STATE NEGATIVE CONTROL** -- the same content assertions run against the failed or unresolved state; they must print `ASSERT-CONTENT: 0 of N met`.
**(d) GROUND MEASURED ON THE ACTUAL CONTAINER** -- `--expect-ground` on the element that carries the surface, not the page field, with a wrong-ground control
(`--inject-css` a silver `#c4cbdb` onto that container; the same assertion must print `FAIL rgb(196, 203, 219)`).
**(e) ABSENT-SELECTOR CONTROL** -- run the same style/ground assertion against a state where the target element genuinely does not exist; the
instrument must print `UNMEASURABLE` (never a vacuous PASS on either the equality or the inequality branch).
A criterion missing any of the five is refused at the cut. A PNG is still read by you (a grep cannot see contrast), but it is a JUDGMENT input, never the
pass/fail line.

**THE INSTRUMENT (your worktree carries FE-s-74's round-12 hardening -- if `ui-smoke.mjs` still reads white for a gradient or an opaque OKLCH
background, or still prints `PASS null` for an absent-selector inequality, STOP: your base is the OLD instrument, report it. Wave-2 cells: if
FE-s-80's round-13 classifier/colour/scroll fixes are not yet in your worktree base, STOP -- your base is stale, wait for the drain).**
Flags on `scripts/ui-smoke.mjs` (repeatable; quote each argument with single quotes; a selector is CSS):
- `--expect '<css>'` prints `EXPECT[<css>]: PASS (<n> visible)` or `EXPECT[<css>]: FAIL (0 visible)`.
- `--expect-text '<css>::<text>'` (case-sensitive substring of the FIRST match's `innerText`) prints `EXPECT-TEXT[<css>::<text>]: PASS|FAIL`.
- `--expect-style '<css>::<property><op><value>'` (`=` or `!=`) prints `EXPECT-STYLE[<css>::<property>]: PASS|FAIL <actual>` -- if `<css>` resolves to
  NOTHING, this prints `UNMEASURABLE`, on EITHER operator, never `PASS null`.
- `--expect-ground '<css>=<rgb(r, g, b)>'` (the nearest self-or-ancestor NON-TRANSPARENT background) prints `EXPECT-GROUND[<css>]: PASS|FAIL <actual>` --
  an unsupported or composited paint (a CSS gradient via `background-image`, an opaque `oklch(...)`/`lab(...)`/`color(...)` value the RGB-only reader
  cannot parse, or any multi-layer background) prints `UNMEASURABLE` and exits non-zero.
- `--inject-css '<css text>'` adds a `<style>` after load and before the expectations: a wrong-state control, nothing else.
- `--delay '<url-substring>=<ms>'` (repeatable) holds a matching fixture response for `<ms>` before fulfilling it.
- Summary lines `ASSERT-CONTENT: <met> of <total> met`, `ASSERT-STYLE: ...`, `ASSERT-GROUND: ...`. `FIXTURES-MATCH: matched <M> of <N>` (fulfilment,
  URL-hit counting) is ACCOMPANIED by a separate `KEY-VALIDITY: <k> of <N> valid consumed.ts operation keys` line (validity, FE-s-80's round-13 fix
  for wave 2 -- a concrete key satisfying a parameterised template now counts as valid, not just the bare prefix).
- Old flags still work: `--fail <url-substring>`, `--click`, `--fill`, `--width`.
- `CANVAS:`/`TEXT:` lines are unchanged and are NOT the bar.
Colour values: navy `#163372` = `rgb(22, 51, 114)`; primary `#5F3BE3` = `rgb(95, 59, 227)`; white = `rgb(255, 255, 255)`; canvas `#F4F6FA` = `rgb(244, 246, 250)`;
band `#0A1733` = `rgb(10, 23, 51)`; hairline `#C4CBDB` = `rgb(196, 203, 219)`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's FWD-12 ENDPOINT row
   (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v9.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5970-5974 (outside the derived range 5400-5899 the browser-gated tests use,
   and outside round 12's 5900-5959): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, in the background, INLINE PREFIX, NEVER
   exported. Test with `curl` first; that number is `<PORT>`. Sibling workers run at the same time: never 5175.
3. **Run each invocation and READ every PNG** it saves. Record per capture: file, viewport, the RAW `FIXTURES-MATCH`/`KEY-VALIDITY`, `EXPECT*` and
   `ASSERT-*` lines verbatim, the DESIGN.md clauses you read it against, and what you saw.
4. **A control is a claim.** Before you trust a passing assertion, run its wrong-state arm (AND its absent-selector arm, part (e)) and confirm both
   fail/UNMEASURABLE as required. If a control passes when it should fail, the assertion cannot tell the states apart: say so and fix it, never
   report it as met.
5. **Stop your dev server before the whole-suite criterion and verify the port closed** (`curl` returns `000`). Run the suite where
   `IRPT_FE_DEV_PORT` is unset.
6. **Fixes.** A defect on YOUR write surface may be fixed with a BEFORE capture kept and an AFTER beside it, one fix per finding, cited to its
   clause. A defect needing another cell's file is ONE surprise row, never a wider grant. A test inside your grant pinning OLD behaviour you are
   correcting is updated in the same commit and named in your result.
7. **Result file** (`<slug>.result.md` in your deliverables folder), FIXTURE-FED disclosure paragraph first, as every prior round.
8. **Keep your context small:** read at most the PNGs your criteria need; write long outputs to files and read their tails.


### ACCEPTANCE

<criterion id="F82-AC1" cell_refs="FE-s-82" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F82-AC1` -- the whole portal typechecks.

<criterion id="F82-AC2" cell_refs="FE-s-82" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~32/f82_breadcrumb_weights.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --clicktext 'Models#3' --expect-style 'span[data-slot="holdings-breadcrumb"]::font-weight=700' --expect-style 'button[data-slot="holdings-breadcrumb"]::font-weight!=700'</invocation><expect>ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F82-AC2` -- the CURRENT (last) breadcrumb segment measures computed weight 700; a LINK (non-current) segment does not -- both assertions on the same capture, positive and negative together.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~32-report, row `IRPT_FNTEND-W32-S1`):** the literal invocation's `--click Holdings` alone lands on the
ROOT node, whose breadcrumb has exactly ONE segment -- so `:last-of-type` and `:first-of-type` both resolve to that SAME single `<span>`
(measured: `PASS 700` / `FAIL 700`, `ASSERT-STYLE: 1 of 2 met`, genuinely not 2 of 2). `:last-of-type`/`:first-of-type` are also structurally wrong
for a global first/last selection -- they scope per parent wrapper, never across the whole breadcrumb. Fix, per the worker's own probe (confirmed
independently by me, live): add a real drill step, `--clicktext 'Models#3'` (disambiguates from two other elements sharing the text "Models" --
the CategoryViewTree card and the recharts Legend), reaching a genuinely two-segment breadcrumb; and TAG-qualify the selectors
(`span[data-slot="holdings-breadcrumb"]` for the current, non-link segment vs. `button[data-slot="holdings-breadcrumb"]` for a link segment,
matching `DrillTree.tsx`'s actual markup) instead of the never-discriminating pseudo-classes. Re-measured: `PASS 700` / `PASS 400`,
`ASSERT-STYLE: 2 of 2 met`. Fix 1 itself (`font-semibold` -> `font-bold`) is unchanged and was never in question; only the invocation's drill depth
and selectors were wrong.

<criterion id="F82-AC3" cell_refs="FE-s-82" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~32/f82_breadcrumb_absent_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --expect-style '[data-slot="holdings-breadcrumb"]::font-weight!=700'</invocation><expect>UNMEASURABLE</expect></criterion>
`F82-AC3` -- ABSENT-SELECTOR CONTROL: against a fixture with no breadcrumb rendered at all, the same inequality reads `UNMEASURABLE`, never a vacuous PASS.

<criterion id="F82-AC4" cell_refs="FE-s-82" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-76</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F82-AC4` -- the upgraded test file passes: the NEW mounted-`DrillTree` case asserts `PanelError`'s named content appears in `DrillTree`'s own rendered output for a real provenance mismatch, alongside whatever of the existing direct-construction assertions still hold.

<criterion id="F82-AC5" cell_refs="FE-s-82" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F82-AC5` -- the whole IRPT_FNTEND suite is green.

<criterion id="F82-AC6" cell_refs="FE-s-82" judgment="true" drives="none"/>
`F82-AC6` -- graded at L9 by the CVO: the breadcrumb weight is genuinely 700 (measured, not assumed from the class name); the upgraded test genuinely mounts `DrillTree` and exercises its own conditional branch, not `PanelError` in isolation. RECORD; NO VERDICT.
<expected_criteria>F82-AC1, F82-AC2, F82-AC3, F82-AC4, F82-AC5, F82-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W32-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`DrillTree.tsx` grant is the breadcrumb weight class only** -- do not touch the link colours, the panel structure, or anything else in this file; those are settled (round 12).
- **AC2/AC3's selectors are illustrative** -- adjust to your actual DOM structure if `:last-of-type`/`:first-of-type` do not resolve to the current/link segments; the requirement is the WEIGHT discrimination (current=700, link!=700), not these exact selector strings.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-76/
portal/src/pages/InvestorReporting/__tests__/fe-s-82/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.13, cell `FE-s-82`.
<owned_cells>FE-s-82</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F82-AC1`, `F82-AC2`, `F82-AC3`, `F82-AC4`, `F82-AC5`, `F82-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-82.breadcrumb-weight-700-and-mounted-revision-guard-test.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F82-AC1,F82-AC2,F82-AC3,F82-AC4,F82-AC5,F82-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-82.breadcrumb-weight-700-and-mounted-revision-guard-test.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `breadcrumb-weight-700-and-mounted-revision-guard-test.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- REMEDIATION_v9.md @d5f199a499, ADJUDICATION_v4.md's C-S1xx rows, and CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_12_20260922.md @94680a3bf2, all read at HEAD.
the spec: RUN -- PRD FWD-12's ENDPOINT row and the CTO's round-12 analysis read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 13, wave 2, slot ~FE-s-82.
