# TO DSGN_REBRND.TO-RB-s-1 -- the token spine -- ONE writer, the measured values, two disjoint colour families

<to_id>DSGN_REBRND.TO-RB-s-1</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-1` | **outcome_ref:** FWD-1, FWD-6, FWD-7 | **depends_on:** -- (chain head) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`RB-s-1` -- the token spine. **Merges PRD candidates R1 and R8**, because both PRODUCE `DesignTokens` into the same sole-writer file and one remedy moves both.

**The one writer.** `portal/design/brands/opal-capital.json` is the ONLY place a token VALUE is written; `portal/design/themes/opal-capital.css` is GENERATED from it (wired live at `portal/src/main.tsx:7`). `portal/src/index.css` `:root` may CONSUME a token and must never REDEFINE a value the JSON carries.

**The measured values**, from `design/brand/opalinvest.com.json` (3 pages, [3/3] agreement, 1440x900, 2026-09-11):
canvas `#F4F6FA` -- dark field `#0A1733` (inverted bands ONLY, never a card) -- navy `#163372` as TEXT AND HAIRLINE, never a container fill -- accent `#5F3BE3` -- radii `2px`/`3px`/`4px` plus pill `720px` and `50%`, **no mid-range radius** -- **no drop shadow**; the focus ring is the only `box-shadow`.

**The two disjoint colour families (R8).** Build `--status-*` (success/danger/warning/info) brand-derived, and `--data-*` carrying the chroma the charts have TODAY. Delete the aliasing at `portal/src/index.css:111-115` (`--chart-1..5` currently resolve onto the Argon status set at `:40-43`). `portal/src/lib/modelPortfolioColors.ts` is an existing DATA palette -- REUSE it, do not replace it. **Andrew's constraint binds here: the charts keep their colour. What goes quiet is the chrome.**

**Delete** `portal/tailwind.config.js`: dead under Tailwind v4.2.1 (no `@config` directive in `src/index.css`), and `primary-500`/`secondary-400` appear in **0** source files. It is cleanup and it is NOT causal -- do not attribute any behaviour change to it.

**The dark theme survives** as the user-selectable toggle, with its own values in the same JSON (brief V.3). It is a choice a user makes, never the residue of a declaration.

### ACCEPTANCE

<criterion id="RB1-AC1" cell_refs="RB-s-1"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB1-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB1-AC2" cell_refs="RB-s-1"><invocation>cd <WS> && timeout 120 python -c "import io,re; s=io.open('portal/src/index.css',encoding='utf-8').read(); lit=re.findall(r'--[a-z0-9-]+\\s*:\\s*(?:#[0-9a-fA-F]{3,8}|[0-9.]+\\s+[0-9.]+%\\s+[0-9.]+%)\\s*;',s); print('LITERAL-COLOUR-DEFS:',len(lit)); print('VERDICT:','ONE-WRITER' if len(lit)==0 else 'MULTI-WRITER')"</invocation><expect>VERDICT: ONE-WRITER</expect></criterion>
`RB1-AC2` -- ZERO literal colour definitions survive in `index.css` -- every value is consumed from the generated theme, so the JSON is the ONE writer. The count prints beside the verdict; **at issuance this reads 60+, so the criterion detects the defect rather than confirming it.**

<criterion id="RB1-AC3" cell_refs="RB-s-1"><invocation>cd <WS>/portal && timeout 120 sh -c 'test -e tailwind.config.js; echo exists=$?'</invocation><expect>exists=1</expect></criterion>
`RB1-AC3` -- the dead Tailwind config is DELETED, not left in place.

<criterion id="RB1-AC4" cell_refs="RB-s-1"><invocation>cd <WS> && timeout 120 python -c "import io; s=io.open('portal/design/themes/opal-capital.css',encoding='utf-8').read().lower(); need=['#f4f6fa','#0a1733','#163372','#5f3be3']; miss=[k for k in need if k not in s]; print('REQUIRED:',need,'MISSING:',miss); print('VERDICT:','ALL-PRESENT' if not miss else 'MISSING-VALUES')"</invocation><expect>VERDICT: ALL-PRESENT</expect></criterion>
`RB1-AC4` -- the generated theme carries ALL FOUR measured brand values. One verdict over the whole set, so a hit on one value cannot satisfy the criterion.

<criterion id="RB1-AC5" cell_refs="RB-s-1"><invocation>cd <WS> && timeout 120 python -c "import io,re; s=io.open('portal/src/index.css',encoding='utf-8').read(); m=re.findall(r'--chart-[1-5]\\s*:\\s*var\\(--(success|danger|warning|info|primary)\\)',s); print('STATUS-ALIASED-CHART-TOKENS:',len(m),m); print('VERDICT:','DISJOINT' if len(m)==0 else 'ALIASED')"</invocation><expect>VERDICT: DISJOINT</expect></criterion>
`RB1-AC5` -- no chart token resolves onto a status token -- the two families are disjoint. **At issuance this reads 5.**

<criterion id="RB1-AC6" cell_refs="RB-s-1" judgment="true"/>
`RB1-AC6` -- graded at L9 from the JSON and the generated CSS: the dark theme is a complete, selectable alternative with its own values in the same file, not a residue. RECORD; NO VERDICT.

<expected_criteria>RB1-AC1, RB1-AC2, RB1-AC3, RB1-AC4, RB1-AC5, RB1-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **This cell is the chain head.** Every colour cell after it consumes what it writes. Do not restyle a component here; that is RB-s-3/4/5.

<paths>
portal/design/brands/opal-capital.json
portal/design/themes/opal-capital.css
portal/design/tokens/
portal/src/index.css
portal/src/main.tsx
portal/tailwind.config.js
portal/src/lib/modelPortfolioColors.ts
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-1`.
<owned_cells>RB-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB1-AC1` .. `RB1-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-1.token-spine.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB1-AC1,RB1-AC2,RB1-AC3,RB1-AC4,RB1-AC5,RB1-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `token-spine.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 1; fresh worktree pair branched from `feature/d13-visual-elevation`.
