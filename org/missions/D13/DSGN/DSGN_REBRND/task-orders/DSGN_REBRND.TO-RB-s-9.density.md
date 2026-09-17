# TO DSGN_REBRND.TO-RB-s-9 -- density -- the work fills the screen, and a designed end state

<to_id>DSGN_REBRND.TO-RB-s-9</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-9` | **outcome_ref:** FWD-10 | **depends_on:** `RB-s-3`, `RB-s-7` | **slot:** ~1, queue position 9

---

## WORKER FACE

### THE CELL

`RB-s-9` -- density.

**The defect.** Every rendered route devotes roughly its **lower third** to empty canvas while the content above it is tightly packed. The density gradient runs the wrong way.

**The rule, from the contract: generous INSIDE a container, disciplined BETWEEN sections.** Space belongs inside the work, not around it. Apply the spacing ladder RB-s-7's contract carries: `13.5 / 20 / 30 / 45 / 53.33 / 80` (the live site's ladder, ratio ~1.5).

**⛔ THIS IS NOT A FOLD QUOTA (CVO correction C3), AND THAT DISTINCTION IS THE WHOLE CELL.** You are graded on SPACING and on an EXPLICIT END STATE -- never on filling a viewport. **Information architecture is out of scope**: adding a panel, stretching a row, or inventing filler to reach the fold is a FAILURE of this cell, not a pass.

**A page that has run out of content ends with the contract's designed terminator**, not with canvas trailing off.

**The negative control is mandatory**: a SPARSE-populated route (one short row, panels intact) must still end with the designed terminator and must still read as finished. It is graded on spacing and that end state, with no filler added.

**Use populated fixtures.** `portal/.frontend-dev/testing/` carries fixtures; mint new JSON where none exists. **The brief's own captures ran against a failing data plane (401s, empty sets) and are evidence of nothing for this cell.**

**AMENDED BY THE ISSUER on row `DSGN_REBRND-S1`, found by ANDREW on `/attribution`.**

**A DATA LABEL IS NEVER PAINTED OVER BY A CHART ORNAMENT.** On the
`STYLE VS BENCHMARK POSITIONING` panel the divergence bar's value label is overlapped and visually
truncated by the centre target icon — the underweight label reads `-8.7` with the percent sign cut,
the overweight label's leading `+` is hidden.

**The mechanism, read from source** (`portal/src/pages/Attribution/components/StylePolicyComparison.tsx`):
the ornament at `:337-341` is `absolute left-1/2 -translate-x-1/2 z-20` around a `px-3 rounded-full`
pill — about **15px of half-width either side of the axis**. Each bar container (`:298`, `:316`)
stops `pr-2` / `pl-2` — **8px** — short of that axis. **15 > 8**, so the ornament's footprint sits
over each bar's inner edge and `z-20` paints it above the label. The labels (`:301`, `:319`) are
placed bar-relative (`justify-start pl-4` / `justify-end pr-4`) inside a bar of `width: barWidth%`,
so a **small tilt gives a narrow bar** the `text-lg` label cannot fit inside, and the overflow runs
toward the axis and under the ornament.

⛔ **BOTH HALVES MUST CHANGE OR IT IS NOT FIXED.** The ornament must **reserve its footprint** (the
bars' gap from the axis must exceed the ornament's half-width), **and** the label must be placed
with **awareness of the ornament** — when the bar is too narrow to hold the label, the label goes
OUTSIDE the bar, away from the axis, where there is room.

⛔ **RAISING OR LOWERING A Z-INDEX IS NOT A FIX.** It only chooses which of the two is hidden.

⚠ **This defect renders ONLY with data.** This lane's own render of `/attribution` returned
skeleton loaders and could not reproduce it — the diagnosis above is from source. **Your populated
fixtures are what make it visible**, which is why it lands in this cell and not another.

⚠ **Scope bound:** this is a LAYOUT fix inside an existing component. You do not change what the
panel shows, what it computes, or which figures appear. Information architecture stays out of scope.

**ALSO -- ONE BOUNDED ACT FOLDED IN BY THE ISSUER (2026-09-14, row `DSGN_REBRND-W1-S24`).** RB-s-6 rewrote four
stale source comments onto the C3 law and found a FIFTH it was not granted: `src/pages/TicketCenter/TicketCenter.tsx:174`
still calls the canvas "silver". Rewrite THAT COMMENT so it states the light canvas `#F4F6FA` and points at
`portal/DESIGN.md` clause C3 as the law. **Comment only -- change no code and no value.** Your `<paths>` already grant
`portal/src/pages/`. Evidence: a census of `silver` (case-insensitive) over that one file, before and after, the after
count printed.

