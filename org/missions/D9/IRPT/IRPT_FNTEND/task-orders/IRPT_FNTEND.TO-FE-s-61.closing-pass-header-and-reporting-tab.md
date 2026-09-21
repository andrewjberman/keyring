# TO IRPT_FNTEND.TO-FE-s-61 -- the real route, header and Reporting tab, read against DESIGN.md at the current vintage

<to_id>IRPT_FNTEND.TO-FE-s-61</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~11</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-61` (round 10, v0.10) | **outcome_ref:** FWD-12 | **depends_on:** none | **slot:** ~1 | **rows:** CTO grades `ledger/COMPLETION_GRADES.round9.json` @4030dac, FWD-12 row; CTO msg 99254

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-61` -- the header and the Reporting tab, exercised on the real route at 1440 and 390 and READ against `DESIGN.md` at its current vintage (FWD-12's closing pass, first of four surfaces).

This cell exists because the design-conformity evidence of record is stale: FE-s-11's captures predate the 2026-09-11 light-canvas ruling, and eight rounds of change (cells FE-s-12 through FE-s-60) have landed since.

**The card this closes.** PRD FWD-12: *"The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the portal needs no re-learning."* DONE WHEN (EXERCISED): *"an advisor who already uses another portal page has used all three tabs and the export without being shown anything new to learn."* The CTO graded this card `NOT_EVALUATED` because no artifact covers that limb on the real route, and named the closing pass: **the real route, all three tabs plus the export, read against DESIGN.md at the CURRENT vintage.** It is the one card where IRPT_BCKEND is NOT ENGAGED, which is why it is cut now and the other seven are not.

**Your surface.** The header (`header/`: the firm dropdown, the client search, `ScopeSummary.tsx`) and the Reporting tab (`tabs/reporting/`), reached through the default state of the route with `fe-s-10-global.json` answering the scoped routes. You may edit only files under those two directories (plus your own `__tests__/fe-s-61/`). `tabs/StatusPanel.tsx`, `state/`, `contracts/` and every shared component are READ-ONLY to you.

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

<criterion id="F61-AC1" cell_refs="FE-s-61" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F61-AC1` -- the whole portal typechecks.

<criterion id="F61-AC2" cell_refs="FE-s-61" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/fe-s-61_reporting_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-10-global.json</invocation><expect>CANVAS: rgb\(244, 246, 250\)</expect></criterion>
`F61-AC2` -- the real route `investor-reporting` at 1440, header and Reporting tab, fixtures answered at the network layer: the printed `CANVAS:` value is `rgb(244, 246, 250)`.

<criterion id="F61-AC3" cell_refs="FE-s-61" drives="none"><invocation>cd <WS>/portal && timeout 180 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/fe-s-61_reporting_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-10-global.json</invocation><expect>CANVAS: rgb\(244, 246, 250\)</expect></criterion>
`F61-AC3` -- the same route at 390: the printed `CANVAS:` value is `rgb(244, 246, 250)`.

<criterion id="F61-AC4" cell_refs="FE-s-61" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F61-AC4` -- the whole IRPT_FNTEND suite is green (with your dev server STOPPED and its port verified closed).

<criterion id="F61-AC5" cell_refs="FE-s-61" judgment="true" drives="none"/>
`F61-AC5` -- graded at L9 by the CVO: for BOTH captures, the header (the firm dropdown, the client search, the ScopeSummary strip including FE-s-59's partial-disclosure fact) and the Reporting tab (summary cards, chart, period results, status panel) are read against DESIGN.md at its current vintage, clause by clause, each citing its `C<n>`; the firm dropdown is confirmed to be the Model Portfolios component by reading the import in source, not by appearance; every fix has its BEFORE and AFTER capture beside it and every unfixed finding is a row. RECORD; NO VERDICT.

<expected_criteria>F61-AC1, F61-AC2, F61-AC3, F61-AC4, F61-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is a JUDGMENT criterion: RECORD the evidence, give NO verdict; the CVO
  grades it at L9. You never self-grade it and you never write "conforms" as a conclusion -- you write what the capture shows.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in
  the workspace repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use
  `.tools/safe-commit.sh` with a message file written by your Write tool.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W11-S<k>`; read the investigation file before minting; append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Disjoint by file from the other three cells of this round** (each owns its own portal write surface; every shared file is read-only
  to all four).
- FE-s-59 recently edited `header/ScopeSummary.tsx` (its own additive fact, merged at portal `baad86f0`); read its `PartialDisclosureFact` before judging that strip.

<paths>
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/__tests__/fe-s-61/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.10, cell `FE-s-61`.
<owned_cells>FE-s-61</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F61-AC1`, `F61-AC2`, `F61-AC3`, `F61-AC4`, `F61-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/IRPT_FNTEND.TO-FE-s-61.closing-pass-header-and-reporting-tab.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F61-AC1,F61-AC2,F61-AC3,F61-AC4,F61-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-61.closing-pass-header-and-reporting-tab.md`
BEFORE the `complete` flip. `F61-AC5` is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `closing-pass-header-and-reporting-tab.result.md` beside it.
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

Seating: wave A of round 10, slot ~1; ready root, no dependency edge with FE-s-62/63/64.
