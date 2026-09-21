# TO IRPT_FNTEND.TO-FE-s-64 -- the component census and the colour-law scan, refreshed at the current vintage

<to_id>IRPT_FNTEND.TO-FE-s-64</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~14</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-64` (round 10, v0.10) | **outcome_ref:** FWD-12 | **depends_on:** none | **slot:** ~4 | **rows:** CTO grades `ledger/COMPLETION_GRADES.round9.json` @4030dac, FWD-12 row; CTO msg 99254

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-64` -- the PRD's FWD-12 PROOF limb -- "a census of EVERY component the page uses ... denominator printed" -- refreshed at the current vintage, plus the colour-law scan re-run (FWD-12's closing pass, fourth of four; EVIDENCE ONLY).

FE-s-11's census (65 components) was taken at round 1. Forty-nine cells (FE-s-12 through FE-s-60, eight rounds) have landed since. The PRD asks for the denominator printed and every NEW component justified; that evidence is eight rounds old.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the portal needs no re-learning."* DONE WHEN (EXERCISED): *"an advisor who already uses another portal page has used all three tabs and the export without being shown anything new to learn."* The CTO graded this card `NOT_EVALUATED` because no artifact covers that limb on the real route, and named the closing pass: **the real route, all three tabs plus the export, read against DESIGN.md at the CURRENT vintage.** It is the one card where IRPT_BCKEND is NOT ENGAGED, which is why it is cut now and the other seven are not.

**Your surface.** NO portal write at all. Your writes are your deliverables folder and, if you find something, ONE surprise row per finding. You read the tree, run the census and the scan, and report what they say.

**HOW.**

1. **Read first, in full:** the PRD's FWD-12 ENDPOINT row (DONE WHEN, ACCEPT, PROOF, CONSTRAINT) in
   `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`, and FE-s-11's own census script header
   (`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/census.ts`) and its recorded output
   (`component-census.md` / `.json` beside it) -- your refresh is compared against THAT, so know exactly what it counted and what it excluded.
2. **Copy, never run the original.** Create your deliverables folder and copy `census.ts` into it as a SETUP step (not a criterion). The script
   writes `component-census.json` and `component-census.md` BESIDE ITSELF, so running the original would overwrite FE-s-11's committed
   evidence -- the defect FE-s-42 fixed for captures. Run only your copy, from `<WS>/portal`.
3. **Compare.** Set your refreshed census beside FE-s-11's recorded one (65 components: 27 REUSED, 38 NEW, all 11 PRD reuse rows accounted).
   Name every component ADDED and every one REMOVED since round 1. For EVERY component marked NEW, write the reason a reviewer can dispute --
   the PRD's FWD-12 CONSTRAINT is *"a new component requires a stated need the existing set cannot meet; matching appearance alone is not
   reuse."* A NEW component with no stated need is a finding (one row), not something you excuse.
4. **Run the two pinned tests and record them.** `fe-s-11/colour-law.test.ts` is a criterion below. `fe-s-11/census.test.ts` is NOT: run it,
   record its result, and if it fails because the tree moved since it was pinned, that is ONE ROW with the diff. You have no portal write grant,
   so you never edit it.
5. **Write your result file** (`<slug>.result.md`). Its first paragraph states that this pass reads the COMMITTED tree at portal DEV
   `ddb172bf` (name the hash you actually read) and that nothing here reaches a live route.

### ACCEPTANCE

<criterion id="F64-AC1" cell_refs="FE-s-64" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F64-AC1` -- the whole portal typechecks.

<criterion id="F64-AC2" cell_refs="FE-s-64" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/census.ts; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F64-AC2` -- your COPY of the FE-s-11 census script, run from your own deliverables folder, exits 0. (Copy `census.ts` there FIRST as a setup step; the script writes `component-census.json` and `.md` BESIDE ITSELF, so running the original would overwrite FE-s-11's committed evidence, the same defect FE-s-42 fixed for captures. Never run the original.)

<criterion id="F64-AC3" cell_refs="FE-s-64" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/census.ts; echo rc=$?</invocation><expect>COMPONENTS: [0-9]+</expect></criterion>
`F64-AC3` -- the same run prints its denominator line `COMPONENTS: N` (the REUSED/NEW split follows it).

<criterion id="F64-AC4" cell_refs="FE-s-64" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/colour-law.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F64-AC4` -- FE-s-11's own colour-law scan, re-run against the tree as it stands NOW, reads `0 fail`.

<criterion id="F64-AC5" cell_refs="FE-s-64" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F64-AC5` -- the whole IRPT_FNTEND suite is green.

<criterion id="F64-AC6" cell_refs="FE-s-64" judgment="true" drives="none"/>
`F64-AC6` -- graded at L9 by the CVO: your result file states the refreshed census beside FE-s-11's recorded one (65 components, 27 REUSED, 38 NEW, all 11 PRD reuse rows accounted), the components ADDED and REMOVED since round 1 each named, and for every NEW component the reason a reviewer can dispute (the PRD's FWD-12 CONSTRAINT: a new component needs a stated need the existing set cannot meet; matching appearance alone is not reuse). Run `__tests__/fe-s-11/census.test.ts` too and record its result; if it fails because the tree moved since it was pinned, that is ONE ROW with the diff, not a fix (you have no portal write grant). RECORD; NO VERDICT.

<expected_criteria>F64-AC1, F64-AC2, F64-AC3, F64-AC4, F64-AC5, F64-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO
  grades it at L9. You never self-grade it and you never write "conforms" as a conclusion -- you write what the capture shows.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in
  the workspace repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use
  `.tools/safe-commit.sh` with a message file written by your Write tool.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W14-S<k>`; read the investigation file before minting; append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Disjoint by file from the other three cells of this round** (each owns its own portal write surface; every shared file is read-only
  to all four).
- The census script and the colour-law test are FE-s-11's; both are read-only to you (a copy of the script in your own folder is the only way you run it).

<paths>
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.10, cell `FE-s-64`.
<owned_cells>FE-s-64</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F64-AC1`, `F64-AC2`, `F64-AC3`, `F64-AC4`, `F64-AC5`, `F64-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/IRPT_FNTEND.TO-FE-s-64.closing-pass-component-census-and-colour-law-refresh.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F64-AC1,F64-AC2,F64-AC3,F64-AC4,F64-AC5,F64-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-64.closing-pass-component-census-and-colour-law-refresh.md`
BEFORE the `complete` flip. `F64-AC6` is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `closing-pass-component-census-and-colour-law-refresh.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- scripts/ui-smoke.mjs flags (--width :123, --console :132, --click :248/:257, the CANVAS line :342) and the five fixture files this round names read at portal DEV ddb172bf; FE-s-11's own invocations (F11-AC4..AC8) used as the shape.
the spec: RUN -- PRD FWD-12's ENDPOINT row (DONE WHEN, ACCEPT, PROOF, CONSTRAINT) and the CTO's FWD-12 grade row read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: wave A of round 10, slot ~4; ready root, no dependency edge with FE-s-61/62/63.