### ACCEPTANCE

<criterion id="RB9-AC1" cell_refs="RB-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB9-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB9-AC2" cell_refs="RB-s-9"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-9_market_populated_1440.png --port <PORT> --fixtures <WS>/portal/.frontend-dev/testing/rb-s-9-market.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB9-AC2` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB9-AC3" cell_refs="RB-s-9"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-9_positioning_sparse_1440.png --port <PORT> --fixtures <WS>/portal/.frontend-dev/testing/rb-s-9-sparse.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB9-AC3` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB9-AC4" cell_refs="RB-s-9" judgment="true"/>
`RB9-AC4` -- graded at L9 from the POPULATED renders: the work fills the screen, and the share of viewport below the last content element is printed before and after. RECORD; NO VERDICT.

<criterion id="RB9-AC5" cell_refs="RB-s-9" judgment="true"/>
`RB9-AC5` -- graded at L9 from the SPARSE negative control: the page ends with the contract's designed terminator and reads as finished -- with NO filler, NO stretched row and NO added panel. RECORD; NO VERDICT.

<criterion id="RB9-AC6" cell_refs="RB-s-9" judgment="true"/>
`RB9-AC6` -- graded at L9: between-section spacing is less than inside-container spacing on the render, read against the contract clause. RECORD; NO VERDICT.

<criterion id="RB9-AC7" cell_refs="RB-s-9"><invocation>cd <WS>/portal && timeout 120 python -c "import json,sys,os; p='.scratch/rb-s-9-label-collision.json'; d=json.load(open(p,encoding='utf-8')) if os.path.exists(p) else None; pairs=(d or {}).get('pairs',[]); bad=[x for x in pairs if x.get('overlap_px',0)>0]; print('LABEL/ORNAMENT PAIRS MEASURED:',len(pairs)); print('OVERLAPPING:',len(bad),[x.get('label') for x in bad][:6]); print('VERDICT:','NO-COLLISION' if (pairs and not bad) else 'COLLIDES-OR-UNMEASURED')"</invocation><expect>VERDICT: NO-COLLISION</expect></criterion>
`RB9-AC7` -- **row `DSGN_REBRND-S1`.** Render `/attribution` with a POPULATED fixture, and for every divergence bar measure the label's bounding box against the centre ornament's, writing each pair and its `overlap_px` to `.scratch/rb-s-9-label-collision.json`. **Every pair must read `overlap_px: 0`, and the pair set must be NON-EMPTY** -- an empty set would pass vacuously, and a skeleton render produces exactly that. Measure both a small tilt (narrow bar, the failing case) and a large one.

<expected_criteria>RB9-AC1, RB9-AC2, RB9-AC3, RB9-AC4, RB9-AC5, RB9-AC6, RB9-AC7</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **Adding a panel or a row to fill space is a FAILURE, not a pass.** Information architecture is out of scope (brief Part II).

<paths>
portal/src/pages/Attribution/components/StylePolicyComparison.tsx
portal/src/ui/components/panels/
portal/src/pages/
portal/.frontend-dev/testing/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-9`.
<owned_cells>RB-s-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids (corrected 2026-09-14 by the issuer -- the row-S1 amendment added `RB9-AC7` to `<expected_criteria>`
but not here, so the collision criterion would never have been graded): `RB9-AC1` .. `RB9-AC7`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB9-AC1,RB9-AC2,RB9-AC3,RB9-AC4,RB9-AC5,RB9-AC6,RB9-AC7` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `density.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 9; fresh worktree pair branched from `feature/d13-visual-elevation`.
