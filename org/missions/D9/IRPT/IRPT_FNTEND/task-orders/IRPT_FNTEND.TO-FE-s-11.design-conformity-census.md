# TO IRPT_FNTEND.TO-FE-s-11 -- design conformity: component census, brand review, narrow viewport

<to_id>IRPT_FNTEND.TO-FE-s-11</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F13; PATHS table, 11 reuse rows) | **Decomp cell:** `FE-s-11` | **outcome_ref:** FWD-12 | **depends_on:** `FE-s-10` (terminal) | **slot:** ~1, queue position 7

---

## WORKER FACE

### THE CELL

`FE-s-11` -- the census, the brand review and the narrow-viewport exercise on the real route. This order writes no portal code; its product is the record.

**Census** at `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/component-census.json` and `.md`: enumerate every import under `portal/src/pages/InvestorReporting/**` (excluding `__tests__/` and `fixtures/`) that resolves to a React component (a `.tsx` module export used as JSX). Denominator printed: `COMPONENTS: N`. Each row: `component`, `importedFrom`, `classification` `REUSED | NEW`, and for REUSED the exact existing repository path outside `pages/InvestorReporting/`, for NEW a `reason` a reviewer can dispute (the existing set could not meet a stated need). The subtraction base is the PRD PATHS table's 11 reuse rows: every reuse row is marked `used by <cells>` or `NOT USED: <reason>`. The census is produced by `census.ts` under your deliverables folder, run with `bun run census.ts` from `<WS>/portal` (bun executes TypeScript directly; the script reads the source tree and writes both files). The `.md` carries the same rows as a table.

**Brand review** at `deliverables/.../brand-review.md`: for each screen PNG (page, three tabs, export modal, print performance, print analysis) the colours, logo clear space and typeface observed against `deck_generation/brand_spec/brand.json` and `deck_generation/brand/opal_brand_guidelines.pdf`; the firm dropdown confirmed as `PageSurfaceControl as="dropdown"` by import (a row in the census); every chart's table equivalent listed with its component.

**Narrow-viewport exercise**: the 390 renders of the page, each tab, the export modal and the print route, saved under your deliverables folder as `fe-s-11_<screen>_390.png`, using the smoke maps earlier cells left under `fixtures/smoke/`.

**Colour-law scan** by `colour-law.test.ts` under `__tests__/fe-s-11/`: reads `pages/InvestorReporting/**/*.tsx` and asserts no `text-white`, `text-[a-z]+-300`, `bg-white/` class token appears outside a JSX element whose ancestor in the same file carries `Panel` or `variant="dark"`; prints `SCANNED: n files`.

**Three repairs (AMENDED BY THE ISSUER at the FE-s-11 report on rows IRPT_FNTEND-W1-S11 and IRPT_FNTEND-W1-S12).** The census found three defects no other order can carry (every other order is terminal); this order repairs them in exactly the three portal files added to `<paths>`, and the BOUNDS clause "this order edits no portal component" is withdrawn for those three files only. Your existing census, brand review, tests and commits stand; re-run the amended criteria and re-capture the PNGs they name.

(1) **One-firm crash (W1-S12)** -- `global/useFirmContext.ts`. The effect keyed on `[scope]` also fires while the re-keyed `resolve-scope` query is loading: `index.tsx` keys the query on `firmId`, so the hook's own `onChange(firm)` re-keys the query, `scope` becomes `undefined` for one render, `resolveFirmSelection(value, undefined)` reads an empty catalogue and returns `global`, `onChange('global')` re-keys back to the cached one-firm answer, which resolves to the firm again -- an infinite ping-pong that React reports as `Maximum update depth exceeded`. With two or more firms the `global` candidate is stable, which is why only one-firm fixtures crash. Repair: as the FIRST statement of the effect, `if (scope == null) return` -- a missing resolution is not a catalogue of zero firms -- placed BEFORE `loadedOnce.current = true`, so the URL/persisted candidate is still read at the first REAL resolution. No other line of the hook changes.

(2) **Colour law (W1-S11)** -- `export/AppliedBranding.tsx` carries `text-white/80` and `text-white` with no dark container in its own file, and nothing mounts it today. Repair: replace those two tokens with `text-slate-700` and `text-slate-900`; nothing else in the file changes. Wiring `AppliedBranding` and `ReceiptPanel` into the export flow is round-2 scope and is NOT done here.

