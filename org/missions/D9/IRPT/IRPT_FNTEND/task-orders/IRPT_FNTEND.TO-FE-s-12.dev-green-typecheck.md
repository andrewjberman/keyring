# TO IRPT_FNTEND.TO-FE-s-12 -- DEV green first: the eight TypeScript errors under the census tests

<to_id>IRPT_FNTEND.TO-FE-s-12</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 | **Decomp cell:** `FE-s-12` (round 2, v0.2) | **outcome_ref:** every outcome (the shared branch) | **depends_on:** none (READY ROOT) | **slot:** ~1, queue position 1 | **slug rows:** S17

---

## WORKER FACE

### THE CELL

`FE-s-12` -- portal DEV @edab15b5 fails `bun run typecheck` (tsc -b --noEmit, exit 2) with exactly eight errors, all inside `src/pages/InvestorReporting/__tests__/fe-s-11/`:

```
census.test.ts(85,8)    TS2339  Property 'each' does not exist on type 'typeof test'
census.test.ts(87,6)    TS7006  Parameter '_name' implicitly has an 'any' type
census.test.ts(87,13)   TS7006  Parameter 'row' implicitly has an 'any' type
census.test.ts(95,30)   TS2339  Property 'toMatch' does not exist on type 'Matchers'
census.test.ts(140,8)   TS2339  Property 'each' does not exist on type 'typeof test'
census.test.ts(140,97)  TS7006  Parameter '_n' implicitly has an 'any' type
census.test.ts(140,101) TS7006  Parameter 'r' implicitly has an 'any' type
colour-law.test.ts(39,37) TS2305 Module '"node:fs"' has no exported member 'statSync'
```

The repo's ambient `bun:test` and `node:fs` shims (under `__tests__/fe-s-1/`, `__tests__/fe-s-3/ambient-shims.d.ts`, `__tests__/fe-s-7/ambient-shims.d.ts`) declare a narrower surface than bun's real API; bun runs the tests green because bun does not typecheck. Repair INSIDE the two test files only: a plain `for` loop over the rows instead of `test.each` (one `test(...)` per row inside the loop, same names); a regex test (`expect(re.test(value)).toBe(true)`) instead of `toMatch`; a shim-declared member (`readdirSync` with `withFileTypes`, or `existsSync` plus `readFileSync`, as the shim allows) instead of `statSync`; explicit parameter types. The shims are not edited; no `// @ts-ignore`, no `any` cast, no tsconfig change, no file excluded from tsc; strictness is not lowered. The tests must still prove what they proved (same assertions, same printed lines `COMPONENTS:` and `SCANNED:`).

### ACCEPTANCE

<criterion id="F12-AC1" cell_refs="FE-s-12"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F12-AC1` -- the whole portal typechecks (record the run time).

<criterion id="F12-AC2" cell_refs="FE-s-12"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11</invocation><expect>0 fail</expect></criterion>
`F12-AC2` -- the census and colour-law tests still pass (record `COMPONENTS:` and `SCANNED:`).

<criterion id="F12-AC3" cell_refs="FE-s-12"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F12-AC3` -- the whole Investor Reporting set is green (record the pass count; 322 at the base).

<criterion id="F12-AC4" cell_refs="FE-s-12"><invocation>cd <WS>/portal && echo "OUTSIDE-GRANT: $(git diff --name-only edab15b5 -- src | grep -vc '__tests__/fe-s-11/')"</invocation><expect>OUTSIDE-GRANT: 0</expect></criterion>
`F12-AC4` -- no file outside the two test files changed.

<criterion id="F12-AC5" cell_refs="FE-s-12"><invocation>cd <WS>/portal && echo "SHIMS-EDITED: $(git diff --name-only edab15b5 -- src/pages/InvestorReporting/__tests__/fe-s-1 src/pages/InvestorReporting/__tests__/fe-s-3/ambient-shims.d.ts src/pages/InvestorReporting/__tests__/fe-s-7/ambient-shims.d.ts tsconfig.json | wc -l)"</invocation><expect>SHIMS-EDITED: 0</expect></criterion>
`F12-AC5` -- the ambient shims and tsconfig are untouched.

<expected_criteria>F12-AC1, F12-AC2, F12-AC3, F12-AC4, F12-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. Commit portal files with cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- src/pages/InvestorReporting/__tests__/fe-s-11/`. Workspace records: cwd `<WS>`, workspace-relative paths under org/ only. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo. Never stage `portal` (the gitlink) in the workspace repo.
- **Bound every invocation** with `timeout` as written.
- **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W1-S<k>` continuing from `IRPT_FNTEND-W1-S15`; the file does not exist yet -- create it with a one-line header and a fenced `json` array holding your row (the row gate refuses an empty file, so create it only with a row in it); copy the field shape of the rows in `INVESTIGATION_v1.md`; never edit an existing row; keep working.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-11/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.2 @430c5fcb4a, cell `FE-s-12`.
<owned_cells>FE-s-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F12-AC1` .. `F12-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.proof_of_spec.json`
(phase `BUILD`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F12-AC1,F12-AC2,F12-AC3,F12-AC4,F12-AC5` BEFORE the `complete` flip. Result file `dev-green-typecheck.result.md` beside it. Flip only when every criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 (ADMITTED under spine v3.15) -- carried; no new complement source.
typecheck at the base: RUN by the issuer on DEV @edab15b5 -- rc=2, 8 errors, all under __tests__/fe-s-11/ (the whole input of this order); bun test 322 pass, 1 skip, 0 fail.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically.
</preflight>

Seating: slot ~1, queue position 1, the ready root; fresh worktree pair from HEAD (workspace) and DEV @edab15b5 (portal). Analysis ruling 1 (DEV green before any push): 0.0.0_AB_MSTR pushes portal DEV only after this order's drain.
