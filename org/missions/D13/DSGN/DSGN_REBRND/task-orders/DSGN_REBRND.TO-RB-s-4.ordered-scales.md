# TO DSGN_REBRND.TO-RB-s-4 -- ordered scales -- one hue, ramped light to dark

<to_id>DSGN_REBRND.TO-RB-s-4</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-4` | **outcome_ref:** FWD-3 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 4

---

## WORKER FACE

### THE CELL

`RB-s-4` -- ordered scales.

**The defect, named.** `/positioning` renders its duration ladder `UST / ST / INT / LT / ULT` in **five unrelated hues** -- orange, orange, filled green, blue, red -- for a **strictly ordered quantity**. An ordered quantity encoded as unordered hue is a READING ERROR, not a style choice, and it is a direct violation of the estate's own precedent: `deck_generation/DESIGN_BIBLE.md` rule **B1**, *dark-to-light traversal*.

**Every ordered quantity gets ONE hue, ramped light to dark.** Census `portal/src/` and print the denominator: duration ladders, performance bands, over/under-weight scales, and the Fear & Greed gauge arc on `/market` (currently a red-orange-yellow-green rainbow -- a consumer-crypto convention).

**Andrew's constraint binds and it cuts BOTH ways.** Chart series that are NOT ordered **keep their colour**. Do not desaturate a categorical palette in the name of this cell. What changes is only what encodes an ORDER.

**The test that matters: legend-covered, the order is still readable.** If a reader must consult a legend to know which end is "more", the ramp has failed.

### ACCEPTANCE

<criterion id="RB4-AC1" cell_refs="RB-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB4-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB4-AC2" cell_refs="RB-s-4"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-4_positioning_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB4-AC2` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB4-AC3" cell_refs="RB-s-4"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-4_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB4-AC3` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB4-AC4" cell_refs="RB-s-4"><invocation>cd <WS> && timeout 120 python -c "import pathlib,re; files=[p for p in pathlib.Path('portal/src').rglob('*.tsx') if re.search(r'\\bUST\\b',p.read_text(encoding='utf-8',errors='replace')) and re.search(r'\\bULT\\b',p.read_text(encoding='utf-8',errors='replace'))]; hues=set(); [hues.update(re.findall(r'(?:text|bg|border|fill|stroke)-(red|orange|amber|yellow|lime|green|emerald|teal|cyan|blue|indigo|violet|purple|fuchsia|pink|rose)-\\d{2,3}', p.read_text(encoding='utf-8',errors='replace'))) for p in files]; print('LADDER-FILES:',len(files),'DISTINCT-HUES:',len(hues),sorted(hues)); print('VERDICT:','ONE-HUE' if len(hues)<=1 else 'MULTI-HUE')"</invocation><expect>VERDICT: ONE-HUE</expect></criterion>
`RB4-AC4` -- the duration ladder resolves to AT MOST ONE named hue family. Five unrelated hues for a strictly ordered quantity is the defect this cell exists to remove; the hue list prints beside the verdict.

<criterion id="RB4-AC5" cell_refs="RB-s-4" judgment="true"/>
`RB4-AC5` -- graded at L9 from the PNGs: each ordered quantity uses ONE hue ramped light to dark; with the legend covered the order is readable; the gauge arc is a ramp, not a rainbow; and chart series that are NOT ordered still carry their colour. RECORD; NO VERDICT.

<expected_criteria>RB4-AC1, RB4-AC2, RB4-AC3, RB4-AC4, RB4-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Do not touch a categorical palette.** Only encodings of ORDER change.
- `deck_generation/DESIGN_BIBLE.md` is PRECEDENT and is READ-ONLY here.

<paths>
portal/src/
portal/src/index.css
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-4`.
<owned_cells>RB-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB4-AC1` .. `RB4-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB4-AC1,RB4-AC2,RB4-AC3,RB4-AC4,RB4-AC5` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `ordered-scales.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 4; fresh worktree pair branched from `feature/d13-visual-elevation`.
