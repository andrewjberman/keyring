# TO IRPT_FNTEND.TO-FE-s-24 -- RENDER_PACKAGE.fonts names three of the four packaged faces

<to_id>IRPT_FNTEND.TO-FE-s-24</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F4, F13; the RenderPackage) | **Decomp cell:** `FE-s-24` (round 3, v0.3 @38f68b965c) | **outcome_ref:** FWD-8, FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~4, queue position 1 | **rows:** W1-S28

---

## WORKER FACE

### THE CELL

`FE-s-24` -- **four font faces are packaged and the manifest's flat array names three.**

Round 2's `FE-s-18` packaged Lato Bold (700) byte-for-byte and updated `fonts.manifest.json` and `render/manifest.ts`'s `fontPackage`. Its face also ordered "add the fourth file name to `RENDER_PACKAGE.fonts` too" -- and that could not be done inside its grant, because `__tests__/fe-s-4/manifest.test.ts:216` asserts the array's LENGTH IS 3 and `__tests__/fe-s-4/` was in no round-2 grant. The worker named it (`W1-S28`) and left it, which was correct.

So today `render/manifest.ts:114`'s `RENDER_PACKAGE.fonts` is a flat string array of 3 while `fontPackage` describes 4, and `__tests__/fe-s-17/fonts.test.ts:294` reads the flat array. **Make the array name all four packaged faces.**

⛔ **AND FIX THE ASSERTION'S SHAPE, NOT JUST ITS NUMBER.** `manifest.test.ts` asserts a LITERAL 3. Changing it to a literal 4 reproduces the defect one face later -- the next packaging change breaks it again and the next cell is again blocked by a test outside its grant. **Derive the expected count from the package itself** (the manifest's own font entries), so the array and the description cannot disagree without a test saying so, whatever the count becomes.

### ACCEPTANCE

<criterion id="F24-AC1" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F24-AC1` -- the whole portal typechecks.

<criterion id="F24-AC2" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts</invocation><expect>FONT NAMES: 4 of 4</expect></criterion>
`F24-AC2` -- `RENDER_PACKAGE.fonts` names all four packaged faces, and the test prints the count it DERIVED from the package beside the count it found in the array.

<criterion id="F24-AC3" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts</invocation><expect>COUNT IS DERIVED, NOT LITERAL</expect></criterion>
`F24-AC3` -- the assertion's shape: a source scan of `__tests__/fe-s-4/manifest.test.ts` for a literal length comparison against a digit returns zero hits, printed with a positive control proving the scan can find one.

<criterion id="F24-AC4" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts</invocation><expect>DISAGREEMENT CAUGHT: 1 of 1</expect></criterion>
`F24-AC4` -- **the difference control.** A seeded package in which `fonts` and `fontPackage` disagree by one face turns the assertion RED. Without this arm a derived count could be derived from the array itself and would agree with everything forever.

<criterion id="F24-AC5" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>FONTS: 4 of 4</expect></criterion>
`F24-AC5` -- FE-s-17's font battery still passes against the widened array, including the Bold entry's sha256 `8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1`.

<criterion id="F24-AC6" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4</invocation><expect>0 fail</expect></criterion>
`F24-AC6` -- the whole fe-s-4 folder is green, including the determinism bounds that also read `RENDER_PACKAGE`.

<criterion id="F24-AC7" cell_refs="FE-s-24"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>2 fail</expect></criterion>
`F24-AC7` -- the whole Investor Reporting set moves NEITHER way: exactly the two failures that exist at this cut (`F18-AC3`'s capture collision, `FE-s-19`'s; and the one stale schema pin, `FE-s-20`'s) and no third. The bar is `2 fail` because this cell cannot clear either and must not introduce one. **Print both failing test names**; if either is not one of those two, that is a BLOCKING row.

<expected_criteria>F24-AC1, F24-AC2, F24-AC3, F24-AC4, F24-AC5, F24-AC6, F24-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. Under `render/` you own `manifest.ts` ONLY -- not `assets/fonts/`, not `print.css`, not `narrative/`. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- ⛔ **DO NOT RE-PACKAGE, RE-FETCH OR MOVE A FONT FILE.** The four faces are already on disk and hashed; `FE-s-18` packaged them under Andrew's explicit word for the one fetch. This cell changes what the manifest SAYS, never what the package CONTAINS. A font binary that is absent or whose hash disagrees is a BLOCKING row, never a re-fetch.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: the files you changed under `src/`, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** Not needed for this cell. If you start one, kill it before your final report; do not run `bun install` (node_modules is a junction).
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W4-S<k>` starting at `IRPT_FNTEND-W4-S1` (the W4 coordinate has no round-3 rows yet; if the file carries no W4 sequence, yours opens it). Re-read the file immediately before minting each id; never edit an existing row; keep working.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/render/manifest.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-4/
portal/src/pages/InvestorReporting/__tests__/fe-s-17/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.3 @38f68b965c, cell `FE-s-24`.
<owned_cells>FE-s-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F24-AC1` .. `F24-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-24.render-package-fonts.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F24-AC1,F24-AC2,F24-AC3,F24-AC4,F24-AC5,F24-AC6,F24-AC7` BEFORE the `complete` flip. This order carries NO judgment criterion -- every bar is mechanical by output. Result file `render-package-fonts.result.md` beside it. Flip only when every criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
symbol location: RUN by the issuer -- comp-find 'RENDER_PACKAGE' over src/pages/InvestorReporting: 29 hits / 305 files, DEF=7. The definition is render/manifest.ts:114; the length assertion is __tests__/fe-s-4/manifest.test.ts; the flat-array read is __tests__/fe-s-17/fonts.test.ts:294.
blocker provenance: RUN -- W1-S28 records that the ordered change could not be made inside FE-s-18's grant because __tests__/fe-s-4/ was outside it. This cell is that grant, and nothing more.
lane: the <paths> block IS the grant; render/ is NARROWED to manifest.ts so this cell cannot collide with a future packaging cell. Portal paths bind by reading.
</preflight>

Seating: slot ~4, queue position 1; READY ROOT, seated at issuance on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row IRPT_FNTEND-S26).
