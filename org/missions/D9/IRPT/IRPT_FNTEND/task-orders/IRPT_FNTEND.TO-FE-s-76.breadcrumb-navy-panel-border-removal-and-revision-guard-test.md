# TO IRPT_FNTEND.TO-FE-s-76 -- DrillTree breadcrumb NAVY + CategoryViewTree panel-border removal + the revision-mismatch component test

<to_id>IRPT_FNTEND.TO-FE-s-76</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~26</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-76` (round 12, v0.12) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-74 | **slot:** ~3 | **rows:** C-S149, W17-S1 | **base:** workspace = the round-12 issuance commit on CLOUD (your worktree branches from it), portal DEV `5c8a9ba9` plus FE-s-74's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-76` -- two CTO rulings tied to the SAME DESIGN.md clause (C8, `:352-361`): the Holdings breadcrumb's colour (C-S149), and
`CategoryViewTree.tsx:936`'s panel-border removal, PLUS the revision-mismatch guard's component-level test (W17-S1).

**Ruling, breadcrumb.** C8 spends `#5F3BE3` (indigo) on exactly ONE persistent primary action per view plus six named identity places
(page-title rule, header subtext, active tab, sidebar active item, rail edge, avatar) -- *"not a chip fill, not a panel border"*. A
tree-navigation breadcrumb is none of these. Fix `DrillTree.tsx`'s breadcrumb: ink is **navy `#163372`**; the CURRENT (non-link) segment
is distinguished by WEIGHT, not colour; LINK segments take an underline on hover and on focus; the focus ring stays indigo (C11,
transient, not a persistent accent).

**Ruling, panel border.** The SAME clause decides `CategoryViewTree.tsx:936`'s indigo top rule: it is a panel border, so it is REMOVED
entirely. The in-code comments at `:563-570` and `:665-666` claiming an invented "one-accent-link allowance" are FALSE -- correct them to
state the actual rule (no generic accent-link exemption exists in C8). The data palette (lilac/teal/amber, C6) and Model Portfolios'
existing dark default are UNTOUCHED.

**Ruling, W17-S1 (the unreachable revision-mismatch branch).** `adaptHoldingsSnapshot` assigns ONE `sourceSetRevision` to every node, so
no truthful wire payload can ever produce the mismatch the `PanelError` guard (DrillTree.tsx:~234) catches. KEEP the guard as
defence-in-depth. Cover it at the COMPONENT level only: a unit test that either drives the adapter's real output or seeds the component
directly with a mismatched revision, and asserts `PanelError` renders. Do NOT invent a wire field, do NOT author a fixture that pretends
the backend emits one, and do NOT claim a browser rendered this state -- record it as unreachable-by-construction, citing the adapter
line, exactly as round 11's `W17-S1` row already established.

**Your surface.** `tabs/holdings/DrillTree.tsx` (the breadcrumb ONLY -- every other line in this file, including its C12 error text from
round 11, is out of your grant), `components/CategoryViewTree.tsx` (the `:936` rule and the `:563-570`/`:665-666` comments ONLY), and
your own `__tests__/fe-s-76/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5920-5929 (outside the derived range 5400-5899 the browser-gated tests use):
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

<criterion id="F76-AC1" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F76-AC1` -- the whole portal typechecks.

<criterion id="F76-AC2" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~26/f76_breadcrumb_navy.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect '[data-slot="holdings-breadcrumb"]' --expect-style '[data-slot="holdings-breadcrumb"]::color=rgb(22, 51, 114)'</invocation><expect>ASSERT-CONTENT: 1 of 1 met[\s\S]*ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F76-AC2` -- the breadcrumb's at-rest ink is navy, not indigo/purple.

<criterion id="F76-AC3" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~26/f76_breadcrumb_absent.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --expect '[data-slot="holdings-breadcrumb"]'</invocation><expect>ASSERT-CONTENT: 0 of 1 met</expect></criterion>
`F76-AC3` -- ABSENT-SELECTOR CONTROL (part e): with no `--click Holdings`, the breadcrumb is genuinely absent, not merely unstyled.

<criterion id="F76-AC4" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~26/f76_categoryview_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --expect-style '[data-slot="holdings-drill-tree"] section[aria-labelledby="asset-category-views"] > div:nth-of-type(2) > div > div::background-color!=rgb(95, 59, 227)'</invocation><expect>ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F76-AC4` -- the `:936` indigo top rule no longer paints the light CategoryViewTree card at either width; adapt the selector to whatever element actually carried the rule if this exact path does not resolve -- read the PNG and the source together.

<criterion id="F76-AC5" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && grep -c 'one-accent-link' src/components/CategoryViewTree.tsx; echo rc=$?</invocation><expect>^0</expect></criterion>
`F76-AC5` -- the false 'one-accent-link allowance' comment text no longer appears anywhere in the file (corrected to state the actual C8 rule).

<criterion id="F76-AC6" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-76</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F76-AC6` -- the authored component-level test drives or seeds a mismatched revision and asserts `PanelError` renders -- W17-S1's guard, covered at the component level, never claimed as browser-reachable.

<criterion id="F76-AC7" cell_refs="FE-s-76" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F76-AC7` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F76-AC8" cell_refs="FE-s-76" judgment="true" drives="none"/>
`F76-AC8` -- graded at L9 by the CVO: the breadcrumb and panel-border fixes cite C8 correctly; the data palette and Model Portfolios' dark default are confirmed untouched; the revision-mismatch test does not invent a wire field or claim browser reachability. RECORD; NO VERDICT.

<expected_criteria>F76-AC1, F76-AC2, F76-AC3, F76-AC4, F76-AC5, F76-AC6, F76-AC7, F76-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W26-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/components/CategoryViewTree.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-76/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.12, cell `FE-s-76`.
<owned_cells>FE-s-76</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F76-AC1`, `F76-AC2`, `F76-AC3`, `F76-AC4`, `F76-AC5`, `F76-AC6`, `F76-AC7`, `F76-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-76.breadcrumb-navy-panel-border-removal-and-revision-guard-test.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F76-AC1,F76-AC2,F76-AC3,F76-AC4,F76-AC5,F76-AC6,F76-AC7,F76-AC8 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-76.breadcrumb-navy-panel-border-removal-and-revision-guard-test.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `breadcrumb-navy-panel-border-removal-and-revision-guard-test.result.md` beside it.
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

Seating: round 12, wave 2, slot ~FE-s-76.
