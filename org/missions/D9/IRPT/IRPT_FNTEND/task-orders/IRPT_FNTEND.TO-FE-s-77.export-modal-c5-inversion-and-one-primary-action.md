# TO IRPT_FNTEND.TO-FE-s-77 -- export modal's actual C5 navy inversion, exercised scroll reachability, and one primary action on the received view

<to_id>IRPT_FNTEND.TO-FE-s-77</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~27</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-77` (round 12, v0.12) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-74 | **slot:** ~4 | **rows:** C-S148, C-S151 | **base:** workspace = the round-12 issuance commit on CLOUD (your worktree branches from it), portal DEV `5c8a9ba9` plus FE-s-74's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-77` -- close TWO real gaps the CVO's round-11 read found underneath round 11's export-modal fix: C-S148 (the ordered C5
navy inversion was NOT delivered -- `ExportModal.tsx` uses `text-slate-900/500/400` and slate borders, never the navy-role
transformation the criterion required) and C-S151 (the received view shows BOTH `Download` and `Create export` as filled-purple
simultaneously -- two primary actions, C8 permits one).

**Fix, C5 inversion.** Replace every `slate-*` ink/border class this round's own fix introduced inside the modal region with its navy
equivalent per DESIGN.md's inversion rule (round 11's cell text already named the pattern: navy text on white, per C5). BEFORE and
AFTER captures required -- round 11's worker supplied only a source-diff, never an actual BEFORE screenshot; this cell corrects that.

**Fix, scroll reachability.** Round 11's `scrollWidth`/`clientWidth`/`overflowX` reading proved CAPACITY (the content is wider than the
viewport) but never EXERCISED reachability (an actual scroll to the far edge, re-captured). This cell performs a real scroll (e.g. via a
Playwright-driven helper or the existing `holdings-driver.mjs`-style mechanism, adapted) and captures the far-edge content itself, not
merely its potential.

