# TO DSGN_REBRND.TO-RB-s-5 -- accent rationing and ONE control vocabulary -- AND ANDREW'S IDENTITY ACCENTS

> **AMENDMENT 1, 2026-09-14, issuer `2.0.0_SA_COO~D`. THIS ORDER IS REOPENED: status is set back to pending and it is
> re-issued to `0.9.0_WK_DSGN_REBRND~2`. It is NOT re-cut.** The first round's work is merged and stands, including
> the one control vocabulary, weight-and-rule active states, chartreuse retired and `::selection` on the accent.
> Andrew then saw the build and widened the accent budget, in his own words:
> *"we've effectively wiped out the indigo accents. I'm not entirely against it, I like a lot of the changes that are
> happening but I'd like to make a concerted effort to keep selective indigo accents, like in the page title vertical
> bar and maybe the subtext"* -- and, on the favicon, *"We should have a similar look but its actually indigo sphere
> with white logo."*
> Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_150xZ_DSGN_REBRND_RESTORE_SELECTIVE_INDIGO_ACCENTS_AND_AN_INDIGO_FAVICON.md`
> @d54876b585 (on `CLOUD`).
> **Read THE AMENDED CELL below.** Where it and the original text disagree, the amendment wins and the original text
> is the defect. `RB5-AC5` is RETIRED and replaced by `RB5-AC5R`. `RB5-AC7` and `RB5-AC8` are new.
> **The checker `rb5-accent-check.py` was built by the issuer and is READ-ONLY to you.** The issuer exercised it on four
> trees before this amendment:
> - today's feature tree: `0 of 7`, `ACCENTS-INCOMPLETE`;
> - the pre-rebrand portal `787015e8`: `4 of 7` (sites 1, 2, 3 and 5 read RESTORED; site 4 lacks the white rule; no
>   indigo favicon);
> - a scratch tree with all seven restored: `7 of 7`, `ACCENTS-RESTORED`;
> - an empty tree: `0 of 7`, every site `NOT-FOUND`.
> So it can go green, it can go red, and it cannot pass on an empty sweep.

<to_id>DSGN_REBRND.TO-RB-s-5</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~2</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-5` | **outcome_ref:** FWD-4 | **depends_on:** `RB-s-1` | **slot:** ~2 (Amendment 1; the original round ran on ~1, queue position 5)

---

## WORKER FACE

### THE AMENDED CELL (AMENDMENT 1 -- READ THIS FIRST)

**The accent budget is now Andrew's:**
- ONE persistent primary ACTION per view, as before.
- PLUS identity accents at exactly **five named places**, and nowhere else.
- The focus ring and the `::selection` highlight stay transient, as before, and are not counted.

**The five identity sites.** Each lists where it is today at the feature head, then what it becomes. The accent token
is `hsl(var(--semantic-action-primary))`; the `--primary` alias resolves to it.

| # | site | file (today) | today | becomes |
|---|---|---|---|---|
| 1 | page-title vertical rule | `portal/src/components/PageHeaderVariants.tsx:38` | `bg-[hsl(var(--foreground))]` | `bg-[hsl(var(--semantic-action-primary))]` |
| 2 | page-header subtext (e.g. *"Daily news and market performance across..."* under MARKET OVERVIEW) | `PageHeaderVariants.tsx:50` | `text-[hsl(var(--foreground))]` | `text-[hsl(var(--semantic-action-primary))]` -- **the `<h1>` itself stays navy** |
| 3 | active tab, label AND 2px underline | `portal/src/components/TabNavigation.tsx:68-69` (active branch) | navy text + navy border | accent text + accent border, still `font-bold`; inactive tabs are unchanged |
| 4 | sidebar active item | `portal/src/App.tsx:188-189` (the `NavLink` active branch) | white bold + white left rule, no fill | accent FILL (`bg-[hsl(var(--semantic-action-primary))]`) **and KEEP** the white bold label and the `border-l-2` white left rule |
| 5 | user avatar circle | `App.tsx:382` | grey ring, no fill | accent FILL (`bg-[hsl(var(--semantic-action-primary))]`), white initial |

**Why site 4 keeps its white label and white rule.** The sidebar sits on the band (`App.tsx:256`, `--bg-header` =
`#0A1733`). An indigo fill against the band measures only **2.72:1**, so the fill alone cannot carry the active state
(WCAG SC 1.4.11). The white label on indigo measures **6.52:1**. The white left rule is what makes the state legible.

**What stays retired.**
- Toggle and segmented-control active fills. Their active state is weight and rule, and no option gets a filled accent
  chip. Andrew was asked this directly and chose NOT to restore them.
- Chartreuse. It stays out of the chrome.
- The canon lock on the duration ladder. It is untouched.

**THE FAVICON: an indigo sphere with the white mark.**
- Build a new SVG: a `#5F3BE3` circle filling its box, with the white mark's three paths centred on it at about 60% of
  the diameter. Take the paths from `portal/public/logos/opal-icon-white.svg`, which already exists (1,606 bytes).
