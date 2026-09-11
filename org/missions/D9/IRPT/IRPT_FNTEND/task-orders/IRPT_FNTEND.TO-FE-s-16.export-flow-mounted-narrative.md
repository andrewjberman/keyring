# TO IRPT_FNTEND.TO-FE-s-16 -- mount the export flow; the narrative's meaning is the backend's

<to_id>IRPT_FNTEND.TO-FE-s-16</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F8, F10; CONTRACTS `ExportBundle`, `ExportReceipt`, `StatusEnvelope`, `NarrativePacket`) | **Decomp cell:** `FE-s-16` (round 2, v0.2) | **outcome_ref:** FWD-8, FWD-4 | **depends_on:** `FE-s-13`, `FE-s-14` (R1: the v1 client) | **slot:** ~3, queue position 1 | **slug rows:** W1-S11, W2-S6

---

## WORKER FACE

### THE CELL

`FE-s-16` -- two things round 1 built and never mounted, and one meaning it guessed.

**Mount the export flow (W1-S11).** `export/AppliedBranding.tsx` and `export/ReceiptPanel.tsx` are exported and imported by nothing. Mount both INSIDE `ExportModal`'s dark `Panel` (their text is now canvas-legal; inside the Panel the colour law is met either way) and wire them to real state: `AppliedBranding` reads the requested branding choice and the composed wire `ExportBundle` (`approved_assets`, the applied label); `ReceiptPanel` reads the `ExportReceipt` the typed client returns from `submit-export` (`POST .../export`) and `export-receipt` (`GET .../export/{exportId}`) -- AMENDED on `docs/contracts/investor-reporting/v1/` @7ce4761a2f: both answer the response envelope with `data` = ExportReceipt and an optional `status` (StatusEnvelope); the download is followed from `data.download_route`, never by calling the `export-download` route by name (the contract names no consumer operation for it); job_state, download_route, timestamps, facts come from the wire receipt through the adapter. The two `ExportAnchorSlot` mounts in `index.tsx` pass the tab's real report refs and revision instead of `reportRefs={[]}` (those two JSX blocks are the only lines of `index.tsx` you change). Five states are proven on the MOUNTED flow, each from a wire fixture: no-assets (Opal template, label `Opal`), approved-assets (advisor / co-branded with the asset ref shown), running (no download link), failed (the public reason code shown, the request preserved), ready/download (the receipt's `download_route` is the rendered link). A branding edit still creates a new export revision without re-fetching performance (FE-s-9's control stays).

**Narrative meaning (W2-S6).** `render/narrative/` reads `NarrativePacket` through the FE-s-13 adapter from the wire fields the schema names -- `events` (the markers and their dates), `cited_evidence`, `prose`, `coverage` (the history window and its cutoff), `performance_revision`, `versions`; the round-1 guesses (`annotations`, `topics`, `historyCutoff`) are gone; a window predating `coverage`'s start renders `MISSING HISTORY` naming that date, never an empty list; the placeholder text no longer renders in any state; the contemporaneous-context statement and the causal-word exclusion stay.

### ACCEPTANCE

