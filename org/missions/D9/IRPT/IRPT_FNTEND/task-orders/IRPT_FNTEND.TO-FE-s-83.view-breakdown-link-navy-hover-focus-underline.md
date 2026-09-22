# TO IRPT_FNTEND.TO-FE-s-83 -- View-breakdown link re-hued navy, hover/focus underline, focus ring stays indigo

<to_id>IRPT_FNTEND.TO-FE-s-83</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~33</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-83` (round 13, v0.13) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-80 | **slot:** ~4 | **rows:** C-S165 | **base:** workspace = the round-13 issuance commit on CLOUD (your worktree branches from it), portal DEV `2d7b2f21` (round 12's close) plus FE-s-80's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-83` -- one residual FE-s-76 correctly found and left out of its own grant, recorded rather than silently fixed (round 12): the light-ground
"View breakdown" action link in `CategoryViewTree.tsx` still renders the site's indigo (`linkColor` at `:574`, applied at `:677`). FE-s-76's own
corrected comment (round 12) now accurately states there is NO C8 exemption for this -- C8 spends indigo on exactly ONE persistent primary action
per view plus six named identity places (page-title, header subtext, active tab, sidebar active item, rail edge, avatar; DESIGN.md `:352-361`),
and this label (a `<span>` styled to look like a link, inside a clickable tile -- "a label, not a second button", per the file's own `:668` comment)
is neither.

**Fix.** Change `linkColor`'s light-ground branch (`:574`, currently `'hsl(var(--palette-indigo))'`) to navy `#163372`. Add an underline on
hover/focus -- since the label itself is not independently focusable (the WHOLE TILE is the interactive element, per the file's own comment), the
underline must respond to the ANCESTOR'S hover/focus state (a `group-hover:underline`/`group-focus-visible:underline` pattern, or whatever
mechanism actually reaches this label given the real DOM -- verify empirically, do not assume `group` is already wired correctly for THIS specific
label). The label's REST state carries no underline (matching `DrillTree.tsx`'s breadcrumb link pattern, round 12 -- an at-rest underline is a
persistent accent spend C8 does not authorize here). **The focus ring itself stays indigo** (C11, a TRANSIENT focus indicator, not a persistent
accent spend) -- do not touch focus-ring styling.

**Your surface.** `components/CategoryViewTree.tsx` (the `linkColor`/View-breakdown label only -- no other change) and your own `__tests__/fe-s-83/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5975-5979 (outside the derived range 5400-5899 the browser-gated tests use,
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

<criterion id="F83-AC1" cell_refs="FE-s-83" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F83-AC1` -- the whole portal typechecks.

<criterion id="F83-AC2" cell_refs="FE-s-83" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~33/f83_view_breakdown_rest.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect-style '[data-slot="view-breakdown-link"]::color=rgb(22, 51, 114)' --expect-style '[data-slot="view-breakdown-link"]::color!=rgb(95, 59, 227)'</invocation><expect>ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F83-AC2` -- AT REST: the label measures navy `rgb(22, 51, 114)`, and explicitly NOT the site indigo `rgb(95, 59, 227)` -- both the positive and the negative assertion, on the same capture. Add a `data-slot="view-breakdown-link"` attribute to the label if it does not already carry one your selector can target.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~33-report, row `IRPT_FNTEND-W33-S1`):** `model-portfolios` is not a real route (`App.tsx:413-423`
declares `/portfolios`, not `/model-portfolios`; the literal invocation lands on `/market`, 0 of 9 fixtures ever match, every assertion reads
`UNMEASURABLE`). Independently confirmed further: even the REAL route (`/portfolios`) would not reach this fix -- `ModelPortfolios.tsx:1286` mounts
`CategoryViewTree` at the DEFAULT `ground='dark'`, never `'light'`; the only caller passing `ground="light"` is `DrillTree.tsx:244`, reached at
`/investor-reporting` after clicking Holdings. Amended to that route/fixture/click, exactly the worker's own supplementary invocation, which
measured `PASS rgb(22, 51, 114)` on both the positive and negative assertion. The bar is unchanged, only the route/fixture were wrong.

<criterion id="F83-AC3" cell_refs="FE-s-83" drives="none"><invocation>cd <WS>/portal && IRPT_FE_DEV_PORT=<PORT> timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-83/hover-underline.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F83-AC3` -- ON HOVER (of the ancestor tile, whichever mechanism you build): the label gains an underline. Exercise the actual hover state your driver produces -- a static capture with no hover simulation does not satisfy this.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~33-report, row `IRPT_FNTEND-W33-S1`):** the literal invocation carried the same broken route AND,
independently, `ui-smoke.mjs` has no generic hover-only mechanism at all (`--click` always fires a real `.click()`, which opens `HeroDialog` and
measurably breaks the tile's own `:hover` state -- confirmed: the identical selector flips from PASS to FAIL under the dialog overlay). This is a
second, genuine instrument gap, correctly worked around within this cell's own grant: `__tests__/fe-s-83/hover-underline-driver.mjs` (the
established per-cell-driver idiom this suite already uses eight times) clicks the Holdings TAB (never the tile), then performs a REAL
`page.hover()` on the label's ancestor button, reading `text-decoration-line` at rest / during hover / after release -- a genuine MUTANT-controlled
3-of-3 result. Amended to run that test directly rather than a raw `ui-smoke.mjs` invocation that structurally cannot reach a hover state. Bar
unchanged (the underline must genuinely appear on hover), only the instrument is corrected.