**Fix, one primary action.** On the RECEIVED view only, demote ONE of `Download`/`Create export` to the existing secondary
`buttonClass('secondary', 'canvas', 'sm')` (the same idiom FE-s-67 used for StatusPanel's safe-action button last round) so exactly ONE
filled-primary remains. Do not touch the idle/submitting/received STATE SPLIT itself (S69 is REMEDIATED and closed; this cell fixes
styling only, not the flow-state logic).

**Your surface.** `export/` (the whole folder, same grant round 11's FE-s-71 held) and your own `__tests__/fe-s-77/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5930-5939 (outside the derived range 5400-5899 the browser-gated tests use):
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

<criterion id="F77-AC1" cell_refs="FE-s-77" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F77-AC1` -- the whole portal typechecks.

<criterion id="F77-AC2" cell_refs="FE-s-77" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~27/f77_idle_before.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export</invocation><expect>SAVED</expect></criterion>
`F77-AC2` -- BEFORE capture: the idle modal at your worktree's OWN HEAD, before this cell's inversion fix -- keep it as the record round 11 never actually supplied.

<criterion id="F77-AC3" cell_refs="FE-s-77" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~27/f77_idle_after.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect-style '[data-slot="receipt-panel"]::color=rgb(22, 51, 114)' --expect-style '[data-slot="receipt-panel"]::color!=rgb(100, 116, 139)'</invocation><expect>ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F77-AC3` -- AFTER: the modal's ink is genuinely navy, no longer slate -- both the positive navy assertion and the negative not-slate-500 assertion must hold together.

<criterion id="F77-AC4" cell_refs="FE-s-77" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~27/f77_preview_far_edge.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export --expect '[data-slot="preview-scroll"]'</invocation><expect>ASSERT-CONTENT: 1 of 1 met</expect></criterion>
`F77-AC4` -- an ACTUAL scroll to the far edge of the preview is exercised (not merely measured for capacity) and the far-edge content is captured in this PNG -- read it yourself and confirm content that was off-screen in the BEFORE-scroll state is now visible.

<criterion id="F77-AC5" cell_refs="FE-s-77" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~27/f77_received_one_primary.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-71/fixtures/export-flow.json --click Export --click 'Create export' --clickwait 3000 --expect '[data-slot="download-link"][class*="hsl(var(--primary))"]' --expect '[data-slot="submit-export"][class*="hsl(var(--primary))"]'</invocation><expect>ASSERT-CONTENT: 1 of 2 met</expect></criterion>
`F77-AC5` -- on the received view, EXACTLY ONE of Download/Create-export carries the filled-primary class -- adjust the selectors to your actual implementation's class names if these literal ones do not match your build; the requirement is the COUNT (1 of 2, never 0 or 2), not these exact strings.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~27-report, row `IRPT_FNTEND-W27-S4`):** the literal selectors (`class*="5F3BE3"`, `.bg-primary`)
never match this build's actual filled-primary idiom -- `ReceiptPanel.tsx`'s `download-link` and `ExportModal.tsx`'s `submit-export` both use
`bg-[hsl(var(--primary))]`, a CSS-custom-property arbitrary value, containing neither substring. Worker `~27` measured `ASSERT-CONTENT: 0 of 2
met` on the literal selectors and, separately, `1 of 2 met` on an adapted pair (`class*="hsl(var(--primary))"`) at the received state, with a
wrong-state control at the IDLE state reading the OPPOSITE pattern (confirming genuine discrimination, not a vacuous match). Fix: swap the two
literal selectors above for the adapted pair; the bar itself (exactly one of two, never 0 or 2) is unchanged.

<criterion id="F77-AC6" cell_refs="FE-s-77" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F77-AC6` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~27-report, row `IRPT_FNTEND-W27-S1`):** worker `~27`'s own in-grant, correctly-ordered fix
(`ReceiptPanel.tsx`'s public-reason-code class, `text-slate-700` -> the ratified `text-[#6B7280]`, per this cell's own "replace every slate-*
ink/border class" mandate) breaks `__tests__/fe-s-42/every-site.test.ts:322`'s `reasonLineBefore()` helper, which hard-codes the OLD class
string byte-for-byte and compares it with `===`. This is a stale byte-pinned reference to a class this round's own ratified work is correctly
retiring, not a defect in FE-s-77's fix. **Grant widened by exactly one file, for exactly one edit:** `<paths>` below now also names
`portal/src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts`, authorizing ONLY updating `reasonLineBefore()`'s hard-coded
`text-slate-700` string to `text-[#6B7280]` (matching the class this cell's own fix now emits) -- nothing else in that file. Confirm `bun test
src/pages/InvestorReporting` reads `0 fail` afterward.

<criterion id="F77-AC7" cell_refs="FE-s-77" judgment="true" drives="none"/>
`F77-AC7` -- graded at L9 by the CVO: the C5 inversion is genuinely delivered (not merely a source diff claim), the scroll reachability is EXERCISED not measured, and exactly one primary action survives on the received view. RECORD; NO VERDICT.

<expected_criteria>F77-AC1, F77-AC2, F77-AC3, F77-AC4, F77-AC5, F77-AC6, F77-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W27-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

<paths>
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/__tests__/fe-s-77/
portal/src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.12, cell `FE-s-77`.
<owned_cells>FE-s-77</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F77-AC1`, `F77-AC2`, `F77-AC3`, `F77-AC4`, `F77-AC5`, `F77-AC6`, `F77-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-77.export-modal-c5-inversion-and-one-primary-action.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F77-AC1,F77-AC2,F77-AC3,F77-AC4,F77-AC5,F77-AC6,F77-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-77.export-modal-c5-inversion-and-one-primary-action.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `export-modal-c5-inversion-and-one-primary-action.result.md` beside it.
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

Seating: round 12, wave 2, slot ~FE-s-77.
