# TO DSGN_REBRND.TO-RB-s-12 -- the affected-surface inventory, with a denominator

<to_id>DSGN_REBRND.TO-RB-s-12</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~3</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-12` | **outcome_ref:** FWD-1, FWD-4, FWD-5, FWD-10, FWD-11 | **depends_on:** -- (chain head, chain C) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`RB-s-12` -- the affected-surface inventory. **PRD candidate R14 split, part 1. This is chain C and it can be minted before any visual change exists.**

**The gap it closes.** The brief admits at VII.2 that **three of twenty-six routes** were rendered. Every visual finding in the brief's IV.9 came from three pages; every code finding came from a tree-wide census. **That asymmetry is what this cell converts into a denominator.**

**Build `design/brand/portal-surface-inventory.json`:** every route (denominator = **the portal's route count, PRINTED**, read from the route table in `portal/src/App.tsx`) x every state a cell touches (default, empty, loading, error, no-permission, and any toggled panel), each row carrying:
- its **fixture source** (an existing `portal/.frontend-dev/testing/` file, or `NONE` where one must be minted),
- its **render obligation** (does a cell touch this route/state),
- its **keyboard obligation** (is the surface interactive).

**The existing verification rule is RETAINED BY NAME, not replaced.** `design/process/UI_VERIFICATION.md` requires a read screenshot for every client-facing visual change and every state touched. This inventory is the DENOMINATOR that rule operates over -- brief IV.7: the estate already has the pattern, do not invent a second mechanism.

**⛔ COMPONENT REUSE IS RECORDED AS EVIDENCE BESIDE A ROW AND NEVER SUBSTITUTES FOR RENDERING A DISTINCT LAYOUT.** "It uses the same Panel" is not a render.

**The three IV.9 routes (`/market`, `/positioning`, `/portfolio-management`) remain the FIXED before/after comparison set** and are marked as such in the inventory.

### ACCEPTANCE

<criterion id="RB12-AC1" cell_refs="RB-s-12"><invocation>cd <WS> && timeout 120 python -c "import json,io,os; p='design/brand/portal-surface-inventory.json'; d=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else None; rows=((d.get('rows') if isinstance(d,dict) else d) or []) if d else []; dec=d.get('route_count') if isinstance(d,dict) else None; print('INVENTORY-ROWS:',len(rows),'ROUTE-DENOMINATOR:',dec); print('VERDICT:','HAS-DENOMINATOR' if (dec and len(rows)>0) else 'ABSENT-OR-UNDENOMINATED')"</invocation><expect>VERDICT: HAS-DENOMINATOR</expect></criterion>
`RB12-AC1` -- the inventory exists, is non-empty AND prints its route denominator -- a row count without a denominator is a sample, not an inventory. A missing file reads ABSENT rather than throwing a traceback at you.

<criterion id="RB12-AC2" cell_refs="RB-s-12"><invocation>cd <WS> && timeout 120 python -c "import re,io,json,os; s=io.open('portal/src/App.tsx',encoding='utf-8').read(); r=sorted(set(x for x in re.findall(r'path=.([A-Za-z0-9_/:*-]+).',s) if x not in ('*','/*'))); p='design/brand/portal-surface-inventory.json'; d=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else {}; dec=d.get('route_count'); print('APP-ROUTES:',len(r),'INVENTORY-DENOMINATOR:',dec); print('VERDICT:','AGREES' if dec==len(r) else 'DISAGREES')"</invocation><expect>VERDICT: AGREES</expect></criterion>
`RB12-AC2` -- the inventory's printed denominator EQUALS the router's own route count. A denominator that does not match its source is a number, not a denominator. **At issuance the router reads 26 and the inventory does not exist.**

<criterion id="RB12-AC3" cell_refs="RB-s-12"><invocation>cd <WS> && timeout 120 python -c "import json,io,os; p='design/brand/portal-surface-inventory.json'; d=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else {}; rows=d.get('rows',[]); miss=[r for r in rows if 'fixture' not in r]; print('ROWS:',len(rows),'WITHOUT-FIXTURE-FIELD:',len(miss)); print('VERDICT:','ALL-SOURCED' if (rows and not miss) else 'INCOMPLETE')"</invocation><expect>VERDICT: ALL-SOURCED</expect></criterion>
`RB12-AC3` -- EVERY row carries a fixture source (NONE is a valid source) and the row set is non-empty -- an empty inventory cannot pass vacuously.

<criterion id="RB12-AC4" cell_refs="RB-s-12" judgment="true"/>
`RB12-AC4` -- graded at L9: the inventory names every route and every touched state with a denominator and a fixture source; the three IV.9 routes are marked as the fixed comparison set; and component reuse appears as evidence beside a row, never as a substitute for a render. RECORD; NO VERDICT.

<expected_criteria>RB12-AC1, RB12-AC2, RB12-AC3, RB12-AC4</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **You are chain C and run in parallel.** You write ONE file and read the router. Do NOT edit any component, stylesheet or token file.

<paths>
design/brand/portal-surface-inventory.json
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-12`.
<owned_cells>RB-s-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB12-AC1` .. `RB12-AC4`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-12.surface-inventory.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB12-AC1,RB12-AC2,RB12-AC3,RB12-AC4` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `surface-inventory.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~3, queue position 1; fresh worktree pair branched from `feature/d13-visual-elevation`.
