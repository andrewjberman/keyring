# TO IRPT_FNTEND.TO-FE-s-86 -- the classifier matches a FULL template segment-for-segment, never a bare prefix

<to_id>IRPT_FNTEND.TO-FE-s-86</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~36</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-86` (round 14, v0.14) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~2 | **rows:** C-S147, F80-AC6 | **base:** workspace = the round-14 issuance commit on CLOUD (your worktree branches from it), portal DEV `467354c9` (round 13's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-86` -- round 13's `F80-AC6` FAILED at L9. The CVO's own probe: `routeKeyCandidates`/`checkKeyValidity`
(`scripts/ui-smoke.mjs:197-231`) widened a parameterised template's match to `k.startsWith(p)` where `p` is only the
template's STATIC PREFIX up to its first `{param}` -- e.g. `holdings/{accountSetId}` contributes the prefix
`holdings/`. That widening is too loose: it accepts `holdings/A-0001/not-a-declared-operation` (a real, undeclared
TRAILING operation no template names) as `valid=1`, because the string merely STARTS WITH the prefix. The static
(no-`{param}`) route set (`exact`) is unaffected and stays correctly exact-only.

**Fix.** Replace the prefix/`startsWith` widening with a SEGMENT-FOR-SEGMENT template matcher: split each declared
template (from `WIRE_CONSUMED_ROUTE_KEYS`, after stripping the HTTP verb) into path segments; split the concrete key
into segments the same way; a concrete key is valid against a template only when (a) the segment COUNT is identical,
(b) every LITERAL segment (no `{`) is byte-equal, and (c) every `{param}` segment corresponds to exactly one
NON-EMPTY concrete segment. A key with an EXTRA trailing segment beyond the template's own segment count is
INVALID, however plausible-looking the extra segment is. The static (`exact`) route set needs no change -- it
already requires whole-string equality and rejects the wrong-tail class by construction; only the parameterised
(prefix-based) branch is wrong.

**Required controls, ALL FOUR, denominator printed (CTO round-13 analysis, item 2):**
1. `holdings/A-0001` (concrete, satisfies the one-parameter holdings template) -> **valid**.
2. `holdings/A-0001/not-a-declared-operation` (the SAME concrete id, one undeclared trailing segment) -> **INVALID**
   -- this is the regression control for the exact defect F80-AC6 caught; it must fail under the OLD widening and
   pass (report invalid) under your fix.
3. A static-only suffix appended to a route with no `{param}` at all (e.g. `status/extra-junk` against a bare
   `status` template) -> **invalid** (unchanged from round 13 -- confirms you did not also loosen the exact set).
4. `status/{jobId}` instantiated concretely (e.g. `status/REQ-1`) -> **valid** -- this IS a declared parameterised
   route, so it is a POSITIVE control, not a negative one; do not conflate it with control 2's undeclared-tail case.

