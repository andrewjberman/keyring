# TO IRPT_FNTEND.TO-FE-s-66 -- fixture classification: retire the dead, keep the adapter-plane four, author the answer-bearing pair

<to_id>IRPT_FNTEND.TO-FE-s-66</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~16</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-66` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** none (READY ROOT, but FE-s-68 depends on your two authored fixtures existing before it can run) | **slot:** ~2 | **rows:** W11-S1, W12-S1 (this cell); W11-S2 (its precondition) | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-66` -- fixture classification: retire the dead, keep the adapter-plane four, author the answer-bearing pair.

**Sixteen of the twenty fixture files in `fixtures/smoke/` are dead**, rows `W11-S1`/`W12-S1`: they are keyed by retired operation names (`resolve-scope`, `performance-report`, `holdings-snapshot`) and their BODIES are also in the old in-process adapter shape (`{schemaVersion, scope, revision, availability, ...}`), never the wire envelope (`{contract_version, operation, firm_id, data, status?, unprojected_grant}`) `contracts/wire/consumed.ts` names. "Repair in place" would mean reshaping every body, not renaming keys, and a census over the WHOLE portal tree (not just this project) found ZERO consumers of these 16: fe-s-10-global.json, fe-s-10-one-firm.json, fe-s-7-smartx.json, fe-s-7-cottonwood.json, fe-s-9-modal.json, fe-s-9-preview.json, fe-s-11-print.json, fe-s-2-default.json, fe-s-2-one-firm.json, fe-s-3-failed.json, fe-s-5-49f-bd.json, fe-s-5-cottonwood-bd.json, fe-s-5-inflection-orion.json, fe-s-6-needs-correction.json, fe-s-6-uncertain.json, fe-s-8-narrative.json. **DELETE them.** Four fixtures are genuinely used by tests OUTSIDE your grant in their OWN (adapter-plane) shape and must be LEFT UNTOUCHED: fe-s-6-ready.json (__tests__/fe-s-34/no-status.test.ts:63); fe-s-3-loading.json (__tests__/fe-s-39/adapter-plane.test.ts:57); fe-s-4-performance.json, fe-s-4-analysis.json (__tests__/fe-s-4/manifest.test.ts:205-206). Verify this census yourself before deleting anything (re-grep the whole portal tree, not just IRPT_FNTEND) and if you find a consumer this order missed, keep that file and file a row instead of deleting it.

