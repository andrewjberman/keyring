# TO IRPT_FNTEND.TO-FE-s-81 -- fixture generator repair -- unprojected_grant survives regeneration

<to_id>IRPT_FNTEND.TO-FE-s-81</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~31</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-81` (round 13, v0.13) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT, independent of FE-s-80 | **slot:** ~2 | **rows:** W25-S1 | **base:** workspace = the round-13 issuance commit on CLOUD (your worktree branches from it), portal DEV `2d7b2f21` (round 12's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-81` -- one real gap FE-s-75 found and correctly left unfixed (out of its own grant): `__tests__/fe-s-13/gen-corpus.ts`'s `envelope()` helper
(`:139-148`) builds every entry `generatePublishedMap()`/`generateSmokeMap()`/`generatePrintMap()` write to `fixtures/smoke/default.json`,
`fixtures/smoke/fe-s-13-wire.json` and `fixtures/smoke/fe-s-14-print-v1.json` -- and `envelope()` never writes an `unprojected_grant` key. Round
12's FE-s-75 hand-repaired `default.json` directly (12 of 12 entries now carry the field), but that repair lives ONLY in the fixture file, not in
the generator that authors it: re-running `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts` (the file's own documented
invocation) would silently strip the repair back out. The two sibling files were measured still missing the field entirely (`fe-s-13-wire.json` 9
of 9, `fe-s-14-print-v1.json` 2 of 2).

**Fix.** Either make `envelope()` emit a correct `unprojected_grant` value on every entry it builds (preferred, if the generator has enough
information to construct a truthful value), or make the generator REFUSE to overwrite a fixture file that a later cell has already repaired
(detect and preserve the field rather than silently regenerating over it) -- your choice, whichever keeps the data truthful. Required control:
regenerate ALL THREE files the generator produces, then parse-check each one; every entry in every file must carry `unprojected_grant` afterward,
and `default.json`'s regenerated content must still be data-equivalent to its round-12 hand repair (same entries, same values, not merely the same
field count).

**Your surface.** `src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts` and your own `__tests__/fe-s-81/`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's FWD-12 ENDPOINT row
   (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v9.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5965-5969 (outside the derived range 5400-5899 the browser-gated tests use,
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

<criterion id="F81-AC1" cell_refs="FE-s-81" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F81-AC1` -- the whole portal typechecks.

<criterion id="F81-AC2" cell_refs="FE-s-81" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F81-AC2` -- the generator runs to completion against the current fixture files (its own documented invocation, no new flags).

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~31-report, row `IRPT_FNTEND-W31-S1`):** the original `<expect>` regex guessed at plausible
completion wording (`wrote|generated|done|complete`) without checking the generator's REAL output. Measured (worker `~31`, independently
confirmed by me, same command, this worktree): `REQUEST RECORDS: 12 of 12; SMOKE KEYS: 9; PUBLISHED MAP KEYS: 12 of 12 DECLARED; PRINT MAP KEYS: 2`,
`rc=0` -- none of the guessed words appear anywhere in the script's real vocabulary. Fix: grade on `rc=0` (echoed explicitly), the genuine signal
of successful completion this generator actually emits; the bar (the generator runs cleanly) is unchanged, only the detection mechanism is
corrected.

<criterion id="F81-AC3" cell_refs="FE-s-81" drives="none"><invocation>cd <WS>/portal && node -e "const fs=require('fs');for (const f of ['src/pages/InvestorReporting/fixtures/smoke/default.json','src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json','src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json']) {const d=JSON.parse(fs.readFileSync(f,'utf8'));let n=0,m=0;for (const k in d) {if (d[k] && typeof d[k]==='object') {n++;if (!('unprojected_grant' in d[k])) m++}}console.log(f+': '+(n-m)+' of '+n+' carry unprojected_grant')}"</invocation><expect>default\.json: 12 of 12 carry unprojected_grant[\s\S]*fe-s-13-wire\.json: 9 of 9 carry unprojected_grant[\s\S]*fe-s-14-print-v1\.json: 2 of 2 carry unprojected_grant</expect></criterion>
`F81-AC3` -- AFTER regenerating (AC2), all three generated fixture files carry `unprojected_grant` on every top-level entry -- printed per-file, with the denominator each file's own entry count (12, 9, 2 respectively, matching the counts FE-s-75/this cell's own measurement established).

<criterion id="F81-AC4" cell_refs="FE-s-81" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-75</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F81-AC4` -- FE-s-75's own `parse-control.test.ts` (round 12) still reads clean against the regenerated `default.json` -- the regeneration did not change any OTHER field's truthful value, only added the missing one.

<criterion id="F81-AC5" cell_refs="FE-s-81" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F81-AC5` -- the whole IRPT_FNTEND suite is green.
<expected_criteria>F81-AC1, F81-AC2, F81-AC3, F81-AC4, F81-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W31-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **No judgment criterion on this cell** -- W25-S1 is a mechanical data-contract fix, fully graded by AC1-AC5.
- **This cell does NOT touch `fixtures/smoke/default.json`/`fe-s-13-wire.json`/`fe-s-14-print-v1.json` directly** -- only the generator that produces them; AC2 regenerates them as a side effect of running the (fixed) generator, never by hand-editing the JSON.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-81/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.13, cell `FE-s-81`.
<owned_cells>FE-s-81</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F81-AC1`, `F81-AC2`, `F81-AC3`, `F81-AC4`, `F81-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-81.fixture-generator-repair-survives-regeneration.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F81-AC1,F81-AC2,F81-AC3,F81-AC4,F81-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-81.fixture-generator-repair-survives-regeneration.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `fixture-generator-repair-survives-regeneration.result.md` beside it.
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

Seating: round 13, wave 1, slot ~FE-s-81.
