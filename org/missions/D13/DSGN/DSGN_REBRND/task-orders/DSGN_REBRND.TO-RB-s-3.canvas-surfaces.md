# TO DSGN_REBRND.TO-RB-s-3 -- canvas and surfaces -- light canvas, navy as ink, bands enumerated, nesting collapsed

<to_id>DSGN_REBRND.TO-RB-s-3</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-3` | **outcome_ref:** FWD-1, FWD-10 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 3

---

## WORKER FACE

### THE CELL

`RB-s-3` -- canvas and surfaces. **This is the cell that resolves the product's core contradiction: today it is a dark-mode dashboard placed on a light-mode page.**

**The canvas becomes `#F4F6FA`.** `portal/src/index.css:52` currently sets `--bg-page` to the mid-silver `#C3CADA`. A field either recedes far enough to disappear or inverts far enough to frame; `#C3CADA` at 81% lightness does neither, which is why panels on it read as stickers.

**Navy stops being a background.** On the live site `#163372` holds **0.2-0.4%** of visible surface -- it is a text and hairline colour. Using it as a panel fill is what forces every other colour on the page to shout.

**Collapse the nesting.** Every rendered route is three rounded containers deep, each a different navy (`--bg-header` / `--bg-medium` / `--bg-card`). Two states only: on the canvas, or an inverted `#0A1733` band. Where a container must be distinguished on the canvas use a `1px #C4CBDB` hairline and a `#FFFFFF` surface -- **never a shadow and never a fourth navy**.

**Every dark band is ENUMERATED with its reason** in the result file. A band that cannot state why it is inverted is not a band.

**Radii 6-8px become 2/3/4px.** `--radius: 0.5rem` is the current uniform value; the live site has no mid-range radius at all.

**`color-scheme` follows the canvas.** `:132` sets `color-scheme: dark` on a light page, which is what renders the unstyled native `<select>` with an OS chevron on `/portfolio-management`. Style every native control.

**Grade the DEFAULT LIGHT MODE, and exercise the retained dark toggle** light -> dark -> light (CVO correction C5). Contrast is computed for text-on-canvas, text-on-band AND in the selected dark mode, against **WCAG 2.1 SC 1.4.3 / 1.4.11** as CONTRACTS pins it -- the brief computed none (VII.4).

**AMENDED BY THE ISSUER on Andrew's word, 2026-09-11 ~13:4xZ, VERBATIM: "Yes fetch lato".**

RB-s-2 shipped Lato 400 and 600 and served `font-weight: 700` from the **SemiBold**, because the
700 face was not on this box (row `DSGN_REBRND-W1-S8`). **It is now.** The CTO performed the one
authorized fetch on Andrew's word; this lane verified the bytes before handing them to you.

`.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/Lato-Bold.ttf` is **already staged
in your worktree** (`.runtime/` is gitignored and absent from fresh worktrees, so a path grant alone
would have pointed at nothing — that trap already cost you one cycle).

| | |
|---|---|
| sha256 | `8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1` |
| name table | family `Lato`, subfamily `Bold`, full `Lato Bold` |
| OS/2 | `usWeightClass` **700**, `fsType` 0, 3023 glyphs (same count as the 400 and 600 you shipped) |

**DO THIS, and it is small:**
1. Convert or copy the Bold into `portal/public/fonts/` the same way you did the others, and
   **record its sha256** in `public/fonts/README.md` beside the existing two.
2. Point the `@font-face` rule for `font-weight: 700` at the **real 700 face**, not the 600.
3. **Delete the substitution line** from `public/fonts/README.md`. It is no longer true, and a
   README that describes a retired workaround is worse than one that says nothing.
4. Keep the 600 face if a `font-weight: 600` rule uses it; drop it if nothing references it. Say
   which, and why, in the result file.

⛔ **NO FETCH. NO NETWORK.** Andrew's word authorized exactly one egress act and the CTO already
performed it. Nothing in this cell may reach off this box.

