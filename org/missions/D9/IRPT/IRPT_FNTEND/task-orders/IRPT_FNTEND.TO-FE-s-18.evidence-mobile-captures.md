# TO IRPT_FNTEND.TO-FE-s-18 -- evidence rules: paired captures from one frozen report, the NOT_EVALUATED surfaces, mobile clipping fixed

<to_id>IRPT_FNTEND.TO-FE-s-18</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F4, F5, F6, F8, F11, F13; FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-18` (round 2, v0.2) | **outcome_ref:** FWD-3, FWD-5, FWD-8, FWD-11, FWD-12 | **depends_on:** `FE-s-14`, `FE-s-15`, `FE-s-16`, `FE-s-17` (all terminal) | **slot:** ~1, queue position 4, last | **slug rows:** C-S43, W3-S1, W4-S1, W1-S12 (retained control)

---

## WORKER FACE

### THE CELL

`FE-s-18` -- the round's evidence, produced under the rules the CTO made face law, plus the layout repairs the 390 captures showed.

**Layout-only edits** (classes and structure; no behaviour, no data, no new component): at 390 the Holdings summary card's values overlap, the firm attribution floats outside its card, the slice table and the pie labels clip, the Reporting period columns clip, the header actions wrap badly. Fix each with the portal's own utilities (a horizontal-scroll container for wide tables, stacked cards, wrapped actions), keeping the 1440 layout as it is.

**Captures**, every one a unique file under your deliverables folder, recorded in `captures.manifest.json` (`file`, `sha256`, `viewport`, `fixture`, `discriminator line`); the evidence rules:
- **Paired views from ONE frozen report.** `fixtures/smoke/fe-s-18-frozen.json` serves one performance report at one revision to the Reporting tab (screen), the export modal's preview and the print route; the three maps carry the same `performance-report` body (the test hashes it).
- **The four NOT_EVALUATED surfaces on the mounted views:** Analysis clean and needs-correction (FE-s-15's fixtures), Holdings observed / target / missing-attribution (three fixtures built from FE-s-13's wire holdings fixture: the observed custody basis, a target-blend basis, a node with attribution unavailable), print narrative-on and pre-history (FE-s-16's fixtures).
- **Global at 1440** with two firms (FE-s-14's fixture).
**Lato Bold (AMENDED BY THE ISSUER on 1.0.0_SA_CTO 95967, Andrew's word 13:4xZ "Yes fetch lato").** The 700 weight is now on this box: `/c/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/Lato-Bold.ttf`, 656544 bytes, sha256 `8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1` (fetched once by the CTO from the font's OFL upstream; no other fetch is authorized). Before the captures: copy it byte for byte into `render/assets/fonts/`; add its entry to `fonts.manifest.json` (weight 700, style normal, licence OFL-1.1) and set `stand_ins` to an empty object and `not_packaged` to `["italic"]`; point `print.css`'s 700 face at `Lato-Bold.ttf` and remove the stand-in comment; mirror the change in `render/manifest.ts`'s `fontPackage` (FE-s-17 put the full mirror there because `RENDER_PACKAGE.fonts` is a flat string array consumed by fe-s-4's manifest test; add the fourth file name to `fonts` too, and if fe-s-4's test asserts the array length, a surprise row names it and you leave the length as the test needs). FE-s-17's `__tests__/fe-s-17/fonts.test.ts` is updated for four files and no stand-in. This is the one non-layout edit this order carries, and it is the ONLY edit under `render/assets/fonts/`, `render/print.css` and `render/manifest.ts`.

- The census and the colour-law scan re-run on the round-2 tree (`bun run census.ts` from `deliverables/0.9.0_WK_IRPT_FNTEND~1/`, the FE-s-11 script; its outputs overwrite `component-census.json` / `.md`).

### R3 -- RE-PIN TO THE CURRENT v1 VINTAGE FIRST (AMENDED BY THE ISSUER at the FE-s-16 drain, row IRPT_FNTEND-S28)

⛔ **SUPERSEDED IN PART by the ROUND-4 ISSUER AMENDMENT at the top of BOUNDS -- read it before acting on anything in this section. `WIRE_SCHEMA_PINS` is RETIRED and must not be re-pinned by hand.**

**This is the THIRD time this round the producer has moved `docs/contracts/investor-reporting/v1/` under a consumer cell** (S20, then S21, now this). FE-s-15 re-pinned to `d9c940244a`; since that drain the counterpart landed `98d579cd1b` (the optional `date_claim` enum on AnalysisReport, both published copies) and `b8e98d5a4d` (IRPT_BCKEND PRD v0.14: `StatusEnvelope.business_date` becomes STATE-CONDITIONAL -- REQUIRED on the five answer-bearing states, MAY BE ABSENT and NEVER NULL on QUEUED / RUNNING / UNAVAILABLE / FAILED).

MEASURED BY THE ISSUER on the main checkout at portal DEV `774c595b`: `bun test src/pages/InvestorReporting` reads **406 pass, 1 skip, 1 fail**, the single failure being `__tests__/fe-s-13/producer-fixtures.test.ts:104` -- `expect(stale).toEqual([])` receiving **4** stale fixture copies. `F18-AC17` ('0 fail') cannot pass until those are refreshed, and no surface that carries them was in this order's original grant.

**BEFORE ANY CAPTURE:** refresh `WIRE_SCHEMA_PINS` and the `fixtures/wire/` copies to the artifact at `<WS>/docs/contracts/investor-reporting/v1/` as your worktree carries it, and record that vintage (`git log -1 --format=%h -- docs/contracts/investor-reporting/v1`) in the result file. Regenerate the wire types if any schema body changed. Then re-run `bun test src/pages/InvestorReporting/__tests__/fe-s-13` and record it.

**Grant for R3 ONLY:** `src/pages/InvestorReporting/fixtures/` (widened from `fixtures/smoke/`), `src/pages/InvestorReporting/contracts/`, `src/pages/InvestorReporting/__tests__/fe-s-13/`. These are granted for the re-pin and for nothing else; beyond R3 they are READ only.

⛔ **AND THE CAPTURES COME AFTER IT, NOT BEFORE.** Every PNG this order produces is the round's EVIDENCE. A capture taken against a stale pin is evidence of a tree that will not exist once the pin is refreshed, and it would be indistinguishable from a good one. Do R3, prove it, then capture.

### ACCEPTANCE

<criterion id="F18-AC1" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F18-AC1` -- the whole portal typechecks.

