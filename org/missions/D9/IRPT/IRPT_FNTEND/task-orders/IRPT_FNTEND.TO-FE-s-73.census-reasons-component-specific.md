# TO IRPT_FNTEND.TO-FE-s-73 -- census reasons: a component-specific need against a named existing candidate, for every NEW entry

<to_id>IRPT_FNTEND.TO-FE-s-73</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~23</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-73` (round 11, v0.11) | **outcome_ref:** FWD-12 | **depends_on:** none (READY ROOT; independent of the visual cells) | **slot:** ~9 | **rows:** W14-S2 | **base:** workspace = the round-11 issuance commit on CLOUD (your worktree branches from it), portal DEV `243089eb` plus every drained round-11 cell this one depends on

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-73` -- census reasons: a component-specific need against a named existing candidate, for every NEW entry.

**The cause is in the census script, not in the components.** `census.ts`'s `extractHeaderComment(fileRel)` (FE-s-11, copied by FE-s-64) takes the FIRST `/** ... */` block of the FILE and uses it as the reason for EVERY component defined in that file. `render/Page.tsx` defines `PageSheet` and `UnnamedReasonCodeFlag` together, so both carry the frame comment (`FE-s-4 -- the page frame both templates share: sheet, header, footer.`), although `UnnamedReasonCodeFlag` has its own JSDoc directly above it (`The flag beside a code the contract does not name. ...`). That is row W14-S2's `copied reason`: a method defect. The same method gives every NEW component in a multi-component file the file's reason, and a role label (`FE-s-N -- <what it is>`) where the leading comment names a feature instead of a need. **Your job:** (1) in YOUR copy, extract each component's OWN leading JSDoc (the block immediately above its `export function Name`), and fall back to the file's block only when the component has none, marking that entry `FILE-LEVEL (shared)`; (2) add a `needs` field to every NEW entry: one sentence naming what this component does that the NEAREST EXISTING candidate cannot, and a `nearestExisting` field naming that candidate (a component that exists in the tree or the REUSED set), so a reviewer can dispute it; (3) state the census's boundary in ONE place in the output (a component used only inside its own file, an entry counted as `self -- no import statement`, and the thin wrappers over REUSED parts `TabShell`, `ClientSearch`, `FirmDropdown`: classify them consistently and say what rule you applied). You have NO source write: every fix is in your copy and its outputs, and a component whose need you cannot state is a finding (one row), never an invented reason. Do not search outside the portal or run any vendor tool.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the
portal needs no re-learning."* Round 10 read it `NOT_REALIZED` (1.0.0_SA_CTO, `CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md`): grounded C3, C8 and C12 violations remain on shipped
surfaces and the Reporting tab's answer-bearing state has never been rendered. Round 11 fixes them and proves each fix on a state that CANNOT pass on the wrong page.

**Your surface.** EVIDENCE ONLY: your deliverables folder (the corrected `census.ts` copy and its `component-census.json` / `.md`) and your own `__tests__/fe-s-73/` (`reasons.test.ts`). NO edit to any component, any test outside `__tests__/fe-s-73/`, or any other cell's surface. Read from FE-s-64's `deliverables/0.9.0_WK_IRPT_FNTEND~14/`; write only to yours.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5980-5989 (outside the derived range 5400-5899 that the browser-gated tests use
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

<criterion id="F73-AC1" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F73-AC1` -- the whole portal typechecks.

<criterion id="F73-AC2" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~23/census.ts; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F73-AC2` -- YOUR corrected copy of the census script, run from your own deliverables folder, exits 0. (Copy FE-s-64's `census.ts` there first; never run FE-s-11's or FE-s-64's original, which would overwrite committed evidence.)

<criterion id="F73-AC3" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~23/census.ts; echo rc=$?</invocation><expect>COMPONENTS: [0-9]+ \(REUSED [0-9]+, NEW [0-9]+\)</expect></criterion>
`F73-AC3` -- the same run prints its denominator line with the REUSED/NEW split.

<criterion id="F73-AC4" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-73/reasons.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F73-AC4` -- your `reasons.test.ts` passes with no failure.

<criterion id="F73-AC5" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-73/reasons.test.ts</invocation><expect>REASONS: (\d+) of \1 NEW entries name a component-specific need and a nearest existing candidate</expect></criterion>
`F73-AC5` -- EVERY NEW entry (the same number twice) carries a `needs` sentence specific to that component and the name of the NEAREST EXISTING component that was considered, with why it cannot serve; the test prints the line only when the counts are equal.

<criterion id="F73-AC6" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-73/reasons.test.ts</invocation><expect>CONTROL: round-10 census FAILS the same check</expect></criterion>
`F73-AC6` -- THE CONTROL: the same check run over FE-s-64's round-10 `component-census.json` (`deliverables/0.9.0_WK_IRPT_FNTEND~14/`) must FAIL, and the test prints this line only if it does. A check that also passes the old census cannot tell a role label from a need.

<criterion id="F73-AC7" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-73/reasons.test.ts</invocation><expect>REASON-COPY: UnnamedReasonCodeFlag differs from PageSheet</expect></criterion>
`F73-AC7` -- `UnnamedReasonCodeFlag`'s reason is its OWN (row W14-S2): it differs from `PageSheet`'s.

<criterion id="F73-AC8" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-73/reasons.test.ts</invocation><expect>CONTROL: round-10 census had identical reasons for UnnamedReasonCodeFlag and PageSheet</expect></criterion>
`F73-AC8` -- THE CONTROL for the copy check: the round-10 JSON DID carry identical reasons for those two, and the test prints this line only if it reads them identical there.

<criterion id="F73-AC9" cell_refs="FE-s-73" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F73-AC9` -- the whole IRPT_FNTEND suite is green (no dev server of yours running; `IRPT_FE_DEV_PORT` unset).

<criterion id="F73-AC10" cell_refs="FE-s-73" judgment="true" drives="none"/>
`F73-AC10` -- graded at L9 by the CVO against the PRD's FWD-12 CONSTRAINT (*a new component requires a stated need the existing set cannot meet; matching appearance alone is not reuse*): each of the NEW entries states a component-specific need against a NAMED existing candidate, the census states its own self-use and wrapper boundary in one place, and any entry you could not justify is a finding, not an excuse. RECORD; NO VERDICT.

<expected_criteria>F73-AC1, F73-AC2, F73-AC3, F73-AC4, F73-AC5, F73-AC6, F73-AC7, F73-AC8, F73-AC9, F73-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO grades it at L9.
  You never self-grade it and you never write "conforms" as a conclusion: you write what the capture and the assertion lines show.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
  `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message file
  written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W23-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion, and do not edit a criterion's expectation: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

- This cell is not a visual cell: the CTO's four-part rule does not apply, and it carries its own controls (F73-AC6, F73-AC8). It starts a dev server for nothing: none is needed.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-73/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.11, cell `FE-s-73`.
<owned_cells>FE-s-73</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F73-AC1`, `F73-AC2`, `F73-AC3`, `F73-AC4`, `F73-AC5`, `F73-AC6`, `F73-AC7`, `F73-AC8`, `F73-AC9`, `F73-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~23/IRPT_FNTEND.TO-FE-s-73.census-reasons-component-specific.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F73-AC1,F73-AC2,F73-AC3,F73-AC4,F73-AC5,F73-AC6,F73-AC7,F73-AC8,F73-AC9,F73-AC10 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-73.census-reasons-component-specific.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `census-reasons-component-specific.result.md` beside it.
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

Seating: round 11, wave 1, slot ~9.
