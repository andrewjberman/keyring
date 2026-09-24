# TO IRPT_FNTEND.TO-FE-s-63 -- the export modal and the print page, read against DESIGN.md at the current vintage, and round 9's open F60-AC6

<to_id>IRPT_FNTEND.TO-FE-s-63</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~13</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~23:00Z).** Two passes. Pass 1 (drained `d66882cd65`) FAILED F63-AC5 and F63-AC6 as written and was correctly left `pending`: the defect was in this order (dead fixtures, a print URL without tenant, scope and revision), amended at `84077faa2d`. The first worker instance then hung twice with no tool round; a replacement instance of the same serial finished pass 2 (workspace `96519aea44`, portal `994d25f9`), drained at workspace `8cbf3daf77` and portal `243089eb`: first-parent diff 15 added, 12 modified, 0 deleted, first-pass evidence kept under `pass1/`. Verified independently on the merged tree by this seat: `proof-of-spec-check` VALID (8 rows); `bun run typecheck` rc=0; the whole `src/pages/InvestorReporting` suite `612 pass / 22 skip / 0 fail`, 634 tests across 114 files, run with no dev server up (portal `243089eb`); and my own run of the amended F63-AC5 and the export criterion against my own server: `REFS RESOLVED: 1 of 1` printed twice, `FIXTURES: 2 declared; 2 matched`, a page TEXT that is the rendered document and not the refusal panel; the export run `FIXTURES: 3 declared; 3 matched`. That is the same command run by a different seat, so it corroborates reproducibility on the merged tree, not a different method. Rows disarmed, evidenced by these measurements and this note and NOT by editing the rows (a row's `hazard_standing` is a birth property): `IRPT_FNTEND-W13-S1` (the print criteria could not print `REFS RESOLVED`; now met, above), `IRPT_FNTEND-W13-S3` (the F60-AC6 note could not be rendered; it renders on print page 2, and I read it in the worker's crop as "1 of 5 events not yet reflected in this narrative." in small light-grey text on the white sheet; the `#595959` value is the worker's read of `print.css`, not my measurement), `IRPT_FNTEND-W13-S2` (the print route's retired silver ground `#c4cbdb`; fixed at portal `8894e765`, BEFORE and AFTER captures read by me). NOT disarmed and not claimed: W13-S2's class-level point, that the `CANVAS:` line cannot see a route's own ground, which stays an observation carried to the CVO. New row `IRPT_FNTEND-S69` (mine): the export modal's receipt card reads "Loading / No source age yet" before Create export is pressed, because `export/ReceiptPanel.tsx:42-44` hard-codes the LOADING state for a null receipt; the worker recorded it as an observation and filed no row. `F63-AC8` is a JUDGMENT criterion: the CVO grades it at L9, not this note.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-63` (round 10, v0.10) | **outcome_ref:** FWD-12 | **depends_on:** none | **slot:** ~3 | **rows:** CTO grades `ledger/COMPLETION_GRADES.round9.json` @4030dac, FWD-12 row; CTO msg 99254

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-63` -- the export (modal, preview) and the print page, exercised at 1440 and 390 and READ against `DESIGN.md` at its current vintage, which also answers round 9's open `F60-AC6` (FWD-12's closing pass, third of four surfaces).

Round 9's CVO left `F60-AC6` open because the worker who wrote the period-in-context badge had no screenshot capability and disclosed that rather than asserting compliance. You have the instrument (`ui-smoke.mjs` is run from Bash and its PNG is read with the Read tool); use it.

**COO AMENDMENT (2026-09-21, `2.0.0_SA_COO~F`) -- READ THIS BEFORE THE CRITERIA. THE DEFECT WAS IN THIS ORDER, NOT IN YOUR WORK.** Your first pass reported (rows `IRPT_FNTEND-W13-S1`, `-S2`, `-S3`, drained at `d66882cd65`) that the fixtures this order named (`fe-s-9-modal.json`, `fe-s-11-print.json`) are keyed by retired operation names and match no URL the client requests, and that the print invocation omitted the `tenant`, `scope` and `revision` the route needs. That is correct, and I verified it against `contracts/wire/consumed.ts:45-51`, the fixture keys, and your PNGs. I wrote the order with the fixture FILES and ui-smoke FLAGS checked for existence but never their KEYS against the wire, which is why an anchored `CANVAS:` criterion could pass on an error page. The criteria above are re-pointed at two fixtures YOU author (below); the cell's text, surface, bounds and judgment criterion are unchanged. Your first pass's evidence stands as recorded: keep it, do not delete it.

**What you do now, in this order.**
1. Author `portal/src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json` and `.../print-ready.json` (inside your granted `__tests__/fe-s-63/`; `fixtures/smoke/` stays read-only to you). Start from wire-keyed fixtures already in the tree (`fe-s-16-ready.json`, `fe-s-16-print-narrative.json`, `fe-s-13-wire.json`, `fe-s-18-frozen.json`) and repair whatever keys the current client's requests do not match: every key you declare must match at least one request (`FIXTURES: N declared; N matched`, no `FIXTURE-DEAD` line). The client's request shapes are in `portal/src/api/endpoints/investor-reporting.ts` and `contracts/wire/consumed.ts`.
2. Your diagnostic run against `fe-s-16-print-narrative.json` with `tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091` still printed "rev-49f-000091 is absent" and you did not find which step rejects it. FIND IT (read `render/PrintEntry.tsx`, `export/resolveBundle.ts`, `render/manifest.ts:296`) and say in your result whether it is a fixture defect or a defect in the print path. A print-path defect on YOUR surface (`export/`, `render/`) you may fix under HOW step 6; one outside it is a row.
3. Re-run F63-AC2 through F63-AC6 as now written; quote each `FIXTURES:` line verbatim; read every PNG. F63-AC5/AC6 must print `REFS RESOLVED: 1 of 1` and the PNG must be a rendered document. If, after a real attempt, one still cannot be met, REFUSE it again with the measurement and say which step rejects; do not weaken the criterion.
4. The period-in-context note (`F60-AC6`) is RENDERED and READ once a document renders, and F63-AC8 is recorded with no verdict, as before. Re-record the proof instance for the changed invocations, validate it with the same `proof-of-spec-check` command, and flip `<status>` only if it returns VALID with no FAIL row; otherwise leave `pending` and say why.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the portal needs no re-learning."* DONE WHEN (EXERCISED): *"an advisor who already uses another portal page has used all three tabs and the export without being shown anything new to learn."* The CTO graded this card `NOT_EVALUATED` because no artifact covers that limb on the real route, and named the closing pass: **the real route, all three tabs plus the export, read against DESIGN.md at the CURRENT vintage.** It is the one card where IRPT_BCKEND is NOT ENGAGED, which is why it is cut now and the other seven are not.

**Your surface.** The export (`export/`: the modal, branding choices, applied-branding display, receipt) and the print page path (`render/`, including `render/print.css` and `render/narrative/PeriodInContextPage.tsx`). You may edit only files under `export/` and `render/` (plus your own `__tests__/fe-s-63/`). `tabs/StatusPanel.tsx`, `state/`, `contracts/`, `src/index.css` and every shared component are READ-ONLY to you. The print route is `investor-reporting/print` with `bundle`, `tenant`, `scope`, `revision` (and `narrative=1`) query parameters, exactly as F63-AC5 spells it; the export modal is opened by clicking Export.

**HOW (the same for all four cells of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (the portal's visual contract, clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`
   (the color law table, the Verification law). A finding cites a clause NUMBER (`C3`, `C5.8`, ...) beside its evidence; "it looks
   off" is not a finding. Also read the PRD's FWD-12 ENDPOINT row and its ACCEPT / PROOF / CONSTRAINT lines
   (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`) -- that row is what you are closing, not this order's summary of it.
2. **Start your worktree's own dev server** and export its port: choose a port no other process holds (test with `curl`), run
   `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal` in the background, wait until it answers, and use that number as
   `<PORT>` in every invocation below. Other seats and three sibling workers run at the same time: do not use 5175.
3. **Capture, then LOOK.** Run each invocation; the PNG lands in your deliverables folder. **Open every PNG with the Read tool and read it
   -- a grep cannot see contrast.** Record in your result file, per capture: the file name, the viewport, the `CANVAS:` line printed
   VERBATIM, which DESIGN.md clauses you checked it against, and what you saw.
4. **The discriminator.** FE-s-11's recorded capture printed `CANVAS: rgb(195, 202, 218)` (the silver ground the 2026-09-11 ruling
   retired; evidence at `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/`). Quote that value beside your own in
   the result, so the reader can see the check has an arm that can fail. NOTE: `ui-smoke.mjs` prints the literal text
   `rgb(244, 246, 250)` inside its own explanatory parenthetical on EVERY run whatever the real canvas is, so a search for that string
   alone proves nothing; the criteria below anchor on `CANVAS: ` immediately followed by the value, and you must read the value itself.
5. **Stop your dev server before the whole-suite criterion and verify the port is closed** (`curl` returns `000`). A live server makes the
   browser-gated suites run instead of skip, which is a different measurement (rows `IRPT_FNTEND-W8-S1` / `W9-S1`). On Windows, `ps`
   from Git Bash can miss a node process: find the listener with PowerShell `Get-NetTCPConnection -LocalPort <n> -State Listen` and stop
   it with `Stop-Process`.
6. **Fixes.** A defect a capture in THIS pass demonstrates, on YOUR write surface (the `<paths>` block below), you may fix -- keep the
   BEFORE capture, take an AFTER capture beside it, one fix per finding, each cited to its clause. A defect whose fix needs ANY other
   file (`tabs/StatusPanel.tsx`, `state/`, `contracts/`, `src/index.css`, `src/App.tsx`, anything outside `InvestorReporting/`, another
   cell's surface) is ONE surprise row and you keep going -- never widen your own grant. If a fix of yours breaks a test outside your
   grant, REVERT that fix, keep the BEFORE capture, and file the finding as a row.
7. **Write your result file** (`<slug>.result.md` in your deliverables folder). Its FIRST paragraph says, plainly, that these captures are
   FIXTURE-FED (the real route with fixtures answered at the network layer; no live route was reached) and why that is the right kind of
   evidence for THIS card and not for the other seven (FWD-12's DONE WHEN is about familiarity on the real page and needs no
   counterpart half).

### ACCEPTANCE

<criterion id="F63-AC1" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F63-AC1` -- the whole portal typechecks.

<criterion id="F63-AC2" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export</invocation><expect>CLICKED: Export</expect></criterion>
`F63-AC2` -- the export modal is reached on the real route by clicking Export (fixture `__tests__/fe-s-63/fixtures/export-ready.json`, which you author, 1440): the run prints `CLICKED: Export`. AMENDED: this criterion cannot tell a READY modal from an error page, so the run's own `FIXTURES: N declared; M matched` line must be quoted VERBATIM in your result with M equal to N (no `FIXTURE-DEAD` line), and you read the PNG to confirm the modal is the READY state.

<criterion id="F63-AC3" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export</invocation><expect>CANVAS: rgb\(244, 246, 250\)</expect></criterion>
`F63-AC3` -- the same export capture at 1440: the printed `CANVAS:` value is `rgb(244, 246, 250)`.

<criterion id="F63-AC4" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/export-ready.json --click Export</invocation><expect>CANVAS: rgb\(244, 246, 250\)</expect></criterion>
`F63-AC4` -- the export modal at 390: the printed `CANVAS:` value is `rgb(244, 246, 250)`.

<criterion id="F63-AC5" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-16-narrative&narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_print_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/print-ready.json --console "REFS RESOLVED"</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F63-AC5` -- the print page (the exported-PDF path; bundle `fe-s-16-narrative` with the tenant, scope and revision the route requires, fixture `__tests__/fe-s-63/fixtures/print-ready.json`, which you author) at 1440 resolves its references: the run prints `REFS RESOLVED: 1 of 1`. AMENDED: the run's `FIXTURES:` line is quoted verbatim in your result with M equal to N, and the PNG is a rendered DOCUMENT, not "This bundle was not rendered".

<criterion id="F63-AC6" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-16-narrative&narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_print_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/print-ready.json --console "REFS RESOLVED"</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F63-AC6` -- the print page at 390 resolves its references: the run prints `REFS RESOLVED: 1 of 1`.

<criterion id="F63-AC7" cell_refs="FE-s-63" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F63-AC7` -- the whole IRPT_FNTEND suite is green (with your dev server STOPPED and its port verified closed).

<criterion id="F63-AC8" cell_refs="FE-s-63" judgment="true" drives="none"/>
`F63-AC8` -- graded at L9 by the CVO, and it answers TWO questions. (1) The export surface read against DESIGN.md at its current vintage: the export modal, the branding choices, the preview, and the print page, each finding citing its `C<n>`, including the PRD's own constraint that "modals, previews and exports carry the same brand as screens". (2) **Round 9's open `F60-AC6` color-law question**: the period-in-context page's partial-disclosure note (FE-s-60, `render/narrative/PeriodInContextPage.tsx`, classes `ir-note ir-muted`, `#595959` from `render/print.css`) is RENDERED and READ, and you record what it shows and WHICH DESIGN.md clause, if any, speaks to a print surface (the interactive-canvas law names `page canvas`, `panel` and `band`, none of them a print sheet). If no clause speaks to it, say so as a finding; do not invent one. RECORD; NO VERDICT.

<expected_criteria>F63-AC1, F63-AC2, F63-AC3, F63-AC4, F63-AC5, F63-AC6, F63-AC7, F63-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO
  grades it at L9. You never self-grade it and you never write "conforms" as a conclusion -- you write what the capture shows.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in
  the workspace repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use
  `.tools/safe-commit.sh` with a message file written by your Write tool.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W13-S<k>`; read the investigation file before minting; append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Disjoint by file from the other three cells of this round** (each owns its own portal write surface; every shared file is read-only
  to all four).
- `render/performance/PerformanceDocument.tsx` mounts `PeriodInContextPage` for the print path; FE-s-60 added ONE node there and its test proves one shared render path -- do not add a second copy anywhere.

<paths>
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/render/
portal/src/pages/InvestorReporting/__tests__/fe-s-63/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.10, cell `FE-s-63`.
<owned_cells>FE-s-63</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F63-AC1`, `F63-AC2`, `F63-AC3`, `F63-AC4`, `F63-AC5`, `F63-AC6`, `F63-AC7`, `F63-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/IRPT_FNTEND.TO-FE-s-63.closing-pass-export-and-print-page.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F63-AC1,F63-AC2,F63-AC3,F63-AC4,F63-AC5,F63-AC6,F63-AC7,F63-AC8 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-63.closing-pass-export-and-print-page.md`
BEFORE the `complete` flip. `F63-AC8` is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `closing-pass-export-and-print-page.result.md` beside it.
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

Seating: wave A of round 10, slot ~3; ready root, no dependency edge with FE-s-61/62/64.