<criterion id="F18-AC2" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-18/paired.test.ts</invocation><expect>PAIRED: 1 report, 3 views</expect></criterion>
`F18-AC2` -- the screen, preview and print fixture maps carry one identical performance-report body (sha256 equal across the three), printed with the hash.

<criterion id="F18-AC3" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-18/manifest.test.ts</invocation><expect>UNIQUE FILES: ok</expect></criterion>
`F18-AC3` -- every PNG this order names exists under the deliverables folder, its sha256 equals the manifest's, no two entries share a file or a hash (printed `MANIFEST: n entries`).

<criterion id="F18-AC4" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_reporting_frozen_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --click Reporting --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Reporting</expect></criterion>
`F18-AC4` -- the Reporting tab on the frozen report at 390 (screen view of the pair).

<criterion id="F18-AC5" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_preview_frozen_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --click Export --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Export</expect></criterion>
`F18-AC5` -- the export modal's preview of the same frozen report at 1440 (preview view of the pair).

<criterion id="F18-AC6" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-18-frozen&narrative=0&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_print_frozen_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --console "REFS RESOLVED"; echo rc=$?</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F18-AC6` (INVOCATION AMENDED BY THE ISSUER, row IRPT_FNTEND-S31 -- the URL now carries `&tenant=&scope=&revision=`, exactly the params the worker's own CONTROL used. THE BAR IS UNCHANGED at `REFS RESOLVED: 1 of 1`.) -- the print route on the same frozen report (print view of the pair).

<criterion id="F18-AC7" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_analysis_clean_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-15-clean.json --click Analysis --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Analysis</expect></criterion>
`F18-AC7` -- Analysis clean at 390 after the layout repairs.

<criterion id="F18-AC8" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_analysis_correction_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-15-needs-correction.json --click Analysis --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Analysis</expect></criterion>
`F18-AC8` -- Analysis needs-correction at 390.

<criterion id="F18-AC9" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_holdings_observed_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F18-AC9` -- Holdings, observed custody basis, at 390.

<criterion id="F18-AC10" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_holdings_target_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-target.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F18-AC10` -- Holdings, target-blend basis, at 390.

<criterion id="F18-AC11" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_holdings_missing_attribution_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-missing-attribution.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F18-AC11` -- Holdings with a node whose attribution is unavailable, at 390.