(3) **Print route fixture** -- since FE-s-9, `render/PrintEntry.tsx` resolves the bundle's referenced report and narrative packet THROUGH THE TYPED CLIENT (`export/resolveBundle.ts`), and `fixtures/smoke/fe-s-8-narrative.json` serves only `export-preview` (its inline `performanceReport`/`narrativePacket` are the pre-FE-s-9 shape and are never read), so the print PNG reads "rev-000401 is absent". Repair: add `fixtures/smoke/fe-s-11-print.json` with three keys: the `investor-reporting/export-preview` body copied from `fe-s-8-narrative.json` unchanged, plus the two route substrings the typed client requests for the performance report and the narrative packet (read them from the client under `contracts/` and match the key shape `fe-s-6-ready.json` uses), each serving the response the client expects at revision `rev-000401`, built from `fe-s-8-narrative.json`'s inline payloads. `fe-s-8-narrative.json` itself is not edited. `resolveBundle` logs `REFS RESOLVED: n of n` to the page console, and ui-smoke's `--console <substring>` flag prints matching console lines as `CONSOLE[log]: ...`.

### ACCEPTANCE

<criterion id="F11-AC1" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/census.ts; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC1` -- the census runs and prints `COMPONENTS: N` (record N and the REUSED/NEW split).

<criterion id="F11-AC2" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/census.test.ts</invocation><expect>0 fail</expect></criterion>
`F11-AC2` -- every census row is REUSED with a path that exists or NEW with a non-empty reason; every one of the 11 PRD reuse rows is used or carries a reason.

<criterion id="F11-AC3" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/colour-law.test.ts</invocation><expect>0 fail</expect></criterion>
`F11-AC3` -- no light-on-canvas class outside a dark container (record `SCANNED:`).

<criterion id="F11-AC4" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_page_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-10-global.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC4` -- the page at 390.

<criterion id="F11-AC5" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_analysis_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-6-ready.json --click Analysis --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Analysis</expect></criterion>
`F11-AC5` -- the Analysis tab at 390 (AMENDED: the bar is the printed `CLICKED: Analysis`; the error boundary has no Analysis control, so a crash prints `CLICK-FAIL` instead; a one-firm scope is the case).

<criterion id="F11-AC6" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_holdings_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-7-smartx.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F11-AC6` -- the Holdings tab at 390 (AMENDED: the bar is the printed `CLICKED: Holdings`).

<criterion id="F11-AC7" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_export_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-9-modal.json --click Export --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Export</expect></criterion>
`F11-AC7` -- the export modal at 390 (AMENDED: the bar is the printed `CLICKED: Export`).

<criterion id="F11-AC8" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=perf-narrative-fixture-1" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_print_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-11-print.json --console "REFS RESOLVED"; echo rc=$?</invocation><expect>CONSOLE[log]: REFS RESOLVED: 1 of 1</expect></criterion>
`F11-AC8` -- the print route at 390 (AMENDED: the fixture is `fe-s-11-print.json` and the bar is the resolver's own printed line; the PNG then shows the performance document, not the "was not rendered" panel).

<criterion id="F11-AC9" cell_refs="FE-s-11" judgment="true"/>
`F11-AC9` -- graded at L9 from the census, the brand review and every PNG of this round: the screens and the export read as one Opal product to a reviewer who knows another portal page; the controls are in the same places doing the same things. RECORD; NO VERDICT.

<criterion id="F11-AC10" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F11-AC10` (AMENDED, added) -- the whole Investor Reporting test set is green after the three repairs (record the pass count; 236 passed on DEV before this order's own tests).

<expected_criteria>F11-AC1, F11-AC2, F11-AC3, F11-AC4, F11-AC5, F11-AC6, F11-AC7, F11-AC8, F11-AC9, F11-AC10</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. This order edits no portal component EXCEPT the three files the amendment names (`global/useFirmContext.ts`, `export/AppliedBranding.tsx`, `fixtures/smoke/fe-s-11-print.json`), each exactly as the amendment states; any other defect found is a surprise row on its cell.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. The portal paths in the grant are the test folder and the three amendment files; commit them with cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- src/pages/InvestorReporting/__tests__/fe-s-11/ src/pages/InvestorReporting/global/useFirmContext.ts src/pages/InvestorReporting/export/AppliedBranding.tsx src/pages/InvestorReporting/fixtures/smoke/fe-s-11-print.json`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash; quote a route carrying `?`.
- **Numbers.** The width 390 is a test setup, not an acceptance value.
- **Reuse.** Every path under `portal/src/` is READ only.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-11/
portal/src/pages/InvestorReporting/global/useFirmContext.ts
portal/src/pages/InvestorReporting/export/AppliedBranding.tsx
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-11-print.json
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-11`.
<owned_cells>FE-s-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F11-AC1` .. `F11-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json`
(phase `INVESTIGATION`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F11-AC1,F11-AC2,F11-AC3,F11-AC4,F11-AC5,F11-AC6,F11-AC7,F11-AC8,F11-AC9,F11-AC10` BEFORE the `complete` flip. `F11-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `design-conformity-census.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
lane: the <paths> block IS the grant; the deliverables folder is grant-free by the tree convention and carries the census, the review and the PNGs.
</preflight>

Seating: slot ~1, queue position 7, last; seated when `FE-s-10` is terminal and drained, fresh worktree pair from HEAD.
