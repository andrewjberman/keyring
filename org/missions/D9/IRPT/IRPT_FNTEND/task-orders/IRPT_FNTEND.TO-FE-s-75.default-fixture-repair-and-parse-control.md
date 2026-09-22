# TO IRPT_FNTEND.TO-FE-s-75 -- default smoke fixture repair (or retirement) and a parse control

<to_id>IRPT_FNTEND.TO-FE-s-75</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~25</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-75` (round 12, v0.12) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-74 | **slot:** ~2 | **rows:** W17-S3 | **base:** workspace = the round-12 issuance commit on CLOUD (your worktree branches from it), portal DEV `5c8a9ba9` plus FE-s-74's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-75` -- repair (or retire) `fixtures/smoke/default.json` (W17-S3): all 12 of its declared entries omit `unprojected_grant`, so
`contracts/envelope.ts`'s `parseIrEnvelope` throws `EnvelopeMismatch('unprojected_grant', ...)` UNCONDITIONALLY against it -- any cell
that uses this fixture as a "clean, resolved" control (F67-AC3's original use) actually exercises a parse error, not a resolved state.

**Fix.** Census every consumer of `default.json` in the tree (source, tests, scripts) FIRST and print the denominator -- if it has zero
real consumers left after round 11's fixture-family migrations (FE-s-66 retired 16 dead fixtures the same way), the correct fix may be
RETIREMENT, not repair; if it has live consumers, add `unprojected_grant: {"count": 0, "denominator": 1, "kinds": []}` (or the shape
`envelope.ts` actually requires -- read `isUnprojectedGrantShaped` first) to all 12 entries. Either way, add a parse-control unit test
that feeds every entry through `parseIrEnvelope` and asserts it does NOT throw (or, if retired, asserts the file no longer exists and no
source references it).

**Your surface.** `fixtures/smoke/default.json` and your own `__tests__/fe-s-75/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5910-5919 (outside the derived range 5400-5899 the browser-gated tests use):
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

<criterion id="F75-AC1" cell_refs="FE-s-75" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F75-AC1` -- the whole portal typechecks.

<criterion id="F75-AC2" cell_refs="FE-s-75" drives="none"><invocation>cd <WS>/portal && grep -rn "fixtures/smoke/default.json\|smoke/default'\|smoke/default\"" src/ --include='*.ts' --include='*.tsx' | wc -l</invocation><expect>^[0-9]+$</expect></criterion>
`F75-AC2` -- CENSUS: count every consumer reference to `default.json` in the tree; print and read the exact number before deciding repair vs retire.

<criterion id="F75-AC3" cell_refs="FE-s-75" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~25/f75_default_clean.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/default.json --expect '[data-slot="scope-error"]' --expect-text '[data-slot="scope-error"]::Scope could not be resolved'</invocation><expect>ASSERT-CONTENT: 0 of 2 met</expect></criterion>
`F75-AC3` -- if default.json is REPAIRED (kept): the same control F67-AC3 originally wanted now genuinely reads clean (0 of 2, no parse-error-driven false content). If default.json is RETIRED instead, report this criterion as N/A with the retirement evidence, not a fabricated invocation.

<criterion id="F75-AC4" cell_refs="FE-s-75" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-75</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F75-AC4` -- the authored parse-control test (every default.json entry parses clean via parseIrEnvelope, or the retirement is asserted) passes.

<criterion id="F75-AC5" cell_refs="FE-s-75" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F75-AC5` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

<criterion id="F75-AC6" cell_refs="FE-s-75" judgment="true" drives="none"/>
`F75-AC6` -- graded at L9 by the CVO: repair-vs-retire was the right call given the measured consumer census; no other fixture family was silently touched. RECORD; NO VERDICT.

<expected_criteria>F75-AC1, F75-AC2, F75-AC3, F75-AC4, F75-AC5, F75-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W25-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

<paths>
portal/src/pages/InvestorReporting/fixtures/smoke/default.json
portal/src/pages/InvestorReporting/__tests__/fe-s-75/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.12, cell `FE-s-75`.
<owned_cells>FE-s-75</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F75-AC1`, `F75-AC2`, `F75-AC3`, `F75-AC4`, `F75-AC5`, `F75-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-75.default-fixture-repair-and-parse-control.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F75-AC1,F75-AC2,F75-AC3,F75-AC4,F75-AC5,F75-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-75.default-fixture-repair-and-parse-control.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `default-fixture-repair-and-parse-control.result.md` beside it.
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

Seating: round 12, wave 2, slot ~FE-s-75.