**The Reporting tab's answer-bearing state has never been rendered** (row `W11-S2`, and FE-s-68's whole cell depends on it). `tabs/reporting/ReportingTab.tsx`'s `isAnswerBearing(report.availability)` needs the performance response's `status` half present (`state: 'READY'`, plus `operation`, `source_dates.business_date`, `actions: []`, `public_reason_code`) AND envelope-level `unprojected_grant` on every key (`contracts/envelope.ts:277-281`). `__tests__/fe-s-63/fixtures/export-ready.json` already has both -- copy it into `fixtures/smoke/reporting-answer-bearing.json` verbatim (all three keys: `directory/resolve`, `performance/`, `holdings/`). Then make a SECOND file, `reporting-answer-bearing-partial.json`, identical except `directory/resolve`'s `unprojected_grant` becomes `{"count": 2, "denominator": 5, "kinds": ["accounts"]}` -- that is what drives `header/ScopeSummary.tsx`'s partial-disclosure fact (`scope.availability.unprojectedGrant.count > 0`), which FE-s-68 needs. Do not build a THIRD variant unless a criterion above needs one.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** `fixtures/smoke/` (delete the 16, add the 2 authored files) and your own `__tests__/fe-s-66/` (`smoke-classification.test.ts`). No component or test outside your grant.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5910-5919 (outside the derived range 5400-5899 that the browser-gated tests use
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

<criterion id="F66-AC1" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F66-AC1` -- the whole portal typechecks.

<criterion id="F66-AC2" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-66/smoke-classification.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F66-AC2` -- `smoke-classification.test.ts` passes.

<criterion id="F66-AC3" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-66/smoke-classification.test.ts</invocation><expect>SMOKE FILES: (\d+); WIRE-KEYED: (\d+); ADAPTER-PLANE: 4; UNCLASSIFIED: 0</expect></criterion>
`F66-AC3` -- the classification guard prints its denominator: every remaining file in `fixtures/smoke/` is either WIRE-KEYED (every key begins `/api/scoped/investor-reporting/` and matches a template in `contracts/wire/consumed.ts`) or the 4-file ADAPTER-PLANE allowlist (`fe-s-6-ready.json`, `fe-s-3-loading.json`, `fe-s-4-performance.json`, `fe-s-4-analysis.json`); UNCLASSIFIED is 0.

<criterion id="F66-AC4" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-66/smoke-classification.test.ts</invocation><expect>SEEDED-UNCLASSIFIED: correctly flagged</expect></criterion>
`F66-AC4` -- THE CONTROL: the test seeds one throwaway unclassified file into a temp copy of the directory (never into the real `fixtures/smoke/`) and asserts the same classifier flags it, proving UNCLASSIFIED: 0 above is not vacuous.

<criterion id="F66-AC5" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34 src/pages/InvestorReporting/__tests__/fe-s-39 src/pages/InvestorReporting/__tests__/fe-s-4</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F66-AC5` -- the three suites that consume the kept adapter-plane fixtures are still green after the retirement.

<criterion id="F66-AC6" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~16/f66_ac6.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json</invocation><expect>FIXTURES-MATCH: matched (\d+) of \1(?![0-9])</expect></criterion>
`F66-AC6` -- your authored answer-bearing fixture (built from `__tests__/fe-s-63/fixtures/export-ready.json`, which already carries `status.state=READY` and `unprojected_grant` on all three keys) matches every key it declares.

<criterion id="F66-AC7" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~16/f66_ac7.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing-partial.json</invocation><expect>FIXTURES-MATCH: matched (\d+) of \1(?![0-9])</expect></criterion>
`F66-AC7` -- your partial variant (the same fixture with `directory/resolve`'s `unprojected_grant` set to `count=2, denominator=5, kinds:["accounts"]`) also matches every key.

<criterion id="F66-AC8" cell_refs="FE-s-66" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F66-AC8` -- the whole IRPT_FNTEND suite is green (dev server stopped, `IRPT_FE_DEV_PORT` unset in that shell).

<criterion id="F66-AC9" cell_refs="FE-s-66" judgment="true" drives="none"/>
`F66-AC9` -- graded at L9 by the CVO: the 16 retired fixtures truly have zero consumers (a census over the whole portal tree, not just IRPT_FNTEND, quoted with its denominator), the 2 authored fixtures are read and their `FIXTURES-MATCH` lines quoted, and the classification test's control (F66-AC4) genuinely proves the guard can fail. RECORD; NO VERDICT.

<expected_criteria>F66-AC1, F66-AC2, F66-AC3, F66-AC4, F66-AC5, F66-AC6, F66-AC7, F66-AC8, F66-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W16-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- FE-s-68 depends on your `reporting-answer-bearing*.json` files; land this cell first or hand them over before FE-s-68 runs.

<paths>
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-66/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-66`.
<owned_cells>FE-s-66</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F66-AC1`, `F66-AC2`, `F66-AC3`, `F66-AC4`, `F66-AC5`, `F66-AC6`, `F66-AC7`, `F66-AC8`, `F66-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~16/IRPT_FNTEND.TO-FE-s-66.fixture-classification-and-answer-bearing-authoring.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F66-AC1,F66-AC2,F66-AC3,F66-AC4,F66-AC5,F66-AC6,F66-AC7,F66-AC8,F66-AC9 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-66.fixture-classification-and-answer-bearing-authoring.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `fixture-classification-and-answer-bearing-authoring.result.md` beside it.
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

Seating: round 11, wave 2, slot ~2.