⚠ **`portal/public/fonts/` is added to your `<paths>` for this.** Row `DSGN_REBRND-W1-S8` is
SUPERSEDED by Andrew's ruling, not deleted — the channel is append-only; note the supersession in
your result file rather than editing the row.

⛔ **AND A HOLD YOU MUST NOT STEP OVER.** The same ruling says **"wait on DEV"**. Portal `DEV` is
held. Nothing in this cell promotes, merges toward, or bumps a gitlink into `DEV` — your branch is
`wk-dsgn_rebrnd-1d` off `feature/d13-visual-elevation` and it stays there.

### ACCEPTANCE

<criterion id="RB3-AC1" cell_refs="RB-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB3-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB3-AC2" cell_refs="RB-s-3"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-3_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB3-AC2` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB3-AC3" cell_refs="RB-s-3"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs positioning <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-3_positioning_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB3-AC3` -- the `/positioning` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB3-AC4" cell_refs="RB-s-3"><invocation>cd <WS> && timeout 120 python -c "import io,re; s=io.open('portal/src/index.css',encoding='utf-8').read(); m=re.search(r'color-scheme:\\s*(\\w+)',s); v=m.group(1) if m else 'ABSENT'; print('COLOR-SCHEME:',v); print('VERDICT:','FOLLOWS-CANVAS' if v=='light' else 'CONTRADICTS-CANVAS')"</invocation><expect>VERDICT: FOLLOWS-CANVAS</expect></criterion>
`RB3-AC4` -- `color-scheme` follows the light canvas instead of contradicting it. **At issuance this reads `dark` on a light page**, which is what renders the unstyled native `<select>`.

<criterion id="RB3-AC5" cell_refs="RB-s-3"><invocation>cd <WS> && timeout 120 python -c "import io,re; s=io.open('portal/src/index.css',encoding='utf-8').read(); r=[x.strip() for x in re.findall(r'--radius[^:]*:\\s*([^;]+);',s)]; bad=[x for x in r if not re.match(r'^(0|0px|[1-4]px|720px|50%|9999px)$',x)]; print('RADII:',r,'OFF-BAND:',bad); print('VERDICT:','SHARP' if (r and not bad) else 'MID-RANGE')"</invocation><expect>VERDICT: SHARP</expect></criterion>
`RB3-AC5` -- every radius token sits in the 2/3/4px band (or a pill/circle). **At issuance this reads `['0.5rem']` -> MID-RANGE**, so the criterion fails today and can only pass once the work lands.

<criterion id="RB3-AC6" cell_refs="RB-s-3" judgment="true"/>
`RB3-AC6` -- graded at L9 from the PNGs: the canvas reads as one near-white field, navy appears as ink and never as a container fill, no route nests more than one visible container, no native unstyled control renders, and every dark band is on the enumerated list with its reason. RECORD; NO VERDICT.

<criterion id="RB3-AC7" cell_refs="RB-s-3" judgment="true"/>
`RB3-AC7` -- graded at L9 from the contrast table in the result file: every text/background pair on the canvas, on the inverted bands AND in the selected dark mode meets WCAG 2.1 SC 1.4.3 / 1.4.11, denominator printed. RECORD; NO VERDICT.

<expected_criteria>RB3-AC1, RB3-AC2, RB3-AC3, RB3-AC4, RB3-AC5, RB3-AC6, RB3-AC7</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Information architecture is OUT OF SCOPE.** Which panels exist and what they show does not change. You are changing how a surface looks, never what it is for.
- The `ui-smoke.mjs` script prints the resolved canvas; that printed value is the evidence, not your reading of the CSS.

<paths>
portal/src/index.css
portal/public/fonts/
.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/
portal/src/ui/components/panels/
portal/src/ui/
portal/src/components/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-3`.
<owned_cells>RB-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB3-AC1` .. `RB3-AC7`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB3-AC1,RB3-AC2,RB3-AC3,RB3-AC4,RB3-AC5,RB3-AC6,RB3-AC7` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `canvas-surfaces.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 3; fresh worktree pair branched from `feature/d13-visual-elevation`.