**Your surface.** `scripts/ui-smoke.mjs` (the `routeKeyCandidates`/`checkKeyValidity` functions ONLY, lines ~197-231
-- no other change to this file), `__tests__/fe-s-80/key-classifier.test.ts` (UPGRADE in place -- add the four named
controls above alongside the existing round-13 tests, which must still pass; do not delete or weaken them), and
your own `__tests__/fe-s-86/`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text your
   cell names (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-13 analysis
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_13_20260922.md` @4bc62712f2); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v10.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5995-5999 (outside the derived range 5400-5899 the browser-gated tests use,
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

<criterion id="F86-AC1" cell_refs="FE-s-86" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F86-AC1` -- the whole portal typechecks.

<criterion id="F86-AC2" cell_refs="FE-s-86" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-80/key-classifier.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F86-AC2` -- the upgraded unit test is green: all four CTO-named controls (holdings/A-0001 valid; holdings/A-0001/not-a-declared-operation INVALID; a static-only suffix invalid; status/{jobId} concrete valid) plus every pre-existing round-13 assertion, with the printed denominator (N of N controls correct) reading 4 of 4 on the new control set.

<criterion id="F86-AC3" cell_refs="FE-s-86" drives="none"><invocation>cd <WS>/portal && NODE_DISABLE_COLORS=1 NO_COLOR=1 timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~36/f86_holdings_key_validity_regression.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/default.json --click Holdings</invocation><expect>KEY-VALIDITY: 12 of 12 valid consumed\.ts operation keys</expect></criterion>
`F86-AC3` -- REGRESSION CONTROL, end-to-end: the real default.json fixture (12/12 entries, every key genuinely declared) still reads 12 of 12 under your stricter matcher -- the fix removes the false positive without also removing a true positive.

<criterion id="F86-AC4" cell_refs="FE-s-86" drives="none"><invocation>cd <WS>/portal && NO_COLOR=1 timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting > <WS>/.suite_check_86.log 2>&1; sed -r 's/\x1b\[[0-9;]*m//g' <WS>/.suite_check_86.log > <WS>/.suite_check_86_clean.log; UNEXPECTED=$(grep "^✗" <WS>/.suite_check_86_clean.log | grep -vc "F81-AC3/AC4"); echo "UNEXPECTED-FAIL-COUNT=$UNEXPECTED"</invocation><expect>UNEXPECTED-FAIL-COUNT=0</expect></criterion>
**COO AMENDMENT 2 (2.0.0_SA_COO~F, post-worker-~36-report, row `IRPT_FNTEND-W36-S1` continued):** amendment 1's
filter was ITSELF BROKEN, in two independent ways, both caught before any further harm: (a) `NO_COLOR=1` does
NOT suppress bun's ANSI colour codes in this bun version -- the `\x1b[0m\x1b[31m` sequence still precedes the
`✗` glyph, so a bare `grep "^✗"` matches ZERO lines regardless of how many tests genuinely failed, making
`UNEXPECTED-FAIL-COUNT=0` print UNCONDITIONALLY -- a vacuous pass, caught by worker `~36`'s own row `W36-S2`
before this seat had independently re-verified it; (b) the exclusion pattern itself
(`generator-output-carries-unprojected-grant`, hyphenated, matching the TEST FILE's name) never matched the
actual PRINTED line text (`generator output carries unprojected_grant`, spaced, the `describe`/`test` block's own
wording) -- so even after stripping ANSI, the exclusion silently excluded NOTHING and the criterion would have
read a false "2 unexpected" against a truly-zero-unexpected state. Fix, independently re-verified live by the
issuing COO in FE-s-86's own worktree: strip ANSI first (`sed -r 's/\x1b\[[0-9;]*m//g'`), then exclude on the STABLE criterion-id
token `F81-AC3/AC4` (present in both known lines, absent from every other line) rather than either the file name
or the full description text. POSITIVE CONTROL run live: the corrected filter genuinely counts 2 raw `✗` lines
and 0 unexpected, exactly matching the disclosed cross-cell gap. Row `IRPT_FNTEND-W36-S1` (and `W36-S2` where
filed) DISARM on this corrected re-run.

`F86-AC4` -- the whole IRPT_FNTEND suite is green, EXCLUDING the disclosed cross-cell fixture gap (see amendment below).
**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~36-report, row `IRPT_FNTEND-W36-S1`):** the literal invocation's
`bun test src/pages/InvestorReporting` genuinely reads 2 fail in EVERY round-14 worker's isolated worktree, because
none of the four cells' worktrees can see the others' fixes until the drain -- and the 2 failures are `__tests__/fe-s-81`'s
`generator-output-carries-unprojected-grant.test.ts`, exercising `FE-s-85`'s own cell (`W25-S1`), whose regenerated
fixtures are committed on ITS OWN branch only. This is not a regression on THIS cell's surface (confirmed:
`git diff --stat` against the issuance commit touches only this cell's own `<paths>`). The bar is unchanged --
0 unexpected failures -- but the invocation now isolates failures NOT attributable to the known, disclosed,
cross-cell gap, so a REAL regression on this cell's own surface still fails the criterion. Independently
re-verified live by the issuing COO in this worker's own worktree before amending: `UNEXPECTED-FAIL-COUNT=0`,
2 known fe-s-81 fails present and excluded, matching the worker's own report exactly. Row `IRPT_FNTEND-W36-S1` is
DISARMED by this amendment once the order is re-run and flipped complete (the true whole-suite-including-FE-s-85
bar is verified separately by the COO at drain time, in the merged tree).


<criterion id="F86-AC5" cell_refs="FE-s-86" judgment="true" drives="none"/>
`F86-AC5` -- graded at L9 by the CVO: the segment-for-segment matcher genuinely rejects an undeclared trailing segment (control 2) while genuinely accepting a concrete parameterised instantiation (controls 1 and 4), and the static/exact set's behaviour is unchanged (control 3). RECORD; NO VERDICT.

<expected_criteria>F86-AC1, F86-AC2, F86-AC3, F86-AC4, F86-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W36-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`ui-smoke.mjs` grant is the two named functions ONLY** -- do not touch any other function, flag or CLI
  behaviour in this file; those are settled (round 13).
- **C-S176 declared N/A, with reason, at cut time:** this cell's criteria are a pure-logic unit test (string/segment
  matching against literal inputs) plus one end-to-end regression read -- there is no rendered visual state, so the
  five-part visual control rule does not apply. The four CTO-named controls (positive/negative/bound/positive) ARE
  this cell's control set, already fully specified above; nothing here is silently waived.
<paths>
portal/scripts/ui-smoke.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-80/key-classifier.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-86/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.14, cell `FE-s-86`.
<owned_cells>FE-s-86</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F86-AC1`, `F86-AC2`, `F86-AC3`, `F86-AC4`, `F86-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-86.full-template-classifier-no-prefix-widening.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F86-AC1,F86-AC2,F86-AC3,F86-AC4,F86-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-86.full-template-classifier-no-prefix-widening.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `full-template-classifier-no-prefix-widening.result.md` beside it.
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

Seating: round 14, wave 1, slot ~FE-s-86.
