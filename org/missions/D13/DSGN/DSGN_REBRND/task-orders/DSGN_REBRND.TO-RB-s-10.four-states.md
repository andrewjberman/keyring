# TO DSGN_REBRND.TO-RB-s-10 -- empty, loading, error and no-permission -- four designed states

> **AMENDMENT 1, 2026-09-14, issuer `2.0.0_SA_COO~D` -- ON ROW `DSGN_REBRND-W1-S32`: `RB10-AC2` IS RETIRED FOR `RB10-AC2R`.**
> Your migration took AC2 from 143 strings in 57 files to 1, and that 1 is a developer log line --
> `console.error('[TimeMachine] Failed to load restore points:', err)` at `src/context/TimeMachineProvider.tsx:42`. AC2's
> CLAIM is that every ad-hoc STATE string is gone; a string no user can see is not a state string, so AC2's domain (the
> whole text of every `.tsx`) was wider than its claim's population. The issuer's defect, not yours -- and editing a log
> message to turn a regex green would have been the wrong repair. `RB10-AC2R` runs the issuer's
> `task-orders/rb10-state-census.py`: the same four phrases over the same files, EXCLUDING lines that carry a `console.*`
> call and PRINTING every exclusion. Exercised before issue: the tree before this cell (portal `e216de95`) ->
> `RAW-REMAIN` (136 rendered strings in 55 files, 7 log lines excluded -- 143, your count); your tree (`a65b939a`) ->
> `MIGRATED` (1 excluded, the line above); your tree with one planted `<p>Failed to load holdings</p>` -> `RAW-REMAIN`
> naming it; an empty folder -> `NO-TREE`. **YOUR ACT: run `RB10-AC2R`, record it in the proof instance in place of
> `RB10-AC2`, re-validate with the id list in `<proof_of_spec>` below, commit, and flip complete.** Change no portal file.
> Row `W1-S33` (a state paints white inside a still-dark band) rides to L10 with row `S2`; it asks nothing of you.

