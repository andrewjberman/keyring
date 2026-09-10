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

### ACCEPTANCE

<criterion id="F11-AC1" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/census.ts; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC1` -- the census runs and prints `COMPONENTS: N` (record N and the REUSED/NEW split).

<criterion id="F11-AC2" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/census.test.ts</invocation><expect>0 fail</expect></criterion>
`F11-AC2` -- every census row is REUSED with a path that exists or NEW with a non-empty reason; every one of the 11 PRD reuse rows is used or carries a reason.

<criterion id="F11-AC3" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-11/colour-law.test.ts</invocation><expect>0 fail</expect></criterion>
`F11-AC3` -- no light-on-canvas class outside a dark container (record `SCANNED:`).

<criterion id="F11-AC4" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_page_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-10-global.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC4` -- the page at 390.

<criterion id="F11-AC5" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_analysis_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-6-ready.json --click Analysis; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC5` -- the Analysis tab at 390.

<criterion id="F11-AC6" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_holdings_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-7-smartx.json --click Holdings; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC6` -- the Holdings tab at 390.

<criterion id="F11-AC7" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_export_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-9-modal.json --click Export; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC7` -- the export modal at 390.

<criterion id="F11-AC8" cell_refs="FE-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=perf-narrative-fixture-1" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_print_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-8-narrative.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F11-AC8` -- the print route at 390.

<criterion id="F11-AC9" cell_refs="FE-s-11" judgment="true"/>
`F11-AC9` -- graded at L9 from the census, the brand review and every PNG of this round: the screens and the export read as one Opal product to a reviewer who knows another portal page; the controls are in the same places doing the same things. RECORD; NO VERDICT.

<expected_criteria>F11-AC1, F11-AC2, F11-AC3, F11-AC4, F11-AC5, F11-AC6, F11-AC7, F11-AC8, F11-AC9</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. This order edits no portal component; a defect found in one is a surprise row on its cell.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. The one portal path in the grant is the test folder; commit it with cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- src/pages/InvestorReporting/__tests__/fe-s-11/`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash; quote a route carrying `?`.
- **Numbers.** The width 390 is a test setup, not an acceptance value.
- **Reuse.** Every path under `portal/src/` is READ only.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-11/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-11`.
<owned_cells>FE-s-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F11-AC1` .. `F11-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json`
(phase `INVESTIGATION`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F11-AC1,F11-AC2,F11-AC3,F11-AC4,F11-AC5,F11-AC6,F11-AC7,F11-AC8,F11-AC9` BEFORE the `complete` flip. `F11-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `design-conformity-census.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
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
