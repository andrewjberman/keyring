# TO IRPT_FNTEND.TO-FE-s-78 -- cohort chip radius with a truthful fixture, plus screen-report styling and exercised narrow-width reachability

<to_id>IRPT_FNTEND.TO-FE-s-78</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~28</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-78` (round 12, v0.12) | **outcome_ref:** FWD-12 | **depends_on:** FE-s-74 | **slot:** ~5 | **rows:** W18-S1, C-S150 | **base:** workspace = the round-12 issuance commit on CLOUD (your worktree branches from it), portal DEV `5c8a9ba9` plus FE-s-74's hardened instrument once drained

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-78` -- two residuals the CVO's round-11 read left OPEN on the newly-visible Reporting body: W18-S1 (the cohort chip's
`rounded-md`, C11, still source-only because no round-11 fixture populated an authoritative cohort selection) and C-S150 (the sheet's
screen box-shadow at `print.css:520` is visible on-screen where it should not be, and the 390-width content extends beyond the visible
area with no exercised proof of scroll-reachability).

**Fix, cohort chip.** Author a TRUTHFUL fixture (populate `row`/`selection` with a real authoritative cohort, e.g. from a
directory/search result already in another fixture family) that actually MOUNTS the cohort chip, then correct `ScopeSummary.tsx:125`'s
`rounded-md` (6px) to an admitted radius (2/3/4px or a pill, per C11). Do not claim the fix without a fixture that renders the chip.

**Fix, report residuals.** Remove the screen-visible box-shadow at `render/print.css:520` (it belongs on the PRINT sheet, not the live
screen render). At 390 width, EXERCISE the reachability of the metric/chart/account content that currently extends beyond the visible
area (an actual scroll, captured) before concluding anything about clipping -- do not merely note the static image extends past the
fold. Cards that read UNAVAILABLE under the ordered wire shape stay UNAVAILABLE; do not invent populated summary values.

**Your surface.** `header/ScopeSummary.tsx`, `tabs/reporting/` (whole folder), `render/print.css`, and your own `__tests__/fe-s-78/`.

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
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5940-5949 (outside the derived range 5400-5899 the browser-gated tests use):
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

<criterion id="F78-AC1" cell_refs="FE-s-78" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F78-AC1` -- the whole portal typechecks.

<criterion id="F78-AC2" cell_refs="FE-s-78" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node src/pages/InvestorReporting/__tests__/fe-s-78/cohort-select-driver.mjs <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~28/f78_cohort_chip.png --port <PORT> --fixtures src/pages/InvestorReporting/__tests__/fe-s-78/fixtures/cohort-selected.json --select-authoritative --expect '[data-slot="cohort-chip"]' --expect-style '[data-slot="cohort-chip"]::border-radius!=6px'</invocation><expect>ASSERT-CONTENT: 1 of 1 met[\s\S]*ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F78-AC2` -- author `__tests__/fe-s-78/fixtures/cohort-selected.json` (a real authoritative cohort populated) and confirm the chip MOUNTS at an admitted radius, not `rounded-md`'s 6px.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~28-report, row `IRPT_FNTEND-W28-S1`):** the literal invocation carries no interaction step, but
`ScopeSummary.tsx:91`'s cohort chip mounts only from `row?.entry.cohorts`, and `row` (`index.tsx:50-52`) is set ONLY inside `ClientSearch`'s
`onSelectionChange`, itself fired only after a typed search resolves and a result is picked in the header's Combobox (`header/ClientSearch.tsx`,
`@/ui/components/catalyst/combobox`) -- no fixture, however truthful, populates it without that interaction. Worker `~28` correctly measured this
(FAIL, 0 of 1) and further confirmed `ui-smoke.mjs`'s `--fill` cannot reach the control (`page.getByRole('textbox', ...)` times out; Headless UI's
Combobox input is not role=textbox) -- a second, separate gap in the shared instrument, out of this cell's grant to fix directly.

