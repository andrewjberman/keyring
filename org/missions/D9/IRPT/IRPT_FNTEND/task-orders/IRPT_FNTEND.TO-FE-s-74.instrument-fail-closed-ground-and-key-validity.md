# TO IRPT_FNTEND.TO-FE-s-74 -- the instrument's fail-closed ground measurement and key-validity/fulfilment split

<to_id>IRPT_FNTEND.TO-FE-s-74</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~24</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-74` (round 12, v0.12) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT, every round-12 cell depends on this | **slot:** ~1 | **rows:** W20-S2, C-S146, C-S147 | **base:** workspace = the round-12 issuance commit on CLOUD (your worktree branches from it), portal DEV `5c8a9ba9`

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-74` -- the instrument's own two false-pass classes (W20-S2, C-S146) plus the key-validity/fulfilment split (C-S147).

**Facts, all independently re-derived by the CVO's own production-function probe (not a browser render), then re-confirmed by this
issuer at the same source lines.** `groundColor()` (`scripts/ui-smoke.mjs`) reads only `getComputedStyle(el).backgroundColor` and
regex-parses it with an `rgba?\(` pattern. Two classes of real paint defeat it silently: (1) a composited/gradient background set via
`background-image` (a dark `GraphicPanel`'s own paint) leaves `backgroundColor` transparent, so the walker keeps climbing past the
actual surface to whatever solid-colour ancestor it eventually finds; (2) a browser-reported `oklch(...)` (or `lab(...)`/`color(...)`)
computed-style string never matches the `rgba?\(` pattern at all, so it is silently skipped exactly like a transparent value, and the
walk again climbs past the real element. Separately, `--expect-style`'s inequality branch (`!=`) computes `firstMatch === null` as
satisfying `!= expected` (since `null !== expected` is `true`), so an absent selector reads a false `PASS`. And `FIXTURES-MATCH` counts
which declared URLs were actually hit (fulfilment) but never checks whether those keys are real `contracts/wire/consumed.ts` operation
keys (validity) -- an arbitrary invalid key like `/api/` can read `matched 1 of 1`.

**Fix, additive, in `scripts/ui-smoke.mjs` only:**
1. In the ground walker: before accepting a background as the answer, confirm it is a plain solid, single-layer, RGB-parseable value.
   If the current element's own `backgroundImage` is anything other than `none`, or its `backgroundColor` fails the `rgba?\(` parse
   AND is non-empty/non-transparent, STOP THE WALK THERE and print `EXPECT-GROUND[<css>]: UNMEASURABLE <raw-value>`, exit non-zero.
   Never silently continue climbing past it.
2. In the style-inequality branch: if the selector's `firstMatch` is `null`, print `EXPECT-STYLE[<css>::<property>]: UNMEASURABLE` on
   EITHER operator (`=` or `!=`), never a `PASS`/`FAIL` computed from a null actual value.
3. Add a `KEY-VALIDITY: <k> of <N> valid consumed.ts operation keys` summary line: for every key in the `--fixtures` file, check it
   against the operation keys `contracts/wire/consumed.ts` actually declares (read the file, do not hand-maintain a duplicate list).
   Keep `FIXTURES-MATCH` (fulfilment) exactly as it is today -- this is a SEPARATE, additive line, not a replacement.

**Your surface.** `scripts/ui-smoke.mjs` and your own `__tests__/fe-s-74/`. Every design fix this round depends on your hardened
instrument; nothing else in the portal is yours to touch.

**THE CRITERION RULE (round 11's four parts, PLUS the CTO's round-11 addition, binding on every VISUAL criterion this round).**
**(a) WIRE MATCH** -- the fixture's keys equal the operation keys in `contracts/wire/consumed.ts`; the run prints `FIXTURES-MATCH: matched N of N`.
**(b) NAMED CONTENT** -- the specific cards, values or text the state must show, asserted by selector or text (`--expect`, `--expect-text`), never by eye.
**(c) A WRONG-STATE NEGATIVE CONTROL** -- the same content assertions run against the failed or unresolved state; they must print `ASSERT-CONTENT: 0 of N met`.
**(d) GROUND MEASURED ON THE ACTUAL CONTAINER** -- `--expect-ground` on the element that carries the surface, not the page field, with a wrong-ground control
(`--inject-css` a silver `#c4cbdb` onto that container; the same assertion must print `FAIL rgb(196, 203, 219)`).
**(e) ABSENT-SELECTOR CONTROL (NEW, CTO round-11 ruling)** -- run the same style/ground assertion against a state where the target element genuinely does
not exist; the HARDENED instrument must print `UNMEASURABLE` (never a vacuous PASS on either the equality or the inequality branch).
A criterion missing any of the five is refused at the cut. A PNG is still read by you (a grep cannot see contrast), but it is a JUDGMENT input, never the
pass/fail line.

**THE INSTRUMENT, HARDENED by FE-s-74 (your worktree already carries the hardened version -- if `ui-smoke.mjs` still reads white for a gradient or an
opaque OKLCH background, or still prints `PASS null` for an absent-selector inequality, STOP: your base is the OLD instrument, report it).**
Flags on `scripts/ui-smoke.mjs` (repeatable; quote each argument with single quotes; a selector is CSS):
- `--expect '<css>'` prints `EXPECT[<css>]: PASS (<n> visible)` or `EXPECT[<css>]: FAIL (0 visible)`.
- `--expect-text '<css>::<text>'` (case-sensitive substring of the FIRST match's `innerText`) prints `EXPECT-TEXT[<css>::<text>]: PASS|FAIL`.
- `--expect-style '<css>::<property><op><value>'` (`=` or `!=`) prints `EXPECT-STYLE[<css>::<property>]: PASS|FAIL <actual>` -- **HARDENED: if `<css>`
  resolves to NOTHING, this now prints `UNMEASURABLE`, on EITHER operator, never `PASS null`.**
- `--expect-ground '<css>=<rgb(r, g, b)>'` (the nearest self-or-ancestor NON-TRANSPARENT background) prints `EXPECT-GROUND[<css>]: PASS|FAIL <actual>` --
  **HARDENED: an unsupported or composited paint (a CSS gradient via `background-image`, an opaque `oklch(...)`/`lab(...)`/`color(...)` value the
  RGB-only reader cannot parse, or any multi-layer background) now prints `UNMEASURABLE` and the process exits non-zero. It never silently reports the
  nearest RGB ancestor as if it were the target's own ground.**
- `--inject-css '<css text>'` adds a `<style>` after load and before the expectations: a wrong-state control, nothing else.
- `--delay '<url-substring>=<ms>'` (repeatable) holds a matching fixture response for `<ms>` before fulfilling it.
- Summary lines `ASSERT-CONTENT: <met> of <total> met`, `ASSERT-STYLE: ...`, `ASSERT-GROUND: ...`. `FIXTURES-MATCH: matched <M> of <N>` (fulfilment,
  URL-hit counting) is now ACCOMPANIED by a separate `KEY-VALIDITY: <k> of <N> valid consumed.ts operation keys` line (validity) -- the two are
  DIFFERENT questions and the instrument no longer conflates them. `--strict` exits 1 on any failed OR UNMEASURABLE expectation.
- Old flags still work: `--fail <url-substring>`, `--click`, `--fill`, `--width`.
- `CANVAS:`/`TEXT:` lines are unchanged and are NOT the bar.
Colour values: navy `#163372` = `rgb(22, 51, 114)`; primary `#5F3BE3` = `rgb(95, 59, 227)`; white = `rgb(255, 255, 255)`; canvas `#F4F6FA` = `rgb(244, 246, 250)`;
band `#0A1733` = `rgb(10, 23, 51)`; hairline `#C4CBDB` = `rgb(196, 203, 219)`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's FWD-12 ENDPOINT row
   (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v8.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5900-5909 (outside the derived range 5400-5899 the browser-gated tests use):
   `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, in the background, INLINE PREFIX, NEVER exported. Test with `curl` first; that
   number is `<PORT>`. Sibling workers run at the same time: never 5175.
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

<criterion id="F74-AC1" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F74-AC1` -- the whole portal typechecks.

<criterion id="F74-AC2" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_gradient.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --inject-css '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2){background-image:linear-gradient(180deg,#0A1733,#163372) !important; background-color:transparent !important}' --expect-ground '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2)=rgb(255, 255, 255)'</invocation><expect>UNMEASURABLE</expect></criterion>
`F74-AC2` -- a real CSS gradient injected onto a container prints `UNMEASURABLE`, never a silently-climbed-past white. This is the exact W20-S2 shape, now caught.

<criterion id="F74-AC3" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_oklch.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --inject-css '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2){background-color:oklch(0.5 0.15 250) !important; background-image:none !important}' --expect-ground '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2)=rgb(255, 255, 255)'</invocation><expect>UNMEASURABLE</expect></criterion>
`F74-AC3` -- an opaque OKLCH background prints `UNMEASURABLE`, never a silently-climbed-past white. This is C-S146/the CVO's own reproduced defect, now caught. If your browser's computed-style serialization does not report `oklch(...)` literally for this property, measure and record its ACTUAL serialization first (a bare `getComputedStyle` read), then adjust the injected value so the parse genuinely fails as intended -- do not assume the string without checking.

<criterion id="F74-AC4" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_absent_ground.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --expect-ground '[data-slot="this-selector-matches-nothing-f74"]=rgb(255, 255, 255)'</invocation><expect>UNMEASURABLE</expect></criterion>
`F74-AC4` -- a genuinely absent ground selector prints `UNMEASURABLE`, never a silent PASS or a misleading FAIL against some other element's colour.

<criterion id="F74-AC5" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_wrong_ground_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --inject-css '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div{background:#c4cbdb !important}' --expect-ground '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div=rgb(255, 255, 255)'</invocation><expect>FAIL rgb\(196, 203, 219\)</expect></criterion>
`F74-AC5` -- REGRESSION CONTROL: an ordinary solid wrong-colour paint still reads a normal `FAIL <actual>`, never `UNMEASURABLE` -- the hardening only catches genuinely unmeasurable paints, it does not turn every wrong colour into UNMEASURABLE.

<criterion id="F74-AC6" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_ineq_absent.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --expect-style '[data-slot="this-selector-matches-nothing-f74"]::background-color!=rgb(95, 59, 227)'</invocation><expect>UNMEASURABLE</expect></criterion>
`F74-AC6` -- the `!=` inequality branch against an absent selector prints `UNMEASURABLE`, never `PASS null` -- the exact C-S146 defect, now caught.

<criterion id="F74-AC7" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_ineq_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect-style '[data-slot="holdings-breadcrumb"]::color!=rgb(0, 128, 0)'</invocation><expect>PASS</expect></criterion>
`F74-AC7` -- REGRESSION CONTROL: an inequality check against a REAL, resolved element still PASSes/FAILs normally on its actual computed value, never UNMEASURABLE. Compared against an arbitrary reference colour (green, `rgb(0, 128, 0)`) that this element is NEVER expected to be, under any of this round's rulings -- this is deliberately NOT the breadcrumb's own current-vs-navy colour question (that is FE-s-76's cell, still pending when this order runs), so the control stays valid regardless of which colour the breadcrumb carries when you run it.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~24-report):** the ORIGINAL comparator (`!=rgb(95, 59, 227)`, the breadcrumb's own current indigo) was a defect of mine, not the instrument's: it silently assumed FE-s-76's not-yet-landed navy fix had already landed. Worker `~24` correctly refused rather than self-grading past it (`EXPECT-STYLE[...]: FAIL rgb(95, 59, 227)` is a TRUE, correctly-discriminating result -- the breadcrumb genuinely IS still indigo, per `DrillTree.tsx:188`'s own `text-[hsl(var(--primary))]` class, confirmed independently by this issuer at that exact line), then ran an adapted comparator (navy) to prove the underlying inequality mechanism itself works correctly regardless. Row `IRPT_FNTEND-W24-S1` is CORRECT and stays filed; this amendment (a comparator that can never coincide with either the current or the FE-s-76-ruled colour) is the remedy it called for -- the criterion's SUBSTANCE (a resolved element's inequality check behaves normally, never UNMEASURABLE) is unchanged.

<criterion id="F74-AC8" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_keyvalid_bad.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-74/fixtures/one-bad-key.json</invocation><expect>KEY-VALIDITY: [0-9]+ of [0-9]+ valid</expect></criterion>
`F74-AC8` -- author `__tests__/fe-s-74/fixtures/one-bad-key.json`: a byte-copy of any existing smoke fixture with ONE key changed to a string that is NOT a `consumed.ts` operation key (e.g. `/api/scoped/investor-reporting/not-a-real-route`). `KEY-VALIDITY` reads `k of N` with `k < N` (strictly fewer valid than declared) -- print and read the exact numbers, do not assume.

<criterion id="F74-AC9" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_keyvalid_good.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json</invocation><expect>KEY-VALIDITY: 9 of 9 valid</expect></criterion>
`F74-AC9` -- POSITIVE CONTROL: an all-valid, already-established fixture (`fe-s-18-holdings-observed.json`, 9 declared keys) reads `9 of 9 valid` -- confirm the count against the fixture's own declared key count, do not hardcode 9 if the file's actual count differs.

<criterion id="F74-AC10" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~24/f74_fulfilment_unchanged.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings</invocation><expect>FIXTURES-MATCH: matched [0-9]+ of [0-9]+</expect></criterion>
`F74-AC10` -- REGRESSION CONTROL: the existing `FIXTURES-MATCH` (fulfilment) line still prints in its old shape, unreplaced -- validity is additive, not a rewrite.

<criterion id="F74-AC11" cell_refs="FE-s-74" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F74-AC11` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F74-AC12" cell_refs="FE-s-74" judgment="true" drives="none"/>
`F74-AC12` -- graded at L9 by the CVO: the hardening is genuinely ADDITIVE -- every round-11 order's invocation shape (plain `--expect`/`--expect-text`/`--expect-ground`/`--inject-css` against ordinary solid colours) behaves identically to before; only the two named false-pass classes and the validity/fulfilment split are new. RECORD; NO VERDICT.

<expected_criteria>F74-AC1, F74-AC2, F74-AC3, F74-AC4, F74-AC5, F74-AC6, F74-AC7, F74-AC8, F74-AC9, F74-AC10, F74-AC11, F74-AC12</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W24-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

<paths>
portal/scripts/ui-smoke.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-74/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.12, cell `FE-s-74`.
<owned_cells>FE-s-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F74-AC1`, `F74-AC2`, `F74-AC3`, `F74-AC4`, `F74-AC5`, `F74-AC6`, `F74-AC7`, `F74-AC8`, `F74-AC9`, `F74-AC10`, `F74-AC11`, `F74-AC12`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-74.instrument-fail-closed-ground-and-key-validity.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F74-AC1,F74-AC2,F74-AC3,F74-AC4,F74-AC5,F74-AC6,F74-AC7,F74-AC8,F74-AC9,F74-AC10,F74-AC11,F74-AC12 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-74.instrument-fail-closed-ground-and-key-validity.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `instrument-fail-closed-ground-and-key-validity.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- REMEDIATION_v8.md @631b1308cb, ADJUDICATION_v3.md's C-S1xx rows, and CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_11_20260922.md @ce01e0f219, all read at HEAD.
the spec: RUN -- PRD FWD-12's ENDPOINT row and the CTO's round-11 analysis read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 12, wave 1, slot ~FE-s-74.