<criterion id="F18-AC12" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-16-narrative&narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_print_narrative_on_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json --console "REFS RESOLVED"; echo rc=$?</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F18-AC12` -- print with the narrative page on, with the packaged font.

<criterion id="F18-AC13" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-16-prehistory&narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_print_prehistory_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-prehistory.json --console "REFS RESOLVED"; echo rc=$?</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F18-AC13` -- print with a pre-history window (MISSING HISTORY on the page). If FE-s-16 left no `fe-s-16-print-prehistory.json`, build it from FE-s-16's pre-history bun fixture and say so in the result file.

<criterion id="F18-AC14" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_global_two_firms_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F18-AC14` -- Global with two firms at 1440.

<criterion id="F18-AC15" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/census.ts; echo rc=$?</invocation><expect>COMPONENTS:</expect></criterion>
`F18-AC15` -- the census re-run on the round-2 tree (record N and the REUSED/NEW split; a NEW row without a reason is a surprise row on its cell).

<criterion id="F18-AC16" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/colour-law.test.ts</invocation><expect>0 fail</expect></criterion>
`F18-AC16` -- the colour law holds after the layout edits.

<criterion id="F18-AC17" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F18-AC17` -- the whole Investor Reporting set is green.

<criterion id="F18-AC18" cell_refs="FE-s-18" judgment="true"/>
`F18-AC18` -- graded at L9 from the manifest's PNGs: nothing clips or overlaps at 390; screen, preview and print of the frozen report agree figure for figure; the screens and the export read as one Opal product. RECORD; NO VERDICT.

<criterion id="F18-AC19" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>FONTS: 4 of 4</expect></criterion>
`F18-AC19` (AMENDED, added) -- the four Lato files under `render/assets/fonts/` hash to the manifest (Regular, Light, SemiBold, Bold); the Bold entry's sha256 is `8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1`.

<criterion id="F18-AC20" cell_refs="FE-s-18"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>STAND-INS: 0</expect></criterion>
`F18-AC20` (AMENDED, added) -- the manifest and `render/manifest.ts` declare no stand-in; `not_packaged` is exactly `["italic"]`; `print.css`'s 700 face names `Lato-Bold.ttf`.

<expected_criteria>F18-AC1, F18-AC2, F18-AC3, F18-AC4, F18-AC5, F18-AC6, F18-AC7, F18-AC8, F18-AC9, F18-AC10, F18-AC11, F18-AC12, F18-AC13, F18-AC14, F18-AC15, F18-AC16, F18-AC17, F18-AC18, F18-AC19, F18-AC20</expected_criteria>

