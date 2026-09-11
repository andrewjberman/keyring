# TO DSGN_REBRND.TO-RB-s-10 -- empty, loading, error and no-permission -- four designed states

<to_id>DSGN_REBRND.TO-RB-s-10</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-10` | **outcome_ref:** FWD-11 | **depends_on:** `RB-s-7` | **slot:** ~1, queue position 10

---

## WORKER FACE

### THE CELL

`RB-s-10` -- the four states.

**The defect, counted.** SIX distinct "nothing here" treatments across three routes: a centred grey sentence, a two-line grey sentence, a bordered red error, **a duplicated error string on the raw canvas**, an em-dash-filled table, and a panel that renders its header and then nothing.

**Four designed states, in the existing component set:** EMPTY, LOADING, ERROR, NO-PERMISSION. Every panel with nothing to show uses exactly one of them, and **the message says WHICH in plain words** -- "no holdings for this model" beats "No data available".

**⛔ No message repeats itself.** `/market` renders *"Failed to load market data: Failed to load market data: Error: Failed to fetch market returns from all available sources"*. That duplication is a real bug in the message assembly, not a styling problem.

**⛔ No error is painted on the bare canvas.** `portal/CLAUDE.md`'s existing colour law already says canvas-level notices are dark-on-light (`text-red-900` on `bg-red-500/10`), never `text-{color}-300`. The duplicated string violates the law the portal already has.

**Census every empty/loading/error/no-permission rendering in `portal/src/` and print the denominator.** The six treatments above came from three routes; the true count across twenty-six is unknown and is almost certainly higher (brief VII.11).

### ACCEPTANCE

<criterion id="RB10-AC1" cell_refs="RB-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB10-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB10-AC2" cell_refs="RB-s-10"><invocation>cd <WS> && timeout 120 python -c "import pathlib,re; pats=[r'No .{0,30} available',r'No .{0,30} data',r'Unable to load',r'Failed to load']; hits=0; fl=0; [ (hits:=hits+sum(len(re.findall(p,t)) for p in pats), fl:=fl+1) for t in [q.read_text(encoding='utf-8',errors='replace') for q in pathlib.Path('portal/src').rglob('*.tsx')] ]; print('RAW-STATE-STRINGS:',hits,'across',fl,'files'); print('VERDICT:','MIGRATED' if hits==0 else 'RAW-REMAIN')"</invocation><expect>VERDICT: MIGRATED</expect></criterion>
`RB10-AC2` -- every ad-hoc state string is gone from `portal/src` -- the four state components own them now. **At issuance this reads 143 across 263 files**, so the criterion measures the migration rather than confirming it.

<criterion id="RB10-AC3" cell_refs="RB-s-10"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-10_positioning_empty_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB10-AC3` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB10-AC4" cell_refs="RB-s-10"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-10_market_error_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB10-AC4` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB10-AC5" cell_refs="RB-s-10" judgment="true"/>
`RB10-AC5` -- graded at L9 from the renders and the census: every panel with nothing to show uses exactly ONE of the four states, the message says which in plain words, no message repeats itself, and no error is painted on the bare canvas. RECORD; NO VERDICT.

<expected_criteria>RB10-AC1, RB10-AC2, RB10-AC3, RB10-AC4, RB10-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- The duplicated error string is a MESSAGE-ASSEMBLY bug. Fixing the assembly is in scope; changing what the request does is not.

<paths>
portal/src/ui/
portal/src/components/
portal/src/pages/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-10`.
<owned_cells>RB-s-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB10-AC1` .. `RB10-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-10.four-states.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB10-AC1,RB10-AC2,RB10-AC3,RB10-AC4,RB10-AC5` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `four-states.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 10; fresh worktree pair branched from `feature/d13-visual-elevation`.
