# TO DSGN_REBRND.TO-RB-s-14 -- the boundary exercise -- measured parity between the site and the portal

<to_id>DSGN_REBRND.TO-RB-s-14</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-14` | **outcome_ref:** FWD-1 | **depends_on:** `RB-s-2`, `RB-s-3`, `RB-s-4`, `RB-s-5`, `RB-s-6`, `RB-s-9`, `RB-s-10`, `RB-s-13` | **slot:** ~1, queue position 11

---

## WORKER FACE

### THE CELL

`RB-s-14` -- the boundary exercise. **PRD candidate R12.**

**Run the SAME extractor on the portal that produced the website's numbers.** `design/brand/opalinvest.com.json` was produced by the `taste` skill's DOM extractor at 1440x900. Run it against the three portal routes and write `design/brand/portal-routes.json` **in the same shape**, so the two files can be read side by side.

**The bar: every dimension of the brief's IV.3 table reads the SAME on both sides, or the difference is an enumerated inverted band with its reason.** The IV.3 dimensions are: typeface, numerals, canvas, navy's role, status colours, chart colours, loudest colour, radius, shadows, focus ring, `color-scheme`.

**⛔ The `taste` extractor is THIRD-PARTY, GITIGNORED and PINNED** in `design/SKILLS_MANIFEST.md` (`senlindesign/taste-skill`, no licence, SHA `6dce223f2f`). **Do not vendor it, do not commit it, do not edit it.** Run it in place. If it is absent, re-pull at the pinned SHA per the manifest's procedure.

**The human half.** One person who has never seen the portal is walked from `opalinvest.com` into a portal route and names capability differences and no visual ones, on record. **You cannot produce that walk.** Produce the ON-DEMAND half -- the two JSON files and a side-by-side render pair -- and record it. The walk is a judgment criterion the CVO grades at L9.

### ACCEPTANCE

<criterion id="RB14-AC1" cell_refs="RB-s-14"><invocation>cd <WS> && timeout 120 python -c "import json,io,os; p='design/brand/portal-routes.json'; d=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else None; n=(len(d) if isinstance(d,list) else len(d.keys())) if d else 0; print('ROUTES-MEASURED:',n); print('VERDICT:','MEASURED' if n>=3 else 'INCOMPLETE')"</invocation><expect>VERDICT: MEASURED</expect></criterion>
`RB14-AC1` -- the portal-side measurements exist in the website file's shape and cover AT LEAST the three fixed comparison routes. A missing file reads INCOMPLETE rather than throwing.

<criterion id="RB14-AC2" cell_refs="RB-s-14"><invocation>cd <WS> && timeout 120 python -c "import json,io,os; a=json.load(io.open('design/brand/opalinvest.com.json',encoding='utf-8')); p='design/brand/portal-routes.json'; b=json.load(io.open(p,encoding='utf-8')) if os.path.exists(p) else None; site=a['color']['canvas']['hex'].upper(); txt=json.dumps(b).upper() if b else ''; print('SITE-CANVAS:',site,'PORTAL-FILE:',bool(b),'CANVAS-IN-PORTAL:',site in txt); print('VERDICT:','PARITY-CANVAS' if (b and site in txt) else 'NO-PARITY')"</invocation><expect>VERDICT: PARITY-CANVAS</expect></criterion>
`RB14-AC2` -- the portal measurements actually CARRY the website's canvas value -- the two files are COMPARED, not merely both present.

<criterion id="RB14-AC3" cell_refs="RB-s-14"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-14_market_final_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB14-AC3` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB14-AC4" cell_refs="RB-s-14" judgment="true"/>
`RB14-AC4` -- graded at L9 from the two JSON files: every dimension of the brief's IV.3 table reads the same on both sides, or the difference is an enumerated inverted band with its reason. RECORD; NO VERDICT.

<criterion id="RB14-AC5" cell_refs="RB-s-14" judgment="true"/>
`RB14-AC5` -- graded at L9: one person who has never seen the portal is walked from opalinvest.com into a portal route and names capability differences and no visual ones, on record. The on-demand half (both JSON files and the side-by-side pair) is in the deliverables; the walk itself is not this worker's to produce. RECORD; NO VERDICT.

<expected_criteria>RB14-AC1, RB14-AC2, RB14-AC3, RB14-AC4, RB14-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **Never vendor, commit or edit the `taste` extractor.** It is unlicensed third-party code, pinned by SHA in `design/SKILLS_MANIFEST.md` and gitignored on Andrew's ruling.
- **No competitor site is captured under this order.** That is egress and needs Andrew's per-use word.

<paths>
design/brand/portal-routes.json
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-14`.
<owned_cells>RB-s-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB14-AC1` .. `RB14-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB14-AC1,RB14-AC2,RB14-AC3,RB14-AC4,RB14-AC5` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `boundary-parity.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 11; fresh worktree pair branched from `feature/d13-visual-elevation`.
