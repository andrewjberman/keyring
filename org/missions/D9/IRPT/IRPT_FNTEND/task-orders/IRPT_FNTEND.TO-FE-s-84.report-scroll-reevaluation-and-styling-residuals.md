# TO IRPT_FNTEND.TO-FE-s-84 -- F78-AC7 re-evaluated with the real scroll instrument + report styling residuals finished

<to_id>IRPT_FNTEND.TO-FE-s-84</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~34</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-84` (round 13, v0.13) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-80 | **slot:** ~5 | **rows:** F78-AC7, C-S150 | **base:** workspace = the round-13 issuance commit on CLOUD (your worktree branches from it), portal DEV `2d7b2f21` (round 12's close) plus FE-s-80's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-84` -- two residuals on `tabs/reporting/`, both carried from round 12:

**Fix 1, re-evaluate F78-AC7 (currently NOT_EVALUATED).** Round 12's 390px report capture was never actually scrolled -- the committed screenshot
is a single, unscrolled frame, so the CVO correctly recorded `NOT_EVALUATED` rather than guessing at clipping. Use `FE-s-80`'s new reusable
scroll-exercise script (`__tests__/fe-s-80/`, built in wave 1 -- read it first, it is written to take an arbitrary scrollable-container selector)
against the report body's actual scrollable element at 390px width. Commit BOTH a before-scroll and an after-scroll capture, and assert that
identifiable content invisible in the before-capture is visible in the after-capture (read both PNGs yourself; a grep cannot see this). Clipping is
NOT declared unless it is exercised -- if the real scroll reaches all content with nothing permanently cut off, say so; do not invent a clipping
finding to have something to report.

**Fix 2, finish the report styling (C-S150).** `AnswerStatus.tsx:67-68` still carries noncanonical `slate-200`/`slate-900` (the base/complete state)
and `amber-500`/`amber-50`/`amber-950` (the qualified/warning state) -- none of these are DESIGN.md-named tokens. Replace each with the correct
named role: the base/complete state's ink and border move to C3's navy-on-white idiom (matching every other panel in this project); the
qualified/warning state needs a role that reads as a WARNING without inventing a new accent -- read DESIGN.md's `colors:` frontmatter for the
closest correct named role (do not invent one). **Do not invent summary card values the wire shape does not carry** -- the UNAVAILABLE cards stay
UNAVAILABLE; this fix is styling only, never fabricated content.

**Your surface.** `tabs/reporting/` (the whole folder, the same grant FE-s-78 held) and your own `__tests__/fe-s-84/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5980-5984 (outside the derived range 5400-5899 the browser-gated tests use,
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

<criterion id="F84-AC1" cell_refs="FE-s-84" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F84-AC1` -- the whole portal typechecks.

<criterion id="F84-AC2" cell_refs="FE-s-84" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~34/f84_report_390_before_scroll.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect '[data-slot="reporting-body"]'</invocation><expect>ASSERT-CONTENT: 1 of 1 met</expect></criterion>
`F84-AC2` -- BEFORE capture at 390px, unscrolled -- the baseline your after-capture is read against.

<criterion id="F84-AC3" cell_refs="FE-s-84" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-84/report-scroll-exercise.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F84-AC3` -- a test (built by you, invoking FE-s-80's reusable scroll-exercise script against the report body's actual scrollable container at 390px) proves a REAL displacement occurred and that content invisible before is present after -- printed verbatim, matching the pattern FE-s-80 itself used to prove its own script against the export modal.

<criterion id="F84-AC4" cell_refs="FE-s-84" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~34/f84_answer_status_navy.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect-style '[data-slot="answer-status"]::color=rgb(22, 51, 114)' --expect-style '[data-slot="answer-status"]::border-color!=rgb(226, 232, 240)'</invocation><expect>ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F84-AC4` -- the base/complete `AnswerStatus` state measures navy ink and a border that is no longer the noncanonical slate-200 value.

<criterion id="F84-AC5" cell_refs="FE-s-84" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~34/f84_answer_status_qualified.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json --expect-style '[data-slot="answer-status"]::background-color!=rgb(255, 251, 235)'</invocation><expect>ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F84-AC5` -- the qualified/warning `AnswerStatus` state's background is no longer the noncanonical `amber-50` value -- named-role replacement, cited to its DESIGN.md clause in your result.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~34-report, row `IRPT_FNTEND-W34-S1`):** the named fixture `fixtures/smoke/fe-s-32/qualified.json` does not
exist anywhere in the repo (confirmed: no `fixtures/smoke/fe-s-32/` directory at all) -- the literal invocation crashes with `ENOENT` before any
assertion runs. No other committed static fixture under `fixtures/smoke/` gives the Reporting route's performance operation a qualified
(PARTIAL/NEEDS_CORRECTION/UNCERTAIN) state either, so this was never a real path. Worker `~34` authored a correct substitute in its own grant,
`__tests__/fe-s-84/fixtures/reporting-qualified.json` (a one-field mutation of the committed `reporting-answer-bearing.json`, `performance.status.state`
READY->PARTIAL -- the same technique `__tests__/fe-s-40/band-at-390.test.ts`'s own `qualifiedReportingMap()` already uses, made static), and measured
`ASSERT-STYLE: 1 of 1 met` against it -- independently reproduced by me, identical result. Amended the fixture path to that file; the bar is
unchanged.

<criterion id="F84-AC6" cell_refs="FE-s-84" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F84-AC6` -- the whole IRPT_FNTEND suite is green.

<criterion id="F84-AC7" cell_refs="FE-s-84" judgment="true" drives="none"/>
`F84-AC7` -- graded at L9 by the CVO: F78-AC7's re-evaluation genuinely exercised a scroll (not merely re-measured capacity); no clipping claim is made without exercise; the styling replacements are real DESIGN.md-named roles, not invented ones; no summary card value was fabricated. RECORD; NO VERDICT.
<expected_criteria>F84-AC1, F84-AC2, F84-AC3, F84-AC4, F84-AC5, F84-AC6, F84-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W34-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **Read `FE-s-80`'s scroll-exercise script before building anything of your own** -- reuse it, do not build a second, incompatible one.
- **Fixture names in AC2/AC4/AC5 are illustrative** -- verify they exist and carry the right shape in your worktree; if `fe-s-32/qualified.json` is not the right fixture for the qualified state, use the correct one and say so in your result.
- **Do not invent a clipping finding** to have something to report on AC3 -- if the real scroll reaches everything, the correct, honest record is that F78-AC7 is now genuinely evaluated and clean.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/__tests__/fe-s-84/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.13, cell `FE-s-84`.
<owned_cells>FE-s-84</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F84-AC1`, `F84-AC2`, `F84-AC3`, `F84-AC4`, `F84-AC5`, `F84-AC6`, `F84-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-84.report-scroll-reevaluation-and-styling-residuals.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F84-AC1,F84-AC2,F84-AC3,F84-AC4,F84-AC5,F84-AC6,F84-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-84.report-scroll-reevaluation-and-styling-residuals.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `report-scroll-reevaluation-and-styling-residuals.result.md` beside it.
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

Seating: round 13, wave 2, slot ~FE-s-84.
