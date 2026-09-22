# TO IRPT_FNTEND.TO-FE-s-85 -- commit the regenerated fixtures so unprojected_grant survives to the git object

<to_id>IRPT_FNTEND.TO-FE-s-85</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~35</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-85` (round 14, v0.14) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~1 | **rows:** W25-S1 | **base:** workspace = the round-14 issuance commit on CLOUD (your worktree branches from it), portal DEV `467354c9` (round 13's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-85` -- round 13 fixed the GENERATOR (`__tests__/fe-s-13/gen-corpus.ts`'s `envelope()` helper now emits `unprojected_grant`
on every entry it builds), but the worker who fixed it never committed the two sibling files the generator writes:
`fixtures/smoke/fe-s-13-wire.json` and `fixtures/smoke/fe-s-14-print-v1.json`. The CVO's round-13 review measured this directly
at the git object: `default.json` 12/12 entries carry `unprojected_grant` (committed, round 12's hand repair), but
`fe-s-13-wire.json` reads 0/9 and `fe-s-14-print-v1.json` reads 0/2 AT THE COMMITTED PIN. The source repair is real; its output
never landed.

**Fix.** Run the generator's own documented invocation (`bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts`),
confirm ALL THREE files it writes now carry `unprojected_grant` on every entry in your WORKING TREE, then COMMIT the two sibling
files (`fe-s-13-wire.json`, `fe-s-14-print-v1.json`) to the portal repo. `default.json` is already committed and correct --
do not re-commit it unless the generator's run changed its content (if it does, that is itself a finding: report it, the round-12
hand repair must be DATA-EQUIVALENT to what the fixed generator now produces, same entries and values, not merely the same field
count).

**THE ACCEPTANCE READS THE GIT OBJECT, NOT THE WORKING TREE** (CTO ruling, round-13 analysis): a criterion below runs
`git -C <WS>/portal show <your commit>:<path>` and counts `unprojected_grant` occurrences in the committed bytes. A regenerated
file sitting uncommitted in your worktree does not satisfy this order -- this is precisely last round's defect, and the fix is
to COMMIT, not merely to regenerate.

**Your surface.** `src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json`,
`src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json`, and your own `__tests__/fe-s-85/`. You may re-run the
generator (already correct, round 13) but you do NOT have a grant to edit `__tests__/fe-s-13/gen-corpus.ts` itself -- if the
generator's OWN code is somehow still wrong, that is a surprise row, not a fix under this cell.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text your
   cell names (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-13 analysis
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_13_20260922.md` @4bc62712f2); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v10.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 5990-5994 (outside the derived range 5400-5899 the browser-gated tests use,
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

<criterion id="F85-AC1" cell_refs="FE-s-85" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F85-AC1` -- the whole portal typechecks.

<criterion id="F85-AC2" cell_refs="FE-s-85" drives="none"><invocation>cd <WS>/portal && /c/Users/AndrewBerman/.bun/bin/bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts</invocation><expect>SMOKE KEYS: 9.*PRINT MAP KEYS: 2</expect></criterion>
`F85-AC2` -- the generator's own run confirms the two sibling files' key counts (9 smoke keys, 2 print-map keys) -- the DENOMINATOR, printed by the generator itself, matching what the working-tree files must now carry.

**Write a small checker under your own grant** (`__tests__/fe-s-85/verify-git-object.mjs` or similar,
plain node, no framework) that: takes a commit-ish, runs `git -C <WS>/portal show <commit>:<path>` for each of
`fixtures/smoke/fe-s-13-wire.json`, `fixtures/smoke/fe-s-14-print-v1.json` and `fixtures/smoke/default.json`, JSON-parses the
result, counts entries with a non-null `unprojected_grant` key present (present-at-zero counts; ABSENT does not), and prints
one line per file: `GIT-OBJECT <path>: <n> of <total> carry unprojected_grant`. Commit your two fixture files FIRST, then run
this checker against your own commit hash.

<criterion id="F85-AC3" cell_refs="FE-s-85" drives="none"><invocation>cd <WS>/portal && /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/fe-s-85/verify-git-object.mjs $(git rev-parse HEAD)</invocation><expect>fe-s-13-wire\.json: 9 of 9.*fe-s-14-print-v1\.json: 2 of 2.*default\.json: 12 of 12</expect></criterion>
`F85-AC3` -- at the COMMITTED git object (not the worktree): fe-s-13-wire.json 9/9, fe-s-14-print-v1.json 2/2, default.json 12/12 -- all carrying unprojected_grant. This is the criterion the round-13 defect failed.

**COO AMENDMENT (2.0.0_SA_COO~F, post-worker-~35-report, row `IRPT_FNTEND-W35-S1`):** the original invocation had two
authoring bugs: (1) the checker path was written relative to `<WS>/portal` as `__tests__/fe-s-85/verify-git-object.mjs`,
missing the `src/pages/InvestorReporting/` prefix that this cell's own `<paths>` grant actually places it under
(`Module not found`, rc=1); (2) `<your-commit-hash>` was prose instruction embedded directly in the executable
`<invocation>` text, not a real, substitutable token. Fix: correct the path, and resolve the commit hash dynamically
via `$(git rev-parse HEAD)` (the worker's own just-made portal commit) instead of a placeholder. Independently
re-verified live by the issuing COO in this worker's own worktree before amending, using the worker's own already
existing checker script and commit: `fe-s-13-wire.json: 9 of 9`, `fe-s-14-print-v1.json: 2 of 2`,
`default.json: 12 of 12` -- exactly matching the worker's own supplementary (ungraded) diagnostic run at the
grant-consistent path. Row `IRPT_FNTEND-W35-S1` is DISARMED by this amendment once the order is re-run and flipped
complete.

<criterion id="F85-AC4" cell_refs="FE-s-85" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F85-AC4` -- the whole IRPT_FNTEND suite is green.

<criterion id="F85-AC5" cell_refs="FE-s-85" judgment="true" drives="none"/>
`F85-AC5` -- graded at L9 by the CVO: the committed fixture content is genuinely the generator's real output (not hand-edited to pass), and default.json's content (if touched) remains data-equivalent to round 12's repair -- same entries and values, not merely the same field count. RECORD; NO VERDICT.

<expected_criteria>F85-AC1, F85-AC2, F85-AC3, F85-AC4, F85-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W35-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`gen-corpus.ts` itself is READ-ONLY to you.** Round 13 already fixed it; you regenerate and commit its OUTPUT, never its
  source. If the generator's own code is still wrong, file a surprise row -- do not patch it under this grant.
- **C-S176 declared N/A, with reason, at cut time:** this cell's criteria are DATA-OBJECT checks (a fixture's field presence at a
  git commit), not a rendered visual assertion -- the five-part visual control rule (wire match / named content / wrong-state /
  ground / absent-selector) does not apply to this cell's subject matter. F85-AC3's git-object read IS this cell's control.
<paths>
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json
portal/src/pages/InvestorReporting/__tests__/fe-s-85/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.14, cell `FE-s-85`.
<owned_cells>FE-s-85</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F85-AC1`, `F85-AC2`, `F85-AC3`, `F85-AC4`, `F85-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-85.commit-generated-fixtures-with-unprojected-grant.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F85-AC1,F85-AC2,F85-AC3,F85-AC4,F85-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-85.commit-generated-fixtures-with-unprojected-grant.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `commit-generated-fixtures-with-unprojected-grant.result.md` beside it.
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

Seating: round 14, wave 1, slot ~FE-s-85.