## BOUNDS
- ⛔ **ROUND-4 ISSUER AMENDMENT -- BOUNDS ONLY. Every criterion is carried UNTOUCHED (1.0.0_SA_CTO ruling 1: `F18-AC3` and `F18-AC17` re-run, never re-issued). Where this block and anything above it differ, THIS BLOCK GOVERNS.** This order was cut in round 2; what sits beneath it has moved since, and four bounds from later rounds are added:
  1. **`WIRE_SCHEMA_PINS` IS RETIRED -- do not look for it and do not re-pin by hand.** Measured by the issuer: present at portal `774c595b` (`contracts/wire/index.ts:48`), ABSENT at `237a9027` and at current DEV; portal `2991992e` ("FE-s-20: the consumer pins CONTENT, not the producer's bytes") removed it. R3's "refresh `WIRE_SCHEMA_PINS` and the `fixtures/wire/` copies" is replaced by: **BEFORE ANY CAPTURE, run `__tests__/fe-s-13/content-pins.test.ts` and `__tests__/fe-s-13/producer-fixtures.test.ts` at your worktree's vintage and record the producer vintage the latter PRINTS.** If either fails, that is a BLOCKING row naming the failing assertion -- never a hand edit. `contracts/` and `fixtures/wire/` were granted for the R3 re-pin ALONE and that re-pin no longer exists, so **do not edit either**. R3's '406 pass, 1 skip, 1 fail at `774c595b`' is round-2 context; measure your own baseline at your cut. The rule that CAPTURES COME AFTER the pin check still stands.
  2. **ROW IDS ARE ALLOCATED ACROSS THE WHOLE CHANNEL PLANE.** Read `INVESTIGATION_v1.md` AND `_v2.md` for the last W1 id before minting -- not only the file the Surprise line below names (row S36).
  3. **Write the channel with `newline='\n'` and READ THE DIFFSTAT of every commit that touches it.** An append that touches lines it did not write is doing something else (row S47; this round a worker's first append re-serialised 16 existing rows and only this check caught it).
  4. **EVIDENCE HYGIENE (1.0.0_SA_CTO 96370): each row's `output_evidence` carries the DECIDING invocation's output and nothing else.** Earlier runs, baselines and BEFORE notes go in `status_reason`. It matters most on `F18-AC16` and `F18-AC17`: their `0 fail` bars are graded by an unanchored search, so a second summary anywhere in the evidence can satisfy them whatever the deciding run said (row S56). The issuer reads their deciding lines by hand at the drain.

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. Under `tabs/`, `header/`, `export/`, `global/`, `render/`: LAYOUT ONLY (class attributes, wrappers, order of siblings), with ONE exception the amendment names -- the Lato Bold packaging under `render/assets/fonts/`, `render/print.css`, `render/manifest.ts` and `__tests__/fe-s-17/`; any other change to a prop, state, data read, adapter call or text is a surprise row on the owning cell, never an edit here. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **R3 IS THE SECOND NON-LAYOUT EXCEPTION** (the Lato packaging is the first). The re-pin surfaces named in R3 are granted for the re-pin alone. Everything else under `tabs/`, `header/`, `export/`, `global/`, `render/` stays LAYOUT ONLY.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: the files you changed under `src/pages/InvestorReporting/` (name each) plus `src/pages/InvestorReporting/fixtures/smoke/ src/pages/InvestorReporting/__tests__/fe-s-18/`. Workspace records under org/ only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints; kill it before your final report. Routes without a leading slash; quote a route carrying `?`.
- **Fixture maps name the whole page's needs and are v1 envelopes** (keys = DECLARED paths; bodies `{contract_version: v1, operation, firm_id, data}` per `docs/contracts/investor-reporting/v1/`; AMENDED at the FE-s-14 R1 repair). Files you add: `fe-s-18-frozen.json`, `fe-s-18-holdings-observed.json`, `fe-s-18-holdings-target.json`, `fe-s-18-holdings-missing-attribution.json` (and `fe-s-16-print-prehistory.json` only if absent).
- **Numbers.** 1440 and 390 are test setups.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder, named exactly as the criteria name them.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W1-S<k>` continuing the W1 sequence (read the file for the last W1 id); never edit an existing row; keep working.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/tabs/
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/global/
portal/src/pages/InvestorReporting/render/
portal/src/pages/InvestorReporting/fixtures/
portal/src/pages/InvestorReporting/contracts/
portal/src/pages/InvestorReporting/__tests__/fe-s-13/
portal/src/pages/InvestorReporting/__tests__/fe-s-18/
portal/src/pages/InvestorReporting/__tests__/fe-s-17/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.2 @430c5fcb4a, cell `FE-s-18`.
<owned_cells>FE-s-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F18-AC1` .. `F18-AC20`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-18.evidence-mobile-captures.proof_of_spec.json`
(phase `INVESTIGATION`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F18-AC1,F18-AC2,F18-AC3,F18-AC4,F18-AC5,F18-AC6,F18-AC7,F18-AC8,F18-AC9,F18-AC10,F18-AC11,F18-AC12,F18-AC13,F18-AC14,F18-AC15,F18-AC16,F18-AC17,F18-AC18,F18-AC19,F18-AC20` BEFORE the `complete` flip. `F18-AC18` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `evidence-mobile-captures.result.md` beside it, listing every layout edit by file and line. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 (ADMITTED) -- carried.
instrument: RUN by the issuer -- ui-smoke prints CLICKED:/CLICK-FAIL:/DID NOT LAND/CONSOLE[type]: for --console; proof-of-spec-check grades expect as a regex (every expect here is a plain token).
lane: the <paths> block IS the grant, LAYOUT ONLY across the round-1 folders; portal paths bind by reading; workspace paths bind mechanically. Seated last so no write surface is shared concurrently.
</preflight>

Seating: slot ~1, queue position 4, last; seated when `FE-s-14`, `FE-s-15`, `FE-s-16` and `FE-s-17` are all terminal and drained, fresh worktree pair from HEAD.
