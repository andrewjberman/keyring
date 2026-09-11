# TO DSGN_REBRND.TO-RB-s-8 -- the archetype rewrites and the review loop's clause-cite step

<to_id>DSGN_REBRND.TO-RB-s-8</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-8` | **outcome_ref:** FWD-6 | **depends_on:** `RB-s-7` | **slot:** ~1, queue position 8

---

## WORKER FACE

### THE CELL

`RB-s-8` -- the standing-law rewrites. **PRD candidate R7 split, part 2.**

**⚠ THIS CELL SUPERSEDES LAW THAT OTHER PROJECTS READ.** `IRPT_FNTEND` is a named consumer. Rewrite IN PLACE; **never leave a second archetype standing beside the old one** -- that is the shadow-system failure and it is banned.

**The four files, all carrying the superseded 2026-07-15 archetype** ("light SILVER canvas `#C3CADA`, dark navy containers floating on it"):
- `design/brand/COLOR_ARCHETYPES.md`
- `design/systems/portal/DESIGN_SYSTEM.md`
- `design/process/UI_VERIFICATION.md`
- `portal/CLAUDE.md` -- the "Color law" section

They are rewritten onto the light-canvas contract RB-s-7 ratified. **Andrew's 2026-09-11 ruling supersedes the 2026-07-15 archetype**; say so in each file, with the date, so a later reader knows which way the supersession runs.

**⛔ THESE FILES ARE `NOT-EVALUATED` IN THE DECOMPOSITION.** This seat never opened their bodies. **Census them first and print what you find** -- the rewrite is not a blind find-and-replace, and if a file turns out not to carry the archetype at all, that is a surprise row.

**The verification loop gains a CLAUSE-CITE STEP.** `design/process/UI_VERIFICATION.md` and `.claude/skills/frontend-dev/SKILL.md` keep their render-LOOK-then-commit rule BY NAME (brief IV.7: the estate already has the pattern; do not invent a second mechanism) and gain one step: a review that rejects a page cites the contract clause NUMBER. `portal/scripts/ui-smoke.mjs` keeps printing the resolved canvas.

### ACCEPTANCE

<criterion id="RB8-AC1" cell_refs="RB-s-8"><invocation>cd <WS> && timeout 120 python -c "import io; fs=['design/brand/COLOR_ARCHETYPES.md','design/systems/portal/DESIGN_SYSTEM.md','design/process/UI_VERIFICATION.md','portal/CLAUDE.md']; hits={p: io.open(p,encoding='utf-8',errors='replace').read().upper().count('C3CADA') for p in fs}; tot=sum(hits.values()); print('PER-FILE:',hits,'TOTAL:',tot); print('VERDICT:','SUPERSEDED' if tot==0 else 'ARCHETYPE-SURVIVES')"</invocation><expect>VERDICT: SUPERSEDED</expect></criterion>
`RB8-AC1` -- the superseded silver-canvas value is gone from ALL FOUR law files, judged on a single TOTAL. **The per-file form of this check was a false pass: `C3CADA-HITS: 0` from one file satisfied the match while another file still carried a hit.**

<criterion id="RB8-AC2" cell_refs="RB-s-8"><invocation>cd <WS> && timeout 120 python -c "import io; fs=['design/brand/COLOR_ARCHETYPES.md','design/systems/portal/DESIGN_SYSTEM.md','portal/CLAUDE.md']; hits={p: io.open(p,encoding='utf-8',errors='replace').read().upper().count('F4F6FA') for p in fs}; missing=[p for p,n in hits.items() if n==0]; print('PER-FILE:',hits,'MISSING:',missing); print('VERDICT:','ALL-STATE-CANVAS' if not missing else 'INCOMPLETE')"</invocation><expect>VERDICT: ALL-STATE-CANVAS</expect></criterion>
`RB8-AC2` -- EVERY rewritten law file states the light canvas. The verdict is driven by the MISSING list, so one file carrying it cannot cover for another that does not.

<criterion id="RB8-AC3" cell_refs="RB-s-8"><invocation>cd <WS> && timeout 120 python -c "import io; s=io.open('design/process/UI_VERIFICATION.md',encoding='utf-8',errors='replace').read().lower(); cc='clause' in s; rr=('screenshot' in s) or ('render' in s); print('CLAUSE-CITE:',cc,'RENDER-RULE-KEPT:',rr); print('VERDICT:','BOTH' if (cc and rr) else 'MISSING-ONE')"</invocation><expect>VERDICT: BOTH</expect></criterion>
`RB8-AC3` -- the clause-cite step is added AND the incumbent render rule is retained by name. **The two-line form was a false pass: `True` matched the second line while the first read False.**

<criterion id="RB8-AC4" cell_refs="RB-s-8"><invocation>cd <WS> && timeout 120 python -c "import pathlib; ds=sorted(str(p) for p in pathlib.Path('design').rglob('*ARCHETYPE*')); print('ARCHETYPE-DOCS:',len(ds),ds); print('VERDICT:','SINGLE-ARCHETYPE' if len(ds)==1 else 'FORKED')"</invocation><expect>VERDICT: SINGLE-ARCHETYPE</expect></criterion>
`RB8-AC4` -- exactly ONE archetype document exists -- no second archetype was created beside the old one. This is a NO-REGRESSION guard: it holds at issuance and must still hold after, which is the point.

<criterion id="RB8-AC5" cell_refs="RB-s-8" judgment="true"/>
`RB8-AC5` -- graded at L9: each rewritten file states the supersession with its date and direction, and a reader of any one of them cannot come away with the 2026-07-15 law. RECORD; NO VERDICT.

<expected_criteria>RB8-AC1, RB8-AC2, RB8-AC3, RB8-AC4, RB8-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- ⛔ **`design/` resolves UNDEFINED in `.owned-paths.yaml`** -- no path rule matches it for any agent. Your `<paths>` block IS your grant under RULING 1, so the write is admitted; if a lane check still refuses, that is a BLOCKING surprise row, never an override.
- `ui-smoke.mjs` must still print the resolved canvas after your edit. That print is load-bearing for six other cells.

<paths>
design/brand/COLOR_ARCHETYPES.md
design/systems/portal/DESIGN_SYSTEM.md
design/process/UI_VERIFICATION.md
portal/CLAUDE.md
.claude/skills/frontend-dev/SKILL.md
portal/scripts/ui-smoke.mjs
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-8`.
<owned_cells>RB-s-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB8-AC1` .. `RB8-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-8.archetype-rewrites.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB8-AC1,RB8-AC2,RB8-AC3,RB8-AC4,RB8-AC5` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `archetype-rewrites.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 8; fresh worktree pair branched from `feature/d13-visual-elevation`.
