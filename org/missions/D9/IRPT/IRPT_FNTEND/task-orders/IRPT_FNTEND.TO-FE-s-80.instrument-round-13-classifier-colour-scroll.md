# TO IRPT_FNTEND.TO-FE-s-80 -- instrument round 13 -- template-matching classifier, discriminating colour command, real scroll command

<to_id>IRPT_FNTEND.TO-FE-s-80</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~30</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-80` (round 13, v0.13) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~1 | **rows:** C-S147, C-S166, W27-S2, W27-S3 | **base:** workspace = the round-13 issuance commit on CLOUD (your worktree branches from it), portal DEV `2d7b2f21` (round 12's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-80` -- three real gaps the round-12 CVO's independent review found in the shared instrument and its own recorded criteria, all on
`scripts/ui-smoke.mjs` plus your own test/probe scripts:

**Fix 1, the key classifier (C-S166/C-S147).** `checkKeyValidity`/`routeKeyCandidates` (`scripts/ui-smoke.mjs:182-211`) currently treat a
parameterised `consumed.ts` template (e.g. `GET /api/scoped/investor-reporting/holdings/{accountSetId}`) as valid ONLY when a fixture key equals
the template's STATIC PREFIX exactly (`routeKeyCandidates` truncates at the first `{` and `checkKeyValidity` does `candidates.has(k)`, an exact-set
membership test). A CONCRETE key that actually satisfies the template by carrying a real parameter value after the prefix (e.g.
`/api/scoped/investor-reporting/holdings/A-0001`) is currently rejected -- measured: the round-12-repaired `fixtures/smoke/default.json` (12/12
entries carry `unprojected_grant`, all with concrete account/relationship ids in their keys) scores `KEY-VALIDITY: 5 of 12` against this classifier,
not 12 of 12. Fix the classifier so a concrete key satisfying a parameterised template's prefix ALSO counts as valid -- but a route with NO
`{param}` still requires an EXACT match (widening prefix-matching to static routes would let an unrelated key masquerade as valid; this must NOT
happen).

**Fix 2, the parent-colour command (W27-S2).** The literal receipt-panel colour assertion used in round 12 (`--expect-style
'[data-slot="receipt-panel"]::color=...'`) inherits navy from an ancestor BOTH before and after a real fix to the actual descendant text node --
the assertion cannot tell the two states apart, so a passing run proves nothing. Read `export/ReceiptPanel.tsx` yourself, find the ACTUAL element
whose own `color` the navy fix changed (not a wrapping container that merely inherits it), and build a corrected `--expect-style` invocation on
that descendant selector. Prove it discriminates: the positive assertion PASSES on the real build, and a wrong-colour control
(`--inject-css` overriding that SAME descendant selector to an obviously wrong colour) FAILS.

**Fix 3, the visibility/scroll command (W27-S3).** The literal preview-visibility assertion used in round 12 (`--expect
'[data-slot="preview-scroll"]'`) only proves the scrollable container EXISTS, never that a scroll actually occurred -- re-running it verbatim
cannot reproduce the real `0->792` displacement `__tests__/fe-s-77/scroll-driver.mjs` separately demonstrated. Build a REUSABLE scroll-exercise
script under your own `__tests__/fe-s-80/` (adapt the `scroll-driver.mjs` pattern: `ui-smoke.mjs`'s own browser/route/auth-stub mechanism, then a
real `element.scrollLeft = element.scrollWidth - element.clientWidth` displacement, before/after captures, before/after content assertions) that
works against AN ARBITRARY horizontally-scrollable container passed by selector -- not hard-coded to the export modal. Prove it against the export
modal's own preview container as your acceptance evidence (the same scenario W27-S3 originally failed on). **This is the instrument `FE-s-84`
needs for `F78-AC7` in wave 2** -- write it so a sibling cell can invoke it against a DIFFERENT container (the Reporting tab's 390px report body)
without modification beyond the selector argument.

**Your surface.** `scripts/ui-smoke.mjs` (hardening, not a rewrite) and your own `__tests__/fe-s-80/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5960-5964 (outside the derived range 5400-5899 the browser-gated tests use,
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

<criterion id="F80-AC1" cell_refs="FE-s-80" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F80-AC1` -- the whole portal typechecks.

<criterion id="F80-AC2" cell_refs="FE-s-80" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-80/key-classifier.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F80-AC2` -- a unit-level test (built by you) directly exercises the corrected classifier with THREE named controls, each printed: a POSITIVE (a concrete key that satisfies a real parameterised template, e.g. a holdings/account-id key against the holdings template), a NEGATIVE (a key matching NO template at all), and a WRONG-SHAPE key (resembles a route but matches none) -- and a printed denominator (`N of N controls correct`).

<criterion id="F80-AC3" cell_refs="FE-s-80" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~30/f80_holdings_key_validity.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/default.json --click Holdings</invocation><expect>KEY-VALIDITY: 12 of 12 valid consumed\.ts operation keys</expect></criterion>
`F80-AC3` -- END-TO-END proof the classifier fix applies in the real instrument: the round-12-repaired `default.json` fixture (12/12 entries, concrete parameterised keys) now reads `KEY-VALIDITY: 12 of 12`, not `5 of 12`.

<criterion id="F80-AC4" cell_refs="FE-s-80" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-80/scroll-instrument.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F80-AC4` -- a test (built by you) proves your new reusable scroll-exercise script performs a REAL displacement (captured before/after `scrollLeft` values, non-equal) against the export modal's preview container, and that before/after content assertions differ (previously off-screen content becomes visible) -- printed verbatim.

<criterion id="F80-AC5" cell_refs="FE-s-80" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F80-AC5` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F80-AC6" cell_refs="FE-s-80" judgment="true" drives="none"/>
`F80-AC6` -- graded at L9 by the CVO: the classifier's parameterised-template widening is correct and does not also widen static-route matching; the parent-colour command's discrimination (wrong-colour control genuinely FAILs) is real, not asserted; the scroll instrument is genuinely reusable (selector-parameterised, not hard-coded) and its displacement is real. RECORD; NO VERDICT.
<expected_criteria>F80-AC1, F80-AC2, F80-AC3, F80-AC4, F80-AC5, F80-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W30-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **This is the round's sole wave-1 root that wave 2 depends on.** `FE-s-82`/`FE-s-83`/`FE-s-84` all wait on this cell's drain -- land it cleanly, do not leave `ui-smoke.mjs` in a half-fixed state.
- **No new production defect is authored here.** `checkKeyValidity` widening must NOT accept a static (no-`{param}`) route by prefix -- that would be a NEW false-pass class, not a fix.

<paths>
portal/scripts/ui-smoke.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-80/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.13, cell `FE-s-80`.
<owned_cells>FE-s-80</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F80-AC1`, `F80-AC2`, `F80-AC3`, `F80-AC4`, `F80-AC5`, `F80-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-80.instrument-round-13-classifier-colour-scroll.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F80-AC1,F80-AC2,F80-AC3,F80-AC4,F80-AC5,F80-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-80.instrument-round-13-classifier-colour-scroll.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `instrument-round-13-classifier-colour-scroll.result.md` beside it.
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

Seating: round 13, wave 1, slot ~FE-s-80.