<criterion id="F83-AC4" cell_refs="FE-s-83" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~33/f83_view_breakdown_absent_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --expect-style '[data-slot="view-breakdown-link"]::color!=rgb(95, 59, 227)'</invocation><expect>UNMEASURABLE</expect></criterion>
`F83-AC4` -- ABSENT-SELECTOR CONTROL: against a fixture/route where this label genuinely does not mount, the same inequality reads `UNMEASURABLE`, never a vacuous PASS.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~33-report, row `IRPT_FNTEND-W33-S1`):** the literal invocation's `UNMEASURABLE` result TEXTUALLY
matched `<expect>` but VACUOUSLY -- the selector was absent because the whole route was broken (same defect as AC2/AC3), not because this specific
fixture/route combination genuinely withholds the category tiles while otherwise rendering correctly. The worker correctly graded this FAIL rather
than self-grade a vacuous match as a real control, per this round's own "a control is a claim" discipline. Amended to the SAME route as AC2
(`investor-reporting`, `fe-s-18-holdings-observed.json`) but WITHOUT `--click Holdings` -- so the Holdings tab, and therefore this label, never
mounts, for the genuine reason. Bar unchanged, only the route is corrected and the omitted click makes the absence real.

<criterion id="F83-AC5" cell_refs="FE-s-83" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F83-AC5` -- the whole IRPT_FNTEND suite is green (a test elsewhere pinning the old indigo value against this label, if any, is updated in this commit and named in your result).

<criterion id="F83-AC6" cell_refs="FE-s-83" judgment="true" drives="none"/>
`F83-AC6` -- graded at L9 by the CVO: the recolour is genuinely navy, genuinely not indigo, the hover/focus underline is genuinely exercised (not merely measured for capability), and the focus ring itself is confirmed untouched (still indigo, C11). RECORD; NO VERDICT.
<expected_criteria>F83-AC1, F83-AC2, F83-AC3, F83-AC4, F83-AC5, F83-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W33-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`CategoryViewTree.tsx` grant is the `linkColor`/View-breakdown label only** -- do not touch the dark-ground branch (`LILAC_LIGHT`), the card fill/hover animation, the data palette (C6), or Model Portfolios' dark default.
- **Route/fixture in AC2-AC4 are illustrative** -- `CategoryViewTree` may mount under a different route than `model-portfolios` in this worktree; verify and adjust, the requirement is the colour/underline discrimination, not these exact route/fixture names.

<paths>
portal/src/components/CategoryViewTree.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-83/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.13, cell `FE-s-83`.
<owned_cells>FE-s-83</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F83-AC1`, `F83-AC2`, `F83-AC3`, `F83-AC4`, `F83-AC5`, `F83-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-83.view-breakdown-link-navy-hover-focus-underline.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F83-AC1,F83-AC2,F83-AC3,F83-AC4,F83-AC5,F83-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-83.view-breakdown-link-navy-hover-focus-underline.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `view-breakdown-link-navy-hover-focus-underline.result.md` beside it.
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

Seating: round 13, wave 2, slot ~FE-s-83.
