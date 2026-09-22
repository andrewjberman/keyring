# TO IRPT_FNTEND.TO-FE-s-87 -- AnswerStatus weights: state label 700, qualifier 400, under C1

<to_id>IRPT_FNTEND.TO-FE-s-87</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~37</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-87` (round 14, v0.14) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~3 | **rows:** C-S150 | **base:** workspace = the round-14 issuance commit on CLOUD (your worktree branches from it), portal DEV `467354c9` (round 13's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-87` -- one residual FE-s-84 explicitly left OPEN (round 13's CVO review): `AnswerStatus.tsx` still measures its
state-label badge (`data-slot="answer-state"`, `:84`) at `font-semibold` (weight 600) and its qualifier badge
(`data-slot="answer-qualifier"`, `:88`, shown only when the report is NOT `complete`) at `font-medium` (weight 500).
DESIGN.md's C1 allows only weight 400 and 700 -- no other value is legal anywhere in the portal.

**Fix.** `AnswerStatus.tsx:84`: `font-semibold` -> `font-bold` (the state-label badge -- this is the text that reads
"Ready", "Partial", or whatever `labelForState` returns; it goes to **700**, matching the CTO's round-11 breadcrumb
ruling that the "emphasis" element in a status family carries the higher weight). `AnswerStatus.tsx:88`:
`font-medium` -> `font-normal` (the qualifier explanatory badge -- "Qualified answer -- not a complete report" --
goes to **400**).

**C-S176 (this round's own CTO ruling) applies in full to this cell -- it is the visual criterion its discipline was
written for.** All five controls are APPLICABLE here (none is declared N/A): wire match, named content (the actual
state-label text), a wrong-state negative control (the SAME content assertion against a different state's fixture),
ground measured on `[data-slot="answer-status"]` (the actual container, white per C3, not the page canvas), and an
absent-selector control (the qualifier badge genuinely does not render on a `complete=true` fixture -- this doubles
as your CTO-required absent-selector control without inventing a new fixture).

**Your surface.** `tabs/reporting/AnswerStatus.tsx` (the two weight classes ONLY -- no other change to this file)
and your own `__tests__/fe-s-87/`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text your
   cell names (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-13 analysis
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_13_20260922.md` @4bc62712f2); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v10.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 6000-6004 (outside the derived range 5400-5899 the browser-gated tests use,
   and outside rounds 12-13's 5900-5989): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, in the background, INLINE PREFIX, NEVER
   exported. Test with `curl` first; that number is `<PORT>`. Sibling workers run at the same time: never 5175.
3. **Run each invocation and READ every PNG** it saves. Record per capture: file, viewport, the RAW `FIXTURES-MATCH`/`KEY-VALIDITY`, `EXPECT*` and
   `ASSERT-*` lines verbatim, the DESIGN.md clauses you read it against, and what you saw.
4. **A control is a claim.** Before you trust a passing assertion, run its wrong-state / negative arm and confirm it fails or reads UNMEASURABLE as
   required. If a control passes when it should fail, the assertion cannot tell the states apart: say so and fix it, never report it as met.
5. **Stop your dev server before the whole-suite criterion and verify the port closed** (`curl` returns `000`). Run the suite where
   `IRPT_FE_DEV_PORT` is unset.
6. **C-S176 (this round's own CTO ruling, binding on every criterion below):** every visual criterion carries five controls (wire match, named
   content, wrong-state control, ground-on-actual-container, absent-selector control) unless a control is declared NOT APPLICABLE, WITH REASON,
   IN THIS ORDER, at cut time -- never waived silently in your result. Report DECLARED-KEY VALIDITY (the proof's keys parse) and EXERCISED
   FULFILMENT (n of N controls actually run) as two SEPARATE figures, never conflated. No retroactive N/A: if a control this order declares
   applicable turns out not to run, that is a defect you report, not a silent omission.
7. **Fixes.** A defect on YOUR write surface may be fixed with a BEFORE capture kept and an AFTER beside it, one fix per finding, cited to its
   clause. A defect needing another cell's file is ONE surprise row, never a wider grant. A test inside your grant pinning OLD behaviour you are
   correcting is updated in the same commit and named in your result.
8. **Result file** (`<slug>.result.md` in your deliverables folder), FIXTURE-FED disclosure paragraph first, as every prior round.
9. **Keep your context small:** read at most the PNGs your criteria need; write long outputs to files and read their tails.

### ACCEPTANCE

<criterion id="F87-AC1" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F87-AC1` -- the whole portal typechecks.

<criterion id="F87-AC2" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~37/f87_ready_state_700.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect-text '[data-slot="answer-state"]::Ready' --expect-style '[data-slot="answer-state"]::font-weight=700'</invocation><expect>ASSERT-CONTENT: 1 of 1 met.*ASSERT-STYLE: 1 of 1 met</expect></criterion>
`F87-AC2` -- (a) WIRE MATCH (printed by --fixtures) + (b) NAMED CONTENT: the READY fixture's state-label reads the text "Ready" AND measures computed weight 700 -- both on the same capture.

<criterion id="F87-AC3" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~37/f87_wrong_state_negative_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json --expect-text '[data-slot="answer-state"]::Ready'</invocation><expect>ASSERT-CONTENT: 0 of 1 met</expect></criterion>
`F87-AC3` -- (c) WRONG-STATE NEGATIVE CONTROL: the SAME "Ready" text assertion, run against the qualified/Partial fixture (whose real state label is "Partial"), reads 0 of 1 met -- the content assertion genuinely discriminates states, it is not a vacuous match.

<criterion id="F87-AC4" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~37/f87_qualifier_400_and_state_700.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json --expect-text '[data-slot="answer-qualifier"]::Qualified answer' --expect-style '[data-slot="answer-qualifier"]::font-weight=400' --expect-style '[data-slot="answer-state"]::font-weight=700'</invocation><expect>ASSERT-CONTENT: 1 of 1 met.*ASSERT-STYLE: 2 of 2 met</expect></criterion>
`F87-AC4` -- on the qualified fixture: the qualifier badge carries its named text AND measures weight 400, while the CO-LOCATED state-label badge on the SAME capture still measures 700 -- proving the two elements are not accidentally given the same weight.

<criterion id="F87-AC5" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~37/f87_ground_positive.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect-ground '[data-slot="answer-status"]=rgb(255, 255, 255)'; echo '---SPLIT---'; NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~37/f87_ground_wrong.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --inject-css '[data-slot="answer-status"]{background-color:#c4cbdb !important}' --expect-ground '[data-slot="answer-status"]=rgb(255, 255, 255)'</invocation><expect>EXPECT-GROUND.*PASS rgb\(255, 255, 255\).*---SPLIT---.*EXPECT-GROUND.*FAIL rgb\(196, 203, 219\)</expect></criterion>
`F87-AC5` -- (d) GROUND ON THE ACTUAL CONTAINER, now TWO separate captures: the first measures [data-slot="answer-status"] at white rgb(255, 255, 255) (C3's panel role) with NO injection; the second, injected with a silver wrong-ground, must print FAIL rgb(196, 203, 219) on the SAME selector -- proving the assertion genuinely discriminates, never a vacuous PASS.
**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~37-report, row `IRPT_FNTEND-W37-S1`):** the original single invocation
combined `--expect-ground` with `--inject-css` in ONE call -- but `scripts/ui-smoke.mjs` applies `--inject-css`
BEFORE any `--expect-*` measurement, unconditionally (`:437-574`), so a single-capture invocation can never print
the required PRE-inject PASS-white line; the worker correctly measured this exact impossibility and refused rather
than self-grading past it. Fix: split into TWO separate node invocations in one shell command -- the first capture
carries NO injection (proves the true, un-injected ground is white); the second carries the injection alone (proves
the wrong-ground control genuinely fails). Independently re-run live by the issuing COO on a fresh ad-hoc dev server
before amending: first capture `PASS rgb(255, 255, 255)`, second capture `FAIL rgb(196, 203, 219)` -- both exactly
as required, matching the worker's own supplementary (ungraded) diagnostic. Row `IRPT_FNTEND-W37-S1` is DISARMED by
this amendment once the order is re-run and flipped complete.


<criterion id="F87-AC6" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~37/f87_absent_qualifier_control.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect-style '[data-slot="answer-qualifier"]::font-weight!=400'</invocation><expect>UNMEASURABLE</expect></criterion>
`F87-AC6` -- (e) ABSENT-SELECTOR CONTROL: on the answer-BEARING (complete=true) fixture, the qualifier badge genuinely does not render at all (the component's own `complete ? null : <qualifier>` branch); the same inequality assertion reads UNMEASURABLE, never a vacuous PASS.

<criterion id="F87-AC7" cell_refs="FE-s-87" drives="none"><invocation>cd <WS>/portal && NO_COLOR=1 timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting > <WS>/.suite_check_87.log 2>&1; sed -r 's/\x1b\[[0-9;]*m//g' <WS>/.suite_check_87.log > <WS>/.suite_check_87_clean.log; UNEXPECTED=$(grep "^✗" <WS>/.suite_check_87_clean.log | grep -vc "F81-AC3/AC4"); echo "UNEXPECTED-FAIL-COUNT=$UNEXPECTED"</invocation><expect>UNEXPECTED-FAIL-COUNT=0</expect></criterion>
**COO AMENDMENT 2 (2.0.0_SA_COO~F, post-worker-~37-report, row `IRPT_FNTEND-W37-S1` continued):** amendment 1's
filter was ITSELF BROKEN, in two independent ways, both caught before any further harm: (a) `NO_COLOR=1` does
NOT suppress bun's ANSI colour codes in this bun version -- the `\x1b[0m\x1b[31m` sequence still precedes the
`✗` glyph, so a bare `grep "^✗"` matches ZERO lines regardless of how many tests genuinely failed, making
`UNEXPECTED-FAIL-COUNT=0` print UNCONDITIONALLY -- a vacuous pass, caught by worker `~36`'s own row `W36-S2`
before this seat had independently re-verified it; (b) the exclusion pattern itself
(`generator-output-carries-unprojected-grant`, hyphenated, matching the TEST FILE's name) never matched the
actual PRINTED line text (`generator output carries unprojected_grant`, spaced, the `describe`/`test` block's own
wording) -- so even after stripping ANSI, the exclusion silently excluded NOTHING and the criterion would have
read a false "2 unexpected" against a truly-zero-unexpected state. Fix, independently re-verified live by the
issuing COO in FE-s-87's own worktree: strip ANSI first (`sed -r 's/\x1b\[[0-9;]*m//g'`), then exclude on the STABLE criterion-id
token `F81-AC3/AC4` (present in both known lines, absent from every other line) rather than either the file name
or the full description text. POSITIVE CONTROL run live: the corrected filter genuinely counts 2 raw `✗` lines
and 0 unexpected, exactly matching the disclosed cross-cell gap. Row `IRPT_FNTEND-W37-S1` (and `W36-S2` where
filed) DISARM on this corrected re-run.

`F87-AC7` -- the whole IRPT_FNTEND suite is green, EXCLUDING the disclosed cross-cell fixture gap (see amendment below).
**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~37-report, row `IRPT_FNTEND-W37-S1`):** the literal invocation's
`bun test src/pages/InvestorReporting` genuinely reads 2 fail in EVERY round-14 worker's isolated worktree, because
none of the four cells' worktrees can see the others' fixes until the drain -- and the 2 failures are `__tests__/fe-s-81`'s
`generator-output-carries-unprojected-grant.test.ts`, exercising `FE-s-85`'s own cell (`W25-S1`), whose regenerated
fixtures are committed on ITS OWN branch only. This is not a regression on THIS cell's surface (confirmed:
`git diff --stat` against the issuance commit touches only this cell's own `<paths>`). The bar is unchanged --
0 unexpected failures -- but the invocation now isolates failures NOT attributable to the known, disclosed,
cross-cell gap, so a REAL regression on this cell's own surface still fails the criterion. Independently
re-verified live by the issuing COO in this worker's own worktree before amending: `UNEXPECTED-FAIL-COUNT=0`,
2 known fe-s-81 fails present and excluded, matching the worker's own report exactly. Row `IRPT_FNTEND-W37-S1` is
DISARMED by this amendment once the order is re-run and flipped complete (the true whole-suite-including-FE-s-85
bar is verified separately by the COO at drain time, in the merged tree).


<criterion id="F87-AC8" cell_refs="FE-s-87" judgment="true" drives="none"/>
`F87-AC8` -- graded at L9 by the CVO: the state-label and qualifier weights are genuinely 700/400 (measured, not assumed from class names), the wrong-state and absent-selector controls genuinely discriminate (not vacuous), and the ground measurement is on the real container, not the page canvas. RECORD; NO VERDICT.

<expected_criteria>F87-AC1, F87-AC2, F87-AC3, F87-AC4, F87-AC5, F87-AC6, F87-AC7, F87-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W37-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`AnswerStatus.tsx` grant is the two font-weight classes ONLY** -- do not touch the border/background classes,
  the icon, or anything else in this file; those are settled (round 13, row IRPT_FNTEND-W34-S1).
- **Selectors are illustrative** -- adjust to the actual DOM if `[data-slot="answer-state"]`/`[data-slot="answer-qualifier"]`
  do not resolve exactly as written; the requirement is the WEIGHT values (700/400) and the five C-S176 controls, not
  these exact strings.
- **`reporting-qualified.json` is FE-s-84's own fixture (`__tests__/fe-s-84/fixtures/`), read-only to you** -- do not
  edit it; if it does not serve your need, author your own under `__tests__/fe-s-87/fixtures/`, same pattern FE-s-84
  used (a minimal field mutation of an existing committed fixture, never invented from nothing).
<paths>
portal/src/pages/InvestorReporting/tabs/reporting/AnswerStatus.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-87/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.14, cell `FE-s-87`.
<owned_cells>FE-s-87</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F87-AC1`, `F87-AC2`, `F87-AC3`, `F87-AC4`, `F87-AC5`, `F87-AC6`, `F87-AC7`, `F87-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-87.answer-status-weights-700-400-under-c1.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F87-AC1,F87-AC2,F87-AC3,F87-AC4,F87-AC5,F87-AC6,F87-AC7,F87-AC8 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-87.answer-status-weights-700-400-under-c1.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `answer-status-weights-700-400-under-c1.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.10 (both L4-R halves SIGNED, prd-signoff.py status ADMITTED).
the design: RUN by the issuer -- REMEDIATION_v10.md @66cf49b513, ADJUDICATION_v5.md's C-S16x..17x rows, and CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_13_20260922.md @4bc62712f2, all read at HEAD.
the spec: RUN -- PRD FWD-12 ENDPOINT row, the F9 CONTRACTS clause (v0.10), and the CTO's round-13 analysis, all read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 14, wave 1, slot ~FE-s-87.
