# TO DSGN_REBRND.TO-RB-s-5 -- accent rationing and ONE control vocabulary

<to_id>DSGN_REBRND.TO-RB-s-5</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-5` | **outcome_ref:** FWD-4 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 5

---

## WORKER FACE

### THE CELL

`RB-s-5` -- accent rationing and one set of controls.

**The budget, by ROLE (CVO correction C2).** A view carries the accent on **exactly ONE PERSISTENT primary action**. The **transient** focus ring (RB-s-6) and the text-selection highlight **share the accent and are NOT counted against that one**. Measured on the live site, `#5F3BE3` never exceeds **1.0%** of visible surface on any page.

**The defect, counted.** `/positioning` carries **FIVE button idioms in one viewport**: a filled accent pill group (MODELS/ETFS/SATELLITES), a second smaller filled accent pill group (Portfolio/Benchmark/Relative/Custom), a five-hue segmented control, a third filled accent pair (Characteristics/Performance), and an outlined ghost button (EXPAND DETAILS). They become **ONE vocabulary**: primary / secondary / ghost / segmented.

**Active state is marked by WEIGHT and RULE, never by a filled accent chip per option.** A segmented control with a filled accent chip on every option spends the budget five times.

**Retire chartreuse from the chrome.** `portal/src/index.css:69` sets `--sentiment-chartreuse: #ADFF2F` -- the loudest colour rendered anywhere in the product and not a brand colour. It may survive INSIDE a chart series only under RB-s-1's data family.

**`::selection`** at `:171` currently uses `--warning` (orange, off-palette); put it on the accent.

**Column-header underlines are removed** -- `DESIGN_BIBLE.md` C4 bans them by name as a generated-design tell, and `/positioning` renders them.

**Walk the counterexample** on each of the three routes: primary visible + a secondary control focused + text selected, and the PERSISTENT count stays one.

### ACCEPTANCE

<criterion id="RB5-AC1" cell_refs="RB-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB5-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB5-AC2" cell_refs="RB-s-5"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-5_positioning_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB5-AC2` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB5-AC3" cell_refs="RB-s-5"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs portfolio-management <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-5_pm_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB5-AC3` -- the `/portfolio-management` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB5-AC4" cell_refs="RB-s-5"><invocation>cd <WS> && timeout 120 python -c "import io; s=io.open('portal/src/index.css',encoding='utf-8').read().lower(); c=s.count('adff2f'); w=len([1 for l in s.splitlines() if '::selection' in l]); print('CHARTREUSE:',c); print('VERDICT:','RETIRED' if c==0 else 'CHARTREUSE-REMAINS')"</invocation><expect>VERDICT: RETIRED</expect></criterion>
`RB5-AC4` -- chartreuse is gone from the stylesheet chrome. **At issuance this reads 1** -- it is the loudest colour rendered anywhere in the product and is not a brand colour.

<criterion id="RB5-AC5" cell_refs="RB-s-5" judgment="true"/>
`RB5-AC5` -- graded at L9 from the PNGs: each route carries the accent on exactly ONE persistent primary action (enumerated in the result file); no tab, toggle or segmented control gives every option a filled accent chip; the five idioms of `/positioning` are one vocabulary; and no colour off the brand-derived palette is the loudest thing on any page. RECORD; NO VERDICT.

<criterion id="RB5-AC6" cell_refs="RB-s-5" judgment="true"/>
`RB5-AC6` -- graded at L9 from the counterexample walk: with a primary visible, a secondary control focused and text selected, the PERSISTENT accent count is still one. RECORD; NO VERDICT.

<expected_criteria>RB5-AC1, RB5-AC2, RB5-AC3, RB5-AC4, RB5-AC5, RB5-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- The transient ring is RB-s-6's to build; this cell must not double-define it.

<paths>
portal/src/index.css
portal/src/ui/
portal/src/components/
portal/src/pages/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-5`.
<owned_cells>RB-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB5-AC1` .. `RB5-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB5-AC1,RB5-AC2,RB5-AC3,RB5-AC4,RB5-AC5,RB5-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `accent-controls.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 5; fresh worktree pair branched from `feature/d13-visual-elevation`.