**Fix, in-grant:** build `__tests__/fe-s-78/cohort-select-driver.mjs`, adapting `ui-smoke.mjs`'s own browser/route/auth-stub mechanism exactly as
`__tests__/fe-s-77/scroll-driver.mjs` did for FE-s-77's AC4 (same precedent, same reuse instruction) -- read that file first as the pattern to
follow. The driver additionally: (1) types a query into the header search control (find it by whatever selector genuinely reaches it -- try
`page.getByRole('combobox', {name: 'Client search'})` first, fall back to a CSS attribute selector on `[aria-label="Client search"]`'s own input if
that role doesn't resolve; verify empirically, do not assume); (2) selects the option matching the fixture's authored directory-search result
(`page.getByRole('option', {name: ...})` or equivalent); (3) THEN runs the same `--expect`/`--expect-style` assertions this criterion already
declares, printing the same `EXPECT*`/`ASSERT-*` summary lines `ui-smoke.mjs` prints, so the `<expect>` regex above still grades it. The bar itself
(chip mounts, radius != 6px) is unchanged; only the interaction mechanism is added.

<criterion id="F78-AC3" cell_refs="FE-s-78" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node src/pages/InvestorReporting/__tests__/fe-s-78/cohort-select-driver.mjs <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~28/f78_cohort_chip_control.png --port <PORT> --fixtures src/pages/InvestorReporting/__tests__/fe-s-78/fixtures/cohort-non-authoritative.json --select-non-authoritative --expect '[data-slot="cohort-chip"]'</invocation><expect>ASSERT-CONTENT: 0 of 1 met</expect></criterion>
`F78-AC3` -- CONTENT CONTROL: an unrelated fixture with no authoritative cohort selected mounts no chip at all -- confirms AC2's fixture genuinely constructed the state.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~28-report, row `IRPT_FNTEND-W28-S1`, informing `IRPT_FNTEND-W28-S3`):** as filed, this control was
CONFOUNDED -- it never interacted either, so it read `0 of 1` for the SAME structural reason as AC2's original failure (row was always null), not
because its fixture specifically lacked an authoritative cohort. Now that AC2 performs a real selection, this criterion must too, or it proves
nothing. Fix: author a second fixture, `__tests__/fe-s-78/fixtures/cohort-non-authoritative.json` (a directory-search result whose only cohort
carries `authoritative: false`, or none at all -- `ScopeSummary.tsx:91`'s `assertable = cohorts.filter((c) => c.authoritative)` must resolve empty),
and use the SAME driver to perform a real search-and-select against it, then confirm the chip still does not mount. This makes the control
genuine: a real selection occurs, and the content assertion still reads 0 of 1 because of the DATA, not the missing interaction.

<criterion id="F78-AC4" cell_refs="FE-s-78" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~28/f78_report_shadow.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect-style '[data-slot="reporting-body"]::box-shadow=none'</invocation><expect>ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F78-AC4` -- the screen render no longer carries the print sheet's box-shadow.

<criterion id="F78-AC5" cell_refs="FE-s-78" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~28/f78_report_390_scrolled.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect '[data-slot="reporting-body"]'</invocation><expect>ASSERT-CONTENT: 1 of 1 met</expect></criterion>
`F78-AC5` -- an ACTUAL scroll at 390 width is exercised on the report body and the far-edge content captured -- read this PNG against the un-scrolled capture and confirm content that was clipped is now visible, or genuinely document permanent clipping if a real scroll cannot reach it.

<criterion id="F78-AC6" cell_refs="FE-s-78" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F78-AC6` -- the whole IRPT_FNTEND suite is green (dev server stopped; `IRPT_FE_DEV_PORT` unset).

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~28-report, row `IRPT_FNTEND-W28-S2`):** this cell's ordered, required fix (`ScopeSummary.tsx:125`'s
`rounded-md` -> `rounded-[2px]`, plus a new `data-slot="cohort-chip"` attribute) breaks 4 pre-existing tests in 3 OTHER cells' out-of-grant files
that pin the OLD byte-exact markup: no admitted-radius choice avoids this (any value != 6px satisfies F78-AC2 and breaks these exact-string
comparisons). **Grant widened by exactly these three files, for exactly the string updates named below:**
- `__tests__/fe-s-42/every-site.test.ts:132` and `__tests__/fe-s-48/withheld.test.ts:219` -- both define an identical `buttonBefore(axis, value)`
  helper returning `'<button type="button" class="rounded-md px-2 py-0.5 text-[11px] text-slate-900 ring-1 ring-slate-500/40 hover:ring-slate-700">'`.
  Update the pinned string to match the ACTUAL new rendered markup byte-for-byte -- read the real rendered output first (do not guess attribute
  order): expected shape is `type`, then `data-slot="cohort-chip"`, then the new `class="rounded-[2px] ..."` (JSX source order), but VERIFY this
  empirically against your own build before finalizing the pin, exactly as these files' own header comments require ("byte for byte... not rendered
  from the component under test" -- the string must still be hand-written, just updated to the new true value).
- `__tests__/fe-s-59/scope-summary-badge.test.ts:163` -- `markup.slice(r.start, r.end).includes('rounded-md')` locates the cohort block by a
  Tailwind class substring. Update this to `.includes('data-slot="cohort-chip"')` instead -- a more stable anchor than a class value that this
  cell's own fix is retiring, and the more robust choice besides.
Nothing else in these three files is authorized to change. Confirm `bun test src/pages/InvestorReporting` reads `0 fail` afterward.

<criterion id="F78-AC7" cell_refs="FE-s-78" judgment="true" drives="none"/>
`F78-AC7` -- graded at L9 by the CVO: the cohort fixture is genuinely truthful (not a shortcut), the print-only shadow is gone from screen, and 390-width reachability was exercised rather than merely measured; no summary card value was invented. RECORD; NO VERDICT.

<expected_criteria>F78-AC1, F78-AC2, F78-AC3, F78-AC4, F78-AC5, F78-AC6, F78-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W28-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.

<paths>
portal/src/pages/InvestorReporting/header/ScopeSummary.tsx
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/render/print.css
portal/src/pages/InvestorReporting/__tests__/fe-s-78/
portal/src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-59/scope-summary-badge.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.12, cell `FE-s-78`.
<owned_cells>FE-s-78</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F78-AC1`, `F78-AC2`, `F78-AC3`, `F78-AC4`, `F78-AC5`, `F78-AC6`, `F78-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-78.cohort-chip-radius-and-report-styling-residuals.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F78-AC1,F78-AC2,F78-AC3,F78-AC4,F78-AC5,F78-AC6,F78-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-78.cohort-chip-radius-and-report-styling-residuals.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `cohort-chip-radius-and-report-styling-residuals.result.md` beside it.
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

Seating: round 12, wave 2, slot ~FE-s-78.