<criterion id="F16-AC1" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F16-AC1` -- the whole portal typechecks.

<criterion id="F16-AC2" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts</invocation><expect>STATES RENDERED: 5 of 5</expect></criterion>
`F16-AC2` -- `renderToStaticMarkup` of the open `ExportModal` with each of the five wire fixtures contains the `AppliedBranding` slot with the expected label and the `ReceiptPanel` slot with the expected state (running renders no link; ready renders the receipt's download route; failed renders the reason code).

<criterion id="F16-AC3" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/colour-law.test.ts</invocation><expect>0 fail</expect></criterion>
`F16-AC3` -- the colour-law scan is still clean after the mount (record `SCANNED:`).

<criterion id="F16-AC4" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-16/narrative-wire.test.ts</invocation><expect>MARKERS: 2</expect></criterion>
`F16-AC4` -- the two-event wire narrative fixture renders exactly two markers at the packet's dates; every quoted term exists in `cited_evidence`; none of caused / because / drove / explains / due to appears (the list is enumerated in the test).

<criterion id="F16-AC5" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-16/narrative-wire.test.ts</invocation><expect>MISSING HISTORY: rendered</expect></criterion>
`F16-AC5` -- the pre-history wire fixture renders the MISSING HISTORY state naming `coverage`'s cutoff and no topic element; a source grep of `render/narrative/` for the placeholder text and for `historyCutoff` returns 0 hits (printed).

<criterion id="F16-AC6" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-16_export_ready_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-16-ready.json --click Export --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Export</expect></criterion>
`F16-AC6` -- the modal opens on the mounted flow in the ready state at 1440.

<criterion id="F16-AC7" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-16_export_ready_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-16-ready.json --click Export --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Export</expect></criterion>
`F16-AC7` -- the same at 390.

<criterion id="F16-AC8" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-16-narrative" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-16_print_narrative_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json --console "REFS RESOLVED"; echo rc=$?</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F16-AC8` -- the print route with the narrative page on, served in wire shape at the declared paths (performance report and narrative packet), resolves its references (ui-smoke prints `DID NOT LAND` for the query-string route; the resolver line is the bar).

<criterion id="F16-AC9" cell_refs="FE-s-16"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F16-AC9` -- the whole Investor Reporting set is green.

<criterion id="F16-AC10" cell_refs="FE-s-16" judgment="true"/>
`F16-AC10` -- graded at L9 from the three PNGs: the modal states what branding was applied and where the export stands, the narrative page reads as contemporaneous context with dated markers. RECORD; NO VERDICT.

<expected_criteria>F16-AC1, F16-AC2, F16-AC3, F16-AC4, F16-AC5, F16-AC6, F16-AC7, F16-AC8, F16-AC9, F16-AC10</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. `index.tsx`: the two `ExportAnchorSlot` JSX blocks only. The typed client and adapters are FE-s-13's and READ only; a field the adapter does not expose is a surprise row. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: `src/pages/InvestorReporting/export/ src/pages/InvestorReporting/render/narrative/ src/pages/InvestorReporting/index.tsx src/pages/InvestorReporting/fixtures/smoke/ src/pages/InvestorReporting/__tests__/fe-s-16/`. Workspace records under org/ only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints; kill it before your final report. Routes without a leading slash; quote a route carrying `?`.
- **Fixture maps name the whole page's needs.** Smoke fixture files you add: `fe-s-16-ready.json`, `fe-s-16-print-narrative.json` (and the four other states as bun-test fixtures under `__tests__/fe-s-16/` or `fixtures/`).
- **Numbers.** 1440 and 390 are test setups.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W3-S<k>` continuing from `IRPT_FNTEND-W3-S3` (read the file for the last W3 id; if it does not exist, create it with a one-line header and a fenced `json` array holding your row); never edit an existing row; keep working.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/render/narrative/
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-16/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.2 @430c5fcb4a, cell `FE-s-16`.
<owned_cells>FE-s-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F16-AC1` .. `F16-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-16.export-flow-mounted-narrative.proof_of_spec.json`
(phase `BUILD-GENERAL` -- AMENDED BY THE ISSUER at the FE-s-12 drain on row IRPT_FNTEND-W1-S15: the schema's phase enum has no BUILD member, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F16-AC1,F16-AC2,F16-AC3,F16-AC4,F16-AC5,F16-AC6,F16-AC7,F16-AC8,F16-AC9,F16-AC10` BEFORE the `complete` flip. `F16-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `export-flow-mounted-narrative.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the export routes and the receipt are the counterpart's.
comp-adversary: RUN at L4 on PRD v0.6 (ADMITTED) -- carried.
lane: the <paths> block IS the grant; index.tsx is granted for the two mount blocks only; portal paths bind by reading; workspace paths bind mechanically. export/ (FE-s-9) and render/narrative/ (FE-s-8) are terminal cells' folders.
</preflight>

Seating: slot ~3, queue position 1; seated when `FE-s-13` is terminal and drained, fresh worktree pair from HEAD.
