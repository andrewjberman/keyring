# TO DSGN_RBNDV2.TO-RV-m-6 -- FWD-3: adopt the shared modal frame -- remaining overlays

<to_id>DSGN_RBNDV2.TO-RV-m-6</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~8</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>2</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-m-6` (decomp v2 @95d724679e) | **outcome_ref:** FWD-3 | **depends_on:** RV-m-1 (chain 1, position 6) | **slot:** ~8, queue position 6 of 6

---

## WORKER FACE

### THE CELL

`RV-m-6` -- ADOPT THE FRAME in the remaining overlays (InvestorReporting, SecurityScanner, SecurityAnalysis, Correlation, CapitalMarketAssumptions) and the account-menu popup (FWD-3, C-MODAL: the one permitted per-file edit).

**What adoption means.** For each file on the list below: if it draws its own modal dialog (its own `fixed inset-0` overlay, `role="dialog"` or `aria-modal`, scrim, header with title and close button, or a `catalyst/dialog` `Dialog`), replace that chrome with `ModalFrame` from `@/ui/components/modal/ModalFrame` (the frame is the first order of your queue and already exists in your worktree when this order runs; if `ModalFrame.tsx` is absent when you start, stop with a BLOCKING surprise row): the modal's title becomes `title`, its action buttons become `footer`, the rest becomes `children`; ALL state, effects, handlers, props and behaviour of the modal stay exactly as they are. If the file turns out NOT to draw a modal (a popover, dropdown, tooltip, drawer, inline panel), do not change it; list it in your test table as NOT-A-MODAL with a one-line reason. The adoption list is the deliverable: the test table names every file with ADOPTED or NOT-A-MODAL, and a modal not on a list is the defect, so also look in the files' own directories for any other `*Modal*`/`*Dialog*` file with its own overlay and name it in a surprise row (a wall: you may not edit it).

The list:
- `portal/src/pages/InvestorReporting/export/ExportModal.tsx`
- `portal/src/pages/InvestorReporting/export/ExportButton.tsx`
- `portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx`
- `portal/src/pages/SecurityScanner/tabs/UniverseScannerTab.tsx`
- `portal/src/pages/SecurityScanner/tabs/UniverseDataTab.tsx`
- `portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx`
- `portal/src/pages/Correlation/components/TickerSelector.tsx`
- `portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`
- `portal/src/App.tsx`

`src/App.tsx` is on the list ONLY for the account-menu popup (surprise row `DSGN_RBNDV2-W2-S3`: it keeps its dark styling, `bg-header`, `border-white/10`, `text-white`). It is a popover, not a modal: do NOT put it in `ModalFrame`; give its surface the A-light look (`bg-[hsl(var(--bg-surface))]`, `border border-[hsl(var(--hairline))]`, no shadow, `data-panel-surface="light"` on it) and mark it ADOPTED-AS-SURFACE in the table (its arm: it carries `data-panel-surface="light"` and no `bg-[hsl(var(--bg-header))]`). `src/ui/components/sidebar/` is NOT yours (a sibling order owns it) and `App.tsx` outside the popup is not to change. The InvestorReporting `BrowseDrawer` is a side drawer: NOT-A-MODAL unless it is a centred dialog.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's: you reproduce the fixture and invent nothing. TOKEN FORMATS (a defect in round 1 came from mixing them): the `--rb-*` tokens (`--rb-rule`, `--rb-row-rule`, `--rb-ink`, `--rb-ink-2`, `--rb-ink-3`, `--rb-quiet`, `--rb-accent`) are HEX values, so you read them as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`; `--bg-surface`, `--bg-page`, `--hairline` and the `--semantic-*` tokens are HSL triples, so you read them as `hsl(var(--X))`. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11), no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `adc70061` (the difference-control base). The fixture is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md`; read it first. Round 1 is merged on the branch: the `--rb-*` tokens, the ground `#EAEAF7`, the white panel primitives, and two scoped rules keyed on `data-panel-surface="light"` (text-white idioms resolve to navy ink; the old dark surface tokens resolve to white and silver). An element carrying `data-panel-surface="light"` therefore reads as a light surface for everything inside it. Do not start any server.

### ACCEPTANCE

<criterion id="RB2M6-AC1" cell_refs="RV-m-6"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/modal/__tests__/dsgn-rbndv2/rb-2-m6.adoption.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ADOPTION-OK</expect></criterion>
`RB2M6-AC1` -- reading each of the 9 listed files as text: a file the test table marks ADOPTED imports `ModalFrame` from `@/ui/components/modal/ModalFrame`, renders `<ModalFrame`, and contains none of `fixed inset-0`, `role="dialog"`, `aria-modal`, `aria-labelledby`, `from '@/ui/components/catalyst/dialog'`; a file marked NOT-A-MODAL carries a non-empty reason in the table and its text is byte-identical to the base (`git show adc70061:portal/<file>` from `<WS>`, compared); the table covers all 9 files with ADOPTED plus NOT-A-MODAL equal to 9 (print the denominator); (difference control: the same ADOPTED arms run on the base text of every ADOPTED file must FAIL, proving the test can fail); and an ADOPTED file contains no literal dark ground class of the form `bg-[hsl(2NN,` with a saturation and a lightness at or below 40 percent (the old navy literals, for example `bg-[hsl(221,28%,25%)]`), so the frame's light surface is never covered by a dark literal inside a modal. The test prints `VERDICT: ADOPTION-OK` only when every arm holds.

<criterion id="RB2M6-AC2" cell_refs="RV-m-6"><invocation>cd <WS>/portal && /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/modal/__tests__/dsgn-rbndv2/rb-2-m6.bound.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ADOPTION-BOUND-OK</expect></criterion>
`RB2M6-AC2` -- for each ADOPTED file, `git diff --numstat adc70061 -- <file>` (run by the test in the portal root with `execSync`) shows insertions plus deletions of at most 160 lines, and the file still contains at least its base count of `useState`, `useEffect` and `onSubmit` tokens, and at least its base count of `onClick` tokens minus 3 (the behaviour-preserved bound: a correct adoption removes at most three chrome handlers that ModalFrame now owns, the overlay click, the card stopPropagation and the header close; every action button keeps its handler). The test prints `VERDICT: ADOPTION-BOUND-OK` only when every arm holds.


<expected_criteria>RB2M6-AC1, RB2M6-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/export/ExportModal.tsx
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/SecurityScanner/tabs/UniverseScannerTab.tsx
portal/src/pages/SecurityScanner/tabs/UniverseDataTab.tsx
portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx
portal/src/pages/Correlation/components/TickerSelector.tsx
portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx
portal/src/App.tsx
portal/src/ui/components/modal/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v2.md</decomp_doc> v2 @95d724679e, cell `RV-m-6`.
<owned_cells>RV-m-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB2M6-AC1, RB2M6-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~8/DSGN_RBNDV2.TO-RV-m-6.remaining-overlays.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB2M6-AC1,RB2M6-AC2` BEFORE the flip, run from inside your worktree. No judgment criterion on this cell.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W8-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v2 -- every named existing file measured present at the feature branch adc70061; write sets are pairwise disjoint (decomp v2 section 3).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~8, queue position 6 of 6; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 8 --portal-ref feature/dsgn-rbndv2-light`.
