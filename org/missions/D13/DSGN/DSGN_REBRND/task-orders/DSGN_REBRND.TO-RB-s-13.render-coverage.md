# TO DSGN_REBRND.TO-RB-s-13 -- render and keyboard coverage over the inventory

<to_id>DSGN_REBRND.TO-RB-s-13</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~3</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-13` | **outcome_ref:** FWD-1, FWD-4, FWD-5, FWD-10, FWD-11 | **depends_on:** `RB-s-12`, and the spine cells whose surfaces it covers | **slot:** ~3, queue position 2

---

## WORKER FACE

### THE CELL

`RB-s-13` -- the coverage campaign. **PRD candidate R14 split, part 2.**

**Execute the obligations RB-s-12's inventory names.** For every row marked with a render obligation: one **read** render (render, LOOK, then commit -- the existing loop's rule, retained by name). For every row marked interactive: a keyboard walk with a screenshot at each stop.

**⛔ "READ" IS THE LOAD-BEARING WORD.** A screenshot that is captured and not looked at is not evidence. `design/process/UI_VERIFICATION.md`'s rule is render-LOOK-then-commit, and the LOOK is the step that catches the defect class a grep cannot see -- light text on the canvas, a ghost button outside a dark panel.

**⚠ THIS CELL MEASURES A TREE THAT MUST HAVE STOPPED MOVING.** The decomposition (§5) states the ordering constraint: chains B and C's first cell drain BEFORE this one, and the spine's visual cells must be terminal. **If you find a surface still changing under you, that is a surprise row and a stop, not a re-render.**

**Coverage is reported against the inventory's denominator**, never against "the routes I got to".

### ACCEPTANCE

<criterion id="RB13-AC1" cell_refs="RB-s-13"><invocation>cd <WS> && timeout 120 python -c "import json,io,os; p='design/brand/portal-surface-inventory.json'; d=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else {}; rows=d.get('rows',[]); need=[r for r in rows if r.get('render_obligation')]; print('RENDER-OBLIGATIONS:',len(need),'of',len(rows)); print('VERDICT:','HAS-OBLIGATIONS' if need else 'EMPTY-SET')"</invocation><expect>VERDICT: HAS-OBLIGATIONS</expect></criterion>
`RB13-AC1` -- the obligation set is read from the inventory and is NON-EMPTY, so coverage is measured against the whole rather than against what was reached. An empty set is REFUSED, never passed.

<criterion id="RB13-AC2" cell_refs="RB-s-13"><invocation>cd <WS> && timeout 120 python -c "import pathlib,json,io,os; d=pathlib.Path('org/missions/D13/DSGN/DSGN_REBRND/deliverables'); pngs=list(d.rglob('*.png')) if d.exists() else []; p='design/brand/portal-surface-inventory.json'; inv=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else {}; need=[r for r in inv.get('rows',[]) if r.get('render_obligation')]; print('RENDERS-ON-RECORD:',len(pngs),'OBLIGATIONS:',len(need)); print('VERDICT:','COVERED' if (need and len(pngs)>=len(need)) else 'SHORT')"</invocation><expect>VERDICT: COVERED</expect></criterion>
`RB13-AC2` -- the renders on record meet or exceed the inventory's render obligations AND the obligation set is non-empty. **At issuance this reads 0 renders / 0 obligations -> SHORT**, which is why the non-empty guard is there: 0 >= 0 would otherwise pass vacuously.

<criterion id="RB13-AC3" cell_refs="RB-s-13"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-13_market_coverage_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB13-AC3` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB13-AC4" cell_refs="RB-s-13" judgment="true"/>
`RB13-AC4` -- graded at L9: every touched surface in the inventory has a read render on record and every touched interactive surface has a keyboard walk; coverage is stated against the inventory's denominator. RECORD; NO VERDICT.

<expected_criteria>RB13-AC1, RB13-AC2, RB13-AC3, RB13-AC4</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **You render and you read. You do not FIX.** A defect you see is a surprise row routed to the owning cell, never an edit here.

<paths>
design/brand/portal-surface-inventory.json
org/missions/D13/DSGN/DSGN_REBRND/deliverables/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-13`.
<owned_cells>RB-s-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB13-AC1` .. `RB13-AC4`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-13.render-coverage.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB13-AC1,RB13-AC2,RB13-AC3,RB13-AC4` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `render-coverage.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- 3 gates registered for this project (FWD-9's grade half, Andrew's; the brief's Appendix A prose defect; comp-adversary's false-GONE path parser). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: an AWS-surface token sweep returned 0 hits over the PRD's SURFACE MANIFEST and 0 over the whole PRD. No cell writes an AWS surface.
comp-adversary: RUN at L5 on the PRD -- 3 of 3 cited commits verified; 19 paths, 16 stable, 3 GONE all resolved (one is the register's own dangling D13 doc, one is `portal/DESIGN.md` correctly absent on CLOUD, one is a FALSE GONE from the tool's path parser). Blindness stated: its complement is filesystem adjacency, not the dependency chain.
lane: the `<paths>` block IS the grant (RULING 1). `design/` resolves UNDEFINED in `.owned-paths.yaml` for every agent -- a refusal there is a BLOCKING row, never an override.
</preflight>

Seating: slot ~3, queue position 2; fresh worktree pair branched from `feature/d13-visual-elevation`.
