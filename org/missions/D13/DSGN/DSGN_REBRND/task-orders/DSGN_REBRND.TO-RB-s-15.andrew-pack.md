# TO DSGN_REBRND.TO-RB-s-15 -- Andrew's side-by-side pack

<to_id>DSGN_REBRND.TO-RB-s-15</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-15` | **outcome_ref:** FWD-9 | **depends_on:** `RB-s-14` | **slot:** ~1, queue position 12

---

## WORKER FACE

### THE CELL

`RB-s-15` -- the pack. **PRD candidate R13.**

**Build a one-page pack** for Andrew to put on screen beside a competitor **HE** chooses: the three routes rendered after RB-s-1..RB-s-13, with the BEFORE renders beside them.

**The before renders already exist** and must be used rather than re-derived: they were captured 2026-09-11 at 1440x900 against the dev server and read into the brief's IV.9. Re-render the AFTER set at the same width, same routes, same fixtures.

**⛔ NO COMPETITOR SITE IS CAPTURED.** The brief's comparator set (§IV.11 -- Addepar, Canoe, Orion, Bloomberg, Koyfin, YCharts) is **NOT MEASURED**; it was named from category knowledge and the brief says so at VII.10. Capturing one is EGRESS and needs Andrew's per-use word, which this order does not carry and does not assume.

**⛔ FWD-9's GRADE IS ANDREW'S AND IS NOT YOURS, NOT THE CVO'S AND NOT THE CTO'S.** A REALIZED on FWD-1..8, 10 and 11 does **not** substitute for it. This order produces the artifact and stops. The pack existing is the on-demand half; his word is the other half and it is registered as an open gate in the decomposition's battery (§6).

### ACCEPTANCE

<criterion id="RB15-AC1" cell_refs="RB-s-15"><invocation>cd <WS> && timeout 120 python -c "import pathlib; d=pathlib.Path('org/missions/D13/DSGN/DSGN_REBRND/deliverables'); ps=([str(p) for p in d.rglob('*fwd9*')] + [str(p) for p in d.rglob('*pack*')]) if d.exists() else []; print('PACK-ARTIFACTS:',len(ps),ps[:6]); print('VERDICT:','PACK-PRESENT' if len(ps)>0 else 'ABSENT')"</invocation><expect>VERDICT: PACK-PRESENT</expect></criterion>
`RB15-AC1` -- the pack artifacts exist in the deliverables -- a NON-ZERO count, so an empty deliverables directory cannot pass vacuously. **At issuance this reads 0.**

<criterion id="RB15-AC2" cell_refs="RB-s-15"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-15_market_after_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB15-AC2` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB15-AC3" cell_refs="RB-s-15"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-15_positioning_after_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB15-AC3` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB15-AC4" cell_refs="RB-s-15"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs portfolio-management <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-15_pm_after_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB15-AC4` -- the `/portfolio-management` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB15-AC5" cell_refs="RB-s-15" judgment="true"/>
`RB15-AC5` -- graded at L9: the pack pairs each AFTER render with its BEFORE at the same route, width and fixtures, and is in a form Andrew can put on screen beside a competitor he chooses. The GRADE OF FWD-9 ITSELF IS ANDREW'S and is recorded verbatim when he gives it. RECORD; NO VERDICT.

<expected_criteria>RB15-AC1, RB15-AC2, RB15-AC3, RB15-AC4, RB15-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **Do not capture any competitor site.** Egress; needs Andrew's per-use word.
- ⛔ **Do not grade FWD-9.** Produce the pack and stop.

<paths>
org/missions/D13/DSGN/DSGN_REBRND/deliverables/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-15`.
<owned_cells>RB-s-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB15-AC1` .. `RB15-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-15.andrew-pack.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB15-AC1,RB15-AC2,RB15-AC3,RB15-AC4,RB15-AC5` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `andrew-pack.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 12; fresh worktree pair branched from `feature/d13-visual-elevation`.
