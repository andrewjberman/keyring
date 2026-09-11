# TO DSGN_REBRND.TO-RB-s-11 -- one rendering system -- charting, icons and animation consolidated

<to_id>DSGN_REBRND.TO-RB-s-11</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~2</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-11` | **outcome_ref:** FWD-8 | **depends_on:** -- (chain head, chain B) | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`RB-s-11` -- one rendering system. **PRD candidate R9. This is chain B and it runs in parallel with the spine.**

**The measured duplication.** Charting: **recharts 36 files** (the incumbent), **apexcharts 4**, **@nivo 1**, **visx 1**. Icons: **lucide-react 102 files**, **phosphor-react 1**. Animation: **`framer-motion` AND `motion` both in `dependencies`**.

**Four renderers cannot produce one visual system.** FWD-8 is unreachable without this.

**Migrate onto the incumbent:** the 4 apexcharts files, the 1 nivo file and the 1 visx file move to recharts; the 1 phosphor file moves to lucide; ONE of `framer-motion`/`motion` is retained. Remove the retired packages from `portal/package.json`.

**⛔ A chart that cannot migrate without changing WHAT IT SHOWS is a SURPRISE ROW, never a quiet exception.** File the row and stop on that criterion. Changing a chart's content to make a migration succeed is out of scope and is a failure.

**`ag-grid` is a GRID, not a renderer**, and is explicitly OUT of this census. Do not touch it.

**One shared axis / tick / tooltip / legend treatment** is applied to every chart, read from RB-s-7's contract. **This cell consumes the contract; it does not define the treatment itself.**

**Enumerate the migrated files** in the result file -- the list is the evidence, not the count.

### ACCEPTANCE

<criterion id="RB11-AC1" cell_refs="RB-s-11"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB11-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB11-AC2" cell_refs="RB-s-11"><invocation>cd <WS> && timeout 120 python -c "import pathlib,collections; libs=['recharts','apexcharts','@nivo','visx','lucide-react','phosphor-react','framer-motion']; c=collections.Counter(); [ [c.__setitem__(l,c[l]+1) for l in libs if l in t] for t in [p.read_text(encoding='utf-8',errors='replace') for p in pathlib.Path('portal/src').rglob('*.tsx')] ]; retired=sum(c[l] for l in ['apexcharts','@nivo','visx','phosphor-react']); print('LIB-FILE-COUNTS:',dict(c),'RETIRED-IMPORTS:',retired); print('VERDICT:','ONE-RENDERER' if retired==0 else 'MULTI-RENDERER')"</invocation><expect>VERDICT: ONE-RENDERER</expect></criterion>
`RB11-AC2` -- apexcharts, @nivo, visx and phosphor-react all read ZERO importing files while recharts and lucide survive. **At issuance the retired set totals 6 files**, so the verdict moves only when the migration happens.

<criterion id="RB11-AC3" cell_refs="RB-s-11"><invocation>cd <WS> && timeout 120 python -c "import json,io; d=json.load(io.open('portal/package.json',encoding='utf-8')).get('dependencies',{}); r=[k for k in ['apexcharts','react-apexcharts','@nivo/core','@nivo/radar','@visx/scale','@visx/text','@visx/wordcloud','phosphor-react'] if k in d]; print('RETIRED-STILL-PRESENT:',len(r),r); print('VERDICT:','REMOVED' if len(r)==0 else 'STILL-DECLARED')"</invocation><expect>VERDICT: REMOVED</expect></criterion>
`RB11-AC3` -- the retired packages are removed from `package.json`, not merely unimported. **At issuance this reads 8.**

<criterion id="RB11-AC4" cell_refs="RB-s-11"><invocation>cd <WS> && timeout 120 python -c "import json,io; d=json.load(io.open('portal/package.json',encoding='utf-8')).get('dependencies',{}); a=[k for k in ['framer-motion','motion'] if k in d]; print('ANIMATION-LIBS:',len(a),a); print('VERDICT:','SINGLE' if len(a)==1 else 'DUPLICATED')"</invocation><expect>VERDICT: SINGLE</expect></criterion>
`RB11-AC4` -- exactly one animation library remains. **At issuance this reads 2** (`framer-motion` and `motion` both declared).

<criterion id="RB11-AC5" cell_refs="RB-s-11"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-11_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB11-AC5` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB11-AC6" cell_refs="RB-s-11" judgment="true"/>
`RB11-AC6` -- graded at L9 from the render: two charts on one screen share axis, tick, tooltip and legend treatment, and no chart shows different content than it did before. RECORD; NO VERDICT.

<expected_criteria>RB11-AC1, RB11-AC2, RB11-AC3, RB11-AC4, RB11-AC5, RB11-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **`ag-grid` is OUT of this census.** It is a grid, not a chart renderer.
- ⛔ **Never change WHAT a chart shows.** A chart that cannot migrate without a content change is a surprise row and a stop.
- **You are chain B and run in parallel with the spine.** Expect `portal/src/index.css` and the panel primitives to be moving under you: do NOT edit either -- your surfaces are the chart/icon call sites and `package.json`.

<paths>
portal/package.json
portal/src/
portal/bun.lock
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-11`.
<owned_cells>RB-s-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB11-AC1` .. `RB11-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-11.one-renderer.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB11-AC1,RB11-AC2,RB11-AC3,RB11-AC4,RB11-AC5,RB11-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `one-renderer.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~2, queue position 1; fresh worktree pair branched from `feature/d13-visual-elevation`.