- Build a matching **PNG at 180x180** for `apple-touch-icon`. Render the SVG with the same `playwright-core` + system
  Edge that `portal/scripts/ui-smoke.mjs` uses. A small script in your deliverables dir is enough, and no new
  dependency is needed.
- Re-point `portal/index.html:5` (`rel="icon"`) at the new SVG and `:6` (`rel="apple-touch-icon"`) at the new PNG.
- Leave the old `favicon.png` and `opal-icon-color.svg` in place; do not delete them.
- **⛔ Do NOT fetch anything from opalinvest.com.** That is egress and needs Andrew's per-use word. His description is
  the spec.
- READ your PNG, and the SVG rendered at 32px, before the flip.

**THE RULE IS WRITTEN IN SEVEN CARRIERS: UPDATE EVERY ONE, OR THE OTHERS KEEP STATING THE RETIRED RULE.**
1. **Contract clause C8** (`portal/DESIGN.md:350-355`). Replace the whole clause with this text, verbatim:
   > C8. **Accent -- one persistent primary action per view, plus the identity accents.** `palette.indigo` `#5F3BE3`
   > fills **exactly one** persistent ACTION per view: the primary action (a filled button, white label `#FFFFFF` at
   > 6.52:1). It also marks the product's IDENTITY in five named places and nowhere else (Andrew-direct 2026-09-14):
   > the page-title rule, the page-header subtext, the active tab's label and 2px underline, the sidebar's active
   > item (an indigo fill that keeps its white label and white left rule, so the state is never carried by the fill
   > alone -- SC 1.4.11), and the user avatar. It is also the focus ring (C11) and the text-selection highlight, which
   > are transient and do not count. It is not a chip fill, not a panel border, and the `<h1>` stays navy. A segmented
   > control or toggle never gets a filled purple chip per option; its active state is weight and rule. The band
   > carries no primary action (`#5F3BE3` on `#0A1733` measures 2.72:1).
2. `portal/DESIGN.md` `:7`, `:415` and `:421`: every other sentence in that file that restates the one-accent rule.
3. `portal/CLAUDE.md:53`.
4. `design/systems/portal/DESIGN_SYSTEM.md` `:64` and `:97`.
5. `.claude/skills/frontend-dev/SKILL.md:58`.
6. The code comments that cite the old C8: `PageHeaderVariants.tsx:34-37` and `:49`, `TabNavigation.tsx:64-67`, and
   `portal/src/ui/components/Controls.tsx:2,6`.

The line numbers are from the issuer's census at the feature head. Re-read each one. A carrier you find that is NOT
on this list is a surprise row, not a skip.

### THE CELL (original, round 1 -- still binding where the amendment does not change it)

`RB-s-5` -- accent rationing and one set of controls.

**The budget, by ROLE (CVO correction C2).** A view carries the accent on **exactly ONE PERSISTENT primary action**. The **transient** focus ring (RB-s-6) and the text-selection highlight **share the accent and are NOT counted against that one**. Measured on the live site, `#5F3BE3` never exceeds **1.0%** of visible surface on any page. *(AMENDMENT 1: plus the five identity sites above.)*

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
`RB5-AC4` -- chartreuse is gone from the stylesheet chrome. *(AMENDMENT 1: round 1 already drove this to `RETIRED`. It is re-run to show the amendment did not bring chartreuse back.)*

`RB5-AC5` -- **RETIRED BY AMENDMENT 1.** Do not record it. It graded a one-accent budget that Andrew has since
widened. It is replaced by `RB5-AC5R`.

<criterion id="RB5-AC5R" cell_refs="RB-s-5" judgment="true"/>
`RB5-AC5R` -- graded at L9 from the PNGs against ANDREW'S BUDGET (Amendment 1). Each route carries:
- the accent on exactly ONE persistent primary ACTION, enumerated in the result file;
- the identity accents at the five named sites AND NOWHERE ELSE, also enumerated.

Also graded:
- no tab, toggle or segmented control gives every option a filled accent chip;
- the sidebar's active item is legible with its fill ignored (white label and white left rule);
- the favicon reads as an indigo sphere with the white mark at 32px and on the 180px touch icon;
- no colour off the brand-derived palette is the loudest thing on any page.

RECORD; NO VERDICT.

<criterion id="RB5-AC6" cell_refs="RB-s-5" judgment="true"/>
`RB5-AC6` -- graded at L9 from the counterexample walk. With a primary visible, a secondary control focused and text
selected, the persistent ACTION count is still one. *(AMENDMENT 1: the five identity sites are not actions. List them
separately in the result file and do not count them here.)* RECORD; NO VERDICT.

