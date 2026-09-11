# TO DSGN_REBRND.TO-RB-s-9 -- density -- the work fills the screen, and a designed end state

<to_id>DSGN_REBRND.TO-RB-s-9</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

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

<expected_criteria>RB9-AC1, RB9-AC2, RB9-AC3, RB9-AC4, RB9-AC5, RB9-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **Adding a panel or a row to fill space is a FAILURE, not a pass.** Information architecture is out of scope (brief Part II).

<paths>
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
Criterion ids: `RB9-AC1` .. `RB9-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB9-AC1,RB9-AC2,RB9-AC3,RB9-AC4,RB9-AC5,RB9-AC6` BEFORE the `complete` flip.
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