<to_id>DSGN_REBRND.TO-RB-s-10</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-10` | **outcome_ref:** FWD-11 | **depends_on:** `RB-s-7` | **slot:** ~1, queue position 10

---

## WORKER FACE

### THE CELL

`RB-s-10` -- the four states.

**The defect, counted.** SIX distinct "nothing here" treatments across three routes: a centred grey sentence, a two-line grey sentence, a bordered red error, **a duplicated error string on the raw canvas**, an em-dash-filled table, and a panel that renders its header and then nothing.

**Four designed states, in the existing component set:** EMPTY, LOADING, ERROR, NO-PERMISSION. Every panel with nothing to show uses exactly one of them, and **the message says WHICH in plain words** -- "no holdings for this model" beats "No data available".

**⛔ No message repeats itself.** `/market` renders *"Failed to load market data: Failed to load market data: Error: Failed to fetch market returns from all available sources"*. That duplication is a real bug in the message assembly, not a styling problem.

**⛔ No error is painted on the bare canvas.** `portal/CLAUDE.md`'s existing colour law already says canvas-level notices are dark-on-light (`text-red-900` on `bg-red-500/10`), never `text-{color}-300`. The duplicated string violates the law the portal already has.

**AMENDED BY THE ISSUER at the RB-s-12 drain, on row `DSGN_REBRND-W3-S1`.**
`0.9.0_WK_DSGN_REBRND~3` measured that **NO-PERMISSION has no observable rendered state anywhere in
`portal/src`**: three route-level branches in `ProtectedRoute.tsx` (`requireAdmin` :39-40,
`requireInternal` :44-46, `isPathAllowedForFirm` :57-59) each `Navigate`-replace so the denied tree
never mounts; `AdvisorPublicProfile.tsx` :1201 and `useTradeSubmissionState.ts` omit an element
outright; `UploadPortfolioModal.tsx` :300 fires a transient `toast.error`. A case-insensitive
census over 468 files found no fourth mechanism.

**So the sentence above is not satisfiable as issued, and this is how it is scoped rather than
widened:**
- **BUILD all four components**, NO-PERMISSION included, so the state exists in the component set
  and the contract can name it.
- **MIGRATE only the three that have live instances** -- EMPTY, LOADING, ERROR. Those are the ones
  a panel can be observed in today.
- ⛔ **DO NOT re-route any access denial to render the new component.** Turning a silent redirect
  into a rendered state is INFORMATION ARCHITECTURE, which the PRD's NOT COMMISSIONED list excludes
  and which no cell of this project may take. **Leaving it unwired is the correct outcome, not a
  shortfall.**
- **Record the gap** in the result file, citing row `DSGN_REBRND-W3-S1`. It rides to L10 as a
  question for the CTO: whether NO-PERMISSION should become a rendered state at all is a product
  decision this project is not chartered to make.

`RB10-AC2`'s census below therefore covers the three migrated states; the NO-PERMISSION component
is graded by its existence and by the judgment criterion, never by a panel using it.

**Census every empty/loading/error/no-permission rendering in `portal/src/` and print the denominator.** The six treatments above came from three routes; the true count across twenty-six is unknown and is almost certainly higher (brief VII.11).

### ACCEPTANCE

<criterion id="RB10-AC1" cell_refs="RB-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB10-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB10-AC2" cell_refs="RB-s-10"><invocation>cd <WS> && timeout 120 python -c "import pathlib,re; pats=[r'No .{0,30} available',r'No .{0,30} data',r'Unable to load',r'Failed to load']; hits=0; fl=0; [ (hits:=hits+sum(len(re.findall(p,t)) for p in pats), fl:=fl+1) for t in [q.read_text(encoding='utf-8',errors='replace') for q in pathlib.Path('portal/src').rglob('*.tsx')] ]; print('RAW-STATE-STRINGS:',hits,'across',fl,'files'); print('VERDICT:','MIGRATED' if hits==0 else 'RAW-REMAIN')"</invocation><expect>VERDICT: MIGRATED</expect></criterion>
`RB10-AC2` -- every ad-hoc state string is gone from `portal/src` -- the four state components own them now. **At issuance this reads 143 across 263 files**, so the criterion measures the migration rather than confirming it. **RETIRED BY AMENDMENT 1 -- DO NOT RE-RUN IT; its domain counted unrendered log lines. Replaced by `RB10-AC2R`.**

<criterion id="RB10-AC2R" cell_refs="RB-s-10"><invocation>cd <WS> && timeout 120 python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb10-state-census.py</invocation><expect>VERDICT: MIGRATED</expect></criterion>
`RB10-AC2R` -- (AMENDMENT 1) every RENDERED ad-hoc state string is gone from `portal/src`; `console.*` log lines are excluded and each exclusion prints. An empty tree reads `NO-TREE`, never a pass.

<criterion id="RB10-AC3" cell_refs="RB-s-10"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-10_positioning_empty_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB10-AC3` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB10-AC4" cell_refs="RB-s-10"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-10_market_error_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB10-AC4` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB10-AC5" cell_refs="RB-s-10" judgment="true"/>
`RB10-AC5` -- graded at L9 from the renders and the census: every panel with nothing to show uses exactly ONE of the four states, the message says which in plain words, no message repeats itself, and no error is painted on the bare canvas. RECORD; NO VERDICT.

<expected_criteria>RB10-AC1, RB10-AC2R, RB10-AC3, RB10-AC4, RB10-AC5</expected_criteria>

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
org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb10-state-census.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-10`.
<owned_cells>RB-s-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids (AMENDMENT 1 -- the retired `RB10-AC2` is NOT an acceptance row): `RB10-AC1`, `RB10-AC2R`, `RB10-AC3`, `RB10-AC4`, `RB10-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-10.four-states.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB10-AC1,RB10-AC2R,RB10-AC3,RB10-AC4,RB10-AC5` BEFORE the `complete` flip.
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