<criterion id="RB5-AC7" cell_refs="RB-s-5"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-5r_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB5-AC7` -- **(AMENDMENT 1)** the `/market` route renders at 1440. It carries the page header, the subtext Andrew
named and the tab bar, so it is the render that shows sites 1-3, and 4-5 in the sidebar. READ the PNG before the flip.

<criterion id="RB5-AC8" cell_refs="RB-s-5"><invocation>cd <WS> && timeout 120 python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb5-accent-check.py</invocation><expect>VERDICT: ACCENTS-RESTORED</expect></criterion>
`RB5-AC8` -- **(AMENDMENT 1)** all seven sites are restored: the five identity accents, the favicon and the touch icon.
Each site prints its `file:line` and the class string or file it read. **At amendment this reads `0 of 7`.** Keep the
markup SHAPE the checker anchors on: the `w-[3px]` rule div, the `{description && (` paragraph, the `isActive ? '...'`
branches, and the avatar `rounded-full` div wrapping `{user?.name...}`. A site you had to restructure so that it reads
`NOT-FOUND` is a surprise row, not an edit to the checker.

<expected_criteria>RB5-AC1, RB5-AC2, RB5-AC3, RB5-AC4, RB5-AC5R, RB5-AC6, RB5-AC7, RB5-AC8</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- The transient ring is RB-s-6's to build; this cell must not double-define it.
- ⛔ **THE CANON LOCK** (Andrew-direct 2026-09-11, carried in the contract's clause C4): `UST #F97316 / ST #F59E0B / INT #10B981 / LT #3B82F6 / ULT #EF4444` are the ONLY locked colours and no act of this order may move them or their order. A five-hue segmented control that encodes the five duration models is the LADDER, not a defect -- its active state moves to weight and rule, its hues stay.
  *(Record note, issuer 2026-09-14, row `DSGN_REBRND-W1-S21`: this bullet was in the worker face at spawn and is landed on the record here after the fact, so the record reads what the worker received. The order was already complete; no criterion changes.)*
- ⛔ **(AMENDMENT 1) No egress.** Nothing is fetched from opalinvest.com or any other site.
- **(AMENDMENT 1) The checker is READ-ONLY.** Do not edit `rb5-accent-check.py` to make a criterion pass. A checker
  you had to edit is a finding, and findings are rows.

<paths>
portal/src/index.css
portal/src/ui/
portal/src/components/
portal/src/pages/
portal/src/App.tsx
portal/public/
portal/index.html
portal/DESIGN.md
portal/CLAUDE.md
design/systems/portal/DESIGN_SYSTEM.md
.claude/skills/frontend-dev/SKILL.md
org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb5-accent-check.py
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

> `rb5-accent-check.py` is an ISSUER artifact and READ-ONLY to you. It is named here because `<paths>` must cover
> every file the worker READS as well as every file it writes.

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-5`.
<owned_cells>RB-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids (AMENDMENT 1; this list matches `<expected_criteria>`, and the retired `RB5-AC5` is NOT an acceptance
row): `RB5-AC1`, `RB5-AC2`, `RB5-AC3`, `RB5-AC4`, `RB5-AC5R`, `RB5-AC6`, `RB5-AC7`, `RB5-AC8`.
**NEW instance** under your own serial, at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`). Round 1's instance under `~1` is the record of round 1;
do not touch it. Validate with
`python .tools/proof-of-spec-check.py <instance> RB5-AC1,RB5-AC2,RB5-AC3,RB5-AC4,RB5-AC5R,RB5-AC6,RB5-AC7,RB5-AC8`
BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `accent-controls.result.md` beside the new instance. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- 3 gates registered for this project (FWD-9's grade half, Andrew's; the brief's Appendix A prose defect; comp-adversary's false-GONE path parser). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: an AWS-surface token sweep returned 0 hits over the PRD's SURFACE MANIFEST and 0 over the whole PRD. No cell writes an AWS surface.
comp-adversary: RUN at L5 on the PRD -- 3 of 3 cited commits verified; 19 paths, 16 stable, 3 GONE all resolved (one is the register's own dangling D13 doc, one is `portal/DESIGN.md` correctly absent on CLOUD, one is a FALSE GONE from the tool's path parser). Blindness stated: its complement is filesystem adjacency, not the dependency chain.
lane: the `<paths>` block IS the grant (RULING 1). `design/` resolves UNDEFINED in `.owned-paths.yaml` for every agent -- a refusal there is a BLOCKING row, never an override.
amendment-1: FWD-4's DONE WHEN / ACCEPT text is `1.0.0_SA_CTO`'s to amend to Andrew's budget (relayed msg 96624). This reopen does not wait on that, because his word is the authority. The L4 notifier and the L4-R halves are not gated by a task-order MODIFICATION (to-pipeline-gate `_newly_added`), so the discipline of not cutting against a stale half is the issuer's, and it is discharged by the Andrew-direct record cited above.
</preflight>

Seating: round 1 on slot ~1, queue position 5. Amendment 1 on slot ~2, in a fresh worktree pair `C:/tmp/wk-dsgn-2c` branched from `feature/d13-visual-elevation` in both repos, port 5193.
